

def selection_sort(lst):
    """ Return a copy of lst with its elements in sorted order.
    Pre: lst is not empty and contains only numbers.
    Post: lst is empty and the returned list has the same values but sorted.
    """
    
    
    result = []
    
    while len(lst) > 0:
        min_v = lst[0]
        min_i = 0
        for i, v in enumerate(lst):
            if v < min_v:
                min_v = v
                min_i = i
        result.append(lst[min_i])
        lst.remove(min_v)
    
    return(result)
        
def bubble_sort(lst):
    """ Sort lst in place.
    Pre: lst is not empty and contains only numbers. """
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swapped = True
    
        
    