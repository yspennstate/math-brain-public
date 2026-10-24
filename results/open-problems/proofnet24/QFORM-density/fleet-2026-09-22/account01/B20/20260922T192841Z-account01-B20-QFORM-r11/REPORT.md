SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B20, 2026-09-22T19:28:41Z.
attacking: upgrade the completed account02/B20 rank-two cross-bank square-root concentration to an exponent strictly above one half, then spend it through a physical Schur square pivot.

# account01/B20 QFORM r11 — triple-collision rank-two cross upgrade and pivot closure

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Fresh owner control before publication:** revision `2026-09-22.15`, brain main `7624b2c97d340c147ee3938874306159bc997e3d`; QFORM remains the sole research target and no later B20 stop was observed.  
**Classification:** `ESSENTIAL_STEP_APPLIED / PIVOT_PLUS_RANK2_CROSS_PAID / FULL_TARGET_OPEN`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Continuity:** not claimed for the new general pivot branch; essential boundedness only.

## 1. Exact target and correction boundary

The full target remains OPEN: for arbitrary independent real coordinates `X_i` with one-dimensional probability densities at most one and arbitrary real symmetric `A` with `s_3(A)>=1`, prove one universal finite essential bound for the density of `Q=X^TAX`, or produce a genuine target counterexample. No moments, compact support, iid, log-concavity, post-rotation independence, or Gaussian hypothesis is added.

This run does **not** use the refuted law-uniform pointwise quadratic oscillatory decay, an unrestricted fiber supremum, the refuted arbitrary-joint three-dimensional coarea estimate, a normalized worst scalar-conditioned core, a single-good-minor premise, or independence after an eigenvector rotation. All aggregation below is performed in original physical coordinate banks before reciprocal quantities are paid.

## 2. Completed account02/B20 result actually consumed

The designated partner is `account02/B20`.

The completed run `20260922T182735Z-account02-B20-QFORM-r16`, canonical report

