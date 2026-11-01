"""E0060 = Rozikov Problem 3: is there a (transversal Volterra QSO) trajectory with a periodic itinerary?
Record the itinerary (sequence of fixed-point neighbourhoods visited) for Zakharevich's m=3 cyclic map
and for a cyclic-type m=4 Volterra map (Ganikhodjaev-Zanin 2012 analyse routes 1-4-3-2-1, 1-4-2-1, 1-4-3-1)."""
import numpy as np
def V(x, A):
    y = x*(1 + A@x); return y/y.sum()
def itinerary(A, x0, K, eps=0.02):
    x = x0.copy(); it = []; cur = None
    for k in range(K):
        x = V(x, A)
        v = int(np.argmax(x))
        if x[v] > 1-eps:
            if v != cur: it.append((v+1, k)); cur = v
        else:
            cur = None
    return it
A3 = np.array([[0,1,-1],[-1,0,1],[1,-1,0]], float)         # a=b=c=1: leading 2x2 minor = 1, transversal; fixed points: 3 vertices + centre
it3 = itinerary(A3, np.array([0.5,0.3,0.2]), 3_000_000)
print("m=3 Zakharevich: vertices visited (vertex, first step):", it3[:14])
print("   itinerary indices:", [v for v,_ in it3][:20], " sojourn lengths:", [it3[i+1][1]-it3[i][1] for i in range(min(10,len(it3)-1))])
# m=4: skew matrix of the 2012 paper's third class with all a_ij >= 0 in the pattern (5): choose generic positive entries
rng = np.random.default_rng(60)
for trial in range(3):
    a12,a13,a14,a23,a24,a34 = rng.uniform(0.3,1.0,6)
    A4 = np.array([[0,a12,a13,-a14],[-a12,0,a23,a24],[-a13,-a23,0,a34],[a14,-a24,-a34,0]])
    lead2 = np.linalg.det(A4[:2,:2]); lead4 = np.linalg.det(A4)
    it4 = itinerary(A4, rng.dirichlet([1,1,1,1]), 3_000_000)
    print(f"m=4 trial {trial}: leading minors {lead2:.3f}, {lead4:.3f}; itinerary:", [v for v,_ in it4][:24])
