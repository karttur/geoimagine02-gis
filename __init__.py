"""
Postgres connection for karttur Geo Imagine Framework

Author
______
Thomas Gumbricht
"""

from .version import __version__, VERSION, metadataD

from .kt_gis import MjProj, GetVectorProjection, GetRasterMetaData, Geometry, ESRIOpenGetLayer

__all__ = ['MjProj','GetVectorProjection','GetRasterMetaData','Geometry','ESRIOpenGetLayer']