"""Same incoming subsidy after querying the negative full terminal; exact finite domain."""
from reproduce_spent import *
import itertools,sys

def neg(a):return -a[1],-a[0]
def pos(a):return max(0,a[0]),max(0,a[1])
def equalcheck(a,b):overlaps(a,b)

def restrict_active(t,a,b):
    # t has remaining original block0 labels [1,4,5].
    if b is not None:t=child(t,2,b)
    if a is not None:t=child(t,1,a)
    return t

def compare(p):
    h,I,s=independent(p['ts']);ck(I==p['I']);equalcheck(h,p['H']);equalcheck(s,p['S'])
    return h,I,s

def anchors_and_review():
    root,first,second,third,debits,D,e1,e2,e3=setup()
    anchors,_,_=split(third[0],1,0)
    review=[];negative=[];parents=[];donors=[]
    for b,p in enumerate(anchors):
        for a,c in itertools.product([None,0,1],repeat=2):
            ts=list(p['ts']);ts[0]=restrict_active(ts[0],a,c);q=full(tuple(ts));compare(q)
            review.append(dict(b=b,bit4=a,bit5=c,S=q['S'],I=str(q['I'])))
            if a==0 and c==0:negative.append(q)
        ts=list(p['ts']);ts[0]=restrict_active(ts[0],0,None);parents.append(full(tuple(ts)))
        ts=list(p['ts']);ts[0]=restrict_active(ts[0],0,1);donors.append(full(tuple(ts)))
    ck(sum(r['S'][1]<0 for r in review)==2)
    # Reconstruct both active-query orders and all actual labels.
    policy=[]
    for b,p in enumerate(anchors):
        for orig in [4,5]:
            ix=1 if orig==4 else 2
            mid,e4,_=split(p,0,ix)
            last,e5,_=split(mid[0],0,1)
            s0,s1=last[0]['S'],last[1]['S'];ck(s0[1]<0 and s1[0]>0)
            A=neg(s0);T=plus(mid[0]['S'],e5)
            ck(T[0]>0);equalcheck(scale(T,F(2)),sub(s1,A))
            ck(sub(s1,A)[0]>0)
            equalcheck(avg([(0,0),scale(mid[0]['S'],F(2))]),mid[0]['S'])
            equalcheck(avg([(0,0),scale(e5,F(2))]),e5)
            equalcheck(avg([A,neg(A)]),(0,0))
            policy.append(dict(b=b,first_original_bit=orig,A=A,donor_capacity=s1,
                               donor_booked=sub(s1,A),source_booked=[0,0],donor_reach='1/64',source_reach='1/64'))
    (ROOT/'out/SOURCE_REVIEW.json').write_text(json.dumps(dict(states=review,policies=policy,scope='Reconstruct all18 signs and4 physical transfers; no acceptance of unrelated source clauses.'),indent=2)+'\n',encoding='utf-8')
    return negative,donors,policy

def main():
    start=time.perf_counter();parents,donors,policies=anchors_and_review();rows=[]
    domain=[(b,i) for b in [0,1] for i in range(1,6)]
    if '--pilot' in sys.argv:domain=domain[:2]
    for b,original in domain:
        p=parents[b];A=neg(p['S']);ck(A[0]>0)
        cs,e,d=split(p,1,original-1)
        hh,ii,ss=compare(p)
        vals=[compare(c) for c in cs]
        ei=sub(sub(hh,avg([v[0] for v in vals])),const(4*d));equalcheck(e,ei)
        N=avg([pos(neg(c['S'])) for c in cs]);P=avg([pos(c['S']) for c in cs])
        gap=sub(N,A);extra=pos(gap)
        shifted=[plus(c['S'],A) for c in cs]
        flat=avg([pos(neg(s)) for s in shifted])
        equalcheck(plus(avg([c['S'] for c in cs]),A),e)
        ck(all(c['I']>0 for c in cs))
        row=dict(b=b,original_coordinate=original,physical_influence=str(d),incoming_A=A,
                 source_incoming_debit=[0,0],donor_A_already_spent=A,
                 old_donor_booked=policies[2*b]['donor_booked'],new_query_e=e,
                 full_children=[dict(H=c['H'],I=str(c['I']),S=c['S']) for c in cs],
                 N=N,P=P,negative_part_gap=gap,minimum_new_gross=extra,
                 flat_A_new_gross=flat,shifted_full_children=shifted,
                 no_new_transfer_feasible=gap[1]<=0,
                 no_new_transfer_impossible=gap[0]>0,
                 query_net_nonnegative=e[0]>=0,
                 recipient_child_root_reach='1/128',stopped_donor_root_reach='1/64')
        if d==0:
            ck(e[0]<=0<=e[1]);row['dummy_exact_query_excess_zero']=True
        else:ck(e[0]>0 or e[1]<0)
        rows.append(row)
        (ROOT/'out'/('PILOT_CASES.json' if '--pilot' in sys.argv else 'SUBSIDY_CASES.json')).write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
        ck(time.perf_counter()-start<55)
    result=dict(version='A071-inherited-subsidy-v1',cases=len(rows),engine_checks=engine.tests,
      negative_part_increase_cases=sum(r['no_new_transfer_impossible'] for r in rows),
      nonnegative_net_cases=sum(r['query_net_nonnegative'] for r in rows),
      negative_net_cases=sum(r['new_query_e'][1]<0 for r in rows),
      independent_states=independent.cache_info().currsize,runtime_seconds=time.perf_counter()-start,
      display=[dict(b=r['b'],i=r['original_coordinate'],e=display(r['new_query_e']),
        A=display(r['incoming_A']),N=display(r['N']),gap=display(r['negative_part_gap']),
        children=[display(c['S']) for c in r['full_children']],flat_flow=display(r['flat_A_new_gross'])) for r in rows])
    (ROOT/'out'/('PILOT.json' if '--pilot' in sys.argv else 'RESULTS.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))

if __name__=='__main__':main()
