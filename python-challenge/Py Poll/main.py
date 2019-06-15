import os 
import csv
#setting the variables and list 
totalrows = []
x = 0
a = 0
b = 0
c = 0
d = 0


csvpath = os.path.join("..","03-Python_Homework_PyPoll_Resources_election_data.csv")

with open(csvpath,newline="") as csvfile:
    #reads the files
    csvreader = csv.reader(csvfile,delimiter = ",")

    #takes the header of the csv file and saves it. The cursor is now on the second row that has initial values we need to work with. 
    header = next(csvreader)

    
    for row in csvreader:
        #create a list that has the voter id and candidate
        totalrows.append([row[0],row[2]])
    

    #for loop that runs through the list totalrows and add up the number of votes
    for i in range(len(totalrows)):
        x = x + 1
    

    #The total number of votes each candidate received 
    for j in range(len(totalrows)):
        if totalrows[j][1] == "Khan":
            a = a + 1
        elif totalrows[j][1] == "Correy":
            b = b + 1
        elif totalrows[j][1] == "Li":
            c = c + 1
        else:
            d = d + 1

    #find the max number of votes by candidate
    winner = max(a,b,c,d)

    #find the corresponding candidate for the max number of votes
    if winner == a:
        name = "Khan"
    elif winner == b:
        name = "Correy" 
    elif winner == c:
        name = "Li"
    else:
        name = "O'Tooley"


    #print the results
    print("Election Results")
    print("---------------------------")
    print("Total Votes: ",x)
    print("---------------------------")
    print("Khan: ","{0:.3f}%".format(a/len(totalrows) * 100),"(",a,")")
    print("Correy: ","{0:.3f}%".format(b/len(totalrows) * 100),"(",b,")")
    print("Li: ","{0:.3f}%".format(c/len(totalrows) * 100),"(",c,")")
    print("O'Tooley: ","{0:.3f}%".format(d/len(totalrows) * 100),"(",d,")")     
    print("---------------------------")
    print("Winner: ",name)
    print("---------------------------")