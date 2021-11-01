class Company:

    def __init__(self, name, num_employees, sector, stock_price) -> None:
        self.name = name
        self.num_employees = num_employees
        self.sector = sector
        self.stock_price = stock_price

    def stock_price_alert (self, stock_threshold):
        if self.stock_price < stock_threshold:
            return True
        else:
            return False