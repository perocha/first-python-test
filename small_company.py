'''
Example of using inhereted class
'''
from company import Company

class SmallCompany(Company):
    '''Class definition'''

    def small_company_specific (self):
        '''New method specific to this new class'''
        print (self.name)
        print (self.num_employees)
        print (self.sector)
        return True

    def stock_price_alert (self, stock_threshold):
        '''Redefine an existing method'''
        print (f"Not applicable to {self.name}")
        return False
