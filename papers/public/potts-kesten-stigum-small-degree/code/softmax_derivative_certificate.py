"""Exact, resumable Bernstein certificates; no floating arithmetic is used.

This is a candidate verifier, not a theorem until its full cover passes.
The independently rebuilt operator/cumulant identities are checked before use.
"""
import os
os.environ['OMP_NUM_THREADS'] = '1'
import argparse, hashlib, itertools, json, math, time
from datetime import datetime, timezone
from pathlib import Path
import sympy as s

HERE = Path(__file__).resolve().parent
OUT = HERE / 'softmax_derivative_v1'
SOURCE = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
u, v, t = s.symbols('u v t')
VAR = (u, v, t)

def digest(c):
    return hashlib.sha256(','.join(map(str,c)).encode()).hexdigest()

def polynomials():
    p = s.symbols('p0:3')
    h = s.symbols('h0:3')
    mean = sum(p[i]*h[i] for i in range(3))
    op = p[0]
    derivatives = {}
    for n in range(1,5):
        op = s.expand(sum(s.diff(op,p[i])*p[i]*(h[i]-mean) for i in range(3)))
        derivatives[n] = op
    pp = (u,(1-u)*v,(1-u)*(1-v))
    N = s.Rational(2,3)*(1-t+t*t)
    result = []
    for case, hh in [('endpoint',(0,t,1)), ('middle',(t,0,1))]:
        sub = dict(zip(p,pp)) | dict(zip(h,hh))
        ds = {n:s.expand(derivatives[n].subs(sub, simultaneous=True)) for n in (2,3,4)}
        m = sum(pp[i]*hh[i] for i in range(3))
        r = hh[0]-m
        k2 = sum(pp[i]*(hh[i]-m)**2 for i in range(3))
        k3 = sum(pp[i]*(hh[i]-m)**3 for i in range(3))
        k4 = sum(pp[i]*(hh[i]-m)**4 for i in range(3))-3*k2*k2
        rebuilt = {2:pp[0]*(r*r-k2),
                   3:pp[0]*(r**3-3*r*k2-k3),
                   4:pp[0]*(r**4-6*r*r*k2-4*r*k3+3*k2*k2-k4)}
        for n in (2,3,4):
            assert s.Poly(ds[n]-rebuilt[n],*VAR).is_zero, (case,n)
        for n,K,power in [(2,s.Rational(1,5),1),(4,s.Rational(3,5),2)]:
            for sign in (-1,1):
                result.append((f'{case}_D{n}_{sign:+d}',s.Poly(K*N**power+sign*ds[n],*VAR)))
        result.append((f'{case}_D3_squared',s.Poly(s.Rational(4,25)*N**3-ds[3]**2,*VAR)))
    # Exact negative controls: the verifier must reject constants below the truth.
    controls = []
    for n,point,expected,K,power in [
        (2,{u:s.Rational(1,4),v:0,t:s.Rational(1,2)},s.Rational(3,32),s.Rational(1,10),1),
        (4,{u:s.Rational(1,4),v:0,t:s.Rational(1,2)},s.Rational(15,128),s.Rational(2,5),2),
        (3,{u:s.Rational(1,2),v:0,t:s.Rational(1,2)},s.Rational(1,8),s.Rational(1,5),s.Rational(3,2))]:
        actual = abs(derivatives[n].subs(dict(zip(p,pp))|dict(zip(h,(0,t,1))),simultaneous=True).subs(point))
        assert actual == expected
        if n == 3:
            assert actual**2 > K*K*N.subs(point)**3
        else:
            assert actual > K*N.subs(point)**power
        controls.append({'order':n,'actual':str(actual),'rejected_constant':str(K)})
    return result, controls

def lines(shape,axis):
    strides = (shape[1]*shape[2],shape[2],1)
    other = [k for k in range(3) if k != axis]
    for ij in itertools.product(*(range(shape[k]) for k in other)):
        base = sum(i*strides[k] for i,k in zip(ij,other))
        yield [base+j*strides[axis] for j in range(shape[axis])]

