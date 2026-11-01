SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B20, 2026-09-22T19:49:15Z.
attacking: the one-effective-direction Schur survivor after rank-two-cross closure, via a ridge-or-uniform-near-rank-one-cut dichotomy and fleet04/B20's second-Schur gate.

# fleet03/B20 QFORM r16 — ridge-or-uniform-near-rank-one Schur closure

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Control at start:** `yspennstate/math-research-brain@2b13c645a4b95504c6ef52317faf238b09d34b16`, owner revision `2026-09-22.15`.  
**Classification:** `ESSENTIAL_STEP_APPLIED / ONE-EFFECTIVE-DIRECTION SCHUR SURVIVOR SHARPENED / FULL TARGET OPEN`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Continuity:** the residual ridge branch has a continuous density, but the final dependent physical-pivot square step below is used only for essential boundedness; full-target continuity is NOT claimed.

## 1. Exact target and correction boundary

The full target remains open: for every real symmetric `A` with at least three eigenvalues of modulus at least one, and every independent cap-one product input, prove a universal finite essential density bound for `X^T A X`, or give a genuine target counterexample. No Gaussian/log-concave/moment/compact-support/connected-support/eigen-coordinate independence hypothesis is used.

This run does not use law-uniform pointwise quadratic Fourier decay, arbitrary-joint three-dimensional coarea, worst-fiber density normalization, post-rotation independence, single-good-minor selection, or a conditional density cap created by conditioning on a dependent statistic.

## 2. Fresh cross-account input actually consumed

The newest compatible synthesis input is fleet01/B20 run `20260922T192841Z-fleet01-B20-QFORM-r11`, canonical report

