# coding=UTF-8
# Author:Gentlesprite
# Software:PyCharm
# Time:2025/9/9 14:19
# File:config.py
import random
from typing import Optional

YEAR: str = '2026'
MONTH: str = '11'

activity_id: str = '1068562'  # 签到活动ID。
flow_id: str = '1269051'  # 签到礼包。
sd_id: str = ''.join(random.choices('0123456789abcdef', k=32))
special_date: list = [f'{YEAR}-{MONTH}-06', f'{YEAR}-{MONTH}-13', f'{YEAR}-{MONTH}-20', f'{YEAR}-{MONTH}-27']
special_date_flow_id: str = str(int(flow_id) + 4)  # 限定日期礼包。
cumulative_day: list = [3, 5, 9, 15, 20, 25]
cumulative_day_flow_id: str = str(int(flow_id) - 1)  # 累计签到礼包。
sign_gift_end_date: str = f'{int(YEAR) + 1 if MONTH == '12' else YEAR}-{'01' if MONTH == '12' else int(MONTH) + 1}-01'  # 活动结束日期。

# 版本福利配置（可选）。
version_gift_activity_id: Optional[str] = '1065559'  # 版本福利活动ID。
version_gift_play_flow_id: Optional[str] = '1266583'  # 游玩一局礼包。
version_gift_share_flow_id: str = str(
    int(version_gift_play_flow_id) + 1) if version_gift_play_flow_id else None  # 分享礼包。
version_gift_flow_id: str = str(int(version_gift_play_flow_id) + 2) if version_gift_play_flow_id else None  # 抽奖。
version_gift_end_date: str = '2026-11-29'
