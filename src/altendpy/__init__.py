import altendpy._version
__version__ = altendpy._version.get_versions()['version']

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
