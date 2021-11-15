log_file = open("um-server-01.txt") #This allows us to access the other file with the information


def sales_reports(log_file): #this is starting a function called sales reports that passes is log_file as a parameter
    for line in log_file: #This is for each line in the file 
        line = line.rstrip() #This gets rid of the spaces in the lines
        day = line[0:3] #This is accessing the data from the days at 0 index
        if day == "Mon": # if it's monday, print the line and what happened
            print(line)


sales_reports(log_file) #calling the function, produces the result 
