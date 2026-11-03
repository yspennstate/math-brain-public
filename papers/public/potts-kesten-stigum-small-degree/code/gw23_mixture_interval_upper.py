"""Exact weighted offspring2/3 upgrade, separate from every frozen producer."""
import argparse,datetime,hashlib,json,pathlib,time
from fractions import Fraction as F
from universal_fusion import unit_table,edge_table,signal,apply_edge,apply_table,exact_depth_one
from fourth_polynomial_certificate import memory_check
r=pathlib.Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def mix(left,right,theta,scale,vertex):
    assert sum(left)==sum(right)==scale and 0<=theta<=1
    n,d=theta.numerator,theta.denominator
    out=[((d-n)*a+n*b)//d for a,b in zip(left,right)]
    loss=scale-sum(out);assert loss>=0;out[vertex]+=loss
    return out,loss
def step(table,edge,masses,theta,scale,vertex):
    child,l0=apply_edge(edge,masses,scale,vertex)
    pair,l1=apply_table(table,child,child,scale,False)
    triple,l2=apply_table(table,pair,child,scale,False)
    out,l3=mix(pair,triple,theta,scale,vertex)
    return out,[l0,l1,l2,l3]
def validate():
    from universal_fusion import reference_pair
    N=6;table=unit_table(N);keys=table[0];vertex=keys.index((0,0,N));scale=1<<16
    refs={(i,j):reference_pair(N,keys,i,j)[0] for i in range(len(keys)) for j in range(len(keys))}
    def rounded(values):
        out=[v.numerator*scale//v.denominator for v in values]
        out[vertex]+=scale-sum(out);return [F(v,scale) for v in out]
    def fuse(left,right):
        out=[F(0)]*len(keys)
        for i,x in enumerate(left):
            for j,y in enumerate(right):
                for k,w in refs[i,j].items():out[k]+=x*y*w
        return rounded(out)
    rows=[]
    for theta in [F(0),F(1,2),F(51,100),F(1)]:
        for eta in [F(0),F(253,400),F(1)]:
            edge=edge_table(N,eta,keys);masses=[0]*len(keys);masses[vertex]=scale
            law=[F(v,scale) for v in masses]
            for depth in range(1,5):
                child=[F(0)]*len(keys)
                for i,x in enumerate(law):
                    for k,n in edge[1][i].items():child[k]+=x*F(n,edge[0])
                child=rounded(child);pair=fuse(child,child);triple=fuse(pair,child)
                law=rounded([(1-theta)*x+theta*y for x,y in zip(pair,triple)])
                masses,losses=step(table,edge,masses,theta,scale,vertex)
                assert law==[F(v,scale) for v in masses]
                x=signal(keys,masses,N,scale)
                if depth==1:assert x>=(1-theta)*exact_depth_one(2,eta)+theta*exact_depth_one(3,eta)
                if eta==0:assert x==0
                if eta==1:assert x==F(2,3)
                rows.append({'theta':str(theta),'eta':str(eta),'depth':depth,'x':str(x)})
    packet={'status':'PASS separate Fraction-path weighted mixture validation; author check, not independent audit','checks':rows,'source_sha256':sha(pathlib.Path(__file__))}
    (r/'gw23_mixture_interval_small_validation.json').write_text(json.dumps(packet,indent=2),encoding='utf-8');print(json.dumps(packet),flush=True)
def main():
    p=argparse.ArgumentParser();p.add_argument('--validate-small',action='store_true');p.add_argument('--seconds',type=int,default=90);p.add_argument('--maximum-depth',type=int,default=180);p.add_argument('--theta-lower',default='1/2');p.add_argument('--theta-upper',default='51/100');p.add_argument('--eta',default='253/400');p.add_argument('--bits',type=int,default=32);a=p.parse_args()
    if a.validate_small:validate();return
    assert 0<a.seconds<=180 and 1<=a.bits<=48
    lo,hi,eta=map(F,[a.theta_lower,a.theta_upper,a.eta]);assert F(1,2)<=lo<=hi<=1 and 0<eta<1 and (2+lo)*eta**2>=1
    valid=json.loads((r/'gw23_mixture_interval_small_validation.json').read_text(encoding='utf-8'));assert valid['status'].startswith('PASS') and valid['source_sha256']==sha(pathlib.Path(__file__))
    memory_check();N=96;stem=r/'universal_unit_N96_1'
    parts=[pathlib.Path(str(stem)+'_'+name+'.bin') for name in ['dest_indices','numerators','offsets','pair_i','pair_j']]
    assert stem.with_suffix('.json').is_file() and all(q.is_file() for q in parts)
    assert sum(q.stat().st_size for q in parts)==106408056,'No cache rebuilding permitted.'
    label=lambda q:str(q.numerator)+'-'+str(q.denominator)
    path=r/('gw23_interval_'+label(lo)+'_'+label(hi)+'_eta'+label(eta)+'_bits'+str(a.bits)+'.json')
    names=['gw23_mixture_interval_upper.py','gw23_mixture_interval_small_validation.json','universal_fusion.py','ternary_bp_int.py','quantized_bp.py','fourth_polynomial_certificate.py']
    binding={name:sha(r/name) for name in names}
    table=unit_table(N);keys=table[0];assert len(keys)==817
    scale=1<<a.bits;vertex=keys.index((0,0,N));edge=edge_table(N,eta,keys)
    masses=[0]*len(keys);masses[vertex]=scale;depth=0;rows=[]
    if path.exists():
        old=json.loads(path.read_text(encoding='utf-8'));assert old['source_sha256']==binding and old['theta_interval']==[str(lo),str(hi)] and old['eta']==str(eta)
        masses=list(map(int,old['integer_masses']));depth=old['completed_depth'];rows=old['rows'];assert sum(masses)==scale
        if old['strict_entry']:print('Already entered; no replay.',flush=True);return
    start=time.monotonic()
    while depth<a.maximum_depth:
        masses,losses=step(table,edge,masses,hi,scale,vertex);depth+=1;x=signal(keys,masses,N,scale)
        if depth==1:assert x>=(1-hi)*exact_depth_one(2,eta)+hi*exact_depth_one(3,eta)
        row={'depth':depth,'x':str(x),'rounding_loss_masses':losses};rows.append(row)
        packet={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'exact author upper-experiment candidate; no independent audit or admitted family theorem','theta_interval':[str(lo),str(hi)],'theta_comparison':str(hi),'eta':str(eta),'grid':N,'bits':a.bits,'completed_depth':depth,'x':str(x),'local_target':'1/50','strict_entry':x<F(1,50),'orbit_keys':keys,'integer_masses':[str(v) for v in masses],'rows':rows,'source_sha256':binding,'comparison':'Observed offspring at upper endpoint; channel at rational upper bound to lower-endpoint critical eigenvalue; fresh conditionally independent child copies each update.'}
        tmp=path.with_suffix('.json.part');tmp.write_text(json.dumps(packet,separators=(',',':')),encoding='utf-8');tmp.replace(path)
        print(json.dumps(row),flush=True)
        if packet['strict_entry'] or time.monotonic()-start>=a.seconds:break
if __name__=='__main__':main()
