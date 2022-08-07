"""通过网络访问配置

> 通过RPC服务来获取配置
> 通过Restful来获取配置
> 通过REDIS来获取配置
"""
import os
import socket
import platform
import getpass
import uuid


def get_architecture():
    '''获取操作系统的位数'''
    _result = list(platform.architecture())
    return " ".join(_result)


def get_machine():
    '''计算机类型'''
    return platform.machine()


def get_node():
    '''计算机的网络名称'''
    return platform.node()


def get_processor():
    '''计算机处理器信息'''
    return platform.processor()


def get_system():
    '''获取操作系统类型'''
    return platform.system()


def get_TotalInfo():
    '''汇总信息'''
    uname = platform.uname()
    result = []
    for _att in uname._fields:
        result.append(getattr(uname, _att))
    return " ".join(result)


def get_localDataPath():
    '''当前用户路径'''
    return os.path.expanduser('~')


def get_UserName():
    '''当前用户名'''
    return getpass.getuser()


def get_ComputerName1():
    '''获取机器名称'''
    return platform.node()()


def get_ComputerName():
    '''获取机器名称'''
    return socket.gethostname()


def get_AddressIp():
    '''获取本机IP'''
    return socket.gethostbyname(get_ComputerName())


def get_Mac():
    '''获取MAC地址'''
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ':'.join(mac[e:e+2].upper() for e in range(0, 11, 2))


def show_os_all_info():
    '''打印os的全部信息'''
    print('操作系统的位数 : [{}]'.format(get_architecture()))
    print('计算机类型 : [{}]'.format(get_machine()))
    print('计算机的网络名称 : [{}]'.format(get_node()))
    print('计算机处理器信息 : [{}]'.format(get_processor()))
    print('操作系统类型 : [{}]'.format(get_system()))
    print('汇总信息 : [{}]'.format(get_TotalInfo()))
    print('当前用户路径: [{}]'.format(get_localDataPath()))
    print('当前用户名: [{}]'.format(get_UserName()))
    print('机器名称: [{}]'.format(get_ComputerName()))
    print('机器IP: [{}]'.format(get_AddressIp()))
    print('MAC地址: [{}]'.format(get_Mac()))


class NetworkMonitorConnect(object):

    def __init__(self, ip, port, *args, **kwargs):
        self.ip = ip
        self.port = port
        self.args = args
        self.kwargs = kwargs

    def register(self):
        """注册当前机器为Woker

        """
        pass


if __name__ == '__main__':
    show_os_all_info()
