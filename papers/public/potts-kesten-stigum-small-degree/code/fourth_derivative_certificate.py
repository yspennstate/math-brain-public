"""Exact polynomial certificates for Q(p)=(9 sum p_i^2-3)^2.

One CPU, estimated memory <500 MB. Unfinished covers are NOT proofs.
Reuses only the rational Bernstein engine, not its softmax polynomials.
"""
import os
os.environ['OMP_NUM_THREADS']='1'
import argparse, ctypes, hashlib, json, time
from pathlib import Path
import sympy as s
import softmax_derivative_certificate as engine

HERE=Path(__file__).resolve().parent
OUT=HERE/'fourth_derivative_v1'
SOURCE=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()

def polynomials():
    a,b=s.symbols('a b'); t=engine.t
    p=(a,b,1-a-b); h=(0,t,1)
    mean=sum(p[i]*h[i] for i in range(3))
    def directional(f):
        return s.Poly(p[0]*(h[0]-mean)*s.diff(f,a)+p[1]*(h[1]-mean)*s.diff(f,b),a,b,t).as_expr()
    def coordinate(f,j):
        return s.expand(p[0]*(int(j==0)-p[j])*s.diff(f,a)+p[1]*(int(j==1)-p[j])*s.diff(f,b))
    A=9*sum(z*z for z in p)-3
    Q=s.expand(A*A); ds={0:Q}
    for n in range(1,5): ds[n]=directional(ds[n-1])
    mixed=[coordinate(ds[2],j) for j in range(3)]
    assert s.expand(sum(mixed))==0
    # All directions reduce to (0,t,1), 0<=t<=1, by simultaneous
    # permutation, translation, and scaling. Q is permutation invariant.
    N=s.Rational(2,3)*(1-t+t*t)
    raw=[]
    for sign in (-1,1):
        raw.extend([(f'Gv_{sign:+d}',8+sign*coordinate(Q,0)/2),
                    (f'D2_{sign:+d}',20*N+sign*ds[2]),
                    (f'D4_{sign:+d}',99*N*N+sign*ds[4])])
    raw.extend([('D3_squared',38**2*N**3-ds[3]**2),
                ('D3_mixed_squared',38**2*N**2-sum(z*z for z in mixed))])
    sub={a:engine.u,b:(1-engine.u)*engine.v}
    return [(name,s.Poly(f.subs(sub,simultaneous=True),*engine.VAR)) for name,f in raw]

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--seconds',type=float,default=90)
    args=parser.parse_args(); start=time.monotonic()
    class Mem(ctypes.Structure):
        _fields_=[('length',ctypes.c_ulong),('load',ctypes.c_ulong)]+[(n,ctypes.c_ulonglong) for n in ['total','available','page_total','page_available','virtual_total','virtual_available','extended']]
    mem=Mem();mem.length=ctypes.sizeof(mem)
    assert ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(mem)) and mem.available>2_000_000_000
    OUT.mkdir(exist_ok=True); cp=OUT/'checkpoint.json'; final=OUT/'report.json'
    if final.exists():
        state=json.loads(final.read_text(encoding='utf-8'));assert state['source_sha256']==SOURCE
        print(json.dumps({'status':state['status'],'already_complete':True}));return
    if cp.exists():
        state=json.loads(cp.read_text(encoding='utf-8'));assert state['source_sha256']==SOURCE
        assert len(state['jobs'])==8
    else:
        state={'source_sha256':SOURCE,'engine_sha256':hashlib.sha256(Path(engine.__file__).read_bytes()).hexdigest(),
               'scope':'Global Q derivatives only; no reconstruction cutoff',
               'targets':{'Gv':'8','D2':'20','D3':'38','D3mixed':'38','D4':'99'},'jobs':[]}
        for name,poly in polynomials():
            shape,c,den=engine.bernstein(poly)
            state['jobs'].append({'name':name,'shape':shape,'root_denominator':den,
                'root_sha256':engine.digest(c),'root_power_terms':[[list(e),str(q)] for e,q in poly.terms()],
                'stack':[{'path':'','coefficients':c}],'leaves':[],'visited':0})
        assert len(state['jobs'])==8
        engine.atomic(cp,state)
    deadline=time.monotonic()+args.seconds
    for job in state['jobs']:
        while job['stack']:
            if time.monotonic()>deadline:
                engine.atomic(cp,state);print(json.dumps({'status':'CHECKPOINT','completed':sum(not j['stack'] for j in state['jobs']),'elapsed':time.monotonic()-start}));return
            node=job['stack'].pop();path,c=node['path'],node['coefficients'];job['visited']+=1
            if min(c)>=0:
                job['leaves'].append({'path':path,'minimum':min(c),'sha256':engine.digest(c)})
            elif max(c)<0:
                state['status']='NEGATIVE_BOX';state['failure']={'job':job['name'],'path':path}
                engine.atomic(OUT/'failure.json',state);raise AssertionError(state['failure'])
            elif len(path)>=36:
                job['stack'].append(node);engine.atomic(cp,state);print(json.dumps({'status':'UNRESOLVED','job':job['name'],'path':path}));return
            else:
                left,right=engine.split(c,job['shape'],len(path)%3)
                job['stack'].extend([{'path':path+'1','coefficients':right},{'path':path+'0','coefficients':left}])
        engine.cover(job['leaves']);engine.atomic(cp,state)
    state['status']='EXACT BERNSTEIN COVER PASS';engine.atomic(final,state)
    print(json.dumps({'status':state['status'],'jobs':len(state['jobs']),'leaves':sum(len(j['leaves']) for j in state['jobs']),'elapsed':time.monotonic()-start}))

if __name__=='__main__':main()
