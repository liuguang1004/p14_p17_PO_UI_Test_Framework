import os
import configparser

current_path=os.path.dirname(__file__)
config_path=os.path.join(current_path,'../config/config.ini')

class ConfigUtils():
    def __init__(self,path=config_path):
        self.cfg=configparser.ConfigParser()
        self.cfg.read(path,encoding='utf-8')

    @property
    def get_url(self):
        value=self.cfg.get('default','url')
        return value

    @property
    def log_path(self):
        value = self.cfg.get('default', 'log_path')
        return value

    @property  #方法当属性用
    def get_driver_path(self):
        value=self.cfg.get('default','driver_path')
        return value

    @property
    def get_driver_name(self):
        value=self.cfg.get('default','driver_name')
        return value


local_config=ConfigUtils()

if __name__=='__main__':
    print(local_config.get_url)
    print(local_config.log_path)
    print(local_config.get_driver_path)
    print(local_config.get_driver_name)
