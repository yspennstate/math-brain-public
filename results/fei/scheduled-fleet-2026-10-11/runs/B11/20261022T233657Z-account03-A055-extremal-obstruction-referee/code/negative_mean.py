from activation import fw,H,AH,add,restrict
from fractions import Fraction as Q
from pathlib import Path
import json,time
start=time.perf_counter();R=Path(__file__).resolve().parents[1];C=[0,1,3,12,6,24,48,32];seed=[1,-1,-1,-1]
pv=[-1 if ((x&63)&C[x>>6]).bit_count()%2 else 1 for x in range(512)]
g=[pv[x&511]*seed[x>>9] for x in range(2048)];wg=fw(g);mu=Q(wg[0],2048);HG=H(wg,2048);f=g+[1]*6144;wf=fw(f);HF=H(wf,8192)
assert mu==Q(-1,16);assert HF==AH(HG,mu,2)
IF=Q(sum(f[x]!=f[x^(1<<j)] for x in range(8192) for j in range(13)),8192);assert IF==Q(49,32)
for z in range(2):
 ch=restrict(f,[2],z);wc=fw(ch);assert H(wc,4096)==HF;assert Q(sum(s.bit_count()*w*w for s,w in enumerate(wc)),4096**2)==IF-Q(1,16)
out={'status':'PASS','assertions':7,'negative_G_mean':'-1/16','I':'49/32','actual_root_entries':8192,'actual_singleton_children':2,'elapsed_seconds':time.perf_counter()-start}
(R/'out/NEGATIVE_MEAN.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
