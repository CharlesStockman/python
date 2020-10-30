# Define a same_first_and_last_letter function that accepts a string as an argument. 
# The function should return a True if the first and last character are equal, and False otherwise
# Assume the string will always have 1 or more characters.
#
# EXAMPLES:
# same_first_and_last_letter("runner") => True
# same_first_and_last_letter("Runner") => False
# same_first_and_last_letter("clock")  => False
# same_first_and_last_letter("q")      => True

def algorithm(input:str) -> None:
    def same_first_and_last_letter(input:str) -> bool:
        return(input[0] == input[-1])
    print("For", input, "are first and last character the same", same_first_and_last_letter(input))

algorithm("runner") 
algorithm("Runner")  
algorithm("clock")   
algorithm("q")    

# Define a three_number_sum function that accepts a 3-character string as an argument. 
# The function should add up the sum of the digits of the string. 
# HINT: You’ll have to figure out a way to convert the string-ified numbers to integers.
#
# EXAMPLES:
# three_number_sum("123") => 6
# three_number_sum("567") => 18
# three_number_sum("444") => 12
# three_number_sum("000") => 0

def algorithm2(numbers:str) -> None:
    def sum(numberString:str) -> int:
        result = int(numberString[0]) + int(numberString[1]) + int(numberString[2])
        return result
    print("The sum of", str, "=", sum(numbers))

algorithm2("123")
algorithm2("567")
algorithm2("444")
algorithm2("000")


