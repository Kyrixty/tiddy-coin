"""
Refer to 'SettingsHandler' for description.
"""

import os
import json
import datetime

from app import utilities

basedir = os.path.dirname(__file__)

class SettingsHandler:
    '''
    Handles app settings.

    Base settings are:
    {
        "secret_key": [key],
        "App_Version": [version],
        "Last_Updated": [date]
    }
    '''
    def getAppSettings():
        '''
        Returns app settings.
        '''
        with open(basedir+"\\appSettings.json", mode="r") as f:
            return json.load(f)
    
    def writeAppSettings(settings: dict):
        '''
        Save app settings to file 'appSettings.json'
        '''
        settings["Last_Updated"] = str(datetime.datetime.now())

        with open(basedir+"\\appSettings.json", mode="w") as f:
            f.write(json.dumps(settings, indent=4))
    
    def editAppSettings(settings: dict):
        '''
        Expects a dictionary containing the key+value pairs
        to be edited. Does not require the full settings.

        Usage:
        editAppSettings({"secret_key": "abcde"})

        If the value does not exist, a new value will be created
        under the settings and will then be stored.
        '''

        appSettings = SettingsHandler.getAppSettings()

        for key, value in settings:
            appSettings[key] = value
        
        SettingsHandler.writeAppSettings(appSettings)
    
    def gen_new_secret_key():
        return utilities.Utility.genRandomString(size=256)
    
    def get_secret_key():
        return SettingsHandler.getAppSettings()["secret_key"]
    
    def get_app_version():
        return SettingsHandler.getAppSettings()["App_Version"]
    
    def get_last_update_date():
        return SettingsHandler.getAppSettings()["Last_Updated"]