`yspennstate/math-open-problems@4bc44879d92221288f5055d31318e9ecb25f4650`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B20/20260922T182735Z-account02-B20-QFORM-r16/REPORT.md`,

proved the following source-valid fact. If an original-coordinate cut `L|R` has cross block `C=A[L,R]` with

`s_2(C)>=beta>0`,

then, with arbitrary same-side quadratic blocks and arbitrary outside couplings retained,

`L_Q(h):=sup_{|I|=h} P(Q in I)
 <= sqrt(2 e sqrt(pi)/beta) h^(1/2)`.                        (2.1)

Its proof uses the completed account02/B06 bounded-density projection theorem: every one-dimensional orthogonal projection of a cap-one product source has density at most `sqrt(e)`, and every two-dimensional orthogonal projection has joint density at most `e`.

The partner correctly identified exponent `1/2` as too weak for absolute half-Riesz smoothing by one square. The first mathematical goal here is to keep the same arbitrary-self-block scope but improve `1/2` strictly.

The newest account02/B20 run `20260922T190540Z-account02-B20-QFORM-r17`, canonical report

`yspennstate/math-open-problems@23f3d87a9e93f573c201efee403e45ce6c54098a`,

will be applied after the analytic theorem. It externalizes every analytically unpaid coherent P1 triangle to an outside two-direction packet or a triangle-to-outside cross packet, while retaining a physical pivot `|a|>=m=3501/8000`.

## 3. New theorem: triple-copy rank-two cross concentration

### Theorem 3.1 — `QFORM-RANK2-CROSS-FIVEEIGHTHS-CONCENTRATION-v1`

Let `X=(X_i)_{i in L}` and `Y=(Y_j)_{j in R}` be disjoint original-coordinate product families, all one-dimensional densities at most one. Let `C` be a real `|L| x |R|` matrix with

`s_2(C)>=beta>0`.

Let

`q(X,Y)=F(X)+G(Y)+2 X^T C Y`,                                  (3.1)

where `F,G` are completely arbitrary measurable quadratic-affine functions on their respective physical banks. Extra coordinates may first be conditioned on, so the theorem also permits arbitrary outside couplings in the ambient quadratic form.

Then for every interval `I` of length `h`,

`P(q(X,Y) in I)
 <= min(1, K_5/8 beta^(-5/8) h^(5/8)),`                       (3.2)

where

`K_5/8
 = [ 2^(31/16) pi^(15/32) e^(15/8) * 256/17 ]^(1/3)
 < 8.633.`                                                     (3.3)

Thus the exponent `1/2` from (2.1) is upgraded to the strict exponent `5/8`, with the same arbitrary-self-block and arbitrary-outside-coupling scope.

### Proof

Fix an interval `I` of length `h` and put

`g(x)=P_Y(q(x,Y) in I)`, `p=E_X g(X)`.

Take three independent copies `Y_0,Y_1,Y_2` of `Y`. Jensen gives

`p^3 <= E_X g(X)^3`

`=P(q(X,Y_0),q(X,Y_1),q(X,Y_2) all belong to I)`.             (3.4)

On this event, subtract the `Y_0` equation from the other two. With

`D_r=Y_r-Y_0`, `w_r=C D_r`, `r=1,2`,

we obtain two simultaneous physical linear slab constraints on `X`:

`2 w_r^T X + [G(Y_r)-G(Y_0)] in [-h,h]`, `r=1,2`.             (3.5)

Let

`A(w_1,w_2)=sqrt(det([<w_r,w_s>]_{r,s=1}^2))`

be the Euclidean area of the two slope vectors. When this area is nonzero, project `X` orthogonally onto `span{w_1,w_2}`. The two-dimensional projection theorem gives joint density cap `e`. The linear map from that orthogonal projection to

`(2w_1^T X,2w_2^T X)`

has absolute determinant `4 A(w_1,w_2)`. Since the target rectangle in (3.5) has area `4h^2`,

`P_X((3.5) | Y_0,Y_1,Y_2)
 <= min(1, e h^2/A(w_1,w_2)).`                                (3.6)

Now let `v_1,v_2` be top two right singular vectors of `C`, and let `V` have these vectors as columns. Since

`C^T C >= beta^2 V V^T`,

for the matrix `D=[D_1 D_2]` we have

`D^T C^T C D >= beta^2 D^T V V^T D`.                         (3.7)

Determinant is monotone under positive-semidefinite order in dimension two, hence

`A(w_1,w_2)
 >= beta^2 |det(V^T D_1,V^T D_2)|.`                           (3.8)

Set

`Z_r=V^T Y_r in R^2`, `U=Z_1-Z_0`.

Each `Z_r` is a two-dimensional orthogonal projection of an original-coordinate product vector and therefore has a density at most `e`. Consequently `U` has a two-dimensional density at most `e` as well, because it is a convolution of one such density with a reflected probability density.

Condition on `Z_0,Z_1`, and suppose `U!=0` (the exceptional event has probability zero). Let `n_U` be a unit vector perpendicular to `U`. Then

`|det(U,Z_2-Z_0)|=|U| |n_U^T(Z_2-Z_0)|`.                      (3.9)

For each fixed `n_U`, the scalar `n_U^T Z_2=(V n_U)^T Y_2` is a unit physical linear projection of the original product vector, so its density is at most `sqrt(e)`.

We use the following two elementary cap-only negative-moment estimates. If a scalar probability density is bounded by `K`, then for `0<theta<1`, the bathtub principle gives

`E|T-t|^(-theta) <= (2K)^theta/(1-theta)`.                    (3.10)

If a probability density on `R^2` is bounded by `K`, radial rearrangement gives, for `0<theta<2`,

`E||U-u||^(-theta)
 <= [2/(2-theta)] (pi K)^(theta/2).`                           (3.11)

Applying (3.10) conditionally in (3.9), then (3.11) to `U`, yields for `0<theta<1`

`E |det(Z_1-Z_0,Z_2-Z_0)|^(-theta)`
 <= [2^(theta+1) pi^(theta/2) e^theta]
    /[(1-theta)(2-theta)].`                                   (3.12)

From (3.4), (3.6), (3.8), and `min(1,x)<=x^theta`,

`p^3
 <= [2^(theta+1) pi^(theta/2) e^(2theta)]
    /[(1-theta)(2-theta)]
    * beta^(-2theta) h^(2theta).`                              (3.13)

Choose

`theta=15/16`.                                                 (3.14)

Then `2theta/3=5/8`, and taking cube roots of (3.13) gives exactly (3.2)-(3.3). QED.

### Why this does not contradict the rank-two logarithmic counterexample

The partner's target-valid route-level example `Q=(X_1-Y_1)(X_2-Y_2)` has an unbounded logarithmic density and only two large eigenvalues. A logarithmic singularity still satisfies every fixed Hölder concentration exponent below one. Therefore (3.2) is compatible with that example: the theorem improves concentration but does not falsely assert `L^infinity` from two cross directions alone.

