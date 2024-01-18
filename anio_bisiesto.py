año = 2000

def is_anio_bisiesto(año):
    if año%100 == 0:
        if año%400 == 0 and año%4 == 0:
            #print(f"El año {año} es bisiesto")
            return True
        else:
            #print(f"El año {año} no es bisiesto")
            return False
    else:
        if año % 4 == 0:
            #print(f"El año {año} es bisiesto")
            return True
        else:
            #print(f"El año {año} no es bisiesto")
            return False

if __name__ == "__main__":
    año = 2000
    is_anio_bisiesto(año)