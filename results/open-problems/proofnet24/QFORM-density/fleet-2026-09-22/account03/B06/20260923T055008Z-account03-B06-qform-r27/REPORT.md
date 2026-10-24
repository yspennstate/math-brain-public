SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B06, 2026-09-23T05:50:08Z.
attacking: rank-two-tube stability via a mixed-order aggregate-curvature L3 receiver, followed by a dependence-safe original-coordinate square.

# account03/B06 r27 — mixed-order curved-fiber L3 compiler and 9/10 occupancy squeeze

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** revision `2026-09-22.15`  
**Assignment:** Curved fiber integration  
**Classification:** `NEW SUPPORTING THEOREM + LIVE PACKET APPLICATION / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and first missing implication

The unrestricted target remains: for every dimension, independent ORIGINAL real coordinates with one-dimensional probability densities bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal essential-density bound for `Q=X^T A X`, or give a valid counterexample. No Gaussian, moment, compact-support, connected-support, log-concavity, iid, or diagonal-basis hypothesis is added. A general rotation is never used to manufacture independent spectral coordinates.

The preceding B06 run proved a leverage-free aggregate third-volume `L3` receiver and spent it through a genuine original-coordinate square. The remaining low-third-volume / near-rank-two chamber still needs a stability mechanism which retains the nonzero tail and aggregates physical curvature before any reciprocal payment.

This run proves such a transducer for **mixed physical minor orders**. It weakens the integrability threshold in the newest mixed-order Jensen compiler from direct `L1` Fourier inversion to exactly the threshold needed for an `L3` residual. A completed dependence-safe square then upgrades that residual to `L_infinity`. The gain is concrete: in the live anchored order-3/order-2 packet, the admissible residual occupancy threshold moves from `<5/8` for direct continuous inversion to `<15/16` before the outer square. A clean finite collar at `9/10` is paid explicitly.

Consumed corrections include: law-uniform pointwise quadratic-phase decay is false; arbitrary-joint rank-three coarea is false; positive conditional projection-density moments are false; post-rotation independence is false; unrestricted fiber suprema lose dimension; aggregate determinant mass need not contain one universally large physical minor/row; and a small nonzero cross tail may not be discarded.

## 2. Source-valid inputs

### 2.1 Mixed-order Jensen compiler before inversion

The fresh account03/B08 proof

`yspennstate/math-open-problems@211405a8dcc939a517ac0b9b0a8995707d6bb388`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T052144Z-account03-B08-qform-diffuse-r28/REPORT.md`,

proves the following pre-inversion estimate. Let `M` be a physical cross block between disjoint ORIGINAL-coordinate banks. Let `Omega` be a probability law on nonzero square physical minors `(S,T)` of possibly varying orders `k>=1`. Put

`alpha_i=P_Omega(i in S)`, `beta_j=P_Omega(j in T)`,
`kbar=E_Omega k=sum_i alpha_i=sum_j beta_j`,

and

`K(Omega)=exp(E_Omega log det(M_ST)^2 + H(Omega)).`

For `q>=1` define

`H_q(c)=q^(q/2-c)(q-c)^(-(q-c)/2)`, `H_q(0)=1`,

`B_beta=prod_j (1-beta_j)^(-(1-beta_j)/2)`,

and

`G_q(Omega)=B_beta prod_i H_q(alpha_i).`

If `alpha_i<=q/2` for all rows, the proof gives, **before** imposing the direct-inversion condition `kbar>2q`,

`|phi_R(t)| <= min(1,(T/|t|)^a)`,                                    (2.1)

where

`a=kbar/(2q)`,

`T=pi G_q(Omega)^(1/kbar) K(Omega)^(-1/(2kbar)).`                    (2.2)

The source's continuous-density theorem then assumes `a>1`. The present run does not reuse that final step; it integrates only the `3/2` power of (2.1), which has a strictly weaker threshold.

The same source proves the coarse dimension-free factor

`G_q(Omega)^(1/kbar) <= e q^(-1/2).`                                  (2.3)

All same-bank quadratic terms, affine terms, outside couplings and extra cross directions remain inside the original-coordinate argument.

### 2.2 Dependence-safe square kernel from account04

The completed account04/B18 theorem

`QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`,
`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`,

proves in its square-completion argument that for a genuine ORIGINAL-coordinate pivot `a!=0`, after disintegration one has the pointwise domination

`p_Q(t) <= |a|^(-1/2) int_0^infinity p_R(t-sgn(a)u) u^(-1/2) du.`      (2.4)

No independence between `R` and the translated square variable is assumed.

