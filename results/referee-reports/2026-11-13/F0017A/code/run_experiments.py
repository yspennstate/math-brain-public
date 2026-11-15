"""Sequential, resumable experiment runner. Every completed sample is flushed."""
import json
import os
from pathlib import Path
import subprocess
import time

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data';DATA.mkdir(exist_ok=True)
EXE=ROOT/'code/enumerate'
PLAN={7:1000,8:1000,9:1000,10:1000,11:1000,12:1000,13:1000,14:1000,
      15:1000,16:1000,17:500,18:500,19:300,20:300,21:150,22:150,23:100,24:100}

def main():
    assert os.getpriority(os.PRIO_PROCESS,0)>=10
    timings=[]
    for n in range(1,7):
        path=DATA/f'exhaustive_{n}.json'
        if path.exists():continue
        st=time.time()
        r=subprocess.run([str(EXE),'exhaustive',str(n)],capture_output=True,text=True,check=True)
        obj=json.loads(r.stdout)
        path.write_text(json.dumps(obj,indent=2)+'\n')
        timings.append(dict(mode='exhaustive',n=n,seconds=time.time()-st,diagnostics=r.stderr))
        print(f'exhaustive n={n} saved',flush=True)
    for n,count in PLAN.items():
        path=DATA/f'monte_{n}.jsonl'
        # Reproducibility: an interrupted dimension is re-run deterministically.
        if path.exists() and len(path.read_text().splitlines())==count:continue
        st=time.time();seed=170017000+n
        with path.open('w') as out:
            p=subprocess.Popen([str(EXE),'monte',str(n),str(count),str(seed)],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
            for i,line in enumerate(p.stdout):
                obj=json.loads(line);assert obj['visited']==1<<n
                out.write(line);out.flush()
                if (i+1)%max(1,count//10)==0:print(f'n={n} {i+1}/{count}, elapsed {time.time()-st:.1f}s',flush=True)
            err=p.stderr.read();assert p.wait()==0,err
        timings.append(dict(mode='monte',n=n,count=count,seed=seed,seconds=time.time()-st,diagnostics=err))
        with (DATA/'timings.jsonl').open('a') as f:
            for item in timings:f.write(json.dumps(item)+'\n')
        timings=[]
    print('experiment plan complete',flush=True)

if __name__=='__main__':main()
