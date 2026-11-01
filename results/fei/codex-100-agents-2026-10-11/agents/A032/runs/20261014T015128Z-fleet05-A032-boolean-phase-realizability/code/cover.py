import json,time,math
from collections import defaultdict
from pilot import ROOT,load
def main():
    start=time.monotonic();rows=load();groups=defaultdict(dict)
    for i,r in enumerate(rows):
        key=(r['pure_mask'],r['mixed_negative_mask'],r['norm_integer'],r['N'])
        groups[r['mixed_mask']].setdefault(key,i)
    objectives={};reports=[];matches=0
    for M,unique in sorted(groups.items()):
        if M in (0,65535):continue # pure covers handled separately below
        ids=list(unique.values());pairs={};empty=65535^M
        for pos,a in enumerate(ids):
            A=rows[a]
            for b in ids[pos:]:
                B=rows[b]
                if A['pure_mask']&B['pure_mask']:continue
                norms=tuple(sorted((A['norm_integer'],B['norm_integer']),reverse=True))
                q=A['norm_integer']*A['N']+B['norm_integer']*B['N']
                key=(A['pure_mask']|B['pure_mask'],A['mixed_negative_mask']^B['mixed_negative_mask'],norms,q)
                pairs.setdefault(key,(a,b))
        lookup=defaultdict(list)
        for (U,R,ks,q),ab in pairs.items():lookup[U,R].append((ks,q,ab))
        for (U,R,ks,q),ab in pairs.items():
            for phase in (R,R^M):
                for ls,t,cd in lookup.get((empty^U,phase),[]):
                    masses=tuple(sorted(ks+ls,reverse=True));assert sum(masses)==64
                    objectives.setdefault((masses,q+t),{'row_indices':list(ab+cd),'mixed_mask':M});matches+=1
        reports.append({'mixed_mask':M,'compressed_rows':len(ids),'pair_records':len(pairs)})
        assert time.monotonic()-start<240,'FROZEN_RUNTIME_LIMIT'
    assert all(r['N']==0 for r in rows if r['mixed_mask']==65535)
    pure={};byfirst=defaultdict(list);bywhole=defaultdict(list)
    for i,r in enumerate(rows):
        if r['mixed_mask']==0:pure.setdefault((r['pure_mask'],r['N']),i)
    for (mask,n),i in pure.items():
        bywhole[mask].append(i)
        for x in range(16):
            if mask>>x&1:byfirst[x].append(i)
    pure_count=0
    def accept(chosen):
        nonlocal pure_count
        pure_count+=1
        masses=tuple(sorted([rows[i]['norm_integer'] for i in chosen]+[0]*(4-len(chosen)),reverse=True))
        q=sum(rows[i]['norm_integer']*rows[i]['N'] for i in chosen)
        objectives.setdefault((masses,q),{'row_indices':chosen.copy(),'mixed_mask':0})
    def visit(covered,chosen):
        if covered==65535:accept(chosen);return
        remain=65535^covered
        if len(chosen)==3:
            for i in bywhole.get(remain,[]):accept(chosen+[i])
            return
        x=(remain&-remain).bit_length()-1
        for i in byfirst[x]:
            mask=rows[i]['pure_mask']
            if not mask&covered:visit(covered|mask,chosen+[i])
    visit(0,[])
    results=[]
    for (ks,q),w in sorted(objectives.items()):
        address=ks[1]+ks[2]+2*ks[3]
        H=6-sum(k*math.log2(k) for k in ks if k)/64
        results.append({'masses':ks,'Q_numerator':q,'address_numerator':address,'ratio_discovery':q/(64*H+address) if H+address else 0,**w})
    best=max(results,key=lambda r:r['ratio_discovery'])
    out={'status':'COMPLETE','rows':len(rows),'groups':reports,'pure_compressed_covers':pure_count,'objective_signatures':results,'best':best,'diagnostic_pair_matches':matches,'seconds':time.monotonic()-start}
    (ROOT/'out/heavy_cover.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items() if k not in ('groups','objective_signatures')}))
if __name__=='__main__':main()
