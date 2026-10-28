from pathlib import Path
import sys,subprocess,json,os,hashlib
ROOT=Path(__file__).resolve().parents[1]
admit=subprocess.run([sys.executable,'-X','utf8',r'tools\memok.py'],capture_output=True,text=True,encoding='utf-8',timeout=55)
(ROOT/'out/LEAN_MEMOK.txt').write_text(admit.stdout+admit.stderr,encoding='utf-8')
result={'admission_returncode':admit.returncode,'admission':admit.stdout.strip(),'scope':'Natural-number algebraic conversion only; not the full analytic entropy theorem'}
if admit.returncode==0:
    env=dict(os.environ);env['LEAN_CHECK_DIR']=str(ROOT/'out/lean');env['TEMP']=env['TMP']=str(ROOT/'out/temp')
    Path(env['TEMP']).mkdir(exist_ok=True)
    source=ROOT/'code/PriceConversion.lean'
    cmd=[sys.executable,'-X','utf8',r'lean_check.py','--file',str(source),'--core','--target','a030_price_conversion','--reviewed-sha256',hashlib.sha256(source.read_bytes()).hexdigest(),'--timeout','55','--json']
    with (ROOT/'out/LEAN.json').open('w',encoding='utf-8',newline='') as out:
        proc=subprocess.run(cmd,stdout=out,stderr=subprocess.STDOUT,env=env,timeout=75)
    result['returncode']=proc.returncode
    try:
        receipt=json.loads((ROOT/'out/LEAN.json').read_text(encoding='utf-8'));result['result']=receipt.get('result');result['receipt_directory']=receipt.get('receipt_directory')
    except json.JSONDecodeError:result['setup_output']=(ROOT/'out/LEAN.json').read_text(encoding='utf-8')[:1800]
(ROOT/'out/LEAN_RUN.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
