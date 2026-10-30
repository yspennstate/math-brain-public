SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B09, 2026-09-23T20:00:16Z.
attacking: the high-leverage carrier survivor by balancing the genuine spectral carrier on a literal source-coordinate cut, then retaining every nonzero residual inside the cross block rather than treating it as a small random quadratic perturbation.

# fleet01/B09 — no-marginal balanced crossing and residual-stable carrier payment

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control: revision `2026-09-22.15`  
Status: **ESSENTIAL STEP APPLIED / NEW SUPPORTING THEOREMS / FULL TARGET OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains OPEN / not proved / not disproved. Full-target continuity also remains open. This run strengthens the preceding B09 diffuse-carrier result in two ways:

1. the newly completed physical-third-volume receiver removes the row-volume-marginal gate, expanding the exact rank-four carrier branch from `q<=1/16` to every `q<1/4`;
2. a genuinely nonzero matrix residual can be retained exactly and paid by singular-value stability of the *physical cross block*, so a quantitatively small residual is no longer merely a structural certificate in this diffuse chamber.

A second top-three refinement pays examples whose full rank-four leverage equals one when that localization comes only from a weak fourth spectral mode.

## 1. Fresh sources and correction discipline


The decisive receiver is the completed fleet01/B20 theorem

`QFORM-PHYSICAL-D3-NO-MARGINAL-GATE-v1`,

source

`yspennstate/math-open-problems@8a4e6d0048174e047fc3b4ae8cabfbabba3cdc3b`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B20/20260923T165154Z-fleet01-B20-QFORM-auto11/NO_MARGINAL_D3.md`.

For any literal original-coordinate cut `I|J`, if

`Z_3=e_3(A[I,J] A[I,J]^T)>0`,

then the full ambient quadratic form has a continuous `C_0` density and

`||p_Q||_infinity <= C_3 Z_3^(-1/6)`,                           (1.1)

where

`C_3=3*2^(4/3)*exp(1/3)=10.5501688311...`.                      (1.2)

There is no row- or column-volume-marginal hypothesis; arbitrary same-side blocks, diagonals, outside coordinates and exterior couplings remain in the full form.

The newest completed designated partner result actually applied below is fleet02/B09 r19,

`QFORM-R4-CARRIER-ETA-LOCALIZATION-FORK-v1`,

source

`yspennstate/math-open-problems@8ab6f5a06544fdf25b8fc82b1792049b098a8868`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B09/20260923T190048Z-fleet02-B09-QFORM-r19/REPORT.md`.

All live corrections are retained. In particular, no pointwise one-dimensional quadratic-phase decay, no post-rotation independence, no arbitrary-joint coarea bound, no conditional-density supremum or positive-moment shortcut, no uniformly good single minor, and no claim that a small matrix is automatically a small random quadratic error is used.

## 2. Main theorem — residual-stable no-marginal balanced crossing

### Theorem `QFORM-RESIDUAL-STABLE-CARRIER-CROSSING-v1`

Let

`A = D + U K U^T + E`,                                         (2.1)

where

- `D` is diagonal in the ORIGINAL independent coordinates;
- `U in R^(n x r)` has orthonormal columns, `U^T U=I_r`, with `r>=3`;
- `K=K^T` and `s_3(K)>=a>0`;
- `E=E^T` is arbitrary, with `||E||_op<=b`.

Write the physical rows of `U` as `u_i^T` and put

`q=max_i ||u_i||_2^2`.                                         (2.2)

Assume

`r q < 1`,                                                       (2.3)

and define

`gamma=(1-sqrt(rq))/2`.                                         (2.4)

If

`beta:=gamma a-b>0`,                                            (2.5)

then for every independent real input law with scalar densities bounded by one, the full quadratic form `Q=X^TAX` has a continuous `C_0` density satisfying

`boxed:
 ||p_Q||_infinity <= C_3/beta,
 C_3=3*2^(4/3)*exp(1/3).`                                      (2.6)

Moreover for every interval `L`,

`boxed:
 P{Q in L} <= (C_3/beta)|L|.`                                  (2.7)

No sign condition is imposed on `K`, and no rank, support, moment or distributional assumption is imposed on `E` beyond the deterministic operator-norm bound in (2.1).

