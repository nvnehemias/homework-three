import os 
import csv
#total will be used to sum the total number of months
monthtotal = 0
#sumtotal will be the sum of profit/losses over the entire period
sumtotal = 0
#sums will be used in the equation for the average change 
sums = 0
#listrows  will be used for storing the profit/losses over the entire period
listrows = []
#mylist2 used for difference and month matching
listrows2 = []
#allmonths is a list of all the months 
allmonths = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

csvpath = os.path.join("..","03-Python_Homework_PyBank_Resources_budget_data.csv")

with open(csvpath, newline = "") as csvfile:

    #reads the files
    csvreader = csv.reader(csvfile,delimiter = ",")

    #header will take in the name of the columns in the first row 
    header = next(csvreader)

    #loop that runs through csvfile 
    for row in csvreader:

        #add the row to our first list
        listrows.append(row)

        #splitting month-year
        monthyear = row[0]
        month = monthyear.split("-")
        #if statement check if the month is in the list months
        if allmonths.count(month[0]) == 1:
            monthtotal = monthtotal + 1

        #adds up the profits 
        profit_loss = int(row[1])
        sumtotal = sumtotal + profit_loss

    #---------------------The average of the changes in "Profit/Losses" over the entire period-----------------------------------------
    for i in range(1,len(listrows)):
        #taking the difference of the two "Profit/Losses" and saving them to a list. From that list created we find the max, min, and average
        difference = int(listrows[i][1]) - int(listrows[i-1][1])
        mymonth = listrows[i][0] #takes the month corresponding to the difference
        listrows2.append([mymonth,difference]) 

    #for loop that takes the average of the changes in "Profit/Losses" over the entire period
    for j in range(len(listrows2)):
        sums = sums + int(listrows2[j][1])
    averagee = sums/len(listrows2)
    average = round(averagee,2) 

    #for loop and if statement that finds the greatest value and the corresponding month 
    maxvalue = listrows2[0][1]
    maxmonth = listrows2[0][0]
    for k in range(1,len(listrows2)):
        if int(listrows2[k][1]) > int(maxvalue):
            maxvalue = listrows2[k][1]
            maxmonth = listrows2[k][0] 

    #for loop and if statement that finds the Greatest Decrease in Profit and the corresponding month
    minvalue = listrows2[0][1]
    minmonth = listrows2[0][0]
    for h in range(1,len(listrows2)):
        if int(listrows2[h][1]) < int(minvalue):
            minvalue = listrows2[h][1]
            minmonth = listrows2[h][0] 

    print("Financial Analysis")
    print("------------------------------")
    print("Total months: ", monthtotal)
    print("Total: $",sumtotal)
    print("Average Change: $",average)
    print("Greatest Increase in Profits:",maxmonth,"($",maxvalue,")")
    print("Greatest Decrease in Profits:",minmonth,"($",minvalue,")")
