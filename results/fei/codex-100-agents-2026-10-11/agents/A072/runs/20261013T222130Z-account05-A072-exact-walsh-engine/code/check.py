import importlib.util,itertools,json,math,sys,time
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parent/'20261012T004036Z-account05-A072-exact-walsh-engine/EXACT_WALSH_INTERFACE.py'
sp=importlib.util.spec_from_file_location('a072_v2',OLD);e=importlib.util.module_from_spec(sp);sp.loader.exec_module(e)
BASE=e.baseline
SEED_POINTS=(0,1,2,4,8,16,32,6,17,40)
H=tuple(-1 if x in SEED_POINTS else 1 for x in range(64))
NAT=1<<128;SCALE=1<<96;TERMS=48
def dump(name,r):
    (ROOT/name).write_text(json.dumps(r,indent=2,default=str)+'\n',encoding='utf-8')
def truth(mask):return tuple(1-2*((mask>>x)&1) for x in range(64))
def unit(a,b):
    assert b<=a<=2*b
    u,v=a-b,a+b
    lo=sum(2*NAT*u**(2*j+1)//((2*j+1)*v**(2*j+1)) for j in range(TERMS))
    rn=2*NAT*u**97*v*v;rd=97*v**97*(v*v-u*u)
    return lo,lo+TERMS+(rn+rd-1)//rd
LN2=unit(2,1)
@lru_cache(None)
def logint(n):
    k=n.bit_length()-1
    if n==1<<k:return k*SCALE,k*SCALE
    a,b=unit(n,1<<k)
    # Range exponent stays exact outside division; this avoids correlated
    # ln2 terms in A071's original enclosure but is equally rigorous.
    return k*SCALE+a*SCALE//LN2[1],k*SCALE+(b*SCALE+LN2[0]-1)//LN2[0]
def phi(x,y):
    if not x or not y:return Q(0),Q(0)
    D=math.lcm(x.denominator,y.denominator);a=int(x*D);b=int(y*D)
    al,ah=logint(a);bl,bh=logint(b);sl,sh=logint(a+b)
    return Q((a+b)*sl-a*ah-b*bh,D*SCALE),Q((a+b)*sh-a*al-b*bl,D*SCALE)
def subtract(a,b):return a[0]-b[1],a[1]-b[0]
def classify(a):
    if a==(0,0):return 0
    if a[0]>0:return 1
    if a[1]<0:return -1
    raise ArithmeticError('Unresolved frozen-precision sign')

@lru_cache(None)
def sections(M):
    p=Q(M,64);v=p*(1-p);m=1-2*p
    packets=[];q=Q(0)
    # Direct signed sections h0,h1 on the other five physical outer inputs.
    for T in range(32):
        A=B=Q(0)
        for z in range(32):
            h0,h1=H[z<<1],H[(z<<1)|1]
            c0=Q(h0+h1,2);c1=Q(h0-h1,2)
            weight=p**z.bit_count()*(1-p)**(5-z.bit_count())
            basis=math.prod(Q((z>>j)&1)-p for j in range(5) if T>>j&1)
            A+=weight*basis*(c0+m*c1);B+=weight*basis*c1
        norm=v**T.bit_count();U=A*A/norm;D=B*B/norm
        packets.append((U,D));q+=D
    assert q==2*p*(1-p)**3*(2-p)
    # An independent checked uniform-Walsh-to-biased polynomial conversion
    # certifies Parseval, signs, inverse and physical pivotal probabilities.
    bc=BASE.biased_certificate(H,(p,)*6);sq=bc['spectrum'];vs=4*v
    for T,(U,D) in enumerate(packets):
        assert U==sq[T<<1] and D==sq[(T<<1)|1]/vs
    assert bc['pivotal_probabilities']==[q]*6
    alpha=(1-p)**4*(1+4*p-2*p*p)
    assert sq[0]==(1-2*alpha)**2
    terminal_terms=[{'coefficient':-s,'log2_argument':s} for s in sq if s]
    terminal_terms.extend({'coefficient':6*q*s,'log2_argument':s} for s in (m*m,vs) if s)
    dump('out/outer_bias_'+str(M)+'.json',{'M':M,'p':p,'mean_core':m,'variance_core':vs,'q':q,
        'spectral_masses':sq,'section_packets_U_D':packets,
        'terminal_correction_log_terms':terminal_terms,
        'terminal_identity':'H(F)=6*q*H(g)+terminal_correction; I(F)=6*q*I(g)'})
    return tuple(packets),q

def reserve(M,d):
    p=Q(M,64);m=1-2*p;t=Q(d,32)**2
    packets,q=sections(M);A=B=Q(0)
    for U,D in packets:
        a,b=phi(U,t*D);A+=a;B+=b
    cost=phi(m*m,t)
    return subtract((A,B),(q*cost[0],q*cost[1])),q

def sparse_cases():
    yield {'kind':'singleton'},1
    for d in range(1,7):yield {'kind':'pair','distance':d},1|(1<<((1<<d)-1))
    for a in range(7):
        for b in range(a,7):
            for c in range(b,7):
                if a+b==0 or a+b+c>6:continue
                u=((1<<a)-1)|(((1<<c)-1)<<(a+b))
                v=(((1<<b)-1)<<a)|(((1<<c)-1)<<(a+b))
                yield {'kind':'triple','column_counts':[a,b,c]},1|(1<<u)|(1<<v)

def run(pilot):
    start=time.perf_counter();domain=[1,4,16,32] if pilot else range(1,64)
    signs={};counts={-1:0,0:0,1:0};maxwidth=Q(0)
    file='out/pilot_signatures.jsonl' if pilot else 'out/signatures.jsonl'
    with (ROOT/file).open('w',encoding='utf-8') as f:
        for M in domain:
            for d in range(M%2,min(M,64-M)+1,2):
                a,b=(M+d)//2,(M-d)//2
                mask=sum(1<<(2*x) for x in range(a))+sum(1<<(2*x+1) for x in range(b))
                uc=BASE.uniform_certificate(truth(mask))
                assert uc['walsh'][0]==64-2*M and uc['walsh'][1]==-2*d
                R,q=reserve(M,d);s=classify(R);signs[M,d]=s;counts[s]+=1;maxwidth=max(maxwidth,R[1]-R[0])
                f.write(json.dumps({'M':M,'d':d,'actual_mask':str(mask),'q':str(q),'reserve_bounds':[str(x) for x in R],'sign':s})+'\n');f.flush()
                if time.perf_counter()-start>(55 if pilot else 120):raise RuntimeError('Frozen runtime cap')
    expected=30 if pilot else 559;assert len(signs)==expected
    if pilot:
        result={'pilot_signatures':len(signs),'counts':counts,'runtime_seconds':time.perf_counter()-start}
        dump('out/pilot.json',result);print(json.dumps(result));return
    # Compare to A071 only after independent computations are complete.
    prior=ROOT.parents[2]/'A071/runs/20261013T215901Z-account05-A071-search-space-design/out/signatures.jsonl'
    a071={(r['M'],r['d']):{'negative':-1,'zero':0,'positive':1}[r['reserve_sign']]
          for r in map(json.loads,prior.read_text().splitlines())}
    assert signs==a071
    choices=[]
    for M in range(4,33):
        ds=list(range(M%2,M+1,2))
        opts=[s for s in (1,-1) if all(signs[M if s==1 else 64-M,d]>=0 for d in ds)]
        assert opts
        choices.append({'minority_count':M,'admissible_output_signs':opts,'selected_sign':opts[0]})
    dump('out/orientation_policy.json',choices)
    sparse=[]
    for geometry,mask in sparse_cases():
        cert=e.uniform_entropy_certificate(truth(mask));rows=cert['coordinates']
        candidates=[r for r in rows if r['influence']]
        # A single exact coordinate below 14/5 suffices; do not search/minimize
        # the full orbit unnecessarily or use display numbers for decisions.
        chosen=None
        for r in candidates:
            form=e.add((Q(14,5),{2:Q(1)}),(-1,r['B_over_influence_prime_log']))
            product=e.sign(form)
            if product['sign']>0:chosen={'coordinate':r['coordinate'],'prime_log':r['B_over_influence_prime_log'],'strict_14_over_5_certificate':product};break
        assert chosen is not None
        item={'geometry':geometry,'mask':str(mask),'selected_coordinate':chosen,'certificate':cert}
        sparse.append(item)
        dump('out/sparse_'+str(len(sparse))+'.json',item)
    assert len(sparse)==23
    K6={2:Q(16,3),3:Q(-21,8),5:Q(95,24),11:Q(-121,24),13:Q(65,24)}
    guard=e.sign(e.add((1,K6),(Q(-14,5),{2:Q(1)})));assert guard['sign']>0
    dump('out/guard_gap.json',guard)
    result={'signatures':559,'biases':63,'reserve_sign_counts':counts,'independent_A071_matches':559,
            'orientation_policy_rows':29,'sparse_isometry_representatives':23,'sparse_cutoff':'14/5',
            'K6_strictly_above_sparse_cutoff':True,'max_interval_width':str(maxwidth),
            'all_signs_resolved':True,'failures':0,'runtime_seconds':time.perf_counter()-start}
    assert result['runtime_seconds']<120
    dump('ENGINE_CERTIFICATE.json',result);print(json.dumps(result))

if __name__=='__main__':run('--pilot' in sys.argv)
