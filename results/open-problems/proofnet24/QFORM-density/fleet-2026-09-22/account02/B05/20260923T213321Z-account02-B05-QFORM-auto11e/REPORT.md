SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B05, 2026-09-23T21:33:21Z.
attacking: QFORM-TWOBANK-HUB-PUNCTURED-COUPLING-v1 — replace the power loss as the overlapping coupling b tends to zero by a product-sensitive logarithmic bridge, then isolate the genuinely uniform critical-window endpoint.

# account02/B05 — logarithmic punctured-coupling bridge

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**OWNER CONTROL:** revision `2026-09-22.15`; actual invocation began from fresh `math-research-brain@5acc3c1a42fa387c15be82c742273af3929751de`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Status:** `PROVED_SUPPORTING_THEOREM / POWER LOSS REDUCED TO LOGARITHM / FULL QFORM OPEN`.  
**Regularity:** essential boundedness is proved in the stated scope; continuity is not claimed.

## 1. First unpaid implication

The preceding B05 theorem combined an independent scalar hub with the two-bank curved tube estimate and obtained a full-line bound deteriorating like `|b|^(-1/3)` for

`Q = 2HL + 2bLP + V^2 + alpha L^2 + beta L + gamma0`,

where `H` is a genuinely independent original-coordinate/product-bank scalar and `(L,V,P)` is supplied by two disjoint product banks. The exact endpoint `b=0` is separately paid by `QFORM-NULL-HUB-TRANSVERSE-SQUARE-v1`, so the open issue is punctured stability as `b -> 0`, not existence of a bound for each fixed `b`.

This run proves that once the honest one-dimensional density cap of `L` is retained, the `|b|^(-1/3)` loss is unnecessary. The deterioration is only logarithmic. Away from the quadratic critical value it is only square-root logarithmic after optimization.

The first unpaid implication after this run is therefore

`QFORM-TWOBANK-HUB-CRITICAL-PUNCTURED-UNIFORM-v1`:

remove the remaining logarithm uniformly through `b -> 0` in the critical output window, while retaining the two-bank/original-product provenance and taking no arbitrary curved-fiber supremum. The exact `b=0` endpoint, every fixed `b != 0`, and the diffuse `|b|>=1` spectral chamber are already paid.

## 2. Input theorem: the fresh two-bank curved tube

The compatible source is

`math-open-problems@5e23223ed8626d8df8343d2d26879c08cf139093:`
`proofnet24/QFORM-density/interactive/20260923T202245Z-two-bank-curved-tube/REPORT.md`.

Let `A=(L_A,V_A,P_A)` and `B=(L_B,V_B,P_B)` be independent three-dimensional product-bank projections, with `(L,V)` marginal caps `M_{2,A},M_{2,B}` and joint caps `M_{3,A},M_{3,B}`. Put

`(L,V,P)=A+B`,
`K_2=(M_{2,A}M_{2,B})^(1/2)`,
`K_3=(M_{3,A}M_{3,B})^(1/2)`,
`K=K_2+K_3`.

For `b != 0`, arbitrary `c,d,gamma`, and `0<r<=1`, the source proves

`P(r<=|L|<=2r, |bP+c+dL+(gamma+V^2)/(2L)|<=a)`
`    <= C_T a r^(3/2) |b|^(-1/2) K`.                                 (2.1)

If `|gamma|>=1`, it proves for every `r>0`

`P(tube) <= C_T a r^2 [K_2{1+log_+(1/(|b|r))}+K_3]`.                 (2.2)

The arbitrary affine shear `dL` is already included. This matters because the stronger shear-uniform `O(ar^2)` statement without the logarithm is false.

## 3. New theorem: logarithmic punctured bridge

### Theorem 3.1 — `QFORM-TWOBANK-HUB-LOG-PUNCTURED-v1`

Assume the hypotheses above. In addition assume the total scalar `L` has an honest density satisfying

`||p_L||_infinity <= M_L`.                                            (3.1)

Let `H` be independent of both banks with