### Proof

A literal source-coordinate partition is enough. Let `eps_i` be iid Rademacher signs and set

`F=(1/2) sum_i eps_i u_i u_i^T`.                                (2.8)

Since `U^T U=I_r`,

`E ||F||_F^2
 = (1/4) sum_i ||u_i u_i^T||_F^2
 = (1/4) sum_i ||u_i||^4
 <= (q/4) sum_i ||u_i||^2
 = rq/4.`                                                       (2.9)

Hence some sign choice satisfies

`||F||_op <= ||F||_F <= sqrt(rq)/2`.                            (2.10)

Let `I` be the positive-sign coordinates and `J` the negative-sign coordinates. Their restricted Gram matrices are

`G_I=U_I^T U_I=I_r/2+F`,
`G_J=U_J^T U_J=I_r/2-F`,                                       (2.11)

so by (2.10)

`G_I,G_J >= gamma I_r`.                                         (2.12)

Because the physical diagonal `D` has no entries across the literal cut,

`B:=A[I,J]=B_0+E[I,J]`,
`B_0=U_I K U_J^T`.                                              (2.13)

Write

`U_I=Q_I G_I^(1/2)`, `U_J=Q_J G_J^(1/2)`                       (2.14)

with `Q_I,Q_J` orthonormal-column frames. The nonzero singular values of `B_0` are those of

`G_I^(1/2) K G_J^(1/2)`.                                       (2.15)

Therefore the singular-value min-max inequality gives

`s_3(B_0)
 >= s_min(G_I^(1/2)) s_3(K) s_min(G_J^(1/2))
 >= gamma a`.                                                    (2.16)

The residual is *not discarded*. It remains inside the actual physical cross block. Compression cannot increase operator norm, hence

`||E[I,J]||_op<=||E||_op<=b`.                                  (2.17)

Weyl's rectangular singular-value perturbation inequality now gives

`boxed: s_3(B)>=gamma a-b=beta.`                                (2.18)

Consequently

`Z_3=e_3(BB^T)
 >=s_1(B)^2 s_2(B)^2 s_3(B)^2
 >=s_3(B)^6
 >=beta^6`.                                                     (2.19)

Apply the completed no-marginal physical-third-volume receiver (1.1):

`||p_Q||_infinity
 <=C_3 Z_3^(-1/6)
 <=C_3/beta`.                                                    (2.20)

That receiver has an integrable Fourier envelope and therefore supplies the continuous `C_0` density and the direct linear interval estimate (2.7). `QED`

### Important point about the residual

Equation (2.17) is a deterministic statement about the *coefficient cross block*. At no point is `X^T E X` called small. Thus this theorem is compatible with arbitrary unbounded and fragmented cap-one source laws and does not use the invalid implication “small operator norm => small random quadratic perturbation.”

## 3. Consequences for the exact rank-three/rank-four carrier

Take `E=0`. Then `b=0`, so every carrier satisfying `rq<1` is paid:

`boxed:
 ||p_Q||_infinity
 <= {2 C_3}/[a(1-sqrt(rq))].`                                  (3.1)

For rank four this is valid for every

`q<1/4`,                                                        (3.2)

and is uniform through `s_4(K)->0` because only `s_3(K)` appears. This strictly enlarges the preceding fleet01/B09 diffuse gate `q<=1/16`; the missing row-volume-marginal condition is exactly what the new B20 receiver removes.

For the useful fixed threshold `r<=4`, `q<=1/16` gives `gamma>=1/4`, hence the sharper exact-carrier bound

`boxed:
 ||p_Q||_infinity <=4 C_3/a<42.201/a.`                          (3.3)

The previous B09 bound on this chamber was `<56/a`; (3.3) improves it while retaining the fourth direction exactly.

For rank three the corresponding threshold is simply `q<1/3`, with

`||p_Q||_infinity
 <=2C_3/[a(1-sqrt(3q))]`.                                      (3.4)

## 4. First legitimate analytic use of the r38 nonzero residual

Fleet03/B09 r38 gives, in its two-sided small-singleton-volume rank-two-cross chamber,

`A=D_0+S+E`, `rank S<=4`,                                      (4.1)

with

`||E||_op<=||E||_F<=epsilon`,                                  (4.2)

