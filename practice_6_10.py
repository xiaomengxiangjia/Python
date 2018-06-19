nums = {
    'bin': [2,3,4], 'fu': [4,5,6], 'li': [1,3,5], 'xiang': [8,9,7]
}
for name,numbers in nums.items():
    print(name.title() + "'s favorite number is: ")
    for number in numbers:
        print(number)