The designated exact partner `account04/B06` still has no completed current-QFORM canonical handoff at the fresh lookup, so no partner theorem is invented. The compatible completed account04/B18 result is applied to the actual inequality (2.4).

## 3. New mixed-order L3 compiler

### Theorem 3.1 — `QFORM-MIXED-ORDER-L3-COMPILER-v1`

Use the setup of Section 2.1. Assume

`q>=1`,
`alpha_i<=q/2` for every row,
`kbar>4q/3`.                                                           (3.1)

Then the full residual form `R` has an `L3` density satisfying

`boxed:
 ||p_R||_3
 <= 3^(1/6) 2^(-1/3)
    [3kbar/(3kbar-4q)]^(2/3)
    G_q(Omega)^(2/(3kbar))
    K(Omega)^(-1/(3kbar)).
`                                                                        (3.2)

In particular, using (2.3),

`boxed:
 ||p_R||_3
 <= 3^(1/6) 2^(-1/3) e^(2/3) q^(-1/3)
    [3kbar/(3kbar-4q)]^(2/3)
    K(Omega)^(-1/(3kbar)).
`                                                                        (3.3)

#### Proof

From (2.1), set `a0=kbar/(2q)`. Condition (3.1) is exactly

`3a0/2>1`.

Hence

`int_R |phi_R(t)|^(3/2) dt
 <=2T[1+int_1^infinity s^(-3a0/2) ds]
 =2T [3a0/(3a0-2)]
 =2T [3kbar/(3kbar-4q)].`                                              (3.4)

With Fourier convention `hat f(t)=int exp(itx)f(x)dx`, sharp inverse Hausdorff--Young at exponents `(3/2,3)` gives

`||p_R||_3
 <= [3^(1/6)/(2 pi^(2/3))]
    ||phi_R||_(3/2).`                                                   (3.5)

Substituting (3.4) and (2.2) into (3.5) gives (3.2). Equation (3.3) follows from (2.3). Since the characteristic transform belongs to `L^(3/2)`, inverse Hausdorff--Young produces an `L3` density representing the original probability measure. QED.

### Why this is genuinely weaker than direct inversion

The continuous mixed-order theorem requires `kbar>2q`. The new theorem only requires

`kbar>4q/3`.

That difference is not cosmetic: an outer original-coordinate square only needs enough fractional regularity to control a half-Riesz potential. It does not need the residual characteristic function in `L1`.

## 4. Spend the L3 residual through the completed account04 square inequality

For any probability density `p` with `||p||_3=M`, split the half-Riesz integral at `U>0`:

`int_0^U p(t-u)u^(-1/2)du
 <= M (int_0^U u^(-3/4)du)^(2/3)
 =2^(4/3) M U^(1/6),`

while

`int_U^infinity p(t-u)u^(-1/2)du <= U^(-1/2).`

Optimizing in `U` gives

`sup_t int_0^infinity p(t-u)u^(-1/2)du
 <= [8/3^(3/4)] M^(3/4).`                                             (4.1)

Applying (4.1) to the actual account04/B18 domination (2.4) and then Theorem 3.1 gives:

### Theorem 4.1 — `QFORM-MIXED-ORDER-OUTER-SQUARE-v1`

Under the hypotheses of Theorem 3.1 and a genuine original-coordinate square pivot `a!=0`, the final quadratic form has an essentially bounded density with

`boxed:
 ||p_Q||_infinity
 <= 2^(11/4) 3^(-5/8)
    [3kbar/(3kbar-4q)]^(1/2)
    G_q(Omega)^(1/(2kbar))
    K(Omega)^(-1/(4kbar))
    |a|^(-1/2).
`                                                                        (4.2)

Using the coarse factor (2.3),

`boxed:
 ||p_Q||_infinity
 <= 2^(11/4) 3^(-5/8) e^(1/2) q^(-1/4)
    [3kbar/(3kbar-4q)]^(1/2)
    K(Omega)^(-1/(4kbar))
    |a|^(-1/2).
`                                                                        (4.3)

This conclusion is essential boundedness. The proof does **not** establish a continuous final representative: the residual is only placed in `L3`, and the last step is a half-Riesz domination.

## 5. Live application: the anchored order-3/order-2 packet now survives occupancy up to 15/16

The same account03/B08 r28 source starts from an anchored third-volume packet

`Z=sum_(R,C) det B[{i} union R,{a0} union C]^2>0`,

with normalized order-three law `w3`. For residual rows let

