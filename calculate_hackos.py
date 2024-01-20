def is_anio_bisiesto(anio):
    if anio%100 == 0:
        if anio%400 == 0 and anio%4 == 0:
            return True
        else:
            return False
    else:
        if anio % 4 == 0:
            return True
        else:
            return False

def calculate_days(date1, date2):
    try:
        date1 = date1.split(" ")
    except:
        pass
    try:
        date2 = date2.split(" ")
    except:
        pass
    day1, month1, year1 = int(date1[0]), int(date1[1]), int(date1[2]) # Returned date
    day2, month2, year2 = int(date2[0]), int(date2[1]), int(date2[2]) # Due date
    dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    numDias = 0
    for anio in range(year1, year2 + 1):
        if is_anio_bisiesto(anio):
            dias[1] = 29
        else:
            dias[1] = 28
        if anio == year1:
            start_month = month1 - 1
        else:
            start_month = 0
        for mes in range(start_month, len(dias)):
            if mes == month1 - 1 and anio == year1:
                start_day = day1 - 1
            else:
                start_day = 0
            for dia in range(start_day, dias[mes]):
                crrnt_day = [dia + 1, mes + 1, anio]
                date2 = [day2, month2, year2]
                if crrnt_day == date2:
                    #print("The num of days is:", numDias)
                    return numDias
                else:
                    #print(f'{crrnt_day} is not the same than {date2}')
                    pass
                numDias += 1
    else:
        print("Nothing found")

def calc_hackos(date1, date2):
    date1 = date1.split(" ")
    date2 = date2.split(" ")
    day1, month1, year1 = int(date1[0]), int(date1[1]), int(date1[2]) # Returned date
    day2, month2, year2 = int(date2[0]), int(date2[1]), int(date2[2]) # Due date

    if year1 > year2:
        print(10000)
        pass
    elif year1 == year2:
        # There might be a fine
        if month1 > month2:
            # There is a fine. Calculate months
            print(500*(month1-month2))
            pass
        elif month1 == month2:
            # There might be a fine
            pass
            if day1 > day2:
                # There is a fine. Calculate days
                days_late = calculate_days(date2, date1)
                print(15*days_late)
            else:
                # No fine as book was returned on the same day as the due day
                print(0)
        else:
            # There is no fine
            print(0)
    else:
        # There is no fine
        print(0)

if __name__ == '__main__':
    #date1 = input("")
    #date2 = input("")
    date1 = '24 12 1898' # return date
    date2 = '18 9 1898' # due date
    calc_hackos(date1, date2)