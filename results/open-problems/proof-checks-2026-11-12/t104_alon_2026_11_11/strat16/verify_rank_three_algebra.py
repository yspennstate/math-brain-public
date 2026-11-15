"""Universal exact operator and canonical-chart identities for the rank-3 face."""
from sympy.polys.domains import QQ
from rank_three_target import construct


def main():
    rr,V,R,mats,controls,gs,bounds=construct();t=rr.gens[0];T=5*t
    one=rr.one;zero=rr.zero
    assert all(sum(v[a]for v in V)==0 for a in range(2))
    assert t+R[3][4]==0
    for i in range(5):
        assert sum(t+R[i][j]for j in range(5)if j!=i)==4*t-R[i][i]
    # These identities prove the root bounds from nonnegative edge weights,
    # ordered x1<=x2<=x3, and choosing ||V4||>=||V5||.
    assert R[3][3]==t*t and R[4][4]==1+rr.gens[5]**2
    xx=[V[i][0]for i in range(3)]
    assert sum(xx)==1-t
    assert -3*xx[0]==t-1+(xx[1]-xx[0])+(xx[2]-xx[0])
    assert 1-2*xx[1]==t-1+(xx[0]+1)+(xx[2]-xx[1])
    for i in range(5):assert 16-V[i][1]**2==16-4*t+V[i][0]**2+(4*t-R[i][i])
    L=[[T*(int(i==j)-QQ(1,5))-R[i][j]for j in range(5)]for i in range(5)]
    A=[[T/5+R[i][j]for j in range(5)]for i in range(5)]
    tr=sum(L[i][i]for i in range(5));tr2=sum(L[i][j]**2 for i in range(5)for j in range(5))
    massnum=tr+T;Z=massnum-2*T
    full=[]
    for c in range(3):
        F=[[zero for j in range(5)]for i in range(5)]
        for i in range(5):
            for j in range(5):
                if c==0:F[i][j]+=int(i==j)*4*(T*tr-tr2)
                if c<2:F[i][j]+=(4 if c==0 else 8)*A[i][j]**2
                F[i][j]+=int(i==j)*Z*((2*T if c==0 else (-T-2*massnum if c==1 else -2*T)))
            if c>0:F[i][i]+=(2 if c==1 else 4)*Z*L[i][i]
        if c==0:
            for i in range(5):
                for j in range(i+1,5):
                    w=4*(T/5+R[i][j])*(R[i][i]+R[j][j]-2*R[i][j])
                    F[i][i]-=w;F[j][j]-=w;F[i][j]+=w;F[j][i]+=w
        full.append(F)
    # The full original selected-u operator differs from the target by
    # J, S, DS+SD and d1^T+1d^T terms. All vanish quadratically on
    # u perpendicular to 1 with S u=0. Target additionally contains +S.
    for c in range(3):
        difference=[[zero for j in range(5)]for i in range(5)]
        for i in range(5):
            for j in range(5):
                if c<2:
                    difference[i][j]+=QQ(4,25)*T*T*(1 if c==0 else 2)
                    difference[i][j]+=2*T*(-1 if c==0 else QQ(8,5))*R[i][j]
                if c==0:
                    difference[i][j]+=4*(R[i][i]+R[j][j])*R[i][j]+QQ(4,5)*T*(R[i][i]+R[j][j])
        for i in range(4):
            for j in range(4):
                def restrict(M):return M[i][j]-M[i][4]-M[4][j]+M[4][4]
                assert restrict(full[c])-mats[c][i][j]==restrict(difference)
    for i in range(4):
        for j in range(4):
            assert controls[0][i][j]==mats[0][i][j]
            assert 10*(controls[1][i][j]-controls[0][i][j])==mats[1][i][j]
            assert 25*(controls[2][i][j]-2*controls[1][i][j]+controls[0][i][j])==mats[2][i][j]
    print('PROVED (verify_rank_three_algebra.py): universal original-operator identity, zero-edge chart normalization, root-bound identities and all three padding controls.')

if __name__=='__main__':main()
