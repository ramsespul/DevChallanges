from datetime import datetime

def calcular_antiguedad(fecha_ingreso):
    fecha_transformada = datetime.strptime(fecha_ingreso, "%d/%m/%Y").date()
    fecha_hoy = datetime.now().date()
    diferencia = fecha_hoy - fecha_transformada
    return int(diferencia.days / 30)

def calcular_base_imponible(sueldo_base, meses_trabajados, cant_familiar):
    bonificacion = sueldo_base * (1 / 100) * meses_trabajados
    ang_familiar = sueldo_base * (5 / 100) * cant_familiar
    bs_imponible = sueldo_base + bonificacion + ang_familiar
    return bs_imponible

def calcular_cotizacion_salud(sueldo_base):
    cotiz_salud = sueldo_base * (7 / 100)
    return cotiz_salud

def calcular_contribucion_sso(emp, sueld_imponible):
    cnt_sso = 0
    if emp == 1:
        cnt_sso = sueld_imponible * (12 / 100)
    else:
        cnt_sso = sueld_imponible * (11.4 / 100)
    return cnt_sso
