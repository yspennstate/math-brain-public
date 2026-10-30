import json,time
from fractions import Fraction as Q
from pathlib import Path
import check as lib

cases=0;admitted=0;constants=0;max_tree_rate=(Q(0),Q(0))
for m in [1,2,3]:
    for table in range(1<<(1<<m)):
        base=[1 if table&(1<<x) else -1 for x in range(1<<m)]
        edited_base=list(base);edited_base[0]*=-1
        g=lib.info(base);edited=lib.info(edited_base)
        if not g['I']:
            constants+=1
        for r in [1,2,3,4]:
            delta=Q(1,1<<r);d=Q(1,1<<(m+r-1))
            values=[base[x&((1<<m)-1)] for x in range(1<<(m+r))]
            values[0]*=-1
            root=lib.info(values)
            core=root['I']-r*d
            lib.check(core==(1-delta)*g['I']+delta*edited['I'])
            lib.check(core>=m*d)
            drop=lib.add(root['H'],lib.scale(g['H'],-(1-delta)),lib.scale(edited['H'],-delta))
            lib.check(drop[1]<=4*r*d+(1+6/lib.LN2[0])*core)
            if g['U']<=g['I'] and edited['U']<=edited['I']:
                admitted+=1
                tree=lib.tree(values,list(range(m+r)),set(range(m,m+r)))
                # Because both full-padding core leaves are admitted, no core query is needed.
                lib.check(tree['QI']<=r*d)
                lib.check(tree['QH'][1]<=4*tree['QI']+(1+6/lib.LN2[0])*core)
                lib.check(tree['leaf_predicate'])
                lib.check(root['H'][1]<=(5+6/lib.LN2[0])*root['I'])
                max_tree_rate=max(max_tree_rate,tree['max_ratio'],key=lambda x:x[1])
            cases+=1
result={'complete':True,'cases':cases,'admitted_stopping_trees':admitted,'constant_seeds':constants,'assertions':lib.ASSERTIONS,'maximum_admitted_node_ratio':max_tree_rate,'elapsed_seconds':time.perf_counter()-lib.START,'arithmetic':'integer truth-table spectra and Fraction; certified logarithm intervals','unadmitted_cases':'Not asserted closed; core access remains unpaid'}
(Path(__file__).resolve().parents[1]/'out'/'check_reserve.json').write_text(json.dumps(lib.encode(result),indent=2)+'\n',encoding='utf-8')
print(json.dumps(lib.encode(result),indent=2))
