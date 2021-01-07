import logging
import datetime
import os

def get_fomated_time(pstr = "%Y%m%d"):
    return ( datetime.datetime.now().strftime(pstr))

#日志目录路径
path1 = os.path.join(r'.\log',r'python-{}'.format(get_fomated_time(pstr = "%Y%m%d")))
# print(path1)

#日志文件名
fileName = 'test.log'
# filename=os.path.join(path1,fileName)
# print(filename)


#判断是否存在目标路径和文件，存在则写入日志
if not os.path.exists(path1):
    os.makedirs(path1)
    open(fileName,'a')

logging.basicConfig(filename=os.path.join(path1,fileName),
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)s %(name)-8s %(levelname)-8s %(message)s ')

logging.info('info messsage ')
logging.debug('debug messsage')
logging.warning('warning messsage')
logging.error('error messsage')
logging.critical('critical messsage')

