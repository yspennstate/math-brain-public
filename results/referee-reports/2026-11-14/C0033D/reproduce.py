"""Sequential, checkpoint-preserving reproduction for the Mac workspace."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[key]='1'
import argparse,subprocess,sys,json,platform,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def run(script,args=(),log=None):
    print(script,*args,flush=True)
    with open(ROOT/'data'/(log or (Path(script).stem+'_run.log')),'w') as out:
        subprocess.run([sys.executable,script,*args],stdout=out,stderr=subprocess.STDOUT,check=True)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--search',action='store_true');args=ap.parse_args()
    os.chdir(ROOT);(ROOT/'data').mkdir(exist_ok=True)
    subprocess.run(['clang++','-O3','-std=c++17','-dynamiclib','dpp.cpp','-o','libdpp.dylib'],check=True)
    if args.search:
        run('search.py')
        run('bnb.py',['--max-nodes','10000','--file','data/bnb_local_improved.json'],'bnb_local_improved_run.log')
        run('bnb.py',['--interior','1/10','--max-nodes','10000','--file','data/bnb_interior.json'],'bnb_interior_run.log')
        run('bnb.py',['--interior','1/10','--full-hessian','--max-nodes','20000','--file','data/bnb_interior_full.json'],'bnb_interior_full_run.log')
    for script in ('certify.py','boundary.py','family.py','audit.py'):run(script)
    run('bnb.py',['--small-box','--max-nodes','10000','--file','data/bnb_small.json'],'bnb_small_run.log')
    run('cover_audit.py')
    subprocess.run([sys.executable,'make_tables.py'],check=True)
    import numpy,scipy,sympy,mpmath
    inherited={}
    for name in ('dpp.py','dpp.cpp'):
        local=(ROOT/name).read_bytes()
        for prior in ('C0033A','C0033B','C0033C'):assert local==(ROOT.parent/prior/name).read_bytes()
        inherited[name]=hashlib.sha256(local).hexdigest()
    files={}
    for p in sorted(ROOT.rglob('*')):
        if p.is_file() and p.suffix in ('.py','.cpp','.json','.npz','.md') and '__pycache__' not in str(p) and p.name!='artifact_manifest.json':
            files[str(p.relative_to(ROOT))]=hashlib.sha256(p.read_bytes()).hexdigest()
    out=dict(python=platform.python_version(),platform=platform.platform(),packages={m.__name__:m.__version__ for m in (numpy,scipy,sympy,mpmath)},
             inherited_verbatim_sha256=inherited,numerical_threads=1,worker_pools=0,priority=os.getpriority(os.PRIO_PROCESS,0),sha256=files)
    (ROOT/'artifact_manifest.json').write_text(json.dumps(out,indent=2)+'\n')
    print('Point certificates, local cover, partition audits and identities passed.',flush=True)
if __name__=='__main__':main()
