from pathlib import Path
import json,time
run=Path(__file__).resolve().parents[1]
helper=run.parent/'20261012T003951Z-account05-A062-influence-compensator/code/check_reserve.py'
env={'__file__':str(helper)}
exec(compile(helper.read_text().split('core_rows=[]')[0],str(helper),'exec'),env)
F=env['F']; measure=env['measure']; equal=env['equal']; plus=env['plus']; mul=env['mul']; leq=env['leq']
start=time.perf_counter(); cases=0
for mask in range(16):
    g=tuple(1 if (mask>>x)&1 else -1 for x in range(4))
    for v in range(4):
        gv=tuple(-y if x==v else y for x,y in enumerate(g))
        f=tuple(-g[x&3] if x==v else g[x&3] for x in range(64))
        actual=[tuple(f[x+(a<<2)] for x in range(4)) for a in range(16)]
        equal(actual,[gv]+[g]*15,'terminal_actual_core_assignment')
        _,Hg,Ig=measure(g); _,Hv,Iv=measure(gv); _,Hf,If=measure(f)
        expectedI=(15*sum(Ig)+sum(Iv))/16
        equal(sum(If)-expectedI,F(4,32),'initial_minus_retained_influence')
        equal(If[2:],[F(1,32)]*4,'four_owned_dummy_accounts')
        Hactual=env['point'](0)
        for h in actual: Hactual=plus(Hactual,mul(measure(h)[1],F(1,16)))
        Hexpected=mul(plus(mul(Hg,15),Hv),F(1,16))
        leq(max(Hactual[0],Hexpected[0]),min(Hactual[1],Hexpected[1]),'retained_entropy_interval_overlap')
        cases+=1
elapsed=time.perf_counter()-start
assert elapsed<60
out={'reviewed_scope':'A061-ARBITRARY-CORE-EDIT-ADMISSION v1 terminal ownership only','cases':cases,'assertions':sum(env['counts'].values()),'counts':dict(env['counts']),'failures':0,'runtime_seconds':elapsed,'whole_claim_accepted':False}
(run/'out/TERMINAL_REVIEW.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
