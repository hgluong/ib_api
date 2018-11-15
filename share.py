# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 13:24:31 2018

@author: nguye
"""

#%%
import ib.ext.Contract as ibContract
import ib.ext.Order as ibOrder
import ib.ext.TagValue as ibTagValue
import ib.ext.ComboLeg as ibComboLeg
from ib.ext.EClientSocket import EClientSocket
from IBWrapper import IBWrapper
#%%
callback = IBWrapper()
tws = EClientSocket(callback)
callback.initiate_variables()
host = ""
#host = "192.168.1.235"
port = 7497
clientId = 0
tws.eConnect(host, port, clientId)
tws.checkConnected(host) 

