#!/usr/bin/env python3
import itertools,re,sys
from math import ceil
import sympy as sp

if len(sys.argv)!=2:
    raise SystemExit('usage: postcheck.py finite_output.txt')
lines=open(sys.argv[1],encoding='utf-8').read().splitlines()
text='\n'.join(lines)
for seg,count in [('A',69245080),('B',113371000),('C',105346400)]:
    needle=f'PASS q4 segment={seg} c=311249/1000000 profiles_total=34 configs={count}'
    assert needle in text, needle
assert 'DONE q5 c=311249/1000000 profiles=22 configs=6047460 uniq=827034 u20=6309 enhanced=2560 enh20=160 fails=160' in text

# Parse every q=5 residual and prove they are exactly one signed-coordinate orbit.
pat=re.compile(r'^FAILCFG\s+\d+\s+pidx=(\d+)\s+profile\s+([0-9 ]+)\s+N=\d+\s+uniq=\d+(.*)$')
fail=[]
for line in lines:
    m=pat.match(line.strip())
    if not m: continue
    blocks=[]
    for piece in m.group(3).split('|'):
        piece=piece.strip()
        if not piece: continue
        ma,pa=map(int,piece.split(':'))
        blocks.append((ma.bit_count(),ma,pa))
    fail.append(tuple(sorted(blocks)))
Fset=set(fail)
assert len(fail)==160 and len(Fset)==160
assert all(tuple(k for k,_,__ in x)==(2,2,4,4,4) for x in Fset)
S=[]
for m in range(16):
    S.append((1,)+tuple(1 if (m>>j)&1 else -1 for j in range(4)))
rep_to_idx={v:i for i,v in enumerate(S)}
def decode_block(mask,plus):
    out=[]
    for ix in range(16):
        if (mask>>ix)&1:
            sg=1 if (plus>>ix)&1 else -1
            out.append(tuple(sg*z for z in S[ix]))
    return out
def encode_block(vecs):
    items=[]
    for y in vecs:
        sg=y[0]
        rep=tuple(sg*z for z in y)
        items.append([rep_to_idx[rep],sg])
    items.sort()
    if items[0][1] < 0:
        items=[[ix,-sg] for ix,sg in items]
    mask=plus=0
    for ix,sg in items:
        mask |= 1<<ix
        if sg>0: plus |= 1<<ix
    return (len(items),mask,plus)
rep=((2,3,3),(2,12,12),(4,1440,160),(4,20560,20560),(4,43520,43520))
blocks=[decode_block(m,p) for _,m,p in rep]
def transform_key(perm,signs):
    out=[]
    for vecs in blocks:
        tv=[tuple(signs[j]*y[perm[j]] for j in range(5)) for y in vecs]
        out.append(encode_block(tv))
    return tuple(sorted(out))
orbit=set()
for perm in itertools.permutations(range(5)):
    for bits in range(16):
        signs=(1,)+tuple(1 if (bits>>(j-1))&1 else -1 for j in range(1,5))
        orbit.add(transform_key(perm,signs))
assert len(orbit)==160 and Fset==orbit

# Exact radical lower obstruction and exact dual certificate for the exceptional orbit.
T=(2*sp.sqrt(2)+3*sp.sqrt(3)+2*sp.sqrt(51+3*sp.sqrt(6)))/13
b=1/sp.sqrt(3); d=1/sp.sqrt(2); a=(T-b)/2; c=(T-d)/3
cstar=sp.simplify(1/T**2); c1=sp.Rational(311249,10**6)
assert sp.simplify(2*a+b-T)==0 and sp.simplify(3*c+d-T)==0
assert sp.simplify(a*a+c*c-sp.Rational(1,2))==0
assert all(x.is_positive for x in (T,a,b,c,d))
A=sp.Matrix([[0,a,0,a,b],[-a,0,0,a,-b],[a,a,0,0,-b],[-c,c,-d,-c,0],[-c,c,d,-c,0]])
for j in range(5): assert sp.simplify(sum(A[i,j]**2 for i in range(5))-1)==0
witness={'----':(0,-1),'---+':(1,-1),'--+-':(4,-1),'--++':(4,-1),'-+--':(0,-1),'-+-+':(1,-1),'-++-':(3,-1),'-+++':(3,-1),'+---':(2,+1),'+--+':(1,-1),'+-+-':(2,+1),'+-++':(0,+1),'++--':(2,+1),'++-+':(1,-1),'+++-':(2,+1),'++++':(0,+1)}
for tail,(ri,mul) in witness.items():
    eps=sp.Matrix([1]+[1 if x=='+' else -1 for x in tail])
    assert sp.simplify(mul*(A.row(ri)*eps)[0]-T)==0
D=sp.simplify(3+a/b+c/d); p=sp.simplify(1/D); q=sp.simplify(p*a/b); r=sp.simplify(p*c/d)
assert sp.simplify(3*p+q+r-1)==0 and all(x.is_positive for x in (p,q,r))
term4=sp.simplify(p*r/(p+3*r)); term3=sp.simplify(p*q/(p+2*q)); dual=sp.simplify(2*term4+3*term3)
assert sp.simplify(term4-p*c/T)==0 and sp.simplify(term3-p*a/T)==0
assert sp.simplify(T*(3*a+2*c)-D)==0 and sp.simplify(dual-cstar)==0

# Screening and analytic regime inequalities.
assert sp.simplify(c1-cstar).is_positive
assert sp.simplify(sp.Rational(1,3)-cstar).is_positive
assert sp.simplify(sp.Rational(49,30)-5*cstar).is_positive
assert sp.simplify(sp.Rational(100,31)-T**2).is_positive

# Exact fixed-envelope movement against the previous sqrt(100/31) envelope.
improved=[]; new_active=[]
for n in range(5,86):
    bal=sp.Rational(3*n,4); oldblk=sp.Rational(100,31)*ceil(n/5); newblk=sp.simplify(T**2*ceil(n/5))
    oldsq=bal if bal <= oldblk else oldblk
    if sp.Lt(newblk,bal)==sp.S.true: newsq=newblk; new_active.append(n)
    else: newsq=bal
    if sp.Lt(newsq,oldsq)==sp.S.true: improved.append(n)
expected=[5]+list(range(9,11))+list(range(13,16))+list(range(18,21))+list(range(22,86))
assert improved==expected and new_active==expected and len(improved)==73
# Crossover: use 333/106 < pi < 22/7 externally; verify exact algebraic sides.
assert sp.Lt(17*T**2,18*sp.Rational(333,106))==sp.S.true
assert sp.Gt(T**2,sp.Rational(22,7))==sp.S.true
assert sp.Gt(sp.Rational(3*86,4),18*sp.Rational(22,7))==sp.S.true

print('q4_configs =',69245080+113371000+105346400)
print('q5_configs =',6047460)
print('q5_exceptional_configs =',len(Fset))
print('exceptional_signed_coordinate_orbit =',len(orbit))
print('T =',sp.N(T,30))
print('cstar =',sp.N(cstar,30))
print('c1-cstar =',sp.N(c1-cstar,30))
print('lambda =',[sp.N(x,20) for x in (p,q,r,p,p)])
print('dual_sum =',sp.N(dual,30))
print('improved_dimensions =',len(improved))
print('R13_K5_EXACT_POSTCHECK_PASS')
