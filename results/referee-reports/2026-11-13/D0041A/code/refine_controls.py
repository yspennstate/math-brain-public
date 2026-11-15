from compare_pde import *
qsol,ints=painleve()
errors=[]
for b in [2,4]:
 for t in [-4,-3,-2,-1,0,1,3]:
  for w in [1,2,3]:
   f=formula(b,t,w,qsol,ints)
   g=formula(b,t,w,qsol,ints,zright=9,laxtol=1e-10)
   errors.append(abs(f-g))
result={'positive_spike_BVP_refinement_points':len(errors),'max_abs_change_zright8_to9_and_tolerance':float(max(errors))}
(ROOT/'data/control_refinement.json').write_text(json.dumps(result,indent=2))
print(result)
