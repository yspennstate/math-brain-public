"""Sharp signed-capacity transfer at actual negative full terminals."""
from mixed import *
import mixed as ledger
from itertools import product

def exact_boundaries():
    count=0;checks=0;features=set()
    for s0,s1 in product(range(-2,3),repeat=2):
        ss=[F(s0),F(s1)];P=sum(max(s,0) for s in ss)/2;N=sum(max(-s,0) for s in ss)/2
        for k in range(9):
            T=F(k,2)
            if T>P-N:continue
            count+=1
            kernels=[max(s,0)/P for s in ss] if P else [F(1),F(1)]
            flow=[max(-s,0)-N*max(s,0)/P for s in ss] if P else [F(0),F(0)]
            debit=[T*a for a in kernels]
            labels=[[F(1,3)*a,(T-F(1,3))*a] for a in kernels]
            assert sum(flow)==0;checks+=1
            assert sum(debit)/2==T;checks+=1
            assert all(s+f-d>=0 for s,f,d in zip(ss,flow,debit));checks+=1
            assert sum(max(f,0) for f in flow)/2==N;checks+=1
            assert all(sum(l)==d for l,d in zip(labels,debit));checks+=1
            assert sum(l[0] for l in labels)/2==F(1,3);checks+=1
            assert sum(l[1] for l in labels)/2==T-F(1,3);checks+=1
            if T==0:features.add('T=0 signed labels retained')
            if P==0:features.add('P=0 no division')
            if N>0:features.add('negative terminal paid')
            if T==P-N:features.add('saturation')
    return {'cases':count,'exact_predicates':checks,'features':sorted(features)}

def main():
    start=time.perf_counter();root=profile([G]*6);first,e1,_=query(root,0,2);second,e2,_=query(first[0],0,0)
    sat= query(second[0],0,1)[0][0]
    anchors,e4,_=query(sat,1,0);records=[]
    for b,anchor in enumerate(anchors):
      for first_label in [4,5]:
        first_index=[1,4,5].index(first_label)
        cs,e5,_=query(anchor,0,first_index)
        hit,stopped=cs;labels=[x for x in [1,4,5] if x!=first_label]
        last_index=labels.index(9-first_label)
        leaves,e6,_=query(hit,0,last_index);negative,positive_leaf=leaves
        test(hit['S'][0]>0);test(stopped['S'][0]>0)
        test(negative['S'][1]<0);test(positive_leaf['S'][0]>0)
        T=plus(hit['S'],e6);P=scale(positive_leaf['S'],F(1,2));N=scale(negative_cost(negative['S']),F(1,2))
        test(T[0]>0);test(sub(P,N)[0]>0)
        identity=sub(T,sub(P,N));test(identity[0]<=0<=identity[1])
        A=negative_cost(negative['S'])
        # Common kernel is exactly (0,2), since only one child has positive S.
        debit=[(0,0),scale(T,F(2))]
        old_labels=[(0,0),scale(hit['S'],F(2))]
        new_labels=[(0,0),scale(e6,F(2))]
        transfers=[A,(-A[1],-A[0])]
        residuals=[sub(plus(c['S'],f),d) for c,f,d in zip(leaves,transfers,debit)]
        for residual in residuals:test(residual[0]<=0<=residual[1])
        test(negative['I']>0 and positive_leaf['I']>0)
        # Rigorous terminal and transfer ranges, simple rational comparisons.
        if b==0:
            test(A[0]*1000>55*Q);test(A[1]*1000<56*Q)
        else:
            test(A[0]*1000>45*Q);test(A[1]*1000<46*Q)
        records.append({'block1_answer':b,'first_core0_original_coordinate':first_label,
          'last_core0_original_coordinate':9-first_label,'last_parent_H':hit['H'],'last_parent_I':str(hit['I']),
          'unchanged_incoming_saturated_debit':hit['S'],'new_signed_query_excess':e6,'required_T':T,
          'positive_mean_capacity_P':P,'minimum_mean_transfer_N':N,'common_kernel':['0','2'],
          'full_terminal_H':[c['H'] for c in leaves],'full_terminal_I':[str(c['I']) for c in leaves],
          'full_terminal_S':[c['S'] for c in leaves],'old_label_children':old_labels,'new_label_children':new_labels,
          'total_children_debit':debit,'net_terminal_transfers':transfers,'zero_residual_diagnostics':residuals,
          'negative_terminal_needed_subsidy':A,'negative_terminal_root_reach':'1/64',
          'positive_terminal_root_reach':'1/64','earlier_stopped_positive_terminal':retain(stopped,'1/32',stopped['S'],'first core0 bit=1; saturation unchanged'),
          'old_parked_sibling_additional_draw':'0'})
        (ROOT/'out/COUPLED_CASES.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
    scalar=exact_boundaries();test(len(scalar['features'])==4)
    both_root=scale(plus(records[0]['negative_terminal_needed_subsidy'],records[2]['negative_terminal_needed_subsidy']),F(1,64))
    test(both_root[0]*640>Q);test(both_root[1]*32000<51*Q)
    result={'version':'signed-capacity-common-kernel-v1','physical_cases':len(records),'scalar':scalar,
      'explicit_ledger_predicates_including_runtime':ledger.explicit,'engine_assertions':engine.tests,
      'runtime_seconds':time.perf_counter()-start,'parked_reserve_new_draw':'0','failed':0,
      'both_anchor_root_weighted_minimum_transfer':both_root,'certified_root_transfer_bounds':['1/640','51/32000']}
    test(result['runtime_seconds']<55)
    (ROOT/'out/COUPLED_VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':main()
