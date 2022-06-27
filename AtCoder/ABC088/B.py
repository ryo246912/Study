N = int(input())
card = list(map(int,input().split()))
card_sort = sorted(card,reverse=True)

alice = sum([ x for i, x in enumerate(card_sort) if i % 2 == 0 ])
bob = sum([ x for i, x in enumerate(card_sort) if i % 2 == 1 ])

print(alice - bob)