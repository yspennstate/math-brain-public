from pathlib import Path
import subprocess,os,json,datetime
ROOT=Path(__file__).resolve().parents[1]
HOME=Path('~')
gate=subprocess.run(['python','-X','utf8',str(HOME/'brain_workers/FEI100_20261011/tools/memok.py')],capture_output=True,text=True,encoding='utf-8')
(ROOT/'out/MEMOK.txt').write_text(gate.stdout+gate.stderr,encoding='utf-8')
if gate.returncode:
 result={'status':'NOT_ATTEMPTED_MEMORY_ADMISSION','exit_code':gate.returncode}
else:
 env=dict(os.environ);env['LEAN_CHECK_DIR']=str(ROOT/'out/lean')
 stmt='example (h : ℚ) : 1 - (5/4:ℚ)*h + (13/16:ℚ)*h^2 = (27/52:ℚ) + (13/16:ℚ)*(h-10/13)^2 := by ring'
 run=subprocess.run(['python','-X','utf8',str(HOME/'.claude/dreaming/lean_check.py'),'--stmt',stmt,'--timeout','45','--json'],capture_output=True,text=True,encoding='utf-8',env=env)
 (ROOT/'out/LEAN.txt').write_text(run.stdout+run.stderr,encoding='utf-8')
 result={'status':'ATTEMPT_RECORDED_SEE_LEAN_TXT','exit_code':run.returncode,'statement':stmt}
(ROOT/'out/FORMAL_RECEIPT.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
