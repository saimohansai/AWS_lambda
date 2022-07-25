from datetime import datetime


# # dates in string format
# str_d1 = '2020/10/20'
# str_d2 = '2021/10/20'

# print(datetime.date())
#print(datetime.time())
#print(datetime.ctime())
#d = datetime.date("2013", "10", "23")
#print(d)
#
Present_date = str(datetime.now()).split(" ")[0]
# \AWS_date="2022-06-07T19:42:09.000Z"
# AWS_date= AWS_date.split("T")[0]
# print(Present_date)
# print(AWS_date)
# # convert string to date object
# d1 = datetime.strptime(Present_date, "%Y-%m-%d")
# d2 = datetime.strptime(AWS_date, "%Y-%m-%d")
#
# # difference between dates in timedelta
# delta = d1 - d2
# print(f'Difference is {delta.days} days')
#
#
Present_date = datetime.now()
print(Present_date)
print(type(Present_date))

Present_date=str(Present_date)
print(type(Present_date))

My_date= Present_date.split(" ")
print(My_date)
print(type(My_date))

My_date= Present_date.split(" ")[0]
print(My_date)
print(type(My_date))

#
# print(date)
# print(type(date))

