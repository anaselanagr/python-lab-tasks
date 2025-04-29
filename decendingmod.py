def sort_numbers():
    anas = []
    for i in range(5):
        num = int(input("Enter your 5 numbers: "))  # Convert input to integer
        anas.append(num)

    asend = sorted(anas)
    descesnd = sorted(anas, reverse=True)

    return asend, descesnd

asend, descesnd = sort_numbers()
print("Sorted in ascending order:", asend)
print("Sorted in descending order:", descesnd)
