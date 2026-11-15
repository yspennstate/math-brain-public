"""Independent path/count check and brute-force check of the lattice-disc statistic."""
import json
import math
import pathlib
import subprocess
import numpy as np
from scipy.ndimage import distance_transform_edt
from simulate import ROOT

MASK=(1<<64)-1
def python_walk(n,seed):
    x=y=steps=0
    state=seed
    out=np.zeros((2*n+1,2*n+1),dtype=np.uint32)
    out[n,n]=1
    while True:
        state=(state+0x9e3779b97f4a7c15)&MASK
        z=state
        z=((z^(z>>30))*0xbf58476d1ce4e5b9)&MASK
        z=((z^(z>>27))*0x94d049bb133111eb)&MASK
        d=(z^(z>>31))>>62
        dx,dy=[(1,0),(-1,0),(0,1),(0,-1)][d]
        x+=dx;y+=dy;steps+=1
        if x*x+y*y>n*n:return out,steps,x,y
        out[y+n,x+n]+=1

def main():
    path=ROOT/'data'/'check_counts.bin'
    cases=0
    for n in (1,2,7,19):
        for seed in (0,1,86000123):
            meta=json.loads(subprocess.check_output([str(ROOT/'code'/'srw'),str(n),str(seed),str(path)]))
            out,steps,x,y=python_walk(n,seed)
            actual=np.fromfile(path,dtype=np.uint32).reshape(out.shape)
            assert np.array_equal(actual,out)
            assert (meta['exit_time'],meta['exit_x'],meta['exit_y'])==(steps,x,y)
            cases+=1
    path.unlink()
    rng=np.random.default_rng(86)
    for _ in range(30):
        good=rng.random((9,9))<.75
        padded=np.pad(good,1)
        dist=distance_transform_edt(padded)[1:-1,1:-1]
        # Exhaust all possible centers/radii and enumerate every point of each disc.
        brute=0
        for y,x in np.argwhere(good):
            for r in range(1,10):
                covered=True
                for dy in range(-r,r+1):
                    for dx in range(-r,r+1):
                        if dx*dx+dy*dy<=r*r:
                            yy,xx=y+dy,x+dx
                            if not (0<=yy<9 and 0<=xx<9 and good[yy,xx]):covered=False
                if covered:brute=max(brute,r)
        assert brute==max(0,math.ceil(float(dist.max()))-1)
    result={'independent_C_vs_Python_paths':cases,'brute_force_disc_masks':30,'status':'passed'}
    (ROOT/'data'/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))

if __name__=='__main__':main()
