"""NUMERICAL discovery of split-scale, finer high-ratio cells; exact acceptance."""
import json,time
from pathlib import Path
from fractions import Fraction as F
import cubic_discovery
from fast_conic import solve
from moment_polytope import vertices
cubic_discovery.solve=solve

def main():
    vs=vertices(True);bank=json.load(open('cubic_cells.json'));old=json.load(open('moment_cells.json'));out=[];attempts=[]
    strips=[(F(3,20),F(4,25))]+[(F(j,100),F(j+1,100))for j in range(90,100)]
    for lo,hi in strips:
        parents=[(i,c)for i,c in enumerate(bank)if F(c['rlo'])<=lo and hi<=F(c['rhi'])]
        if parents:i,parent=max(parents,key=lambda ic:F(ic[1]['ahi']));name='cubic_cells.json'
        else:i,parent=max(((i,c)for i,c in enumerate(old)if F(c['rlo'])<=lo and hi<=F(c['rhi'])),key=lambda ic:F(ic[1]['ahi']));name='moment_cells.json'
        base=F(parent['ahi']);alo=base-F(1,1000);low,high=int(base*10000),int(base*10000)+301;best=None
        while low+1<high:
            mid=(low+high)//2;rec=cubic_discovery.discover(vs,lo,hi,F(mid,10000),alo=alo)
            attempts.append(dict(rlo=str(lo),rhi=str(hi),alo=str(alo),ahi=str(F(mid,10000)),accepted=rec is not None))
            if rec:low,best=mid,rec
            else:high=mid
        if best:
            best['base_cover']=dict(file=name,index=i);out.append(best)
            msg=f"PROVED: split-scale sextic cell r=[{lo},{hi}], a=[{alo},{best['ahi']}]; parent {name}:{i}."
        else:msg=f'OPEN: no split-scale extension found for r=[{lo},{hi}].'
        print(msg,flush=True)
        Path('stacked_cells.json').write_text(json.dumps(out,indent=2)+'\n');Path('stacked_attempts.json').write_text(json.dumps(dict(label='NUMERICAL',attempts=attempts),indent=2)+'\n')
        with open('LOG.md','a')as f:f.write('\n'+msg+'\n')
if __name__=='__main__':main()