where explicitly

`epsilon=(sqrt(2)/Delta)
 [G_I/(1-q_I)+G_H/(1-q_H)]^(1/2)`,                              (4.3)

and if `s_3(A)>=1`, `||D_0||op<=tau`, then

`s_3(S)>=1-tau-epsilon`.                                        (4.4)

Let `U` be an orthonormal frame for `range(S)`, let `r=rank S in {3,4}`, and let

`q_S=max_i ||U_{i,*}||^2`.                                     (4.5)

Theorem 2 applies directly with

`a=1-tau-epsilon`, `b=epsilon`.                                (4.6)

Hence whenever

`rq_S<1`,
`gamma(1-tau-epsilon)>epsilon`,                                (4.7)

where `gamma=(1-sqrt(rq_S))/2`, the **original full matrix including the nonzero retained residual** has a continuous density with

`boxed:
 ||p_Q||_infinity
 <= C_3/[gamma(1-tau-epsilon)-epsilon].`                        (4.8)

This is the first B09 analytic payment in this chain that uses the quantitative r38 residual as an actual retained term rather than leaving it only as a structural certificate.

A simple fixed corollary is useful. If

`r<=4`, `q_S<=1/16`,
`epsilon <= (1-tau)/10`,                                       (4.9)

then `gamma>=1/4` and

`a>=(9/10)(1-tau)`, so

`gamma a-epsilon
 >=(9/40-1/10)(1-tau)
 =(1/8)(1-tau)`.                                                (4.10)

Therefore

`boxed:
 ||p_Q||_infinity
 <84.402/(1-tau),`                                             (4.11)

with continuous density and the same coefficient times interval length.

This does not solve the whole r38 chamber: high carrier leverage and residuals too large compared with the carrier remain separate.

## 5. Top-three refinement — high full leverage caused only by a weak fourth mode

The full rank-four leverage can be large solely because a weak fourth carrier direction is physically localized. It is unnecessary to balance that weak direction.

### Corollary `QFORM-TOP3-BALANCE-WEAK-FOURTH-v1`

Suppose

`A=D+W Lambda W^T+kappa z z^T+E`,                               (5.1)

where

- `W^T W=I_3`, `z` is unit and orthogonal to `range(W)`;
- `Lambda=diag(lambda_1,lambda_2,lambda_3)` with `min_j |lambda_j|>=a`;
- `q_3=max_i ||W_{i,*}||^2<1/3`;
- `||E||op<=b`.

Put

`gamma_3=(1-sqrt(3q_3))/2`.                                    (5.2)

The same Rademacher argument balances only `W`. For the resulting literal cut, the top-three cross block has third singular value at least `gamma_3 a`. The weak rank-one fourth mode satisfies

`||kappa z_I z_J^T||op
 =|kappa| ||z_I|| ||z_J||
 <=|kappa|/2`,                                                   (5.3)

because `||z_I||^2+||z_J||^2=1`. Hence the complete physical cross block obeys

