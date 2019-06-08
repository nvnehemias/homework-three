import os 
import csv
total = 0
sumtotal = 0
mylist = []
#list used for difference and month matching
mylist2 = []
monthdiffer = []
csvpath = os.path.join("..","03-Python_Homework_PyBank_Resources_budget_data.csv")

with open(csvpath, newline = "") as csvfile:

    #reads the files
    csvreader = csv.reader(csvfile,delimiter = ",")

    #allmonths is a list of all the months 
    allmonths = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

    #loop that runs through csvfile 
    for row in csvreader:


        #splitting month-year
        monthyear = row[0]
        month = monthyear.split("-")
        #if statement check if the month is in the list months
        if allmonths.count(month[0]) == 1:
            total = int(total) + 1

        
        #If statement that adds the profit/losses over the entire period
        if row[1] == 'Profit/Losses':
            sumtotal = 0
        else: 
            profit_loss = int(row[1])
            sumtotal = sumtotal + profit_loss
        mylist.append(row)
    print("Total months: ", total)
    print("Total: $",sumtotal)
    #print(mylist)


    #---------------------The average of the changes in "Profit/Losses" over the entire period-----------------------------------------
    for i in range(2,len(mylist)):
        #taking the difference of the two "Profit/Losses" and saving them to a list. From that list created we find the max, min, and average
        if mylist[i][1] != 'Profit/Losses':
            difference = int(mylist[i][1]) - int(mylist[i-1][1])
            mymonth = mylist[i][0] #takes the month
            match = [mymonth,difference] #matches month with difference value
        mylist2.append(match) #add the match and month to the list mylist2
    
    for j in range(len(mylist2)):
        if mylist2[i][1]
    print(mylist2)
    #summ = sum(mylist2)
    #longlist = len(mylist2)
    #Average = summ/longlist
    #greatest = max(mylist2)
    #least = min(mylist2)
    #The average of the changes in "Profit/Losses" over the entire period
    #print("Average Change: $",Average)
    #print("Greatest Increase in Profits: $",greatest)
    #print("Greatest Decrease in Profits: $",least)
