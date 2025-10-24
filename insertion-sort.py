import argparse


def insertion_sort(arr, length):
    print("Sorting array using Insertion Sort...")
    print("Original array:", arr)
    



if __name__ == "__main__":
    print("Insertion Sort Implementation")
    parser = argparse.ArgumentParser(description="Insertion Sort Algorithm")
    parser.add_argument("--elements", nargs="*", type=int, help="List of integers to sort")
    args = parser.parse_args()
    elements = args.elements
    insertion_sort(elements, len(elements))