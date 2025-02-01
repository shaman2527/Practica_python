ingresos = float(input("Introduce tu monto de ingresos: $ "))
gastos = float(input("Introduce tu monto de gastos: $"))
IVA = 0.16

ganancias_neta =ingresos - gastos
if ganancias_neta > 0:
    print("Tienes ganancias netas ") 
    print(f"Tu ganancia neta: ${ganancias_neta:.2f}")
    
    iva_a_pagar = ingresos * IVA
    print(f"Tu IVA a pagar es 16 %  $ {iva_a_pagar:.2f}") 
    
elif ganancias_neta < 0:
    print(f"\n ! Atencion ! tienes perdidas netas de: ${ganancias_neta:.2f}") 
    print(f"Tu perdida neta es de: ${ganancias_neta:.2f}")
else:
    print("No tienes ganancias ni perdidas") 