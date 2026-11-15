"""Match the physical padding identity to the exact canonical target."""
from exact_bernstein import base,HERE
from sympy.polys.domains import QQ

def main():
    rr,t,V,R,M,delta,Q,tau,D,edges,P,C=base.construct()
    cs=[C.coeff_wrt(6,j)for j in range(3)]
    pr2=sum(P[i][j]*R[i][j]**2 for i in range(5)for j in range(5))
    pr=sum(P[i][i]*R[i][i]for i in range(5))
    # K=sum Pi_ij S_ij^2 = 4 pr2/(5 D^2 Delta).
    # h_d=sum Pi_ii degree_i, h_d-lambda=(30tDelta-2pr)/(5DDelta).
    Bn=QQ(16,5)*pr2+(D-10*t)*(QQ(12)*t*delta-QQ(4,5)*pr-4*D*delta)
    En=QQ(4,5)*(D-10*t)*(30*t*delta-2*pr)
    assert cs[2]==cs[0]/16-QQ(5,2)*Bn-QQ(5,8)*En
    assert cs[1]==8*cs[2]+10*Bn
    assert cs[0]==16*cs[2]+40*Bn+10*En
    # Hence T_N=T_inf+B/(N-2)+E/(N-2)^2, exactly. The
    # physical control construction uses precisely these three quantities.
    print('PROVED (verify_padding.py): canonical and physical all-N padding identities match coefficientwise.')
if __name__=='__main__':main()
