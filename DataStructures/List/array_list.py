def new_list():
    new_list = {"elements": [],
                "size": 0,
                }
    return new_list

def get_element(my_list, index):
    return my_list["elements"][index]

def is_present(my_list, element, cmp_function):
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def add_first(my_list, element):
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list

def size(my_list):
    return my_list["size"]

def first_element(my_list):
    return my_list["elements"][0]

def is_empty(my_list):
    return my_list["size"] == 0

def get_fist_element(my_list):
    return my_list["elements"][0]

def insert_element(my_list, element, index):
    my_list["elements"].insert(index, element)
    my_list["size"] += 1
    return my_list

def delete_element(my_list, index):
    if my_list["size"] > 0:
        my_list["elements"].pop(index)
        my_list["size"] -= 1
    return my_list

def change_info(my_list, index, element):
    my_list["elements"][index] = element
    return my_list

def exchange(my_list, pos1, pos2):
    temp = my_list["elements"][pos1]
    my_list["elements"][pos1] = my_list["elements"][pos2]
    my_list["elements"][pos2] = temp
    return my_list

def sub_list(my_list, start, num_elements):
    sublist = new_list()
    if start > num_elements:
        raise Exception('IndexError: list index out of range')
    else: 
        for i in range(start, num_elements):
            add_last(sublist, my_list["elements"][i])
        return sublist
    


def remove_last(my_list):
    if my_list["size"] == 0:
        raise Exception('IndexError: list index out of range')
    else: 
        elementos = my_list["elements"]
        size = my_list["size"]
        elemento = elementos[size-1]
        del elementos[size-1]
        my_list["size"] -= 1
        return elemento
    
def remove_first(my_list):
    if my_list["size"] == 0:
        raise Exception('IndexError: list index out of range')
    else: 
        elementos = my_list["elements"]
        elemento = elementos[0]
        my_list["size"] -= 1
        del elementos[0]
        return elemento
    

#Laboraorio 5: Funciones de ordenamiento con array list

def default_sort_criteria(element_1, element_2):
    if element_1 > element_2:
        return 1
    
    elif element_1 < element_2:
        return 2
    
    else:
        return 3

def selection_sort(my_list, sort_criteria):
    tamano = size(my_list)
    
    if tamano <= 1:
        result = my_list

    else: 

        for i in range(tamano):
            menor = get_element(my_list, i)
            f = 1 + i
            pos_menor = i
            while f < tamano:
                sort = sort_criteria(get_element(my_list, f),menor)# pedro edita esto con base al nuevo sort criteria
                if sort == True:
                    menor = get_element(my_list, f)
                    pos_menor = f

                f += 1
            exchange(my_list, i, pos_menor)
        
        result = my_list
    
    return result

def insertion_sort(my_list, sort_crit):
    tamano = size(my_list)

    if tamano <= 1:
        result = my_list

    else:
        for i in range(tamano):
            f = i - 1
            x = i
            while f > -1:
                sort = sort_crit(get_element(my_list, x), get_element(my_list,f))# lo mismo pq la f me confunde xddd
                if sort == True:
                    exchange(my_list, x, f)
                    x -= 1
                else:
                    f = -1
                f -= 1
        result = my_list

    return result

def shell_sort(my_list, sort_crit):
    n = size(my_list)

    if n <= 1:
        result = my_list

    else:

        gap = n // 2

        while gap > 0:

            for i in range(gap, n):
                elem = get_element(my_list, i)
                j = i

                while j >= gap and sort_crit(elem, get_element(my_list, j - gap)) == 2:

                    exchange(my_list, j, j-gap)
                    j -= gap

            gap = gap // 2

        result = my_list

    return result




def merge_sort(my_list, sort_crit):

    if size(my_list) == 0 or size(my_list) == 1:
        return my_list

    n = size(my_list)
    m = n // 2

    sub1 = sub_list(my_list, 0, m)
    sub1 = merge_sort(sub1, sort_crit)

    sub2 = new_list()
    if n % 2 != 0:
        sub2 = sub_list(my_list, m, m+1)

    else:
        sub2 = sub_list(my_list, m, m)

    sub2 = merge_sort(sub2, sort_crit)

    return merge(sub1,sub2, sort_crit)

def merge(lista1, lista2, sort_crit):
    lista = new_list

    i = 0 
    j = 0 

    while i < size(lista1) or j < size(lista2):

        sort = sort_crit(get_element(lista1, i), get_element(lista2, j))

        if sort == 1:
            add_last(lista, get_element(lista2, j))
          

        elif sort == 2:
            add_last(lista, get_element(lista1, i))
            
        else:
            add_last(lista, get_element(lista1, i))
  

        

    return lista




def partition(arr, low, high):

    pivot = get_element(arr,high)

    i = low - 1

    for j in range(low, high):
        if get_element(arr,j) < pivot:
            i += 1
            exchange(arr, i, j)
    
    exchange(arr, i + 1, high)
    return i + 1



def quickSort(arr, low, high, sort_crit):
    if sort_crit(low, high) == 2:
        
        pi = partition(arr, low, high)
        
        quickSort(arr, low, pi - 1,sort_crit)
        quickSort(arr, pi + 1, high,sort_crit)

