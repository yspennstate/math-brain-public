SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B06, 2026-09-23T11:17:29Z.
attacking: the sign-opposite nonzero scalar/dependent-pair kernel: pay the two-sheet curved half-Riesz branch with the original independent scalar retained, then splice the newest ruled one-sheet theorem for a target-valid near-coloop family.

# account03/B06 r34 — opposite-sign semi-aligned two-sheet transducer

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Curved fiber integration  
Status: **NEW SUPPORTING THEOREM + TARGET-VALID NEAR-COLOOP FAMILY CLOSED / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.


## 1. Source-valid predecessors actually used

### 1.1 account02/B16: same-sign and exact-null scalar/dependent-pair transducer

Source snapshot containing the completed report:

`yspennstate/math-open-problems@f13d13f2dd1d240c98505a03afebe80f64d4bf10`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260923T082859Z-account02-B16-QFORM-r11/REPORT.md`.

Its Theorem 2.1 treats

`Y=gamma X+H`,
`Q=delta Y^2+2kUY+beta V^2`,

with `X`, `V`, and `(H,U)` mutually independent source objects, while `H` and `U` may be arbitrarily dependent. It proves a uniform full-line bound when `delta beta>=0`, and the exact-null endpoint `delta=0`. The present run attacks the complementary nonzero sign `delta beta<0`; it does not rename the already-paid same-sign case.

### 1.2 Newest Claude ruled one-sheet theorem

The current Claude package is

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`

and Theorem C states: for an actual rank-three product projection with signature `(+, +, -)` and all three spectral moduli at least one, the one-sheet side satisfies

`p(s)<=pi sqrt(2)` for `s>=0`.

The proof uses ruled-hyperboloid line integrals that are two-dimensional marginals of the ORIGINAL product law. It does not assert independence of the three spectral coordinates. I apply this exact result to the complementary side of the target-valid family in Section 4.

### 1.3 account04 result actually applied

