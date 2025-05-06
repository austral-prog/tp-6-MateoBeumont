# Replace the "ANSWER HERE" with your answer
def remove_elements(list_to_remove_elements):
	del list_to_remove_elements[5]
	del list_to_remove_elements[4]
	del list_to_remove_elements[0]
	return list_to_remove_elements

def add_elements(list_to_add_elements):
	list_to_add_elements.insert(0, "Pink")
	list_to_add_elements.append("Yellow")
	return list_to_add_elements

def is_empty(list_to_check):
	return len(list_to_check) == 0
		
def check_lists(list_to_compare1, list_to_compare2):
	if len(list_to_compare1) >= 3 and len(list_to_compare2) >= 3
		return list_to_compare1[2] == list_to_compare2[2]:
	return false

def list_of_lists(list_of_lists_to_modify):
    if len(list_of_lists_to_modify[0]) < 3:
        paso_3 = list_of_lists_to_modify[0]
    else:
        paso_3 = list_of_lists_to_modify[0][0:2]

    if len(list_of_lists_to_modify[1]) < 5:
        if len(list_of_lists_to_modify[1]) >= 2:
            paso_2 = list_of_lists_to_modify[1][1:]
        else:
            paso_2 = []
    else:
        paso_2 = list_of_lists_to_modify[1][1:4]

    if len(list_of_lists_to_modify[2]) < 3:
        paso_1 = list_of_lists_to_modify[2]
    else:
        paso_1 = list_of_lists_to_modify[2][-2:]

    return [paso_3, paso_2, paso_1]
