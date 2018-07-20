def insert_operation(n, data):
    numbers = data[:n]
    op_num = data[n:]
    [number*op_num for number in numbers]

    max = 0
    min = 0
    return (max, min)

n = 2
data = [5,6,0,0,1,0]

print(insert_operation(n,data))