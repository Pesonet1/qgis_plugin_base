def pushWarningMessage(message):
    iface.messageBar().pushMessage('PROJECT X', message, level = Qgis.Warning, duration = 0)

def openDefaultTemplate():
    try:
        import os
        appdataDir = os.environ.get('APPDATA')
        templateFile = f'{appdataDir}\\QGIS\\QGIS3\\profiles\\default\\project_templates\\project.qgs'

        if not os.path.isfile(templateFile):
            pushWarningMessage(f'Projektin template-tiedostoa ei löydy: {templateFile}')
            return

        project = QgsProject.instance()

        if not project.read(templateFile):
            pushWarningMessage(f'Projektin template-tiedoston avaaminen epäonnistui: {project.error()}')
            return

        project.setFileName(None)

    except Exception as e:
        pushWarningMessage(f'Projektin template-tiedoston avaaminen epäonnistui: {e}')

openDefaultTemplate()
