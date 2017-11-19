__author__ = 'nickyuan'


def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


def dayofyear(year, month, day):
    if leap_year(year):
        l = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return sum(l[:month - 1]) + day
    else:
        l = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return sum(l[:month - 1]) + day


print(dayofyear(2016, 3, 3))
print(dayofyear(2017, 3, 3))
