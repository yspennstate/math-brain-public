from explore import *
x1=permute(x0,0,3); b1=contrast(rotate(F,0,3,np.pi/2)); bm=contrast(rotate(F,0,3,np.pi/4)); h=bm-(b0+b1)/2
P=np.column_stack([permute(np.eye(90)[:,i],0,3) for i in range(90)])
M=np.zeros((100,180));M[:50,:90]=D;M[50:,90:]=D
ineq=np.vstack([np.column_stack([-np.eye(90),np.eye(90)]),np.column_stack([-np.eye(90),-np.eye(90)]),np.column_stack([-P,np.eye(90)]),np.column_stack([-P,-np.eye(90)])])
res=linprog(np.zeros(180),A_eq=M,b_eq=np.r_[b0,h],A_ub=ineq,b_ub=np.zeros(360),bounds=[(0,None)]*90+[(None,None)]*90,method='highs')
print('new quadratic seed feasible',res.success)
if res.success:
 print('seed216',np.round(216*res.x[:90],8).tolist())
 print('flow216',np.round(216*res.x[90:],8).tolist())
 np.savez(Path(__file__).resolve().parent/'one_angle_seed.npz',x=res.x[:90],y=res.x[90:])
