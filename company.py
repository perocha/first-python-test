'''
Simple class example
'''
class Company:
    '''Company class'''

    def __init__(self, name, num_employees, sector, stock_price) -> None:
        '''Constructor'''
        self.name = name
        self.num_employees = num_employees
        self.sector = sector
        self.stock_price = stock_price

    def stock_price_alert (self, stock_threshold):
        '''Return true or false depending if the stock threshold has been reached'''
        return bool(self.stock_price < stock_threshold)

    def public_method (self, test):
        '''Dummy method'''
        self.name = test
        return True
