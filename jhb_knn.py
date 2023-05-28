import os

def accdiff(str1, str2):
    lens = len(str1)
    count = 0
    for i in range(lens):
        if str1[i] != str2[i]:
            count += 1
    return count


patht = 'C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\testDigits\\'
pathl = 'C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\trainingDigits\\'

test_number = os.listdir(patht)
learn_number = os.listdir(pathl)

class Image:
    def __init__(self,matrix,tag):
        self.matrix = matrix
        self.tag = tag

imageList = []

for file in learn_number:
    fp = open(pathl + file, "r")
    str = fp.read().strip()
    images = Image(str, file[0])
    imageList.append(images)
    fp.close()


right = 0
wrong = 0

for file in test_number:
    fp = open(patht + file, "r")
    str = fp.read().strip()
    minn = [[10005,file[0]], [10005,file[0]], [10005,file[0]]]
    for obj in imageList:
        diff = accdiff(str, obj.matrix)
        if diff < minn[0][0]:
            minn[2] = minn[1]
            minn[1] = minn[0]
            minn[0] = [diff, obj.tag]
        elif diff < minn[1][0]:
            minn[2] = minn[1]
            minn[1] = [diff, obj.tag]
        elif diff < minn[2][0]:
            minn[2] = [diff, obj.tag]
    a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    tag = int(minn[0][1])
    for x in minn:
        a[int(x[1])] += 1
    for i in range(0, 10):
        if a[i] > 1:
            tag = i
            break
    if tag != int(file[0]):
        wrong += 1
        print("Wrong Answer")
    else:
        right += 1
        print("Accept")
    fp.close()

print("总识别成功率%.2f" % (right / (right + wrong) * 100),end = "%\n")



