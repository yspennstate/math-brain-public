import json,sys,hashlib,time
from pathlib import Path
from fractions import Fraction as F
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parents[1];TEAM=R.parents[3]
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def iv(x):return tuple(map(F,x))
def plus(*xs):return tuple(sum(x[k] for x in xs) for k in (0,1))
def times(x,c):return x[0]*c,x[1]*c
def subtract(x,y):return x[0]-y[1],x[1]-y[0]
def overlap(x,y):return x[0]<=y[1] and y[0]<=x[1]
ledger=read(R/'out/ledger.json');checks=0;start=time.perf_counter()
def ck(x):
    global checks
    assert x;checks+=1
source=TEAM/'agents/A089/runs/20261014T061326Z-account05-A089-repair-specialist'
orig=read(source/'out/CONTINUATION.json');unit=1<<192
source_old=tuple(F(x,unit) for x in orig['old_conditional_debit'])
source_total=tuple(F(x,unit) for x in orig['total_old_plus_new_debit'])
own_old=iv(ledger['old_conditional_debit_after_first']);own_second=iv(ledger['prefix_rate4_excesses'][1])
ck(overlap(source_old,own_old));ck(overlap(source_total,plus(own_old,own_second)))
for node in ledger['continuation']:
    first,second=node['children']
    for key in first['incoming_labels']:
        mean=times(plus(iv(first['incoming_labels'][key]),iv(second['incoming_labels'][key])),F(1,2))
        expected=iv(node['parent_labels'][key]) if key in node['parent_labels'] else iv(node['query']['excess_K'])
        ck(overlap(mean,expected))
    ck(all(iv(c['remaining_full_owner'])[0]>0 for c in node['children']))
leaves=ledger['complete_terminals'];ck(sum(F(x['reach']) for x in leaves)==1)
root_state=read(R/'out/state_xxxxxx.json');q_receipts=[]
for l in range(1,6):
    terminal_q=sum(F(leaf['reach'])*F(read(R/('out/state_'+leaf['tag'].replace('*','x')+'.json'))['outer']['q'][l]) for leaf in leaves)
    root_q=F(root_state['outer']['q'][l]);ck(terminal_q==root_q)
    q_receipts.append({'other_core':l,'root_q':root_q,'terminal_reach_weighted_q':terminal_q})
totals={}
for leaf in leaves:
    for label,bound in leaf['labels'].items():totals[label]=plus(totals.get(label,(F(0),F(0))),times(iv(bound),F(leaf['reach'])))
ck(overlap(totals['first_query_K4'],iv(ledger['prefix_rate4_excesses'][0])))
ck(overlap(totals['second_query_K4'],times(own_second,F(1,2))))
ck(iv(ledger['target_tag00000star']['remaining_full_owner'])[0]>F(12,25))
ck(iv(ledger['root_remaining_after_tax'])[0]>F(11,10))
target=ledger['target_tag00000star'];T=iv(target['selected_to_outer_transfer'])
ck(F(1,10)<T[0]<=T[1]<F(11,100));ck(iv(ledger['target_other_owner_margin'])[1]<-F(1,10))
incoming=iv(target['net_debit']);ck(incoming[0]>0)
accepted=read(TEAM/'agents/A074/runs/20261014T060751Z-account05-A074-independent-reproducer/CLAIMS.json')[0]
original=read(R.parent/'20261014T020611Z-account05-A072-exact-walsh-engine/CLAIMS.json')[0]
for key in ['claim_id','version','exact_statement','hypotheses','statement_sha256']:ck(accepted[key]==original[key])
ck(accepted['status']=='INDEPENDENTLY_ACCEPTED')
result={'passed':True,'assertions':checks,'runtime_seconds':time.perf_counter()-start,
 'source_A089_old_conditional_debit':source_old,'own_old_conditional_debit':own_old,'source_A089_old_plus_second':source_total,'own_old_plus_second':plus(own_old,own_second),
 'source_review':'HOLDS_SCOPED: actual J/block0/coordinate2 then surviving0 K4 booking/constant child and3/5 cap. No whole-eight sharpness review.',
 'final_reach_weighted_label_totals':totals,'other_owner_exact_pivotal_weight_conservation':q_receipts,'target_incoming_net_debit':incoming,'target_transfer':T,'target_remaining':iv(target['remaining_full_owner']),
 'consumed_independent_acceptance':{'claim_id':accepted['claim_id'],'version':accepted['version'],'statement_sha256':accepted['statement_sha256'],'reviewer':'A074','status':accepted['status']}}
ck(time.perf_counter()-start<55)
(R/'out/SOURCE_AND_LABEL_AUDIT.json').write_text(json.dumps(result,indent=2,default=str)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ['passed','assertions','runtime_seconds','source_review']}))