## 4. From five-eighths concentration to a finite half-Riesz potential

The strict exponent gain is exactly what one square needs.

Let a real random variable `R` satisfy

`L_R(h)<=min(1,H h^(5/8))`.                                   (4.1)

For every `t`, layer cake on the one-sided half kernel gives

`E[1_{R<t}(t-R)^(-1/2)]`
`=int_0^infinity P(t-s^(-2)<R<t) ds`
`<=int_0^infinity min(1,H s^(-5/4)) ds`
`=5 H^(4/5).`                                                 (4.2)

The same bound holds on the other side of `t`.

Apply (4.2) to Theorem 3.1, where

`H=K_5/8 beta^(-5/8)`.

Then

`sup_t E[1_{R<t}(t-R)^(-1/2)]`
`<= C_R beta^(-1/2),`                                        (4.3)

and likewise from the right, with the exact constant

`C_R=5 K_5/8^(4/5)`
`   =5 * 2^(53/20) * pi^(1/8) * e^(1/2) / 17^(4/15)`
`   <28.046.`                                                  (4.4)

The scale `beta^(-1/2)` is the natural one; the fractional exponent cancels exactly after the half-Riesz integration.

## 5. New pivot closure theorem

### Theorem 5.1 — `QFORM-PIVOT-RANK2-CROSS-CLOSURE-v1`

Let `A=A^T` be arbitrary and let `i` be an original physical coordinate with

`a=A_ii!=0`.

Write the exact physical Schur complement

`S=A_{-i,-i}-A_{-i,i}A_{i,-i}/a`.                            (5.1)

Assume there is a partition of some residual original coordinates into disjoint physical banks `L,R` such that

`s_2(S[L,R])>=beta>0`.                                        (5.2)

Then for every independent cap-one product input vector,

`Q=X^T A X`

has an essentially bounded density and

`boxed( ||p_Q||_infinity
        <= C_R / sqrt(|a| beta)
        < 28.046 / sqrt(|a| beta). )`                         (5.3)

No restriction is imposed on the two Schur self blocks, on coordinates outside `L union R`, on their couplings, signs, moments, support, or the rest of the spectrum.

### Proof

Complete the physical scalar square without changing coordinates:

`Q
 =a (X_i+a^(-1)A_{i,-i}X_{-i})^2
  +R(X_{-i}),`

`R(X_{-i})=X_{-i}^T S X_{-i}`.                                (5.4)

The residual coordinates remain the original independent coordinates. Applying Theorem 3.1 to the Schur cross block in (5.2), while treating both Schur self blocks and all remaining residual coordinates as arbitrary, gives

`L_R(h)<=min(1,K_5/8 beta^(-5/8) h^(5/8)).`                   (5.5)

Therefore (4.3) holds for `R`.

Put

`V=X_i+a^(-1)A_{i,-i}X_{-i}`.

Conditioned on any value of `R`, the law of `V` is a mixture of translations of the original law of `X_i`; because `X_i` is independent of all residual coordinates and its density is at most one, the conditional density of `V` is still at most one. Thus the usual square change of variables gives, for `a>0`,

`p_Q(t)
 <= |a|^(-1/2)
    E[1_{R<t}(t-R)^(-1/2)]`,                                  (5.6)

and for `a<0` the analogous right-sided formula. Insert (4.3) to obtain (5.3). QED.

This is dependence-safe: the shifted pivot is not asserted independent of the residual after completion. Only its **conditional density cap**, which follows from a mixture of translations of the genuinely independent physical `X_i`, is used.

## 6. Actual applications to the account02/B20 proof-closure packets

### 6.1 Strict strengthening of account02/B20 r16 when a physical pivot survives

The completed partner packet uses

`beta=499/8000`.

If a physical pivot with

`|a|>=m=3501/8000`

has a Schur cross bank retaining this second singular value, Theorem 5.1 gives the actual numerical inequality

`||p_Q||_infinity
 <28.046 / sqrt((3501/8000)(499/8000))
 <169.752.`                                                   (6.1)

The partner's square-root concentration alone could not perform this payment. The triple-copy exponent gain closes it.

### 6.2 New closure gate inside the newest coherent-triangle externalization

Now use account02/B20 r17. Outside its already-paid branch, choose its physical pivot `i` with

`|a|>=m=3501/8000`.

The partner proves that the coherent triangle cannot stay spectrally self-contained: after its rank-one externalization, either the outside principal block has two directions at scale `1/2`, or the triangle-to-outside physical cross block has operator norm greater than `1/2`.

