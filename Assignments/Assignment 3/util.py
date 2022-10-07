import torch
def onehot(x):
    temp = torch.zeros(10)
    temp[x] = 1
    return temp