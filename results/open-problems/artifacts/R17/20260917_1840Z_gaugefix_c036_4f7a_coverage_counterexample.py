#!/usr/bin/env python3

def bar(c): return 1-c

def mmp(c,l):
    if l>=0: return ((str(bar(c))*l)+str(c), str(c))
    return (str(c), (str(bar(c))*(-l))+str(c))

def cat(word):
    a=b=''
    for c,l in word:
        x,y=mmp(c,l); a+=x; b+=y
    return a,b

def lcs(a,b):
    d=[0]*(len(b)+1)
    for x in a:
        n=[0]*(len(b)+1)
        for j,y in enumerate(b,1):
            n[j]=d[j-1]+1 if x==y else max(d[j],n[j-1])
        d=n
    return d[-1]

def minimal_match_pair(c,l):
    a,b=mmp(c,l)
    L=lcs(a,b)
    return L==1 and lcs(a[:-1],b)==0 and lcs(a,b[:-1])==0

def pack4(x,y,dx,dy): return x | (y<<8) | (dx<<16) | (dy<<24)
def unpack4(s): return s&255,(s>>8)&255,(s>>16)&255,(s>>24)&255

class TC:
    def __init__(self,h): self.h=h; self.mask=(1<<h)-1
    def reduce_with_flip(self,s):
        x,y,dx,dy=unpack4(s)
        flip=1 if (x & (1<<(self.h-1))) else 0
        if flip:
            x ^= self.mask; y ^= self.mask
        return pack4(x,y,dx,dy),flip
    def trans(self,s,c,l):
        h=self.h
        x,y,dx,dy=unpack4(s)
        ta=l+1 if l>=0 else 1
        tb=-l+1 if l<0 else 1
        na,nb=h+ta,h+tb
        L=[[0]*18 for _ in range(18)]
        L[h][h]=h
        cur=h
        for k in range(h-1,-1,-1):
            cur -= (dx>>(h-1-k))&1; L[k][h]=cur
        cur=h
        for k in range(h-1,-1,-1):
            cur -= (dy>>(h-1-k))&1; L[h][k]=cur
        def achar(i):
            if i<=h: return (x>>(h-i))&1
            q=i-h-1
            return (1-c if q<l else c) if l>=0 else c
        def bchar(j):
            if j<=h: return (y>>(h-j))&1
            q=j-h-1
            return (1-c if q<(-l) else c) if l<0 else c
        for i in range(na+1):
            for j in range(nb+1):
                if i<=h and j<=h: continue
                if i==0: L[i][j]=L[i][j-1]
                elif j==0: L[i][j]=L[i-1][j]
                elif achar(i)==bchar(j): L[i][j]=L[i-1][j-1]+1
                else: L[i][j]=max(L[i][j-1],L[i-1][j])
        i,j=na,nb
        while i>=h and j>=h:
            if L[i][j]==L[i-1][j]: i-=1
            elif L[i][j]==L[i][j-1]: j-=1
            else: i-=1; j-=1
            if i==h and j==h:
                xs,ys=x,y
                if l>=0:
                    for _ in range(l): xs=((xs<<1)|(1-c))&self.mask
                    xs=((xs<<1)|c)&self.mask; ys=((ys<<1)|c)&self.mask
                else:
                    xs=((xs<<1)|c)&self.mask
                    for _ in range(-l): ys=((ys<<1)|(1-c))&self.mask
                    ys=((ys<<1)|c)&self.mask
                ndx=ndy=0
                for k in range(na-h+1,na+1): ndx=(ndx<<1)|(L[k][nb]-L[k-1][nb])
                for k in range(nb-h+1,nb+1): ndy=(ndy<<1)|(L[na][k]-L[na][k-1])
                return self.reduce_with_flip(pack4(xs,ys,ndx,ndy))
        return None,None