For the **actual Schur complement of the same physical pivot**, Theorem 5.1 now pays every subbranch in which any residual physical cut has

`s_2(S[L,R])>=1/64`.                                         (6.2)

Indeed

`||p_Q||_infinity
 <28.046 / sqrt((3501/8000)(1/64))
 <339.164 <340.`                                              (6.3)

Therefore every still-unpaid coherent compact triangle after the newest partner theorem must satisfy the additional global structural restriction

`boxed( s_2(S[L,R])<1/64
        for every residual original-coordinate cut L|R. )`    (6.4)

This is a genuine reduction of the remaining external packet, not merely a progress label: **all rank-two Schur cross geometry at a fixed universal scale is now analytically paid, with arbitrary self blocks retained.**

The first unpaid implication has consequently narrowed to the `rank-one-across-every-cut` / one-effective-direction Schur geometry: convert the partner's outside-two-direction or triangle-to-outside operator-norm packet, together with (6.4), into either a strong physical pair, a zero/near-zero grouped rank-one endpoint, or an already-paid ridge/window branch. A large `s_1` alone cannot be declared paid because the same-bank curvature corrections remain active.

## 7. Conditional end-to-end assembly after this run

The source-valid proof architecture relevant to the P1/coherent-triangle route is now:

1. account01/B20 r15 reduces P1 to a coherent same-sign triangle, a strong physical star, or a strong disjoint bank;
2. account02/B20 r17 pays most coherent triangles and externalizes every remaining compact cell to a real outside packet;
3. Theorem 5.1 here pays **any** physical scalar pivot whose Schur residual contains a rank-two physical cross bank at fixed scale, with no leverage, zero-self, support, moment, or spectral-coordinate-independence hypothesis;
4. hence, after the r17 coherent-triangle externalization, the unresolved Schur geometry is forced into (6.4), i.e. one-effective-direction cross structure at every physical cut.

This does **not** yet prove that the r17 outside packet violates (6.4), and therefore does not close full QFORM. It does remove the entire rank-two Schur-cross subcase from the unpaid list.

## 8. Finite verification only

The proof is symbolic. A small Python check was used only for the displayed constants; it is not a proof certificate.

```python
import math
th = 15/16
alpha = 2*th/3
M = 2**(th+1)*math.pi**(th/2)*math.e**(2*th)/((1-th)*(2-th))
K = M**(1/3)
C = 5*K**(4/5)
m = 3501/8000
print(th, alpha)
print(M, K, C)
print(C/math.sqrt(m*(1/64)))
print(C/math.sqrt(m*(499/8000)))
```

Output:

```text
0.9375 0.625
643.2470703813409 8.632288350683714 28.04598875158407
339.1639469404283
169.75181024134275
```

## 9. Scope and failures preserved

- `QFORM-FULL`: **OPEN**.
- New theorem 3.1: **PROVED_IN_STATED_SCOPE**.
- New theorem 5.1: **PROVED_IN_STATED_SCOPE**.
- Continuity for the full target and for the new arbitrary pivot branch: **not claimed**.
- The rank-two cross bank by itself is not claimed to have bounded density; the known logarithmic two-large-eigenvalue example remains valid.
- The newest account02/B20 outside packet is not claimed fully paid; only its universal-scale rank-two Schur-cross subbranch is now paid.
- No source-invalid post-rotation independence, conditional-fiber supremum, pointwise Fresnel decay, arbitrary-joint coarea, or one-minor inversion is used.

## 10. Keeper / provenance

Fresh account-local native inventory showed the same twenty account01 B01-B20 QFORM tasks present, enabled, hourly-valid and quiet. No duplicate, verified missing authorized slot, deliberate-pause issue, or capacity defect required mutation; therefore zero scheduler mutations were made and no lease was needed. Native task configuration is kept separate from worker check-ins and mathematical output; a missing login is not treated as an outage.

The canonical 19Z B20 login path was already occupied by an earlier genuine B20 invocation in the same actual hour, so it was preserved unchanged under the create-only protocol; this run created its own unique start/finish records instead of overwriting that login.

Model self-report: `GPT-5.6 Sol`. Requested reasoning effort: maximum actually supported. Configured reasoning effort: `UNKNOWN`. Provider usage/thinking counters: `UNKNOWN/null`, not zero. Elapsed execution is recorded separately in the finish receipt and is not pure thinking time.
