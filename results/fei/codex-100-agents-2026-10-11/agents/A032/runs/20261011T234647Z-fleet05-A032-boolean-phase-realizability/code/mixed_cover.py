import json,time,math
from collections import defaultdict,Counter
from pathlib import Path
from cover_search import prime_factors
ROOT=Path(__file__).resolve().parents[1]

def search(resume=False):
    started=time.monotonic();raw=json.loads((ROOT/'out'/'mixed_slices_m4.json').read_text());rows=raw['records'];groups=defaultdict(list)
    for i,row in enumerate(rows):
        signature=Counter({2:10*sum(v*c for v,c in row['histogram'])})
        for v,c in row['histogram']:
            for p,e in prime_factors(v).items():signature[p]-=v*c*e
        row['signature']=tuple(sorted((p,v) for p,v in signature.items() if v));row['entropy_discovery']=sum(v*math.log2(p) for p,v in row['signature'])
        groups[row['mixed_mask']].append(i)
    objectives={};best=None;group_reports=[];matches=0
    if resume:
        checkpoint=json.loads((ROOT/'out'/'mixed_cover_results.json').read_text())
        group_reports=checkpoint['groups_completed'];best=checkpoint['best'];matches=checkpoint['mixed_complementary_pair_matches']
        for row in checkpoint['objective_signatures']:
            key=(tuple(map(tuple,row['log_signature'])),row['influence_numerator'])
            objectives[key]={k:v for k,v in row.items() if k not in('log_signature','influence_numerator')}
    completed_masks={g['mixed_mask'] for g in group_reports}
    def save_progress(status):
        results=[{'log_signature':sig,'influence_numerator':inf,**v} for (sig,inf),v in sorted(objectives.items())]
        out={'status':status,'groups_completed':group_reports,'mixed_complementary_pair_matches':matches,'objective_signatures':results,'best':best,'seconds':time.monotonic()-started,'excluded_masks':{'0':'pure class separately certified12/5','65535':'all-mixed analytic H<=2I'}}
        (ROOT/'out'/'mixed_cover_results.json').write_text(json.dumps(out,indent=2));return out
    for M,indices in sorted(groups.items()):
        if M in(0,65535) or M in completed_masks:continue
        empty=65535^M;pairtable={};pairs=0
        for ia,a in enumerate(indices):
            A=rows[a]
            for b in indices[ia:]:
                B=rows[b]
                if A['pure_mask']&B['pure_mask']:continue
                pairs+=1
                U=A['pure_mask']|B['pure_mask'];R=A['mixed_negative_mask']^B['mixed_negative_mask']
                sig=Counter(dict(A['signature']));sig.update(dict(B['signature']));sig=tuple(sorted((p,v) for p,v in sig.items() if v))
                norms=tuple(sorted((A['norm_integer'],B['norm_integer']),reverse=True))
                key=(U,R,norms,sig);influence=A['influence_numerator']+B['influence_numerator']
                old=pairtable.get(key)
                if old is None or influence<old[0]:pairtable[key]=(influence,(a,b))
                if len(pairtable)>500000:
                    save_progress('PARTIAL_PAIR_TABLE_CAP');print('PAIR_TABLE_CAP');return
            if time.monotonic()-started>180:
                save_progress('PARTIAL_RUNTIME_CAP');print('RUNTIME_CAP');return
        lookup=defaultdict(list)
        for (U,R,norms,sig),(influence,pair) in pairtable.items():lookup[(U,R)].append((norms,sig,influence,pair))
        groupmatches=0
        for (U,R,norms,sig),(influence,pair) in pairtable.items():
            complement=empty^U
            for Q in(R,R^M):
                for norms2,sig2,influence2,pair2 in lookup.get((complement,Q),[]):
                    matches+=1;groupmatches+=1
                    masses=sorted(norms+norms2,reverse=True)
                    assert sum(masses)==64
                    totalI=influence+influence2+16*(masses[1]+masses[2]+2*masses[3])
                    totalH=Counter(dict(sig));totalH.update(dict(sig2));totalH=tuple(sorted((p,v) for p,v in totalH.items() if v))
                    key=(totalH,totalI)
                    if key not in objectives:objectives[key]={'row_indices':list(pair+pair2),'mixed_mask':M,'mass_norms':masses,'pair_matches':0}
                    objectives[key]['pair_matches']+=1
                    ratio=sum(v*math.log2(p) for p,v in totalH)/totalI
                    if best is None or ratio>best['ratio_discovery']:
                        best={'log_signature':totalH,'influence_numerator':totalI,'row_indices':list(pair+pair2),'mixed_mask':M,'mass_norms':masses,'ratio_discovery':ratio,'slices_h':[rows[i]['truth_h'] for i in pair+pair2]}
            if matches%10000==0 and time.monotonic()-started>180:
                save_progress('PARTIAL_RUNTIME_CAP');print('RUNTIME_CAP');return
        group_reports.append({'mixed_mask':M,'rows':len(indices),'compatible_unordered_pairs':pairs,'objective_preserving_pair_records':len(pairtable),'pair_matches':groupmatches})
        save_progress('IN_PROGRESS')
    out=save_progress('COMPLETE')
    print(json.dumps({k:v for k,v in out.items() if k not in('objective_signatures','groups_completed')}),flush=True)
    print(json.dumps({'groups_completed':len(group_reports),'objective_signatures':len(objectives)}))
if __name__=='__main__':
    import sys
    search('--resume' in sys.argv)