`alpha_k=P_w3(k in R)`, `sum_(k!=i)alpha_k=2`,
`h=max_(k!=i) alpha_k`,

and let `R_i` denote its row-star norm. The source constructs an order-two law `v2*` with the **same residual-row marginals** and forms

`Omega=(w3+v2*)/2`,

for which

`kbar=5/2`,
`K(Omega)>=2Z/R_i`,
`anchor-row marginal=1/2`,
`residual-row marginals=alpha_k`.                                      (5.1)

To satisfy the row Hausdorff--Young gates, take

`q=max(1,2h).`                                                         (5.2)

The direct continuous compiler required `q<5/4`, i.e. `h<5/8`. Theorem 3.1 requires only

`5/2 > 4q/3`,

so every

`boxed(h<15/16)`                                                       (5.3)

is analytically admissible before the outer square. Thus the mixed-order packet can be far more concentrated on one residual row than direct `L1` inversion allows, yet the original product structure still produces enough fractional integrability for the square smoother.

## 6. Concrete 9/10 collar and a sharper nested-packet router

Use the live B08 diffuse packet scale from the same source:

`Z>L^6/6912`,
`R_i<=L`.                                                              (6.1)

In a B06 branch where this packet belongs to the residual cross block after completing a genuine original-coordinate square with coefficient `a!=0`, suppose

`h<=9/10`.

Choose `q=9/5`. Then

`3kbar/(3kbar-4q)=25`,

and (4.3), (5.1), (6.1) give

`||p_Q||_infinity
 <= C_* |a|^(-1/2) (2Z/R_i)^(-1/10)
 < C_* 3456^(1/10) / sqrt(|a|L),`

where

`C_*=2^(11/4)3^(-5/8)e^(1/2)(9/5)^(-1/4)*5
    =24.0952159461...`.

Therefore

`boxed:
 h<=9/10
 => ||p_Q||_infinity <54.424/sqrt(|a|L).
`                                                                        (6.2)

Conversely, within the packet hypotheses (6.1), failure of this occupancy gate forces some residual row to carry more than `9/10` of the **aggregate** anchored third-volume law. Hence the nested packet on that row has mass

`> (9/10) Z > L^6/7680.`                                               (6.3)

This is an aggregate statement only. It does not infer a single large local determinant, so it respects the live co-heavy/single-row extraction correction. Transposition gives the identical column statement.

The practical B06 dichotomy is therefore:

* either the mixed order-3/order-2 curved packet is paid through the actual outer square by (6.2); or
* a residual physical row (and analogously a column when the corresponding orientation is invoked) carries `>90%` of the anchored determinant law, leaving an explicit near-coloop/nested-bank structure for the next grouped-coordinate step.

If additionally `|a|L>=eta>0`, the paid branch becomes the universal bound `54.424/sqrt(eta)`.

## 7. What changed and what remains unpaid

The substantive gain is the threshold relaxation

`direct continuous Fourier inversion: kbar>2q`

versus

`L3 residual + dependence-safe square: kbar>4q/3`.

For the live `kbar=5/2` packet this moves the maximal payable residual occupancy from `<5/8` to `<15/16`. The finite `9/10` collar gives an explicit constant and strengthens the nested aggregate from the neighboring `<317/L` router's `>3/5` occupancy to `>9/10` in the genuine-outer-square branch.

This does **not** solve the zero or arbitrarily small scalar-pivot branch: the bound still contains `|a|^(-1/2)`. It also does not allow a nonzero higher-rank tail to be deleted. The next exact B06 implication is therefore

`QFORM-NEARZERO-PIVOT-DOUBLE-NESTED-PRODUCT-PAYMENT-v1`:

in the surviving `>9/10` row/column nested packet or a near-zero scalar pivot, use a grouped original-coordinate pair/ridge window to pay the determinant law before any reciprocal local minor is selected, while retaining the full complementary spectrum. A successful step should either produce a dimension-free lower bound on the product `|a|L`, or replace the scalar square by a dependence-safe grouped smoother which remains valid at `a=0`.

## 8. Status

* `QFORM-MIXED-ORDER-L3-COMPILER-v1`: proved here from the source-valid pre-inversion mixed-order estimate.
* `QFORM-MIXED-ORDER-OUTER-SQUARE-v1`: proved here, with the completed account04/B18 square inequality applied to the actual derivation.
* Anchored `9/10` packet branch: paid by `<54.424/sqrt(|a|L)`; failure yields nested aggregate `>L^6/7680`.
* Full QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
* Universal continuity conclusion: **OPEN**; this branch proves essential boundedness only after the outer square.
