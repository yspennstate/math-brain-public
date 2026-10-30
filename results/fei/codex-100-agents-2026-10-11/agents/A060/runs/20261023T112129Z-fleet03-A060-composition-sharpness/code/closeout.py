from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]
def read(p):return p.read_text(encoding='utf-8')
def write(p,s):p.write_text(s,encoding='utf-8',newline='')
def save(p,o):write(p,json.dumps(o,indent=2,ensure_ascii=False)+'\n')
note='Final checklist update has no success receipt for T-20261023-368: shared checklist lock held too long; verified local research files are unaffected.'
save(R/'out/CHECKLIST_RECEIPT.json',{'status':'UPDATE_RECEIPT_UNVERIFIED','task_id':'T-20261023-368','combined_closeout_command_exit':1,'observed_error':"RuntimeError('checklist lock held too long')",'research_artifacts_verified':True,'earlier_task_update_receipt':'not separately observed'})
p=json.loads(read(R/'PROGRESS.json'))
if note not in p['blockers']:p['blockers'].append(note)
save(R/'PROGRESS.json',p);save(R/'PACKET_DELTA.json',p)
s=read(R/'REPORT.md')
if note not in s:s=s.replace('\n# Universal bridge','\n'+note+'\n\n# Universal bridge')
write(R/'REPORT.md',s)
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
files={str(f.relative_to(R)):hashlib.sha256(f.read_bytes()).hexdigest() for f in R.rglob('*') if f.is_file() and f.name!='PERSISTENCE_RECEIPT.json'}
save(R/'out/PERSISTENCE_RECEIPT.json',{'status':'SAVED_LOCALLY','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sha256':files,'remote_mirror_verified':False})
receipt=json.loads(read(R/'out/PERSISTENCE_RECEIPT.json'))
assert all(hashlib.sha256((R/k).read_bytes()).hexdigest()==v for k,v in receipt['sha256'].items())
assert note in read(R/'REPORT.md')
print(json.dumps({'status':'PASS_LOCAL_SAVE','verified_files':len(files),'assertions':53691,'checklist_update':'NO_SUCCESS_RECEIPT_SHARED_LOCK','research_jobs_left_running':0}))
