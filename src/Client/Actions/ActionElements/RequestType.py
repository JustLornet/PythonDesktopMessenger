from enum import Enum


class RequestType(Enum):
    Handled = 1,
    Error = 2,
    Empty = 3
