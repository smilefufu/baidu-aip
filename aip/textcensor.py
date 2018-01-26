# -*- coding: utf-8 -*-

from .base import AipBase

class AipTextCensor(AipBase):
    """
        Aip TextCensor
    """

    __antiSpamUrl = 'https://aip.baidubce.com/rest/2.0/antispam/v1/spam'
    
    def antiSpam(self, text, command_no="500071"):
        """
            antispam
        """

        data = {}
        data['content'] = text
        data['command_no'] = command_no

        return self._request(self.__antiSpamUrl, data)
