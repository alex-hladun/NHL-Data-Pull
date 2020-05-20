Array Function was first function I built. Try the function with a schedule range input from NHL API (eg. "https://statsapi.web.nhl.com/api/v1/schedule?startDate=2007-09-29&endDate=2008-06-04") and you'll see it takes the game data and gives a list of dataframes for the data (each date is an item in the list, comtaining each game as a row in that dataframe).

Then I built "CleanTimeFunction" to convert the times to local times, and convert the dates to a format that allowed for easier merging with Excel odds data (dates changed to same format as Excel sheet). This function was built to run for an individual season, as it requires Spring Forward date (DSTdate) as an input.

Next function is the "NHLOddsMergerFunction", which takes this data from the NHL website and merges it with a season of betting odds. These odds were found at https://www.sportsbookreviewsonline.com/scoresoddsarchives/nhl/nhloddsarchives.htm,
and the Excel files are in this Github, with slight adjustments to allow easier merging (biggest thing was I changed the team name formatting to match data pulled from NHL website, so that it could find games and merge)

**Finally, all 3 of these functions were saved in "SaveMergedDataset Function". This function basically does everything described above. Put in a range of dates within an NHL season into the URL, enter DST date for that season, enter Excel file path for that season, and choose a filename to export to. This will save the file under the filename given, using the Pickle function, in your directory. Basically this data becomes stored in your directory and you can use it when you want, with the following code (filename is example):

filename = '2007-08dataset'
infile = open(filename, 'rb')
df1 = pickle.load(infile)
infile.close()

Again, this file is a LIST of dataframes, organized by date with all odds data.

The file "ImportMergedDataforEachYear" is just an example of using this final function to import data for 07-08 season. I've done this for every other season as well, and the pickle files are in the Github (2007-08dataset, 2008-09dataset etc), see 4 lines of code above for how to import these files as datasets. 

I then created a short file "CombineAllYears" that combines all of this data into one big dataset, also in this GitHub, saved as "2007-20 dataset." This file has each year of data as an item in a list. Each of these items is a list of dates for that season. Each date is a dataframe containing the games for that day as rows. Essentially it's a list of lists of dataframes. Listception.

This dataset could then be used to quickly test betting strategies, which I haven't really got to yet, other than a couple other random files in here (HomeRecord580AfternoonOver, VisitorUnderdogAfternoonHome550W%).









