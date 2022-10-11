import numpy as np

def try_arange():
    a = np.arange(6)
    
    a2=a[np.newaxis, :]

    print(a)
    print(a.shape)


    print(a2)
    print(a2.shape)



if __name__=="__main__":
    try_arange()