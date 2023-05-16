class activity():
    def __init__(self, start, end, name) -> None:
        """
        start = activity start time in unix epoch time(milliseconds since 1970)
        end = activity end time in unix epoch time
        name = activity name(string)
        """
        self.start = start
        self.end = end
        self.time = start - end
        self.name = name

    def convertTime():
        pass