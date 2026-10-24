SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B11, 2026-09-23T05:13:56Z.
attacking: whether the balanced-sign pair-PSD survivor from B11 r23 can force a fixed-scale eight-coordinate packet; test the implication before trying to invert local minors.

# Early substantive checkpoint — balanced three-bank obstruction

Let m>5 and split 3m ORIGINAL coordinates into three disjoint banks G1,G2,G3 of size m. Define a block-constant symmetric matrix A_m by diagonal and within-bank entries 1, and cross-bank entries

rho_12=1-5/m,   rho_13=rho_23=1-1/(10m).

All physical 2x2 principal blocks are PSD and every nonzero physical edge has positive sign. On the normalized bank-constant vectors e_g=1_{G_g}/sqrt(m), the only nonzero part is

B_m = [[m,m-5,m-1/10],
       [m-5,m,m-1/10],
       [m-1/10,m-1/10,m]].

The vector (1,-1,0) has eigenvalue 5. On the complementary symmetric two-plane the trace is T=3m-5 and determinant D=-(23/5)m-1/50. Hence det B_m=-(230m+1)/10<0. If p(lambda)=lambda^2-T lambda+D, then

p(-3/2)=-(10m+527)/100<0,

so the negative eigenvalue is < -3/2; the other is positive. Thus A_m has exact rank three, signature (2,1), and all three nonzero eigenvalues have absolute value >1.

However every 2x2 submatrix C of the normalized physical coefficient matrix differs from the rank-one all-ones matrix J_2 entrywise by at most 5/m, so

s_2(C) <= ||C-J_2||_op <= ||C-J_2||_F <= 10/m.

Therefore for every fixed c>0, choosing m>10/c destroys the child condition s_2(C),s_2(D)>=c in the B11-r23 eight-coordinate packet theorem, even though the exact target spectral hypothesis and the balanced pair-PSD chamber hold. This is a source-valid obstruction to a fixed-scale LOCAL packet extraction, not a counterexample to QFORM.

The family is nevertheless product-aggregable. Put Y_g=m^{-1/2} sum_{i in G_g} X_i. The Y_g are independent because the banks are disjoint, and each has density cap <=sqrt(2). Then Q=Y^T B_m Y. Setting Z_g=sqrt(2)Y_g gives independent cap-one Z_g and Q=(1/2)Z^T B_m Z. Since the smallest absolute eigenvalue of B_m is >3/2, the three-variable finite-dimensional theorem gives

||p_Q||_infinity <= 6sqrt(pi)/(3/4)=8sqrt(pi).

So the correct operation in this survivor is aggregation BEFORE local packet inversion.

Next: write the exact checker; splice the designated account04/B11 sign-frustrated triangle theorem into the companion bank-sign branch to show that flipping the bank-sign product to -1 immediately restores a local physical triple bound, thereby isolating balanced sign as the genuine obstruction.
