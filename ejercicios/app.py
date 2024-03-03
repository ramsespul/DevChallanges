from calculadora_pago import *

pagos_empleados = []

while True:
    nombre = ''
    apellido = ''
    sueldo_base = 0
    fecha_ingreso = ''
    cantidad_de_hijos = 0
    empresa = 0
    antiguedad = 0
    base_imponible = 0
    cotizacion_salud = 0
    contribucion_sso = 0
    
    nombre = input("NOMBRE:")
    apellido = input("APELLIDO:")
    
    while True:
        try:
            sueldo_base = float(input("SUELDO BASE:"))
            break
        except ValueError:
            print("ERROR: Ingrese el sueldo")
    
    fecha_ingreso = input("FECHA INGRESO (dd/mm/aaaa):")
    antiguedad = calcular_antiguedad(fecha_ingreso)
    
    while True:
        try:
            cantidad_de_hijos = int(input("CANTIDAD DE HIJOS:"))
            break
        except ValueError:
            print("ERROR: Ingrese la cantidad de hijos")
    
    while True:
        try:
            empresa = int(input("EMPRESA (1 o 2):"))
            if empresa in (1, 2):
                break
            else:
                print("ERROR: Valor permitido para la empresa es 1 o 2")
                continue
        except ValueError:
            print("ERROR: Ingrese número de empresa")
            
    base_imponible = calcular_base_imponible(sueldo_base, antiguedad, cantidad_de_hijos)
    cotizacion_salud = calcular_cotizacion_salud(sueldo_base)
    contribucion_sso = calcular_contribucion_sso(empresa, base_imponible)
    pago_total = cotizacion_salud + contribucion_sso
    
    pagos_empleados.append(pago_total)
    
    print(f' BASE IMPONIBLE: {base_imponible}')
    print(f' COTIZACIÓN EN SALUD: {cotizacion_salud}')
    print(f' PAGO TOTAL: {pago_total}')
    
    continuar = input("¿Desea ingresar los datos de un nuevo trabajador (S/N):?")
    if continuar.upper() == "S":
        continue
    else:
        print("Calculando promedio de pagos...")
        if pagos_empleados:
            promedio_pago = sum(pagos_empleados) / len(pagos_empleados)
            print(f"El promedio de pago a los empleados es: {promedio_pago}")
        else:
            print("No se han registrado pagos.")
        break
