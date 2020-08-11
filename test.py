

nk = input().split()
n = int(nk[0])
k = int(nk[1])
arr=list(map(int,input().split()))
arr.sort()
count=0
for i in range(n):

    if (i==0):
        if(arr[i+1]-arr[i]<=k):
            count+=1
    elif(i!=0 and i<n-1):
        if(arr[i+1]-arr[i]<=k or arr[i]-arr[i-1]<=k):
            count+=1
    elif(i==n-1):
        if(arr[i]-arr[i-1]<=k):
            count+=1
print(count)
        