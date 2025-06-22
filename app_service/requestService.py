import json
from app_enums.cache_keys_enum import CacheKeysEnum
from app_enums.http_methods_enum import HttpMethodsEnum
from app_service.CacheService import CacheService
from helpers.showMessages import ShowMessages
from kivy.network.urlrequest import UrlRequest

class RequestService(CacheService, ShowMessages):
    """This class have request general methods"""
    http = UrlRequest
    bearerToken:str = None
    
    def makeAuthRequest(self, method: HttpMethodsEnum, on_failure: any, on_success: any, url: str, body: dict = None) -> None:
        """This function make request autenticated with the JWT"""
        headers = {
            "Authorization": self.bearerToken, "Content-type": "application/json"
        }

        if(body is None):
            self.http(
                url=url,
                method=method,
                on_error=self.showError,
                on_success=on_success,
                req_headers=headers,
                on_failure=on_failure
            )
        elif( body is not None ):
            body = json.dumps(body)
            self.http(
                url=url,
                method=method,
                on_error=self.showError,
                on_success=on_success,
                req_headers=headers,
                on_failure=on_failure,
                req_body=body
            )

    def makeAuthSyncRequest(self, method: HttpMethodsEnum, url: str, on_failure: any = None, on_success: any = None, body: dict = None):
        """This function make request autenticated with the JWT & sincronus"""
        headers = {
            "Authorization": self.bearerToken, "Content-type": "application/json"
        }

        if (body is None):
            self.http(
                url=url,
                method=method,
                on_error=self.showError,
                on_success=on_success,
                req_headers=headers,
                on_failure=on_failure
            ).wait()
        elif (body is not None):
            body = json.dumps(body)
            self.http(
                url=url,
                method=method,
                on_error=self.showError,
                on_success=on_success,
                req_headers=headers,
                on_failure=on_failure,
                req_body=body
            ).wait()

    def makeRequest(self, method: HttpMethodsEnum, on_failure: any, on_success: any, url: str, on_progress: any = None, body: dict = None) -> None:
        body = json.dumps(body)
        self.http(
            url=url, 
            method=method, 
            req_body=body, 
            on_error=self.showError,
            on_success=on_success, 
            req_headers={ "Content-type": "application/json" },
            on_failure=on_failure,
            on_progress=on_progress
        )

    def showError(self, req, result) -> None:
        print(str(result))
        print(result)
        self.showToast(str(result))

    def json_validator(self, data) -> bool:
        try:
            json.loads(data)
            return True
        except ValueError as error:
            print("invalid json: %s" % error)
            return False
    
    def setBearerTokenInCache(self, bearerToken):
        self.writeCache(key=CacheKeysEnum.bearerToken, obj={ CacheKeysEnum.bearerToken: bearerToken })
        #print(self.readCache(CacheKeysEnum.bearerToken))

    def handleHttpErr(self, req, result):
        print(result)
        if type(result)==str:
            self.showToast(result)
        else:
            if "success" in result:
                self.showToast(result["message"])