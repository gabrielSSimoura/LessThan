# Take a list, say for example this one:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# Extras:

# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.


def getLessThan5(list_of_integers, limitNumber):
    lessThanLimit = []
    for item in list_of_integers:
        if (item < limitNumber):
            lessThanLimit.append(item)

    return lessThanLimit


def main():
    userList = input("Digite uma lista de numeros: ")
    limitNumber = int(input(
        "Digite um numero para selecionar os menores que ele da lista acima: "))

    userList = userList.split()
    map_object = map(int, userList)
    list_of_integers = list(map_object)

    list_of_integers = getLessThan5(list_of_integers, limitNumber)
    print("Numeros menores que " + str(limitNumber) +
          "sao " + str(list_of_integers))


main()
