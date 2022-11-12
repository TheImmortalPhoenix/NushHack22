savings = input("Enter your current savings: \n")
rent = input("Enter the rent you pay each month: \n")
bills= input("Enter the average amount of money you pay for bills and others each month: \n")
monthlyIncome = input("Enter your monthly income: \n")
savings=float(savings)
bills=float(bills)
monthlyIncome=float(monthlyIncome)
loansName = []
loansValue = []
rent=float(rent)
def addLoan(name, value): 
    ind = 0
    if name in loansName:
        ind = loansName.index(name)

        loansValue[ind] += value
    else: 
        loansName.append(name)
        loansValue.append(value)
while True:
    action= input()
    if action=="Add loan":
        name=input("Name of person?")
        value=input("How much money do you owe them? (Use negative sign if they owe you money instead)")
        value=float(value)
        addLoan(name, value)
    if action=="View loans":
        res = "\n".join("{} {}".format(x, y) for x, y in zip(loansName, loansValue))
        print(res)
    if action=="Total":
        print(sum(loansValue))
    if action=="Edit bills and others":
        bills= input("Enter the average amount of money you pay for bills each month: ")
        bills=float(bills)
    if action =="Edit savings":
        savings = input("Enter your current savings: ")
        savings=float(savings)
    if action =="Edit rent":
        rent = input("Enter the rent you pay: ")
        rent=float(rent)
    if action =="Edit monthly income":
        monthlyIncome = input("Enter your monthly income: ")
        monthlyIncome=float(monthlyIncome)

    if action =="How much to spend?":
        save=input("How much do you want your total savings to be by the end of month?")
        save=float(save)
        x=save-savings
        print("You are recommended to spend up to", round(((monthlyIncome-(rent+bills))-x)/30,2), "per day")
        
        
        
        


        
