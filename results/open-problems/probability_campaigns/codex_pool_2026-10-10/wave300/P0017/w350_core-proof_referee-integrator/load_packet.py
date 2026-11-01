from pathlib import Path
import json
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
BASE = Path('~')
OUT = ROOT/'context'
OUT.mkdir(exist_ok=True)

def run(label, args, timeout=35, lines=90):
    print('RUN', label, flush=True)
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONIOENCODING='utf-8')
    try:
        p = subprocess.run(args, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=timeout, env=env)
        (OUT/(label+'.txt')).write_text(p.stdout+'\nSTDERR:\n'+p.stderr, encoding='utf-8')
        print('EXIT', p.returncode, '\n'.join(p.stdout.splitlines()[:lines]), p.stderr[:400], flush=True)
    except subprocess.TimeoutExpired as e:
        output = e.stdout or b''
        if isinstance(output, bytes): output = output.decode('utf-8','replace')
        (OUT/(label+'.txt')).write_text('TIMEOUT\n'+output, encoding='utf-8')
        print('TIMEOUT', label, flush=True)

if sys.argv[1:] == ['recall']:
    run('recall_P0017', [sys.executable,'-X','utf8',str(BASE/'.claude/dreaming/brain.py'),'recall','P0017 KLS log-concave proof audit mistakes'], timeout=60,lines=60)
    sys.exit()

intake = BASE/'<private-repo>/06_math_research/probability_1000_intake_claude_20260907'
pattern = ('P0017','Dimension-free log-concave','dimension-free-log-concave')
matches=[]
def visit(x, trail):
    if isinstance(x,dict):
        if any(any(k in str(v) for k in pattern) for v in x.values() if not isinstance(v,(dict,list))):
            matches.append({'path':trail,'record':x})
            return
        for k,v in x.items(): visit(v,trail+'/'+k)
    elif isinstance(x,list):
        for i,v in enumerate(x): visit(v,trail+'/'+str(i))

for name in ['brain_bundle_C006p01.json','brain_bundle_C006a04.json','brain_retrieval_C006_after.json']:
    p=intake/name
    if p.exists(): visit(json.loads(p.read_text(encoding='utf-8-sig')),str(p))
(OUT/'intake_records.json').write_text(json.dumps(matches,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
for match in matches: print(json.dumps(match,ensure_ascii=False),flush=True)

for slug in ['perceptron_proof_open_gaps_fleet_2026_07_12','method_grow_mathbrain_safely_2026_08_12','referee_pass_before_shipping_proofs_2026_07_14']:
    p=BASE/'.claude/projects/<project>/memory'/ (slug+'.md')
    if p.exists():
        print('MEMORY',slug,flush=True)
        print(p.read_text(encoding='utf-8-sig')[:7500],flush=True)
    else: print('MEMORY MISSING',slug,flush=True)

research=BASE/'<private-repo>/06_math_research'
for d in ['probability_1000_attempts_H_20260912','probability_1000_attempts_I_20260914','prob1000_lean_20260908']:
    run(d+'_gaps',['rg','-n','-i','--max-columns','600','-m','3','-g','*.md','-g','*.json','-g','*.jsonl','-g','*.lean',r'P0017\b',str(research/d)],lines=35)

run('brain_recall_code',['rg','-n','-A','80',r'^def recall\(',str(BASE/'.claude/dreaming/brain.py')],lines=85)
run('team_read_initial',[sys.executable,'-X','utf8',str(BASE/'<private-repo>/12_cognitive_architecture/agent_mesh/team_comm.py'),'read','--as','w350','--max','8'],timeout=30,lines=60)
