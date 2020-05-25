# -*- coding: utf-8 -*-

import os

if os.environ.get('QGIS_PLUGIN_USE_DEBUGGER') == 'ptvsd':
    try:
        import ptvsd
        if ptvsd.is_attached():
            print('ptvsd debugging already active')
        else:
            ptvsd.enable_attach(address=('localhost', 5678))
    except Exception as e:
        print('Unable to use ptvsd debugger', e)


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load QgisPluginBase class from file QgisPluginBase.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .plugin_base import QgisPluginBase
    return QgisPluginBase(iface)
