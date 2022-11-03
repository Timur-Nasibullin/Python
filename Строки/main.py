str = input()
# split() функция, разделяющая строку по пробелам
# [...] генератор
nums = [int(i) for i in str.split()]
print(max(nums))
imax = 0
imin = 0
for i in range(len(nums)):
    if nums[i] > nums[imax]:
        imax = i
    if nums[i] < nums[imin]:
        imin = i
# Обмен местами двух переменных
nums[imax], nums[imin] = nums[imin], nums[imax]
print(nums)