`yspennstate/math-open-problems@306b0acf13b9e10147cca740baf23c8e27961f97`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B20/20260922T192841Z-fleet01-B20-QFORM-r11/REPORT.md`.

Its theorem `QFORM-PIVOT-RANK2-CROSS-CLOSURE-v1` proves that, after retaining a physical pivot `a` with

`|a| >= m := 3501/8000`,

and writing the exact physical Schur complement

`S=A_{-i,-i}-A_{-i,i}A_{i,-i}/a`,

every residual original-coordinate cut `L|R` with

`s_2(S[L,R]) >= beta := 1/64`

is already paid by an essentially bounded density estimate `<340`. Consequently every still-unpaid coherent/externalized P1 survivor satisfies

`(A)  s_2(S[L,R]) < beta=1/64`

for **every** residual original-coordinate cut.

The same fleet01 proof explicitly preserves arbitrary Schur self blocks and arbitrary remaining couplings, so (A) is a full residual physical-cut restriction, not a two-by-two-minor proxy.

The general one-scale ridge theorem used below is the complete supporting theorem `QFORM-RIDGE-DENSITY-v1`, canonical proof `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`. For an original-coordinate cross block `C`, scale `gamma>0`,

`K=C C^T (gamma^2 I+C C^T)^(-1)`, `theta=tr K`,

if `1<=q<=2`, `max diag K<=q/2`, and `theta>2q`, then the corresponding full quadratic form in those independent physical coordinates, with arbitrary self blocks and outside couplings, has a continuous density with

`||p||_infinity <= sqrt(e)/(sqrt(2q) gamma) * theta/(theta-2q)`.

## 3. New theorem — `QFORM-SCHUR-RIDGE-OR-UNIFORM-NEARRANK1-v1`

### Theorem

Assume the physical-pivot setup above, with `|a|>=m=3501/8000`, and assume (A). For each residual physical cut `L|R`, put

`C=S[L,R]`,

`K_beta(C)=C C^T (beta^2 I+C C^T)^(-1)`,

`theta_beta(C)=tr K_beta(C)`, where `beta=1/64`.

Then one of the following two alternatives holds.

**Ridge-paid alternative.** There exists a residual physical cut with

`theta_beta(C) >=5`.

Then the original ambient quadratic form `Q=X^TAX` has an essentially bounded density and

`boxed( ||p_Q||_infinity <800. )`

**Uniform one-effective-direction alternative.** For every residual physical cut,

`theta_beta(C)<5`,

and the entire cut is dimension-freely close to rank one in Frobenius norm:

`boxed( dist_F(C,{rank<=1}) < sqrt(10)/64 <0.049411. )`          (3.1)

In particular every still-unpaid coherent/externalized P1 survivor after fleet01/B20 r11 lies in the second alternative.

### Proof of the ridge-paid alternative

Fix a cut `C` with `theta:=theta_beta(C)>=5`. Apply `QFORM-RIDGE-DENSITY-v1` not to a rotated source, but directly to the residual quadratic form

`R(Y)=Y^T S Y`

on the original residual independent coordinates. Take `gamma=beta` and `q=2`. Since

`0 <= K_beta(C) < I`,

we have `max diag K_beta(C)<=1=q/2`, while `theta>=5>4=2q`. Hence `R` has a continuous density `p_R` satisfying

`||p_R||_infinity
 <= sqrt(e)/(2 beta) * theta/(theta-4)
 <= 5 sqrt(e)/(2 beta)
 =160 sqrt(e)`.                                                  (3.2)

The last inequality uses that `theta/(theta-4)` is decreasing on `(4,infinity)`.

Now complete only the original physical scalar pivot:

`Q=a (X_i+a^(-1) A_{i,-i}Y)^2 + R(Y)`.                         (3.3)

No independence is asserted between the shifted square and `R`. Instead, condition on the genuine residual coordinates `Y`. The conditional law of

`X_i+a^(-1)A_{i,-i}Y`

is just a translate of the original law of `X_i`, and therefore still has density at most one. The scalar square change of variables gives, for `a>0`,

`p_Q(t) <= |a|^(-1/2) E[ 1_{R<t} (t-R)^(-1/2) ]`,              (3.4)

and the analogous right-sided expression for `a<0`.

For either side, split the half-Riesz kernel at distance one. If `M=||p_R||_infinity`,

`sup_t E[1_{R<t}(t-R)^(-1/2)]
 <= M int_0^1 u^(-1/2) du +1
 =2M+1`,                                                        (3.5)

with the same estimate on the right. Combining (3.2)-(3.5) and `|a|>=m` gives

`||p_Q||_infinity
 <= m^(-1/2) [ 5 sqrt(e)/beta +1 ]
 = (320 sqrt(e)+1)/sqrt(3501/8000)
 =799.040043... <800`.                                         (3.6)

This proves the first alternative. Notice that continuity of `R` is proved by the ridge theorem, but (3.4) is used only to prove an essential bound for `Q`; continuity of `Q` is not asserted.

### Proof of the uniform near-rank-one alternative

Suppose no cut is ridge-paid. Then `theta_beta(C)<5` for every cut. Let

`sigma_1>=sigma_2>=...>=0`

be the singular values of one such `C`. By (A), `sigma_k<beta` for every `k>=2`. Put

`x_k=sigma_k^2/beta^2`, `k>=2`.

Then `0<=x_k<1`, and therefore

`x_k/(1+x_k) >= x_k/2`.                                        (3.7)

Since

`theta_beta(C)=sum_k sigma_k^2/(beta^2+sigma_k^2)<5`,

we obtain

`sum_{k>=2} sigma_k^2/beta^2
 =sum_{k>=2} x_k
 <=2 sum_{k>=2} x_k/(1+x_k)
 <10`.                                                         (3.8)

By Eckart-Young,

`dist_F(C,{rank<=1})^2=sum_{k>=2}sigma_k^2<10 beta^2`,

which is exactly (3.1). QED.

## 4. Immediate algebraic consequences for the remaining survivor

The conclusion is much stronger than the previous statement `s_2(C)<1/64`: a large number of sub-threshold transverse singular directions cannot accumulate. For **every** physical residual cut, all singular directions after the first have total squared mass below

`10/4096=5/2048`.

For every four distinct residual physical indices `i,j,k,l`, choose a physical cut with `i,j` on one side and `k,l` on the other. Its `2x2` submatrix obeys

`|S_ik S_jl-S_il S_jk|
 < beta sqrt(S_ik^2+S_il^2+S_jk^2+S_jl^2)`,                  (4.1)

because singular values cannot increase under row/column restriction and `|det B|=s_1(B)s_2(B)`. Thus every unpaid survivor satisfies a uniform approximate tetrad relation in the original physical coordinates. No arbitrary bistochastic or eigenbasis data enter (4.1).

## 5. Required fleet04/B20 result applied to an actual inequality

The designated fleet04/B20 completed result is run `20260922T172057Z-fleet04-B20-QFORM-r3`, canonical proof

`yspennstate/math-open-problems@25ad8faaac5064b6814d51ae63d894fe97c1eac4`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B20/20260922T172057Z-fleet04-B20-QFORM-r3/REPORT.md`.

