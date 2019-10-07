import pathlib

from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="PyISY_beta",
    version_format='{tag}.dev{commitcount}',  # Dev Versions -{gitsha}
    # version_format='{tag}',  # Release Version
    license='Apache License 2.0',
    url='http://automic.us/projects/pyisy',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Ryan Kraus',
    author_email='automicus@gmail.com',
    description='Python module to talk to ISY994 from UDI.',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    setup_requires=['setuptools-git-version'],
    install_requires=['requests', 'VarEvents'],
    keywords=['home automation', 'isy', 'isy994', 'isy-994', 'UDI'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
