import math,json,pathlib
root=pathlib.Path(__file__).parent
lo,hi=2.,10.
for _ in range(100):
 y=(lo+hi)/2
 if math.log(2/y)+1-1/y>0:lo=y
 else:hi=y
y=(lo+hi)/2;theta=y-1;a=1/y;c=y
out={'model':'binary offspring, independent Exp(1) activation times; auxiliary BRW, not asserted to be an OU cascade','theta':theta,'a':a,'positive_speed':c,'printed_speed':1/(math.log(2/y)/theta),'boundary_residual':math.log(2/y)+theta/y,'inverted_log_coefficient':3*c/(2*theta),'source_coefficient_if_speed_sign_only_repaired':3/(2*theta*c)}
rho=(5+math.sqrt(33))/2
left=[3/(rho-1),1]
right=[2/(rho-1),1]
out['left_vector_martingale_check']={'M':[[1,2],[3,4]],'rho':rho,'left_vector':left,'M_times_left':[left[0]+2,3*left[0]+4],'rho_times_left':[rho*left[0],rho],'right_vector':right}
(root/'numerical_checks.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps(out,indent=2))
