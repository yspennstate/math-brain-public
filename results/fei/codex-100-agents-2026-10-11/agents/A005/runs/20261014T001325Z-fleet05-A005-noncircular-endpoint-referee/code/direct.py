from pathlib import Path
import json,time
P=Path(__file__).resolve();scope={'__name__':'reuse','__file__':str(P.with_name('check.py'))}
exec(compile(P.with_name('check.py').read_text(),str(P.with_name('check.py')),'exec'),scope)
Q=scope['Q'];ROOT=P.parents[1];start=time.perf_counter();checks=0
def eq(a,b):
    global checks
    checks+=1;assert a==b,(a,b)
f=scope['seed'](3,254);v=[f[x&7] for x in range(4096)];v[0]*=-1
a=scope['fwht'](v);al=Q(1,2048)
eq(len(a),4096);eq(all(a),True);eq(sum((x*x for x in a),Q(0)),1)
for i in range(12):
    eq(scope['influence'](a,i),scope['physical_i'](v,12,i))
    eq(scope['scope']['scope']['erasure'](a,i),scope['core_B'](scope['fwht'](f),-1,3,12,i) if i<3 else scope['dummy_B'](scope['fwht'](f),-1,3,12))
C=Q(8,3)
for i in [0,3]:
    Hs=[];Is=[]
    for b in [0,1]:
        child=scope['scope']['restricted'](v,12,i,b);ca=scope['fwht'](child)
        Hs.append(scope['entropy'](ca));Is.append(scope['total'](ca,11))
    eq((Is[0]+Is[1])/2,scope['total'](a,12)-scope['influence'](a,i))
    sigma=scope['add'](scope['const'](C*(Is[0]+Is[1])/2),scope['scale'](scope['add'](*Hs),-Q(1,2)))
    eq(scope['sign'](sigma),1 if i==0 else -1)
    eq([scope['sign'](scope['add'](scope['const'](C*I),scope['scale'](H,-1))) for H,I in zip(Hs,Is)],[1,0] if i==0 else [-1,-1])
elapsed=time.perf_counter()-start;assert elapsed<60
r={'cases':1,'assertions':checks,'failures':0,'dimension':12,'elapsed_seconds':elapsed,'arithmetic':'Actual physical truth tables and integer Walsh transform; exact rational log-prime identities and outward rational logarithm intervals'}
(ROOT/'out/DIRECT_VALIDATION.json').write_text(json.dumps(r,indent=2),encoding='utf-8');print(json.dumps(r))
