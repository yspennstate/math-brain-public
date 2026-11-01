SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B03, 2026-09-23T10:47:50Z.
attacking: two-dimensional balanced-basis Fresnel compiler — aggregate the whole right-bank `(h_R,v)` product Fourier transform before spending the true left projection, aiming to upgrade the exact angular-cancellation endpoint from the critical `|t|^-1` envelope to an integrable `|t|^-3/2` envelope.

# Early substantive checkpoint


## First essential calculation

Let `r_j=(h_j,v_j) in R^2` span `R^2`. For every two-set `S={j,k}` write

`D_S=det(r_j,r_k)` and `E2=sum_S D_S^2=det([h,v]^T[h,v])`.

Let `p_S=D_S^2/E2`, and let

`delta=P_{S,T iid~p}(S cap T=emptyset)`.

Assume `delta>0`. Condition the iid pair `(S,T)` on disjointness, and let `q` be either one-set marginal. Symmetry and disjointness give every coordinate incidence marginal

`alpha_j=P_{S~q}(j in S)<=1/2`, `sum_j alpha_j=2`.

Define the determinant-entropy certificate

`Z_q=exp(H(q)+sum_S q_S log D_S^2)`.

Because `p_S=D_S^2/E2`,

`log Z_q=log E2-D_KL(q||p)`.

The conditioned joint law has

`D_KL(mu || p tensor p)=log(1/delta)`,

so data processing under `(S,T)->S` yields

`D_KL(q||p)<=log(1/delta)` and therefore

`boxed: Z_q >= E2 delta.`

Now let `Psi_j` be arbitrary twisted characteristic functions of cap-one one-dimensional laws. The newest Claude package proves for every `p>=2`

`int_R |Psi_j(s)|^p ds <=4pi/sqrt(p)`.

Apply rank-one Brascamp--Lieb in `R^2` with exponents `alpha_j`. Cauchy--Binet plus weighted AM--GM with weights `q_S` gives

`det(sum_j d_j r_j r_j^T)>=Z_q prod_j d_j^{alpha_j}`.

The Gaussian BL constant is thus at most

`Z_q^(-1/2) prod_j alpha_j^(-alpha_j/2)`.

Taking `f_j=|Psi_j|^(1/alpha_j)` and using the preceding `L^(1/alpha_j)` estimate cancels all `alpha_j` factors, yielding the translation-uniform two-dimensional product estimate

`boxed:
 int_R2 prod_j |Psi_j(h_j s+v_j eta+c_j)| ds deta
 <=16 pi^2 Z_q^(-1/2)
 <=16 pi^2 (E2 delta)^(-1/2).
}`

Zero-incidence coordinates are simply dropped using `|Psi_j|<=1`.

## Exact packet application under derivation

Return to the exact-rank-three one-sided packet already established in the preceding B03 reports,

`Q=a^(-1) H^2+2 sigma U V`,
`H=aX_i+h_L.X_L+h_R.X_R+h_K.X_K`,
`U=u.X_L`, `V=v.X_R`,
`h_R=beta v+m q`, `q perpendicular v`, `m=rho y`, `y^2>1/2`.

Condition only on the original coordinates `X_i,X_K`. The left and right banks remain genuinely independent. Fresnel-linearize the single square **before** completing away any right coordinate. For fixed left-bank value, the right-bank expectation is exactly

`prod_j psi_j(s h_R,j + 2t sigma U v_j)`.

Crucially this product is fixed independently of the left-bank realization except through the true scalar `U`; there is no illegal conditioning on a sum/difference variable and no post-rotation independence. If `||p_U||inf<=L0`, then the change `eta=2t sigma U` and the two-dimensional bound above give

`|phi_Q(t)| <= min(1,K |t|^(-3/2))`,

`K=4 pi^(3/2) L0 sqrt(|a|) / (|sigma| sqrt(E2 delta)).`

Here Cauchy--Binet gives exactly

`E2=det([h_R,v]^T[h_R,v])=m^2`.

At the exact angular-cancellation heavy row used in r29, `h_r=0`, the earlier spectral-leverage identity gives `|sigma v_r|>s_3(A)/2`, hence `|sigma|>s_3(A)/2`; the source spectral relation gives `(|sigma| rho^2/|a|)>=s_3(A)^2`, and `m=rho y`, `y^2>1/2`. Consequently

`boxed: sigma^2 m^2/|a| >= s_3(A)^3/4.`

Using the completed scalar product-projection cap `L0<=sqrt(e)`, this predicts the target-scale bound

`boxed:
 ||p_Q||inf <=12 e^(1/3) s_3(A)^(-1) delta^(-1/3)
 =16.7473491010... s_3(A)^(-1) delta^(-1/3).
}`

Because the envelope is now `L1`, this branch should have a continuous `C_0` density. The independent-copy weighted time integral should be

`int |t|^(-1/2)|phi_Q(t)|^2 dt <=(24/5)K^(1/3)`,

and the designated fleet04/B03 collision lemma will be applied to the resulting `L2` density estimate.

## Remaining check before final publication

The analytic calculation above is useful only for `delta>0`. The exact `delta=0` support has pairwise-intersecting physical two-bases (graphically: star or triangle support), while `delta->0` is a genuine near-coloop/near-three-coordinate structural collar. I will not claim the full conjecture from this estimate; the final report will state exactly that remaining structural implication and will keep full-target continuity separately open.
