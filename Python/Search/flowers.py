NK = input()

N = int(NK.partition(' ')[0])
K = int(NK.partition(' ')[2])

prices = [int(x) for x in input().strip().split(' ')]

if K == N:
    print(sum(prices))
else:
    prices.sort()
    friends = [[] for friend in range(K)]
    
    for friend in friends:
        friend.append(prices.pop())
    
    index = 0
    while prices:
        friends[index].append(prices.pop()*(1+len(friends[index])))
        index = (index + 1)%K
        
    total = 0
    for friend in friends:
        total += sum(friend)
        
    print(total)