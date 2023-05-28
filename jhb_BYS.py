def getdata(file):
    fp = open(file, "r")
    type_name = fp.readline().split()
    x = []
    y = []
    while True:
        text = fp.readline()
        if text == "":
            break
        text = text.split()
        x.append(text[:-1])
        y.append(text[-1])
    return type_name,x,y


if __name__ == "__main__":
    typename,x,y = getdata("data_bys.txt")
    dic_listx = []
    dic_y = {}
    list_y = []
    row = len(x)
    col = len(x[0])
    for i in range(col):
        dic_temp = {}
        for j in range(row):
            if x[j][i] not in dic_temp:
                dic_temp[x[j][i]] = 1
            else:
                dic_temp[x[j][i]] += 1
        dic_listx.append(dic_temp)
    for i in range(row):
        if y[i] not in dic_y:
            dic_y[y[i]] = 1
        else:
            dic_y[y[i]] += 1
    for i in dic_y:
        list_y.append(i)
    dic_plist = []
    lentype = len(dic_y)
    for one in dic_listx:
        dic_temp = {}
        for key in one:
            val_temp = {}
            for i in range(lentype):
                val_temp[list_y[i]] = 0
            dic_temp[key] = val_temp
        dic_plist.append(dic_temp)
    for i in range(col):
        for j in range(row):
            dic_plist[i][x[j][i]][y[j]] += 1
    target = ['3', 'L']
    key_target = 'none'
    maxp = 0
    allp = 0
    for i in range(lentype):
        p = 1
        p_y = dic_y[list_y[i]] / row
        for j in range(col):
            px_y = dic_plist[j][target[j]][list_y[i]] / dic_y[list_y[i]]
            p_x = dic_listx[j][target[j]] / row
            p *= px_y / p_x
        p *= p_y
        allp += p
        if p > maxp:
            maxp = p
            key_target = list_y[i]
    print("预测结果为%s,概率为%.2f%%" % (key_target, maxp * 100 / allp))