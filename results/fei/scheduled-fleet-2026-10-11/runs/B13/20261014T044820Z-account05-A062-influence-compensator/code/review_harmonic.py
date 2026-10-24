from pathlib import Path
import json,time
run=Path(__file__).resolve().parents[1]
prior=run.parent/'20261014T015800Z-account05-A062-influence-compensator/code/check_transfer.py'
env={'__file__':str(prior)}
exec(compile(prior.read_text().split("pilot='--pilot'")[0],str(prior),'exec'),env)
F=env['F']; point=env['point']; plus=env['plus']; mul=env['mul']; tree=env['tree']; equal=env['equal']; measure=env['measure']; leq=env['leq']; fmt=env['fmt']
start=time.perf_counter()
# Core zero is a three-bit point defect after revealing its first bit as zero.
cores=[tuple(-1 if x==0 else 1 for x in range(4)),tuple(-1 if x==0 else 1 for x in range(8)),(1,-1)]
Rs=[tree(g,tuple(range(len(g).bit_length()-1)),1)[0] for g in cores]
leq(F(1),Rs[0][0],'partial_core_nonzero_reserve')
leq(F(3,2),Rs[1][0],'second_core_nonzero_reserve')
cases=0
for code in range(81):
    a=code; labels=[]
    for _ in range(4): labels.append(a%3); a//=3
    values=[]
    for x in range(256):
        state=labels[x&3]
        data=((x>>2)&3,(x>>4)&7,(x>>7)&1)
        values.append(cores[state][data[state]])
    measure(tuple(values)) # actual spectrum and physical edges independently agree.
    qp=[F(labels.count(j),4) for j in range(3)]
    for i in range(2):
        qc=[[F(sum(labels[x]==j for x in range(4) if ((x>>i)&1)==bit),2) for j in range(3)] for bit in (0,1)]
        drift=point(0)
        for j in range(3):
            coeff=qp[j]-(qc[0][j]+qc[1][j])/2
            equal(coeff,F(0),'actual_core_route_martingale')
            drift=plus(drift,mul(Rs[j],coeff))
        equal(drift,point(0),'owned_actual_core_reserve_harmonic')
        cases+=1
elapsed=time.perf_counter()-start
assert elapsed<60,elapsed
out={'source_claim':'A064 repeated-fallback/global-priority potential current version; core-weight harmonic controller clause only','cases':cases,'assertions':sum(env['env']['counts'].values()),'counts':dict(env['env']['counts']),'failures':0,'runtime_seconds':elapsed,'whole_claim_accepted':False,'remaining_core_reserves':[fmt(q) for q in Rs]}
(run/'out/HARMONIC_REVIEW.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='remaining_core_reserves'},indent=2))
