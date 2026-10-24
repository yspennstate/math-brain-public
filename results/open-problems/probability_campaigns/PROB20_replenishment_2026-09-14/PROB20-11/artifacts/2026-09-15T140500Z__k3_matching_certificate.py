#!/usr/bin/env python3
"""Exact certificate for the three-edge-matching exactly-three-close-pair cases.

The seven active-even coordinate orbits are exhausted. Six admit no completion under
the third-Bonferroni deficit budget. The sole budget-compatible orbit has exactly 144
full distance/budget-compatible configurations, whose maximum covered union is 1989<2048.
"""
N=2048

def fd(x,y):
    w=(x^y).bit_count(); return min(w,12-w)
B=[x for x in range(N) if fd(0,x)<=3]
balls=[]
for c in range(N):
    m=0
    for b in B:m|=1<<(c^b)
    balls.append(m)
def tri(a,b,c):return (balls[a]&balls[b]&balls[c]).bit_count()
def bits(L):
    z=0
    for i in L:z|=1<<i
    return z

def budget(kind,a,b,c):
    if kind=='222':return a+b+c<=1
    if kind=='242':return 4*a+b+6*c<=4 and 6*a+3*b+4*c<=16
    if kind=='442':return a+b+6*c<=2 and 3*(a+b)+4*c<=6
    raise ValueError

def high(e1,e2,y,d):return tri(e1,e2,y)==(10 if d==2 else 4)

A2=bits([0,1]);A4=bits([0,1,2,3]);B6=bits([0,2,3,4,5,6]);B4=bits([0,1,4,5,6,7])
configs=[
('M222_same',[0,A2,B6,bits([0,2,3,4,5,7])],2,2,'222'),
('M222_diff',[0,A2,B6,bits([1,2,3,4,5,6])],2,2,'222'),
('M242_same',[0,A2,B6,bits([0,2,3,4,7,8])],2,4,'242'),
('M242_diff',[0,A2,B6,bits([1,2,3,4,5,7])],2,4,'242'),
('M442_s0',[0,A4,B4,bits([2,3,4,5,6,7])],4,4,'442'),
('M442_s1',[0,A4,B4,bits([0,2,4,5,6,8])],4,4,'442'),
('M442_s2',[0,A4,B4,bits([0,1,4,5,8,9])],4,4,'442'),
]

def search(E,d1,d2,kind,enumerate_all=False):
    O=[]
    for y in range(N):
        if y.bit_count()%2==0:continue
        if all(fd(y,e)==5 for e in E):
            O.append((y,0 if high(E[0],E[1],y,d1) else 1,0 if high(E[2],E[3],y,d2) else 1))
    Xbase=[x for x in range(N) if x.bit_count()%2==0 and x not in E and all(fd(x,e)==6 for e in E)]
    completions=0;max_union=0
    for i,(u,au,bu) in enumerate(O):
      for v,av,bv in O[i+1:]:
        if fd(u,v)!=2:continue
        a0=au+av;b0=bu+bv;c0=sum(tri(u,v,e)!=10 for e in E)
        if not budget(kind,a0,b0,c0):continue
        X=[]
        for x in Xbase:
          if fd(x,u)==5 and fd(x,v)==5:
            lc=0 if tri(u,v,x)==10 else 1
            if budget(kind,a0,b0,c0+lc):X.append((x,lc))
        for xi,(x,lx) in enumerate(X):
          for z,lz in X[xi+1:]:
            if fd(x,z)!=6:continue
            c1=c0+lx+lz
            if not budget(kind,a0,b0,c1):continue
            Oc=[]
            for y,aa,bb in O:
              if y in (u,v):continue
              if fd(y,u)==6 and fd(y,v)==6 and fd(y,x)==5 and fd(y,z)==5 and budget(kind,a0+aa,b0+bb,c1):
                Oc.append((y,aa,bb))
            m=len(Oc)
            if m<4:continue
            adj=[0]*m
            for p in range(m):
              for q in range(p+1,m):
                if fd(Oc[p][0],Oc[q][0])==6:
                  adj[p]|=1<<q;adj[q]|=1<<p
            def rec(ch,P,a,b,chosen):
                nonlocal completions,max_union
                if ch==4:
                    completions+=1
                    if enumerate_all:
                        U=0
                        centers=E+[x,z,u,v]+[Oc[j][0] for j in chosen]
                        for cc in centers:U|=balls[cc]
                        max_union=max(max_union,U.bit_count())
                    return True
                if P.bit_count()<4-ch:return False
                found=False
                while P:
                    l=P&-P;j=l.bit_length()-1;P-=l
                    na=a+Oc[j][1];nb=b+Oc[j][2]
                    if budget(kind,na,nb,c1):
                        r=rec(ch+1,P&adj[j],na,nb,chosen+[j])
                        found|=r
                        if r and not enumerate_all:return True
                return found
            if rec(0,(1<<m)-1,a0,b0,[]) and not enumerate_all:
                return completions,max_union
    return completions,max_union

results={}
for name,E,d1,d2,kind in configs:
    results[name]=search(E,d1,d2,kind,enumerate_all=(name=='M442_s1'))
for name in ['M222_same','M222_diff','M242_same','M242_diff','M442_s0','M442_s2']:
    assert results[name][0]==0
assert results['M442_s1']==(144,1989)
print('CERTIFICATE PASSED')
for k,v in results.items():print(k,v)
print('All three-edge-matching canonical cases fail to cover; sole budget-compatible orbit has max union 1989.')
