from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
import json,time,sys
R=Path(__file__).resolve().parents[1];checks=0
def ck(v):
    global checks
    checks+=1
    assert v,checks
def factor(n):
    a={};p=2
    while p*p<=n:
        while n%p==0:a[p]=a.get(p,0)+1;n//=p
        p+=1
    if n>1:a[n]=a.get(n,0)+1
    return a
def clean(a):return {p:v for p,v in a.items() if v}
def sumlog(*args):
    a=defaultdict(F)
    for b in args:
        for p,v in b.items():a[p]+=v
    return clean(a)
def mul(a,c):return clean({p:v*c for p,v in a.items()})
def number(q):return {2:F(q)} if q else {}
def eta(q):
    if not q:return {}
    a=defaultdict(F)
    for n,s in ((q.numerator,-1),(q.denominator,1)):
        for p,k in factor(n).items():a[p]+=s*k*q
    return clean(a)
def phi(a,b):return sumlog(eta(a),eta(b),mul(eta(a+b),-1))
@lru_cache(None)
def ln_unit(q):
    v=(q-1)/(q+1);ck(0<=v<=F(1,3));s=F(0)
    for j in range(32):s+=2*v**(2*j+1)/F(2*j+1)
    err=2*v**65/F(65)/(1-v*v)
    return s,s+err
@lru_cache(None)
def logprime(p):
    if p==2:return F(1),F(1)
    k=p.bit_length()-1;l,h=ln_unit(F(p,1<<k));l2,h2=ln_unit(F(2))
    return k+l/h2,k+h/l2
def bounds(a):
    lo=hi=F(0)
    for p,c in a.items():
        l,h=logprime(p);lo+=c*(l if c>=0 else h);hi+=c*(h if c>=0 else l)
    return lo,hi
def between(a,l,h):
    low,high=bounds(a);ck(low>l and high<h)
