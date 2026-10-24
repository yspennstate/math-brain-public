# account03/B15 r13 — nine-direction same-constant C0 closure and eight-direction regularity ledger

Run: `20260924T140459Z-account03-B15-fixedmult-continuity-r13`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Nonduplication and current mathematical sources

The complete 790-line baseline was already independently reread by this slot in r12; that report found the written seventeen-direction theorem mathematically PASS, with only the known nonfatal product-projection indexing wording issue. I do not repeat that audit here.

This run consumes four later source-pinned results that were not all available at the start of r12:

1. account03/B04, `QFORM-FIXED-MULTIPLICITY-9-v1`, complete replacement proof reducing the height theorem to `s_9(A)>=s`, at `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account03/B04/20260924T121940Z-account03-B04-fixedmult-audit-r1/REPORT.md`; current blob `054facef834d29927713c5d42a1f09a541c5644b`;
2. account01/B16 independent reconstruction of that nine-direction proof, commit `54ec2a651d854563f8db0d92c4c3426f76551786`;
3. account03/B14 independent audit plus exact constant sharpening to `<2582 K^2/s`, commit `9861ed55f7865b2a67346a66bc178eb7f81df190`;
4. account03/B04's eight-direction terminal-collar theorem, blob `851e0ae9c78a4d9a49f60a1cc5f0026b734579e6`, together with account01/B11's three-color `E_2` consequence, commit `d823d8d8fcf93c3e3d39dc18d8b86e2f742683dc`.

For regularity I use the completed account03/B15 affine fixed-instance theorem at commit `26ef4e7b08ecc3336e8ee7fcfdf0445e868745c5` and the designated-partner account04/B15 same-constant homogeneous compiler in `proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260923T221909Z-account04-B15-ruled-trace-c0-r8/REPORT.md`.

The unrestricted three-eigenvalue conjecture remains OPEN.

## 2. The nine-direction theorem has a canonical C0 density with the same sharpened height

### Theorem `QFORM-FIXED-MULTIPLICITY-9-C0-v1`

Let `X=(X_1,...,X_n)` have independent real coordinates with probability densities bounded by `K<infinity`. Let `A=A^T`, `b in R^n`, `c in R`, and assume

` s_9(A) >= s > 0.`

Then the current nine-direction proof and its sharpened constant imply that

`Q=X^TAX+b^TX+c`

has a **canonical continuous density vanishing at infinity** and

`boxed: p_Q in C_0(R),   ||p_Q||_infinity < 2582 K^2/s.`          (2.1)

No law-uniform or matrix-uniform modulus of continuity is asserted.

### Proof

The B04 replacement proof, independently reconstructed by account01/B16, establishes the interval/density theorem under `s_9(A)>=s` with all original hypotheses retained. The B14 audit sharpens the largest normalized branch from `6010` to the exact rational upper bound

`2259248/875 = 2581.997714285714... < 2582`,                    (2.2)

without changing any structural hypothesis. Thus for every interval `I`,

`P{Q in I} < (2582 K^2/s)|I|`.                                  (2.3)

On the other hand, the completed affine fixed-instance theorem at commit `26ef4e...` applies to every fixed symmetric Hessian of rank at least three and arbitrary cap-one product inputs and affine terms. Since `s_9(A)>=s>0` forces `rank(A)>=9`, after the standard normalization it supplies a canonical representative in `C_0(R)`.

To spell out scaling without hiding a regularity assumption, define

`Y=KX`, `A'=A/s`, `b'=(K/s)b`, `c'=(K^2/s)c`,

and

`Qtilde=Y^T A'Y+b'^T Y+c'`.

Then the coordinates of `Y` have densities bounded by one, `rank(A')>=9`, and

`Q=(s/K^2) Qtilde`.                                               (2.4)

The fixed-instance theorem gives `p_Qtilde in C_0`; scalar dilation in (2.4) gives `p_Q in C_0`.

Equation (2.3) gives `p_Q<=2582 K^2/s` almost everywhere. If the continuous representative exceeded `2582 K^2/s` at one point, continuity would produce a nonempty interval on which it exceeded that value, contradicting (2.3). Hence (2.1).

This continuity conclusion is not inferred from essential boundedness alone; it is supplied by the separate fixed-instance quadratic/product theorem.

## 3. Designated partner applied to an actual nine-direction inequality

Account04/B15 Theorem 6.1 in the source above states: for a **fixed homogeneous** rank-at-least-three quadratic form under cap-one product inputs, any separately paid interval estimate

`P{Z in I} <= M |I|`                                             (3.1)

upgrades to a canonical `C_0` density with the identical height `M`.

Apply it to the homogeneous specialization `b=c=0` of the sharpened nine-direction theorem. Normalize with `Y=KX`, `A'=A/s`. The actual paid inequality is

`P{Y^T A'Y in I} < 2582 |I|`.                                   (3.2)

Since `rank(A')>=9`, the partner theorem gives

`p_(Y^T A'Y) in C_0(R),   ||p_(Y^T A'Y)||_infinity <=2582`.       (3.3)

Scaling back gives the concrete partner-applied inequality

