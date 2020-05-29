from PyQt5.QtCore import QCoreApplication

# noinspection PyMethodMayBeStatic
def tr(message):
    """Get the translation for a string using Qt translation API.

    :param context: Context of the translation e.g. class name etc.
    :param message: String for translation.

    :returns: Translated version of message.
    :rtype: QString
    """
    # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
    return QCoreApplication.translate('translation', message)
