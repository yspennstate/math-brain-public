#!/usr/bin/env python3
"""Exhaustive certificate for the 5-input quarter/half balanced gate slice.

Slice: y has bias 1/4, x1..x4 have bias 1/2, output is balanced.
For any symmetric Gamma with C=Gamma(1/2), g=Gamma(1/4) and the exact
quarter AND constraint g<=C-2, this checker computes the largest center C
forced by any Boolean gate in the slice.

All Walsh transforms, influences, orbit coverage and spectral mass numerators
are exact integers.  Transcendental comparisons are independently replayed
at 100-decimal-digit precision after collapsing 1,453,596 gates to exact
spectral/influence signatures.
"""
import itertools, math, time
from collections import Counter
from decimal import Decimal, getcontext

N=16
pop=[i.bit_count() for i in range(N)]
chi=[[1 if ((t & x).bit_count()%2)==0 else -1 for x in range(N)] for t in range(N)]

# Unnormalised Walsh sums of ±1 truth tables on Q4.
walsh=[]
for mask in range(1<<N):
    w=mask.bit_count(); arr=[2*w-N]
    for t in range(1,N):
        s=0; mm=mask
        while mm:
            lsb=mm & -mm; x=lsb.bit_length()-1
            s += chi[t][x]; mm ^= lsb
        arr.append(2*s)
    walsh.append(tuple(arr))

# Full cube automorphism group: coordinate permutations and bit flips.
maps=[]
for perm in itertools.permutations(range(4)):
    for flip in range(16):
        mp=[]
        for x in range(16):
            y=0
            for j in range(4):
                y |= ((x>>perm[j])&1)<<j
            mp.append(y^flip)
        maps.append(tuple(mp))
assert len(maps)==384 and len(set(maps))==384

def transform(mask,mp):
    out=0; mm=mask
    while mm:
        lsb=mm&-mm; x=lsb.bit_length()-1
        out |= 1<<mp[x]; mm ^= lsb
    return out

def canon(mask):
    return min(transform(mask,mp) for mp in maps)

# Balance at y-bias 1/4 means 3*k0+k1=32.
pairs=[(6,14),(7,11),(8,8),(9,5),(10,2)]
reps={}
for k0,_ in pairs:
    reps[k0]=sorted({canon(sum(1<<i for i in c))
                     for c in itertools.combinations(range(16),k0)})
assert {k:len(v) for k,v in reps.items()}=={6:50,7:56,8:74,9:56,10:50}

# Fast first pass; no floating quantity enters the exact signature.
ent=[0.0]*4097
for n in range(1,4097):
    p=n/4096.0; ent[n]=-p*math.log2(p)
hv=2.0-0.75*math.log2(3.0)

def signature_and_float(m0,m1):
    a=walsh[m0]; b=walsh[m1]
    nums=[]; iy=0; bn=0; H=0.0
    for t in range(16):
        xn=(3*a[t]+b[t])**2
        yn=3*(b[t]-a[t])**2
        nums.extend((xn,yn)); iy+=yn; bn+=pop[t]*(xn+yn)
        H += ent[xn]+ent[yn]
    A=iy/3072.0; B=bn/4096.0; den=A+B-1.0
    sig=(tuple(sorted(Counter(nums).items())),iy,bn)
    if den<=0: return sig,None
    C=(H+A*(2-hv))/den
    return sig,C

signatures=set(); total=0; by_case={}; witness=None; best=-1.0
t0=time.time()
for k0,k1 in pairs:
    g1=[sum(1<<i for i in c) for c in itertools.combinations(range(16),k1)]
    cbest=-1.0; cw=None
    for m0 in reps[k0]:
        for m1 in g1:
            total+=1
            sig,C=signature_and_float(m0,m1); signatures.add(sig)
            if C is not None and C>cbest: cbest=C; cw=(m0,m1)
            if C is not None and C>best: best=C; witness=(m0,m1,k0,k1,sig)
    by_case[(k0,k1)]=(cbest,cw,len(reps[k0])*len(g1))

