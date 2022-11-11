#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 先去改config.py
# 再启动nb 
# 再启动我
# python app.py

import uvicorn


if __name__ == "__main__":
    import ayaka_test.terminal
    import ayaka_test.cqhttp
    from ayaka_test.core import app
    # 随便一个没被占用的端口
    port = 22132
    uvicorn.run(app="__mp_main__:app", host="127.0.0.1", port=port)
