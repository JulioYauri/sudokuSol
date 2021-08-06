def sudoku(tablero):

    def imprimir(g):
        for n, linea in enumerate(g):
            for m, c in enumerate(linea):
                P(str(c).replace("0", "."), end="")
                #dibujando dos lineas verticales
                if m in {2, 5}:
                    P("+", end="")
            P()
            #dibujando dos lineas horizontales 
            if n in {2, 5}:
                P("+" * 11)

    #s será el tablero a resolver
    #q es la posicion de algun 0 
    def casosPosibles(q, s):
        #obtiene todos los numeros de la fila
        linea = set(s[q[0]])
        #obtiene todos los numeros de la columna
        linea |= {s[i][q[1]] for i in range(9)}
        k = q[0] // 3, q[1] // 3
        #obtiene todos los numeros de la celda
        for i in range(3):
            linea |= set(s[k[0] * 3 + i][k[1] * 3:(k[1] + 1) * 3])
        return set(range(1, 10)) - linea

    #retorna true si no cumple
    def comprobarLista(linea):
        q = set(linea) - {0}
        for c in q:
            if linea.count(c) != 1:
                return True
        return False

    P = print
    imprimir(tablero)

    #s guarda el tablero 
    #t guarda las posiciones que contienen 0s
    s = []
    t = []

    for numLinea, linea in enumerate(tablero):
        try:
            n = list(map(int, linea))
        except:
            P("La linea " + str(numLinea + 1) + " no contiene un numero.")
            return
        if len(n) != 9:
            P("La linea " + str(numLinea + 1) + " no contiene 9 digitos.")
            return
        #actualizado t y s
        t += [[numLinea, i] for i in range(9) if n[i] == 0]
        s.append(n)
    if numLinea != 8:
        P("El juego contiene " + str(numLinea + 1) + " lineas en lugar de 9.")
        return

    #comprobando en filas
    for linea in range(9):
        if comprobarLista(s[linea]):
            P("La linea " + str(linea + 1) + " es contradictoria.")
            return
    #comprobando en columnas
    for col in range(9):
        #convierte una columna a una lista y la guarda en k
        k = [s[linea][col] for linea in range(9)]
        if comprobarLista(k):
            P("La columna " + str(col + 1) + " es contradictoria.")
            return
    #comprobando en cuadrados 3x3
    for linea in range(3):
        for col in range(3):
            q = []
            #guardando una celda en q
            for i in range(3):
                q += s[linea * 3 + i][col * 3:(col + 1) * 3]
            if comprobarLista(q):
                P("La celda (" + str(linea + 1) + ";" +
                  str(col + 1) + ") contradictoria.")
                return

    #inicializando matriz vacia del tamaño de t
    p = [[] for i in t]
    cr = 0

    #backtracking
    #completando todos los 0s
    while cr < len(t):
        p[cr] = casosPosibles(t[cr], s)
        try:
            #no hay casos
            while not p[cr]:
                s[t[cr][0]][t[cr][1]] = 0
                cr -= 1
        except:
            P("El sudoku no tiene solucion.")
            return
        #intenta con una solucion y la borra
        s[t[cr][0]][t[cr][1]] = p[cr].pop()
        cr += 1

    imprimir(s)
    return(s)