assert total==1453596
assert len(signatures)==12138
nonpos=[sig for sig in signatures if (sig[1]/3072 + sig[2]/4096 - 1)<=0]
assert nonpos==[(((0,31),(4096,1)),0,4096)] or set(nonpos)=={(((0,31),(4096,1)),0,4096)}

# Independent high-precision replay over every exact signature.
getcontext().prec=100
D=Decimal
ln2=D(2).ln(); l3=D(3).ln()/ln2
E=[D(0)]*4097
for n in range(1,4097):
    p=D(n)/D(4096)
    E[n]=-p*(p.ln()/ln2)

def exactish(sig):
    hist,iy,bn=sig
    H=sum(D(c)*E[n] for n,c in hist)
    A=D(iy)/D(3072); B=D(bn)/D(4096); den=A+B-D(1)
    if den<=0: return None
    return (H+A*(D(3)/D(4))*l3)/den

vals=[]
for sig in signatures:
    c=exactish(sig)
    if c is not None: vals.append((c,sig))
vals.sort(key=lambda x:x[0], reverse=True)
target=D(52)/D(5)-D(27)/D(10)*l3
# Ties are permitted within 1e-80; every non-tied signature must be well below.
eps=D('1e-80')
ties=[(c,s) for c,s in vals if abs(c-target)<=eps]
others=[(c,s) for c,s in vals if abs(c-target)>eps]
assert ties
assert vals[0][0] <= target+eps
assert others[0][0] < target-D('0.1')

m0,m1,k0,k1,sig=witness
a=walsh[m0]; b=walsh[m1]
xnums=[]; ynums=[]; iy=0; bn=0
for t in range(16):
    xn=(3*a[t]+b[t])**2; yn=3*(b[t]-a[t])**2
    xnums.append(xn); ynums.append(yn); iy+=yn; bn+=pop[t]*(xn+yn)
assert (m0,m1)==(63,32639)
assert Counter(xnums)==Counter({1296:1,256:3,144:3,16:4,0:5})
assert Counter(ynums)==Counter({768:1,432:1,48:7,0:7})
assert iy==1536 and bn==4608 # It_y=3/8; B=9/8

# Exact closed-form entropy from the certified histogram.
Htarget=D(13)/D(2)-D(33)/D(16)*l3
Hsig=sum(D(c)*E[n] for n,c in Counter(xnums+ynums).items())
assert abs(Hsig-Htarget)<eps

print('PASS quarter-slice arity-5 exhaustive certificate')
print('orbit_reps', {k:len(v) for k,v in reps.items()})
for kk in pairs:
    print('case',kk,'pairs',by_case[kk][2],'float_best','%.15f'%by_case[kk][0], 'witness',by_case[kk][1])
print('total_gate_pairs',total)
print('unique_exact_signatures',len(signatures))
print('zero_currency_signature = character: H=0, A=0, B=1 (automatic equality)')
print('max_center_exact_form = 52/5 - (27/10) log2(3)')
print('max_center_decimal =', target)
print('next_distinct_signature =', others[0][0])
print('gap_to_next_distinct =', target-others[0][0])
print('maximizer_branch_masks',m0,m1)
print('maximizer_branch0_positive',[i for i in range(16) if (m0>>i)&1])
print('maximizer_branch1_positive',[i for i in range(16) if (m1>>i)&1])
print('maximizer_H_exact_form = 13/2 - (33/16) log2(3)')
print('maximizer_H_decimal =',Htarget)
print('maximizer_It_y = 3/8; A=1/2; B=9/8; denominator=5/8')
print('X_mass_numerators_over_4096',sorted(Counter(xnums).items()))
print('Y_mass_numerators_over_4096',sorted(Counter(ynums).items()))
print('runtime_seconds','%.3f'%(time.time()-t0))
