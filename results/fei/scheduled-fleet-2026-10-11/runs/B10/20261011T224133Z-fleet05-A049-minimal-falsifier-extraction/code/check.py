from fractions import Fraction as F
from pathlib import Path
from itertools import product
import json, time, hashlib

RUN=Path(__file__).resolve().parents[1]
OUT=RUN/'out'
OUT.mkdir(exist_ok=True)
count=0
def check(v):
    global count
    assert v
    count+=1
def wire(v):
    if isinstance(v,F): return str(v)
    if isinstance(v,dict): return {str(k):wire(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)): return [wire(x) for x in v]
    return v
def save(name,v):
    (OUT/name).write_text(json.dumps(wire(v),indent=2)+'\n',encoding='utf-8')

def walsh(table):
    N=len(table)
    return [sum(table[x]*(-1 if (s&x).bit_count()%2 else 1) for x in range(N)) for s in range(N)]
def fwht(table):
    a=list(table); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]; a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def centered_masses(table,biases):
    n=len(biases); out=[]
    for s in range(1<<n):
        v=F(0); norm=F(1)
        for i,p in enumerate(biases):
            if s>>i&1: norm*=p*(1-p)
        for x in range(1<<n):
            prob=F(1); basis=F(1)
            for i,p in enumerate(biases):
                bit=x>>i&1
                prob*=p if bit else 1-p
                if s>>i&1: basis*=bit-p
            v+=prob*table[x]*basis
        out.append(v*v/norm)
    check(sum(out)==1)
    return out

# An entropy combination sum w H(probabilities) with rational probabilities
# is certified by clearing denominators and comparing a rational product to 1.
def exact_entropy_sign(terms):
    from math import lcm
    exponents={}
    for weight,masses in terms:
        check(sum(masses)==1)
        for z in masses:
            check(z>=0)
            if z: exponents[z]=exponents.get(z,F(0))-weight*z
    scale=lcm(*(x.denominator for x in exponents.values()))
    ratio=F(1)
    for base,power in exponents.items():
        e=int(power*scale)
        ratio*=base**e
    return (ratio>1)-(ratio<1),scale,ratio

start=time.perf_counter()
p=q=F(1,4); table=[1,1,1,-1]
masses=centered_masses(table,[p,q])
check(masses==[F(49,64),F(3,64),F(3,64),F(9,64)])
residual=[masses[0]+masses[1],masses[2]+masses[3]]
children=[centered_masses([1,1],[q]),centered_masses([1,-1],[q])]
check(residual==[F(13,16),F(3,16)])
check(children==[[F(1),F(0)],[F(1,4),F(3,4)]])
check(all(residual[t]==(1-p)*children[0][t]+p*children[1][t] for t in range(2)))
sign,scale,ratio=exact_entropy_sign([(F(2),residual),(-F(1),masses),(-p,children[1])])
left=2**48*3**6*7**49; right=13**52
check(left>right); check(sign==1); check(ratio==F(left,right)**2); check(scale==64)
check(4*right<left<8*right)
save('MINIMAL_CERTIFICATE.json',{
    'status':'PASS','truth_table_order':'X+2Y for X,Y in {0,1}; X=0 means x=-1 in original sign-cube encoding',
    'truth_table':table,'biases':[p,q], 'exact_circuit':'f=1-2XY; X=(1+x)/2, Y=(1+y)/2',
    'squared_spectrum_order':['empty','X','Y','XY'],'squared_spectrum':masses,
    'residual_marginal':residual,'child_spectra':children,
    'debt_formula':'32*(J-M)=48+6 log2(3)+49 log2(7)-52 log2(13)',
    'integer_left':left,'integer_right':right,'integer_gap':left-right,
    'positive_ratio':F(left,right),'entropy_sign_clear_denominator':scale,
    'rigorous_debt_bounds_bits':['1/16','3/32'],
    'minimality':'n<=1 has J=0 because residual spectral set is deterministic'
})

# Shared bias 1/2 is the coarsest interior dyadic choice. Exhaust all 16 tables.
uniform=[]
for values in product([-1,1],repeat=4):
    mass=centered_masses(values,[F(1,2),F(1,2)])
    marginal=[mass[0]+mass[1],mass[2]+mass[3]]
    c0=centered_masses([values[0],values[2]],[F(1,2)])
    c1=centered_masses([values[1],values[3]],[F(1,2)])
    sig,_,_=exact_entropy_sign([(F(2),marginal),(-F(1),mass),(-F(1,2),c0),(-F(1,2),c1)])
    check(sig<=0)
    uniform.append({'table':values,'debt_sign':sig})
save('SHARED_DYADIC_BASELINE.json',uniform)

