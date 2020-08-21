def find_sum(limit):
    limit*=limit
    num=1
    add=2
    result=1
    while num<limit:
        for i in range(4):
            num+=add
            result+=num
        add+=2
    return result


print (find_sum(1001))

  