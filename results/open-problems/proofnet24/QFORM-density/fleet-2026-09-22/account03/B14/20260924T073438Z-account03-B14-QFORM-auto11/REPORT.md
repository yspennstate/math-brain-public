SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B14, 2026-09-24T07:34:38Z.
attacking: a simultaneous zero-loss canonical localization: compact connected smooth marginals, fixed median gauge, exact cap saturation and generic strict-margin matrices, with all translations retained as affine leakage.

# account03/B14 — simultaneous canonical-core localization

Run: `20260924T073438Z-account03-B14-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: translations and localization  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Full unrestricted QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.

## 1. Source state and what is new here


The ingredients are source-pinned and are not relabelled as individually new:

1. this slot's exact quantile-gauge theorem, `QFORM-QUANTILE-GAUGE-ZERO-LOSS-LOCALIZATION-v1`, at `yspennstate/math-open-problems@7b0507a694df2c6f727f4d293c92d616bb46befb`;
2. this slot's exact cap-saturation congruence theorem, `QFORM-CAP-SATURATION-CONGRUENCE-LOCALIZATION-v1`, at `yspennstate/math-open-problems@27524c090248516692abfa19911c411adaa62c23`;
3. this slot's compact/connected-support zero-loss approximation at `yspennstate/math-open-problems@46f817e053914df4ed718042194c1ff39f425e46` and the earlier cap-preserving tail-mass compactification at `a0917bc3d1bea79d37bf8e5e043ec673d3084517`;
4. account01/B15's weak-lower-semicontinuity/generic-core theorem at `yspennstate/math-open-problems@df6d00a11422f16763e8bccccc6bada6e4949a83`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B15/20260923T190251Z-account01-B15-QFORM-auto11/REPORT.md`;
5. designated partner account04/B14 r10 at `yspennstate/math-open-problems@deb713bc8e6df3f7e0ac5398e8cccbf00d1e7513`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260924T001624Z-account04-B14-scaled-schur-localization-r10/REPORT.md`;
6. account04/B15's same-constant `C_0` compiler at `yspennstate/math-open-problems@7b2b0f54db9acbd23a5f69f715178ab666e22d8e`.

A visible-corpus search for the simultaneous combination `median + connected support + exact cap saturation + generic affine core` returned no matching theorem. The new content of this run is the compatibility proof below: all of these gauges can be imposed **at once**, with the exact same optimal universal height constant, despite unbounded original supports and possibly unbounded/oscillating recentering parameters.

## 2. Height functional

For a probability measure `mu` on `R`, define

`H(mu)=sup_I mu(I)/|I|`,

where the supremum runs over bounded nonempty open intervals. As recorded in account01/B15, `H(mu)` is exactly the essential `L^infinity` density height when finite, and is weakly lower semicontinuous:

`mu_j => mu  ==>  H(mu) <= liminf_j H(mu_j)`.                    (2.1)

Let `C_full` be the extended optimal height over the exact owner target:

- arbitrary dimension;
- independent real probability densities `0<=f_i<=1`;
- real symmetric `A` with at least three eigenvalues of absolute value at least one;
- homogeneous output `X^T A X`.

Fix `p=1/2` (the proof works for any fixed `p in (0,1)`). Define `C_can` to be the corresponding supremum for **affine** outputs

`Y^T GY + b^T Y + c`                                             (2.2)

under all of the following simultaneous restrictions:

1. each marginal density `h_i` belongs to `C_c^infinity(R)`;
2. `supp(h_i)` is one finite closed interval and `h_i>0` on its interior;
3. the lower median of `h_i` is exactly zero;
4. `||h_i||_(infinity,ess)=1` exactly;
5. `G` is symmetric, has rational entries, `s_3(G)>1`, simple spectrum, every nonempty principal minor nonzero, and every off-diagonal entry nonzero;
6. `b` and `c` are arbitrary deterministic affine coefficients.

There is deliberately **no common bound** on support diameter, derivative norms, the positive bridge floor, the affine coefficients, or any moment.

## 3. Main theorem

### Theorem 3.1 — `QFORM-CANONICAL-SATURATED-MEDIAN-GENERIC-CORE-v1`

`boxed: C_can = C_full`,                                          (3.1)

including the value `+infinity`.

Thus, for the universal height problem, arbitrary source translations, arbitrarily distant fragments, arbitrary unbounded supports, marginal cap slack, algebraic matrix degeneracies, and the threshold equality `s_3=1` can all be removed **simultaneously with zero loss in the universal constant**, provided the deterministic affine term created by translation is retained.

### 3.1 Forward reduction: rough homogeneous target -> canonical affine core

Fix an arbitrary owner-target instance `(A,X)`.

#### Step A: cap-preserving compact connected smooth approximation

For one marginal `f<=1`, let

`delta_R = int_(|x|>R) f(x) dx`.

Relocate only this tail mass rather than renormalising the truncated law:

`f_R = f 1_[-R,R] + 1_[R+1,R+1+delta_R]`.

Then `f_R` is a probability density, `f_R<=1`, and

`||f_R-f||_1 <= 2 delta_R ->0`.                                  (3.2)

Mollify by a compactly supported probability kernel. The result remains a probability density bounded by one and converges in `L^1`. To fill every gap without a diameter bound, choose a smooth probability bump `q` supported on one interval containing the mollified support, positive throughout its interior, with `||q||_infinity<1`, and form

`g=(1-epsilon)g_0+epsilon q`.                                    (3.3)

Then `g in C_c^infinity`, its support is one interval, it is positive on the interval interior, `||g||_infinity<1`, and `||g-g_0||_1<=2 epsilon`. Performing this coordinatewise gives independent variables `W^(m)` with product laws converging in total variation to the original product law. No moment, centre, support radius, gap length or fragment count is used.

#### Step B: exact median gauge

For coordinate `i`, let

`r_i^(m)=q_(1/2)(W_i^(m))`

and set

`Z_i^(m)=W_i^(m)-r_i^(m)`.

The density is merely translated, hence it remains smooth, compact, connected-support and strictly subcap, while its lower median is zero. The values `r_i^(m)` need not converge and may diverge. We never estimate them.

#### Step C: exact cap saturation

Put

`k_i^(m)=||p_(Z_i^(m))||_infinity`,
`K_m=diag(k_1^(m),...,k_n^(m))`,
`Y^(m)=K_m Z^(m)`.

Since every `0<k_i^(m)<1`, the transformed density is

`h_i^(m)(y)= [k_i^(m)]^(-1) p_(Z_i^(m))(y/k_i^(m))`,              (3.4)

and therefore

`||h_i^(m)||_infinity=1` exactly.                                (3.5)

Positive scaling preserves smoothness, one-interval support, positivity on the interior and median zero.

Because

`W^(m)=r^(m)+K_m^(-1)Y^(m)`,

we have the exact samplewise identity

`(W^(m))^T A W^(m)
 = (Y^(m))^T A_m^0 Y^(m) + (b_m^0)^T Y^(m)+c_m^0`,               (3.6)

where

`A_m^0=K_m^(-1) A K_m^(-1)`,
`b_m^0=2 K_m^(-1) A r^(m)`,
`c_m^0=(r^(m))^T A r^(m)`.                                      (3.7)

No size bound on `r^(m)` is needed because (3.6) is algebraic.

The cap-saturation congruence theorem proves more than `s_3(A_m^0)>=1`: for every `t>0`, the counts of eigenvalues `>=t` and `<=-t` cannot decrease under the expansive congruence `K_m^(-1) A K_m^(-1)`, because `K_m^(-1)>=I`. Thus every `A_m^0` is still an exact owner-target matrix.

#### Step D: strict generic rational matrix without a moment assumption

At this stage the source law is compact for each fixed `m`. Let

`R_m = sup{||y||_2 : y in supp(Y^(m))}<infinity`.                 (3.8)

Choose `eta_m>0` so small that

`eta_m ||A_m^0||_op R_m^2 <= 1/m`.                               (3.9)

Then `s_3((1+eta_m)A_m^0)>=1+eta_m`. The set of symmetric matrices having simple spectrum, every principal minor nonzero and every off-diagonal entry nonzero is the complement of finitely many proper algebraic hypersurfaces, hence is open dense; rational symmetric matrices are dense. Choose a rational generic symmetric `G_m` such that

`||G_m-(1+eta_m)A_m^0||_op
 <= min{eta_m/4, 1/(m max(1,R_m^2))}`.                             (3.10)

Weyl's inequality gives `s_3(G_m)>1`. Moreover, uniformly on the compact support,

`| y^T(G_m-A_m^0)y |
 <= [eta_m||A_m^0||_op + ||G_m-(1+eta_m)A_m^0||_op] R_m^2
 <= 2/m`.                                                        (3.11)

Therefore the canonical affine random variables

`T_m=(Y^(m))^T G_mY^(m)+(b_m^0)^T Y^(m)+c_m^0`                   (3.12)

satisfy

`T_m-(W^(m))^T A W^(m) ->0` deterministically in absolute value.  (3.13)

The product laws of `W^(m)` converge to the original product law in total variation, so the pushforwards under the fixed map `x->x^T A x` also converge in total variation. Combining this with (3.13),

`law(T_m) => law(X^TAX)`.                                        (3.14)

Every `T_m` belongs to the simultaneous canonical affine class. By weak lower semicontinuity (2.1),

`H(law(X^TAX))
 <= liminf_m H(law(T_m))
 <= C_can`.                                                       (3.15)

Taking the supremum over the full target gives

`C_full <= C_can`.                                                (3.16)

The key point is the order: compactify first, then median-gauge, then saturate the exact caps, and **only then** perturb the matrix. This avoids any use of moments even if the support radii, medians or inverse caps diverge along the approximation.

### 3.2 Reverse reduction: canonical affine core -> original homogeneous target

Take one canonical affine instance

`Q=Y^T GY+b^T Y+c`, with `s_3(G)>1`.                              (3.17)

The scalar `c` only translates the output and does not change height, so omit it. Let `U~Unif[0,1]` be independent and put

`V_T=T+U`.

Define the homogeneous `(n+1)x(n+1)` symmetric matrix

`B_T = [[G, b/(2T)], [b^T/(2T), 0]]`.                            (3.18)

The perturbation of `diag(G,0)` has operator norm `||b||_2/(2T)`. Since the protected three eigenvalues of `G` lie strictly outside `[-1,1]`, Weyl's inequality implies that for all sufficiently large `T`, `B_T` has at least three eigenvalues of absolute value at least one. The new coordinate `V_T` has a cap-one density and is independent of `Y`.

Its homogeneous output is

`Q_T=(Y,V_T)^T B_T(Y,V_T)
   =Y^T GY +(V_T/T)b^T Y`.                                       (3.19)

Since `V_T/T=1+U/T ->1` uniformly,

`Q_T -> Y^T GY+b^T Y` almost surely,                             (3.20)

with no moment assumption. Hence

`H(law(Q)) <= liminf_T H(law(Q_T)) <= C_full`.                   (3.21)

Taking the supremum over the canonical affine class gives `C_can<=C_full`, which together with (3.16) proves (3.1).

## 4. Why the simultaneous theorem is stronger than the ingredients separately

The compatibility is not formal unless the operations are ordered correctly.

- Median recentering can move by an unbounded amount, so one must carry the full affine term instead of estimating the shift.
- Filling remote support gaps makes a smooth connected-support law but generally lowers the exact `L^infinity` cap below one; the diagonal congruence then restores cap exactly one without losing the spectral threshold.
- Cap saturation can make matrix entries very large when a marginal cap is tiny; matrix genericisation is therefore done **after** compactification, where an arbitrarily small perturbation can be chosen relative to the actual finite support radius. No second moment is needed.
- Genericisation alone gives no quantitative lower bound on the nonzero physical pivots/minors. This theorem therefore does not license any proof that pays an uncontrolled reciprocal pivot.
- The interval-height conclusion survives the final weak limit. Continuity is not passed through this weak-limit step by itself.

The canonical class is still large in exactly the ways that matter: interval lengths can diverge, bridge floors can tend to zero, derivative norms can diverge, and affine coefficients can diverge. Thus this reduction does not silently replace the original problem by bounded-support, log-concave, connected-extremal or moment-controlled inputs.

## 5. Designated partner applied at an actual inequality, plus a `C_0` upgrade

The completed account04/B14 r10 theorem states: if an original-coordinate `3x3` principal block `B` is invertible and

`sigma=min_j |lambda_j(B)|>0`,

then for every admissible cap-one product law, arbitrary outside curvature/couplings and arbitrary affine leakage,

`Pr{X^TAX in I} <= (6 sqrt(pi)/sigma)|I|`,                        (5.1)

so

`||p_(X^TAX)||_(infinity,ess) <= 6 sqrt(pi)/sigma`.               (5.2)

This is exactly the designated partner result at
`yspennstate/math-open-problems@deb713bc8e6df3f7e0ac5398e8cccbf00d1e7513`.

Apply it to arbitrary deterministic coordinate translations. For every `t in R^n`,

`(X+t)^T A(X+t)=X^TAX+2(At)^T X+t^TAt`.                           (5.3)

The same physical principal block `B` remains unchanged and r10 is uniform in the generated affine term. Therefore

`boxed:
 sup_(t in R^n) ||p_((X+t)^T A(X+t))||_(infinity,ess)
 <= 6 sqrt(pi)/sigma.`                                            (5.4)

This is an actual inequality, not merely a formal partner citation. It has zero support/fragment/moment/translation tax.

Now apply the completed account04/B15 same-constant regularity compiler at
`yspennstate/math-open-problems@7b2b0f54db9acbd23a5f69f715178ab666e22d8e`.
That theorem says that for any fixed rank-at-least-three product quadratic instance, an already-proved interval domination by `M|I|` has a canonical density in `C_0(R)` with the **same** height `M`. Since an invertible physical triple forces rank at least three, every translated instance in (5.4) has a representative

`p_t in C_0(R),   ||p_t||_infinity <= 6 sqrt(pi)/sigma`.          (5.5)

Thus the partner's physical-triple chamber is now translation-uniform both in height and in qualitative continuity.

For the concrete reflection block

`B_*=I_3-(2/3)11^T`, `spec(B_*)={1,1,-1}`,                        (5.6)

we have `sigma=1`. Every ambient extension

`A=[[B_*,C],[C^T,D]]`

with arbitrary `C,D` is a literal owner-target chamber by interlacing. Equations (5.4)-(5.5) give

`boxed:
 p_t in C_0(R),
 ||p_t||_infinity <= 6 sqrt(pi)=10.634723105433096...`

for every admissible product law and every deterministic translation vector `t`.   (5.7)

## 6. Continuity ledger

The simultaneous canonical-core theorem (Section 3) is fundamentally a height/interval-measure localization and its weak-limit proof **does not itself pass continuity**. That distinction is retained.

Separately, the source-pinned account04/B15 theorem proves the same-height `C_0` upgrade once an interval estimate has been paid for any fixed rank-at-least-three product quadratic instance. Therefore:

- continuity is proved with the partner constant on the physical-triple chamber (5.5);
- if a universal interval-height constant is eventually proved on the canonical class of Theorem 3.1, the equality `C_can=C_full` plus the fixed-instance compiler gives a continuous representative with the same universal height for every owner-target instance;
- this run does **not** claim the universal height theorem itself, so the unrestricted QFORM conjecture remains OPEN.

The consolidated brain `CLAIMS.json` still labels the full continuous-representative item OPEN; this worker does not rewrite owner/B20 consolidated status. The later source-pinned regularity theorem is recorded here only at its proved scope.

## 7. Remaining implication

The localization assignment is now close to exhausted at the level of source geometry: the full sharp constant is unchanged after imposing all of the canonical gauges in Theorem 3.1 simultaneously. The remaining obstruction is not tails, translations, fragmentation, cap slack or algebraic zero sets. It is the genuinely quantitative matrix/product interaction as generic physical pivots and minors approach zero or spectral mass delocalises.

A useful successor, if kept within B14, is to use the canonical class as a no-loss test bed for the live punctured-hub/near-coloop state: prove an estimate whose constant is uniform as the generic pivots tend to zero, rather than attempting any further support localization. The newest correction `QFORM-HUBSTAR-FIBERL2-MIXEDNORM-UNIVERSAL-FALSE-v1` rules out the absoluteized `int |t|^(-1/2)||G_t||_2 dt` closure even on a strict target, so the third resource must be retained jointly before absolute values or paid through an already-certified source-separated receiver.

No scheduler state, task identity, cadence, email/push setting, account permission, public visibility or cross-account authentication is changed in this run.
