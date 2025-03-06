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
    ordenado = False
    if element_2 < element_1:
        ordenado = True
    return ordenado

def selection_sort(my_list, sort_criteria):
    tamano = size(my_list)

    for i in range(tamano):
        menor = get_element(my_list, i)
        f = 1 + i
        pos_menor = i
        while f < tamano:
            sort_criteria = default_sort_criteria(menor, get_element(my_list, f))
            if sort_criteria == True:
                menor = get_element(my_list, f)
                pos_menor = f
            f += 1
        exchange(my_list, i, pos_menor)
    
    return my_list

def insertion_sort(my_list, sort_crit):
    tamano = size(my_list)
    for i in range(tamano):
        f = i - 1
        x = i
        while f > -1:
            sort_crit = default_sort_criteria(get_element(my_list, x), get_element(my_list,f))
            if sort_crit == True:
                exchange(my_list, x, f)
                x -= 1
            else:
                f = -1
            f -= 1

    return my_list

def shell_sort(my_list, sort_crit):
    pass