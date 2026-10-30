from fractions import Fraction as F
from functools import lru_cache
import itertools,math

def all_matchings(vertices,edges):
    if not vertices:yield [];return
    u=vertices[0];rest=vertices[1:]
    yield from all_matchings(rest,edges)
    for v in rest:
        if (min(u,v),max(u,v)) in edges:
            for M in all_matchings([x for x in rest if x!=v],edges):yield [(u,v)]+M

def pm(k):
    if k<0 or k%2:return 0
    return math.factorial(k)//(2**(k//2)*math.factorial(k//2))

def falling(l,c):return math.factorial(l)//math.factorial(l-c) if 0<=c<=l else 0

@lru_cache(None)
def mass(a,b,edges,SA,l):
    if SA==0 and l==0:return F(0)
    n=a+b;lam=F(1,n-1);E=set(edges);X=[x for x in range(a) if SA>>x&1];k=len(X)+l;total=F(0)
    # Enumerate the independent set of unmatched X vertices first.
    for mask in range(1<<len(X)):
        U=[x for j,x in enumerate(X) if mask>>j&1]
        if any((min(u,v),max(u,v)) in E for u,v in itertools.combinations(U,2)):continue
        W=[x for x in X if x not in U]
        for AA in all_matchings(W,E):
            used={x for pair in AA for x in pair};cross=[x for x in W if x not in used];c=len(cross)
            if c>l or (l-c)%2:continue
            multiplicity=falling(l,c)*pm(l-c)
            roots=AA+[(x,a+j) for j,x in enumerate(cross)]+[(a+j,a+j+1) for j in range(c,l,2)]
            endpoints=[x for pair in roots for x in pair];choices=[]
            for u in U:
                external=b-l+sum(not(SA>>x&1) and (min(u,x),max(u,x)) in E for x in range(a) if x!=u)
                opts=[(None,external*lam/32)] if external else []
                opts += [(x,lam/8) for x in endpoints if x>=a or (min(u,x),max(u,x)) in E]
                choices.append(opts)
            val=F(0)
            for selected in itertools.product(*choices):
                count={x:0 for x in endpoints};term=F(1)
                for x,w in selected:
                    term*=w
                    if x is not None:count[x]+=1
                for u,v in roots:
                    aa,bb=count[u],count[v];z=aa+bb
                    term*=F(math.factorial(aa)*math.factorial(bb),(z+1)**2*(z+2))
                val+=term
            total+=multiplicity*(lam/24)**len(roots)*val
    # The only other possible unmatched sector is ONE Y vertex.
    if l:
        for AA in all_matchings(X,E):
            c=len(X)-2*len(AA)
            if c>l-1 or (l-1-c)%2:continue
            multiplicity=l*falling(l-1,c)*pm(l-1-c)
            roots=(k-1)//2
            leaf=lam*(F(n-k,32)+F(k-1,48))
            total+=multiplicity*(lam/48)**roots*leaf
    return total

def reference(a,b,edges):
    table={(S,l):mass(a,b,edges,S,l) for S in range(1<<a) for l in range(b+1) if S or l}
    Z=sum((math.comb(b,l)*v for (S,l),v in table.items()),F(0))
    return table,Z,{key:v/Z for key,v in table.items()}

def core_characters(values):
    return [sum(v*(-1 if (x&S).bit_count()%2 else 1) for x,v in enumerate(values)) for S in range(len(values))]

def core_boundary(values,a):
    return sum(values[x]!=values[x^(1<<i)] for x in range(1<<a) for i in range(a))//2
