importmergeddataset("https://statsapi.web.nhl.com/api/v1/schedule?startDate=2007-09-29&endDate=2008-06-04",
                    "2008-03-09", "/Users/willmadsen/Documents/Python Stuff/Sports Betting Code/nhlodds2007-08.xlsx",
                    "2007-08dataset")
# could copy and paste this function for every schedule range,associated Excel file, DST date for that year
# and changing output file name, or just use the pickle files that I've already done this with
# (eg. 2007-08dataset, 2008-09dataset, 2007-20dataset etc)
