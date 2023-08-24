
print('List of months: January, February, March, April, May, June, July, August, September, October, November, and December')
month_name = input('Input the name of a month: ')

if month_name == 'February':
    print('Number of days: 28/29 days')
elif month_name in ('April', 'June', 'September', 'November'):      
    print('Number of days: 30 days')
elif month_name in ('January', 'March', 'May', 'July', 'October', 'December'):
    print('Number of days: 31 days')
else:
    print('Error: Invalid month name')

    # found out that use  of 'in' operator to check if month_name matches any of the values within a tuple:(several strings or possibly other class in ())
