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
 empol_dict= {} 
 

#use a loop to iterate through the csv file
for row in reader: 
    
     if row['Department'] == 'Marketing'  row['Title'] == 'Customer Service Represetatives':
        empol_dict[row['First Name'] +  row['Last Name']] = (row['Salary']) * .1
    


   for name, nsalary in empol_dict.items():
        current_salary = row['Salary']
        print(f"{name}: Current Salary: ${current_salary:.2f})")
        print(f"{name}: New Salary: ${nsalary:.2f}")




    #check if the employee fits the search criteria


    

print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per printout
#print(empol_dict)



          
        

        
    
