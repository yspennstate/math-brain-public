import pathlib,json,math
root=pathlib.Path(__file__).resolve().parent
def simp(f,a,b,n=120):
 h=(b-a)/n
 return h/3*(f(a)+f(b)+sum((4 if i%2 else 2)*f(a+i*h) for i in range(1,n)))
def gap(R):
 return simp(lambda x:simp(lambda y:2/(y-x)**2*(-math.expm1(-(y-x)**2/R**2))**2,2*R,3*R),0,R)
def both_intensity(h):
 if h>=1:return 0.0
 # A=[0,1]: possible centers have length 1-sqrt(z).
 return 2/h**0.5-2+math.log(h)
out={'scaled_window_cross_gap':{str(R):gap(R) for R in [1,2,4,8,16,32]},
 'tail_count_variance':{},'finite_cluster_multiplicity_check':all(a*a<=2*a for a in [0,1,2])}
for h in [1,0.1,0.01,0.001,0.0001]:
 count_mean=4/h**0.5
 count_variance=count_mean+2*both_intensity(h)
 out['tail_count_variance'][str(h)]={'exact_normalized_variance':h*count_variance/16,'upper_bound':h**0.5/2}
out['checks']={'scale_invariant_gap':max(out['scaled_window_cross_gap'].values())-min(out['scaled_window_cross_gap'].values())<1e-12,
 'positive_gap':min(out['scaled_window_cross_gap'].values())>0,
 'tail_variance_bound':all(0<=r['exact_normalized_variance']<=r['upper_bound'] for r in out['tail_count_variance'].values()),
 'multiplicity_bound':out['finite_cluster_multiplicity_check']}
(root/'second_numerical_results.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps(out,indent=2))
