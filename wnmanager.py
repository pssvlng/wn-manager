from _typeshed import Self
from .wntype import WnType

class WnManager:
   __instance = None
   @staticmethod 
   def getInstance():
      if WnManager.__instance == None:
         WnManager()
      return WnManager.__instance

   def __init__(self, type: WnType):      
      if WnManager.__instance != None:
         raise Exception("WnManager Singleton can only be created once. Use static method getInstance()")
      else:
         WnManager.__instance = self
         self.__wnType = type

   def setWnType(self, type: WnType):
      self.__wnType = type      

   def save(self):
      pass   

   def download(self, lang):
      pass