def bernstein(poly):
    deg = tuple(poly.degree(z) for z in VAR)
    shape = tuple(n+1 for n in deg)
    den = math.lcm(*(int(q.q) for _,q in poly.terms()))
    c = [0]*math.prod(shape)
    for e,q in poly.terms():
        c[(e[0]*shape[1]+e[1])*shape[2]+e[2]] = int(q*den)
    for axis,n in enumerate(deg):
        scale = math.lcm(*(math.comb(n,j) for j in range(n+1)))
        out = c.copy()
        for idx in lines(shape,axis):
            for k in range(n+1):
                out[idx[k]] = sum(c[idx[j]]*math.comb(k,j)*(scale//math.comb(n,j)) for j in range(k+1))
        den *= scale
        c = out
    return shape,c,den

def split(c,shape,axis):
    n = shape[axis]-1
    left, right = c.copy(),c.copy()
    for idx in lines(shape,axis):
        tri = [c[j] for j in idx]
        for depth in range(n+1):
            left[idx[depth]] = tri[0] << (n-depth)
            right[idx[n-depth]] = tri[-1] << (n-depth)
            tri = [tri[k]+tri[k+1] for k in range(len(tri)-1)]
    return left,right

def atomic(path,obj):
    tmp = path.with_suffix(path.suffix+'.part')
    tmp.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    tmp.replace(path)

def cover(leaves):
    paths = sorted(q['path'] for q in leaves)
    assert len(paths)==len(set(paths))
    assert all(not b.startswith(a) for a,b in zip(paths,paths[1:]))
    depth = max(map(len,paths),default=0)
    assert sum(1 << (depth-len(p)) for p in paths)==1 << depth

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--seconds',type=float,default=100)
    ap.add_argument('--max-depth',type=int,default=27)
    args=ap.parse_args(); start=time.monotonic(); deadline=start+args.seconds
    OUT.mkdir(exist_ok=True)
    checkpoint=OUT/'checkpoint.json'; final=OUT/'report.json'
    if final.exists():
        r=json.loads(final.read_text(encoding='utf-8')); assert r['source_sha256']==SOURCE
        print(json.dumps(r)); return
    if checkpoint.exists():
        state=json.loads(checkpoint.read_text(encoding='utf-8')); assert state['source_sha256']==SOURCE
    else:
        polys,controls=polynomials()
        jobs=[]
        for name,poly in polys:
            shape,c,den=bernstein(poly)
            jobs.append({'name':name,'shape':shape,'root_denominator':den,'root_sha256':digest(c),
                         'root_power_terms':[[list(e),str(q)] for e,q in poly.terms()],
                         'stack':[{'path':'','coefficients':c}], 'leaves':[], 'visited':0})
        state={'source_sha256':SOURCE,'created_at':datetime.now(timezone.utc).isoformat(),
               'scope':'Exact rational polynomial cover; not a full Lindeberg proof',
               'constants':{'K2':'1/5','K3':'2/5','K4':'3/5'},'negative_controls':controls,'jobs':jobs}
        atomic(checkpoint,state)
    last=time.monotonic()
    for job in state['jobs']:
        while job['stack']:
            if time.monotonic()>deadline:
                atomic(checkpoint,state)
                print(json.dumps({'status':'CHECKPOINT','completed':sum(not j['stack'] for j in state['jobs']),
                                  'visited':sum(j['visited'] for j in state['jobs']),
                                  'seconds':time.monotonic()-start})); return
            node=job['stack'].pop(); path,c=node['path'],node['coefficients']; job['visited']+=1
            lo,hi=min(c),max(c)
            if lo>=0:
                job['leaves'].append({'path':path,'minimum':lo,'maximum':hi,'sha256':digest(c)})
            elif hi<0:
                state['status']='REFUTED_BY_ALL_NEGATIVE_BOX'; state['failure']={'job':job['name'],'path':path}
                atomic(OUT/'failure.json',state); raise AssertionError(state['failure'])
            elif len(path)>=args.max_depth:
                job['stack'].append(node); atomic(checkpoint,state)
                print(json.dumps({'status':'UNRESOLVED_DEPTH','job':job['name'],'path':path})); return
            else:
                left,right=split(c,job['shape'],len(path)%3)
                job['stack'].extend([{'path':path+'1','coefficients':right},{'path':path+'0','coefficients':left}])
            if time.monotonic()-last>10:
                atomic(checkpoint,state);last=time.monotonic()
        cover(job['leaves'])
    state['status']='EXACT BERNSTEIN COVER PASS'
    state['completed_at']=datetime.now(timezone.utc).isoformat()
    atomic(final,state)
    print(json.dumps({'status':state['status'],'jobs':len(state['jobs']),
                      'leaves':sum(len(j['leaves']) for j in state['jobs']),
                      'visited':sum(j['visited'] for j in state['jobs']),
                      'seconds':time.monotonic()-start}))

if __name__=='__main__':main()
