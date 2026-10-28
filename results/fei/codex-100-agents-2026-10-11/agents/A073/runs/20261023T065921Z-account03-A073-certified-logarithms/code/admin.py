from pathlib import Path
import subprocess,json,hashlib
R=Path(__file__).resolve().parents[1]
P=R.parent/'20261023T065417Z-account03-A073-certified-logarithms'
rows=[]
for task,description in [('T-20261023-270','A073 stage20 saved: independent scoped first-reset review HOLDS.'),('T-20261023-272','A073 stage21 saved: any finite fixed1/7 activation refreshes paid same rate4/all widths/load;27600 exact checks;FEI open,review pending.')]:
 p=subprocess.run(['python','-X','utf8','task_checklist_hook.py','done',task,description],capture_output=True,text=True,encoding='utf-8')
 rows.append({'task':task,'exit_code':p.returncode,'stdout':p.stdout[-1500:],'stderr':p.stderr[-1500:]})
for run in (P,R):
 (run/'out/ADMIN_RECEIPT.json').write_text(json.dumps({'attempts':rows,'mathematical_artifacts':'saved and checked independently of external checklist bookkeeping'},indent=2)+'\n',encoding='utf-8')
 if any(x['exit_code'] for x in rows):
  text=(run/'REPORT.md').read_text(encoding='utf-8');text=text.replace('## Universal bridge','External checklist completion callbacks were attempted twice but the shared checklist lock remained held; out/ADMIN_RECEIPT.json records the exact returned errors. All mathematical artifacts and local rolling files are saved; this is an external administrative receipt blocker only.\n\n## Universal bridge');(run/'REPORT.md').write_text(text,encoding='utf-8')
 manifest={str(p.relative_to(run)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(run.rglob('*')) if p.is_file() and p.name!='MANIFEST.json'}
 (run/'out/MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
 assert all(hashlib.sha256((run/p).read_bytes()).hexdigest()==h for p,h in manifest.items())
print(json.dumps({'checklist_attempts':[{'task':x['task'],'exit_code':x['exit_code']} for x in rows],'local_manifests':'verified'}))
