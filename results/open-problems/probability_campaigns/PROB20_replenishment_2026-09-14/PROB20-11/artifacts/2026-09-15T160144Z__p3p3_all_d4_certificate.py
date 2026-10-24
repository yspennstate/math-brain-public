#!/usr/bin/env python3
"""Exact PROB20-11 certificate eliminating the balanced K=4 class whose
close-edge graph is two disjoint P3's and all four close distances are 4.
No solver and no floating point.
"""
N=2048

def fd(a,b):
    w=(a^b).bit_count()
    return min(w,12-w)

B=[x for x in range(N) if fd(0,x)<=3]
assert len(B)==299
balls=[]
for c in range(N):
    m=0
    for b in B: m |= 1<<(c^b)
    balls.append(m)
EVEN=sum(1<<x for x in range(N) if x.bit_count()%2==0)
ODD=((1<<N)-1)^EVEN

def tri_halves(a,b,c):
    z=balls[a]&balls[b]&balls[c]
    return (z&EVEN).bit_count(),(z&ODD).bit_count()

def bits(ii):
    z=0
    for i in ii:z|=1<<i
    return z

seen=set()
for a in range(1,N):
    if a.bit_count()%2==0 and fd(0,a)==4:
        for b in range(1,N):
            if b.bit_count()%2==1 and fd(0,b)==5 and fd(a,b)==5:
                seen.add(tri_halves(0,a,b))
assert seen=={(1,3),(0,0)}

for LE in range(25):
    for LO in range(25):
        if LE+3*LO<=2 and 3*LE+LO<=2:
            assert (LE,LO)==(0,0)

A=bits([0,1,2,3])
C=bits([0,4,5,6])
assert (fd(0,A),fd(0,C),fd(A,C))==(4,4,6)

O=[]
for x in range(N):
    if x.bit_count()%2==1 and fd(x,0)==5 and fd(x,A)==5 and fd(x,C)==5:
        if tri_halves(0,A,x)==(1,3) and tri_halves(0,C,x)==(1,3):
            O.append(x)
assert len(O)==135
m=len(O)
d4=[0]*m; d6=[0]*m
for i in range(m):
    for j in range(i+1,m):
        d=fd(O[i],O[j])
        if d==4:
            d4[i]|=1<<j; d4[j]|=1<<i
        elif d==6:
            d6[i]|=1<<j; d6[j]|=1<<i

E=[x for x in range(N) if x.bit_count()%2==0 and fd(x,0)==6 and fd(x,A)==6 and fd(x,C)==6]
assert len(E)==90
ne=len(E); EALL=(1<<ne)-1
crossE=[]
for o in O:
    z=0
    for i,e in enumerate(E):
        if fd(o,e)==5:z|=1<<i
    crossE.append(z)
highE={}
for i in range(m):
    q=d4[i]
    while q:
        l=q&-q; j=l.bit_length()-1; q-=l
        if i<j:
            z=0
            for k,e in enumerate(E):
                if tri_halves(O[i],O[j],e)==(3,1):z|=1<<k
            highE[(i,j)]=z
ed6=[0]*ne
for i in range(ne):
    for j in range(i+1,ne):
        if fd(E[i],E[j])==6:
            ed6[i]|=1<<j;ed6[j]|=1<<i

def has_d6_triangle(S):
    q=S
    while q:
        l=q&-q;i=l.bit_length()-1;q-=l
        common=ed6[i]&q
        r=common
        while r:
            ll=r&-r;j=ll.bit_length()-1;r-=ll
            if ed6[j]&common:
                return True
    return False

path_triples=0
odd_six=0
max_E_pool=0
for mid in range(m):
    q=d4[mid]
    neigh=[]
    while q:
        l=q&-q;neigh.append(l.bit_length()-1);q-=l
    for ai in range(len(neigh)):
        u=neigh[ai]
        for bi in range(ai+1,len(neigh)):
            v=neigh[bi]
            if not ((d6[u]>>v)&1):continue
            path_triples+=1
            S=d6[mid]&d6[u]&d6[v]
            hu=highE[tuple(sorted((mid,u)))]
            hv=highE[tuple(sorted((mid,v)))]
            qx=S
            while qx:
                lx=qx&-qx;x=lx.bit_length()-1;qx-=lx
                sy=d6[x]&qx
                qy=sy
                while qy:
                    ly=qy&-qy;y=ly.bit_length()-1;qy-=ly
                    sz=d6[y]&sy
                    sz &= ~((1<<(y+1))-1)
                    while sz:
                        lz=sz&-sz;z=lz.bit_length()-1;sz-=lz
                        odd_six+=1
                        EC=EALL
                        for oi in (mid,u,v,x,y,z): EC &= crossE[oi]
                        EC &= hu & hv
                        bc=EC.bit_count()
                        if bc>max_E_pool:max_E_pool=bc
                        assert not has_d6_triangle(EC)

assert path_triples==120420
assert odd_six==436320
assert max_E_pool==4
print('CERTIFICATE PASSED')
print('odd candidate pool =',len(O))
print('odd path triples =',path_triples)
print('odd six-center configurations =',odd_six)
print('base even-isolate candidates =',len(E))
print('maximum final even-isolate pool =',max_E_pool)
print('no final pool contains a d6 triangle')
print('CONCLUSION: the all-d4 two-P3 K=4 class is impossible')
