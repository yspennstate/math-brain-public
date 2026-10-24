from check_refunds import *
import check_refunds as library
h=[-1,1,1,1];logical=[h[x&3]*h[x>>2] for x in range(16)]
f=coded_truth(logical);N=len(f);n=12;p=F(1,N);old=fwht(f)
check(N==4096 and f[0]==1)
check(sum(v!=0 for v in old)==16)
check(all(abs(v)==N//4 for v in old if v))
supp=[s for s,a in enumerate(old) if a]
check(min((s^t).bit_count() for s,t in combinations(supp,2))==3)
check(infs(f)==[F(1,2)]*12)
g=f.copy();g[0]*=-1;new=fwht(g)
check(sum(v<0 for v in g)%2==1)
check(all(v%4==2 for v in new))
check(all(v!=0 for v in new))
check(new==[v-2 for v in old]);check(infs(g)==[F(1,2)-2*p]*12)
H=entropy([F(v*v,N*N) for v in new]);I=sum(infs(g));K=F(1,2)
check(H[0]-K*I>0)
records=[]
for i,j in ((0,1),(0,3),(0,6)):
    vals=[F(0)]*6
    for t in range(N):
        if t&(1<<i|1<<j):continue
        q=quartet(new[t],new[t|1<<i],new[t|1<<j],new[t|1<<i|1<<j])
        for k,v in enumerate(q):vals[k]+=v/(N*N)
    check(vals[2]<=16*p and vals[4]+vals[5]<=16*p)
    records.append({'pair':[i,j],'C_i':str(vals[0]),'C_j':str(vals[1]),'C_pair':str(vals[2]),'P':str(vals[3]),'refund_sum':str(vals[4]+vals[5])})
child=[g[(1<<6)|((x&1)<<0)|(((x>>1)&1)<<3)] for x in range(4)]
check(child==h)
childH=entropy([F(v*v,16) for v in fwht(child)]);childI=sum(infs(child))
check(childH[0]-K*childI>0)
check(K*(F(1,2)-2*p)>(2*n+13)*p)
save('PRIME_TENSOR_CERTIFICATE.json',{'status':'PASS','n':n,'logical_seed':h,'tensor_copies':2,'parity_repetition':3,'seed_H':'4','seed_I':'6','edited_H_interval':[str(v) for v in H],'edited_I':str(I),'fixed_K':'1/2','edited_D_lower':str(H[0]-K*I),'odd_negative_count':True,'integer_Walsh_sums_mod4':2,'all_Fourier_coefficients_nonzero':True,'prime_proof':'Odd negative count excludes every nontrivial coordinate product','three_representative_pairs':records,'proper_child':{'free_coordinates':[0,3],'fixed_one_coordinate':6,'all_other_fixed_bits':0,'truth':child,'H_interval':[str(v) for v in childH],'I':str(childI),'D_lower':str(childH[0]-K*childI)},'minimality_exclusion':{'K_times_seed_influence_minus_surgery_error':str(K*(F(1,2)-2*p)),'singleton_price_upper':str((2*n+13)*p)},'assertions':library.assertions,'runtime_seconds':time.perf_counter()-START})
print(json.dumps({'status':'PASS','n':n,'assertions':library.assertions,'runtime_seconds':time.perf_counter()-START,'prime_full_support':True,'actual_violating_child_retained':True},indent=2))
