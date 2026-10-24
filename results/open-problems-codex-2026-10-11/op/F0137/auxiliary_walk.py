from fractions import Fraction as F
import pathlib,json,math
R=pathlib.Path(__file__).resolve().parent
p,q,r=F(2,5),F(3,10),F(2,25)
A=p+q+2*r; delta=p-q; kappa=2*A-max(p+q,2*r)
M=F(1); terms=[]; total=F(0)
for n in range(3):
 if n: M *= (p+n-1)*(q+n-1)/(A+n-1)**2
 term=M*(delta-n)/(A+n); total+=term
 terms.append({'n':n,'loop_probability':str(M),'signed_drift_term':str(term),'partial_sum':str(total)})
assert total<0 and kappa>1 and 0<delta<1
result={'alpha':['2/5','2/25','3/10','2/25'],'A':str(A),'delta':str(delta),'kappa':str(kappa),
 'three_terms':terms,'negative_partial_sum':str(total),'negative_partial_sum_float':float(total),
 'proof':'All subsequent signed numerator terms are strictly negative; denominator is finite positive because kappa>1.'}
# Exact path reversal identity on paths with loops. The walk need not be simulated.
dirs={(1,0):0,(0,1):1,(-1,0):2,(0,-1):3}; alpha=(p,r,q,r)
def cylinder(path):
 counts={}
 for x,y in zip(path,path[1:]):
  e=dirs[(y[0]-x[0],y[1]-x[1])]; counts.setdefault(x,[0]*4)[e]+=1
 prob=F(1)
 for counts_x in counts.values():
  for e,n in enumerate(counts_x):
   for k in range(n): prob*=alpha[e]+k
  for k in range(sum(counts_x)): prob/=A+k
 return prob,counts
def rising(a,n):
 v=F(1)
 for k in range(n): v*=a+k
 return v
paths=[[(0,0),(1,0)],[(0,0),(-1,0),(0,0),(-1,0),(0,0),(1,0)],
 [(0,0),(1,0),(1,1),(0,1),(0,0),(1,0)],
 [(0,0),(0,1),(1,1),(1,0),(0,0),(-1,0),(-1,1)]]
checks=[]
for path in paths:
 prob,counts=cylinder(path); revprob,revcounts=cylinder(list(reversed(path)))
 # The actual reversed path starts at path[-1]; translation is immaterial.
 u,v=path[0],path[-1]
 endpoint=(A+sum(counts.get(v,[0]*4)))/(A+sum(counts.get(u,[0]*4))-1)
 factor=F(1)
 for x,cx in counts.items():
  for i,n in enumerate(cx): factor*=rising(alpha[i],n)/rising(alpha[(i+2)%4],n)
 predicted=endpoint*factor
 assert prob/revprob==predicted
 checks.append({'path':path,'likelihood_ratio':str(prob/revprob),'formula_ratio':str(predicted)})
result['reversal_checks']=checks
# Test the proposed repair: sum the drift over the entire two-site residence.
p2,q2,r2=F(41,100),F(39,100),F(3,40)
A2=p2+q2+2*r2; delta2=p2-q2; kappa2=2*A2-(p2+q2)
M=F(1); origin=F(0); escape=F(0); rows=[]
B=2*delta2+q2-A2
for n in range(3):
 if n: M*=(p2+n-1)*(q2+n-1)/(A2+n-1)**2
 term0=M*(delta2-n)/(A2+n)
 termz=M*(q2+n)*(delta2+n)/(A2+n)**2
 grouped=M*(delta2*(A2+q2)+n*B)/(A2+n)**2
 assert term0+termz==grouped
 origin+=term0; escape+=grouped
 rows.append({'n':n,'M_n':str(M),'origin_drift_term':str(term0),'neighbor_drift_term':str(termz),
 'grouped_exit_term':str(grouped),'origin_partial_sum':str(origin),'exit_partial_sum':str(escape)})
assert origin<0 and escape<0 and delta2*(A2+q2)+B<0 and B<0 and kappa2>1
result['compressed_pair']={'alpha':['41/100','3/40','39/100','3/40'],'A':str(A2),
 'delta':str(delta2),'kappa':str(kappa2),'B':str(B),'terms':rows,
 'origin_numerator_upper_bound':str(origin),'exit_displacement_upper_bound':str(escape),
 'exit_displacement_upper_bound_float':float(escape),
 'all_later_grouped_terms_negative':'B<0 and delta*(A+q)+B<0 imply the numerator is negative for every integer n>=1.'}
# Long paths with heavily traversed edges: the exact reversal tilt loses its exponential rate.
saturated=[]
for L in [1,2,4,8]:
 n=L; path=[(0,0)]
 for k in range(L):
  for _ in range(n): path.extend([(k+1,0),(k,0)])
  path.append((k+1,0))
 prob,counts=cylinder(path); rp,rc=cylinder(list(reversed(path)))
 ratio=((p+n)/(q+n))**L
 assert prob/rp==ratio
 saturated.append({'L':L,'loops_per_edge':n,'length':len(path)-1,'ratio':str(ratio),
  'log_ratio_per_distance':math.log(float(ratio))/L,'log_path_probability':math.log(float(prob))})
result['saturated_reversal_paths']=saturated
# Stronger example: both failures already certified with two terms and A>1.
pp,qq,tt=F(49,100),F(12,25),F(3,50)
AA=pp+qq+tt; dd=pp-qq; kk=2*AA-pp-qq
mm=pp*qq/AA**2; BB=2*dd+qq-AA; CC=dd*(AA+qq)
origin_two=dd/AA+mm*(dd-1)/(AA+1)
exit_two=CC/AA**2+mm*(CC+BB)/(AA+1)**2
assert AA>1 and kk>1 and dd>0 and origin_two<0 and exit_two<0 and BB<0 and CC+BB<0
result['stronger_example']={'p':str(pp),'q':str(qq),'transverse_total':str(tt),
 'transverse_each_direction_d2':'3/100','A':str(AA),'delta':str(dd),'kappa':str(kk),
 'M_1':str(mm),'B':str(BB),'C':str(CC),
 'origin_numerator_two_term_bound':str(origin_two),
 'exit_displacement_two_term_bound':str(exit_two),'exit_displacement_two_term_bound_float':float(exit_two)}
(R/'auxiliary_results.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps(result,indent=2))
