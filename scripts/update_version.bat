REM Bat-script for manually updating users plugin version

@echo off

set selectedversion=<version-date>

set pluginfolder=%appdata%\QGIS\QGIS3\profiles\default
if not exist "%pluginfolder%\" goto HASNOPLUGIN

:HASPLUGIN
echo Plugin kansio löytyi, päivitetään versioon %selectedversion%
robocopy "%~dp0\versiot\%selectedversion%" "%pluginfolder%\python\plugins\project_x" /MIR > NUL
robocopy "%~dp0\versiot\%selectedversion%" "%pluginfolder%\project_templates" project.qgs > NUL
echo Päivitetty
goto END

:HASNOPLUGIN
echo Plugin kansiota ei loydy, tee ensin QGIS-käyttöliittymän kautta profiili ohjeiden mukaan.
goto END

:END
pause
