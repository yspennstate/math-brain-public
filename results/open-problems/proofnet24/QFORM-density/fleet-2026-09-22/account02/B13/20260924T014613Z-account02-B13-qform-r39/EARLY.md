SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B13, 2026-09-24T01:46:13.729913Z.
attacking: partner r40 four-point tau rigidity on the r38 tau-clean physical e2 crossing; force a dimension-free physical star or a low-score tau-clean bank, then retain pinned D5 on the same physical-crossing interface.

# Early calculation: tau-clean weighted 4-cycle-or-star

Programme `QFORM-DENSITY-3EIG-20260922`. Full unrestricted target remains OPEN. No moments, bounded support, connected support, log-concavity, diagonal-basis assumption, post-rotation independence, attained optimizer, or deletion of a coefficient-small random quadratic form is used.

Use account02/B13 r38: in the hard diffuse exact-rank-two chamber

`A=D+U Lambda U^T`, `U^T U=I_2`, `max_i ||u_i||^2<=1/3`,

there are a physical pivot `k`, a physical cut `C|C^c` of `[n]\\{k}`, and the good pair set

`G={E={i,j}: |tau_E|<=T rho^{-1}}`, `T<536`,

such that, with `q_E=det(U_E)^2`,

`(det Lambda)^2 X Y >= (det Lambda)^2/384`,

where

`X=sum_{E subset C, E in G} q_E`, `Y=sum_{F subset C^c, |F|=2} q_F`.

Hence `XY>=1/384`; because `sum_{|E|=2}q_E=det(U^T U)=1`, both `X,Y<=1`, so

`X>=1/384`, `Y>=1/384`.                                           (E1)

Moreover every pair `P subset C` has complement determinant

`Delta_P=sum_{F disjoint P,k}q_F >=Y>=1/384`.                     (E2)

The grouped three-leaf inequality used by partner r40 is

`Delta_P (det Lambda)^2 |tau_P| <= C_T rho^{-5}`,
`C_T=759375/2`,

while the hard branch gives

`|det Lambda|>H0 rho^{-2}`, `H0^2=1536 e^2`, `|d_k|>=1`.

Thus for every pair `P subset C`, not only the good pairs,

`|tau_P| <= L rho^{-1}`,
`L:=384 C_T/H0^2=C_T/(4e^2)=12846.2788384754...`.                 (E3)

Rotate only the deterministic latent coefficient basis so `u_k=(sqrt(c),0)` and write `u_i=(x_i,y_i)`, `s_i=y_i^2`. Partner r40 proves, for positive `s` endpoints,

`G_ij+G_lm-G_il-G_jm=-2d_k(t_i-t_m)(t_j-t_l)`,
`G_ab=tau_ab/(s_a s_b)`.

Multiplying by `s_i s_j s_l s_m` gives the denominator-free form

`tau_ij s_l s_m + tau_lm s_i s_j - tau_il s_j s_m - tau_jm s_i s_l`
` = -2 d_k s_i s_j s_l s_m (t_i-t_m)(t_j-t_l)`.                 (E4)

Let `E={i,j}` and `E'={l,m}` be vertex-disjoint good edges in `C`. The two base tau terms are at most `536 rho^{-1}`; by (E3) the two cross terms are at most `L rho^{-1}`. Since every `s_a<=||u_a||^2<=1/3`, (E4) implies

`sqrt(s_i s_j s_l s_m q_im q_jl) <= (536+L)/(9 rho)`             (E5)

after orienting the cross-difference as displayed. The four-row Pluecker identity gives

`max(q_il q_jm, q_im q_jl) >= q_ij q_lm/4`.

Choose the orientation in (E4) for the larger cross matching. With

`a_E:=q_E s_i s_j`,

we obtain for every two disjoint good edges

`sqrt(a_E a_E') <= K rho^{-1}`,
`K:=2(536+L)/9 <2974`.                                           (E6)

If an endpoint has `s=0`, then the corresponding `a_E=0` and (E6) is trivial, so (E6) is valid for all disjoint good edges.

Now normalize the good-edge weights on `C` by `p_E=q_E/X`, and write the vertex star marginals `r_v=sum_{E contains v}p_E`. Then `sum_v r_v=2`.

If `max_v r_v>=1/4`, some physical center `h` carries good q-mass at least `X/4`.

Otherwise, for independent `E,E'~p`,

`P(E intersects E') <= sum_v r_v^2 <=(max_v r_v) sum_v r_v <1/2`,

so the ordered disjoint-pair q-mass is greater than `X^2/2`. Define the low-score bank

`L0={E in G, E subset C: a_E<=K/rho}`.

By (E6), two high-score edges cannot be disjoint. Hence every disjoint ordered pair touches `L0`, and its total mass is at most `2 X sum_{E in L0}q_E`. Therefore

`sum_{E in L0}q_E >=X/4`.                                       (E7)

Combining both cases with (E1), and multiplying by the complementary pair mass `Y`, gives the physical-crossing consequence:

Either a single physical center `h` satisfies

`sum_{E subset C, E good, h in E} sum_{F subset C^c} det A[E,F]^2`
` >= (det Lambda)^2 XY/4 > e^2 rho^{-4}`,                       (E8)

or the low-score good bank satisfies

`sum_{E in L0} sum_{F subset C^c} det A[E,F]^2`
` >= (det Lambda)^2 XY/4 > e^2 rho^{-4}`.                       (E9)

Here `det A[E,F]^2=(det Lambda)^2 q_E q_F` and `(det Lambda)^2>1536 e^2 rho^{-4}`. In the low-score branch, since `q_ki=c s_i`, every contributing pair also obeys

`q_ij q_ki q_kj <= c^2 K/rho <= K/(9rho) <331/rho`.              (E10)

Thus the weighted four-cycle problem is reduced, with dimension-free constants, to a genuine physical star or a genuine physical low-score bank. The remaining analytic endpoint is to pay (E9) without dividing by an individual star determinant.

Pinned Fourier D5 remains simultaneously available for every physical cross block `B=A[I,J]`:

`s_5(B)<=5 sqrt(2e)/rho=11.658219907986.../rho`.                  (E11)

This is retained as a spectral obstruction, not as permission to discard the coefficient-small tail on rough/unbounded product laws.
