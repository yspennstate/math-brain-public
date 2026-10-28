"""Adversarial independent active-set and endpoint audit, bounded to 55s."""
from check import *
import check

start=time.perf_counter();cases=0
for mask in range(0,256,17):
    v=tuple(1 if mask>>t&1 else -1 for t in range(8));p=direct(v)
    ck(p==spectrum(v))
    a=1-p[0]
    if not a:continue
    pi=tuple(z/a for z in p[1:]);N=len(pi)
    for c in (F(1,4),F(3,4)):
        T=tuple(F(j+1,N*(N+1)//2) for j in range(N));l=tuple(c*x for x in T)
        x,k=projection(pi,l);ck(enumerate_projection(pi,l)=={x})
        A=[j for j in range(N) if l[j]>=k*pi[j]];C=[j for j in range(N) if j not in A]
        pa=sum((pi[j] for j in A),F(0));pc=1-pa;la=sum((l[j] for j in A),F(0))
        ck(pc>0 and 1-la>0);ck(k==(1-la)/pc)
        form=add(*[(pi[j],logq(pi[j]/l[j])) for j in A if pi[j]],(pc,logq(pc/(1-la))))
        ck(form==KL(pi,x))
        upper=logq(1/(1-c));ck(bounds(add((1,upper),(-1,form)))[0]>=0)
        cases+=1
        ck(time.perf_counter()-start<55)
# Actual character, matched source: a target on a ghost forces positive debt.
p=spectrum((1,-1,1,-1));ck(p==(F(0),F(1),F(0),F(0)))
pi=p[1:];l=(F(0),F(1,4),F(0));x,k=projection(pi,l)
ck(x==(F(3,4),F(1,4),F(0)));ck(KL(pi,x)==logq(F(4,3)))
ck(bounds(KL(pi,x))[0]>0)
# c=1 can force infinite CE; it is excluded from the theorem.
T=(F(0),F(1),F(0));ck(pi[0]>0 and T[0]==0)
# The same source meets a=0 only when constant: conversion costs exactly zero.
pc=spectrum((1,1));ck(pc==(F(1),F(0)))
ck(CE(pc,(F(1,2),F(1,2)))==logq(F(2)))
out={'status':'PASS','cases':cases,'exact_assertions':check.COUNT,'seconds':time.perf_counter()-start,'independence':'direct characters, complete active-subset enumeration, scalar formula and boundary guards','lean_status':'NOT_RUN_MEMOK_EXIT_1: physical free3.9GB<4.0GB; saved Lean statement is not a certificate'}
(RUN/'out/AUDIT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
