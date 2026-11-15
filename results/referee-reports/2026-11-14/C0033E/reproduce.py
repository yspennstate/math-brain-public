"""Sequential reproduction. Add --search to regenerate all finite searches."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import argparse,subprocess,sys,json,hashlib,platform
from pathlib import Path

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--search',action='store_true');args=ap.parse_args()
    root=Path(__file__).resolve().parent;os.chdir(root)
    if not (root/'libdpp.dylib').exists():subprocess.run(['clang++','-O3','-std=c++17','-dynamiclib','dpp.cpp','-o','libdpp.dylib'],check=True)
    scripts=['exact_cyclic.py']
    if args.search:scripts+=['search_mp.py','optimize_collar.py','refine_scaled.py']
    scripts+=['audit_inputs.py','mixed_limit.py','verify_results.py']
    for script in scripts:
        with (root/'data'/('reproduce_'+script[:-3]+'.txt')).open('w') as f:
            subprocess.run([sys.executable,script],stdout=f,stderr=subprocess.STDOUT,check=True)
    subprocess.run([sys.executable,'bnb.py','--small-box','--file','data/bnb_small.json','--max-nodes','100'],check=True)
    subprocess.run([sys.executable,'make_tables.py'],check=True)
    import numpy,scipy,sympy,mpmath
    manifest={'python':sys.version,'platform':platform.platform(),'priority':os.getpriority(os.PRIO_PROCESS,0),'packages':{m.__name__:m.__version__ for m in (numpy,scipy,sympy,mpmath)},'files':{}}
    for p in sorted(root.rglob('*')):
        if p.is_file() and (p.suffix in ('.py','.cpp','.md','.json') or p.name=='libdpp.dylib') and '__pycache__' not in str(p) and p.name not in ('codex.log','artifact_manifest.json'):
            manifest['files'][str(p.relative_to(root))]=hashlib.sha256(p.read_bytes()).hexdigest()
    (root/'artifact_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
if __name__=='__main__':main()
