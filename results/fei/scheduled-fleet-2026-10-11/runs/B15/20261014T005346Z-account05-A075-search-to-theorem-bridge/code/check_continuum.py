from pathlib import Path
from fractions import Fraction as Q
import json,time
ROOT=Path(__file__).resolve().parents[1]
from arithmetic import *
import arithmetic as arithmetic_state
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter()
SOURCE=Path('~/brain_workers/FEI100_20261011/agents/A084/runs/20261014T000747Z-account05-A084-continuum-parameters')
def trim(a):
    a=list(a)
    while len(a)>1 and not a[-1]:a.pop()
    return a
def pa(a,b):
    c=[Q(0)]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]+=x
    for i,x in enumerate(b):c[i]+=x
    return trim(c)
def ps(a,c):return trim([x*c for x in a])
def pm(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)
def pw(a,k):
    b=[Q(1)]
    for _ in range(k):b=pm(b,a)
    return b
ONE=[Q(1)];M=[Q(0),Q(1)];PLUS=[Q(1),Q(1)];MINUS=[Q(-1),Q(1)];THREE=[Q(3),Q(1)]
S=[Q(-1),Q(2),Q(1)];PP=[Q(-11),Q(-4),Q(2),Q(4),Q(1)];V=[Q(1),Q(0),Q(-1)]
C0=ps(pm(S,PP),Q(1,16));D0=ps(pm(pm(MINUS,pw(PLUS,3)),THREE),Q(1,16))
num=[pw(C0,2),pw(pm(pm(MINUS,PLUS),THREE),2),pw(S,2),pw(PLUS,2)]
den=[pw(D0,2),pw(S,2),pw(PLUS,2),ONE]
wa=ps(pm(pm(pw(S,2),pw(PLUS,2)),pa(ps(pm(V,pw(PLUS,2)),Q(4)),ps(pw(V,2),Q(2)))),Q(1,256))
wb=ps(pm(pm(pw(V,2),pw(PLUS,4)),pw(THREE,2)),Q(1,256))
wc=[Q(0)]
for z in [pm(pm(pm(V,pw(MINUS,2)),pw(PLUS,4)),pw(THREE,2)),ps(pm(pm(pw(V,2),pw(PLUS,2)),pw(S,2)),Q(4)),ps(pm(pw(V,3),pw(S,2)),Q(2)),ps(pm(pw(V,3),pw(PLUS,4)),Q(4)),ps(pm(pw(V,4),pw(PLUS,2)),Q(4)),pw(V,5)]:wc=pa(wc,z)
weights=[pw(D0,2),wa,wb,ps(wc,Q(1,256))]
NEG={0,1,2,4,8,16,32,6,17,40};truth=[-1 if x in NEG else 1 for x in range(64)]
W=fwht(truth);grouped=[[Q(0)] for _ in range(4)];rows=[]
for T in range(32):
    mask=T<<1;k=T.bit_count();c=[Q(0)]*(7-k);d=[Q(0)]*(6-k)
    for Z,w in enumerate(W):
        if Z&mask==mask:c[Z.bit_count()-k]+=Q(w,64)
        if Z&(mask|1)==mask|1:d[Z.bit_count()-k-1]+=Q(w,64)
    c=trim(c);d=trim(d)
    matches=[]
    for j in range(4):
        if pa(pm(pw(c,2),den[j]),ps(pm(pw(d,2),num[j]),Q(-1)))==[Q(0)]:matches.append(j)
    ck(len(matches)==1);j=matches[0]
    grouped[j]=pa(grouped[j],pm(pw(V,k),pw(d,2)))
    rows.append({'T':T,'group':j,'C_poly':[str(x) for x in c],'D_poly':[str(x) for x in d]})
for a,b in zip(grouped,weights):ck(a==b)
q=ps(pm(pm(ps(MINUS,Q(-1)),pw(PLUS,3)),THREE),Q(1,16))
sumw=[Q(0)]
for w in weights:sumw=pa(sumw,w)
ck(sumw==q)
# Directly check generators of the transitive matching automorphism action.
for perm in [[4,1,2,3,0,5],[0,2,1,3,4,5],[1,0,4,3,2,5],[3,1,2,0,5,4]]:
    for x in range(64):
        y=sum(((x>>i)&1)<<perm[i] for i in range(6))
        ck(truth[x]==truth[y])
