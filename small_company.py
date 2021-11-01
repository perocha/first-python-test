from company import Company

class SmallCompany(Company):

    def smallCompanySpecific (self):
        return True

    def stock_price_alert (self, stock_threshold):
        return False