`||f_H||_infinity <= m`.                                              (3.2)

For `b != 0`, arbitrary real affine/shear parameters, and `|lambda|>=1`, let

`Q = 2HL + 2bLP + lambda(V+sL+v0)^2 + alpha L^2 + beta L + gamma0`.    (3.3)

Put

`A_0 = C_T K/4`, `B_0=m M_L`.                                        (3.4)

Then for every interval `I` and every `0<R<=1`,

`P(Q in I) <= |I| { m/(2R)`
` + B_0 [2+sqrt(2)+log_2^+(A_0^2 R/(|b|B_0^2))] }`.                  (3.5)

Consequently

`boxed{ ||p_Q||_(infinity,ess) <= inf_{0<R<=1} [ m/(2R)`
` + mM_L {2+sqrt(2)+log_2^+( C_T^2 K^2 R/(16 |b| m^2 M_L^2) )} ]. }` (3.6)

In particular, with the unoptimized choice `R=1`,

`||p_Q||_(infinity,ess)`
` <= m/2 + mM_L [2+sqrt(2)+log_2^+( C_T^2 K^2/(16 |b|m^2M_L^2))].`    (3.7)

Thus, for fixed product-bank density currencies, the punctured loss is `O(log(1/|b|))` as `b -> 0`, rather than the predecessor's `O(|b|^(-1/3))`.

For a literal cap-one original-coordinate hub and a normalized product linear form `L`, one may take `m<=1`, `M_L<=sqrt(2)`. Then

`boxed{ ||p_Q||_(infinity,ess)`
` <= 1/2 + sqrt(2)[2+sqrt(2)+log_2^+(C_T^2 K^2/(32|b|))]. }`          (3.8)

### Proof

Let `h=|I|` and let `t` be the centre of `I`.

#### Step 1. Small-shell curved estimate

Fix `0<r<=1` and restrict to

`S_r={r<=|L|<=2r}`.

Condition only on the genuinely independent hub `H`. For each fixed hub value, divide the event `|Q-t|<=h/2` by `2L`. The hub contributes only an arbitrary constant to the centre; all `L^2`, linear, translated-square and shear terms are of the exact type allowed in (2.1). The width after division is at most `h/(4r)`. Hence

`P(Q in I, S_r) <= (C_T K/4) h sqrt(r/|b|)`
`                   = A_0 h sqrt(r/|b|).`                            (3.9)

No conditional density of `(L,V,P)` is asserted: independence of the disjoint hub means its conditioning leaves the two-bank law unchanged.

#### Step 2. The plateau bound from the honest `L` marginal

Condition instead on both product banks. Since `Q` is affine in `H` with slope `2L`,

`P(Q in I | banks) <= m h/(2|L|)`.                                   (3.10)

On `S_r`, this is at most `mh/(2r)`. The true one-dimensional marginal cap gives

`P(S_r) <= 2 M_L r`,                                                  (3.11)

because the two sign components have total Lebesgue length `2r`. Therefore

`P(Q in I,S_r) <= mM_L h = B_0 h`.                                  (3.12)

Combining (3.9) and (3.12),

`P(Q in I,S_r) <= h min{A_0 sqrt(r/|b|), B_0}.`                       (3.13)

This is the new point. The previous proof summed (3.9) until an optimized large-`L` cutoff and paid a power of `|b|`. The marginal cap (3.11) inserts a scale-independent plateau before that optimization.

#### Step 3. Dyadic summation below `R`

Take the disjoint shells

`r_k = R 2^(-k-1)`, `k=0,1,...`,                                    (3.14)

which cover `0<|L|<=R`. Since `R<=1`, every shell lies in the range of (2.1). Set

`x = A_0^2 R/(|b|B_0^2)`.                                            (3.15)

Then (3.13) gives

`P(Q in I,0<|L|<=R)`
` <= B_0 h sum_{k>=0} min{1,sqrt(x 2^(-k-1))}.`                       (3.16)

The elementary dyadic estimate

