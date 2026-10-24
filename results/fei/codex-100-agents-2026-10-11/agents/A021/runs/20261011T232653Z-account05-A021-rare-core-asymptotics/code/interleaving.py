from check import *
from itertools import permutations

def main():
    records=[]
    for t,k in ((1,2),(2,1)):
        f=activated(t,k);q=F(1,1<<k)
        selectors=[6*j+4 for j in range(t)]
        controls=list(range(6*t,6*t+k))
        rest=[6*j+r for j in range(t) for r in range(4)]+[6*j+5 for j in range(t)]
        for prefix in permutations(selectors+controls):
            r=k;rsum=0
            for coordinate in prefix:
                if coordinate in controls:r-=1
                else:rsum+=r
            result=tree(f,tuple(prefix)+tuple(rest),4)
            predicted=q*F(4*t+rsum,16)
            assert result[0]==predicted and result[1]==influence(f)
            records.append({'t':t,'k':k,'prefix':prefix,'sum_unrevealed_controls_at_selectors':rsum,'Q_bad':str(result[0]),'I':str(result[1])})
    t=2;k=1;f=activated(t,k);j=4
    bad,d,c,lo,hi=node(f,j,4);assert bad
    original_rest=[6*u+r for u in range(t) for r in range(4)]+[5,11]
    left_order=[12,10]+original_rest;right_order=[10,12]+original_rest
    left_order=tuple(x-(x>j) for x in left_order)
    right_order=tuple(x-(x>j) for x in right_order)
    left=tree(lo,left_order,4);right=tree(hi,right_order,4)
    Q=c+(left[0]+right[0])/2;expected=F(1,2)*F(8+F(3,2),16)
    assert Q==expected==F(19,64)
    records.append({'t':2,'k':1,'policy':'first selector; control before second selector only on zero branch','expected_sum_r_j':'3/2','Q_bad':str(Q),'I':str(influence(f))})
    output={'cases':len(records),'records':records,'status':'PASS','elapsed_seconds':time.perf_counter()-START}
    (ROOT/'out'/'interleaving_certificates.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({'cases':len(records),'adaptive_Q_bad':str(Q),'elapsed_seconds':output['elapsed_seconds'],'status':'PASS'},indent=2))
if __name__=='__main__':main()
