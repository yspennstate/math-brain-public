import itertools, math, random

def fwht(a):
    a = list(map(float, a))
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return [x/len(a) for x in a]

def entropy(v):
    return sum(-x*math.log2(x) for x in v if x>0)

def quantities(vals):
    N=len(vals); n=N.bit_length()-1
    wh=fwht(vals); p=[x*x for x in wh]
    pi=[]
    for s in range(N):
        pi.append(sum(p[t] for t in range(N) if (t&s)==s))
    U=sum(p[s]*math.log2(pi[s]/p[s]) for s in range(N) if p[s]>1e-30)
    H=entropy(p)
    I=sum(s.bit_count()*p[s] for s in range(N))
    deltas=[]
    for i in range(n):
        plus=[]; minus=[]
        for base in range(N):
            if (base>>i)&1: continue
            minus.append(vals[base])
            plus.append(vals[base|(1<<i)])
        Up=quantities_noG(plus)[0]
        Um=quantities_noG(minus)[0]
        deltas.append(U-(Up+Um)/2)
    # dual total correlation B=sum_i H(1_{i in S}|S_{-i}) for S~p
    B=0.0; Bis=[]
    for i in range(n):
        bit=1<<i
        Bi=0.0
        for s in range(N):
            if s&bit: continue
            a=p[s]; b=p[s|bit]; t=a+b
            if t>0:
                if a>0: Bi-=a*math.log2(a/t)
                if b>0: Bi-=b*math.log2(b/t)
        Bis.append(Bi); B+=Bi
    Uis=[]
    for i in range(n):
        Ui=0.0
        for s in range(1,N):
            if (s>>i)&1 and p[s]>1e-30:
                Ui += p[s]/s.bit_count()*math.log2(pi[s]/p[s])
        Uis.append(Ui)
    return U,H,I,sum(deltas),deltas,p,pi,B,Bis,Uis

def quantities_noG(vals):
    N=len(vals)
    wh=fwht(vals); p=[x*x for x in wh]
    pi=[sum(p[t] for t in range(N) if (t&s)==s) for s in range(N)]
    U=sum(p[s]*math.log2(pi[s]/p[s]) for s in range(N) if p[s]>1e-30)
    H=entropy(p)
    I=sum(s.bit_count()*p[s] for s in range(N))
    return U,H,I

def enumerate_n(n):
    N=1<<n
    best={"G-U_over_I":(-1e9,None),"G-halfU_over_I":(-1e9,None),"G_over_I":(-1e9,None)}
    # fix first output +1 to quotient global sign
    for mask in range(1<<(N-1)):
        vals=[1]+[1 if (mask>>(j-1))&1 else -1 for j in range(1,N)]
        U,H,I,G,*tail=quantities(vals); B=tail[-3]; Bis=tail[-2]; Uis=tail[-1]
        if I<1e-15: continue
        M=G-B
        rows={"G-U_over_I":(G-U)/I,"G-halfU_over_I":(G-.5*U)/I,"G_over_I":G/I,
              "M+U_over_I":(M+U)/I,"M+1.25U_over_I":(M+1.25*U)/I,
              "M+1.5U_over_I":(M+1.5*U)/I}
        for k,v in rows.items():
            if k not in best: best[k]=(-1e9,None)
            if v>best[k][0]: best[k]=(v,(mask,U,H,I,G,B,vals))
        infs=[]
        for i in range(n):
            inf=sum(p for s,p in enumerate(tail[1]) if (s>>i)&1)
            infs.append(inf)
            if inf>1e-15:
                v=(tail[0][i]-Bis[i]+1.25*Uis[i])/inf
                k="local_Mi+1.25Ui_over_Inf"
                if k not in best: best[k]=(-1e9,None)
                if v>best[k][0]: best[k]=(v,(mask,i,U,H,I,G,B,infs[-1],tail[0][i],Bis[i],Uis[i],vals))
    return best

if __name__=='__main__':
    for n in range(1,5):
        print(n,enumerate_n(n))
    rng=random.Random(20261014)
    for n,trials in [(5,20000),(6,10000),(7,5000),(8,2000),(9,500)]:
        N=1<<n; best=(-1e9,None); best_local=(-1e9,None)
        for _ in range(trials):
            vals=[1 if rng.getrandbits(1) else -1 for _ in range(N)]
            U,H,I,G,*tail=quantities(vals); B=tail[-3]; Bis=tail[-2]; Uis=tail[-1]
            if I<1e-15: continue
            ratio=(G-B+1.25*U)/I
            if ratio>best[0]: best=(ratio,(U,H,I,G,B,vals))
            p=tail[1]
            for i in range(n):
                inf=sum(pp for s,pp in enumerate(p) if (s>>i)&1)
                if inf>1e-15:
                    lr=(tail[0][i]-Bis[i]+1.25*Uis[i])/inf
                    if lr>best_local[0]: best_local=(lr,(i,U,H,I,G,B,inf,tail[0][i],Bis[i],Uis[i],vals))
        truth_mask=sum((1<<j) for j,v in enumerate(best_local[1][-1]) if v==1)
        print('random',n,trials,best[0],best[1][:5],'local',best_local[0],best_local[1][:10],'truth_mask',truth_mask)

