from pynamodb.pagination import ResultIterator

# Not used but left it in
def scancount(scanResult):
    c = 0
    for sr in scanResult:
        c+=1
    
    return c 