import datetime as dt

class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if not date:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today = dt.datetime.now().date()
        total_amount = 0
        for record in self.records:
            if record.date == today:
                total_amount += record.amount
        return total_amount

    def get_week_stats(self):
        today = dt.date.today()
        one_week_ago = today - dt.timedelta(days=7)
        total_amount = 0
        for record in self.records:
            if one_week_ago <= record.date <= today:
                total_amount += record.amount
        return total_amount

class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        if self.get_today_stats() < self.limit:
            calories_remained = self.limit - self.get_today_stats()
            return (f'Сегодня можно съесть что-нибудь ещё, но с '
                    f'общей калорийностью не более {calories_remained} кКал')
        else:
            return 'Хватит есть!'

class CashCalculator(Calculator):
    EURO_RATE = 3.131
    USD_RATE = 2.587

    def exchange_rate(self, currency):
        rate_name_exchange = {
            'руб': (1, 'руб'),
            'rub': (1, 'руб'),
            'eur': (self.EURO_RATE, 'Euro'),
            'usd': (self.USD_RATE, 'USD'),
        }
        return rate_name_exchange[currency]

    def get_today_cash_remained(self, currency):
        rate, currency = self.exchange_rate(currency)
        if self.get_today_stats() < self.limit:
            cash_remained = round((self.limit - self.get_today_stats()) / rate, 2)
            return f'На сегодня осталось {cash_remained} {currency}'
        elif self.get_today_stats() == self.limit:
            return 'Денег нет, держись'
        else:
            debt = round((self.get_today_stats() - self.limit) / rate, 2)
            return f'Денег нет, держись: твой долг - {debt} {currency}'

cash_calculator = CashCalculator(100)

cash_calculator.add_record(Record(3.2, 'Кофе'))
cash_calculator.add_record(Record(amount=50, comment='Заправка топливом'))
record1 = Record(15, 'Покупки в продуктовом', '13.02.2021')
cash_calculator.add_record(record1)
cash_calculator.add_record(Record(amount=10, comment='Бильярд', date='2.02.2021'))

print(cash_calculator.get_today_cash_remained('eur'))
print(cash_calculator.get_today_cash_remained('rub'))
print(f'За прошедшую неделю потрачено {cash_calculator.get_week_stats()} руб.')
print()

calories_calculator = CaloriesCalculator(5000)

calories_calculator.add_record(Record(1000, 'Плюшка'))
calories_calculator.add_record(Record(2000, 'Две плюшки', '13.02.2021'))
calories_calculator.add_record(Record(2000, 'Три плюшки'))
calories_calculator.add_record(Record(5000, 'Пять плюшек', '02.02.2021'))

print(calories_calculator.get_calories_remained())
print(f'За прошедшую неделю наел {calories_calculator.get_week_stats()} кКал.')