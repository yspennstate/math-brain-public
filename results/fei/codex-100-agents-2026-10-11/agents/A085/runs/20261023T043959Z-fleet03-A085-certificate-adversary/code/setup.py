from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[1]
(R/'out').mkdir(exist_ok=True)
old=R.parents[0]/'20261021T174013Z-fleet03-A085-certificate-adversary/code/check_reset.py'
src=old.read_text(encoding='utf-8').split('\ndef run(n):')[0]
(R/'code/log_intervals.py').write_text(src,encoding='utf-8')
p=R/'code/check.py'
spec={'helper_version':'A085-stage8-independent-fwht-v1','helper_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'log_helper_origin':str(old),'log_helper_sha256':hashlib.sha256((R/'code/log_intervals.py').read_bytes()).hexdigest(),'family':'Actual F=a+z*(1-a^2)*h, fixed 4-bit controller row; physical restrictions; complete supplied references','pilot_domain':'All 6 labelled seeds n=0,1; controller root and two fully fixed beta endpoints; two signed children; two reference models','pilot_signed_fixtures':72,'domain':'All 22 labelled seeds n=0,1,2; controller root, first-bit 0/1, fully fixed indices 0/1; both signs; two reference models; one explicit four-bit seed with negative indices 0,1,2,4','main_signed_fixtures':440,'explicit_histories':1,'symmetry':'none; no exhaustive adaptive-tree claim','arithmetic':'integer FWHT plus independent direct characters, Fraction laws, prime-log identities and 100-bit/40-term outward dyadic atanh signs; integer-power scalar certificates','memory_estimate_MB':120,'pilot_max_seconds':55,'main_max_seconds':55,'max_truth_dimension':9,'automatic_dimension_escalation':False,'gpu':False,'heavy_job':False}
(R/'out/FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
print('FROZEN spec and own portable log helper saved')
