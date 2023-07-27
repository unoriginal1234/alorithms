# Go through an array and find the smallest value
# 
# Put the smallest value into slot one then slot 2, etc.
# place after the last smallest value

# List = [12, 653, 245, -13, .2, 999, 1, -.01, 25]
List = [23, 53, -1, .87, 23423, -123, 234.5, 23, 23, 23, 17, 23, 23]

n = len(List)

# for i in range(0, n - 1):
#     small = List[i]
#     placeholder = List[i]
#     j = i + 1
#     while j < n:
#         if List[j] < small:
#             small = List[j]
#             key = j
#         j += 1
#     List[i] = small
#     List[key] = placeholder

for i in range(n):
    small = List[i]
    key = i
    j = i + 1
    while j < n:
        if List[j] < small:
            small = List[j]
            key = j
        j += 1
    List[key] = List[i]
    List[i] = small

        
print(List)
    
    