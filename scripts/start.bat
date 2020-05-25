REM This can be used as starting script for opening QGIS and setting all necessary configuration
REM without users doing it on their own. This script can be attached to a shortcut.

REM Set running environment PostgreSQL environment variables

set PGDATABASE=<db-name>
set PGPORT=<db-port>
set PGHOST=<db-host>
set PGSSLMODE=disable

REM Start QGIS and use few utility scripts to set up things...
REM settings.ini contains QGIS settings that are set automatically, without use manually setting them
REM load-template.py contains custom python script for loading the project template automatically on QGIS start

start "" C:\OSGeo4W64\bin\qgis-bin.exe ^
	--globalsettingsfile "%~dp0settings.ini" ^
	--profile default ^
	--code "%~dp0load-template.py"

