# finish the function
def find_the_parent(child):
    if issubclass(child, Drinks):
        print('Drinks')
    elif issubclass(child, Pastry):
        print('Pastry')
    elif issubclass(child, Sweets):
        print('Sweets')

    # Solution by Pablo Z
    # classes = [Drinks, Pastry, Sweets]
    # for cl in classes:
    #     if issubclass(child, cl):
    #         print(cl.__name__)
