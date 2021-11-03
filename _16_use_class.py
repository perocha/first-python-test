'''
Example of using a class
'''
from company import Company
from small_company import SmallCompany

company1 = Company("Microsoft", 130000, "IT", 324.54)
company2 = Company("Google", 100000, "Advertising", 2500)

print (company1)

print (company1.stock_price)
print (company1.name)
print (company2.name)

print (company1.stock_price_alert(300))
print (company1.stock_price_alert(350))

company3 = SmallCompany ("Small", 1230, "Retail", 20)
print (company3.smallCompanySpecific())
print (company3.stock_price_alert(50))
