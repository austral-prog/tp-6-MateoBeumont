# Replace the "ANSWER HERE" with your answer
def remove_elements(lst):
    indices_to_remove = [0, 4, 5]  # primer, quinto y sexto elemento
    # Crear una nueva lista ignorando los índices a eliminar
    return [item for idx, item in enumerate(lst) if idx not in indices_to_remove]

# 2. add_elements
def add_elements(lst):
    return ['Pink'] + lst + ['Yellow']

# 3. is_empty
def is_empty(lst):
    return len(lst) == 0

# 4. check_lists
def check_lists(lst1, lst2):
    if len(lst1) >= 3 and len(lst2) >= 3:
        return lst1[2] == lst2[2]
    return False

# 5. list_of_lists
def list_of_lists(lst):
    result = []
    if len(lst) >= 1:
        result.append(lst[0][:2])
    if len(lst) >= 2:
        result.append(lst[1][1:4])
    if len(lst) >= 3:
        result.append(lst[2][-2:])
    return result
