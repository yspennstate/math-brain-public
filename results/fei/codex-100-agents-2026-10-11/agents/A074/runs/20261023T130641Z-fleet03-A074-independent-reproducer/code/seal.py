from pathlib import Path
import json,hashlib,runpy
R=Path(__file__).resolve().parents[1]
f=R/'code/finalize.py';text=f.read_text(encoding='utf-8')
if 'Final audit hardened' not in text:
 marker="report='# A074: independent acceptance of universal signed composition coherence"
 note="sections[3]=(sections[3][0],sections[3][1]+' Final audit hardened interval signs to raise on uncertainty instead of choosing a hull branch. The same frozen domain was repeated once for this specific concern; all counts/verdicts remained unchanged, with no unresolved sign. Earlier output is retained as VALIDATION_BEFORE_SIGN_GUARD.json; the repeat is not additional cases.')\n"
 assert marker in text;text=text.replace(marker,note+marker,1);f.write_text(text,encoding='utf-8')
runpy.run_path(str(f),run_name='__main__')
report=(R/'REPORT.md').read_text(encoding='utf-8')
assert 'Final audit hardened' in report and 'Full FEI remains OPEN' in report
assert report.split('## Universal bridge\n\n')[1].strip()
v=json.loads((R/'out/VALIDATION.json').read_text(encoding='utf-8'))
assert v['unresolved_sign_policy'].startswith('raise ArithmeticError')
manifest=json.loads((R/'out/MANIFEST.json').read_text(encoding='utf-8'))
for row in manifest['files']:
 b=(R/row['path']).read_bytes()
 assert len(b)==row['bytes'] and hashlib.sha256(b).hexdigest()==row['sha256']
receipt={'status':'PASS','existing_manifest_entries_rehashed':len(manifest['files']),'owner_report_read_back':True,'unresolved_sign_guard_checked':True,'repeated_scope_unchanged':True,'full_fei':'OPEN','running_mathematical_jobs':0,'mirror':'UNVERIFIED'}
(R/'out/FINAL_READBACK.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
rows=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='MANIFEST.json':
  b=p.read_bytes();assert len(b)<20*1024*1024
  rows.append({'path':p.relative_to(R).as_posix(),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
(R/'out/MANIFEST.json').write_text(json.dumps({'files':rows,'excludes':'out/MANIFEST.json itself','count':len(rows)},indent=2)+'\n',encoding='utf-8')
print(report)
print((R.parents[1]/'STATUS.md').read_text(encoding='utf-8'))
print(json.dumps(receipt))
