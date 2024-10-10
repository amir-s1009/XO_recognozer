import json

def train(x_vector, label):

    def encode_label(label):
        # 1 for x and -1 for o
        label = label.lower()
        if label == 'x':
            return 1
        elif label == 'o':
            return -1
        else:
            raise ValueError('please select a valid label among x or o')

    file = None
    
    try:
        
        # read weights and bias from file:
        file = open('weights.txt', 'r')
        result = file.readline()
        result = json.loads(result)     #{'weights':[[]], 'bias':number}
        file.close()

        weights = result['weights']
        bias = result['bias']

        y = encode_label(label)

        #iterate over all of neurons and update weights & bias:

        for i in range(len(weights)):
            for j in range(len(weights[0])):
                weights[i][j] = weights[i][j] + (x_vector[i][j]*y)
        bias = bias + y

        # end of updating weights & bias

        # store the weights and bias:
        file = open("weights.txt", "w")
        file.write(json.dumps({"weights":weights, "bias":bias}))
        file.close()

        print('training successful!')

    except ValueError as err:
        if err:
            print(err)
        else:
            print('An unExpected error occured!')

    finally:
        if file:
            file.close()


def test(test_data):
    file = None
    try:
        file = open("weights.txt", "r")
        data = file.readline()
        data = json.loads(data)
        file.close()

        weights = data['weights']
        bias = data['bias']

        Yin = 0

        for i in range(5):
            for j in range(5):
                Yin += test_data[i][j]*weights[i][j]
        Yin += bias

        print('Yin is:', Yin)

        if Yin >= 0:
            return 'X'
        else:
            return 'O'

    except:
        print("An Unexpected error occured!")
    finally:
        if file:
            file.close()
        