desde estadistica.medidas_posicion importar *
desde estadistica.graficas importar puntos
desde redondeo.redondeo importar *

escribir("1.1")
escribir("Mediciones tiempo de secado en pintura (horas)")
muestra = [3.4, 2.5, 4.8, 2.9, 3.6,
           2.8, 3.3, 5.6, 3.7, 2.8,
           4.4, 4.0, 5.2, 3.0, 4.8]
escribir(muestra)
escribir("a) Tamaño de la muestra =", tamaño(muestra), "datos")
escribir("b) Media de la muestra =", redondear(media(muestra), 3), "horas")
escribir("c) Mediana de la muestra =", mediana(muestra), "horas")
escribir("e) x_tr(20) =", redondear(media_recortada(muestra, 0.2), 3), "horas")

puntos.dibujar( 
       [{'color': 'b', 'muestra': muestra}], 
       "d) Análisis pintura esmaltada",
       "Tiempo secado (horas)")


escribir("")
escribir("1.3")
escribir("Mediciones resistencia a la tensión en aviones (psi)")
escribir("Sin deterioro acelerado")
muestra_1 = [227, 222, 218, 217, 225,
             218, 216, 229, 228, 221]
escribir(muestra_1)
escribir("Con deterioro acelerado")
muestra_2 = [219, 214, 215, 211, 209,
             218, 203, 204, 201, 205]
escribir(muestra_2)
escribir("c)")
escribir("Media Deterioro =", redondear(media(muestra_2), 2), "psi")
escribir("Media NoDeterioro =", redondear(media(muestra_1), 2), "psi")
escribir("d)")
escribir("Mediana Deterioro =", redondear(mediana(muestra_2), 2), "psi")
escribir("Mediana NoDeterioro =", redondear(mediana(muestra_1), 2), "psi")

puntos.dibujar( 
        [{'nombre': 'Sin deterioro', 'color': 'b', 'muestra': muestra_1},
         {'nombre': 'Con deterioro', 'color': 'r', 'muestra': muestra_2}],
        "a) Análisis aviones",
        "Resistencia tensión (psi)")


escribir("")
escribir("1.5")
escribir("Mediciones reducción de Colesterol en personas (mg/dL)")
escribir("Grupo de control")
muestra_1 = [7,  3, -4, 14, 2,
             5, 22, -7,  9, 5]
escribir(muestra_1)
escribir("Grupo de tratamiento")
muestra_2 = [-6,  5, 9, 4, 4,
             12, 37, 5, 3, 3]
escribir(muestra_2)
escribir("b)")
escribir("Control")
escribir("x_ =", redondear(media(muestra_1), 2), "mg/dL")
escribir("x~ =", redondear(mediana(muestra_1), 2), "mg/dL")
escribir("x_tr(10) =", redondear(media_recortada(muestra_1, 0.1), 2), "mg/dL")
escribir("Tratamiento")
escribir("x_ =", redondear(media(muestra_2), 2), "mg/dL")
escribir("x~ =", redondear(mediana(muestra_2), 2), "mg/dL")
escribir("x_tr(10) =", redondear(media_recortada(muestra_2, 0.1), 2), "mg/dL")

puntos.dibujar( 
        [{'nombre': 'Control', 'color': 'b', 'muestra': muestra_1},
         {'nombre': 'Tratamiento', 'color': 'r', 'muestra': muestra_2}],
        "a) Análisis personas",
        "Reducción colesterol (mg/dL)")