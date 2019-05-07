(loc, path)
visited=set()
while q:
    loc,path = q.popleft()
    if loc==tar:
        return path
    for nei in loc:
        if nei not in visited:
            q.push((nei, path+[nei]))