The exact designated partner path `account04/B06` is still absent from the current QFORM archive at the publication check, so no theorem from that slot is fabricated. The compatible completed account04/B18 theorem is

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`.

Its dependence-safe square smoothing says

`||p_{R+aV_R^2}||_inf <=2 sqrt(M/|a|)`

whenever `||p_R||_inf<=M` and the conditional density of the translated scalar is capped by one. I apply it at an actual equation in Section 5.

## 2. Main theorem: opposite-sign two-sheet curved kernel

### Theorem 2.1 — `QFORM-OPPOSITE-SIGN-SEMI-ALIGNED-TWOSHEET-v1`

Let `(H,U)` be an arbitrary real random pair. Let `X` and `V` be real random variables such that the three source objects

`X`, `V`, `(H,U)`

are mutually independent. Assume the marginal density caps

`||p_X||_inf<=L_X`, `||p_U||_inf<=L_U`, `||p_V||_inf<=L_V`.

Let `gamma,k,beta,delta` be nonzero reals with

`delta beta<0`.

Put

`Y=gamma X+H`,
`Q=delta Y^2+2kUY+beta V^2`.

Then `Q` is absolutely continuous. On the two-sheet/minority-sign side

`s beta<0`

its density satisfies

`boxed: p_Q(s) <= 4 sqrt(2) L_V sqrt( L_X L_U / |beta gamma k| ).`   (2.1)

The bound is independent of `|delta|`; in particular it is uniform as the nonzero pivot tends to zero from the sign-opposite side.

No conditional density bound for `U|H` is assumed or used.

### Proof

Reflect the output if necessary. Since reflection preserves density norms, it is enough to assume

`beta>0`, `delta=-a<0`, `a>0`.

The relevant side is then `s<0`.

Let

`W=-aY^2+2kUY`.

Because `V` is independent of `(X,H,U)` and `p_V<=L_V`, the density of `beta V^2` obeys

`g(z)<=L_V/(sqrt(beta) sqrt(z)) 1_{z>0}`.

Therefore for almost every `s`,

`p_Q(s)<=L_V beta^(-1/2) E[(s-W)_+^(-1/2)].`                       (2.2)

Now condition on `(H,U)=(h,u)`. Genuine source independence leaves

`Y=gamma X+h`

with a translated density cap

`L_Y=L_X/|gamma|`.                                                   (2.3)

Complete the deterministic quadratic only inside the curved kernel:

`W=-a(Y-ku/a)^2+k^2u^2/a`.                                          (2.4)

For `s<0` define

`R= k^2u^2/a-s = k^2u^2/a+|s|>0`.

Then

`s-W=a(Y-ku/a)^2-R`.

For fixed `u` write

`K(y)=(a(y-ku/a)^2-R)_+^(-1/2)`.

For every `lambda>0`, the superlevel set is exactly two short shells:

`0<a(y-ku/a)^2-R<lambda^(-2)`.

Its total length is

`2 a^(-1/2)[sqrt(R+lambda^(-2))-sqrt(R)]`.

Rationalising the difference gives

`|{K>lambda}|`
`= 2 a^(-1/2) lambda^(-2)/(sqrt(R+lambda^(-2))+sqrt(R))`
`<= [sqrt(aR) lambda^2]^(-1).`                                      (2.5)

This is the weighted curved-fiber replacement: the full shell length is paid before taking a pointwise fiber maximum.

Using both the cap (2.3) and probability normalization, layer cake gives

`E[K(Y)|H=h,U=u]`
`<=int_0^inf min(1,L_Y/(sqrt(aR)lambda^2)) dlambda`
`=2 sqrt(L_Y) a^(-1/4) R^(-1/4).`                                  (2.6)

Because

`R>=k^2u^2/a`,

we have

`a^(-1/4)R^(-1/4)<=|k|^(-1/2)|u|^(-1/2)`.                         (2.7)

For any probability density capped by `L_U`, the sharp bathtub estimate is

`E|U|^(-1/2)<=2 sqrt(2L_U)`.                                        (2.8)

Averaging (2.6)-(2.8) over the unconditional marginal of `U` gives

`E[(s-W)_+^(-1/2)]`
`<=4 sqrt(2) sqrt(L_Y L_U/|k|).`                                   (2.9)

Substitute `L_Y=L_X/|gamma|` into (2.2), yielding exactly (2.1).

At no point is `U` conditioned on `H` through a density cap; dependence inside `(H,U)` is preserved. QED.

## 3. Why the sign and side matter

The sign-opposite case cannot be obtained by the same one-variable estimate as the completed `delta beta>=0` theorem. For `beta>0`, `delta<0`, the kernel after completion is

`(a z^2-R)_+^(-1/2)`

on `s<0`, so the level set is a pair of hyperbolic shells. The exact shell-length estimate (2.5) yields the crucial `lambda^-2` tail after retaining the positive gap `R=k^2u^2/a+|s|`.

This is also why the arbitrary dependence between `H` and `U` does not hurt: the vertex location depends on `H`, but the critical value after completion is

`k^2u^2/a`,

which is independent of `H`. The final `u`-integration can therefore use only the genuine unconditional marginal cap for `U`.

The theorem deliberately claims only the side `s beta<0`. The complementary one-sheet side is supplied by the newest product-provenance ruled theorem when the deterministic rank-three target hypotheses are actually present.

## 4. Target-valid sign-opposite near-coloop family

This section turns Theorem 2.1 into an actual three-large-eigenvalue statement rather than an abstract kernel bound.

Fix even `m`, balanced signs `epsilon_j in {+1,-1}`, and `c in (0,1)`. Put

`a0=1-c`,
`T=m^(-1/2) sum_j X_j`,
`U=m^(-1/2) sum_j epsilon_j X_j`,
`V=m^(-1/2) sum_j Z_j`,

where `X_0`, the whole `X_j` bank, and the whole `Z_j` bank are disjoint collections of independent cap-one original coordinates. The pair `(T,U)` may be dependent; no independence inside that bank is claimed.

For `eta>=0` define

`Y=sqrt(c) X_0+sqrt(a0)T`,

and

`Q_{c,-eta}`
`= -eta Y^2 + 2 sqrt(1+eta) UY + V^2`.                              (4.1)

The Parseval frame is the same source-valid frame as in account02/B16 r11. The deterministic spectral matrix is

`B_eta=[[-eta,sqrt(1+eta),0],`
`       [sqrt(1+eta),0,0],`
`       [0,0,1]]`.

Its eigenvalues are exactly

`boxed: {1,-(1+eta),1}.`                                            (4.2)

Indeed, the 2x2 characteristic polynomial is

`lambda^2+eta lambda-(1+eta)=(lambda-1)(lambda+1+eta)`.

Hence every `eta>=0` is an actual three-large-eigenvalue target instance.

The one-dimensional product-projection bound used by the predecessor gives

`||p_U||_inf, ||p_V||_inf <=sqrt(2)`.                               (4.3)

For `eta>0`, Theorem 2.1 with

`gamma=sqrt(c)`, `k=sqrt(1+eta)`, `beta=1`, `L_X=1`, `L_U=L_V=sqrt(2)`

gives on the two-sheet side `s<0`

`boxed: p(s)<=2^(13/4)[c(1+eta)]^(-1/4).`                           (4.4)

At `eta=0`, the exact-null endpoint is already paid by account02/B16 r11, with a smaller constant.

On the complementary side `s>=0`, the newest Claude Theorem C applies to the actual product projection (4.1)-(4.2) and gives

`boxed: p(s)<=pi sqrt(2).`                                          (4.5)

Therefore in the live near-coloop collar `c>63/64`,

`boxed: ||p_{Q_{c,-eta}}||_inf < 9.552`                             (4.6)

for every `eta>=0`. The numerical value is

`2^(13/4)(64/63)^(1/4)=9.5511868672...`,

while `pi sqrt(2)=4.4428829381...`.

Thus the sign-opposite semi-aligned nonzero near-null family is uniformly paid all the way to the null endpoint.

### 4.1 This is genuinely a no-pivot/near-null family

The hub diagonal is

`A_00=-c eta`.

For a first-bank leaf `j`, direct calculation gives

`det A[{0,j},{0,j}] = -c(1+eta)/m`.                                 (4.7)

All first-bank leaf diagonals are

`[-eta a0 +2sqrt(1+eta)sqrt(a0) epsilon_j]/m`,

all second-bank diagonals equal `1/m`, first-first pair determinants are `O(a0(1+eta)/m^2)`, hub-second determinants are `-c eta/m`, and the remaining pair determinants are `O(eta/m)+O(m^-2)`.

Hence for every fixed physical no-pivot threshold `tau>0`, first choose `eta>0` sufficiently small and then `m` sufficiently large. Every physical diagonal and every physical 2x2 principal determinant is below `tau`, while the exact spectrum (4.2) remains in the target class and the density stays bounded by (4.6).

So this is not a localized principal-minor theorem in disguise.

## 5. Actual account04/B18 splice

Let the base variable in Section 4 be denoted `R=Q_{c,-eta}`. In the near-coloop collar it has density cap

`M<9.552`.

Suppose an untouched original scalar `T_0`, with conditional density cap one after conditioning on the base source, enters through an actual translated square

`Q_*=R+a_1[T_0+Psi]^2`, `a_1!=0`,                                  (5.1)

where `Psi` may depend on the base source. The completed account04/B18 dependence-safe square theorem applies directly to (5.1): no independence between the numerical value `R` and the translated square is required. Therefore

`||p_{Q_*}||_inf <=2 sqrt(M/|a_1|)`
`<6.181/sqrt(|a_1|).`                                               (5.2)

This is a completed account04 result applied at an actual equation. The exact designated `account04/B06` artifact remains unavailable and is not fabricated.

## 6. Checks

`CHECKS.md` beside this report records:

- exact/numerical eigenvalue checks for (4.2), including `eta=100`;
- the constants `9.5511868672...` and `4.4428829381...`;
- the exact ratio form proving the shell-length inequality (2.5);
- a 100,000-point logarithmic random sanity check of that ratio, with maximum stable-form ratio `1.0` to machine precision.

These computations are sanity checks only. Equations (2.2)-(2.9) are the proof.

## 7. What changed and what remains

New theorem:

`QFORM-OPPOSITE-SIGN-SEMI-ALIGNED-TWOSHEET-v1`.

New target-valid closure:

`QFORM-SIGN-OPPOSITE-NEAR-COLOOP-FAMILY-v1`.

Together with account02/B16 r11 and the newest Claude ruled theorem, the semi-aligned near-coloop model is now paid on both nonzero pivot signs and at the exact null endpoint, with original source provenance preserved.

This does **not** prove the full conjecture. The first B06 debt is now:

`QFORM-SHARED-BANK-SQUARE-OR-HIGHERRANK-TAIL-v1`:

> extend the two-sheet shell payment when the final smoothing square is not carried by a disjoint original-coordinate bank, or when a nonseparable higher-rank ambient tail remains. The replacement must preserve the original product grouping and cannot treat a small matrix tail as a uniformly small random quadratic perturbation on arbitrary unbounded inputs.

The full QFORM conjecture remains `OPEN / NOT PROVED / NOT DISPROVED`.

Continuity is separate. This run proves absolute continuity and an essential density bound for the stated sign-opposite branch, but does not prove a continuous representative uniformly on the whole target.
