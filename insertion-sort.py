import argparse


def insertion_sort(arr, length):
    print("Sorting array using Insertion Sort...")
    
    if(length <= 1):
        return arr

    for index in range(1, length):
        # Select the element to be positioned
        key = arr[index]

        prevIndex = index - 1
        # Ascending order : sort the element into its correct position 
        while prevIndex >= 0 and key > arr[prevIndex]:
            arr[prevIndex + 1] = arr[prevIndex]
            prevIndex = prevIndex -1
            # print("Current array state:", arr)
        arr[prevIndex + 1] = key
    return arr


if __name__ == "__main__":
    print("Insertion Sort Implementation")
    parser = argparse.ArgumentParser(description="Insertion Sort Algorithm")
    parser.add_argument("--elements", nargs="*", type=int, help="List of integers to sort")
    args = parser.parse_args()
    elements = args.elements
    print("Original array:", elements)
    sorted_array = insertion_sort(elements, len(elements))
    print("Sorted array:", sorted_array)
