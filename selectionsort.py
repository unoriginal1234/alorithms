# Go through an array and find the smallest value
# 
# Put the smallest value into slot one then slot 2, etc.
# place after the last smallest value

List = [6, 2, 7, 9, 1, 5, 5, -12]

n = len(List)

for i in range(0, n - 2):
    small = List[i]
    placeholder = List[i]
    j = i + 1
    while j < n:
        if List[j] < small:
            small = List[j]
            key = j
        j += 1
    List[i] = small
    List[key] = placeholder

        
print(List)
    
    