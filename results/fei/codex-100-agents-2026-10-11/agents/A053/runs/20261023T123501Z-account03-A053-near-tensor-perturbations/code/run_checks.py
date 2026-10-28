from pathlib import Path
import subprocess,sys,json,hashlib,time,os
RUN=Path(__file__).resolve().parents[1]
spec=json.loads((RUN/'out/FROZEN_SPEC.json').read_text(encoding='utf-8'))
spec.update({'revision':2,'main_case_count':1503,'main_coordinate_cuts':4572,'pilot_case_count':592,'independent_case_count':1478,'independent_fixtures':[[6,[0]],[6,[0,7]],[6,list(range(8))],[9,[0]],[9,[0,1]],[9,list(range(8))]],'code_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (RUN/'code').glob('*.py')}})
(RUN/'out/FROZEN_SPEC_V2.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
records=[]
for label,args in [('pilot',['check_linear.py','--pilot']),('full',['check_linear.py']),('independent',['independent.py'])]:
 cmd=[sys.executable,'-B','-X','utf8',str(RUN/'code'/args[0])]+args[1:]
 start=time.perf_counter()
 try:
  r=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,encoding='utf-8',timeout=60,creationflags=0x08000000 if os.name=='nt' else 0)
  output=r.stdout;exitcode=r.returncode
 except subprocess.TimeoutExpired as e:
  output='FROZEN WALL-TIME GUARD EXPIRED';exitcode=124
 (RUN/'out'/f'{label}.log').write_text(output,encoding='utf-8')
 records.append({'label':label,'command':cmd,'exit_code':exitcode,'controller_wall_seconds':time.perf_counter()-start})
 (RUN/'out/JOBS.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
 print(label,'exit',exitcode,flush=True)
 if exitcode:
  print(output);raise SystemExit(exitcode)
for name in ['PILOT.json','EXACT_CHECK.json','INDEPENDENT.json']:
 print(name,(RUN/'out'/name).read_text(encoding='utf-8'))
