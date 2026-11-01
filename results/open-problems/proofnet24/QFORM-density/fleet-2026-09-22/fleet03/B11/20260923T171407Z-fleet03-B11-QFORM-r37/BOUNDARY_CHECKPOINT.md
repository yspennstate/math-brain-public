# r37 mechanism switch after source-matching duplicate

A fresh source refresh after `CHECKPOINT.md` found the same projected-crossing determinant mechanism already published more strongly by fleet02/B11 at `e54396c223673fb01a571fe84048595b684eb874` and then recognized by fleet01/B11 at `a8464073b21943a8194edac6886389139d4fdcf7`. I therefore stop claiming `(CP)`/`(CANCEL)` as new. The early checkpoint is preserved as required, but its identity is SOURCE-MATCHED DUPLICATE. The following changes mechanism on the same true-near-coloop target.

# New exact boundary theorem: one graph bank is already paid

Retain the exact-rank-three true-near-coloop state

    A=R M R^T,   R^T R=I_3,   s=min |eig M|>=1,
    r_0=sqrt(c)e, c>63/64,
    r_j=s_j e+w_j.

First use the completed designated-partner fleet04/B11 pair-area inequality. Since

    g_{0j}=||r_0 wedge r_j||^2=c||w_j||^2,

if some `||w_j||^2>=1/36`, then

    ||p_Q||_infinity
      <=128 sqrt(2)/(s sqrt(g_0j))
      <2048 sqrt(2/7)/s
      =1094.7020469.../s.                                      (1)

Thus the remaining chamber may assume every transverse leaf leverage is `<1/36`. The determinant-pair coloring argument then gives a literal original-coordinate split `S,T` with

    det G_S det G_T >17/288,
    lambda_min(G_S),lambda_min(G_T)>17/288,                     (2)

where `G_B=sum_{j in B}w_jw_j^T`.

For a bank `B`, put

    tau_B=sum_{j in B}s_j^2,
    h_B=sum_{j in B}s_j w_j,
    rho_B=tau_B-h_B^T G_B^{-1}h_B >=0.                          (3)

### Theorem `QFORM-ONEBANK-EXACT-GRAPH-DEPENDENT-PAIR-v1`

If `rho_B=0` for either selected bank `B`, then the exact-rank-three form has an essentially bounded density and

    ||p_Q||_infinity <128/s.                                    (4)

No continuity claim is made by this argument.

### Proof

Assume `rho_B=0`. Put `a_B=G_B^{-1}h_B` and let `W_B` be the row matrix with rows `w_j`. Least-squares equality gives the exact source-coordinate identity

    s_B=W_B a_B.                                                (5)

Define the two-dimensional bank projection

    Y_B=W_B^T X_B.

Then, in the deterministic spectral splitting `span(e) direct_sum e^perp`, the entire spectral contribution of bank B is

    R_B^T X_B=J_B Y_B,
    J_B y=(a_B^T y)e+y.                                         (6)

Condition on every original coordinate outside `{0} union B`. Only affine and constant terms are created. The remaining random variables are the ORIGINAL scalar `X_0` and the dependent pair `Y_B`; they are independent because their source-coordinate sets are disjoint.

The product-projection theorem gives

    ||p_{Y_B}||_infinity <=2/sqrt(det G_B)
                         <2 sqrt(288/17).                       (7)

Let

    L_B=[sqrt(c)e, J_B],
    B_B=L_B^T M L_B.                                            (8)

Thus, after conditioning, the quadratic matrix in `(X_0,Y_B)` is `B_B`; arbitrary affine terms can be removed by a deterministic translation because `B_B` is invertible. Moreover

    det B_B=c det M.                                            (9)

We need a uniform lower singular scale only to quantify the cofactor step. Since `rho_B=0`,

    a_B^T G_B a_B=tau_B <=1-c<1/64.

Together with (2),

    ||a_B||^2 < (1/64)/(17/288)=9/34.                           (10)

In the basis `(e,e^perp)`,

    L_B=[[sqrt(c), a_B^T],[0,I_2]],
    L_B^{-1}=[[1/sqrt(c),-a_B^T/sqrt(c)],[0,I_2]].

Hence

    sigma_min(L_B)^2
      >= ||L_B^{-1}||_F^{-2}
      > [ (43/34)(64/63)+2 ]^{-1}
      =1071/3518.                                               (11)

Therefore

    t_B:=sigma_min(B_B)
      >= s sigma_min(L_B)^2
      > (1071/3518)s.                                          (12)

Rotate only the two coordinates of the dependent pair `Y_B` so that the scalar-pair cross vector of `B_B` is `(beta,0)`. This orthogonal pair rotation preserves the joint density cap. Write

    B_B=[[a,beta,0],[beta,alpha,delta],[0,delta,gamma]].        (13)

Here `a=c q`, where `q=e^T M e`. In the live hard branch `|q|<1/100`, so `|a|<1/100`. Since `||(B_B)^{-1}||<=1/t_B`,

    |alpha gamma-delta^2| <= |det B_B|/t_B.                    (14)

Expanding the determinant in the first row gives

    |beta^2 gamma|
      >= |det B_B|[1-|a|/t_B]
      > |det B_B|[1-3518/107100].                              (15)

Thus

    |beta^2 gamma det B_B|
      > theta_0 |det B_B|^2,
    theta_0:=1-3518/107100>0.96715.                             (16)

Apply the completed scalar/dependent-pair theorem `QFORM-NEARNULL-SCALAR-DEPENDENT-PAIR-v1` from fleet02/B05 to the genuinely independent original scalar `X_0` and the arbitrary dependent pair `Y_B`. With (7), (9), and `|det M|>=s^3`,

    ||p_Q||_infinity
      <=31 [2 sqrt(288/17)]^(2/3)
            theta_0^(-1/6) c^(-1/3) s^(-1)
      <127.760/s
      <128/s.                                                   (17)

The estimate is uniform in the conditioned outside coordinates, so averaging preserves it. QED.

This pays the exact graph boundary `rho_B=0` without declaring any rotated coordinates independent: only the original hub scalar is independent of the entire bank projection. Combined with the fleet02/B11 projected-crossing result, the genuine interpolation survivor is now the punctured double-graph collar

    0<rho_S,rho_T <<1,

with both tending to zero allowed. The exact boundary itself is no longer the obstruction.
