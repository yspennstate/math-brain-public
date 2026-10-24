import json, os, pathlib, subprocess, time
w = pathlib.Path('~/brain_workers/w538')
query = 'P0309 Riesz crystalline Gibbs phases missing bridge proof mistakes'
started = time.monotonic()
env = os.environ.copy()
env['PYTHONDONTWRITEBYTECODE'] = '1'
env['BRAIN_RECALL_PUBLISH'] = '0'
try:
    r = subprocess.run(['python','-X','utf8','~/.claude/dreaming/brain.py','recall',query,'-n','3'],capture_output=True,text=True,encoding='utf-8',timeout=60,env=env)
    result = {'query':query,'seconds':time.monotonic()-started,'returncode':r.returncode,'stdout':r.stdout,'stderr':r.stderr,'timeout_seconds':60}
except subprocess.TimeoutExpired as e:
    result = {'query':query,'seconds':time.monotonic()-started,'timeout':True,'timeout_seconds':60,'stdout':(e.stdout or b'').decode('utf-8',errors='replace') if isinstance(e.stdout,bytes) else (e.stdout or '')}
(w/'brain_recall_receipt.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False)[:14000])
