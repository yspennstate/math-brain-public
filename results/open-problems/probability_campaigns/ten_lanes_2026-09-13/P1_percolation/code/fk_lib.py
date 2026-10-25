"""Exact / high-precision machinery for the random-cluster model on small (multi)graphs."""
import itertools
from fractions import Fraction

def comps(n, edges, mask):
    par = list(range(n))
    def find(x):
        r=x
        while par[r]!=r: r=par[r]
        while par[x]!=r: par[x],x = r,par[x]
        return r
    c=n
    for i,(u,v) in enumerate(edges):
        if mask>>i & 1:
            a,b=find(u),find(v)
            if a!=b: par[a]=b; c-=1
    return c

def profile(n, edges):
    """popcount and component count for every configuration."""
    m=len(edges)
    pc=[0]*(1<<m); kk=[0]*(1<<m)
    for mask in range(1<<m):
        pc[mask]=bin(mask).count("1")
        kk[mask]=comps(n,edges,mask)
    return pc,kk

def weights(pc,kk,p,q,m):
    w=[None]*(1<<m)
    for mask in range(1<<m):
        c=pc[mask]
        w[mask]=(p**c)*((1-p)**(m-c))*(q**kk[mask])
    return w

# ---------- max-weight closure (up-set) via Dinic ----------
class Dinic:
    def __init__(self,n):
        self.n=n; self.g=[[] for _ in range(n)]
    def add(self,u,v,c):
        self.g[u].append([v,c,len(self.g[v])])
        self.g[v].append([u,0,len(self.g[u])-1])
    def bfs(self,s,t):
        self.lv=[-1]*self.n; self.lv[s]=0; q=[s]
        for u in q:
            for e in self.g[u]:
                if e[1]>1e-12 and self.lv[e[0]]<0:
                    self.lv[e[0]]=self.lv[u]+1; q.append(e[0])
        return self.lv[t]>=0
    def dfs(self,u,t,f):
        if u==t: return f
        while self.it[u]<len(self.g[u]):
            e=self.g[u][self.it[u]]
            v=e[0]
            if e[1]>1e-12 and self.lv[v]==self.lv[u]+1:
                d=self.dfs(v,t,min(f,e[1]))
                if d>1e-12:
                    e[1]-=d; self.g[v][e[2]][1]+=d; return d
            self.it[u]+=1
        return 0.0
    def maxflow(self,s,t):
        fl=0.0
        while self.bfs(s,t):
            self.it=[0]*self.n
            while True:
                f=self.dfs(s,t,float('inf'))
                if f<=1e-12: break
                fl+=f
        return fl
    def mincut_side(self,s):
        # vertices reachable from s in residual graph
        seen=[False]*self.n; seen[s]=True; q=[s]
        for u in q:
            for e in self.g[u]:
                if e[1]>1e-12 and not seen[e[0]]:
                    seen[e[0]]=True; q.append(e[0])
        return seen

def min_over_upsets(m, val):
    """min over nonempty-or-empty up-closed A of sum_{x in A} val[x].
    Returns (minimum, membership list)."""
    N=1<<m
    S=N; T=N+1
    d=Dinic(N+2)
    INF=float('inf')
    # we maximise sum of -val over up-sets; w[x] = -val[x]
    pos=0.0
    for x in range(N):
        w=-val[x]
        if w>0: d.add(S,x,w); pos+=w
        elif w<0: d.add(x,T,-w)
    for x in range(N):
        for b in range(m):
            if not (x>>b&1):
                d.add(x, x|(1<<b), 1e18)   # x in A forces x+bit in A
    fl=d.maxflow(S,T)
    best=pos-fl
    side=d.mincut_side(S)
    A=[x for x in range(N) if side[x]]
    return -best, A
