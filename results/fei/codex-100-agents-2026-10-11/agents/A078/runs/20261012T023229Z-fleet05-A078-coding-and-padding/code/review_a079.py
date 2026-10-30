from pathlib import Path
from fractions import Fraction as F
import json,time
from check_overlap import fwht
ROOT=Path(__file__).resolve().parents[1]
count=0
def ck(p):
    global count
    count+=1
    assert p
def direct(t):return [sum(t[x]*(-1 if (s&x).bit_count()%2 else 1) for x in range(len(t))) for s in range(len(t))]
def main():
    start=time.perf_counter();rows=[]
    for k in [1,2]:
        seedN=1<<k
        for mask in range(1<<seedN):
            seed=[1-2*((mask>>x)&1) for x in range(seedN)];c=direct(seed)
            p=[F(z*z,seedN*seedN) for z in c]
            Ig=sum(p[z]*z.bit_count() for z in range(seedN))
            for m in [k+1,k+2]:
                B=1<<m;N=k+2*m;size=1<<N
                tab=[]
                for z in range(size):
                    x=z&(seedN-1);a=(z>>k)&(B-1);b=z>>(k+m)
                    tab.append(seed[x]*(-1 if ((a&b).bit_count()%2)^(b==x) else 1))
                w=fwht(tab);px=[F(0)]*seedN
                for label in range(size):
                    v=label&(seedN-1);s=(label>>k)&(B-1);t=label>>(k+m)
                    phase=seed[:]
                    if s<seedN:phase[s]*=-1
                    expected=direct(phase)[v]*B*(-1 if (s&t).bit_count()%2 else 1)
                    ck(w[label]==expected)
                    px[v]+=F(w[label]*w[label],size*size)
                eps=F(4,B)
                ck(px==[(1-eps)*p[v]+eps/seedN for v in range(seedN)])
                Ix=sum(F(sum(tab[x]!=tab[x^(1<<i)] for x in range(size)),size) for i in range(k))
                Iy=sum(F(sum(tab[x]!=tab[x^(1<<i)] for x in range(size)),size) for i in range(k,N))
                ck(Ix==Ig+F(2,B)*(k-2*Ig));ck(Iy==m)
                branches=[]
                for x in range(seedN):
                    br=[tab[x|(y<<k)] for y in range(B*B)];bw=fwht(br)
                    ck(all(z*z==B*B for z in bw));branches.append(br)
                for i in range(seedN):
                    for j in range(i):ck(branches[i]!=branches[j] and branches[i]!=[-z for z in branches[j]])
                rows.append({'k':k,'m':m,'seed_mask':mask,'I_X':str(Ix),'I_Y':str(Iy),'epsilon':str(eps)})
    out={'status':'PASS','reviewed':'A079 bent-phase and distinct-tag ledger','verdict':'ACCEPT_AT_STATED_SCOPE','cases':len(rows),'assertions':count,'seconds':time.perf_counter()-start,'rows':rows,'independence':'Own full truth tables/FWHT, own direct row character sums and edge influence; source code not executed or imported'}
    (ROOT/'out'/'review_a079.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
if __name__=='__main__':main()