`s_3(A[I,J])
 >=gamma_3 a-|kappa|/2-b.                                      (5.4)

Whenever the right side is positive,

`boxed:
 ||p_Q||infinity
 <=C_3/[gamma_3 a-|kappa|/2-b]`,                               (5.5)

with continuous `C_0` density and the corresponding linear interval bound.

Thus a highly localized *weak* fourth mode does not force promotion to a hub: the three genuinely large directions can be balanced and the weak mode can be retained exactly as a deterministic perturbation of the actual cross block.

## 6. Exact target regression outside the old full-leverage gate

Take `N=64` and let `W` be any three normalized Walsh columns in `R^64`. Every physical row has

`||W_{i,*}||^2=3/64`,                                          (6.1)

so

`gamma_3=(1-sqrt(9/64))/2=5/16`.                               (6.2)

Let

`z=(e_1-WW^T e_1)/sqrt(1-3/64)`.                               (6.3)

Then `z` is unit and orthogonal to `W`. At physical coordinate 1,

`||W_{1,*}||^2+z_1^2
 =3/64+(1-3/64)=1`.                                             (6.4)

Thus the **full four-dimensional carrier leverage equals one**, far outside the old `q<=1/16` diffuse gate and outside the partner's `q<=1/2` Fresnel gate.

For `0<=epsilon<=1/4`, define

`A_epsilon
 =W diag(1,1,-1) W^T+epsilon z z^T`.                           (6.5)

Its nonzero spectrum is exactly

`{1,1,-1,epsilon}`,                                             (6.6)

so it satisfies the owner target for every `epsilon` in the interval. Apply Corollary 5 with `a=1`, `b=0`, `|kappa|=epsilon`. From (6.2),

`s_3(A_epsilon[I,J])
 >=5/16-epsilon/2
 >=3/16`.                                                       (6.7)

Therefore for every admissible independent cap-one product law,

`boxed:
 ||p_{X^T A_epsilon X}||infinity
 <=(16/3) C_3
 =56.2675670995...<56.268,`                                    (6.8)

and

`boxed:
 P{X^T A_epsilon X in L}<56.268 |L|.`                           (6.9)

The density is continuous and vanishes at infinity. This is a genuinely overlapping high-full-leverage rank transition: the localized fourth direction shares the same physical coordinates as the large three-dimensional frame, but its small coefficient is retained rather than discarded.

## 7. Required application of the newest designated fleet02/B09 theorem

Apply fleet02/B09 r19 `QFORM-R4-CARRIER-ETA-LOCALIZATION-FORK-v1` to an explicit target-valid family.

Let `N=4096`, let `U` be the first four normalized Walsh columns in `R^N`, and let

`K=diag(1,1,-1,1/4)`,
`A=UKU^T`.                                                       (7.1)

Then the nonzero spectrum of `A` is exactly

`{1,1,-1,1/4}`,                                                 (7.2)

so the owner target holds. Every physical row of `U` has squared norm

`4/N=1/1024`.                                                    (7.3)

Take the partner theorem with `eta=1/2` and `gamma=s_3(K)=1`. Its localization alternative would require a set `H` of at most

`64 eta^(-2)=256`                                                (7.4)

physical coordinates and a unit coefficient vector `u` with

`||(Uu)_H||^2>1/2`.                                             (7.5)

But by Cauchy--Schwarz and (7.3), for every unit `u` and every such set,

`||(Uu)_H||^2
 <=|H| max_i ||U_{i,*}||^2
 <=256/1024
 =1/4`.                                                         (7.6)

So the partner's localization alternative is impossible, and its paid alternative must hold. Hence this literal target family satisfies

`boxed:
 ||p_{X^TAX}||infinity
 <=24sqrt(2e)/sqrt((1/2)(3/2))
 =48 sqrt(2e/3)
 =64.6164134606...<64.617,`                                    (7.7)

with a continuous density and

`boxed:
 P{X^TAX in L}<64.617 |L|.`                                    (7.8)

This is an equation-level use of the newest completed designated partner result, not a citation-only dependency.

## 8. Updated B09 frontier

For the exact diagonal-plus-rank-three/rank-four carrier, the diffuse branch is now larger than in the preceding run:

- rank four is paid for every full range leverage `q<1/4`, uniformly through `s_4->0`;
- rank three is paid for every range leverage `q<1/3`;
- a nonzero retained residual is paid whenever `||E||op < gamma s_3(S)`; in the r38 normalization, the explicit sufficient regime (4.9) gives `<84.402/(1-tau)`;
- even when the **full** rank-four leverage is one, the form is paid if the top-three large subspace is diffuse and the localized fourth direction is weak enough, as in Section 6.

The first unpaid implication is therefore sharpened to

`QFORM-STRONG-LARGE-SUBSPACE-LOCALIZATION-OR-NONSMALL-TAIL-v1`:

> In the remaining r38/dual-zero carrier chamber, after the residual-stable payment above, either the subspace supporting the three large carrier singular directions itself has a genuinely high physical leverage, or the fourth/residual component is large enough to prevent the physical third-crossing lower bound. Route those two cases to a literal hub/fixed-pair/grouped-square/anchored-volume exit without deleting the tail and without rotating the source variables.

This is narrower than the preceding “q>1/16” frontier: high leverage carried only by a weak extra direction is no longer an obstruction.

Full-target essential boundedness: **OPEN**.  
Full-target continuous density: **OPEN**.  
No valid counterexample was found in this run.