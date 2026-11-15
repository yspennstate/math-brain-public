"""A 2N+4-state family with limiting ratio N+2, checked exactly."""
from fractions import Fraction as F
from exact_core import calculate, save_json


def build(N,t):
    r = t**3
    alpha = t
    n = 2*N+4
    a,b,c = 0,2*N+2,2*N+3
    z = list(range(1,N+2))
    y = list(range(N+2,2*N+2))
    w = [[0]*n for _ in range(n)]
    def edge(i,j,v):
        w[i][j] = w[j][i] = v
    edge(a,z[0],1)
    w[a][a] = t-1
    for k in range(N):
        edge(z[k],z[k+1],r**(k+1))
        edge(y[k],z[k+1],alpha*r**(k+1))
        w[y[k]][y[k]] = (t-1)*alpha*r**(k+1)
    edge(b,z[N],alpha*r**(N+1))
    w[b][b] = (t-1)*alpha*r**(N+1)
    edge(c,z[N],r**(N+2))
    w[c][c] = (N+2)*r**(N+4)
    groups = [[a]] + [[z[k],y[k]] for k in range(N)] + [[z[N],c],[b]]
    hw = [[sum(w[i][j] for i in g for j in h) for h in groups] for g in groups]
    return w,hw,groups


def formulas(N,t):
    r,alpha = t**3,t
    G = lambda k: sum(r**l for l in range(1,k+1))
    B = 2+alpha*(t+1)
    S = [t+1+r**(k+1)+B*G(k) for k in range(N)]
    SN = t+1+r**(N+2)+B*G(N)+(t+1)*alpha*r**(N+1)
    W = (N+2)*r**(N+4)+r**(N+2)+SN
    M = F(t)+sum((F(S[k],r**(k+1)) for k in range(N)),F(0))+F(SN,r**(N+2))
    Q = [S[k]+t*alpha*r**(k+1) for k in range(N)]
    A = F(t)+sum((F(Q[k],(1+alpha)*r**(k+1)) for k in range(N)),F(0))
    mu = (F(t*t*(1+alpha*G(N+1)))+
          sum((F(S[k]**2,r**(k+1)) for k in range(N)),F(0))+
          F(SN**2,r**(N+2)))/W
    mh = (F(t*t*(1+alpha*r**(N+1)))+
          sum((F(Q[k]**2,(1+alpha)*r**(k+1)) for k in range(N)),F(0)))/W
    assert F(W,r**(N+2)) >= M
    assert N == 0 or F(W,(1+alpha)*r**N) >= A-t
    return M-mu,A+t-mh


def main():
    rows = []
    for N in (0,1,2,3):
        for t in (2,10,100,1000):
            w,hw,g = build(N,t)
            x,y = calculate(w),calculate(hw)
            tx,ty = formulas(N,t)
            assert (x['tmix'],y['tmix']) == (tx,ty)
            rec = dict(N=N,n=2*N+4,t=t,original=tx,quotient=ty,
                       ratio=ty/tx,original_pairs=x['pairs'],
                       quotient_pairs=y['pairs'],groups=g)
            rows.append(rec)
            print(f"n={2*N+4} N={N} t={t} X={float(tx):.12f} "
                  f"hX={float(ty):.12f} ratio={float(ty/tx):.12f}")
    save_json('fork_comb_exact.json',rows)


if __name__ == '__main__':
    main()
