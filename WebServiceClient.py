# -*- coding: utf-8 -*-

import sys
from suds.client import Client
from suds import WebFault

class WebServiceClint():
    def __init__(self):
        self.webFunList = {}

    def load_web_info(self, webServiceAddress):
        try:
            errorInfo = ""
            self.webFunList.clear()

            self.webClient = Client(webServiceAddress)
            self.soapName = self.webClient.sd[0].ports[0][0][1]

            webFunInfoList = self.webClient.sd[0].ports[0][1]
            for webFun in webFunInfoList:
                webFunName = webFun[0]
                paramList = []
                for param in webFun[1]:
                    paramList.append(param[0])

                self.webFunList[webFunName] = paramList

            return errorInfo, True
        except WebFault as error:
            errorInfo = str(error)
            return errorInfo, False
        except:
            errorInfo = "调用webService时: " + str(sys.exc_info()[1])
            return errorInfo, False

    def execute_web_fun(self, webFunName, **webParam):
        try:
            result = self.webClient.service[self.soapName][webFunName](**webParam)
            return result
        except WebFault as error:
            return str(error)
        except:
            errorInfo = "调用webService时: " + str(sys.exc_info()[1])
            return errorInfo