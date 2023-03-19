# 211RDB475 Kristofers Zellītis 9.grupa


def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n//2, -1, -1):
        swaps = heap_sort(data, i, swaps)
    return swaps

def heap_sort(data, i, swaps):
    n = len(data)
    min_index = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and data[l] < data[min_index]:
        min_index = l
    if r < n and data[r] < data[min_index]:
        min_index = r
    if i != min_index:
        data[i], data[min_index] = data[min_index], data[i]
        swaps.append((i, min_index))
        swaps = heap_sort(data, min_index, swaps)
    return swaps



def main():
    mode = input("Enter F (for file) or I (for input): ").strip()
    if "I" in mode:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n

    # input from file
    elif "F" in mode:
        filename = input("Enter file name: ")
        with open (f"tests/{filename}") as f:
            n = int(f.readline().strip())
            data = list(map(int, f.readline().strip().split()))

            # checks if length of data is the same as the said length
            assert len(data) == n

    else:
        print("Error. Try again")
        return

    swaps = build_heap(data)

    for i in range(n//2):
        if 2*i+1 < n and data[i] > data[2*i+1]:
            print("Error. Not satisfied")
            return

        if 2*i+2 < n and data[i] > data[2*i+2]:
            print("Error: Not satisfied")
            return

    print(len(swaps))

    for i, j in swaps:
        print(i, j)



if __name__ == "__main__":
    main()