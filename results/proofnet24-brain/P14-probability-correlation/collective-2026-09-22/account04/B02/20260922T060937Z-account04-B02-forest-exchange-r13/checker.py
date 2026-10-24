from collections import Counter, deque

NVERT = 5
E = tuple((i,j) for i in range(NVERT) for j in range(i+1,NVERT))
e = (0,1)
f = (2,3)
E0 = tuple(g for g in E if g not in (e,f))

class DSU:
    def __init__(self,n): self.p=list(range(n))
    def find(self,x):
        while self.p[x]!=x:
            self.p[x]=self.p[self.p[x]]; x=self.p[x]
        return x
    def union(self,a,b):
        a=self.find(a); b=self.find(b)
        if a==b: return False
        self.p[b]=a; return True

def subset(mask):
    return frozenset(E0[i] for i in range(len(E0)) if (mask>>i)&1)

def forest(F):
    d=DSU(NVERT)
    for a,b in F:
        if not d.union(a,b): return False
    return True

def conn(F,a,b):
    d=DSU(NVERT)
    for x,y in F: d.union(x,y)
    return d.find(a)==d.find(b)

def addable(F,g): return not conn(F,*g)
def joint(F): return forest(set(F)|{e,f})

forests=[subset(m) for m in range(1<<len(E0)) if forest(subset(m))]
A={F for F in forests if addable(F,e)}
B={F for F in forests if addable(F,f)}
D={F for F in forests if joint(F)}
L=[(F,H) for F in forests if F not in A for H in D]
R=[(F,H) for F in A for H in B if H not in D]

def multvec(F,H):
    return tuple(int(g in F)+int(g in H) for g in E0)

LC=Counter(multvec(F,H) for F,H in L)
RC=Counter(multvec(F,H) for F,H in R)
witness_edges={(0,2),(0,3),(1,2),(1,3)}
witness=tuple(1 if g in witness_edges else 0 for g in E0)
LW=[(F,H) for F,H in L if multvec(F,H)==witness]
RW=[(F,H) for F,H in R if multvec(F,H)==witness]
diagonal_capacity=sum(min(c,RC.get(mu,0)) for mu,c in LC.items())

class Dinic:
    def __init__(self,n): self.g=[[] for _ in range(n)]
    def add(self,u,v,c):
        a=[v,c,None]; b=[u,0,a]; a[2]=b
        self.g[u].append(a); self.g[v].append(b)
    def flow(self,s,t):
        total=0
        while True:
            lev=[-1]*len(self.g); lev[s]=0; q=deque([s])
            while q:
                u=q.popleft()
                for v,c,rev in self.g[u]:
                    if c and lev[v]<0: lev[v]=lev[u]+1; q.append(v)
            if lev[t]<0: return total
            it=[0]*len(self.g)
            def dfs(u,push):
                if u==t: return push
                while it[u]<len(self.g[u]):
                    ed=self.g[u][it[u]]; v,c,rev=ed
                    if c and lev[v]==lev[u]+1:
                        got=dfs(v,min(push,c))
                        if got:
                            ed[1]-=got; rev[1]+=got; return got
                    it[u]+=1
                return 0
            while True:
                got=dfs(s,10**18)
                if not got: break
                total+=got

def hdist(mu,nu): return sum(a!=b for a,b in zip(mu,nu))
Lkeys=list(LC); Rkeys=list(RC)
s=0; lo=1; ro=lo+len(Lkeys); t=ro+len(Rkeys)
net=Dinic(t+1)
for i,mu in enumerate(Lkeys): net.add(s,lo+i,LC[mu])
for j,nu in enumerate(Rkeys): net.add(ro+j,t,RC[nu])
INF=len(L)+1
for i,mu in enumerate(Lkeys):
    for j,nu in enumerate(Rkeys):
        if hdist(mu,nu)<=1: net.add(lo+i,ro+j,INF)
one_defect_flow=net.flow(s,t)

def fmt_pair(p):
    F,H=p
    return "F={"+",".join(f"{a}{b}" for a,b in sorted(F))+"};H={"+",".join(f"{a}{b}" for a,b in sorted(H))+"}"

print(f"N={len(forests)} A={len(A)} B={len(B)} D={len(D)}")
print(f"residual_L={len(L)} residual_R={len(R)} Delta={len(A)*len(B)-len(forests)*len(D)}")
print("witness_E0="+",".join(f"{a}{b}" for a,b in E0))
print("witness_mu="+str(witness))
print(f"witness_L={len(LW)} witness_R={len(RW)} witness_deficiency={len(LW)-len(RW)}")
for p in LW: print("L_W "+fmt_pair(p))
for p in RW: print("R_W "+fmt_pair(p))
print(f"multiplicity_preserving_capacity={diagonal_capacity} total_L={len(L)} global_deficiency={len(L)-diagonal_capacity}")
print(f"one_defect_capacity={one_defect_flow} total_L={len(L)}")
assert (len(forests),len(A),len(B),len(D))==(134,64,64,29)
assert (len(L),len(R))==(2030,2240)
assert len(A)*len(B)-len(forests)*len(D)==210
assert (len(LW),len(RW))==(4,2)
assert diagonal_capacity==1924
assert one_defect_flow==len(L)==2030
print("ALL_EXACT_ASSERTIONS_PASSED")
