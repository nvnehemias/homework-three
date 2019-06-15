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
        #counts the total number of votes
        x = x + 1
        #if statement that adds up the total number of votes for each candidate
        if row[2] == 'Khan':
            a = a + 1
        elif row[2] == 'Correy':
            b = b + 1
        elif row[2] == 'Li':
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

print("Election Results")
print("---------------------------")
print("Total Votes: ",x)
print("Khan: ","{0:.3f}%".format(a/x * 100),"(",a,")")
print("Correy: ","{0:.3f}%".format(b/x * 100),"(",b,")")
print("Li: ","{0:.3f}%".format(c/x * 100),"(",c,")")
print("O'Tooley: ","{0:.3f}%".format(d/x * 100),"(",d,")")
print("---------------------------")
print("Winner: ",name)
print("---------------------------")

#Export a text file    
file = "PyPoll_Report.txt"
with open(file,'w') as f:
    print("Election Results",file = f)
    print("---------------------------",file = f)
    print("Total Votes: ",x,file = f)
    print("---------------------------", file = f)
    print("Khan: ","{0:.3f}%".format(a/x * 100),"(",a,")",file = f)
    print("Correy: ","{0:.3f}%".format(b/x * 100),"(",b,")",file = f)
    print("Li: ","{0:.3f}%".format(c/x * 100),"(",c,")", file = f)
    print("O'Tooley: ","{0:.3f}%".format(d/x * 100),"(",d,")", file = f)      
    print("---------------------------",file = f)
    print("Winner: ",name,file = f)
    print("---------------------------", file = f)
    f.close()