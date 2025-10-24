import argparse


def insertion_sort(arr, length):
    print("Sorting array using Insertion Sort...")
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
