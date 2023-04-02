num=[1,2,3,4]
ordered=sorted(num)
n=len(ordered)
for i in range(n-1):
    if ordered[i]==ordered[i+1]:
        print('true')
        break
    else:
        print('false')
        break
