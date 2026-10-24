import json,time
from fractions import Fraction as Q
from pathlib import Path
import check as lib

records=[]
def visit(values,labels,padding,path):
    s=lib.info(values)
    if s['U']<=s['I']:
        return
    relevant=[i for i in range(s['n']) if any(v and mask&(1<<i) for mask,v in enumerate(s['a']))]
    i=next((i for i in relevant if labels[i] in padding),relevant[0])
    child=lib.children(values,i)
    stats=[lib.info(v) for v in child]
    edge=s['I']-(stats[0]['I']+stats[1]['I'])/2
    drop=lib.add(s['H'],lib.scale(stats[0]['H'],-Q(1,2)),lib.scale(stats[1]['H'],-Q(1,2)))
    ratio=lib.scale(drop,1/edge)
    records.append({'path':path,'labels':labels,'query_original_coordinate':labels[i],'truth_values':values,'I':s['I'],'U':s['U'],'queried_influence':edge,'entropy_drop':drop,'ratio':ratio})
    rest=labels[:i]+labels[i+1:]
    for b in [0,1]:
        visit(child[b],rest,padding,path+[(labels[i],b)])

outputs=[]
for blocks in [2,3]:
    m=2*blocks;r=2
    base=[-1 if any(((x>>(2*j))&3)==0 for j in range(blocks)) else 1 for x in range(1<<m)]
    values=[base[x&((1<<m)-1)] for x in range(1<<(m+r))]
    values[0]*=-1
    records.clear()
    visit(values,list(range(m+r)),set(range(m,m+r)),[])
    worst=max(records,key=lambda v:v['ratio'][1])
    lib.check(worst['ratio'][0]>5)
    if blocks==2:
        lib.check(worst['ratio'][0]>8)
    outputs.append({'family':'edited_tribes','blocks':blocks,'padding':r,'worst_node':worst})
lib.check(3**9*5**25<2**76)
lib.check(3**9>2**14)
result={'complete':True,'cases':2,'assertions':lib.ASSERTIONS,'elapsed_seconds':time.perf_counter()-lib.START,'rows':outputs,'bent_m2_r2_rate':'24-(9/4)log2(3)-(25/4)log2(5)>5','bent_exact_integer_certificate':{'left':3**9*5**25,'right':2**76},'point_defect_n3_exact_integer_certificate':{'left':3**9,'right':2**14}}
(Path(__file__).resolve().parents[1]/'out'/'TRIBES_NODE_WITNESS.json').write_text(json.dumps(lib.encode(result),indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:lib.encode(v) for k,v in result.items() if k!='rows'},indent=2))
