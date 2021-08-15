desde decimal importar Decimal
desde fractions importar Fraction como Fracción
desde conteoPM importar *
desde redondeo importar *

escribir("2.55")
escribir("S -> Ubicado en Shanghai")
escribir("B -> Ubicado en Beijing")
prob = Decimal('0.4') + Decimal('0.7') - Decimal('0.8')
escribir("a) P(S ∩ B) =", prob)
prob = 1 - Decimal('0.8')
escribir("b) P(S' ∩ B') =", prob)

escribir("")
escribir("2.57")
prob = Fracción(5, 26)
escribir("a) Vocal excepto y:", prob)
prob = Fracción(9, 26)
escribir("b) Listada antes de la j:", prob)
prob = Fracción(19, 26)
escribir("c) Listada despues de la g:", prob)

escribir("")
escribir("2.59")
prob = Fracción(5*P(25,2)*(9**3)*4, P(26,3)*(9**4))
escribir("Seleccionar artículo:", prob)

escribir("")
escribir("2.61")
prob = Fracción(C(20,2),C(52,2))
escribir("Escoger cartas correctas:", prob)

escribir("")
escribir("2.63")
prob = Fracción(C(4,3)*C(48,2),C(52,5))
escribir("a) Tener 3 ases:", prob)
prob = Fracción(C(13,4)*C(13,1),C(52,5))
escribir("b) Tener 4 corazones y 1 tréboles:", prob)

escribir("")
escribir("2.65")
escribir("M -> Estudio matemáticas")
escribir("H -> Estudio historia")
prob = Fracción(54+69-35,100)
escribir("a) P(M ∪ H) =", prob)
prob = 1 - prob
escribir("b) P(M' ∩ H') =", prob)
prob = Fracción(69-35,100)
escribir("c) P(M ∩ H') = ", prob)

escribir("")
escribir("2.67")
escribir("A -> PC en dormitorio de adultos")
escribir("N -> PC en dormitorio de niños")
escribir("O -> PC en otro dormitorio")
escribir("F -> Oficina o estudio")
escribir("H -> Otra habitación")
prob = Decimal('0.03') + Decimal('0.15') + Decimal('0.14')
escribir("a) P(A ∪ N ∪ O) =", prob)
prob = 1 - prob
escribir("b) P(F ∪ H) =", prob)

escribir("")
escribir("2.69")
escribir("A -> Componente falle")
escribir("B -> Componente falle pero no se deforme")
prob = 1 - Decimal('0.2')
escribir("a) P(A') =", prob)
prob = prob - Decimal('0.35')
escribir("b) P(A' ∩ B') =", prob)
prob = 1 - prob
escribir("c) P(A ∩ B) =", prob)

escribir("")
escribir("2.71")
prob = Decimal('0.12') + Decimal('0.19')
escribir("a) No mas de 4 autos reciba servicio:", prob)
prob = 1 - Decimal('0.07')
escribir("b) Menos de 8 autos reciben servicio:", prob)
prob = Decimal('0.12') + Decimal('0.19')
escribir("c) 3 o 4 autos reciben servicio:", prob)

escribir("")
escribir("2.73")
escribir("A -> Cumple con llenado")
escribir("B -> Llena por debajo")
escribir("C -> Llena por arriba")
prob = 1 - Decimal('0.990') - Decimal('0.001')
escribir("a) P(C) =", prob)
prob = 1 - Decimal('0.001')
escribir("b) P(B') =", prob)
prob = 1 - Decimal('0.99')
escribir("c) P(A') =", prob)

escribir("")
escribir("2.75")
prob = 1 - Decimal('0.95') - Decimal('0.002')
escribir("a) Paquete muy pesado:", prob)
utilidades = (25 - 20) * 10000
escribir("b) Utilidades 10000 paquetes ideal: $", utilidades)
utilidades = redondear(utilidades - ((25*0.95 - 20)*10000), 0)
escribir("c) Reducción utilidad defectuosos: $", utilidades)