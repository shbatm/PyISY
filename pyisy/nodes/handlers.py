"""Node Event Handler Classes."""

from ..constants import TAG_CATEGORY, TAG_GENERIC, TAG_MFG
from ..helpers import value_from_xml


class EventEmitter:
    """Event Emitter class."""

    def __init__(self):
        """Initialize a new Event Emitter class."""
        self._subscribers = []

    def subscribe(self, callback):
        """Subscribe to the events."""
        listener = EventListener(self, callback)
        self._subscribers.append(listener)
        return listener

    def unsubscribe(self, listener):
        """Unsubscribe from the events."""
        self._subscribers.remove(listener)

    def notify(self, event):
        """Notify a listener."""
        for subscriber in self._subscribers:
            subscriber.callback(event)


class EventListener:
    """Event Listener class."""

    def __init__(self, emitter, callback):
        """Initialize a new Event Listener class."""
        self._emitter = emitter
        self.callback = callback

    def unsubscribe(self):
        """Unsubscribe from the events."""
        self._emitter.unsubscribe(self)


class ZWaveProperties(dict):
    """Class to hold Z-Wave Product Details from a Z-Wave Node."""

    def __init__(self, xml=None):
        """Initialize an control result or aux property."""
        self._category = None
        self._devtype_mfg = None
        self._devtype_gen = None
        self._raw = ""
        self._basic_type = 0
        self._generic_type = 0
        self._specific_type = 0
        self._mfr_id = 0
        self._prod_type_id = 0
        self._product_id = 0

        if xml:
            self._category = value_from_xml(xml, TAG_CATEGORY)
            self._devtype_mfg = value_from_xml(xml, TAG_MFG)
            self._devtype_gen = value_from_xml(xml, TAG_GENERIC)
            self._raw = xml.toxml()
        if self._devtype_gen:
            (
                self._basic_type,
                self._generic_type,
                self._specific_type,
            ) = self._devtype_gen.split(".")
        if self._devtype_mfg:
            (
                self._mfr_id,
                self._prod_type_id,
                self._product_id,
            ) = self._devtype_mfg.split(".")

        super().__init__(
            self,
            category=self._category,
            devtype_mfg=self._devtype_mfg,
            devtype_gen=self._devtype_gen,
            basic_type=self._basic_type,
            generic_type=self._generic_type,
            specific_type=self._specific_type,
            mfr_id=self._mfr_id,
            prod_type_id=self._prod_type_id,
            product_id=self._product_id,
        )

    @property
    def category(self):
        """Return the ISY Z-Wave Category Property."""
        return self._category

    @property
    def devtype_mfg(self):
        """Return the Full Devtype Mfg Z-Wave Property String."""
        return self._devtype_mfg

    @property
    def devtype_gen(self):
        """Return the Full Devtype Generic Z-Wave Property String."""
        return self._devtype_gen

    @property
    def basic_type(self):
        """Return the Z-Wave basic type Property."""
        return self._basic_type

    @property
    def generic_type(self):
        """Return the Z-Wave generic type Property."""
        return self._generic_type

    @property
    def specific_type(self):
        """Return the Z-Wave specific type Property."""
        return self._specific_type

    @property
    def mfr_id(self):
        """Return the Z-Wave Manufacterer ID Property."""
        return self._mfr_id

    @property
    def prod_type_id(self):
        """Return the Z-Wave Product Type ID Property."""
        return self._prod_type_id

    @property
    def product_id(self):
        """Return the Z-Wave Product ID Property."""
        return self._product_id

    def __str__(self):
        """Return just the original raw xml string from the ISY."""
        return self._raw

    __repr__ = f"ZWaveProperties({__str__})"

    def __getattr__(self, name):
        """Retrieve the properties."""
        return self[name]

    def __setattr__(self, name, value):
        """Allow setting of properties."""
        self[name] = value
