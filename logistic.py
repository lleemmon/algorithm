import numpy as np

def getdata(file):
    fp = open(file, "r")
    x = []
    y = []
    while True:
        text = fp.readline()
        if text == "":
            break
        text = text.strip().split()
        tempx = [1]
        lenx = len(text) - 1
        for i in range(lenx):
            tempx.append(int(text[i]))
        x.append(tempx)
        tempy = [0, 0]
        tempy[int(text[lenx])] += 1
        y.append(tempy)
    return x, y

def softmax(z):#H
    H = []
    for i in z:#每一行
        temp = []
        sums = sum(np.exp(i))
        for j in i:
            temp.append(np.exp(j)/sums)
        H.append(temp)
    return H

def logistic(x, y, counts, learning_rate):
    w = np.array(np.random.rand(len(y[0]),len(x[0])))#两行三列
    for i in range(counts):
        z = np.dot(x, w.T)
        H = softmax(z)
        w -= learning_rate * np.dot((H - y).T, x)
    return w


if __name__ == "__main__":
    x, y = getdata("logisticData.txt")
    x = np.array(x)
    y = np.array(y)
    w = logistic(x,y,10000, 0.1)
    H = softmax(np.dot(x, w.T))
    for h in H:
        print(h)#列表中哪个的值大，就说明应该被分为什么类别