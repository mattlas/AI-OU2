import sys,random

# 1: Happy 2: Sad 3: Mischievous 4: Angry

moods = 4

def readData(filename):
    dataFile = open(filename, "r")

    array = []
    for lines in dataFile:
        if (lines.startswith('#') == False and lines.startswith('Image')):
            values = lines.split(' ')
            array.append(int(values[1]))

    dataFile.close()
    return array

def readImage(filename):
    imageFile = open(filename, "r")
    images = []
    image = []
    n = 0

    for line in imageFile:
        if (line.startswith('#') == False and line.startswith('Image') == False and line.isspace() == False):
            values = line.split(' ')
            row = []
            for value in values:
                num = int(value.rstrip())
                row.append(num)
            n += 1
            image.append(row)
            if n == 20:
                image = rotateImage(image)
                images.append(image)
                image = []
                n = 0

    imageFile.close()
    return images

def rotateImage(image):
    topSum = bottomSum = leftSum = rightSum = 0;

    #top sum
    for row in range(0,10):
        for col in range(0,20):
            topSum += (image[row][col])

    #right sum
    for row in range(0,20):
        for col in range(10,20):
            rightSum += (image[row][col])

    #bottom sum
    for row in range(10,20):
        for col in range(0,20):
            bottomSum += (image[row][col])

    #left sum
    for row in range(0,20):
        for col in range(0,10):
            leftSum += (image[row][col])

    sums = [topSum,rightSum,bottomSum,leftSum]
    ind = sums.index(max(sums))
    if ind == 1:
        return rotate(rotate(rotate(image)))
    elif ind == 2:
        return rotate(rotate(image))
    elif ind == 3:
        return rotate(image)
    return image

def rotate(image):
    rotatedImage = []
    for col in range(0,20):
        row = 19
        rotated = []
        for i in range(0, 20):
            rotated.append(image[row][col])
            row -= 1
        rotatedImage.append(rotated)
    return rotatedImage

def pprint(images):
    i = 1
    for image in images:
        print "Image " + str(i)
        for row in image:
            print row
        print ""
        i = i + 1

    return

def printFacit(facit):
    i = 1
    for ans in facit:
        print "Answer " + str(i) + ": " + str(ans)
        print ""
        i = i + 1
    return

def generateWeights():
    weights = []
    for i in range(0,moods):
        randomValues = []
        for j in range(0,400):
            randomValue = random.uniform(-0.1,0.1)
            randomValues.append(randomValue)

        weights.append(randomValues)
    return weights

def train(images,facit, weights):
    avgError = 0
    alpha = 0.1
    for mood in range(0,moods):
        w = weights[mood]
        errorSum = 0
        for image in range(0, len(images)):

            nodeValue = 0

            if(facit[image] == mood + 1):
                desiredOutput = 1
            else:
                desiredOutput = -1

            i = 0
            for row in images[image]:
                for value in row:
                    nodeValue += value * w[i]
                    i += 1

            if nodeValue > 0:
                nodeValue = 1
            else:
                nodeValue = -1

            error = desiredOutput - nodeValue
            errorSum += abs(error)

            i = 0
            for row in images[image]:
                for value in row:
                    delta = alpha * error * value
                    w[i] += delta
                    i += 1

        weights[mood] = w
        avgError += errorSum
        avgError = avgError
    return weights, avgError

if __name__ == '__main__':
    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv)

    training_filename = sys.argv[1]
    training_facit_filename = sys.argv[2]

    training_array = readImage(training_filename)
    facit_array = readData(training_facit_filename)

    weights = generateWeights()

    for i in range(0, 10):
        weights, avgError = train(training_array,facit_array, weights)
        #print(avgError)
