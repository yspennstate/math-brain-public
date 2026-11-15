"""Independent subset/partition audit of C021-C023; no solver imports."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from hashlib import sha256
from datetime import datetime
import itertools,json,time
ROOT=Path(__file__).resolve().parent;start=time.monotonic()

def universe(n):
    edges=list(itertools.combinations(range(n),2));labels=[]
    for mask in range(1<<len(edges)):
        parent=list(range(n))
        def find(x):
            while parent[x]!=x:x=parent[x]
            return x
        bits=mask
        while bits:
            b=bits&-bits;i=b.bit_length()-1;u,v=edges[i];u=find(u);v=find(v);parent[u]=v;bits-=b
        labels.append(tuple(find(i) for i in range(n)))
    counts=[len(set(v)) for v in labels]
    return edges,labels,counts

def classify(n,edges,labels,k,adj):
    e=edges.index((0,1));f=edges.index((1,2) if adj else (2,3));be=1<<e;bf=1<<f;marked=be|bf
    data={};same_map=Counter();diff_maps=[Counter(),Counter()];same_sources=diff_sources=0
    crosses=[edges.index(v) for v in ([(0,2)] if adj else [(0,2),(1,3),(0,3),(1,2)])]
    def joint(a):return k[a^be]==k[a^bf]==k[a] and k[a^be^bf]==k[a]+1
    for a in range(1<<len(edges)):
        if a&marked!=marked:continue
        pe=k[a^be]==k[a]+1;pf=k[a^bf]==k[a]+1;j=joint(a)
        assert k[a^be^bf]-k[a]==int(pe)+int(pf)+int(j)
        both=pe and pf;same=both and (adj or labels[a][0]==labels[a][2])
        data[a]=(pe,pf,both,j,same)
        if not both:continue
        if same:
            same_sources+=1
            candidates=[g for g in crosses if not a&(1<<g) and joint(a|(1<<g)) and k[a|(1<<g)]==k[a]]
            assert len(candidates)==1,(n,a,candidates)
            g=candidates[0];image=a|(1<<g);same_map[image]+=1
            if not adj:
                deleted=image^marked
                candidates_partition=crosses[:2] if labels[deleted][0]==labels[deleted][2] else crosses[2:]
                assert g in candidates_partition
        else:
            diff_sources+=1
            for h,matching in enumerate([crosses[:2],crosses[2:]]):
                extra=sum(1<<g for g in matching);assert not a&extra
                image=a|extra;assert joint(image) and k[image]==k[a]-1
                diff_maps[h][image]+=1
    assert max(same_map.values(),default=0)<=(1 if adj else 2)
    assert all(max(v.values(),default=0)<=1 for v in diff_maps)
    return e,f,data,{'n':n,'pair':'adjacent' if adj else 'disjoint','configurations':1<<len(edges),'both_bridge_same_sources':same_sources,'both_bridge_different_sources':diff_sources,'same_image_max_preimages':max(same_map.values(),default=0),'different_image_max_preimages':[max(v.values(),default=0) for v in diff_maps]},crosses

def weighted(n,edges,k,e,f,data,crosses,q,weights,adj):
    marked=(1<<e)|(1<<f);prod=[F(1)]*(1<<len(edges));W=[F(0)]*4
    T=Pe=Pf=B=J=Bs=Bd=F(0);qp=[q**i for i in range(n+1)]
    for a in range(1<<len(edges)):
        if a:
            bit=a&-a;idx=bit.bit_length()-1
            prod[a]=prod[a^bit]*(1 if bit&marked else weights[idx])
        w=qp[k[a]]*prod[a]
        state=int(bool(a&(1<<e)))+2*int(bool(a&(1<<f)));W[state]+=w
        if state==3:
            pe,pf,b,j,same=data[a];T+=w
            if pe:Pe+=w
            if pf:Pf+=w
            if b:B+=w
            if j:J+=w
            if same:Bs+=w
            elif b:Bd+=w
    s=1-q
    assert W[3]==T and W[1]==T-s*Pf and W[2]==T-s*Pe
    assert W[0]==T-s*(Pe+Pf)+s*s*B-s*J
    R=W[1]*W[2]-W[0]*W[3]
    assert R==s*s*Pe*Pf+s*T*(J-s*B)
    if adj:
        gain=weights[crosses[0]];assert J>=gain*B
        valid=gain>=s;condition=str(gain-s)
    else:
        x,y,u,v=[weights[g] for g in crosses]
        M=max(1/x+1/y,1/u+1/v);P=max(x*y,u*v)
        assert Bs<=M*J and Bd<=q/P*J
        assert B<=(M+q/P)*J
        valid=s*(M+q/P)<=1;condition=str(1-s*(M+q/P))
    ze=weights[e];zf=weights[f];assert ze>0 and zf>0
    Z=W[0]+ze*W[1]+zf*W[2]+ze*zf*W[3]
    covariance=ze*zf*T/Z-(ze*(W[1]+zf*T)/Z)*(zf*(W[2]+ze*T)/Z)
    assert covariance==-ze*zf*R/(Z*Z)
    if valid:assert R>=s*s*Pe*Pf>0 and covariance<0
    return {'n':n,'pair':'adjacent' if adj else 'disjoint','q':str(q),'weights':[str(v) for v in weights],'criterion_holds':valid,'criterion_margin':condition,'covariance':str(covariance),'rayleigh':str(R),'B':str(B),'J':str(J),'global_identity':True}

geometry=[];cases=[]
for n in range(3,7):
    edges,labels,k=universe(n)
    for adj in ([True] if n==3 else [True,False]):
        e,f,data,g,crosses=classify(n,edges,labels,k,adj);geometry.append(g)
        for r in [F(1,4),F(1,2),F(3,4)]:
            q=1-r*r;lam=r*r+r
            cases.append(weighted(n,edges,k,e,f,data,crosses,q,[lam]*len(edges),adj))
        if n in [4,5,6]:
            weights=[F((i*7)%11,3) for i in range(len(edges))];weights[e]=F(2,7);weights[f]=F(13,5)
            if adj:weights[crosses[0]]=F(1,4)
            else:
                for g,v in zip(crosses,[F(1,2),F(3,2),F(2),F(1)]):weights[g]=v
            cases.append(weighted(n,edges,k,e,f,data,crosses,F(3,4),weights,adj))
            if not adj:
                for g in crosses:weights[g]=F(1,20)
                case=weighted(n,edges,k,e,f,data,crosses,F(3,4),weights,adj)
                assert not case['criterion_holds'];cases.append(case)
proofs={}
for i in [21,22,23]:
    p=Path(f'~/brain_workers/w680/proofs/T084-C{i:03}_v1.md');proofs[p.name]=sha256(p.read_bytes()).hexdigest()
out={'at':datetime.now().astimezone().isoformat(),'status':'PASS','method':'All subsets, independent union-find partitions, exact Fraction weights; tests global unconditioned state sums and full map preimage multiplicities','geometry':geometry,'weighted_cases':cases,'proof_sha256':proofs,'seconds':time.monotonic()-start,'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'t084_rc_injections_own.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','geometry_families':len(geometry),'weighted_cases':len(cases),'largest_graph_edges':15,'largest_configuration_family':32768,'seconds':out['seconds'],'proof_sha256':proofs}))
