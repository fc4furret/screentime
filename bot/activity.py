import datetime

from datetime import datetime
from datetime import timedelta

class activity:
    def __init__(self):
        self.start = 0
        self.end = 0
        self.time = 0
        self.name = 0

    def __init__(self, start : datetime, end : datetime, name) -> None:
        """
        start = activity start time in utc time 
        end = activity end time in utc time
        name = activity name(string)
        """
        self.start : datetime = start
        self.end : datetime = end
        self.time : timedelta = end - start
        self.name = name

    def __str__(self) -> str:
        return f'played {self.name} for {self.time} time'

    def convertTime():
        pass