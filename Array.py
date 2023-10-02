def solution(a, k):
    remainder_counts = {}
    count = 0
    
    for num in a:
        remainder = num % k
        if remainder in remainder_counts:
            count += remainder_counts[remainder]
        complement = (k - remainder) % k
        if complement in remainder_counts:
            remainder_counts[complement] += 1
        else:
            remainder_counts[complement] = 1
    
    return count
    '''       
    return sum([1 for x in range(len(a)) for y in range(x+1,len(a)) if (a[x]+a[y])%k==0])'''
