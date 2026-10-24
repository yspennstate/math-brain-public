from explore import *
def unitary_row(Q,theta,phi):
 ans=Q.copy();c=np.cos(theta);s=np.sin(theta);e=np.exp(1j*phi)
 ans[0]=c*Q[0]+s*e*Q[3];ans[3]=-s*e.conjugate()*Q[0]+c*Q[3]
 return ans
b1=contrast(unitary_row(F,np.pi/2,0));bc=(b0+b1)/2; H=(b0-b1)/2
G=contrast(unitary_row(F,np.pi/4,0))-bc
J=(contrast(unitary_row(F,np.pi/4,np.pi/2))-bc)/np.sqrt(3)
print('H*72',np.round(H*72,8).tolist())
print('G*72',np.round(G*72,8).tolist())
print('J*72',np.round(J*72,8).tolist())
for x,z in [(2,0),(-2,0),(0,2),(0,-2)]:
 for y in [-1,1]:
  b=bc+x*H+y*G+z*J
  res=linprog(np.zeros(90),A_eq=D,b_eq=b,bounds=(0,None),method='highs')
  print('vertex',x,y,z,'feasible',res.success,'min_atom',min(np.r_[b[:15],-b[15:35],b[35:]]))
