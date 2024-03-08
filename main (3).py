salary = float(1250.0)
numDependents = float(2)
stateTax = salary * 0.065
federalTax = salary * 0.28
dependentsDeduction = float(numDependents) * float(2.5) * salary / 100
totalWithholding = stateTax + federalTax + dependentsDeduction 
takeHomePay = salary - totalWithholding
print("State Tax: $" + str(stateTax))
print("Federal Tax: $" + str(federalTax))
print("Dependents: $" + str(dependentsDeduction))
print("salary: $" + str(salary))
print("Take-Home Pay: $" + str(takeHomePay))