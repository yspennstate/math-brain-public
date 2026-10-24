from pathlib import Path
import json
run=Path(__file__).resolve().parents[1]
# Load the independent physical-tree oracle without executing its case loop.
p=run/'code/check_transfer.py'; env={'__file__':str(p)}
exec(compile(p.read_text().split("pilot='--pilot'")[0],str(p),'exec'),env)
F=env['F']; tree=env['tree']; equal=env['equal']; plus=env['plus']; mul=env['mul']; point=env['point']; leq=env['leq']; measure=env['measure']
controllers=[tuple(1 if (m>>x)&1 else -1 for x in range(4)) for m in range(16)]
controllers.append(tuple(-1 if x==0 else 1 for x in range(8)))
cases=0
for h in controllers:
 r=len(h).bit_length()-1
 values=tuple((1 if ((x>>(r+(0 if h[x&((1<<r)-1)]==1 else 1)))&1)==0 else -1) for x in range(1<<(r+2)))
 _,_,inf=measure(values)
 _,Hh,Ih=measure(h)
 equal(sum(inf[:r]),sum(Ih)/2,'root_controller_account')
 leaves=[tuple(values[x+(a<<r)] for x in range(1<<r)) for a in range(4)]
 equal(leaves,[tuple([1]*len(h)),tuple(-v for v in h),h,tuple([-1]*len(h))],'actual_data_frontier')
 for C in (1,2,6):
    R=tree(h,tuple(range(r)),C)[0]
    Rs=point(0); Hs=point(0); Is=F(0)
    for leaf in leaves:
        Rleaf,Hleaf,Ileaf=tree(leaf,tuple(range(r)),C)
        Rs=plus(Rs,mul(Rleaf,F(1,4)))
        Hs=plus(Hs,mul(Hleaf,F(1,4))); Is+=Ileaf/4
    expected=mul(R,F(1,2))
    leq(max(Rs[0],expected[0]),min(Rs[1],expected[1]),'retained_reserve_half_overlap')
    expectedH=mul(Hh,F(1,2))
    leq(max(Hs[0],expectedH[0]),min(Hs[1],expectedH[1]),'retained_entropy_half_overlap')
    equal(Is,sum(Ih)/2,'retained_influence_half')
    cases+=1
out={'scope':'A064 exclusive-controller boundary obstruction only; not full prefix theorem','cases':cases,'failures':0,'assertions':sum(env['env']['counts'].values()),'counts':dict(env['env']['counts']),'whole_claim_accepted':False}
(run/'out/BOUNDARY_REVIEW.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
