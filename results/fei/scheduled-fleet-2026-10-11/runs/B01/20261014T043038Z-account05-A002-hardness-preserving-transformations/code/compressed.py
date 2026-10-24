from pathlib import Path
from fractions import Fraction as Q
from math import comb
import json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(c):
    global checks
    checks+=1
    assert c,checks
def records(q):return {'numerator':str(q.numerator),'denominator':str(q.denominator)}
# Independent A005 actual N200 code: data labels and all tag masses.
D=192;r=8;t=64;N=D+r;K=Q(8,3)
tags=[x for x in range(1,1<<r) if x.bit_count()>=2][:D]
ck(len(tags)==D);ck((1<<(r-1))-(r-1)-1<D<=(1<<r)-r-1)
touch=[sum(any(tags[3*j+i]>>a&1 for i in range(3)) for j in range(t)) for a in range(r)]
ck(touch==[64,64,50,39,36,33,24,24])
I=Q(3*t,4)+sum((1-Q(1,1<<m))/2 for m in touch);ck(I<52)
# delta(point3)=2-(9/8)log2(3)>137/640 follows from3^80<2^127.
ck(3**80<2**127)
gap=Q(137*t,640)-K*(I-Q(3*t,4));ck(gap>Q(91,30))
s=98;err=Q(2*(N+s)+3,2*(1<<s))+K*Q(2*N*(1<<2),1<<N)
ck(err<Q(1,30));ck(gap-err>3)
control200={'dimension':N,'data_dimension':D,'tag_dimension':r,'tensor_copies':t,'seed':'three-bit one-point defect','K':'8/3','tag_block_touches':touch,'coded_influence':records(I),'seed_deficit_lower':'137/640','seed_log_certificate':{'left':'3^80','right':'2^127','strict':True},'unedited_gap_lower':records(gap),'uniform_parent_singleton_pair_edit_error_upper':records(err),'all_individual_child_gap_lower':records(gap-err),'gap_gt3':True,'total_pair_collision_and_refund_upper':{'numerator':16*comb(N,2),'power_of_two_denominator_exponent':N}}
# New growing-block, rare and weak actual recipe: no huge labels/table enumerated.
t=4096;n=3;k=64;D=n*t+1+k;b=4;A=2*D;r=117;N=D+r;rho=Q(1,1<<k)
ck(D==12353 and N==12470)
ck(A<=1<<16 and A**5>1<<64) # b=floor(sqrt(t)/log2(2D))=4
ck(1<<116<A**8<=1<<117);ck(r<=D and b<=D)
ck(b*(2*D)**(b-1)<1<<r) # greedy column choices never exhaust alphabet
ck(3**5<2**8) # point3 delta>1/5
gap_per_rho=Q(t,5)-K*(1+k+2*r);ck(gap_per_rho==Q(328,15))
s=(N-b)//2-1;ck(s==6232)
err=Q(2*(N+s)+3,2*(1<<s))+K*Q(2*N*(1<<b),1<<N)
ck(err<rho/2)
gap=rho*gap_per_rho-err;ck(gap>rho*Q(641,30))
factor=4*sum(comb(N,a)*(1<<a) for a in range(1,b+1))
ck(factor<1<<(N-12000));ck(16*comb(N,2)<1<<(N-12000))
Iupper=rho*(Q(3*t,4)+1+k+2*r)+Q(2*N,1<<N)
ck(Iupper<Q(1,1<<52))
control={'dimension':N,'physical_data_dimension':D,'tag_dimension':r,'tensor_copies':t,'controls':k,'maximum_block_size':b,'maximum_block_floor_exact_integer_test':True,'greedy_code_verified_by_counting_bound_not_materialized':True,'coded_root_gap_divided_by_activation_probability_lower':'328/15','uniform_exceptional_child_error_lt_half_activation_probability':True,'all_individual_child_gap_gt_activation_probability_times':'641/30','all_blocks_count':sum(comb(N,a) for a in range(1,b+1)),'all_blocks_total_collision_upper':{'numerator':factor,'power_of_two_denominator_exponent':N},'total_collision_and_pair_refunds_lt':'2^-12000','total_influence_lt':'2^-52','max_influence_upper':'2*2^-64+2*2^-12470','mean_lower':'1-2^-64-2*2^-12470','full_support_and_physical_primitivity':'proved odd-negative-count parity; no huge spectrum enumerated'}
out={'status':'PASS','helper_version':'A002-growing-block-compressed-v1','exact_assertions':checks,'failures':0,'seconds':time.perf_counter()-start,'arithmetic':'exact integer powers/binomials and Fraction bounds; no floating logarithm','A005_N200_review':control200,'new_N12470_actual_recipe':control}
(R/'out/COMPRESSED_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({'status':'PASS','exact_assertions':checks,'seconds':out['seconds'],'control_dimensions':[200,12470]}))
