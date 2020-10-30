# Define a sum_of_lengths function that accepts a list of strings.
# The function should return the sum of the string lengths.
#
# sum_of_lengths(["Hello", "Bob"]) => 8
# sum_of_lengths(["Nonsense"])     => 8
# sum_of_lengths(["Nonsense", "or", "confidence"]) => 20

def algorithm( collection:list ) -> None:
    def sum_of_lengths(collection:list) -> None:
        result = 0
        for item in collection:
           result += len(item)
        return result
    print("For the List the size of all the strings is", sum_of_lengths(collection))
    

algorithm(["Hello", "Bob"]) 
algorithm(["Nonsense"])     
algorithm(["Nonsense", "or", "confidence"])

# Define a product function that accepts a list of numbers.
# The function should return the product of the numbers.
# The list will always have at least one value
#
# product([1, 2, 3]) => 6
# product([4, 5, 6, 7]) => 840
# product([10]) => 10

def algorithm2( collection:list) -> None:
    def product(collection:list) -> int:
        value = 1
        for item in collection:
            value *= item
        return value
    print("All values of the list multipied together produce", product(collection))


algorithm2([1, 2, 3]) 
algorithm2([4, 5, 6, 7]) 
algorithm2([10])

# Define a smallest_number function  that accepts a list of numbers.
# It should return the smallest value in the list.

# smallest_number([1, 2, 3])     => 1
# smallest_number([3, 2, 1])     => 1
# smallest_number([4, 5, 4])     => 4
# smallest_number([-3, -2, -1])  => -3

def algorithm3(collection:list) -> None:
    def smallest_number(collection:list) -> None:
        smallest_number = collection[0]
        for item in collection:
            if ( item < smallest_number):
                smallest_number = 1
        return smallest_number
    print("The smallest number of the list is ", smallest_number(collection))

algorithm3([1, 2, 3])  
algorithm3([3, 2, 1])     
algorithm3([4, 5, 4])     
algorithm3([-3, -2, -1])  