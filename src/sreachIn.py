import sys

def wrapData(data):
    wasChecked = {}
    if data == None:
        return None
    for e in data:
        if e in wasChecked:
            wasChecked[e] += 1
        else:
            wasChecked[e] = 1
    print(wasChecked)
    return wasChecked

def checkData(data,n):
    checkedData = []
    for i in data:
        if data[i] == n:
            checkedData.append(i)
    return checkedData

def main():
    data = [1,1,1,2,2,2,3,1]
    n = None
    data2 = []

    wdata = wrapData(data)
    print(checkData(wdata,n))

    return 0

if __name__ == '__main__':
    sys.exit(main())
    pass
