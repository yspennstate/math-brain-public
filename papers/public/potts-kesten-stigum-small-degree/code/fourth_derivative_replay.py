"""Rebuild Q derivatives from normalized exponential series; replay exact boxes.

Does not import the producing checker or its Bernstein engine.
"""
import os
os.environ['OMP_NUM_THREADS']='1'
import hashlib,itertools,json,math,time
from pathlib import Path
from fractions import Fraction as F
import sympy as s
HERE=Path(__file__).resolve().parent

def main():
    start=time.monotonic();u,v,t=s.symbols('u v t');a,b=s.symbols('a b')
    p=(a,b,1-a-b);h=(0,t,1)
    def expand(x):return s.Poly(x,a,b,t).as_expr()
    def jet(hh):
        z=[sum(p[i]*hh[i]**k for i in range(3))/math.factorial(k) for k in range(5)]
        r=[]
        for i in range(3):
            ri=[p[i]]
            for n in range(1,5):
                ri.append(expand(p[i]*hh[i]**n/math.factorial(n)-sum(z[k]*ri[n-k] for k in range(1,n+1))))
            r.append(ri)
        A=[]
        for n in range(5):
            A.append(expand(9*sum(r[i][k]*r[i][n-k] for i in range(3) for k in range(n+1))-(3 if n==0 else 0)))
        return [expand(math.factorial(n)*sum(A[k]*A[n-k] for k in range(n+1))) for n in range(5)]
    ds=jet(h);grad=jet((1,0,0))[1]/2
    vec=[expand(p[0]*(int(j==0)-p[j])*s.diff(ds[2],a)+p[1]*(int(j==1)-p[j])*s.diff(ds[2],b)) for j in range(3)]
    assert expand(sum(vec))==0
    N=s.Rational(2,3)*(1-t+t*t)
    raw={}
    for sign in (-1,1):
        raw[f'Gv_{sign:+d}']=8+sign*grad
        raw[f'D2_{sign:+d}']=20*N+sign*ds[2]
        raw[f'D4_{sign:+d}']=99*N*N+sign*ds[4]
    raw['D3_squared']=38**2*N**3-ds[3]**2
    raw['D3_mixed_squared']=38**2*N**2-sum(x*x for x in vec)
    report_path=HERE/'fourth_derivative_v1/report.json'
    report=json.loads(report_path.read_text(encoding='utf-8'))
    assert report['status']=='EXACT BERNSTEIN COVER PASS' and len(report['jobs'])==8
    rebuilt={name:s.Poly(poly.subs({a:u,b:(1-u)*v},simultaneous=True),u,v,t) for name,poly in raw.items()}
    rows=[]
    for job in report['jobs']:
        poly=rebuilt[job['name']]
        saved=s.Poly.from_dict({tuple(e):s.Rational(q) for e,q in job['root_power_terms']},(u,v,t))
        assert poly==saved,job['name']
        shape=tuple(job['shape']);assert shape==tuple(poly.degree(z)+1 for z in (u,v,t))
        # Independent direct basis conversion, one tensor axis at a time.
        coeff={e:F(int(q.p),int(q.q)) for e,q in poly.terms()}
        for axis in range(3):
            out={};n=shape[axis]-1
            for idx in itertools.product(*(range(k) for k in shape)):
                val=F(0)
                for j in range(idx[axis]+1):
                    source=list(idx);source[axis]=j
                    val+=coeff.get(tuple(source),F(0))*F(math.comb(idx[axis],j),math.comb(n,j))
                if val:out[idx]=val
            coeff=out
        den=math.lcm(*(q.denominator for q in coeff.values()))
        indices=list(itertools.product(*(range(k) for k in shape)))
        root=[int(coeff.get(idx,F(0))*den) for idx in indices]
        positions={idx:i for i,idx in enumerate(indices)}
        def children(values,axis):
            n=shape[axis]-1;left=values.copy();right=values.copy()
            others=[k for k in range(3) if k!=axis]
            for pair in itertools.product(*(range(shape[k]) for k in others)):
                base=dict(zip(others,pair));ix=[]
                for j in range(n+1):
                    pos=tuple(j if k==axis else base[k] for k in range(3));ix.append(positions[pos])
                tri=[values[i] for i in ix]
                for depth in range(n+1):
                    left[ix[depth]]=tri[0]*2**(n-depth)
                    right[ix[n-depth]]=tri[-1]*2**(n-depth)
                    tri=[x+y for x,y in zip(tri,tri[1:])]
            return left,right
        leaves={r['path']:r for r in job['leaves']};paths=sorted(leaves)
        assert len(paths)==len(job['leaves']) and all(not y.startswith(x) for x,y in zip(paths,paths[1:]))
        depth=max(map(len,paths));assert sum(2**(depth-len(path)) for path in paths)==2**depth
        stack=[('',root)];seen=set()
        while stack:
            path,c=stack.pop()
            if path in leaves:
                assert min(c)>=0,(job['name'],path);seen.add(path)
            else:
                assert any(q.startswith(path) for q in paths)
                left,right=children(c,len(path)%3)
                stack.extend([(path+'0',left),(path+'1',right)])
        assert seen==set(paths)
        rows.append({'name':job['name'],'jet_identity':True,'complete_cover':True,'leaves':len(paths)})
    # A deliberately impossible curvature constant is refuted at an exact point.
    point={a:s.Rational(1,2),b:s.Rational(1,2),t:1}
    assert ds[2].subs(point)!=0
    output={'status':'INDEPENDENT_JET_AND_RATIONAL_COVER_PASS','rows':rows,
            'negative_control':'zero Hessian bound rejected at (1/2,1/2,0), h=(0,1,1)',
            'producer_report_sha256':hashlib.sha256(report_path.read_bytes()).hexdigest(),
            'replay_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'elapsed_seconds':time.monotonic()-start}
    (HERE/'fourth_derivative_replay.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(output))

if __name__=='__main__':main()
