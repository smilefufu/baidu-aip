# -*- coding: utf-8 -*-

from .imagecensor import AipImageCensor

class AipTextCensor(AipImageCensor):
    pass
"""
官方sdk在imagecensor中已经有了同名方法了，这里继承调用一下，保证自己业务代码不做修改，后续再去掉此文件

    __antiSpamUrl = 'https://aip.baidubce.com/rest/2.0/antispam/v1/spam'

    def antiSpam(self, text, command_no="500071"):

        data = {}
        data['content'] = text
        data['command_no'] = command_no

        return self._request(self.__antiSpamUrl, data)
"""
