import datetime as dt

class Record:
    def __init__(self, amount, date=dt.date.today().strftime('%d.%m.%Y'), comment):
        self.amount = amount
        self.date = date
        self.comment = comment

class Calculator:
    records = []
    def __init__(self, limit):
        self.limit = limit

    def add_record(self, record, records):
        return records = append(record)

    def get_today_stats(self):

    def get_week_stat(self):

