"""Own capped-Poisson Palm enumeration and fixed-point/stability checks."""
from pathlib import Path
from math import factorial
from hashlib import sha256
import itertools
import json
from flint import arb,ctx
from t186_c007_zero_own import image,Q,P

ROOT=Path(__file__).resolve().parent
SOLVER=Path('~/brain_workers/w674/T186')
ctx.prec=512

def bounds_pair(pair,scale):
    return (arb(int(pair[0]))/scale).union(arb(int(pair[1]))/scale)

def inside(x,pair,scale):
    return x.lower() >= arb(int(pair[0]))/scale and x.upper() <= arb(int(pair[1]))/scale

def message(z,b,a,k,added):
    z+=added==0; b+=added>=2; a+=added==3
    if z==0 and b>=k: return 3
    if z==0 and b>=k-1: return 2
    if a>=k-1: return 1
    return 0

def jacobian(c,u,k):
    p,q,s=u; d=(-c*(1-s)).exp()
    return [[arb(0),d*c*P(k-1,c*q),c*d*Q(k,c*q)],
            [arb(0),d*c*P(k-2,c*q),c*d*Q(k-1,c*q)],
            [(1-d)*c*P(k-2,c*p),d*c*P(k-2,c*q),c*d*(Q(k-1,c*q)-Q(k-1,c*p))]]

def verify(path):
    data=json.loads(path.read_text(encoding='utf-8')); k=data['k']; c=arb(data['c']); scale=int(data['scale'])
    # c decimals are enclosing balls, retained through all calculations.
    box=data['fixed_point_box']; lo=[arb(int(v))/scale for v in box['lower']]; hi=[arb(int(v))/scale for v in box['upper']]
    assert all(x<=y for x,y in zip(lo,hi)) and lo[0]>0
    assert all(x>=y for x,y in zip(image(c,lo,k),lo))
    assert all(x<=y for x,y in zip(image(c,hi,k),hi))
    top=[arb(1)]*3
    for count in range(1,10001):
        top=[v.upper() for v in image(c,top,k)]
        if all(v<=w for v,w in zip(top,hi)): break
    else: raise ArithmeticError('Top enclosure did not enter '+path.name)
    # Monotone brackets are invariant; refine before comparing submitted cells.
    for _ in range(2000):
        lo=[v.lower() for v in image(c,lo,k)]; hi=[v.upper() for v in image(c,hi,k)]
        if all(b-a<arb('1e-90') for a,b in zip(lo,hi)): break
    u=[a.union(b) for a,b in zip(lo,hi)]; p,q,s=u
    pi=[1-s,s-q,q-p,p]; assert all(x>0 for x in pi)
    states=[tuple(v) for v in data['states']]
    assert set(states)=={(a,b) for a in range(4) for b in range(4) if a+b<=3}
    index={v:i for i,v in enumerate(states)}
    matrix=[[arb(0) for _ in states] for _ in states]
    zero=(-c*pi[0]).exp(); probs0=[zero,1-zero]
    def capped(rate):
        return [P(i,rate) for i in range(k)]+[Q(k,rate)]
    probs2=capped(c*pi[2]); probs3=capped(c*pi[3])
    for z,i,j in itertools.product(range(2),range(k+1),range(k+1)):
        weight=probs0[z]*probs2[i]*probs3[j]
        outputs=[message(z,i+j,j,k,add) for add in range(4)]
        for alpha,beta in states:
            row=index[alpha,beta]
            for delta in range(4):
                eta=outputs[beta]
                if outputs[delta]==alpha and (delta,eta) in index:
                    matrix[row][index[delta,eta]] += weight*c*pi[delta]/pi[alpha]
    for i,row in enumerate(matrix):
        for j,x in enumerate(row): assert inside(x,data['matrix'][i][j],scale),(path.name,i,j)
    w=[arb(int(v))/scale for v in data['perron_weight']]; assert all(x>0 for x in w)
    ratios=[sum((v*w[j] for j,v in enumerate(row)),arb(0))/w[i] for i,row in enumerate(matrix)]
    lower=arb(int(data['rho_scaled'][0]))/scale; upper=arb(int(data['rho_scaled'][1]))/scale
    assert all(x>=lower and x<=upper for x in ratios)
    J=jacobian(c,u,k)
    for i,row in enumerate(J):
        for j,x in enumerate(row): assert inside(x,data['jacobian'][i][j],scale),(path.name,'J',i,j)
    v=[arb(int(x))/scale for x in data['stability_weight']]; assert all(x>0 for x in v)
    norms=[sum((abs(x)*v[j] for j,x in enumerate(row)),arb(0))/v[i] for i,row in enumerate(J)]
    bound=arb(int(data['jacobian_weighted_norm_upper_scaled']))/scale
    assert bound<1 and all(x<=bound for x in norms)
    return {'file':path.name,'sha256':sha256(path.read_bytes()).hexdigest(),'k':k,'c':data['c'],'top_rounds':count,'matrix_entries':100,'jacobian_entries':9,'rho_scaled':data['rho_scaled'],'verdict':'PASS'}

def main():
    selected=[r for r in json.loads((SOLVER/'logs/t3_python_kernel_replay.json').read_text(encoding='utf-8'))['results'] if 'file' in r]
    results=[]
    for row in selected:
        path=SOLVER/row['file'].replace('\\','/')
        results.append(verify(path))
        (ROOT/'t186_c007_matrices_own.json').write_text(json.dumps({'precision':512,'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'results':results},indent=2)+'\n',encoding='utf-8')
        print(json.dumps(results[-1]),flush=True)
    assert len(results)==9
    positive=[]
    for k in (3,4):
        path=SOLVER/f'logs/t3_positive_JS_k{k}.json'; data=json.loads(path.read_text(encoding='utf-8')); scale=int(data['scale'])
        point=[arb(int(x))/scale for x in data['point_scaled']]
        assert 0<point[0]<=point[1]<=point[2]<=1
        assert all(a>=b for a,b in zip(image(arb(data['c']),point,k),point))
        positive.append({'k':k,'c':data['c'],'sha256':sha256(path.read_bytes()).hexdigest(),'verdict':'PASS'})
    (ROOT/'t186_c007_positive_own.json').write_text(json.dumps({'precision':512,'results':positive},indent=2)+'\n',encoding='utf-8')
if __name__=='__main__': main()
