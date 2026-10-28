from pathlib import Path
import hashlib,json,shutil
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT.parent.parent.parent.parent/'agents/A084/runs/20261023T035136Z-account03-A084-continuum-parameters'
(ROOT/'out').mkdir(exist_ok=True)
pins={}
for name,dest in [('joint.py','profile_engine.py'),('arithmetic.py','arithmetic.py')]:
    p=SOURCE/'code'/name;pins[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest();shutil.copyfile(p,ROOT/'code'/dest)
for name in ['REPORT.md','CLAIMS.json','out/JOINT_CASES.json']:
    p=SOURCE/name;pins[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
spec={'version':'A075-third-core-v1','source_helper_pins':pins,
 'family':'Fplus=J(-1,+1,g,g,g,g), original six-bit g negative {0,1,2}, J=-h(x xor1), h negative {0,1,2,4,8,16,32,6,17,40}',
 'pilot':{'cores':[2,4],'profile_states':144},
 'triples':[[2,3,4],[2,3,5]],'profile_states_per_triple':1728,
 'cuts':'for each triple, all three admitted source pairs and all144 pair-profile states; propagate actual minimum carried credit through every source-pair envelope allocation; compare full triple stopping hull',
 'symmetry':'only literal outer swaps2<->4 and3<->5, checked at all16 outer inputs; no unproved orbit quotient',
 'arithmetic':'exact rational prime-log forms, exact cancellation, directed192-bit logarithm intervals with proved atanh tail',
 'memory_estimate_mb':240,'pilot_max_seconds':55,'maximum_runtime_per_triple_seconds':300,
 'automatic_dimension_escalation':False,'root_credit':'same exact -S(Fplus), all stopped full functions and original donor bookings unchanged',
 'failure_policy':'save first unresolved comparison/runtime or credit failure; no theorem inferred from floats or absent failures outside declared finite domain'}
(ROOT/'out/FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
(ROOT.parent.parent/'STATUS.md').write_text('STATE: A075 stage8 active: testing third-core stopping hull against ACTUAL carried two-core credit; no new donor; FEI OPEN.\nNEXT: certify both fixed triple orbits and source-prefix cuts, or save first true credit shortfall with original physical path.\n',encoding='utf-8')
print(json.dumps({'frozen':str(ROOT/'out/FROZEN_SPEC.json'),'copied_helpers':2}))
