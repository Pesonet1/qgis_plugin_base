
# Deployment scripts & instructions for QGIS Plugins

### 1. Create QGIS profile for each user

In QGIS:

`Settings` -> `Profiles` -> `New profile...`

Give profile name that is used within the scripts

### 2. Set up auth configration for this profile

In QGIS:

`Settings` -> `Options` -> `Authentication`

Every user will give their own "master password" that they use for accessing this auth configuration. Select option -> `save to password manager`

Add new auth configuration with the following information:

- Name -> Name of the configuration file. Used for loading auth config
- Id -> Id of the auth config. Used for accessing auth config
- Type -> Authentication type. Basic authentication is suggested for simple configuration (username, password)
- Username -> db username
- Password -> db password

AFTER THIS CLOSE QGIS

### 3. Attach start.bat with copied QGIS shortcut

Make it convenient for the users to open QGIS with correct project template and plugin.

### 4. Run update_version.bat

This updates plugin version from path that is accessible for every user.

### 5. Open QGIS from the create QGIS shorcut

Set project plugin from `Plugins` -> `Manage and install plugins`

Select the projects plugin to active it for the user profile.

# Using

After installation plugin should be available for use. Any time user needs to update plugin new version needs to be copied
to the target environment to the specified version path (that the scripts use). These scripts don't provide any automated solution for this.
However CI tools (Jenkins, Gitlab CI etc.) can be used to automatically load source code into new folder and update scripts files.

Copied plugin code can be placed in a path which name follows update date. Update `update_version.bat` file according to these changes (newest source code folder & location).

NOTE: These scripts assumes that EVERY user have the following set up:

- Profile -> same for each user
- PostgreSQL database user with permissions
- Set up QGIS shortcut to run common .bat-scripts
- Run update_version.bat manually
