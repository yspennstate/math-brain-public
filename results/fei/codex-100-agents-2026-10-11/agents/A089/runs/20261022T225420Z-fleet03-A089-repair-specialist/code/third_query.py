"""Frozen third-query continuation; exact arithmetic, no fresh bank."""
from check import *
import check as engine

def mul(a,b):
    vals=[x*y for x in a for y in b]
    return min(vals)//Q,ceildiv(max(vals),Q)
def div(a,b):
    assert b[0]>0
    vals=[F(x*Q,y) for x in a for y in b]
    return min(vals).__floor__(),max(vals).__ceil__()
def avg(xs):
    z=(0,0)
    for x in xs:z=plus(z,x)
    return scale(z,F(1,len(xs)))
def display(x):return [float(F(t,Q)) for t in x]

def profile(truth):
    cg=core(G);c=core(truth);cs=[cg]*6;cs[0]=c
    op=outer('J',tuple(x['p'] for x in cs));h,I=composed(op,cs)
    U=scale(c['S'],op['q'][0]);M=sub(sub(const(4*I),h),U)
    return {'truth':truth,'core':c,'op':op,'H':h,'I':I,'U':U,'M':M,'S':plus(U,M)}

def query(p,i):
    children=[profile(child(p['truth'],i,b)) for b in [0,1]]
    d=p['op']['q'][0]*p['core']['d'][i]
    e=sub(sub(p['H'],avg([x['H'] for x in children])),const(4*d))
    dc=sub(p['op']['C'],avg([x['op']['C'] for x in children]))
    assert p['I']-(children[0]['I']+children[1]['I'])/2==d
    return children,e,dc

def main():
    start=time.perf_counter();root=profile(G)
    first,e1,_=query(root,2);g5=first[0]
    assert first[1]['core']['I']==0 and first[1]['I']>0
    old=scale(e1,F(2));second,e2,_=query(g5,0)
    B2=avg([x['U'] for x in second]);T2=plus(old,e2)
    assert sub(scale(B2,F(3,5)),T2)[0]>0
    rows=[]
    for b,p in enumerate(second):
        incoming=mul(div(T2,B2),p['U'])
        assert sub(p['U'],incoming)[0]>0 and p['M'][0]>0
        for i,d in enumerate(p['core']['d']):
            if not d:continue
            children,e,dc=query(p,i);B=avg([x['U'] for x in children]);M=avg([x['M'] for x in children]);T=plus(incoming,e)
            selected_remaining=sub(B,T)
            full_remaining=sub(plus(B,M),T)
            # Audit these hypotheses; do not assume the previous-stage sign persists.
            transfer=(max(0,-selected_remaining[1]),max(0,-selected_remaining[0]))
            identity=sub(selected_remaining,sub(sub(p['U'],incoming),dc))
            assert identity[0]<=0<=identity[1]
            leaf=[]
            for bit,c in enumerate(children):
                leaf.append({'bit':bit,'reach':'1/8','negative_points':[j for j,v in enumerate(c['truth']) if v==-1],
                  'core_dimension':(len(c['truth'])-1).bit_length(),'H_full':c['H'],'I_full':str(c['I']),
                  'selected_U':c['U'],'untouched_other_M':c['M'],'full_S4':c['S']})
            row={'second_bit':b,'third_coordinate_current_index':i,'original_coordinate':[1,3,4,5][i],
              'incoming_debit':incoming,'incoming_selected_U':p['U'],'full_query_excess':e,'delta_C':dc,
              'mean_raw_selected_B_before_outer_payment':B,'old_plus_new_debit':T,'raw_selected_remaining_before_outer_payment':selected_remaining,
              'mean_other_M':M,'minimal_other_transfer':transfer,'full_remaining':full_remaining,
              'raw_U_comparison_holds':selected_remaining[0]>=0,'raw_U_comparison_fails':selected_remaining[1]<0,
              'all_child_other_positive':all(x['M'][0]>0 for x in children),
              'all_child_full_positive':all(x['S'][0]>0 for x in children),
              'full_remaining_positive':full_remaining[0]>0,
              'no_renewal_identity':identity,'leaves':leaf}
            if B[0]>0:row['selected_fraction']=div(T,B)
            rows.append(row)
            (ROOT/'out/THIRD_QUERY_CASES.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
            assert time.perf_counter()-start<55
    result={'version':'grandchild-owner-v1','cases':len(rows),'engine_assertions':engine.tests,
      'scale_bits':192,'runtime_seconds':time.perf_counter()-start,
      'raw_U_only_failures_ignoring_outer_deductions':sum(x['raw_U_comparison_fails'] for x in rows),
      'display':[{'b':x['second_bit'],'i':x['original_coordinate'],'e':display(x['full_query_excess']),
        'raw_remaining_before_outer_deductions':display(x['raw_selected_remaining_before_outer_payment']),'raw_transfer_ignoring_outer_deductions':display(x['minimal_other_transfer']),
        'full_remaining':display(x['full_remaining']),
        'children_M':[display(c['untouched_other_M']) for c in x['leaves']],
        'children_S':[display(c['full_S4']) for c in x['leaves']]} for x in rows]}
    (ROOT/'out/THIRD_QUERY_SUMMARY.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
if __name__=='__main__':main()
