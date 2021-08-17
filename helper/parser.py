import pickle

def pdumps(input):
    return pickle.dumps(input)

def ploads(input):
    return pickle.loads(input)
