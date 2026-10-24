import sympy as sp

pe,pf,pg,C,A,B=sp.symbols('pe pf pg C A B', positive=True)
M=sp.Matrix([[pe**2,-C,A],[-C,pf**2,B],[A,B,pg**2]])
det=sp.expand(M.det())
upper=sp.expand(pg**2*(pe**2*pf**2-C**2)-2*A*B*(pe*pf+C))
print('DET=',sp.factor(det))
print('UPPER_MINUS_DET=',sp.factor(upper-det))
after=sp.factor((pg**2*(pe*pf-C)-2*C*pg*(1-pg))/pg)
print('AFTER_SIMPSON=',after)
print('FLOOR_RESIDUAL=',sp.factor(after-(pg*(pe*pf+C)-2*C)))
assert sp.factor(upper-det)==(A*pf-B*pe)**2
assert sp.factor(after-(pg*(pe*pf+C)-2*C))==0

# Exact K4 regression for conditioning/contraction.  A multigraph forest treats a
# parallel pair as a 2-cycle, hence at most one member can be selected.
def forest(n,edges,mask):
    p=list(range(n))
    def find(x):
        while p[x]!=x:
            p[x]=p[p[x]]; x=p[x]
        return x
    for i,(u,v) in enumerate(edges):
        if not (mask>>i)&1: continue
        if u==v: return False
        a,b=find(u),find(v)
        if a==b: return False
        p[a]=b
    return True

def counts(n,edges,e,f,condition=lambda m: True):
    Z=Ze=Zf=Zef=0
    for mask in range(1<<len(edges)):
        if forest(n,edges,mask) and condition(mask):
            Z+=1
            xe=(mask>>e)&1; xf=(mask>>f)&1
            Ze+=xe; Zf+=xf; Zef+=xe*xf
    return (Z,Ze,Zf,Zef,Ze*Zf-Z*Zef)

G=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
cond=counts(4,G,1,4,lambda m:(m&1)==1)
# Contract 01; retained edges are 02(mark),03,12,13(mark),23.
Q=[(0,1),(0,2),(0,1),(0,2),(1,2)]
contracted=counts(3,Q,0,3)
print('K4_GIVEN_G=',cond)
print('K4_CONTRACTED=',contracted)
assert cond==contracted==(14,4,4,1,2)
print('STATUS=PASS')
