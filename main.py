# coding=UTF-8
# Author:Gentlesprite
# Software:PyCharm
# Time:2025/9/6 22:16
# File:main_refresh.py
# coding=UTF-8
import os
import sys

from module import console
from module.signer import NZSigner
from module.handler import Handler

if __name__ == '__main__':
    try:
        from config import cookies, activity_id, flow_id, sd_id, push_key
    except ImportError:
        cookies = os.getenv('cookies')
        activity_id = os.getenv('activity_id')
        flow_id = os.getenv('flow_id')
        sd_id = os.getenv('sd_id')
        push_key = os.getenv('push_key')
        if not all([cookies, activity_id, flow_id, sd_id]):
            console.print(
                '请配置以下环境变量或新建config.py设置以下变量后运行。\n'
                '# Linux/macOS 设置教程:export 变量="your_cookie_value_here"\n'
                '# Windows 设置教程:set 变量=your_cookie_value_here\n'
                '需设置以下变量:\n'
                'cookies\n'
                'activity_id\n'
                'flow_id\n'
                'sd_id\n'
                'push_key(可选)'
            )
            sys.exit()
    try:
        handler = Handler()
        signer = NZSigner(cookies=cookies, push_key=push_key)
        signer.sign(
            activity_id=activity_id,
            flow_id=flow_id,
            sd_id=sd_id
        )
        handler.task(
            func=signer.sign,
            activity_id=activity_id,
            flow_id=flow_id,
            sd_id=sd_id,
            handler=handler.task
        )
    except KeyboardInterrupt:
        console.log('键盘中断。')
