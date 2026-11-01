from fractions import Fraction
from itertools import product

UV=((0,0),(0,1),(1,0),(1,1))

def update(w,x,g,u,v):
    L=2*w
    c=[]
    cp=0
    for i in range(L):
        ci=0 if g[i] else max(cp,int(x[i]==v))
        c.append(ci); cp=ci
    gp=[]
    for i in range(L-1):
        gp.append(g[i+1]+c[i+1]-c[i])
    gp.append((1-c[-1])*int(u==v))
    return tuple(gp)

# Exact finite exhaustive self-check: a one-bit gradient discrepancy never branches.
for w in range(1,4):
    L=2*w
    checked=0
    max_out=0
    for x in product((0,1), repeat=L):
        for g in product((0,1), repeat=L):
            for p in range(L):
                h=list(g); h[p]^=1; h=tuple(h)
                for u,v in UV:
                    a=update(w,x,g,u,v)
                    b=update(w,x,h,u,v)
                    dout=sum(aa!=bb for aa,bb in zip(a,b))
                    assert dout <= 1
                    max_out=max(max_out,dout)
                    checked+=1
    print("NONBRANCHING_EXHAUSTIVE", "w",w,"cases",checked,"max_output_hamming",max_out)

print("ONE_DISCREPANCY_NONBRANCHING_K_LE_3_PASS")

# Conditional jump-tail envelope: R has P(R=r)=2^{-(r+1)}, r>=0.
# Exact optimized Chernoff bound for a sum of T such envelopes crossing M>T:
# B(M,T)=((M+T)/(2M))^M ((M+T)/(2T))^T.
def B(M,T):
    assert M>T>0
    return Fraction((M+T)**(M+T),(2*M)**M*(2*T)**T)

for M,T in [(12,4),(24,8),(48,16),(64,16),(96,32),(128,32)]:
    b=B(M,T)
    print("CHERNOFF_BOUND","M",M,"T",T,"exact",b,"float",format(float(b),".17g"),
          "T_times",format(float(T*b),".17g"))
    assert b < 1
print("EXACT_NEGATIVE_BINOMIAL_CHERNOFF_ARITHMETIC_PASS")
print("ALL_EXACT_CHECKS_PASS")
