"""Full independent endpoint and exact quadratic audit, using only saved bound inputs."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from time import monotonic
import json
from t067_piecewise_gaussian_own import GaussianQuadrature

HERE=Path(__file__).resolve().parent
SOLVER=Path('~/brain_workers/w682')
RAW=SOLVER/'checks/piecewise_raw_endpoint_verification.json'
CERT=SOLVER/'checks/piecewise_cutoff_independent.json'
MANIFEST=SOLVER/'checks/piecewise156_submission.json'
PROOF=SOLVER/'proofs/T067-PIECEWISE-D0-001_v1.md'
SUBJECT='9a8a26b8c0631b4549f29bdc7ee231130a080a680408394bb75e0a8c16986226'

def constants(L):
    B4=F(25,288)+F(49,100)*L/(1-L)
    B3=F(1,6)+F(49,20)*L*B4
    B1=F(5,24)+F(49,20)*L*B3
    CU=F(1,48)+F(49,160)*L*B4+F(1,10)*(F(1,24)+B3*(1/(1-L)+1+L/2)+F(1,6))+B1/(4*(1-L)**2)+F(1,15)+1/(40*(1-L)**4)
    CM=F(1,60)+F(5,48)+L*L/36+(2+4*L*L+L**4)/40
    return CU,CM

def height(x,a,b,U,CU,CM):
    chord=((b-x)*U[a]+(x-a)*U[b])/(b-a)
    return x-chord-16*(x-a)*(b-x)-F(81,156)*(CU*min(5*x*x,2*x/3)+CM*x*x)

def min_quadratic(a,b,U,CU,CM):
    f0=height(a,a,b,U,CU,CM); f1=height(b,a,b,U,CU,CM)
    fm=height((a+b)/2,a,b,U,CU,CM)
    A=2*(f1+f0-2*fm); B=f1-f0-A
    candidates=[(f0,a),(f1,b)]
    if A>0:
        t=-B/(2*A)
        if 0<t<1: candidates.append((f0-B*B/(4*A),a+(b-a)*t))
    return min(candidates)

def check_exact(points,U,cert):
    assert set(U)==set(points), 'incomplete endpoint map'
    L=F(16013,200000); CU,CM=constants(L)
    assert 156*16013**2-200000**2==922364 and L<=F(1,10)
    assert str(CU)==cert['CU'] and str(CM)==cert['CM'] and F(cert['L'])==L
    assert 156*L*L-1==F(cert['lambda_square_margin'])>0
    assert F(27,10)+F(135,8)+F(243,20)==F(1269,40)<32
    parents=list(zip(points,points[1:])); parent_set=set(parents)
    minima=[]
    for a,b in parents:
        assert not a<F(2,15)<b
        value,where=min_quadratic(a,b,U,CU,CM)
        assert value>0, ('nonpositive C1',str(a),str(b),str(value))
        minima.append((value,where,a,b))
    leaves_by_parent={p:[] for p in parents}; smallest=None
    for leaf in cert['leaves']:
        parent=F(leaf['parent_a']),F(leaf['parent_b']); assert parent in parent_set
        a,b=parent; l,r=F(leaf['a']),F(leaf['b']); assert a<=l<r<=b
        f0=height(l,a,b,U,CU,CM); f1=height(r,a,b,U,CU,CM)
        fm=height((l+r)/2,a,b,U,CU,CM)
        bern=[f0,2*fm-(f0+f1)/2,f1]
        assert bern==list(map(F,leaf['bernstein']))
        assert min(bern)>F(3,10**7)
        smallest=min(bern) if smallest is None else min(smallest,*bern)
        leaves_by_parent[parent].append((l,r))
    assert len(cert['leaves'])==87 and len(parents)==85
    for (a,b),leaves in leaves_by_parent.items():
        cursor=a
        for l,r in sorted(leaves): assert l==cursor; cursor=r
        assert cursor==b
    assert smallest==F(cert['minimum_bernstein_coefficient'])
    return {'CU':str(CU),'CM':str(CM),'exact_minimum':list(map(str,min(minima))),'minimum_bernstein':str(smallest),'parents':85,'leaves':87,'strict_coefficient_floor':'3/10000000','verdict':'PASS'}

def main():
    assert sha256(PROOF.read_bytes()).hexdigest()==SUBJECT
    manifest=json.loads(MANIFEST.read_text(encoding='utf-8')); assert manifest['proof_sha256']==SUBJECT
    bytes_hashed=0
    for item in manifest['files']:
        rel=Path(item['path']); assert not rel.is_absolute() and '..' not in rel.parts
        assert rel.parts[0] in ('checks','proofs','papers')
        assert not any(p.lower() in ('bench','benches','heldout','held_out','test_bank') for p in rel.parts)
        path=SOLVER/rel; assert path.stat().st_size==item['bytes']<5_000_000
        data=path.read_bytes(); bytes_hashed+=len(data)
        assert sha256(data).hexdigest()==item['sha256'], str(rel)
    raw=json.loads(RAW.read_text(encoding='utf-8')); cert=json.loads(CERT.read_text(encoding='utf-8'))
    assert sha256(RAW.read_bytes()).hexdigest()==cert['input_sha256']
    points=[F(10,100-i) for i in range(86)]
    U={F(k):F(v) for k,v in raw['endpoint_g_upper'].items()}
    assert set(U)==set(points) and points[0]==F(1,10) and points[-1]==F(2,3)
    receipt_path=HERE/'t067_piecewise_endpoints_own.json'
    helper=HERE/'t067_piecewise_gaussian_own.py'; helper_hash=sha256(helper.read_bytes()).hexdigest()
    if receipt_path.exists():
        receipt=json.loads(receipt_path.read_text(encoding='utf-8'))
        assert receipt['helper_sha256']==helper_hash and receipt['proof_sha256']==SUBJECT
        assert receipt['raw_sha256']==sha256(RAW.read_bytes()).hexdigest()
    else:
        receipt={'proof_sha256':SUBJECT,'helper_sha256':helper_hash,'raw_sha256':sha256(RAW.read_bytes()).hexdigest(),'precision_bits':192,'bin_width':'1/16','checked':[]}
    start=monotonic(); engine=GaussianQuadrature()
    for index in range(len(receipt['checked']),len(points)):
        point=points[index]
        pilot=HERE/('t067_piecewise_endpoint_'+str(point).replace('/','_')+'_own.json')
        if pilot.exists():
            value=json.loads(pilot.read_text(encoding='utf-8'))
            assert value['script_sha256']==helper_hash and value['signal']==str(point)
        else: value=engine.evaluate(point)
        own_upper=F(value['g_upper']); assert own_upper<=U[point], ('endpoint',index,str(point))
        value.update(index=index,author_upper=str(U[point]),upper_slack=str(U[point]-own_upper))
        receipt['checked'].append(value); receipt['complete']=len(receipt['checked'])==86
        receipt_path.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
        if monotonic()-start>90: break
    if not receipt['complete']:
        print(json.dumps({'checked':len(receipt['checked']),'total':86,'status':'checkpoint'})); return
    exact=check_exact(points,U,cert)
    for mode in ('missing endpoint','raised endpoint'):
        corrupt=dict(U)
        if mode=='missing endpoint': del corrupt[points[25]]
        else: corrupt[points[25]]+=1
        try: check_exact(points,corrupt,cert)
        except AssertionError: pass
        else: raise AssertionError('corruption accepted '+mode)
    result={'proof_sha256':SUBJECT,'manifest_sha256':sha256(MANIFEST.read_bytes()).hexdigest(),'files_hashed':len(manifest['files']),'bytes_hashed':bytes_hashed,'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'helper_sha256':helper_hash,'endpoint_count':86,'precision_bits':192,'full_signed_quadrature':True,'exact_checks':exact,'missing_and_raised_controls':'rejected','seconds_this_batch':monotonic()-start,'verdict':'PASS for all endpoint and exact algebra checks; analytic/documentation audit separate'}
    (HERE/'t067_piecewise_full_own.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('exact_checks',)}))
    print('exact_minimum_display',float(F(exact['exact_minimum'][0])))

if __name__=='__main__': main()
