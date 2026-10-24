import numpy as np
def mats():
    e = np.ones(3)/np.sqrt(3)
    d = {"I-2ee": np.eye(3) - 2*np.outer(e,e),
         "exa": np.array([[.5,.5,1/np.sqrt(2)],[.5,.5,-1/np.sqrt(2)],[1/np.sqrt(2),-1/np.sqrt(2),0]]),
         "2I-J": 2*np.eye(3) - np.ones((3,3)),
         "mJI": -(np.ones((3,3)) - np.eye(3)),
         "d11m1": np.diag([1.,1.,-1.]),
         "d41m1": np.diag([4.,1.,-1.]),
         "d111": np.eye(3),
         "d911": np.diag([9.,1.,1.])}
    rng = np.random.default_rng(11)
    for k in range(6):
        M = rng.normal(size=(3,3)); M = (M+M.T)/2
        w = np.linalg.eigvalsh(M); d["rand%d"%k] = M/np.min(np.abs(w))
    return d
