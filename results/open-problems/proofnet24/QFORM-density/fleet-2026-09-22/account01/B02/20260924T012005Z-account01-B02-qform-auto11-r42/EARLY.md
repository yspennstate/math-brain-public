SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B02, 2026-09-24T01:20:05Z.
attacking: the live disjoint physical-cross packet E2(M)>4/9. I first spend the completed account02/B02 marginal-free E3 Fourier theorem at a literal E3 gate; on its complement I quantify exactly how low E3 collapses the crossing to either an absolute operator-norm rank-one collar or an ultra-thin rank-two tail.

# Early calculation

Let x1>=x2>=x3>=...>=0 be the squared singular values of a literal original-coordinate cross block M. Put e2=E2(M), e3=E3(M), and T=sum_{k>=3} xk.

The exact elementary inequality

x2 (e2-x1*x2) <= 2 e3

follows by writing R2=sum_{3<=k<l}xk xl:

e2-x1*x2=(x1+x2)T+R2,

e3=x1*x2*T+(x1+x2)R2+R3,

so

2e3-x2(e2-x1*x2)
 =x2(x1-x2)T+(2x1+x2)R2+2R3 >=0.

Therefore, on e2>4/9 and e3<2^-18, with tau=1/64, either

(A) x2<1/64, hence dist_op(M, rank<=1)=sqrt(x2)<1/8;

or

(B) x2>=1/64, in which case

x1*x2 > 4/9 - 2*(2^-18)/(1/64) = 4/9 - 1/2048 = 8183/18432,

and since e3>=x1*x2*T,

T < (2^-18)/(8183/18432)=9/1047424=8.5925088598e-6.

Thus in branch (B), dist_F(M,rank<=2)<sqrt(9/1047424)=0.002931299.

In branch (A), if M=M1+E with rank M1<=1 and ||E||op<1/8, then for the full symmetric block decomposition A=diag(A_LL,A_RR)+R1+E_sym, rank R1<=2 and ||E_sym||op<1/8. Since s3(A)>=1, Weyl gives s3(diag(A_LL,A_RR)+R1)>7/8. The rank-two perturbation inequality gives s3(B+R1)<=s1(B), so max(||A_LL||op,||A_RR||op)>7/8. Hence the absolute near-rank-one crossing forces a genuine same-bank curvature direction of size >7/8.

At the complementary gate E3(M)>=2^-18, account02/B02's completed marginal-free physical-E3 theorem gives ||p_Q||inf<=10.345084*8=82.760672 and integral |phi_Q| <=2*pi*82.760672=520.000638...; this branch is continuous C0.

This is only a supporting reduction. It does not discard either nonzero tail and does not claim the full QFORM target solved.
