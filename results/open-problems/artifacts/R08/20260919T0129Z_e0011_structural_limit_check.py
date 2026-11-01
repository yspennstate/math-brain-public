#!/usr/bin/env python3
from collections import deque

DIRS=((1,0),(-1,0),(0,1),(0,-1))
def neigh(c):
    x,y=c; return {(x+dx,y+dy) for dx,dy in DIRS}
def support(label):
    k,a=label
    roots={a} if k=='CO' else set(a)
    S=set(roots)
    for r in roots:S |= neigh(r)
    return S

# B13: infinite-budget trap for the one-vacancy seed in the maximal 16-cell local patch.
SC=[(-2,0),(-2,1),(-1,-1),(-1,0),(-1,1),(-1,2),(0,-1),(0,0),(0,1),(0,2),(1,-1),(1,0),(1,1),(1,2),(2,0),(2,1)]
SI={c:i for i,c in enumerate(SC)}; P3=[3**i for i in range(len(SC))]; SCset=set(SC)
def get(s,i): return (s//P3[i])%3
def put(s,i,v): return s+(v-get(s,i))*P3[i]
def nidx(c):return [SI[z] for z in neigh(c) if z in SI]
def all_local_labels():
    labs=[]
    for c in SC:
        lab=('CO',c)
        if support(lab)<=SCset: labs.append(lab)
    edges=set()
    for u in SC:
        for v in neigh(u):
            if v in SCset:
                e=tuple(sorted((u,v)))
                lab=('O2',e)
                if support(lab)<=SCset: edges.add(e)
    labs += [('O2',e) for e in sorted(edges)]
    return labs
LABS=all_local_labels()
assert len(LABS)==13
assert sum(1 for k,_ in LABS if k=='CO')==6
assert sum(1 for k,_ in LABS if k=='O2')==7

def trans(s,lab):
    k,a=lab; out=set()
    if k=='CO':
        i=SI[a]
        if get(s,i)!=0:return {s}
        u=put(s,i,1)
        os=[j for j in nidx(a) if get(u,j)==2]
        if not os:return {u}
        for j in os:out.add(put(put(u,i,0),j,0))
        return out
    a,b=a; ia,ib=SI[a],SI[b]
    if get(s,ia)!=0 or get(s,ib)!=0:return {s}
    u=put(put(s,ia,2),ib,2)
    ca=[j for j in nidx(a) if get(u,j)==1] or [-1]
    cb=[j for j in nidx(b) if get(u,j)==1] or [-1]
    for ja in ca:
        for jb in cb:
            t=u
            if ja!=-1:t=put(put(t,ia,0),ja,0)
            if jb!=-1:t=put(put(t,ib,0),jb,0)
            out.add(t)
    return out
TARGET={(-1,0),(-1,1),(0,0),(0,1),(1,0),(1,1)}
def is_target(s):return all(get(s,SI[c])==0 for c in TARGET)
TRAP=5513529
assert get(TRAP,SI[(-1,0)])==0
for c in SC:
    vc=get(TRAP,SI[c])
    for z in neigh(c):
        if z in SI:
            vz=get(TRAP,SI[z])
            assert not ((vc==1 and vz==2) or (vc==2 and vz==1))
q=deque([TRAP]); seen={TRAP}
while q:
    s=q.popleft(); assert not is_target(s)
    for lab in LABS:
        for t in trans(s,lab):
            if t not in seen:seen.add(t);q.append(t)
assert len(seen)==6
for s in seen:
    for lab in LABS: assert trans(s,lab)<=seen

# B29: exact L=7 coarse overlap and semantic counter-witness to deleting it naively.
def shift(S,dx=0,dy=0):return {(x+dx,y+dy) for x,y in S}
def shifted_edges(E,dx):return {tuple(sorted(((a[0]+dx,a[1]),(b[0]+dx,b[1])))) for a,b in E}
def interference(S):
    co=set(S)
    for s in tuple(S):co|=neigh(s)
    ed=set()
    for u in co:
        for v in neigh(u):ed.add(tuple(sorted((u,v))))
    return co,ed
LABELS7=(('CO',(0,0)),('O2',((-1,1),(0,1))),('CO',(0,1)),('CO',(1,0)),('O2',((-1,0),(-1,1))),('O2',((0,0),(0,1))),('CO',(-1,1)))
READ=set()
for lab in LABELS7:READ|=support(lab)
LABELS9=LABELS7+(('O2',((-1,0),(0,0))),('CO',(-1,0)))
READ_TERM=set()
for i,lab in enumerate(LABELS9):
    if i!=3:READ_TERM|=support(lab)
def read_down(a):return {(a+y,-x) for x,y in READ}
def read_up(a):return {(a+y,x+1) for x,y in READ}
OPARENT={(-3,0),(-2,0)};CPARENT=(-4,1);OCC=OPARENT|{CPARENT};CURSOR1={(0,0),(0,1)};PARENT_CORE=OCC|CURSOR1
def geometry1(L):
    Ochild=tuple(sorted(((L-3,0),(L-2,0))));Cchild=(L-4,1);child_cursor={(L,0),(L,1)}
    pbuf=support(('O2',Ochild))|support(('CO',Cchild));down=(L-3,L-2);up=(L-4,L-3)
    guards={(x,-1) for x in down}|{(x,2) for x in up};corridor={(x,y) for x in range(0,L+1) for y in (0,1)};req=pbuf|child_cursor|guards;st=[]
    for c in range(2,L+1):
        R=shift(READ_TERM if c==L else READ,c-1,0); cleared={(x,y) for x in range(0,c) for y in (0,1)}
        S=PARENT_CORE|R|(req&cleared); st.append(S)
    gd,gu=read_down(down[0]),read_up(up[0]); cleared=corridor.copy();st.append(PARENT_CORE|gd|child_cursor|pbuf|(guards&cleared));cleared|={(x,-1) for x in down};st.append(PARENT_CORE|gu|child_cursor|pbuf|(guards&cleared))
    final=PARENT_CORE|child_cursor|pbuf|guards;return st,final
def deps(L):
    st,final=geometry1(L);co=set();ed=set()
    for S in st+[final]:a,b=interference(S);co|=a;ed|=b
    return co,ed
co7,ed7=deps(7); shared=ed7 & shifted_edges(ed7,14)
assert not (co7 & shift(co7,14,0))
assert shared=={((8,1),(9,1))}

def stable_dict(st):
    for c,v in st.items():
        for z in neigh(c):
            w=st.get(z,0)
            if (v,w) in ((1,2),(2,1)): return False
    return True
def o2_deterministic(st,a,b):
    st=dict(st); assert st.get(a,0)==0 and st.get(b,0)==0
    st[a]=2;st[b]=2
    choices=[]
    for r in (a,b): choices.append(sorted(z for z in neigh(r) if st.get(z,0)==1))
    assert all(len(c)<=1 for c in choices), choices
    for r,cs in zip((a,b),choices):
        if cs:
            c=cs[0];st[r]=0;st[c]=0
    return {k:v for k,v in st.items() if v}
init={(-1,2):1,(1,1):1}
assert stable_dict(init)
assert all(init.get(c,0)==0 for c in [(-1,0),(-1,1),(0,0),(0,1),(1,0)])
controlled=((-1,1),(0,1)); edge=((2,1),(3,1))
noedge=o2_deterministic(init,*controlled)
assert all(noedge.get(c,0)==0 for c in TARGET)
afteredge=o2_deterministic(init,*edge)
withedge=o2_deterministic(afteredge,*controlled)
assert withedge.get((0,1),0)==2
assert not all(withedge.get(c,0)==0 for c in TARGET)

print('PASS exact R08/E0011 structural limit-and-boundary checks')
print('maximal_support_preserving_labels_16cell=',len(LABS),'CO=',6,'O2=',7)
print('one_vacancy_trap_start=',TRAP,'closed_reachable_class_size=',len(seen),'target_reachable=',False)
print('L7_shared_CO=',sorted(co7 & shift(co7,14,0)))
print('L7_shared_edges=',sorted(shared))
print('L7_semantic_witness_noedge_target=',all(noedge.get(c,0)==0 for c in TARGET))
print('L7_semantic_witness_withedge_target=',all(withedge.get(c,0)==0 for c in TARGET))
print('L7_withedge_residual_target_occupancy=',sorted((c,withedge.get(c,0)) for c in TARGET if withedge.get(c,0)))
