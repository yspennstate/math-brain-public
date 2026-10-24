# B11 checkpoint — exact hub/cross 3-volume identity

Programme `QFORM-DENSITY-3EIG-20260922`; account02/B11. Full QFORM remains open.

First unpaid implication attacked: `QFORM-TRUE-NEARCOLOOP-TWOBANK-SQRT-TO-LINEAR-v1` from account03/B11 r36. Work is in exact rank three first; arbitrary additional spectrum remains separate.

Let `A=R M R^T`, `R^T R=I_3`, with `M` invertible symmetric. Choose a physical hub row `r_0=sqrt(c)e`, and a partition of the residual original coordinates into banks `S,T`. Write `r_j=s_j e+w_j`, `w_j in e^perp`, and let

`G_B=R_B^T R_B`, `Delta_B=det(sum_{j in B} w_j w_j^T)`.

Put `h=A_{0,T}` and, when `h!=0`,

`C=A_{S,T}(I-P_h)`.

A direct adjugate calculation gives the exact identity

`boxed: ||h||^2 e_2(C C^T)=det(M)^2 c Delta_S det(G_T).`        (1)

Proof sketch, to be expanded in REPORT.md: with `z=M r_0`,

`K_T=R_T^T(I-P_h)R_T=G_T-G_T z z^T G_T/(z^T G_T z)`.

For nonsingular `G_T`, `adj(K_T)=det(G_T) z z^T/(z^T G_T z)`; the singular case follows by continuity. Since `C C^T=R_S M K_T M R_S^T`, the rank-two adjugate identity gives

`e_2(C C^T)=tr(adj(K_T) adj(M G_S M))`.

Using `adj(M G_S M)=det(M)^2 M^{-1}adj(G_S)M^{-1}`, `z=M r_0`, and `r_0^T adj(G_S)r_0=c Delta_S` yields (1).

Now let `D=A_{({0} union S),T}`. The Cauchy--Binet terms containing the hub row show

`(s_1(D)s_2(D)s_3(D))^2=e_3(D D^T)>=||h||^2 e_2(CC^T).`       (2)

Therefore the exact-rank crossing theorem in `math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a`, `interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`, applies directly whenever `det(G_T)>0` and gives

`||p_Q||_inf <=6 [det(M)^2 c Delta_S det(G_T)]^(-1/6).`         (3)

No volume-row marginal assumption is used here: this is the r=3 exact-crossing part, with all same-side curvature absorbed into the arbitrary internal functions.

For the account03/B11 r36 partition, `Delta_S,Delta_T>1/32`, `c>63/64`. If `tau_T` is the longitudinal Schur variance of bank T, then `det(G_T)=Delta_T tau_T`, so with `s=min|eig M|`,

`||p_Q||_inf <19.099 s^(-1) tau_T^(-1/6).`                    (4)

Reversing S,T gives the same estimate with `tau_S`. Thus the fresh crossing theorem pays every quantitatively non-graph bank state. The genuinely unpaid endpoint is the double graph collar `tau_S,tau_T ->0`; (1) shows exactly why the projected-crossing currency vanishes there.

Next in this run: analyze the exact double-graph endpoint and construct a target-valid family showing that vanishing projected crossing is a proof-strategy obstruction rather than a QFORM counterexample; retain the rank-two logarithmic endpoint and exhibit the third-direction smoothing mechanism.
