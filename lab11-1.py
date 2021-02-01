import calendar as c 
from datetime import *
    
# using calender to print calendar of year  
# prints calendar of 2018  
d=datetime.today()
print ("The calender of year 2021 is : ")  
print (c.month(2021, 2))  
print("Year:",d.year)
print("Montth:",d.month)
print("Hour:",d.hour)
print("Minute:",d.minute)
print("Seconds:",d.second)
print("Datetime Format:",d)