`sum_{k>=0} min{1,sqrt(x 2^(-k-1))}`
` <= 2+sqrt(2)+log_2^+ x`                                            (3.17)

holds for every `x>0`: for `x<=1` the entire sum is at most `(1+sqrt(2))sqrt(x)`; for `x>1`, at most `floor(log_2 x)` terms equal one and the remaining geometric tail is at most `2+sqrt(2)`.

#### Step 4. Large `|L|`

From (3.10), directly

`P(Q in I,|L|>R) <= m h/(2R)`.                                       (3.18)

Adding (3.16)-(3.18) proves (3.5). A uniform interval inequality implies absolute continuity and the essential density bound (3.6). QED.

### Remarks on provenance

1. The proof never declares any post-rotation variables independent. The only independence used is the genuine disjoint-bank independence of `H` from the two banks.
2. The proof never takes an unrestricted curved-fiber supremum. The curved estimate is the source's two-bank oscillatory tube theorem, then it is summed against the actual `L` marginal.
3. There is no interval-to-Borel promotion. The conclusion sought here is itself an interval inequality, sufficient for essential boundedness.
4. No step treats `bP` as a small random error. Its coefficient enters the exact tube estimate and remains visible as `log(1/|b|)`.
5. The theorem is stable under the displayed deterministic affine shear and translated transverse square. No probabilistic independence is attributed to that change of coordinates.

## 4. Noncritical levels: square-root logarithmic loss

The stronger source estimate (2.2) improves the same calculation away from the quadratic critical value. In the normalization (3.3), fix an output point `t` for which the constant numerator after division satisfies

`|gamma0-t|>=1`                                                       (4.1)

(after the harmless affine normalization implicit in the source theorem). On `S_r`, (2.2) with width `h/(4r)` gives

`P(Q in I,S_r)`
` <= (C_T/4) h r [K_2{1+log_+(1/(|b|r))}+K_3]`.                      (4.2)

Summing `r_k=R2^(-k-1)` gives

`sum r_k = R`,
`sum r_k log_+(1/(|b|r_k))`
` <= R [log_+(1/(|b|R))+2 log 2]`.                                   (4.3)

Combining with the large-`L` hub estimate yields, for such `t`,

`boxed{ p_Q(t) <= inf_{R>0} { (C_T/4)R`
` [K_2{1+2log2+log_+(1/(|b|R))}+K_3] + m/(2R) }. }`                  (4.4)

As `b->0`, choosing `R` of order `1/sqrt(log(1/|b|))` gives only `O(sqrt(log(1/|b|)))` deterioration. Thus the hard transition is further localized to the bounded critical convex/two-sheet output window.

## 5. Required pinned `e5f71d79...` theorem applied to the punctured core

The required source

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:`
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`

