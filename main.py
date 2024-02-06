#parse month should take in the text of the month and return the number 
#as a string
#January -> 1 (as a string)
#YOU MAY USE THIS FUNCTION IF YOU WANT TO OR YOU MAY REMOVE IT
def parse_month(month):
    months = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12"
    }

    return months[a]

#REMOVE PASS AND FIX THIS FUNCTION
#parse_date function should return the date formated as MM/DD/YYYY
#DO NOT REMOVE THIS FUNCTION
def parse_date(date):
    #a = parse_month(a)
    #date = (a, b, c)
    return '/'.join(date)


#REMOVE PASS AND YOUR CODE GOES HERE
if __name__ == '__main__':
    a = input()

    a = a.replace(',','')
    a = a.split()
    b = a[1]
    c = a[2]
    a = a[0]
    a = parse_month(a)
    date = (a, b, c)
    results = parse_date(date)

    print(results)

#testing
