# Define a function first_and_last that accepts a list of strings. 
# The function should return a concatenation of the first element 
# and the last element.# Assume the list will always have 1 or 
# more elements.
#
# first_and_last(["a", "b", "c"]) => "ac"
# first_and_last(["bob", "tom", "rob"]) => "bobrob"
# first_and_last(["a"]) => "aa"

def algorithm(collection:list) -> None:
    def first_and_last(collection:list) -> None:
        value = collection[0] + collection[-1]
        return value
    print("collection:", collection, "string:", first_and_last(collection))

algorithm(["a", "b", "c"]) 
algorithm(["bob", "tom", "rob"])
algorithm(["a"]) 

# Define a function product_of_even_indices that accepts a list of numbers. 
# The list will always have 6 total elements. 
# The function should return the product (multiplied total) of all numbers at an even index (0, 2, 4).
#
# product_of_even_indices([1, 2, 3, 4, 5, 6]) # 15
# product_of_even_indices([3, 4, 3, 5, 3, 6]) # 27

def algoirthm2(collection:list) -> None:
    def product_of_even_indices(collection:list) -> None:
        value = collection[0] * collection[2] * collection[4]
        return value
    print("collection", collection, "number:", product_of_even_indices(collection))

algoirthm2([1, 2, 3, 4, 5, 6]) 
algoirthm2([3, 4, 3, 5, 3, 6]) 

# Define a function first_letter_of_last_string that accepts a list of strings. 
# It should return one character — the first letter of the last string in the list. 
# Assume the list will always have at least one string.
#
# first_letter_of_last_string(["cat", "dog", "zebra"]) => "z"
# first_letter_of_last_string(["nonsense"]) => "n"

def algorithm(collection:list) -> None:
    def first_letter_of_last_string(collection:list) -> str:
        value = collection[-1][0]
        return value
    print("The collection's last value's first character is", collection, "and character", first_letter_of_last_string(collection))


algorithm(["cat", "dog", "zebra"])
algorithm(["nonsense"])

# Declare a nested_extraction function that accepts a list of lists and an index position.
# The function should use the index as the basis of finding both the nested list 
# and the element from that list with the given index position
# You can assume the number of lists will always be equal to 
# the number of elements within each of them.

nl = [[3, 4, 5], [7, 8, 9], [10, 11, 12]]

def algorithm2(collection:list, index:int) -> None:
    def nested_extraction(collection:list, index:int):
        value = nl[index][index]
        return value
    print("For the Collection", nl, "and for two indexes", index, ",", index, "the value is",nested_extraction(collection,index))

algorithm2(nl, 0)
algorithm2(nl, 1)
algorithm2(nl, 2) 