
week = range(1,7)

Dec = 31
Nov = 30
Oct = 31
Sep = 30
Aug = 31
Jul = 31
Jun = 30
May = 31
Apr = 30
Mar = 31
Jan = 31

def febdays(year):
    days = 28
    if (year % 4 == 0):
        days = days + 1
    if (year % 100 == 0)and (year %400 !=0):
        days = days - 1
    return days

def checkMonth(day):
    if ((day % 7) == 0):
        return True
    return False


print "offset test:"
print (365+1)%7

day = 365+1
sunday =0



for i in range (1,101):
    if ((day % 7) == 0):
        print "Jan 1 = Sunday"
        sunday +=1
        print i+1900
    day = day + Jan 
        
    if ((day % 7) == 0):
        print "Feb 1 = Sunday"
        print i+1900
        sunday += 1
    day = day + febdays(i+1900)

    if ((day % 7) == 0):
        print "Mar 1 = Sunday"
        print i+1900
        sunday +=1
    day = day + Mar

    if ((day % 7) == 0):
        print "Apr 1 = Sunday"
        print i+1900
        sunday +=1
    day = day + Apr

    if ((day % 7) == 0):
        print "May 1 = Sunday"
        print i+1900
        sunday +=1
    day = day + May

    if ((day % 7) == 0):
        print "Jun 1 = Sunday"
        print i+1900
        sunday +=1
    day = day + Jun

    if ((day % 7) == 0):
        print "Jul 1 = Sunday"
        print i+1900
        sunday +=1
    day = day + Jul

    if ((day % 7) == 0):
        print "Aug 1 = Sunday"
        print i+1900
        sunday +=1
    day = day + Aug

    if ((day % 7) == 0):
        print "Sep 1 = Sunday"
        print i+1900
        sunday +=1
    day = day + Sep

    if ((day % 7) == 0):
        print "Oct 1 = Sunday"
        print i+1900
        sunday +=1
    day = day + Oct

    if ((day % 7) == 0):
        print "Nov 1 = Sunday"
        print i+1900
        sunday +=1
    day = day + Nov

    if ((day % 7) == 0):
        print "Dec 1 = Sunday"
        print i+1900
        sunday +=1
    day = day + Dec

print sunday












