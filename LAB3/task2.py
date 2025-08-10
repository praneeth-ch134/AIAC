def get_and_sort_numbers():
    try:
        nums_input = input("Enter numbers separated by spaces: ")
        nums = [float(num) for num in nums_input.strip().split()]
        sorted_nums = sorted(nums)
        print("Numbers in sorted order:", sorted_nums)
        return sorted_nums
    except ValueError:
        print("Invalid input. Please enter only numbers separated by spaces.")
        return []

if __name__ == "__main__":
    get_and_sort_numbers()
