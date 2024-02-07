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

    return months[month]

#REMOVE PASS AND FIX THIS FUNCTION
#parse_date function should return the date formated as MM/DD/YYYY
#DO NOT REMOVE THIS FUNCTION
def parse_date(date):
    date = date.replace(',','')
    date = date.split()
    day = date[1]
    if len(day) == 1:
        day = '0' + day
    else:
        pass

    year = date[2]
    date = date[0]
    date = parse_month(date)
    date = (date, day, year)
    #a = parse_month(a)
    #date = (a, b, c)
    return '/'.join(date)


#REMOVE PASS AND YOUR CODE GOES HERE
if __name__ == '__main__':
    a = input()
    parse_date(a)
    results = parse_date(a)

    print(results)

    #testing

