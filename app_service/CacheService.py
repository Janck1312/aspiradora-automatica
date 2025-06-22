from kivy.cache import Cache

class CacheService:
    def __init__(self):
        Cache.register('cache', limit=10)

    def readCache(self, key:str) -> dict:
        return Cache.get('cache', key)
    
    def writeCache(self, obj:dict, key:str) -> None:
        Cache.append('cache', key, obj)
    
    def removeKeyCache(key:str)->None:
        Cache.remove(key)
