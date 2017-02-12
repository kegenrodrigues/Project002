def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    day=0    
    while dayIsBefore(year1, month1, day1, year2, month2, day2):
        year1,month1,day1=nextDay(year1, month1, day1)    
        day+=1
    return day

def dayIsBefore(year1, month1, day1, year2, month2, day2):
    if year1<year2:
        return True
    if year1==year2:
        if month1<month2:
            return True
        if month1==month2:
            if day1<day2:
                return True
    return False                

def test():#Testing Code 
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"
test()
    