(ROOT/'out'/'INDEPENDENT_PACKET_ALGEBRA.json').write_text(json.dumps({'packets':rows,'group_weights_exact':True,'sum_weights_q_exact':True,'symmetry_checks':256},indent=2)+'\n')

def ia(a,b):return a[0]+b[0],a[1]+b[1]
def im(a,b):
    z=[x*y for x in a for y in b];return min(z),max(z)
def idiv(a,b):
    ck(not(b[0]<=0<=b[1]));return im(a,(1/b[1],1/b[0]))
def ipow(a,k):
    if k%2==0:
        return (Q(0) if a[0]<=0<=a[1] else min(a[0]**k,a[1]**k),max(a[0]**k,a[1]**k))
    return a[0]**k,a[1]**k
def const(x):return Q(x),Q(x)
def poly(a,m):
    r=const(0)
    for x in reversed(a):r=ia(im(r,m),const(x))
    return r
def ilog(a):
    ck(a[0]>0)
    l=log_interval(a[0].numerator)[0]-log_interval(a[0].denominator)[1]
    u=log_interval(a[1].numerator)[1]-log_interval(a[1].denominator)[0]
    return l,u
def slope(m):
    # Factored expressions reduce interval dependency; independent exact algebra
    # above links these expressions to the complete truth-table packets.
    one=const(1);v=ia(one,im(const(-1),ipow(m,2)))
    plus=ia(m,one);minus=ia(m,const(-1));three=ia(m,const(3))
    s=ia(ia(ipow(m,2),im(const(2),m)),const(-1))
    pp=poly(PP,m);c0=im(const(Q(1,16)),im(s,pp));d0=im(const(Q(1,16)),im(im(minus,ipow(plus,3)),three))
    us=[ipow(idiv(c0,d0),2),ipow(idiv(im(im(minus,plus),three),s),2),ipow(idiv(s,plus),2),ipow(plus,2)]
    w0=ipow(d0,2)
    wA=im(const(Q(1,256)),im(im(ipow(s,2),ipow(plus,2)),ia(im(const(4),im(v,ipow(plus,2))),im(const(2),ipow(v,2)))))
    wB=im(const(Q(1,256)),im(im(ipow(v,2),ipow(plus,4)),ipow(three,2)))
    wC=const(0)
    for z in [im(im(im(v,ipow(minus,2)),ipow(plus,4)),ipow(three,2)),im(const(4),im(im(ipow(v,2),ipow(plus,2)),ipow(s,2))),im(const(2),im(ipow(v,3),ipow(s,2))),im(const(4),im(ipow(v,3),ipow(plus,4))),im(const(4),im(ipow(v,4),ipow(plus,2))),ipow(v,5)]:wC=ia(wC,z)
    wC=im(const(Q(1,256)),wC);r=const(0)
    for w,u in zip([w0,wA,wB,wC],us):
        ck(w[0]>0);r=ia(r,im(w,ilog(idiv(u,ipow(m,2)))))
    return r
cert=[]
for name in ['MINORITY_ORIENTATION.json','COMPLEMENT_ORIENTATION.json']:
    source=json.loads((SOURCE/'out'/name).read_text());leaves=source['leaves']
    ck(Q(leaves[0]['m_box'][0])==Q(source['domain'][0]));ck(Q(leaves[-1]['m_box'][1])==Q(source['domain'][1]))
    for i,leaf in enumerate(leaves):
        a,b=map(Q,leaf['m_box'])
        if i:ck(a==Q(leaves[i-1]['m_box'][1]))
        for j in range(16):
            l=a+(b-a)*Q(j,16);u=a+(b-a)*Q(j+1,16)
            lo,hi=slope((l,u));ck(lo>0)
            cert.append({'m_box':[str(l),str(u)],'slope_interval':[str(lo),str(hi)]})
ck(len(cert)==208)
(ROOT/'out'/'INDEPENDENT_CONTINUUM_CERTIFICATE.json').write_text(json.dumps({'precision_bits':192,'atanh_terms':80,'boxes':cert,'min_lower':str(min(Q(x['slope_interval'][0]) for x in cert)),'domain':['9/16..7/8','-9/16..-1/2'],'runtime_seconds':time.perf_counter()-start,'checks':arithmetic_state.checks},indent=2)+'\n')
print(json.dumps({'boxes':len(cert),'checks':arithmetic_state.checks,'runtime_seconds':time.perf_counter()-start,'minimum_lower':float(min(Q(x['slope_interval'][0]) for x in cert))}))
