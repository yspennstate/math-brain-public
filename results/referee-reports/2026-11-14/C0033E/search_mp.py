"""Checkpointed, single-process high precision spectral/graph collar searches."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'): os.environ[k]='1'
import json,time,resource,random,math,argparse
from pathlib import Path
import mpmath as mp
from mp_core import *

OUT=Path('data/search_mp.json')

def main():
    rng=random.Random(33505);start=time.monotonic()
    out=dict(seed=33505,arithmetic='mpmath, no binary atom arithmetic',groups={},records=[],failures=[],checkpoints=0,construction_rejections=0)
    count=0
    def save():
        out['seconds']=time.monotonic()-start;out['peak_rss_mib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20
        out['evaluations']=count;out['checkpoints']+=1
        tmp=OUT.with_suffix('.tmp');tmp.write_text(json.dumps(out,indent=2)+'\n');tmp.replace(OUT)
    def test(group,q,params):
        nonlocal count
        count+=1
        try:
            # Spectral construction is exact at working precision; Sylvester is
            # checked independently for entries not directly built spectrally.
            if not strict(q):raise ArithmeticError('not strict')
            ev=evaluate(q)
            row=strings(dict(**ev,group=group,precision=mp.mp.dps),65)
            row['parameters']=strings(params,mp.mp.dps+10)
            row['coordinates']=strings(coordinates(q),mp.mp.dps+10)
            gr=out['groups'].setdefault(group,dict(attempts=0,accepted=0,minimum=None,minimum_scaled=None))
            gr['attempts']+=1;gr['accepted']+=1
            if gr['minimum'] is None or ev['margin']<mp.mpf(gr['minimum']['margin']):gr['minimum']=row
            if gr['minimum_scaled'] is None or ev['scaled']<mp.mpf(gr['minimum_scaled']['scaled']):gr['minimum_scaled']=row
            if ev['margin']<0:out['records'].append(row);save();raise RuntimeError('negative margin: verify immediately')
        except (ArithmeticError,ZeroDivisionError,ValueError) as err:
            gr=out['groups'].setdefault(group,dict(attempts=0,accepted=0,minimum=None,minimum_scaled=None));gr['attempts']+=1
            if len(out['failures'])<50:out['failures'].append(dict(group=group,parameters=strings(params),error=str(err),precision=mp.mp.dps))
        if count%100==0:save()
    # 9 independent coordinate perturbations, both signs and multiple radii,
    # plus dense combinations. Norm controls guarantee their feasibility.
    for L in (20,60,150,400,1000):
        mp.mp.dps=100+int(L/math.log(10));q=cyclic(L)
        gap=mp.mpf('.5')-mp.sqrt(3)*abs(q[0,1]);test(f'cyclic_{L}',q,dict(L=L))
        for i in range(9):
            for sign in (-1,1):
                for factor in (mp.mpf('.01'),mp.mpf('.2'),mp.mpf('.65')):
                    perturb=B[i]*(sign*gap*factor/mp.sqrt(tr(B[i]*B[i])))
                    test(f'ambient_{L}',q+perturb,dict(L=L,direction=i,sign=sign,radius=factor))
        for j in range(120):
            coeff=[mp.mpf(str(rng.gauss(0,1))) for _ in range(9)]
            t=sum((coeff[i]*B[i] for i in range(9)),mp.zeros(3));t/=mp.sqrt(mp.re(tr(t*t)))
            factor=mp.mpf(str(rng.uniform(.01,.9)))
            test(f'ambient_{L}',q+gap*factor*t,dict(L=L,dense_index=j,radius=factor))
        print('ambient',L,'done',count,flush=True);save()
    # Arbitrary spectral orientations, with independent endpoint and middle
    # scales. Angles sampled logarithmically reach disconnected graph limits.
    for L in (20,60,150,400):
        mp.mp.dps=110+int(3*L/math.log(10))
        for j in range(650):
            angles=[]
            for i in range(3):
                if j%3==0:angles.append(mp.mpf(str(rng.uniform(0,math.pi/2))))
                else:angles.append(mp.atan(mp.exp(mp.mpf(str(rng.uniform(-.75,.75)))*L)))
            phase=mp.mpf(str(rng.uniform(-math.pi,math.pi))) if j%4 else mp.mpf(0 if j%8 else str(math.pi))
            g0=mp.mpf(str(rng.uniform(-.8,.8)))*L;g1=mp.mpf(str(rng.uniform(-.8,.8)))*L
            mid=mp.mpf(str(rng.uniform(-.85,.85)))*L
            params=angles+[phase,g0,g1,mid]
            try:q=spectral(params,L)
            except ArithmeticError:out['construction_rejections']+=1;continue
            test(f'spectral_graph_{L}',q,dict(L=L,params=params))
        print('spectral_graph',L,'done',count,flush=True);save()
    # Real/complex mixed face, independent exponents and phases, including
    # Q(t) of D and less symmetric connections.
    for L in (20,60,150,400):
        mp.mp.dps=120+int(5*L/math.log(10));t=mp.exp(-L)
        for j in range(400):
            a=mp.mpf(str(rng.uniform(.15,2.5)));b=mp.mpf(str(rng.uniform(.15,2.5)))
            eta=max(a,b)/2+mp.mpf(str(rng.uniform(.1,2.5)))
            ratio=mp.mpf(str(rng.uniform(.1,2)))
            phase=mp.mpf(0) if j%2==0 else mp.mpf(str(rng.uniform(-math.pi,math.pi)))
            q=mixed(t,a,b,eta,ratio,phase)
            test(f'mixed_{L}',q,dict(L=L,alpha=a,beta=b,eta=eta,ratio=ratio,phase=phase))
        for a,b,e in ((1,2,2),(2,1,2),(.5,2,2),(2,.5,2),(1,1,1.1),(2,2,2.1)):
            test(f'mixed_{L}',mixed(t,a,b,e),dict(L=L,alpha=a,beta=b,eta=e,ratio=1,phase=0))
        print('mixed',L,'done',count,flush=True);save()
    save()
    print('complete',count,out['seconds'],flush=True)
if __name__=='__main__':main()
