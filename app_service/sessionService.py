from app_enums.cache_keys_enum import CacheKeysEnum
from app_enums.http_methods_enum import HttpMethodsEnum
from app_service.CacheService import CacheService
from app_service.requestService import RequestService
from config.app_config import config
from requests import request
import json
class SessionService( RequestService, CacheService ):
    """This class will obtain all user in session data, like photo, permissions, etc..."""
    urlBase = config["URL_BASE"] + "/auth"
    
    def me(self):
        """This function will get the data of user in session..."""
        self.makeAuthRequest(url=config["URL_BASE"]+'/users/me',
                            on_failure=self.handleHttpErr,
                            on_success=self.setUserInSession,
                            method=HttpMethodsEnum.get)
    

    def userHavePermission(self, permission:str) -> bool:
        response = request(
            method=HttpMethodsEnum.get,
            headers={ "Authorization":RequestService.bearerToken },
            url=config["URL_BASE"] + '/users/me'
        )
        response = json.loads(response.content)
        if response is not None:
            #if CacheKeysEnum.userInfo in response:
            #    response = response[CacheKeysEnum.userInfo]
            #    if response is not None:
            if "roles" in response:
                roles = response["roles"]
                for rol in roles:
                    permissionList = rol['permissionList']
                    if permission in permissionList:
                        return True
                    else:
                        return False
        return False
    def getUserRol(self):
        response = request(
            method=HttpMethodsEnum.get,
            headers={"Authorization": RequestService.bearerToken},
            url=config["URL_BASE"] + '/users/me'
        )
        response = json.loads(response.content)
        return response["roles"]
    
    def getUser(self):
        response = request(
            method=HttpMethodsEnum.get,
            headers={"Authorization": RequestService.bearerToken},
            url=config["URL_BASE"] + '/users/me'
        )
        return json.loads(response.content)

    
    def setUserInSession(self, req, response):
        if response is not None:
            self.removeKeyCache(CacheKeysEnum.userInSession)
            self.writeCache(response, CacheKeysEnum.userInSession)
            

    
    def getUserData(self):
        userInSession = self.readCache(CacheKeysEnum.userInSession)
        return userInSession