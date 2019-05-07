def Kruskal(edges):
    # union find
    p={}
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]
    def union(x,y):
        p[find(x)] = find(y)

    ans=set()
    edges.sort()
    for e in edges:
        u,v = e.vertices
        if find(u) != find(v):
            ans.add(e)
            union(u,v)