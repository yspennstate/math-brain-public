from explore_vary_seed import D,P,M,ineq,b0,h,linprog,np,Path
# Diagonal-dominant positive matrix lift, maximizing uniform reserve.
AA=np.column_stack([ineq,np.ones(360)])
MM=np.column_stack([M,np.zeros(100)])
obj=np.zeros(181);obj[-1]=-1
res=linprog(obj,A_eq=MM,b_eq=np.r_[b0,h],A_ub=AA,b_ub=np.zeros(360),bounds=[(0,None)]*90+[(None,None)]*90+[(0,None)],method='highs')
print('max uniform reserve',res.success,res.x[-1] if res.success else '')
if res.success:
 print('seed72',np.round(72*res.x[:90],8).tolist())
 print('flow72',np.round(72*res.x[90:180],8).tolist())
 np.savez(Path(__file__).resolve().parent/'one_angle_seed_positive.npz',x=res.x[:90],y=res.x[90:180],epsilon=res.x[-1])
