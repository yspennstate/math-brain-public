"""Independent direct-Bayes table builder and full exact mass-law replay.
No author implementation is imported. Small oracle integrates BOTH orientations.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations,product
import hashlib,json,os,subprocess,time,math
OUT=Path(__file__).resolve().parent
FLAGS=subprocess.CREATE_NO_WINDOW|subprocess.BELOW_NORMAL_PRIORITY_CLASS
def save(name,o):(OUT/name).write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def event(phase,**kw):
    o=dict(phase=phase,**kw);save('degree6_progress.json',o);print(json.dumps(o),flush=True)
def build():
    vc=Path('C:/Program Files (x86)/Microsoft Visual Studio/18/BuildTools/VC/Tools/MSVC/14.50.35717')
    sdk=Path('C:/Program Files (x86)/Windows Kits/10');v='10.0.26100.0';cc=vc/'bin/Hostx64/x64/cl.exe'
    env=os.environ.copy();env['PATH']=str(cc.parent)+os.pathsep+env.get('PATH','')
    env['INCLUDE']=';'.join(map(str,[vc/'include']+[sdk/'Include'/v/x for x in ['ucrt','shared','um','winrt','cppwinrt']]))
    env['LIB']=';'.join(map(str,[vc/'lib/x64',sdk/'Lib'/v/'ucrt/x64',sdk/'Lib'/v/'um/x64']))
    args=[str(cc),'/nologo','/O2','/EHsc','/std:c++17','/Fo:'+str(OUT/'check_degree6_exact.obj'),'/Fe:'+str(OUT/'check_degree6_exact.exe'),str(OUT/'check_degree6_exact.cpp')]
    with (OUT/'degree6_build.log').open('w',encoding='utf-8') as f:r=subprocess.run(args,cwd=OUT,env=env,stdout=f,stderr=subprocess.STDOUT,creationflags=FLAGS,timeout=180)
    assert r.returncode==0,'build failed'
    save('degree6_build_receipt.json',dict(source_sha256=sha(OUT/'check_degree6_exact.cpp'),exe_sha256=sha(OUT/'check_degree6_exact.exe'),args=args))
def run(tag,N,A,B,bits,depth,degree,dump):
    start=time.monotonic();prefix=OUT/tag
    args=[str(OUT/'check_degree6_exact.exe'),*map(str,[N,A,B,bits,depth,degree]),str(prefix),str(int(dump))]
    with (OUT/(tag+'.jsonl')).open('w',encoding='utf-8') as f:r=subprocess.run(args,cwd=OUT,stdout=f,stderr=subprocess.STDOUT,creationflags=FLAGS,timeout=7200)
    assert r.returncode==0,tag+' native failed'
    events=[json.loads(x) for x in (OUT/(tag+'.jsonl')).read_text(encoding='utf-8').splitlines()];assert events[-1]['complete']
    event(tag+'-native-complete',seconds=time.monotonic()-start)
    return events
def ks(N):return [(a,b,N-a-b) for a in range(N//3+1) for b in range(a,(N-a)//2+1)]
def bary(q,N):
    y=[N*x for x in q];lo=[x.numerator//x.denominator for x in y];r=[x-a for x,a in zip(y,lo)];s=sum(r);out={}
    def add(k,w):
        if w:out[tuple(sorted(k))]=out.get(tuple(sorted(k)),F(0))+w
    if s==0:add(lo,F(1))
    elif s==1:
        for i in range(3):add([lo[j]+int(i==j) for j in range(3)],r[i])
    elif s==2:
        for i in range(3):add([lo[j]+int(i!=j) for j in range(3)],1-r[i])
    else:raise AssertionError(s)
    assert sum(out.values())==1
    return out
def oracle(N,A,B):
    reps=ks(N);idx={k:i for i,k in enumerate(reps)};rows={};nulls=0
    for i,k in enumerate(reps):
        for j,h in enumerate(reps):
            left=set(permutations(k));right=set(permutations(h));o={}
            for p,r in product(left,right):
                dot=sum(F(x*y,N*N) for x,y in zip(p,r))
                if not dot:nulls+=1;continue
                posterior=[F(x*y,N*N)/dot for x,y in zip(p,r)]
                weight=3*dot/len(left)/len(right)
                for v,w in bary(posterior,N).items():o[idx[v]]=o.get(idx[v],F(0))+weight*w
            assert sum(o.values())==1;rows[i,j]=o
    edges=[]
    for k in reps:
        q=[F(1,3)+F(A,B)*(F(x,N)-F(1,3)) for x in k]
        edges.append({idx[v]:w for v,w in bary(q,N).items()})
    return rows,edges,nulls
def readrows(path):
    out={}
    for line in path.read_text(encoding='utf-8').splitlines():
        parts=line.split();key=tuple(map(int,parts[:2]));out[key]={int(x.split(':')[0]):int(x.split(':')[1]) for x in parts[2:]}
    return out
def rounded(raw,S):
    out=[int(x*S) for x in raw];assert all(x>=0 for x in out);out[0]+=S-sum(out);assert sum(out)==S;return out
def tiny():
    controls=[]
    for A,B in [(0,1),(1,1),(89,218),(53,237)]:
        rows,edges,nulls=oracle(6,A,B);n=len(ks(6));S=1<<12
        for d in [3,5,6,21]:
            tag=f'degree6_tiny_{A}_{B}_{d}';run(tag,6,A,B,12,4,d,True)
            native=readrows(OUT/(tag+'.rows.txt'));assert len(native)==n*n
            for key,row in native.items():assert {i:F(c,108*36) for i,c in row.items()}==rows[key]
            edge_lines=(OUT/(tag+'.edges.txt')).read_text(encoding='utf-8').splitlines()
            for line in edge_lines:
                p=line.split();i=int(p[0]);assert {int(x.split(':')[0]):F(int(x.split(':')[1]),3*B) for x in p[1:]}==edges[i]
            observed=[list(map(int,x.split())) for x in (OUT/(tag+'.masses.txt')).read_text(encoding='utf-8').splitlines()]
            def fuse(a,b):
                raw=[F(0)]*n
                for i,j in product(range(n),repeat=2):
                    for v,w in rows[i,j].items():raw[v]+=F(a[i]*b[j],S*S)*w
                return rounded(raw,S)
            m=[S]+[0]*(n-1)
            for depth in range(5):
                assert observed[depth]==[depth]+m
                raw=[sum(F(m[i],S)*edges[i].get(j,0) for i in range(n)) for j in range(n)];power=rounded(raw,S);acc=None;remaining=d
                while remaining:
                    if remaining&1:acc=power if acc is None else fuse(acc,power)
                    remaining>>=1
                    if remaining:power=fuse(power,power)
                m=acc
            controls.append(dict(A=A,B=B,degree=d,rows=n*n,all_mass_depths=5,both_orientation_nulls=nulls))
    save('degree6_small_controls.json',dict(status='PASS',controls=controls,oracle='Fraction direct Bayes, BOTH left/right orientation averages, independent rounding'))
    event('tiny-PASS',controls=len(controls))
def main():
    build();tiny()
    events=run('degree6_full',96,89,218,32,26,6,False)
    depths=[x for x in events if x.get('phase')=='depth'];assert len(depths)==27
    last=depths[-1];actual=F(last['signal_numerator'],last['signal_denominator'])
    assert actual==F(942948951491,19791209299968)
    masses=[list(map(int,x.split())) for x in (OUT/'degree6_full.masses.txt').read_text(encoding='utf-8').splitlines()]
    assert len(masses)==27 and all(len(r)==818 and sum(r[1:])==1<<32 for r in masses)
    save('degree6_exact_replay_checks.json',dict(status='PASS independent native replay; author mass comparison and local proof pending',final_signal=str(actual),radius='217/4500',gap=str(F(217,4500)-actual),all_depths=27,orbits=817,ordered_fusion_rows=817**2,source_sha256=sha(OUT/'check_degree6_exact.cpp'),driver_sha256=sha(Path(__file__)),masses_sha256=sha(OUT/'degree6_full.masses.txt'),events=events))
    event('full-independent-replay-PASS',signal=str(actual))
if __name__=='__main__':main()
