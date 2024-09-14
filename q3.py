global_variable = 100
my_dict = {'ke11': 'value1', 'ke12': 'value2', 'ke13': 'value3'}

def process_numbers():
    global global_variable
    local_variable = 5
    numbers = [1, 2, 3, 4, 5]
    
    while local_variable > 0:
        if local_variable % 2 == 0:  # Check if local variable is even
            if local_variable in numbers:
                numbers.remove(local_variable)
            local_variable -= 1
            return numbers
        
        # Define my_set inside the loop scope
        my_set = {1, 2, 3, 4, 5}
        
        # No need to call process_numbers() recursively here, it's handled internally
        # Call modify_dict() to update the dictionary
        modify_dict()
        
    return numbers

def modify_dict():
    local_variable = 10
    my_dict['ke14'] = local_variable  # Add a new key 'ke14' with value 10
    
    # Call the update_global function
    update_global()

def update_global():
    global global_variable
    global_variable += 10  # Increment global_variable by 10
    
    for i in range(5):
        print(i)  # Print the current value of i

    # Define my_set in this function scope
    my_set = {1, 2, 3, 4, 5}
    
    if my_set is not None and my_dict.get('ke14') == 10:
        # Check condition on my_set and my_dict
        print("Condition met!")
        
        if 5 not in my_dict:  # Check if 5 is not a key in my_dict
            print("5 not found in the dictionary!")
            # Print the values of global_variable, my_dict, and my_set
            print(global_variable)
            print(my_dict)
            print(my_set)
            
            # Call update_global() to run the code
            # Be cautious: This can lead to infinite recursion if not controlled
            # Commenting out the recursive call to prevent infinite loop
            # update_global()

# Example call to initiate the process
print("Result of process_numbers():", process_numbers())
