from django.shortcuts import render, redirect
from operator import itemgetter
import json

_ = [int()]*81
global tablero
tablero = [_[i:i+9] for i in range(0, len(_), 9)]


def tablero_view(request):
    context = {
        'tablero': tablero,
        'iterador': range(1, 10),
    }
    return render(request, 'sudoku/sudoku.html', context)


def verificar_view(request):
    if request.method == 'POST':
        data = json.loads(request.POST.get('data', None))

        if data is None:
            raise AttributeError
        try:
            val, fil, col = [int(i)
                             for i in itemgetter('valor', 'fil', 'col')(data)]

        except ValueError:
            print('')

        if es_valido_online(tablero, val, (fil, col)):
            tablero[fil-1][col-1] = val
        return redirect('tablero')
       

def es_valido_online(tabl, val, pos):
    for col in range(9):
        if tabl[pos[0]-1][col-1] == val and pos[1]-1 != col:
            return False
    for row in range(9):
        if tabl[row][pos[1]-1] == val and pos[0]-1 != row:
            return False
    _fila = (pos[0]-1) // 3
    _col = (pos[1]-1) // 3
    for row in range(_fila*3, _fila*3+3):
        for col in range(_col*3, _col*3+3):
            if tabl[row][col] == val and (row, col) != pos:
                return False
    return True


def solucionar_view(request):
    solucionar(tablero)
    return redirect('tablero')


def clear_view(request):
    global tablero, t
    tablero = [_[i:i+9] for i in range(0, len(_), 9)]
    return redirect('tablero')

#funciones de solución
def es_valido_offline(tabl, val, pos):
    for col in range(9):
        if tabl[pos[0]][col] == val and pos[1] != col:
            return False
    for row in range(9):
        if tabl[row][pos[1]] == val and pos[0] != row:
            return False
    _fila = (pos[0]) // 3
    _col = (pos[1]) // 3
    for row in range(_fila*3, _fila*3+3):
        for col in range(_col*3, _col*3+3):
            if tabl[row][col] == val and (row, col) != pos:
                return False
    return True


def casilla_libre(tabl):
    for fila in range(9):
        for col in range(9):
            if tabl[fila][col] == 0:
                return (fila, col)
    return None


def solucionar(tabl):
    libre = casilla_libre(tabl)
    if not libre:
        return True
    else:
        fila, col = libre
    for num in range(1, 10):
        if es_valido_offline(tabl, num, (fila, col)):
            tabl[fila][col] = num
            if solucionar(tabl):
                return True
            tabl[fila][col] = 0
    return False
