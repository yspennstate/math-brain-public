from check_collision import *
tree=((((((),()),(),()),()),()))
f=[nandtree(tree,iter([1 if x>>i&1 else -1 for i in range(6)])) for x in range(64)]
base=block(f,48)
check(bounds(add(base['H'],{F(2):-F(601,200)}))[0]>0)
check(base['I']==F(5,4) and base['IA']==1)
check(bounds(base['V'])[1]<F(47,20))
for i in range(6):
    b=block(f,1<<i)
    check(b['IA']>=F(1,32))
    check(bounds(add(b['V'],{F(2):-F(319,100)*b['IA']}))[0]>0)
n=24;p=F(1,1<<n);u=F(1,2048);K=F(12,5)
check(37*u<F(19,1000));check(2*K*n*p<F(1,1000))
check(15*u+10*F(1,4096)<F(1,100));check(2*K*2*p<F(1,1000))
check(F(1,20)>F(11,1000));check(F(79,3200)>F(11,1000))
save('TENSOR_BOUNDARY.json',{'status':'PASS','seed_entropy':interval(base['H']),'seed_entropy_lower_bound':'601/200','fixed_K':'12/5','minimum_tensor_copies':4,'minimum_n':24,'entropy_error_upper':'19/1000','total_influence_price_error_upper':'1/1000','collision_certificate_plus_influence_error_upper':'11/1000','joint_seed_slack_lower':'1/20','singleton_seed_opposite_slack_lower':'79/3200','large_cube_enumerated':False,'all_dimensional_extension':'Analytic tensor identities, n->n+6 monotonicity and one-point stability; see proof section4','runtime_seconds':time.perf_counter()-START})
print((RUN/'out'/'TENSOR_BOUNDARY.json').read_text())
