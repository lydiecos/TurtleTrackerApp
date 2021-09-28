#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Lydie Costes(lydie.costes@duke.edu)
# Date:   Fall 2021
#--------------------------------------------------------------

#ask user for the search date
userDate = input("Specify a date to find Sara [M/D/YYYY]: ")

#Create a variable pointing to the data file
fileName = './data/raw/sara.txt'

#Create a file object from the file
fileObj = open(fileName,'r')

#Read contents of file into a list
lineList = fileObj.readlines()

#Close the file
fileObj.close()

#create two empty dictionary objects
dateDict = {}
coordDict = {}

#Iterate through all lines in the linelist
for lineString in lineList:
    # Ignore non-data lines
    if lineString[0] in ("#", "u"): continue
    
    # Use the split command to parse the items in lineString into a list object
    lineData = lineString.split()
    
    # Assign variables to specfic items in the list
    record_id = lineData[0]   # ARGOS tracking record ID
    obs_date = lineData[2]   # Observation date
    obs_lc = lineData[4]       # Observation Location Class
    obs_lat = lineData[6]     # Observation Latitude
    obs_lon = lineData[7]     # Observation Longitude
      
    if obs_lc in ("1", "2", "3"):
        # Print information to the use

        
        dateDict[record_id] = obs_date
        coordDict[record_id] = (obs_lat, obs_lon)

#create empty list to hold matching keys
matchingKeys = []
        
#loop through items in the dateDict and collect keys for matching ones
for dateItem in dateDict.items():
    #get the date of the item
    theKey, theDate = dateItem
    #see if the date matches the user date
    if theDate == userDate:
        #if so, add the key to the list
        matchingKeys.append(theKey)
        
#if no records found, tell the user
if len(matchingKeys) == 0:
    print(f"Sorry, no records were found on {userDate}.")
        
#reveal locations for reach key in matchingKeys
for matchingKey in matchingKeys:
    obs_lat, obs_lon = coordDict[matchingKey]
    #obsDate = dateDict[matchingKey]
    print (f"Record {matchingKey} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {userDate}")
    
    
    
