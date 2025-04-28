# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
	x = del list_to_remove_elements[0]
	y = del x[4]
	z = del y[5]
	return z

def add_elements(list_to_add_elements):
	x = list_to_add_elements.insert(0, "pink")
	y = x.append("yellow")
	return y
	
def is_empty(list_to_check):
	if list_to_check == []:
		rta = "True"
	else:
		rta = "False"
	return rta

def check_lists(list_to_compare1, list_to_compare2):
	if list_to_compare1[2] == list_to_compare2[2]:
		rta = "True"
	else: 
		rta = "False"

def list_of_lists(list_of_lists_to_modify):
	x = list_of_lists_to_modify[0][0:2]
	y = x[1][1:4]
	z = y[3][0:2:-1]
	return z
