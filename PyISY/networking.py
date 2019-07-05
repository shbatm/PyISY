"""ISY Network Resources Module."""
from time import sleep
from xml.dom import minidom

from .constants import ATTR_ID, ATTR_NAME, THREAD_SLEEP_TIME, XML_PARSE_ERROR
from .helpers import value_from_xml


class NetworkResources:
    """
    Network Resources class cobject.

    DESCRIPTION:
        This class handles the ISY networking module.

    USAGE:
        This object may be used in a similar way as a
        dictionary with the either networking command
        names or ids being used as keys and the ISY
        networking command class will be returned.

    EXAMPLE:
        >>> a = networking['test function']
        >>> a.run()

    ATTRIBUTES:
        isy: The ISY device class
        nids: List of net command ids
        nnames: List of net command names
        nobjs: List of net command objects

    """

    nids = []
    nnames = []
    nobjs = []

    def __init__(self, isy, xml=None):
        """
        Initialize the network resources class.

        isy: ISY class
        xml: String of xml data containing the configuration data
        """
        self.isy = isy

        if xml is not None:
            self.parse(xml)

    def parse(self, xml):
        """
        Parse the xml data.

        xml: String of the xml data
        """
        try:
            xmldoc = minidom.parseString(xml)
        except:
            self.isy.log.error("%s: NetworkResources", XML_PARSE_ERROR)
        else:
            features = xmldoc.getElementsByTagName('NetRule')
            for feature in features:
                nid = int(value_from_xml(feature, ATTR_ID))
                if nid not in self.nids:
                    nname = value_from_xml(feature, ATTR_NAME)
                    nobj = NetworkCommand(self, nid)
                    self.nids.append(nid)
                    self.nnames.append(nname)
                    self.nobjs.append(nobj)

            self.isy.log.info('ISY Loaded Network Resources Commands')

    def update(self, wait_time=0):
        """
        Update the contents of the networking class.

        wait_time: [optional] Amount of seconds to wait before updating
        """
        sleep(wait_time)
        xml = self.isy.conn.get_network()
        self.parse(xml)

    def updateThread(self):
        """
        Continually update the class until it is told to stop.

        Should be run in a thread.
        """
        while self.isy.auto_update:
            self.update(THREAD_SLEEP_TIME)

    def __getitem__(self, val):
        """Return the item from the collection."""
        try:
            val = int(val)
            return self.get_by_id(val)
        except:
            return self.get_by_name(val)

    def __setitem__(self, val, value):
        """Set the item value."""
        return None

    def get_by_id(self, val):
        """
        Return command object being given a command id.

        val: Integer representing command id
        """
        try:
            ind = self.nids.index(val)
            return self.get_by_index(ind)
        except:
            return None

    def get_by_name(self, val):
        """
        Return command object being given a command name.

        val: String representing command name
        """
        try:
            ind = self.nnames.index(val)
            return self.get_by_index(ind)
        except:
            return None

    def get_by_index(self, val):
        """
        Return command object being given a command index.

        val: Integer representing command index in List
        """
        return self.nobjs[val]


class NetworkCommand:
    """
    Network Command Class.

    DESCRIPTION:
        This class handles individual networking commands.

    ATTRIBUTES:
        network_resources: The networkin resources class

    """

    def __init__(self, network_resources, rid):
        """Initialize network command class.

        network_resources: NetworkResources class
        rid: Integer of the command id
        """
        self._network_resources = network_resources
        self.isy = network_resources.isy
        self._id = rid

    @property
    def rid(self):
        """Return the Resource ID for the Network Resource."""
        return self._id

    def run(self):
        """Execute the networking command."""
        req_url = self.isy.conn.compile_url(['networking', 'resources',
                                             str(self._id)])

        if not self.isy.conn.request(req_url, ok404=True):
            self.isy.log.warning('ISY could not run networking command: %s',
                                 str(self._id))
            return
        self.isy.log.info('ISY ran networking command: %s', str(self._id))
