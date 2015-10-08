import sys

def readFile(filename):
    with open(filename) as f:
        data = f.readlines()

    array = []


    for lines in data:
        if not (lines.startswith('#')):
            array.append(lines.strip('\n'))
    del array[0]
    return array



if __name__ == '__main__':

    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv)

    training_filename = sys.argv[1]
    training_facit_filename = sys.argv[2]

    training_array = readFile(training_filename)
    facit_array = readFile(training_facit_filename)