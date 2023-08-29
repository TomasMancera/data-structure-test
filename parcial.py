peliculas = [ 
    {'titulo': 'starwars the return of jedi', 'año_estreno':1967, 'recaudacion':1000000, 'valoracion_publico': 4.5},
    {'titulo': 'avengers end game', 'año_estreno':2017, 'recaudacion':230000, 'valoracion_publico': 4.9},
    {'titulo': 'iron man', 'año_estreno':2014, 'recaudacion':7890000, 'valoracion_publico': 5},
    {'titulo': 'fast and avengers', 'año_estreno':2017, 'recaudacion':4500000, 'valoracion_publico': 3},
    {'titulo': 'ironthor', 'año_estreno':2012, 'recaudacion':2000000, 'valoracion_publico': 5},
    {'titulo': 'avengers infinity war', 'año_estreno':2020, 'recaudacion':120000, 'valoracion_publico': 5}
    ]

# ordenar lista

MIN_MERGE = len(peliculas)


def calcMinRun(n):
    
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r


# This function sorts array from left index to
# to right index which is of size atmost RUN
def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j]["titulo"] < arr[j - 1]["titulo"]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


# Merge function merges the sorted runs
def merge(arr, l, m, r):

    # original array is broken in two parts
    # left and right array
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    i, j, k = 0, 0, l

    # after comparing, we merge those two array
    # in larger sub array
    while i < len1 and j < len2:
        if left[i]["titulo"] <= right[j]["titulo"]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1

        k += 1

    # Copy remaining elements of left, if any
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1

    # Copy remaining element of right, if any
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1



def timSort(arr):
    n = len(arr)
    minRun = calcMinRun(n)

    # Sort individual subarrays of size RUN
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(arr, start, end)

    # Start merging from size RUN (or 32). It will merge
    # to form size 64, then 128, 256 and so on ....
    size = minRun
    while size < n:

        # Pick starting point of left sub array. We
        # are going to merge arr[left..left+size-1]
        # and arr[left+size, left+2*size-1]
        # After every merge, we increase left by 2*size
        for left in range(0, n, 2 * size):

            # Find ending point of left sub array
            # mid+1 is starting point of right sub array
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            # Merge sub array arr[left.....mid] &
            # arr[mid+1....right]
            if mid < right:
                merge(arr, left, mid, right)

        size = 2 * size

timSort(peliculas)

def imprimir_titulo():
    print("tituloo-----")
    for elemento in peliculas:
        
        print( elemento)
imprimir_titulo()



def insertionSortDos(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j]["año_estreno"] < arr[j - 1]["año_estreno"]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


# Merge function merges the sorted runs
def mergeDos(arr, l, m, r):

    # original array is broken in two parts
    # left and right array
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    i, j, k = 0, 0, l

    # after comparing, we merge those two array
    # in larger sub array
    while i < len1 and j < len2:
        if left[i]["año_estreno"] <= right[j]["año_estreno"]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1

        k += 1

    # Copy remaining elements of left, if any
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1

    # Copy remaining element of right, if any
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1



def timSortDos(arr):
    n = len(arr)
    minRun = calcMinRun(n)

    # Sort individual subarrays of size RUN
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSortDos(arr, start, end)

    # Start merging from size RUN (or 32). It will merge
    # to form size 64, then 128, 256 and so on ....
    size = minRun
    while size < n:

        # Pick starting point of left sub array. We
        # are going to merge arr[left..left+size-1]
        # and arr[left+size, left+2*size-1]
        # After every merge, we increase left by 2*size
        for left in range(0, n, 2 * size):

            # Find ending point of left sub array
            # mid+1 is starting point of right sub array
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            # Merge sub array arr[left.....mid] &
            # arr[mid+1....right]
            if mid < right:
                mergeDos(arr, left, mid, right)

        size = 2 * size

timSortDos(peliculas)

def imprimir_year():
    print("lanzamiento----------------")
    for elementoDos in peliculas:
       
        print(elementoDos)
imprimir_year()



# Listar por recaudacion
def insertionSortTres(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j]["recaudacion"] > arr[j - 1]["recaudacion"]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