`boxed: p_(X^TAX) in C_0(R),   ||p_(X^TAX)||_infinity <2582 K^2/s.` (3.4)

The affine conclusion (2.1) uses the separate affine fixed-instance theorem; I do not silently extend the partner's homogeneous statement.

## 4. Independent arithmetic check of the 2582 sharpening

The B14 sharpening uses

`q_2=1733/2500`, `q_c=73777/50000`, `pi<22/7`,

and obtains the scalar-pivot truncated half-potential

`10(22/7+4 q_2+2(4+4q_c)) = 1125249/4375
                               =257.199771428571...`              (4.1)

Adding the unit tail gives

`1129624/4375 = 258.199771428571...`.                            (4.2)

The outer scalar pivot costs `eta^{-1/2}=10`, hence

`10*(1129624/4375)=2259248/875
                   =2581.997714285714... <2582`,                (4.3)

with exact margin `2/875`. The no-pivot branch remains `<2400`, the definite-pair branch `<32`, and the indefinite-pair branch `<251`; therefore (4.3) is the controlling branch.

## 5. Exact regularity status at eight directions

The current threshold-eight structural theorem does not yet prove a **uniform** density height, but regularity itself is no longer the missing issue.

For every fixed `A` with `s_8(A)>=s>0`, one has `rank(A)>=8`. Therefore the same affine fixed-instance theorem already gives, for every admissible rough product law and arbitrary affine `b,c`,

`boxed: p_Q in C_0(R) cap L^infinity(R)`                         (5.1)

with a finite constant that may depend badly on the particular matrix `A`. Thus the unresolved `9 -> 8` problem is **uniformity of the height**, not existence of a density and not qualitative continuity.

In the only currently unresolved normalized no-pivot collar branch, account03/B04 proves

`Xi_2(A) >= (delta_*^2/2) kappa^2`,                              (5.2)

where

`kappa=1/6400`,
`delta_*=0.854335140191133771...`.

Account01/B11's three-color extraction gives a literal physical cut `B` with

`E_2(B) >= (sqrt(2) delta_*/27) kappa
          =6.99196957216563e-6...`.                              (5.3)

The completed marginal-free order-two product-Fourier receiver then yields the **full** half-potential bound

`boxed: sup_a E|Q-a|^(-1/2) <53.338.`                            (5.4)

I independently recomputed the constant from

`C_2=8 sqrt(e) 2^(-1/8)=12.095072570796...`

and (5.3):

`C_2 E_2(B)^(-1/8)=53.3376082498547...`.                         (5.5)

Consequently every interval `I` in that normalized terminal branch also obeys the universal square-root concentration estimate

`P{Q in I}
 <= 53.338 sqrt(|I|/2)
 <37.716 sqrt(|I|).`                                             (5.6)

Indeed, if `a` is the midpoint of `I`, then on `{Q in I}` one has `|Q-a|^{-1/2} >= (|I|/2)^(-1/2)` and Markov's inequality applied to (5.4) gives (5.6).

For general cap `K` and spectral scale `s`, (2.4) gives the scaled form

`sup_a E|Q-a|^(-1/2) <53.338 K/sqrt(s)`,                         (5.7)

and therefore

`P{Q in I} <37.716 K sqrt(|I|/s)`.                               (5.8)

Equations (5.1), (5.4), and (5.8) precisely separate what is solved from what is not: the output is already continuous for every fixed matrix and has a universal order-one-half concentration certificate in the unresolved collar, but no dimension-free linear interval estimate `C|I|` is yet known there.

## 6. Why the half-potential does not finish multiplicity eight

The implication

`sup_a E|Q-a|^(-1/2) <=H  =>  P{Q in I}<=H sqrt(|I|/2)`          (6.1)

has exponent `1/2`, not exponent one. Even together with qualitative `C_0` regularity, it does not control the peak height uniformly: continuous densities can form arbitrarily tall, arbitrarily narrow spikes while keeping a square-root interval-mass bound. Therefore no `L^infinity` theorem is inferred from (5.4).

The B04 terminal collar contains more information than (5.4): the overlap-one currency `Omega_1` and the two-sided pair currency `Xi_2`. A valid eight-direction proof must spend that provenance **before** collapsing it to the scalar half-potential, or find another product-preserving smoothing direction. This is the first essential missing implication.

## 7. Status

- Written seventeen-direction baseline: PASS in the completed r12 audit; unchanged here.
- Nine-direction height theorem: complete source proof exists; account01/B16 independently reports PASS; account03/B14 independently audits and sharpens the constant to `<2582 K^2/s`. Release/validation status remains owner/B20 territory.
- New in this run: the nine-direction theorem is upgraded to a canonical `C_0` density with the **same** `<2582 K^2/s` height, including arbitrary affine terms.
- New synthesis for eight directions: every fixed instance already has a `C_0 cap L^infinity` density; in the unresolved collar there is additionally a universal full half-potential `<53.338` and interval concentration `<37.716 sqrt(|I|)` in normalized variables. The sole remaining endpoint debt is a **uniform linear interval bound**.
- Multiplicity eight: OPEN.
- Unrestricted three-eigenvalue conjecture: OPEN.