def positive(a):ck(bounds(a)[0]>0)
def encode(a):return {str(p):str(v) for p,v in a.items()}
def receipt(a):
    l,h=bounds(a)
    return {'prime_log_coefficients':encode(a),'lower':str(l),'upper':str(h),'outward_millionths':[int(l//F(1,10**6)),int(-((-h)//F(1,10**6)))]}
@lru_cache(None)
def spectrum(table):
    N=len(table);a=tuple(F(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(table)),N) for s in range(N));ck(sum(v*v for v in a)==1);return a
def entropy(table):return sumlog(*(eta(v*v) for v in spectrum(table)))
def influence(table,j):return F(sum(table[x]!=table[x^(1<<j)] for x in range(len(table))),len(table))
def totalI(table):return sum(influence(table,j) for j in range(len(table).bit_length()-1))
def erasure(table,j):
    a=spectrum(table);return sumlog(*(phi(a[z]**2,a[z|(1<<j)]**2) for z in range(len(a)) if not (z>>j)&1))
def insert(z,j,bit):return (z&((1<<j)-1))|(bit<<j)|((z>>j)<<(j+1))
def restrict(table,labels,j,bit):
    idx=labels.index(j);child=tuple(table[insert(z,idx,bit)] for z in range(len(table)//2));aa=spectrum(table);ac=spectrum(child)
    for z,v in enumerate(ac):ck(v==aa[insert(z,idx,0)]+(1 if bit==0 else -1)*aa[insert(z,idx,1)])
    return child,tuple(x for x in labels if x!=j)
def stopped(table,labels,order):
    if not order:return {},entropy(table),totalI(table)
    j=order[0];rootB=erasure(table,labels.index(j));rootI=influence(table,labels.index(j));sons=[]
    for bit in (0,1):
        child,clabels=restrict(table,labels,j,bit);sons.append(stopped(child,clabels,order[1:]))
    B=sumlog(rootB,mul(sons[0][0],F(1,2)),mul(sons[1][0],F(1,2)));H=mul(sumlog(sons[0][1],sons[1][1]),F(1,2));I=(sons[0][2]+sons[1][2])/2
    ck(totalI(table)==rootI+(totalI(restrict(table,labels,j,0)[0])+totalI(restrict(table,labels,j,1)[0]))/2)
    return B,H,I
def encoder_formula(bt,ct):
    ab=spectrum(bt);ac=spectrum(ct);ans={}
    for u,v in zip(ab,ac):
        a=(u+v)/2;d=(u-v)/2
        ans=sumlog(ans,phi(a*a,d*d/4),mul(phi((a+d/2)**2,d*d/4),F(1,2)),mul(phi((a-d/2)**2,d*d/4),F(1,2)),number(d*d/2),mul(phi(a*a,d*d),F(1,2)))
    return ans
start=time.perf_counter();pilot='--pilot' in sys.argv
b=tuple(1 if y&7==0 else -1 for y in range(64));c=tuple(-1 if y==0 else b[y] for y in range(64))
root=tuple((1 if (z>>6).bit_count()<=1 else -1) if (z&63)==0 else b[z&63] for z in range(512));labels=tuple(range(9))
shadow=tuple((1 if (z>>6)==0 else -1) if (z&63)==0 else b[z&63] for z in range(128))
I0=(totalI(b)+totalI(c))/2;ck(I0==F(3,4));T0=mul(sumlog(entropy(b),entropy(c)),F(1,2));S=sumlog(number(4*I0),mul(T0,-1));Q=erasure(shadow,6);reserve=sumlog(Q,number(F(1,64)))
E0,term0,leafI0=stopped(root,labels,(6,7,8));ck(E0==encoder_formula(b,c));ck(term0==T0 and leafI0==I0);positive(sumlog(E0,mul(reserve,-1)))
# The physical unlocking state A+v*Maj3*D has disjoint residual gate supports across v.
# A occupies the empty gate mask and Maj3 has zero mean, so every v erasure packet is zero.
am=spectrum(b);cm=spectrum(c);maj=spectrum(tuple(1 if x.bit_count()<=1 else -1 for x in range(8)))
ck(maj[0]==0)
for T in range(64):
    for V in range(8):ck(phi(((am[T]+cm[T])/2)**2 if V==0 else F(0),((am[T]-cm[T])/2)**2*maj[V]**2)=={})
# Exact complete empty-mask derivative mass; A082 review text has an extra delta factor.
ar=spectrum(root);gate_e=influence(root,6);empty_mass=sum(ar[T|(1<<6)]**2/gate_e for T in range(64));ck(empty_mass==F(1,2));ck(empty_mass!=F(1,128))
# Actual physical parity partner has zero erasure, and either child is the unlocked sign up to gate sign reversal.
parity=tuple((1 if (((z>>6)&1)^((z>>7)&1))==0 else -1) if (z&63)==0 else b[z&63] for z in range(256))
ck(erasure(parity,7)=={});ck(influence(parity,7)==F(1,64))
records=[]
for j in ([0] if pilot else range(6)):
    W,T,Il=stopped(root,labels,(j,6,7,8));e=influence(root,j);ck(e==(F(15,64) if j<3 else F(1,64)))
    ck(erasure(root,j)==erasure(shadow,j));childE={};naive={}
    for bit in (0,1):
        bj,bl=restrict(b,tuple(range(6)),j,bit);cj,cl=restrict(c,tuple(range(6)),j,bit)
        childE=sumlog(childE,mul(encoder_formula(bj,cj),F(1,2)))
        # The physical shadow has the same core restriction; inherited origin mass is halved fairly.
        sj,sl=restrict(shadow,tuple(range(7)),j,bit)
        naive=sumlog(naive,mul(erasure(sj,sl.index(6)),F(1,2)))
    naive=sumlog(naive,number(F(1,64)));interaction=sumlog(childE,mul(naive,-1));positive(interaction)
    ck(W==sumlog(erasure(root,j),childE))
    release=sumlog(T0,mul(T,-1));frozen=sumlog(S,mul(W,-1));balance=sumlog(number(4*I0),mul(W,-1),mul(T,-1));positive(balance)
    ck(balance==sumlog(S,mul(reserve,-1),mul(sumlog(W,mul(reserve,-1)),-1),release))
    childS=sumlog(number(4*(I0-e)),mul(T,-1));ck(childS==sumlog(S,number(-4*e),release))
    if j<3:between(frozen,F(-28552,10**6),F(-28551,10**6));ck(bounds(balance)[0]>F(1112678,10**6))
    else:between(frozen,F(546819,10**6),F(546820,10**6));ck(bounds(balance)[0]>F(634309,10**6))
    records.append({'j':j,'influence':str(e),'W':receipt(W),'T':receipt(T),'frozen_balance':receipt(frozen),'terminal_release':receipt(release),'same_original_bank_balance':receipt(balance),'included_encoder_interaction':receipt(interaction)})
two=[]
for j,k in ([(0,1)] if pilot else [(j,k) for j in range(6) for k in range(6) if j!=k]):
    W,T,Il=stopped(root,labels,(j,k,6,7,8));balance=sumlog(number(4*I0),mul(W,-1),mul(T,-1));positive(balance)
    old=next((v for v in records if v['j']==j),None)
    # Direct difference from first policy is the exact continuation debit, not a fresh child quota.
    W1,T1,_=stopped(root,labels,(j,6,7,8));inc=sumlog(W,mul(W1,-1));rel=sumlog(T1,mul(T,-1))
    ck(balance==sumlog(number(4*I0),mul(W1,-1),mul(T1,-1),mul(inc,-1),rel))
    two.append({'ordered_queries':[j,k],'same_original_bank_balance':receipt(balance),'continuation_increment':receipt(inc),'further_terminal_release':receipt(rel)})
# Translation changes phase only; the labeled child laws are not determined by the common parent squared law.
translated=tuple(root[z^1] for z in range(512));ar=spectrum(root);at=spectrum(translated);ck(tuple(v*v for v in ar)==tuple(v*v for v in at))
u,ul=restrict(root,labels,0,0);v,vl=restrict(translated,labels,0,0);pu=tuple(a*a for a in spectrum(u));pv=tuple(a*a for a in spectrum(v));ck(pu!=pv)
phase={'same_parent_squared_spectrum':True,'same_labeled_query':0,'same_physical_outcome':0,'different_child_squared_spectra':True,'witness_child_mask':next(z for z in range(len(pu)) if pu[z]!=pv[z])};z=phase['witness_child_mask'];phase['child_probabilities']=[str(pu[z]),str(pv[z])]
out={'status':'PASS','helper_version':'A081-phase-terminal-history-v1','pilot':pilot,'assertions':checks,'first_data_policies':records,'ordered_two_data_policies':two,'source_claim_review':'All original numeric intervals and complete phase/terminal accounting PASS' if not pilot else 'Pilot only','phase_ambiguity_witness':phase,'review_normalization_fixture':{'delta':'1/64','E_i':'1/2','a_i':'1/2','complete_empty_mask_mass':str(empty_mass),'incorrect_A082_review_text_value':'1/128','original_A096_formula_unchanged':True},'I0':str(I0),'original_surplus':receipt(S),'actual_initial_encoder_erasure':receipt(E0),'pending_shadow_reservation':receipt(reserve),'runtime_seconds':time.perf_counter()-start,'logarithm_certificate':'32-term rational atanh series on [1,2], remainder <=2v^65/(65(1-v^2)); rational interval division by ln2'}
(R/'out'/('PILOT.json' if pilot else 'EXACT_HISTORY.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({'status':out['status'],'assertions':checks,'first_policies':len(records),'two_data_policies':len(two),'runtime_seconds':out['runtime_seconds'],'phase_witness':phase},indent=2))
