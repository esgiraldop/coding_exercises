from anio_bisiesto import is_anio_bisiesto

def iter_days(fecha1, fecha2):
    dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    numDias = 1
    for anio in range(fecha1[2],fecha2[2]+1):
        if is_anio_bisiesto(anio):
            dias[1] = 29
        else:
            dias[1] = 28
        if anio == fecha1[2]:
            start_month = fecha1[1] - 1
        else:
            start_month = 0
        for mes in range(start_month, len(dias)):
            if mes == fecha1[1] - 1 and anio == fecha1[2]:
                start_day = fecha1[0] - 1
            else:
                start_day = 0
            for dia in range(start_day, dias[mes]):
                crrnt_day = (dia+1, mes+1, anio)
                if crrnt_day == fecha2:
                    print("El número de días es :", numDias)
                    return
                else:
                    #print(f'{crrnt_day} is not the same than {fecha2}')
                    pass
                numDias += 1
    else:
        print("Nothing found")

fecha1 = (13, 6, 1975)
fecha2 = (7,3,2576)

iter_days(fecha1, fecha2)