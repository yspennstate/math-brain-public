import argparse,pathlib,subprocess,time
ROOT=pathlib.Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--domain',choices=['full','eta'],required=True);a=p.parse_args();start=time.monotonic()
for phase in ['raw','bern1','bern2','bern3','bern4']:
    subprocess.run(['python','-X','utf8',str(ROOT/'cubic_invariant_certificate.py'),'--domain',a.domain,'--phase',phase],check=True,cwd=ROOT,timeout=120)
print('Completed invariant',a.domain,'seconds',time.monotonic()-start,flush=True)
