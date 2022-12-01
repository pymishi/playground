from functools import reduce

def product_between_numbers(listNumbers, numbers, high):

    # Sort List ASC/DESC
    listNumbers.sort(reverse=high)

    # Calculate the product from the list between the numbers parameter
    product = reduce(lambda x, y: x*y, listNumbers[0:numbers])

    return product

listNumbers = [1, 10, 2, 6, 5, 3]

product = product_between_numbers(listNumbers, 3, True)

print(product)