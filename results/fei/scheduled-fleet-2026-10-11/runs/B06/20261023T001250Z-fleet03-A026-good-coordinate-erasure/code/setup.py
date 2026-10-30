from pathlib import Path
import json,hashlib,subprocess,sys
R=Path(__file__).resolve().parents[1];(R/'out').mkdir(exist_ok=True)
p=Path(r'~\brain_workers\FEI100_20261011\agents\A097\runs\20261021T232544Z-fleet03-A097-cross-route-transfer\code\check_transfer.py')
s=p.read_text(encoding='utf-8').replace("if time.perf_counter()-START>55:","if time.perf_counter()-START>240:")
(R/'code/helper.py').write_text(s,encoding='utf-8')
spec={'helper_version':'A026-dummy-canonical-reset-v1; A097 direct-character helper copied, main uses independent FWHT override','family':'F=1-2A_a+2A_(a+b+r), arbitrary supplied source references tested in four frozen shapes','parameter_domain':{'a':[1,2,3],'b':[1,2],'r':[2,3],'references':['matching','uniform','increasing','dummy-singleton-spiked']},'case_count':'48 roots; all eligible active/control/dummy TYPE words and stopping prefixes, fixed first label in each current type; independent reconstruction on same 48 roots','symmetry':'no source-reference quotient; no claim of exhausting physical label permutations; analytic statement covers relabelings','arithmetic':'Fraction spectra, exact reference matrices, rational22-term atanh intervals with proved tail; independent direct character sums','memory_estimate_mb':100,'max_runtime_seconds':240,'pilot':{'a':[1,2],'b':[1],'r':[2],'references':['matching','increasing'],'roots':4,'max_seconds':55},'no_automatic_escalation':True}
(R/'FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
(R/'out/HELPER_RECEIPT.json').write_text(json.dumps({'source':str(p),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'copied_sha256':hashlib.sha256((R/'code/helper.py').read_bytes()).hexdigest(),'change':'helper internal guard55->240 seconds; original __main__ search not invoked'},indent=2)+'\n',encoding='utf-8')
agent=R.parent.parent
(agent/'STATUS.md').write_text('STATE: Stage18 active: consuming A028/A029 mixed-JS transport; deriving dummy-DATA canonical reset from SAME A097 source bank; FEI OPEN.\nNEXT: Exact local likelihood/canonical marginal checks and all-type mixed histories; retain both full terminals and old debits.\n',encoding='utf-8')
lean='example (q w d : Int) (h : w + d ≤ q) : 0 ≤ q - w - d := by omega\n'
(R/'code/Bank.lean').write_text(lean,encoding='utf-8')
gate=subprocess.run([sys.executable,'-X','utf8',r'~\brain_workers\FEI100_20261011\tools\memok.py'],capture_output=True,text=True,encoding='utf-8',creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
receipt={'admission_exit_code':gate.returncode,'admission_output':gate.stdout+gate.stderr,'statement_scope':'integer bank rearrangement only; no entropy/likelihood/FEI formalization','status':'NOT_RUN_ADMISSION_REFUSED' if gate.returncode else 'ADMITTED'}
if gate.returncode==0:
 p=subprocess.run([sys.executable,'-X','utf8',r'~\.claude\dreaming\lean_check.py','--core','--stmt',lean.strip()],capture_output=True,text=True,encoding='utf-8',creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
 receipt.update(compiler_exit_code=p.returncode,output=p.stdout+p.stderr,status='SEE_COMPILER_RECEIPT_NO_ENTROPY_CERTIFICATE')
(R/'out/FORMAL_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'SETUP_PASS','spec_roots':48,'formal':receipt['status']}))
