"""Local-only source refinement, frozen before the new computations."""
from pathlib import Path
import json
r=Path(__file__).resolve().parents[1]
spec={'helper':'A062-sparse-reference-v2','reason':'v1 full validation exceeded its 55s runtime guard, without a mathematical assertion failure; binary-log input mantissas now rigorously bracketed at 64 bits before the unchanged 28-term interval kernel','family':'point functions n=2..20, both original empty masses; general fixtures below','point_roots':38,'point_histories_including_constants':456,'point_raw_width_max':7,'general_families':[{'widths':w,'parity_shift':b} for w,b in [([2],0),([3],0),([4],0),([2,3],0),([3,3],0),([3,4],0),([4,4],0),([3],1),([4],1)]],'general_cases':54,'lambda':['1','1/2','1/4'],'reference_empty_choices':['actual product empty','actual source empty'],'symmetry':'all active point histories determined by remaining dimension and original reference; general fixtures use all exact Walsh atoms and direct influence edges','arithmetic':'Fraction; rigorous integer log bracketing via floor(v/2^s), outward fixed-point log intervals, no floating mathematical tests','memory_estimate_MB':100,'max_runtime_seconds_per_job':55,'pilot':'point n=2,3,4 and same two empty choices; no dimension escalation','constant':'analytic log2(e); executed strict certificates use its rigorous lower endpoint; rational owner 3/2 also checked','checkpoint':'point results saved after every completed root'}
(r/'REFINEMENT_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
(r/'out/V1_RUNTIME_GUARD.json').write_text(json.dumps({'status':'runtime_guard_failed','domain':'point n=2..20 with two original reference choices','failure':'k.check(time.monotonic()-start<55) at root boundary','mathematical_failure_reported':False,'full_artifact_written':False,'repair':'v2 rigorous log input bracketing and per-root checkpoints'},indent=2)+'\n',encoding='utf-8')
p=r/'code/check.py';s=p.read_text(encoding='utf-8').replace('A062-sparse-reference-v1','A062-sparse-reference-v2').replace('C=F(5,3)','C=F(3,2)\nLOGE_LO=F(1)/k.L2[1]')
s=s.replace('@lru_cache(None)\ndef log(x):','@lru_cache(None)\ndef integer_log(v):\n shift=max(0,v.bit_length()-64)\n if not shift:return k.log_bounds(v)\n a=v>>shift\n return (k.log_bounds(a)[0]+shift*k.SCALE,k.log_bounds(a+1)[1]+shift*k.SCALE)\n@lru_cache(None)\ndef log(x):')
s=s.replace('k.log_bounds(x.numerator),k.log_bounds(x.denominator)','integer_log(x.numerator),integer_log(x.denominator)')
s=s.replace('<=C*row[\'I\']','<=LOGE_LO*row[\'I\']').replace('<C*row[\'I\']','<LOGE_LO*row[\'I\']')
s=s.replace("   k.check(time.monotonic()-start<55)","   (ROOT/'out'/('PILOT_PARTIAL.json' if pilot else 'PARTIAL.json')).write_text(json.dumps(serial({'roots':roots,'assertions':k.ASSERTIONS,'seconds':time.monotonic()-start})),encoding='utf-8')\n   k.check(time.monotonic()-start<55)")
p.write_text(s,encoding='utf-8')
p=r/'code/general.py';s=p.read_text(encoding='utf-8').replace('bkl,C,serial','bkl,C,LOGE_LO,serial')
s=s.replace('for widths in [[3],[4],[3,3],[3,4],[4,4]]:','for widths,phase in [([2],0),([3],0),([4],0),([2,3],0),([3,3],0),([3,4],0),([4,4],0),([3],1),([4],1)]:')
s=s.replace('  truth.append(bit)','  truth.append(bit ^ (phase*(x.bit_count()%2)))')
s=s.replace('and max(marg)<=F(1,4)','and all(0<d<1 for d in marg)')
s=s.replace("<C*I","<LOGE_LO*I").replace("'widths':widths,","'widths':widths,'parity_shift':phase,")
# Equality also occurs when TC and the binary mismatch both vanish.
s=s.replace('if lam==1 and empty==p[0]:','if lam==1 and (empty==p[0] or p[0]==q[0]):')
(r/'out/GENERAL_V1.json').write_bytes((r/'out/GENERAL.json').read_bytes())
p.write_text(s,encoding='utf-8')
print('Frozen v2 refinement and rewritten sources saved.')
