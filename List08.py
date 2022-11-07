def main(fruits):
    """
    A list called "fruits" is given and is five in length and contains at least one "apple". Remove the apples from the list and return the list.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    i = 0
    n = 0
 
    while i<len(fruits):
        if fruits[i]=="apple":

         n = fruits.pop(i)
         i+=1
    return fruits

   
print(main(["apple", "banana", "apple", "pear", "apple"]))   