#Amaan Muhammad
#PSID: 1607608

def selection_sort_descend_trace(numbers):
    for i in range(len(numbers)-1):
        ind = i
        for j in range(i + 1, len(numbers)):
            if numbers[ind] < numbers[j]:
                ind = j
        numbers[i], numbers[ind] = numbers[ind], numbers[i]
        for x in numbers:
            print(x,end=" ")
        print()
    return numbers


if __name__ == "__main__":
    # TODO: Read in a list of integers into numbers, then call
    #       selection_sort_descend_trace() to sort the numbers
    numbers = [int(x) for x in input("").split()]
    selection_sort_descend_trace(numbers)
