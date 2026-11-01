import itertools, math
# object: sum over eps in {-1,0,1}^{K+1} of 2^{-#supp} h(m/2^K), m = sum eps_i 2^i 3^{K-i}
# claim: m/2^K = sum_j eps'_j (3/2)^j  (reindex j=K-i)
K=8
def h(u):
    if abs(u)<1e-12: return 1.0*0+ (math.cos(0)*1.0)  # limit: sin(pi u)/(pi u)->1
    return math.cos(3*math.pi*u)*math.sin(math.pi*u)/(math.pi*u)
tot=0.0; wtot=0.0; ms=set(); dup=0
for eps in itertools.product((-1,0,1),repeat=K+1):
    m=sum(e*(2**i)*(3**(K-i)) for i,e in enumerate(eps))
    if m in ms: dup+=1
    ms.add(m)
    w=2.0**(-sum(1 for e in eps if e!=0))
    wtot+=w
    tot+=w*h(m/2**K)
    # check reindex identity
print("patterns",3**(K+1),"distinct m",len(ms),"dups",dup)
print("total weight",wtot,"2^(K+1)=",2**(K+1))
print("sum w*h(m/2^K) =",tot)
# reindex check on a random sample
import random
for _ in range(5):
    eps=[random.choice((-1,0,1)) for _ in range(K+1)]
    m=sum(e*(2**i)*(3**(K-i)) for i,e in enumerate(eps))
    v=sum(eps[K-j]*(1.5**j) for j in range(K+1))
    assert abs(m/2**K - v)<1e-9,(m/2**K,v)
print("reindex identity ok: m/2^K = sum_j eps_{K-j} (3/2)^j")