Its theorem `QFORM-CROSS-DOMINATED-SECOND-SCHUR-CLOSURE-v1` states, in its validated diagonal-dominated first-pivot reduction, that with `|a|>=tau>=1/4` and high-window second row

`S=[[d,c^T],[c,C0]]`,

if

`||c||_2>|d|` and `||c||_2>tau/9`,

then the full ambient density satisfies `<5262`.

Our retained P1 pivot has `|a|>=3501/8000>1/4`, so on **that partner theorem's validated overlap** we may take `tau=1/4`. Therefore every still-unpaid survivor on that overlap must obey the actual contrapositive inequality

`boxed( ||c||_2 <= max{|d|,1/36}. )`                           (5.1)

Thus the surviving one-effective-direction geometry is not allowed to hide in the partner's cross-dominated second-Schur row: the selected high-window row is either genuinely small (`||c||_2<=1/36`) or diagonally dominated (`||c||_2<=|d|`). This is an actual use of the designated partner theorem, with its scope preserved; (5.1) is not asserted for rows outside that validated reduction.

## 6. What this pays and what remains

The newest fleet02/B20 externalization theorem shows that an unpaid coherent compact physical triangle cannot remain self-contained: after a rank-one subtraction supported on the triple, it yields either an outside two-direction packet or a triangle-to-outside cross packet. The newest fleet01/B20 theorem then pays every residual Schur cut with a second singular value at least `1/64`.

This run pays a further class that fleet01/B20 did not: even when every `s_2<1/64`, **many** sub-threshold transverse singular directions cannot remain if their ridge effective dimension reaches five. Such a cut gives the explicit full ambient bound `<800`. Hence the first genuinely unpaid external-packet geometry is now quantitatively constrained by both

1. every residual original-coordinate cut is within `sqrt(10)/64` in Frobenius norm of rank one; and
2. on fleet04/B20's validated second-Schur overlap, the high-window cross row obeys (5.1).

This is a dimension-free one-effective-direction reduction, not an easy subclass theorem.

The next implication is

`QFORM-UNIFORM-NEARRANK1-CUT-GLUING-v1`:

**glue the cutwise rank-one approximants without dimension loss**. Prove that a symmetric Schur matrix satisfying (3.1) for every physical cut and the source packet supplied by the coherent-triangle externalization must either (i) lie in a product-preserving grouped/star rank-one endpoint that can be paid, (ii) generate a new cut with ridge effective dimension at least five, or (iii) force a physical diagonal/pair packet already covered by existing theorems. The approximate tetrads (4.1) and the partner row gate (5.1) are the first universal constraints for this gluing step.

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains open.

## 7. Numerical regression values

With `m=3501/8000` and `beta=1/64`:

- residual ridge density cap in the `theta>=5` branch: `160 sqrt(e)=263.7954033120...`;
- full pivot density cap from (3.6): `799.0400422276...`;
- uniform cutwise best-rank-one Frobenius error: `sqrt(10)/64=0.04941058844...`;
- partner threshold `tau/9` at `tau=1/4`: `1/36=0.02777777777...`.

These computations only check displayed constants; the proof is analytic.
