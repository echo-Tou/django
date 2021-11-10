# python自身是没有枚举类型的 在python3.4之后引入了枚举包
from enum import Enum
from typing import Sequence

class MessageType(Enum):
    info = 'info'
    warning = 'warning'
    error = 'error'
    danger = 'danger'

MessageType.info.label = '信息'
MessageType.warning.label = '警告'
MessageType.error.label = '错误'
MessageType.danger.label = '危险'


MessageType.info.color = 'green'
MessageType.warning.color = 'orange'
MessageType.error.color = 'gray'
MessageType.danger.color = 'red'


SenstiveWord = [
    '天气','坏人','明天'
]