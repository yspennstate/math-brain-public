from pathlib import Path
import json,sys,subprocess,importlib.util,hashlib,time
R=Path(__file__).resolve().parents[1]
specification={'target':'core Lean integer coefficient signs only; main entropy/variance theorem remains analytic','arithmetic':'Lean Nat decide','memory_estimate_mb':250,'maximum_runtime_seconds':25,'threads':1,'Mathlib':False}
(R/'out'/'FORMAL_SPEC.json').write_text(json.dumps(specification,indent=2),encoding='utf-8')
state=json.loads(Path(r'~\.claude\compute\compute_state.json').read_text(encoding='utf-8-sig'))
receipt={'scope':specification['target'],'state':{k:state.get(k) for k in ['ts','status','mem_avail_mb','commit_avail_mb']}}
if state.get('status')!='ok' or state.get('mem_avail_mb',0)<4000 or state.get('commit_avail_mb',0)<8000:
 receipt['status']='ADMISSION_HELD';receipt['compiler_launched']=False
else:
 tool=Path(r'lean_check.py')
 sys.path.insert(0,str(tool.parent));spec=importlib.util.spec_from_file_location('lc',tool);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
 compiler=Path(mod.LEAN);source=R/'code'/'Coefficients.lean'
 receipt.update({'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'compiler':str(compiler),'compiler_sha256':hashlib.sha256(compiler.read_bytes()).hexdigest(),'project_toolchain':(Path(mod.PROJECT)/'lean-toolchain').read_text(encoding='utf-8').strip(),'compiler_launched':True})
 start=time.perf_counter()
 try:
  out=subprocess.run([str(compiler),'-j1',str(source)],cwd=R/'code',capture_output=True,text=True,encoding='utf-8',timeout=25,creationflags=0x08000000|0x00004000)
  receipt.update({'exit_code':out.returncode,'output':out.stdout+out.stderr,'seconds':time.perf_counter()-start})
  receipt['status']='LEAN_CORE_COEFFICIENTS_ONLY' if out.returncode==0 and out.stdout.count('does not depend on any axioms')==2 else 'RUNTIME_UNVERIFIED'
 except subprocess.TimeoutExpired:
  receipt.update({'status':'RUNTIME_UNVERIFIED','seconds':time.perf_counter()-start,'reason':'25-second timeout; no retry'})
(R/'out'/'FORMAL.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8');print(json.dumps(receipt))
