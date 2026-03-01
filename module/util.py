# coding=UTF-8
# Author:Gentlesprite
# Software:PyCharm
# Time:2025/9/11 16:14
# File:util.py
import time
import schedule
from datetime import datetime
from functools import wraps
from typing import Callable, Union, Optional, Hashable

from rich.console import Console as RichConsole
from rich.live import Live
from rich.panel import Panel
from rich.text import Text

from . import log, console
from .parser import PARSE_ARGS


def safe_index(
        obj: Union[list, None],
        value: Hashable,
        start: Optional[int] = 0
) -> Union[int, None]:
    try:
        return obj.index(value) + start
    except (ValueError, AttributeError):
        return None


def schedule_task(time_str: str = '00:00:00'):
    def decorator(func: Callable):
        @wraps(func)
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)

            if not PARSE_ARGS.loop:
                return result

            schedule.every().day.at(time_str).do(func, *args, **kwargs)

            p = f'开始执行循环任务,当前时间:{datetime.now()}。'
            p2 = f'任务将在每天{time_str}执行。'
            log.info(p)
            log.info(p2)
            console.log(p)
            console.log(p2)

            with Live(refresh_per_second=1, console=console) as live:
                while True:
                    schedule.run_pending()

                    next_run = schedule.next_run()
                    if next_run:
                        remaining_time = (next_run - datetime.now()).total_seconds()
                        remain_hours = int(remaining_time // 3600)
                        remaining_time %= 3600
                        remain_minutes = int(remaining_time // 60)
                        remain_seconds = int(remaining_time % 60)

                        countdown_text = Text()
                        countdown_text.append(f'距离下次执行任务还有', style='white')
                        countdown_text.append(f'{remain_hours}:{remain_minutes:02d}:{remain_seconds:02d}', style='bold cyan')
                        countdown_text.append(f'(将在{time_str}执行)', style='white')

                        panel = Panel(
                            countdown_text,
                            title='[bold green]定时任务倒计时[/bold green]',
                            border_style='green',
                            padding=(1, 2)
                        )

                        live.update(panel)

                    time.sleep(1)

        return inner

    return decorator
