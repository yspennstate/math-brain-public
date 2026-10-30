# fleet02/B16 partial — near-coloop KL barrier and source-cluster escape

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains open.

## First unpaid implication

In the exact-rank-three true near-coloop collar, a capped Pluecker-basis/Fresnel certificate cannot by itself remain uniform as the coloop defect a=1-c tends to zero. A successful compiler must use the original-coordinate hub scalar before paying the rare event of avoiding the hub, or must aggregate source directions so that a quantitative curved receiver appears.

## 1. Exact KL barrier for capped basis weights

Let R have orthonormal columns in R^3 and suppose one physical row is r_0=sqrt(c)e with 0<c<1, a=1-c. Put v_S=det(R_S)^2 on physical triples. Cauchy-Binet gives sum_S v_S=1. If E={S:0 notin S}, then

v(E)=det(I-r_0 r_0^T)=det(I-c ee^T)=a.

For any probability law w on nonsingular physical triples, the determinant-entropy score used by the capped-basis Fresnel theorem is

Z_w=exp(H(w)+sum_S w_S log v_S)=exp(-D(w||v)).

If the hub marginal obeys alpha_0=w(0 in S)<=1/2, then q=w(E)>=1/2. By data processing to the binary event E,

D(w||v)>=d(q||a)>=d(1/2||a)=-log(2 sqrt(a(1-a)))

for a<1/2. Hence

Z_w <= 2 sqrt(ac).

Thus for |det Lambda|=1 the capped-basis theorem's own right-hand side 3e Z_w^{-1/3} cannot be made uniform as a->0; its best possible certificate is at least 3e(2 sqrt(ac))^{-1/3}. This is a mechanism obstruction, not a lower bound on the true density.

## 2. Source-cluster compiler

Suppose two disjoint original-coordinate clusters C_1,C_2 have collinear spectral rows r_i=alpha_i u_nu within C_nu. Put s_nu=(sum_{i in C_nu} alpha_i^2)^{1/2}, g_nu=s_nu u_nu, and Z_nu=s_nu^{-1} sum_{i in C_nu} alpha_i X_i. Then Z_1,Z_2 are independent source objects, each has density cap <=sqrt(2), and the spectral contribution of C_nu is exactly g_nu Z_nu.

Condition on every original coordinate outside {0} union C_1 union C_2. With P=[r_0,g_1,g_2] and B=P^T Lambda P, the remaining quadratic form has quadratic matrix B plus arbitrary affine terms. If det P !=0 and b=g_2^T Lambda g_2 !=0, fleet03/B16 r27's sign-free dependent-pair/fresh-square theorem applies with H=0, gamma=1, L_X=1, L_U,L_V<=sqrt(2), yielding

||p_Q||_infinity <= 16 [ |b det Lambda| det(P)^2 ]^{-1/4}.

No spectral-projection independence is used; independence is only between disjoint original-coordinate clusters.

## 3. Fully shared Walsh family in the true near-coloop collar

Let 0<a<1/64, c=1-a, and m>=132 be divisible by four. Choose (epsilon_j,tau_j) in {+1,-1}^2 with all four sign pairs equally frequent and set

r_0=(sqrt(c),0,0),
r_j=m^{-1/2}(sqrt(a),epsilon_j,tau_j).

Then R^T R=I_3 and every residual row has all three components nonzero; its transverse leverage is 2/m<1/64. Take

Lambda=[[0,1,0],[1,0,0],[0,0,1]],

so A=R Lambda R^T has nonzero spectrum exactly {1,-1,1}. With
L=m^{-1/2}sum X_j, U=m^{-1/2}sum epsilon_j X_j, T=m^{-1/2}sum tau_j X_j,

Q=2(sqrt(c)X_0+sqrt(a)L)U+T^2.

Group the residual source coordinates by sign pair. For C_{++} and C_{+-}, their aggregate spectral vectors are

g_+=(sqrt(a),1,1)/2,  g_-=(sqrt(a),1,-1)/2.

Then det[r_0,g_+,g_-]=-sqrt(c)/2 and
b=g_-^T Lambda g_-=sqrt(a)/2+1/4>=1/4.

The source-cluster compiler therefore gives

||p_Q||_infinity <=16[(sqrt(a)/2+1/4)c/4]^{-1/4}
                 <=32 c^{-1/4}
                 <32(64/63)^{1/4}<32.127.

This family has no pure transverse residual coordinate. The escape comes from aggregating two mixed source-direction clusters before curvature is paid.

The physical-atom version loses badly: for one ++ row and one +- row, |det P_phys|^2=4c/m^2 and b_phys=(1+2sqrt(a))/m, so the same valid r27 theorem gives only

2^(11/4) m^(3/4)[c(1+2sqrt(a))]^{-1/4},

which diverges as m grows while the aggregate bound stays <32.127.
