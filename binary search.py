def rightmost(a,x):
    l=0
    h=len(a)-1
    while l<h:
        m = (l+h)//2 # close to l
        if a[m]>=x:
            h=m # not missing a[m]==x
        else:
            l=m+1 # avoid m,l stuck
    return h
def leftmost(a,x):
    l=0
    h=len(a)-1
    while l<h:
        m = (l+h+1)//2 # close to h
        if a[m]>x:
            h=m-1 # avoid m,l stuck
        else:
            l=m # not missing a[m]==x
    return l

if __name__ == '__main__':
    import bisect
    
    for a in [[1,2,3,4,5,6], [3,4], [3], [4]]:
        for x in 0, 1, 3,3.5, 4,5:
            print(a,x)
            print(bisect.bisect_left(a,x), leftmost(a,x))
            print(bisect.bisect_right(a,x), rightmost(a,x))