from pathlib import Path
from fractions import Fraction as F
import json,time,sys
import kernel as c
import compressed as z
ROOT=Path(__file__).resolve().parents[1]

def direct_truth(k,l,shared,r):
    core_groups=['core']*(k+l)+['selector'] if shared else ['core']*k+['selector']+['core']*l+['selector']
    labels,controls,groups=z.labels_for(core_groups,r)
    n=len(labels)+r;table=bytearray()
    for v in range(1<<n):
        if any((v>>i)&1 for i in controls):table.append(0);continue
        if shared:
            first=labels[:k];second=labels[k:k+l];s1=s2=labels[-1]
        else:
            first=labels[:k];s1=labels[k];second=labels[k+1:k+1+l];s2=labels[-1]
        bits1=[(v>>i)&1 for i in first];bits2=[(v>>i)&1 for i in second]
        b1=sum(bits1[i]*bits1[i+1] for i in range(0,k,2))%2
        b2=sum(bits2[i]*bits2[i+1] for i in range(0,l,2))%2
        b1 ^= int(not any(bits1))*((v>>s1)&1)
        b2 ^= int(not any(bits2))*((v>>s2)&1)
        table.append(b1&b2)
    return bytes(table),[groups[i] for i in range(n)]

def main():
    start=time.monotonic();pilot='--pilot' in sys.argv
    d=json.loads((ROOT/'out'/'VALIDATION.json').read_text());rows=[]
    for k,l in ([(2,2)] if pilot else [(2,2),(2,4),(4,4)]):
        for shared in (False,True):
            for r in ([0] if pilot else [0,2]):
                t,g=direct_truth(k,l,shared,r);family=f'AND-{k}-{l}-shared{int(shared)}-r{r}'
                for rule in c.RULES:
                    raw=c.tree(t,list(range(len(g))),rule,g)
                    ref=next(x for x in d['cases'] if x['family']==family and x['rule']==rule)
                    c.check(raw['I_exact']==ref['I_exact'])
                    c.check(raw['H_scaled'][0]<=ref['H_scaled'][1] and ref['H_scaled'][0]<=raw['H_scaled'][1])
                    for a,b in zip(raw['Q_scaled'],ref['Q_scaled']):c.check(a[0]<=b[1] and b[0]<=a[1])
                    c.check(raw['root_query'][0]['coordinate']==ref['root']['chosen'])
                    rows.append({'family':family,'rule':rule,'raw_Q_scaled':raw['Q_scaled'],'compressed_Q_scaled':ref['Q_scaled'],'raw_nodes':raw['unique_tree_nodes'],'raw_exact_ties':raw['greedy_exact_ties']})
                c.stats.cache_clear();c.children.cache_clear();c.symbolic_H.cache_clear()
                print('replayed',family,flush=True)
                c.check(time.monotonic()-start<(60 if pilot else 1200))
    out={'rows':rows,'assertions':c.ASSERTIONS,'elapsed_seconds':time.monotonic()-start,'external_review':False,'same_log_kernel':True}
    (ROOT/'out'/('REPLAY_PILOT.json' if pilot else 'REPLAY.json')).write_text(json.dumps(out,indent=2)+'\n')
    print('PASS',len(rows),c.ASSERTIONS,out['elapsed_seconds'])
if __name__=='__main__':main()
