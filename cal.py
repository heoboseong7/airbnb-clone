from django.utils import timezone
import calendar


class Day:
    def __init__(self, number, past):
        self.number = number
        self.past = past

    def __str__(self):
        return str(self.number)


class Calendar(calendar.Calendar):
    def __init__(self, year, month):
        super().__init__(firstweekday=6)
        self.year = year
        self.month = month
        self.day_names = ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")
        self.months = (
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        )

    # (date, day of the week)
    # _는 그 자리에 해당하는 값은 무시한다는 의미
    def get_days(self):
        weeks = self.monthdays2calendar(self.year, self.month)
        days = []
        now = timezone.now()
        today = now.day
        month = now.month
        for week in weeks:
            for day, _ in week:
                past = False
                if month == self.month:
                    if day < today:
                        past = True
                new_day = Day(day, past)
                days.append(new_day)

        return days

    def get_month(self):
        return self.months[self.month - 1]
