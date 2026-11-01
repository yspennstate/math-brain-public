import exact as e
from exact import Q,ck,cutoff,save,logint
from collections import Counter
import json,time
data=json.loads((e.ROOT/'out/CONTINUUM_CERTIFICATES.json').read_text());boxes=data['certificates'];ck(len(boxes)==1024)
for pi,p in enumerate(data['profiles']):
    group=[x for x in boxes if x['profile']==pi];ck(len(group)==256);cursor=Q(1,32)
    profile=Counter(Q(c) for c in p)
    for row in group:
        cutoff();lo=Q(row['lo']);hi=Q(row['hi']);ck(lo==cursor);ck(hi-lo==Q(3,8192));cursor=hi
        upper=Q(0)
        for c,multiplicity in profile.items():
            A=max((c-lo)**2,(c-hi)**2);B=hi*hi
            upper+=multiplicity*(A*logint(1+B/A)[1]+B*logint(1+A/B)[1])
        lower=2*lo+16*lo*lo-upper;ck(lower>0);ck(Q(row['gap_lower'])<=lower)
    ck(cursor==Q(1,8))
f=[1 if x.bit_count()>=2 else -1 for x in range(16)]
def place(x,A):return sum(((x>>j)&1)<<i for j,i in enumerate(A))
cofactors=[];partitions=[]
for j in range(4):
    A=[i for i in range(4) if i!=j];children=[]
    for bit in (0,1):
        g=[f[place(x,A)|(bit<<j)] for x in range(8)];children.append(g)
        support=[A[k] for k in range(3) if any(g[x]!=g[x^(1<<k)] for x in range(8))];ck(support==A)
        cofactors.append({'query':j,'value':bit,'truth_table':g,'support':support})
    mismatch=sum(a!=b for a,b in zip(*children));ck(mismatch==3)
    for row in cofactors[-2:]:row['paired_disagreement_count']=mismatch
for mask in range(1,15,2):
    A=[i for i in range(4) if mask>>i&1];B=[i for i in range(4) if not mask>>i&1];witness=None
    for a in range(1<<len(A)):
        for b in range(1<<len(B)):
            lhs=f[place(a,A)|place(b,B)]*f[0];rhs=f[place(a,A)]*f[place(b,B)]
            if lhs!=rhs:witness={'a':a,'b':b,'lhs':lhs,'rhs':rhs}
    ck(witness is not None);partitions.append({'A':A,'B':B,'nonproduct_minor':witness})
save('NONMEMBER_CERTIFICATE.json',{'status':'PASS','function':f,'cofactors':cofactors,'partitions':partitions,'point_rule_excluded':'every cofactor pair differs on3 shared rows, whereas the private-free single-point rule differs on at most1'})
save('VERIFY_RESULTS.json',{'status':'PASS','box_count':1024,'assertions':e.checks,'elapsed_seconds':time.perf_counter()-e.start,'method':'positive direct-log Phi upper enclosures independent of prime-log producer; exact coverage and integer nonmember certificates'})
print({'status':'PASS','assertions':e.checks,'seconds':time.perf_counter()-e.start})
