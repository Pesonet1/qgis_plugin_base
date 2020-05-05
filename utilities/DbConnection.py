import os

from qgis.core import QgsApplication, QgsAuthMethodConfig
from PyQt5.QtSql import QSqlDatabase

class DbConnection:
    """ Creates and holds PostGIS connection """

    authConfigId = "" # Set auth configuration id
    authConfigName = "" # Set auth configuration name

    def __init__(self):
        self.connection = self.createDbConnection()

    def getConnection(self):
        return self.connection

    def loadAuthConfig(self, authConfigId):
        print("Loading auth config for db connections")

        authManager = QgsApplication.instance().authManager()

        authConfig = QgsAuthMethodConfig(self.authConfigName)
        authManager.loadAuthenticationConfig(authConfigId, authConfig, True)

        print("Auth config retreived successfully")
        return authConfig

    def createDbConnection(self):
        db_instance = QSqlDatabase.addDatabase('QPSQL')

        # Get user stored authConfig -> has to be set for each user!
        authConfig = self.loadAuthConfig(self.authConfigId)

        if db_instance.isValid() and authConfig.isValid():
            print("Database instance is valid")

            db_instance.setHostName(os.environ['PGHOST'])
            db_instance.setDatabaseName(os.environ['PGDATABASE'])
            db_instance.setPort(int(os.environ['PGPORT']))
            db_instance.setUserName(authConfig.configMap().get("username"))
            db_instance.setPassword(authConfig.configMap().get("password"))

            if db_instance.open():
                print("Database connection succeeded")
                return db_instance
            else:
                print("Database connection failed")
                err = db_instance.lastError()
                print(err.driverText())
                return
        else:
            print("Database instance is invalid")
            return

    def executeSql(self, sql, reConnectTries = 3):
        """
        Queries given sql clause

        :param sql:
        :param reConnectTries: max recursien stack for reconnecting
        """

        if reConnectTries == 0:
            print("Reconnection tries exceeded")
            return

        if not self.connection.isValid():
            self.connection = self.createDbConnection()
            self.executeSql(sql, reConnectTries - 1)

        if self.connection.isValid():
            if self.connection.open():
                query = self.connection.exec_(sql)
                resultSet = []
                while query.next():
                    resultSet.append(query.record())
                return resultSet
            else:
                print(self.connection.lastError().driverText())
                return []
        else:
            print("Db connection invalid")
            return []
