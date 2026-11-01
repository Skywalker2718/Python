Mo, Tu, We, Th, Fr, Sa, Su = 1, 2, 3, 4, 5, 6, 7
Days = (Mo, Tu, We, Th, Fr, Sa, Su)
Days_Dict = {
    Mo : "Monday",
    Tu : "Tuesday",
    We : "Wednesday",
    Th : "Thursday",
    Fr : "Friday",
    Sa : "Saturday",
    Su : "Sunday"
}

Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
Months_List = (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec)

Months_Having_31_Days = (Jan, Mar, May, Jul, Aug, Oct, Dec)
Months_Having_30_Days = (Apr, Jun, Sep, Nov)

Months_Dict = {
    Jan : "January",
    Feb : "February",
    Mar : "March",
    Apr : "April",
    May : "May",
    Jun : "June",
    Jul : "July",
    Aug : "August",
    Sep : "September",
    Oct : "October",
    Nov : "November",
    Dec : "December"
}

def Get_Date():
    Date = input("Enter The Date (From 1 To 31): ").strip()    
    if ((not Date.isdigit()) or (int(Date) < 1) or (int(Date) > 31)):
        print("Invalid Date!")
        return Get_Date()
    return int(Date)

def Get_Month():
    Month = input("Enter The Month (From 1 To 12): ").strip()
    if ((not Month.isdigit()) or (int(Month)) < 1 or (int(Month) > 12)):
        print("Invalid Month!")
        return Get_Month()
    return int(Month)

def Get_Year():
    Year = input("Enter The Year (From 1 CE To 10,000 CE): ").strip()
    if ((not Year.isdigit()) or (int(Year) < 1) or (int(Year) > 10000)):
        print("Invalid Year!")
        return Get_Year()
    return int(Year)

def Is_Leap_Year(y):
    return (y % 400 == 0) or ((y % 4 == 0) and (y % 100 != 0))

def Leap_Count(n):
    return (n // 4) - (n // 100) + (n // 400)

def Check_Date(d, m, y):
    if m == Feb:
        if d > 29:
            return 0
        if d == 29 and not Is_Leap_Year(y):
            return 0
        return 1
    elif m in Months_Having_30_Days:
        return d <= 30
    return 1

def Calculate_Day(d, m, y):
# Reference Date: 20 July, 2026
    x_1 = (y - 2026) * 365
    x_2 = (m - 7) * 30
    if (m <= 2):
        x_2 = x_2 + 2
    x_3 = (d - 20)
    x_4 = 0
    if (m > 7):
        x_4 = 1
        n = m
        while (n != 8):
            n -= 1
            if (n in Months_Having_31_Days):
                x_4 += 1
            pass
    elif (m < 7):
        for n in range(m , 6):
            if (n in Months_Having_31_Days):
                x_4 -= 1
            pass
    pass
    if y < 2026:
        x_5 = -(Leap_Count(2025) - Leap_Count(y))
        if Is_Leap_Year(y) and m < 3:
            x_5 -= 1

    elif y > 2026:
        x_5 = Leap_Count(y - 1) - Leap_Count(2026)
        if Is_Leap_Year(y) and m >= 3:
            x_5 += 1

    else:
        x_5 = 0
    Difference = x_1 + x_2 + x_3 + x_4 + x_5
    Day = Days_Dict[Days[Difference % 7]]
    return Day

def Display_Day(d, m, y, Day_Final):
    print(f"The Day on {d} {Months_Dict[m]} {y} (CE) is {Day_Final}.")

def main():
    print("WELCOME TO DAY CALCULATOR!")

    d = Get_Date()
    m = Get_Month()
    y = Get_Year()

    if (Check_Date(d, m, y) == 1):
        Day = Calculate_Day(d, m, y)
        Display_Day(d, m, y, Day)
    else:
        print("This Date does not exist! Try again with another date!")
        
main()
while True:
    choice = input("Program has ended. Enter 'E' to exit or 'R' to restart: ").lower()
    if choice == "e":
        print("Thank You!")
        break
    elif choice == "r":
        main()
    else:
        print("Invalid Input!")
