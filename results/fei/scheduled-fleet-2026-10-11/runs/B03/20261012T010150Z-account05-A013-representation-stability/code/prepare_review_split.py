from pathlib import Path
import json
p=Path(__file__).resolve().parents[1]
spec={'helper':'review-v4-split','family':'same balanced activation reference; literal witness','domain':'90 reference cases; literal posterior r1..3; coefficient r1..5 plus analytic all-r tail','case_count':[90,3,5],'symmetry':'none','arithmetic':'exact rational prime-log; rational outward log intervals','memory_MB':70,'maximum_runtime_seconds_each':50,'change':'Separate reference and posterior ledgers after cumulative cutoff; freeze posterior r1..3, no escalation.'}
(p/'out/REVIEW_SPLIT_SPEC.json').write_text(json.dumps(spec,indent=2))
s=(p/'code/check_review_v3.py').read_text();a=s.index('# Independent reference review');b=s.index('# Reconstruct true');d=s.index("result={'helper'")
prefix=s[:a]
ref=s[a:b]+"\nresult={'status':'PASS','exact_assertions':checks,'activation_reference_cases':activation_cases,'elapsed_seconds':time.perf_counter()-start}\n(RUN/'out/REFERENCE_RESULTS.json').write_text(json.dumps(result,indent=2))\nprint(json.dumps(result))\n"
post=s[b:d].replace('for r in [1,2,3,4]:','for r in [1,2,3]:')+"\nresult={'status':'PASS','exact_assertions':checks,'posterior_joint_cases':posterior_cases,'sharp_coefficient_interval':[str(x) for x in enclose(cstar)],'elapsed_seconds':time.perf_counter()-start}\n(RUN/'out/POSTERIOR_RESULTS.json').write_text(json.dumps(result,indent=2))\nprint(json.dumps({k:v for k,v in result.items() if k!='posterior_joint_cases'}))\n"
(p/'code/check_reference.py').write_text(prefix+ref)
(p/'code/check_posterior.py').write_text(prefix+post)
print('Frozen separate review jobs.')