was read through `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

Its Theorem F gives the exact-rank-three Fresnel–Brascamp–Lieb estimate. Here it applies to a real punctured-coupling core, not merely as a generic gate.

Suppose `H` is the literal original-coordinate form with coefficient vector `e_h`, while `P,L,V` have orthonormal coefficient vectors `p,ell,v` supported off `h`. Consider

`Q_b = 2HL + 2bLP + lambda(V+sL)^2 + alpha L^2 + affine`,             (5.1)

with `|lambda|>=1`. Put

`c=sqrt(1+b^2)`,
`w=(e_h+b p)/c`.                                                      (5.2)

Then `w,ell,v` are orthonormal and the quadratic part on their span has matrix

`M_b = [[0,c,0],`
`       [c,alpha+lambda s^2,lambda s],`
`       [0,lambda s,lambda]]`,                                       (5.3)

so

`det M_b = -(1+b^2)lambda`.                                          (5.4)

The active-subspace leverage of the hub row is

`rho_h=1/(1+b^2)`.                                                    (5.5)

For each residual original coordinate `j`,

`rho_j = (b^2/(1+b^2)) p_j^2 + ell_j^2+v_j^2`.                       (5.6)

Therefore, if the residual original three-frame is diffuse in the honest sense

`p_j^2+ell_j^2+v_j^2 <=1/2` for every `j`,                            (5.7)

then every residual active leverage is at most `1/2`. If `|b|>=1`, (5.5) is also at most `1/2`. Theorem F now gives

`||p_{Q_b}||_infinity`
` <= 12 |det M_b|^(-1/3)`
` = 12 [(1+b^2)|lambda|]^(-1/3)`
` <= 12`.                                                            (5.8)

Thus the diffuse punctured chamber with `|b|>=1` is already uniformly paid.

If `0<|b|<1`, condition only on the literal hub `H`. The remaining quadratic form is exact rank three on `span(p,ell,v)` with determinant `-b^2 lambda`, and its row leverages are exactly the left side of (5.7). The same pinned theorem gives

`||p_{Q_b}||_infinity <= 12 (|lambda| b^2)^(-1/3)`.                   (5.9)

Equation (5.9) displays the old power loss produced by deleting the single heavy hub; Theorem 3.1 improves that loss to logarithmic by retaining the hub through the curved two-bank summation. This identifies a concrete obstruction rather than merely restating Theorem F.

The pinned counterexample search still reports no target-valid counterexample. Its ruled Theorem C separately gives `p_Q(s)<=pi sqrt(2)` on the one-sheet side of exact rank-three signature `(2,1)`, so the present critical-window debt remains on the complementary convex/two-sheet geometry.

## 6. Designated partner account03/B05 applied

The newest compatible partner result is account03/B05 r32 (`20260923T204411Z-account03-B05-QFORM-r32`). In its ratio packet let

`m=sum u_i^2`,
`sigma^2=sum(t_i-r u_i)^2`,
`q_X=max_i ||(u_i/sqrt(m),e_i/sigma)||^2`.

When `q_X>=1/2`, take the heavy row and `theta=1/8`. The partner proves the dichotomy

`||p_Q||_infinity < 51.6 (8/(mu m))^(1/3)`,                          (6.1)

or, after conditioning one literal original coordinate,

`m'>7m/8`, `(sigma')^2<=5sigma^2/8`,
`sigma'/sqrt(m') <= sqrt(5/7) sigma/sqrt(m)`,                         (6.2)

and therefore

`m'^2/(sigma')^2 >= (49/40) m^2/sigma^2`.                            (6.3)

For the standard packet `m>=3/20`, (6.1) becomes the real numerical bound

`boxed{ ||p_Q||_infinity < 194.229836362 mu^(-1/3). }`               (6.4)

So a genuinely heavy residual row either pays immediately or forces a strict residual descent. This complements Theorem 3.1: the new logarithmic bridge attacks the diffuse-residual/single-heavy-hub punctured chamber, while r32 supplies a mechanism when the residual packet itself is heavy. The partner's tower compiler remains open and is not assumed here.

## 7. What is now genuinely unpaid

The fixed-nonzero-coupling branch is bounded, and its previous power divergence has been reduced to a single logarithm. The exact zero endpoint is bounded by the earlier Borel null-hub/transverse-square theorem. The diffuse `|b|>=1` chamber is bounded by (5.8), and noncritical output levels enjoy the sharper square-root-log estimate (4.4).

The remaining local analytic question is therefore sharply stated:

`QFORM-TWOBANK-HUB-CRITICAL-PUNCTURED-UNIFORM-v1`:

for the same rough product-bank class, prove a bound in the bounded critical output window that remains finite as `b->0`, using the true product structure before arbitrary-set maximalisation. Any valid proof has to couple the `b=0` Borel square-root geometry to the `b!=0` oscillatory bank variable without invoking conditional density caps, an arbitrary-joint coarea theorem, post-rotation independence, or a small-random-error argument.

A plausible currency is a weak-type/real-interpolation estimate for the two-bank curved transform that interpolates the `b=0` Borel square-root pushforward with the punctured `P`-Fourier gain. This is not proved here.

Full unrestricted QFORM remains OPEN. Independent review of the theorem in this report is PENDING.
