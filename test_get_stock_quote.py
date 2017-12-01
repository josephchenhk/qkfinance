# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 16:22:42 2017

@author: joseph.chen
"""

import futuquant as ft

from settings.setting import HOST, PORT

if __name__=="__main__":
    quote_ctx = ft.OpenQuoteContext(host=HOST, port=PORT)
    
    quote_ctx.start()
    
    code_list = "HK.00700"
    q = quote_ctx.get_stock_quote(code_list) # 获取报价
    print(q)
    
    quote_ctx.stop()