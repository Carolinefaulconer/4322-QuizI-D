'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv
#def main():

#open the file
with open ("employee_data.csv", "r") as input_file: 
    reader = csv.reader(input_file)



#create an empty dictionary
 empol_dict={} 
 

#use a loop to iterate through the csv file
for row in reader: 
    
    ID = row[0]
    first_name= row[1]
    last_name= row[2]
    salary= row[5]
    


   for i, row in empol_dict.items(): 
     print(f" Managers Name: {first_name}, {last_name}")
    print(f" Current Salary: {salary}")




    #check if the employee fits the search criteria


    

print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per printout
print(empol_dict)



          
        

        
    
