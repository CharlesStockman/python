# Declare a  delete_keys function that accepts two arguments: a dictionary 
# and a list of strings. 
# For each string in the list, if the string exists as a dictionary key, 
# delete the key-value pair from the dictionary. 
#
# If the string does not exist as a dictionary key, avoid an error. 
# The return value should be the modified dictionary object.
#
# my_dict = {
#   "A": 1,
#   "B": 2,
#   "C": 3
# }
#
# strings = ["A", "C"]
# delete_keys(my_dict, strings) => {'B': 2}

def algorithm(map:dict, strings:str) -> None:
    def delete_keys(map:dict, strings:str) -> dict:
        for string in strings:
            if string in map:
                del map[string]
        return map
    print("By removing the key found in the string array the new map is ", delete_keys(map, strings))

my_dict = {"A": 1, "B": 2, "C": 3 }
strings = ["A", "C"]
algorithm(my_dict, strings)