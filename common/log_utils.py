import os
import logging
import time

current_path = os.path.dirname(__file__)
log_path = os.path.join( current_path , '..' , 'logs' )

class LogUtils(object):
    def __init__(self,logger=None):
        self.log_name = os.path.join(log_path, 'UITest_%s.log' % time.strftime('%Y_%m_%d')) #一天的日志放一个文件中
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(20) #  日志级别20  info级

        self.fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')  # 追加模式  写日志文件
        self.fh.setLevel(20)
        self.ch = logging.StreamHandler()   #写控制台
        self.ch.setLevel(20)

        formatter = logging.Formatter(
            '[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s')
        self.fh.setFormatter(formatter)
        self.ch.setFormatter(formatter)
        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)
        self.fh.close()
        self.ch.close()

    def get_log(self):
        return self.logger

#创建logger对象
logger = LogUtils().get_log()

if __name__=='__main__':
    logger.info( 'newdream' )
    logger.warning('warning警告日志')
    logger.error('error错误日志')
    logger.critical('critical致命错误日志')
