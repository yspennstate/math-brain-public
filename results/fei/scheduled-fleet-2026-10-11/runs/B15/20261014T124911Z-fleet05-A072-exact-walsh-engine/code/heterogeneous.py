import check as c
import json,time,math
from fractions import Fraction as F
start=time.perf_counter();R=c.R
ledger=json.loads((R/'out/ledger.json').read_text());target=ledger['target_tag00000star']
incoming={k:tuple(map(F,v)) for k,v in target['incoming_labels'].items()}
g0=(-1,1);cores=(g0,)+(c.G,)*5
def packet(tables):
    cs=[c.core(tuple(t)) for t in tables];ps=tuple(x['p'] for x in cs);o=c.outer(ps);q=o['q']
    H=c.add(*(c.scale(x['H'],z) for x,z in zip(cs,q)),o['C']);I=sum(x['I']*z for x,z in zip(cs,q));S=c.sub(c.const(c.K*I),H)
    A=c.scale(cs[0]['SK'],q[0]);M=c.sub(c.add(*(c.scale(cs[j]['SK'],q[j]) for j in range(1,6))),o['C'])
    T=c.scale(M,-1) if M[1]<0 else c.const(0)
    if M[0]<=0<=M[1]:c.ck(M==(0,0))
    U=c.sub(A,T);O=M if M[0]>0 else c.const(0)
    c.positive(S);c.positive(U) if U!=(0,0) else None
    c.overlap(c.sub(S,c.add(U,O)))
    return {'core_certificates':cs,'outer':o,'H':H,'I':I,'S':S,'A_original_owner0':A,'M_other_owners':M,'transfer_original_owner0_to_outer':T,'U':U,'O':O}
parent=packet(cores);children=[]
for bit in (0,1):children.append(packet((g0,tuple(c.G[bit|(x<<1)] for x in range(32)))+(c.G,)*4))
for j in range(6):c.ck(sum(x['outer']['q'][j] for x in children)/2==parent['outer']['q'][j])
d=parent['outer']['q'][1]*c.core(c.G)['influences'][0]
c.ck(parent['I']-sum(x['I'] for x in children)/2==d)
prob=parent['outer']['p'];direct=F(0)
for x in range(32):
    for z in range(32):
        other=(z&1)|((z>>1)<<2)
        if c.J[other|((c.G[x<<1]<0)<<1)]!=c.J[other|((c.G[(x<<1)|1]<0)<<1)]:
            direct+=math.prod(prob[j] if other>>j&1 else 1-prob[j] for j in range(6) if j!=1)/32
c.ck(direct==d)
excess=c.sub(c.sub(parent['H'],c.scale(c.add(*(x['H'] for x in children)),F(1,2))),c.const(c.K*d))
B=c.scale(c.add(*(x['S'] for x in children)),F(1,2));old=c.add(*incoming.values())
c.positive(c.sub(parent['S'],old));c.overlap(c.sub(c.add(parent['S'],excess),B))
labels=dict(incoming);labels['cross_core1_query0_K9over2']=excess
book=[]
for x in children:
    ratio=c.div(x['S'],B);ls={k:c.prod(v,ratio) for k,v in labels.items()};total=c.add(*ls.values());remaining=c.sub(x['S'],total)
    c.positive(remaining)
    selected_debit=c.prod(c.div(x['U'],x['S']),total);other_debit=c.prod(c.div(x['O'],x['S']),total)
    c.positive(c.sub(x['U'],selected_debit)) if x['U']!=(0,0) else c.overlap(selected_debit)
    c.positive(c.sub(x['O'],other_debit)) if x['O']!=(0,0) else c.overlap(other_debit)
    book.append({'unconditional_reach':F(1,64),'labels':ls,'net_debit':total,'remaining':remaining,'selected_debit':selected_debit,'other_debit':other_debit,'full_terminal':x})
for k,v in labels.items():c.overlap(c.sub(c.scale(c.add(*(x['labels'][k] for x in book)),F(1,2)),v))
# Replace only the old last query's2 terminals; all stopped siblings persist.
oldleaves=[x for x in ledger['complete_terminals'] if x['tag'] not in ['000000','000001']]
c.ck(len(oldleaves)==5)
mean=c.add(*(c.scale(tuple(map(F,x['remaining'])),F(x['reach'])) for x in oldleaves),*(c.scale(x['remaining'],F(1,64)) for x in book))
c.overlap(c.sub(mean,tuple(map(F,ledger['root_remaining_after_tax']))));c.positive(c.sub(mean,c.const(F(11,10))))
c.ck(sum(F(x['reach']) for x in oldleaves)+2*F(1,64)==1)
c.ck(all(0<x['core_certificates'][1]['p']<1 for x in children))
c.ck(time.perf_counter()-start<55)
out={'passed':True,'assertions':c.COUNT,'runtime_seconds':time.perf_counter()-start,'continuation_is_alternative':True,'original_owner':0,'queried_block':1,'queried_coordinate':0,'parent':parent,'incoming_old_labels_unchanged':incoming,'physical_influence':d,'full_query_excess_K9over2':excess,'children':book,'unchanged_stopped_siblings':oldleaves,'final_root_mean_remaining':mean,'all_terminal_reaches_sum':1,'note':'No root bank or original booking was renewed; both new queried-core children are nonconstant.'}
c.dump('heterogeneous.json',out)
print(json.dumps({'passed':True,'assertions':c.COUNT,'runtime_seconds':out['runtime_seconds'],'child_biases':[str(x['core_certificates'][1]['p']) for x in children],'alternative_root_remaining_display':float(mean[0]),'excess_sign':'positive' if excess[0]>0 else 'negative' if excess[1]<0 else 'zero_or_unresolved'}))