# Merge function merges the sorted runs
def mergeTres(arr, l, m, r):

    # original array is broken in two parts
    # left and right array
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    i, j, k = 0, 0, l

    # after comparing, we merge those two array
    # in larger sub array
    while i < len1 and j < len2:
        if left[i]["recaudacion"] >= right[j]["recaudacion"]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k]= right[j]
            j += 1

        k += 1

    # Copy remaining elements of left, if any
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1

    # Copy remaining element of right, if any
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1



def timSortTres(arr):
    n = len(arr)
    minRun = calcMinRun(n)

    # Sort individual subarrays of size RUN
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSortTres(arr, start, end)

    # Start merging from size RUN (or 32). It will merge
    # to form size 64, then 128, 256 and so on ....
    size = minRun
    while size < n:

        # Pick starting point of left sub array. We
        # are going to merge arr[left..left+size-1]
        # and arr[left+size, left+2*size-1]
        # After every merge, we increase left by 2*size
        for left in range(0, n, 2 * size):

            # Find ending point of left sub array
            # mid+1 is starting point of right sub array
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            # Merge sub array arr[left.....mid] &
            # arr[mid+1....right]
            if mid < right:
                mergeTres(arr, left, mid, right)

        size = 2 * size

timSortTres(peliculas)



def imprimir_recaudacion():
    print("Recaudacion----------------")
    for x in peliculas:
        print((x))
        
imprimir_recaudacion()

# El de mayor recaudo
print("La pelicula con mas recaudacion fue: ",peliculas[0])

# parte sebas

def secuencialG(lista, buscado):
    
    posicion = -1
    print("peliculas estrenadas en ",buscado,":")
    for i in lista:
        if (i["año_estreno"] == buscado):
            posicion = i
            print(i["titulo"])
    if posicion==-1:
        print("No existe en la lista alguna pelicula que se estrenara en: ",buscado)
        
    return posicion

def secuencialH(lista, buscado):
    
    posicion = -1
    print("peliculas que inician con la palabra ",buscado,":")
    for i in lista:
        palabras=i["titulo"].split(" ")
        if (palabras[0] == buscado):
            posicion = i
            print(i["titulo"])
    if posicion==-1:
        print("No existe en la lista alguna pelicula que inicie con la palabra ",buscado)
        
    return posicion


#punto G
fechaG= 2017
secuencialG(peliculas, fechaG)
print("\n")

#punto H
palabraH="iron"
secuencialH(peliculas,palabraH)
print("\n")


# parte silv


#Return the position of "Stars wars: the return of jedi"----------------------

def secuencial(list, found):
    posicion = -1
    for i in range(0, len(list)):
        if (list[i]["titulo"] == found):
            posicion = i
            print(f'{found} is at the #{i + 1} position')

    if (posicion == -1):
        print("Movie not found.")



print("--------------Print the position of a movie within the list--------------")
finddata = "starwars the return of jedi"
secuencial(peliculas, finddata)


#Return the total amount from the movies by the name including avengers"----------------------

def secuencial1(list, found):
    posicion = -1
    total = 0
    for i in range(0, len(list)):
        if (found in list[i]["titulo"]):
            total+= list[i]["recaudacion"]
            posicion = i
    print("Total earned by the movies including avengers in its name: ", total)

    if (posicion == -1):
        print("Not movie that includes Avengers in it's name has been found.")



findavengers = "avengers"
secuencial1(peliculas, findavengers)

# parte alejo

def secuencialvaloracion(lista, buscado):

    posicion = -1

    for i in range(0, len(lista)):

        if (lista[i]["valoracion_publico"] == buscado):

            print("La pelicula", lista[i]["titulo"], "tiene como valoración: 5")

    return posicion



def secuencialinfinity(lista, buscado):

    posicion = -1

    for i in range(0, len(lista)):

        if (lista[i]["titulo"] == buscado):

            print(lista[i])
    

    return posicion

datobusca = 5

datobusca2 = "avengers infinity war"

secuencialvaloracion(peliculas, datobusca)

secuencialinfinity(peliculas, datobusca2)








