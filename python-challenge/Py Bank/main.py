import os 
import csv
#total will be used to sum the total number of months
total = 0
#sumtotal will be the sum of profit/losses over the entire period
sumtotal = 0

sum = 0
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


    #---------------------The average of the changes in "Profit/Losses" over the entire period-----------------------------------------
    for i in range(2,len(mylist)):
        #taking the difference of the two "Profit/Losses" and saving them to a list. From that list created we find the max, min, and average
        if mylist[i][1] != 'Profit/Losses':
            difference = int(mylist[i][1]) - int(mylist[i-1][1])
            mymonth = mylist[i][0] #takes the month
            match = [mymonth,difference] #matches month with difference value
        mylist2.append(match) #add the match and month to the list mylist2

    #for loop that takes the average of the changes in "Profit/Losses" over the entire period
    for j in range(len(mylist2)):
        sum = sum + int(mylist2[j][1])
    averagee = sum/len(mylist2)
    average = round(averagee,2) 

    #for loop and if statement that finds the greatest value and the corresponding month 
    maxvalue = mylist2[0][1]
    maxmonth = mylist2[0][0]
    for k in range(1,len(mylist2)):
        if int(mylist2[k][1]) > int(maxvalue):
            maxvalue = mylist2[k][1]
            maxmonth = mylist2[k][0] 

    #for loop and if statement that finds the Greatest Decrease in Profit and the corresponding month
    minvalue = mylist2[0][1]
    minmonth = mylist2[0][0]
    for h in range(1,len(mylist2)):
        if int(mylist2[h][1]) < int(minvalue):
            minvalue = mylist2[h][1]
            minmonth = mylist2[h][0] 


    print("Average Change: $",average)
    print("Greatest Increase in Profits:",maxmonth,"($",maxvalue,")")
    print("Greatest Decrease in Profits:",minmonth,"($",minvalue,")")
