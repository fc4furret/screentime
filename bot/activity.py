import datetime

from datetime import datetime
from datetime import timedelta

class activity():
    def __init__(self, start, end, name) -> None:
        """
        start = activity start time in utc time 
        end = activity end time in utc time
        name = activity name(string)
        """
        self.start = start
        self.end = end
        self.time = start - end
        self.name = name

    def convertTime():
        pass