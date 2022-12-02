

def selection_sort(nums):
    for i in range(len(nums)):
        minimum = i

        for j in range(i+1, len(nums)):
            if nums[j] < nums[minimum]:
                minimum = j
        nums[minimum], nums[i] = nums[i], nums[minimum]
    return nums


nums = [155, 12, 12313, 21, 10, 1, -22, 65]

print("unsorted list:\n", nums)
print()
print("sorted list:\n", selection_sort(nums))
