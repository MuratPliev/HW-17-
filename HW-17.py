def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

def sort_list(arr):
    for i in range(1, len(arr)):
        x = arr[i]
        idx = i
        while idx > 0 and arr[idx-1] > x:
            arr[idx] = arr[idx-1]
            idx -= 1
        arr[idx] = x

if __name__ == "__main__":
    input_sequence = input("Введите последовательность чисел через пробел: ")
    try:
        num_list = [int(num) for num in input_sequence.split()]
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите числа через пробел.")
        exit(1)

    user_num = int(input("Введите число для поиска: "))

    sort_list(num_list)

    position = binary_search(num_list, user_num)

    if position == len(num_list):
        print(f"Число {user_num} должно быть вставлено в конец списка.")
    else:
        print(f"Число {user_num} должно быть вставлено после позиции {position}.")
