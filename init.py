import json

def init_file():
    try:
        file = open("weights.txt", "r")
        data = file.readline()
        file.close()

        if not data:
            obj = {"weights":[], "bias":0}
            for i in range(5):
                obj["weights"].append([])
                for j in range(5):
                    obj["weights"][i].append(0)
            obj["bias"] = 0

            file = open('weights.txt', 'w')
            file.write(json.dumps(obj))
            file.close()

    except:
        print('initialization of file failed!')