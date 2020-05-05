# QGIS Plugin base

This QGIS plugin base is created with Plugin Builder plugin.

## Installing

Download OSGeo4W network installer and choose Express Desktop install. It installs all necessary tools (GDAL, PyQt5, QtDesigner, Python etc.) for QGIS plugin development with QGIS itself. After this you can use OSGeo4W shell to access these. Other option is to use Python CLI opened from `C:\OSGeo4W64\bin\python-qgis.bat` script. Python pip packages can be installed using e.g. `python-qgis.bat -m pip install`.

However all of these dependencies can be installed manually to existing python installation if desired.

1. Git clone this repository into `C:\Users\%USERPROFILE%\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins` folder
2. Go to this folder and compile plugin resources with `pyrcc5 -o resources.py resources.qrc`
3. Restart QGIS in order to load profiles again (with plugin)
4. Add plugin `Plugins` -> `Manage and Install Plugins...` -> `Installed` and check the copied plugin

## Qt Designer

This is a convenient tool for designing plugin ui. It modifies .ui files.

## Plugin Reloader

Plugin reloader enables reloading (compiling) project code after code changes. It can be downloaded for QGIS plugins. Hot key for using it is `CTRL + F5`.

## Workspace file

Depending on project it is usually needed to save template workspace for project. It can be included with the project files with type .qgs. Other possiblity is to use zipped version .qgz, but it makes following workspace file changes difficult.

## User profiles

`Settings` -> `User Profile` -> ...

By default user profile named `default` is used. All of its related data is stored under `C:\Users\%USERPROFILE%\AppData\Roaming\QGIS\QGIS3\profiles\default`.

Different profiles can be used to store e.g. different template workspaces, plugins.

## Database authentication

Database authentication can be done using QGIS internal authentication configuration. Every QGIS user has its own configuration file e.g. `db-auth` that plugin interacts with on start. Configuration file can be created from `Settings` -> `Options` -> `Authentication` -> `Add new authentication configuration`. Configuration has following parameters:

- Name -> Name of the configuration file. Used for loading auth config
- Id -> Id of the auth config. Used for accessing auth config
- Type -> Authentication type. Basic authentication is suggested for simple configuration (username, password)
- Username -> db username
- Password -> db password

After creation Master Password needs to be set for QGIS. This is for opening authentication configurations, therefore it is prompted on start of plugin. It can be reseted from `Utilities` -> `Reset master password`.

Generally speaking QGIS saves this auth configuration to users `qgis-auth.db` file. It can be found from users AppData path -> `C:\Users\%USERPROFILE%\AppData\Roaming\QGIS\QGIS3\profiles\default`. Due to this, it is convenient to seperate user data from project files.

## Database connection

Proided utility class DbConnection contains example methods for creating db connection with PostgreSQL database. Class variables `authConfigId` and `authConfigName` has to be set based on instuctions above. Additionally following environment variables needs to set for creating connection since authentication configuration only stores username and password.

- PGDATABASE -> db-name
- PGPORT -> db-port
- PGHOST -> db-host
- PGSSLMODE -> disable

If you are developming on Linux-environment check that QT `QPSQL`-driver is installed by running following .py script:

```
from PyQt5.QtSql import QSqlDatabase
print(QSqlDatabase.isDriverAvailable('QPSQL))
```

If it is not install by running following command

`$ sudo apt install libqt5sql5-psql`

### Database relations

`Project` -> `Properties...` -> `Relations`

This contains all relations between schema tables.

### Dev environment database

1. Install [docker](https://docs.docker.com/docker-for-windows/install/).
2. Run `docker-compose.yaml` file inside dev-folder by running `docker-compose -f docker-compose.yaml up --build`
3. PostgreSQL (with PostGIS) is running on port 5432 and can be accessed from localhost.

Docker container is based on image ([kartoza/postgis](https://github.com/kartoza/docker-postgis)). Link contains more configuration options.

Inside docker-compose.yaml you can specify initial sql-scripts that are run on container start. Currently it runs `setup-db.sql` file that creates dummy table with one of data.

```
Build containers
$ docker-compose -f docker-compose.yaml build

Start containers
$ docker-compose -f docker-compose.yaml up

Start and build containers
$ docker-compose -f docker-compose.yaml up --build
```

Optionally there is a possibility to store the PostgreSQL data directory inside host machine. If the container PostgreSQL data volume is attached data will persist even if the container is stopped.

```
Connect to database from container cli
$ psql -h localhost -U postgres
```

Some useful commands

```
Close connection
$ \q

List databases
$ \l

Connect to database
$ \c test_db

List tables inside database
$ \d

List schemas
$ \dn

List functions
$ \fn

List views
$ \dv
```

## Debugging

TODO