tc2=TC(2); m2=(1<<2)-1
s2,_=tc2.reduce_with_flip(pack4(0,0,m2,m2))
seen={s2}; todo=[s2]; odd_loop=None
while todo and odd_loop is None:
    qq=todo.pop(0)
    for cc in (0,1):
        for ll in range(-1,2):
            tt,ff=tc2.trans(qq,cc,ll)
            if tt is None: continue
            if tt==qq and ff==1:
                odd_loop=(qq,cc,ll,unpack4(qq)); break
            if tt not in seen:
                seen.add(tt); todo.append(tt)
        if odd_loop is not None: break
assert odd_loop is not None and len(seen)<=7

h=8; tc=TC(h); mask=(1<<h)-1
start,_=tc.reduce_with_flip(pack4(0,0,mask,mask))
q1,f1=tc.trans(start,0,+7)
assert q1 is not None and f1==1
q2,f2=tc.trans(q1,0,-7)
assert q2 is not None and f2==0

stored=((0,+7),(0,-7))
gauge=0
physical=[]
q=start
flips=[]
for c,l in stored:
    physical.append((c^gauge,l))
    q,f=tc.trans(q,c,l)
    assert q is not None
    flips.append(f)
    gauge ^= f
assert physical==[(0,+7),(1,-7)]

def pair_bad(u,v):
    c1,l1=u; c2,l2=v
    return c1==c2 and l1*l2<0 and abs(l1)>=2 and abs(l2)>=2
assert pair_bad(*stored)
assert not pair_bad(*physical)

for z in stored+tuple(physical): assert minimal_match_pair(*z)
sa,sb=cat(stored); pa,pb=cat(physical)
Ls=lcs(sa,sb); Lp=lcs(pa,pb)
assert Ls>2 and Lp==2

def canonical_matches(a,b):
    m,n=len(a),len(b); D=[[0]*(n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if a[i-1]==b[j-1]: D[i][j]=D[i-1][j-1]+1
            else: D[i][j]=max(D[i-1][j],D[i][j-1])
    i,j=m,n; out=[]
    while i>0 and j>0:
        if D[i][j]==D[i-1][j]: i-=1
        elif D[i][j]==D[i][j-1]: j-=1
        else:
            out.append((i,j,int(a[i-1]))); i-=1; j-=1
    return tuple(reversed(out)),D[m][n]
cm,cl=canonical_matches(pa,pb)
assert cl==2 and cm==((8,1,0),(9,9,1))

order2=[]
for c1 in (0,1):
    for l1 in range(-8,9):
        for c2 in (0,1):
            for l2 in range(-8,9):
                w=((c1,l1),(c2,l2))
                if not all(minimal_match_pair(*z) for z in w): continue
                aa,bb=cat(w)
                if not (pa.startswith(aa) and pb.startswith(bb)): continue
                ra,rb=pa[len(aa):],pb[len(bb):]
                if lcs(ra,rb)==0:
                    order2.append((w,(ra,rb)))
assert order2==[(((0,+7),(1,-7)),('',''))]

print('R17 C036 exact complement-gauge counterexample')
print('h2_reachable_odd_flip_self_loop =',odd_loop)
print('cocycle_is_not_state_coboundary = True')
print('h =',h)
print('stored_labels =',stored)
print('transition_flip_bits =',tuple(flips))
print('physical_labels =',tuple(physical))
print('naive_pair_filter_rejects_stored =',pair_bad(*stored))
print('correct_physical_pair_filter_rejects =',pair_bad(*physical))
print('stored_generated_strings =',sa,sb)
print('stored_pair_lcs =',Ls)
print('physical_generated_strings =',pa,pb)
print('physical_pair_lcs =',Lp)
print('physical_pair_canonical_backtrack_matches =',cm)
print('physical_list_is_saturated_canonical_collation = True')
print('all_Definition3_2_order2_covers_with_null_suffix =',order2)
print('unique_order2_covering_list = True')
print('naive_filtered_quotient_machine_has_no_order2_cover_for_pair = True')
print('path_accepted_by_h8_canonical_machine = True')
print('EXACT_GAUGE_COUNTEREXAMPLE_PASS')