# Reconstruct finite pairs, endpoint projection bound, and small-dimensional classification.
paircounts=[]
for m in range(3):
    N=1<<m
    tables=list(product([-1,1],repeat=N))
    spectra=[]
    for t in tables:
        w=walsh(t); check(w==fwht(t)); check(sum(a*a for a in w)==N*N)
        spectra.append(w)
    endpoint_positive=balanced=0
    classifications={}
    for i,g in enumerate(tables):
        for j,h in enumerate(tables):
            G=spectra[i]; H=spectra[j]
            c=F(sum(a*b for a,b in zip(G,H)),N*N)
            Z=F(sum(b*b for a,b in zip(G,H) if a==0),N*N)
            kappa=2*Z+2*c-2
            check(kappa<=F(1,2)); check(c*c<=1-Z)
            check(c==F(sum(a*b for a,b in zip(g,h)),N))
            if kappa>0: endpoint_positive+=1
            equal=G==H; opposite=all(a==-b for a,b in zip(G,H))
            disjoint=all(a*b==0 for a,b in zip(G,H))
            if m<=1:
                check(equal or opposite or disjoint)
            if sum(g)==sum(h)==0:
                balanced+=1
                # Every balanced two-bit truth table is a signed character.
                check(sum(a!=0 for a in G)==sum(a!=0 for a in H)==1)
                check(equal or opposite or disjoint)
            key='equal' if equal else 'opposite' if opposite else 'disjoint' if disjoint else 'other'
            classifications[key]=classifications.get(key,0)+1
    paircounts.append({'residual_bits':m,'ordered_pairs':len(tables)**2,
                       'positive_endpoint':endpoint_positive,'balanced_pairs':balanced,
                       'classifications':classifications})
save('PAIR_MINIMALITY.json',paircounts)

# The unbalanced sharp fair-residual example on two bits.
G=walsh([1,1,1,1]); H=walsh([1,1,1,-1]); N=4
c=F(sum(a*b for a,b in zip(G,H)),N*N)
Z=F(sum(b*b for a,b in zip(G,H) if a==0),N*N)
check(c==F(1,2)); check(Z==F(3,4)); check(2*Z+2*c-2==F(1,2))
# Multiply both by a fresh fair character: balanced children on three residual bits.
g=[(-1 if x&1 else 1) for x in range(8)]
h=[g[x]*(1-2*int((x>>1&1) and (x>>2&1))) for x in range(8)]
GG=walsh(g); HH=walsh(h); check(sum(g)==sum(h)==0)
check(GG==fwht(g)); check(HH==fwht(h))
check(F(sum(a*b for a,b in zip(GG,HH)),64)==F(1,2))
check(F(sum(b*b for a,b in zip(GG,HH) if a==0),64)==F(3,4))
# Full 4-variable truth table with selector bit 0 and residual g,h on bits 1..3.
full=[h[x>>1] if x&1 else g[x>>1] for x in range(16)]
mass=centered_masses(full,[p,F(1,2),F(1,2),F(1,2)])
res=[mass[2*t]+mass[2*t+1] for t in range(8)]
child0=[F(a*a,64) for a in GG]; child1=[F(a*a,64) for a in HH]
sig,balanced_scale,balanced_ratio=exact_entropy_sign([(F(2),res),(-F(1),mass),(-(1-p),child0),(-p,child1)])
check(sig==1)
check(balanced_scale%32==0)
check(balanced_ratio==F(left,right)**(balanced_scale//32))
save('BALANCED_CERTIFICATE.json',{'status':'PASS','selector_bias':p,'fair_residual_bits':3,
 'children':[g,h],'truth_table':full,'squared_parent_spectrum':mass,
 'child_spectra':[child0,child1],'endpoint_coefficient':F(1,2),'finite_debt_sign':sig,
 'debt_formula':'32*(J-M)=48+6 log2(3)+49 log2(7)-52 log2(13)'})

# Same finite debt for fair-residual two-bit core selector (3 total physical variables).
unbal=[1 if not (x&1) else table[x>>1] for x in range(8)]
um=centered_masses(unbal,[p,F(1,2),F(1,2)])
ur=[um[2*t]+um[2*t+1] for t in range(4)]
sg,fair_scale,fair_ratio=exact_entropy_sign([(F(2),ur),(-F(1),um),(-p,[F(1,4)]*4)])
check(sg==1)
check(fair_scale%32==0)
check(fair_ratio==F(left,right)**(fair_scale//32))
left3=left; right3=right
check(left3>right3)
save('FAIR_RESIDUAL_CERTIFICATE.json',{'truth_table':unbal,'biases':[p,F(1,2),F(1,2)],
 'squared_spectrum':um,'debt_sign':sg,'integer_left':left3,'integer_right':right3,
 'balanced_lift_same_debt':True})
save('VALIDATION.json',{'status':'PASS','assertions':count,'runtime_seconds':time.perf_counter()-start,
 'search_spec_sha256':hashlib.sha256((RUN/'FROZEN_SPEC.json').read_bytes()).hexdigest(),
 'no_floating_point_entropy':True})
print(json.dumps({'status':'PASS','assertions':count,'seconds':time.perf_counter()-start}))
