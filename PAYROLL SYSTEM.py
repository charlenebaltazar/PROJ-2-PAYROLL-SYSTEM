
def inputs():
    name = input("Employees Name: ")
    
    date = int(input("Enter month (1 - Jan, 2- Feb...): "))
    while date > 12:
        date = int(input("Enter month (1 - Jan, 2- Feb...): "))
        
    position = input("Position: ")
    basicpay = float(input("Basic Pay: "))
    workingdays = int(input("Number of working days: "))
    absence = int(input("Number of Absence: "))
    overtime = int(input("Overtime (hrs): "))
    holiday = int(input("Number of Holiday Work/s: "))
    holidayot = int(input("Holiday Overtime (hrs): "))
    allowance = float(input("Allowance per day: "))
    bonus = float(input("Bonus: "))
    
    return name, date, position, basicpay, workingdays, absence, overtime, holiday, holidayot, allowance, bonus
    
def pagibig(basic):
    pagibigtax = 0
    
    if basic >= 5000:
        pagibigtax = 5000 * .02

    return pagibigtax

def sss(basic):
    ssstax = 0
    
    if basic >= 10000:
        ssstax = 450.00
    else:
        ssstax = 0
        
    return ssstax

def philhealth(basic):
    philhealthtax = 0
    
    if basic <= 10000:
        philhealth = (basic * .045) *.50
    elif basic >= 10001 and basic <= 39999.99:
        philhealth = (basic * .045) *.50
    elif basic >= 70000:
        philhealth = (basic * .045) *.50
    
    return philhealthtax

def incometax(basic):
    incometax = 0
    
    if basic >= 0 and basic <= 250000:
        incometax = 0
    elif basic > 250000 and basic <= 400000:
        incometax = basic * .20
    elif basic > 400000 and basic <= 800000:
        incometax = (basic * .30) + 30000
    elif basic > 800000 and basic <= 2000000:
        incometax = (basic * .30) + 130000
    elif basic > 2000000 and basic <= 8000000:
        incometax = (basic * .32) + 490000
    elif basic > 8000000:
        incometax = (basic * .35) + 2410000
        
    return incometax

def basicpay(payperday, workingdays):
    return payperday * workingdays

def perhour(payperday):
    return payperday / 8

def overtime(perhour, overtimehrs):
    return (perhour * 1.25) * overtimehrs

def holiday(basic, holiday):
    return (basic * 2) * holiday

def holidayOT(perhour, holidayOTpay):
    return (perhour * 2.60) * holidayOTpay

def allowanceamount(workingdays, allowance):
    return workingdays * allowance
    
def totalgross(basicwage, overtimepay, holidaypay, holidayotpay, allowancepay, bonus):
    return basicwage + overtimepay + holidaypay + holidayotpay + allowancepay + bonus

def totaldeduct(incometax, pagibig, sss, philhealth):
    return incometax + pagibig + sss + philhealth

#function computation ng annual gross
def annualgrosspay(payperday, annnualworkingdays):
    return payperday * annnualworkingdays

def computations(raw):
    # for annual gross, fixed 260 working days for regular working days
    annualworkingdays = 260
    
    #       raw[0]  raw[1]  raw[2]     raw[3]    raw[4]       raw[5]   raw[6]    raw[7]   raw[8]     raw[9]     raw[10]
    #return name,   date,   position, basicpay, workingdays, absence, overtime, holiday, holidayot, allowance, bonus
    basic = basicpay(raw[3], raw[4])
    basicperhour = perhour(raw[3])
    
    incometaxdeduction = incometax(basic)
    pagibigdeduction = pagibig(basic)
    sssdeduction = sss(basic)
    philhealthdeduction = philhealth(basic)

    OTpay = overtime(basicperhour, raw[6])
    holidaypay = holiday(raw[4], raw[7])
    holidayOTpay = holidayOT(basicperhour, raw[8])
    allowancepay = allowanceamount(raw[4] , raw[9])

    totalgrosspay = totalgross(basic, OTpay, holidaypay, holidayOTpay, allowancepay, raw[10])
    totaldeduction = totaldeduct(incometaxdeduction, pagibigdeduction, sssdeduction, philhealthdeduction)
    netpay = totalgrosspay - totaldeduction
    annualgross = annualgrosspay(raw[3], annualworkingdays)

    return OTpay, holidaypay, holidayOTpay, allowancepay, incometaxdeduction, pagibigdeduction, sssdeduction, philhealthdeduction, totalgrosspay, totaldeduction, netpay, annualgross

def main():
    #       raw[0]  raw[1]  raw[2]    raw[3]       raw[4]   raw[5]    raw[6]   raw[7]     raw[8]     raw[9]
    #return name,   date,   basicpay, workingdays, absence, overtime, holiday, holidayot, allowance, bonus
    raw = inputs()
    
    #unpacking raw datas
    name = raw[0]
    
    month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    date = month[raw[1] - 1]
    
    basicpay = raw[3] * raw[4]
    workingdays = raw[4]
    absence = raw[5]
    overtime = raw[6]
    holiday = raw[7]
    holidayOT = raw[8]
    bonus = raw[10]
    
    datas = computations(raw)
    
    #unpacking list of datas
    overtimepay = datas[0]
    holidaypay = datas[1]
    holidayOTpay = datas[2]
    allowancepay = datas[3]
    
    incometaxdeduction = datas[4]
    pagibigdeduction = datas[5]
    sssdeduction = datas[6]
    philhealthdeduction = datas[7]
    
    totalgrosspay = datas[8]
    totaldeduction = datas[9]
    netpay = datas[10]
    annualpay = datas[11]
    
    print("\n\n\n")
    print("\t\t\tKALAYAAN ENGINEERING CO., INC.\t\t")
    print("\t\t\t\t   {}\t\t".format(date))
    
    print()
    
    print("Name: {}".format(raw[0]))
    print("Position: {}".format(raw[2]))
    print("\t\t\t\t\t\tGROSS SALARY\t\t\t    DEDUCTIONS\t")
    print("Basic Pay:\t{}\tD\t{}\t    PAG-IBIG:\t\t{}".format(workingdays, basicpay, pagibigdeduction))
    print("Absence:\t{}\t \t \t    SSS:\t\t{}".format(absence, sssdeduction))
    print("Overtime:\t{}\tHR\t{}\t    PHILHEALTH:\t\t{}".format(overtime, overtimepay, philhealthdeduction))
    print("Holiday:\t{}\tD\t{}\t    INCOME TAX:\t\t{}".format(holiday, holidaypay, incometaxdeduction))
    print("Holiday OT:\t{}\tHR\t{}\t".format(holidayOT, holidayOTpay))
    print("Allowance:\t{}\t".format(allowancepay))
    print("Bonus:\t\t{}\t".format(bonus))
    print()
    print("Total Gross Pay:\t\t{}\t    Total Deduction:\t{}".format(int(totalgrosspay), totaldeduction))
    print("Annual Gross Pay:\t\t{}\t    Net Pay:\t\t{}".format(int(annualpay), netpay))
    print("\t\t\t\t\t    Signature:\t\t")
    print("")
    
main()