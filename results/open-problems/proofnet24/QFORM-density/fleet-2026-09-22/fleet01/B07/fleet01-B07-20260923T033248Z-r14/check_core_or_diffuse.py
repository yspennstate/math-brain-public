import itertools, math
import numpy as np

rng=np.random.default_rng(20260923)

def packet(B):
    m,n=B.shape
    W={}; P=0.; a=np.zeros(m); b=np.zeros(n)
    for R in itertools.combinations(range(m),3):
        for C in itertools.combinations(range(n),3):
            w=float(np.linalg.det(B[np.ix_(R,C)]))**2
            W[(R,C)]=w; P+=w
            for i in R: a[i]+=w
            for j in C: b[j]+=w
    a/=P; b/=P
    return P,a,b,W

count=0
for m,n in [(4,4),(5,6),(7,5)]:
    for _ in range(20):
        B=rng.normal(size=(m,n))
        P,a,b,W=packet(B)
        assert abs(a.sum()-3)<1e-8 and abs(b.sum()-3)<1e-8
        i=int(np.argmax(a)); j=int(np.argmax(b))
        M=sum(w for (R,C),w in W.items() if i in R and j in C)
        assert M/P+1e-10 >= a[i]+b[j]-1
        if a[i]>2/3 and b[j]>2/3:
            rr=np.zeros(m); cc=np.zeros(n)
            for (R,C),w in W.items():
                if i in R and j in C:
                    for k in R:
                        if k!=i: rr[k]+=w
                    for l in C:
                        if l!=j: cc[l]+=w
            rr/=M; cc/=M
            assert abs(rr.sum()-2)<1e-8 and abs(cc.sum()-2)<1e-8
            R0={i}|{k for k in range(m) if k!=i and rr[k]>.5}
            C0={j}|{l for l in range(n) if l!=j and cc[l]>.5}
            assert len(R0)<=4 and len(C0)<=4
            dr=sum(rr[k] for k in range(m) if k not in R0)
            dc=sum(cc[l] for l in range(n) if l not in C0)
            if dr+dc<.5:
                core=sum(w for (R,C),w in W.items()
                         if i in R and j in C and set(R)<=R0 and set(C)<=C0)
                assert core+1e-10 >= (1-dr-dc)*M
                assert core > P/6-1e-10
        count+=1

tau=1/128
L2=16*(tau+tau*tau)
s3=32/(129*math.sqrt(6))
core_bound=(129/16)*math.sqrt(288*math.pi)
vol_bound=(9*math.sqrt(3)*math.e/2)*256**(1/6)
print('QFORM_CORE_OR_DIFFUSE_CHECK_PASS')
print('random_packet_tests',count)
print('L2max',repr(L2))
print('s3lower_at_P_1_over_256',repr(s3))
print('core_density_bound',repr(core_bound))
print('volume_density_bound',repr(vol_bound))
