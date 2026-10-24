SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B02, 2026-09-22T21:58:17Z.
attacking: the first unpaid two-sided square/rank-two Fourier step; after a source-valid obstruction to the naive Gabor-line extension, switch mechanism to a full L^q integrated-square family that reduces the near-isotropic cost from a power to a logarithm on the one-sided packet.

# account03/B02 QFORM r16 — Gabor-line obstruction and an L^q Fourier compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T215817Z-account03-B02-qform-r16`  
**Assignment:** Integrated Fourier estimate  
**Fresh owner control at start:** `yspennstate/math-research-brain@52cb2725682f68daf07e9e1583c12d8e641f0344`, OWNER CONTROL revision `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full target:** OPEN / NOT PROVED / NOT DISPROVED  
**Continuity:** proved only on the Fourier branches below because their characteristic functions are in `L^1`; full-target continuity remains open.

## 1. Exact target and first unpaid implication

The target is unchanged: for every finite `n`, every vector `X=(X_1,...,X_n)` of independent real coordinates with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove a universal finite bound on the density of `Q=X^TAX`, or produce a target-valid counterexample. No moment, support, Gaussian, log-concavity, diagonal-basis, or post-rotation-independence assumption is introduced.

The previous B02 run proved an `L^1_t` theorem for a physical packet

`{Z} union I union J union W`

with `d=A_ZZ!=0`, exact-rank-two cross block `B=A[I,J]`, and the one-sided isolation `A[Z,J]=0`. Its first unpaid implication was to remove this isolation. In the genuinely two-sided case, after conditioning on `W`, the active phase is

`d z^2 + 2z(alpha(x)+beta(y)+c) + F(x)+G(y)+2 x^T B y`.       (1.1)

A natural attempt is to use rank-two Plancherel first and then control the remaining one-parameter translation/modulation trace by an `L^2` Gabor-line estimate. Section 3 shows that this exact interface is false, even for cap-one probability-amplitude moduli and arbitrary quadratic same-bank phases, so I do not use it. I then change mechanism on the same target and prove a continuum of integrated `L^q` square estimates. Applied before rank-two Plancherel, this yields a new one-sided packet theorem whose cost at a small physical square coefficient is only logarithmic rather than a fixed negative power.

I found no target-valid counterexample to the stronger universal criterion `int |phi_Q(t)| dt < infinity`; that criterion therefore remains open rather than refuted.

## 2. Completed designated-partner result actually used

The designated partner is account04/B02. I read and use its completed theorem

`QFORM-ZERO-DIAGONAL-TRIPLE-CONTINUITY-v1`,

canonical mathematics

`yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B02/20260922T193108Z-account04-B02-QFORM-r2/REPORT.md`.

If the full ambient form contains a nonsingular physical `3x3` principal block `D` with one exact zero diagonal, the partner proves

`||p_Q||_infinity <= 3*2^(2/3)|det D|^(-1/3)`                         (2.1)

and, crucially for this report,

`int_R |phi_Q(t)|^2 dt <= 6*pi*2^(2/3)|det D|^(-1/3).`                (2.2)

It also proves continuity on that branch. Equation (2.2) is inserted into the low-frequency side of the new general-`q` Fourier estimate in Section 7; this is an actual inequality application, not a citation-only dependency.

## 3. The naive two-sided Gabor-line `L^2` bridge is false

### Proposition 3.1 — `QFORM-TWO-SIDED-GABOR-LINE-L2-FALSE-v1`

Fix any nonzero real `kappa`. For complex amplitudes `b,h` on `R` define

`T_kappa[b,h](z)=int_R b(s-z) h(s) exp(i kappa z s) ds.`               (3.1)

There is no finite constant `C_kappa` such that

`int_R |T_kappa[b,h](z)|^2 dz
 <= C_kappa ||b||_2^2 ||h||_2^2`                                      (3.2)

for all amplitudes whose moduli are probability densities bounded by one.

#### Proof

For `L>=1`, put

`b_L(u)=L^(-1) 1_[0,L](u) exp(i kappa u^2/2)`,
`h_L(s)=L^(-1) 1_[0,L](s) exp(-i kappa s^2/2)`.                       (3.3)

Both moduli are probability densities bounded by one, and

`||b_L||_2^2=||h_L||_2^2=1/L`.                                      (3.4)

Use the exact chirp identity

`exp(i kappa z s)
 =exp(i kappa z^2/2)
  exp(i kappa s^2/2)
  exp(-i kappa(s-z)^2/2)`.                                           (3.5)

The quadratic phases in (3.3) cancel those in (3.5), so

`|T_kappa[b_L,h_L](z)|=(L-|z|)_+/L^2`.                               (3.6)

Hence

`int |T_kappa[b_L,h_L](z)|^2 dz
 =2 L^(-4) int_0^L (L-z)^2 dz
 =2/(3L).`                                                           (3.7)

But the right side of (3.2) would equal `C_kappa/L^2`; their ratio is `2L/(3C_kappa)` and diverges. QED.

The same example tensors with a unit-interval second coordinate, so it defeats the corresponding line-restriction step inside a two-dimensional rank-two bank. The chirps are exactly of the type generated by the arbitrary same-bank quadratic phases `F,G` in (1.1). Thus an argument that removes `A[Z,J]=0` merely by rank-two Plancherel followed by a uniform one-parameter Gabor-line `L^2` restriction estimate cannot be correct.

This is a counterexample to an intermediate proof interface, **not** a counterexample to QFORM and **not** a counterexample to the target-wide `L^1` characteristic-function criterion. It preserves the failure rather than hiding it.

## 4. Uniform scalar-square `L^q` estimate for every `q>2`

The replacement mechanism is an integrated family, not pointwise decay.

### Lemma 4.1 — `QFORM-SHIFTED-SQUARE-LQ-v1`

Let `Z` have a probability density `f<=1`. For `d!=0`, arbitrary real `ell`, and every `q>2`, define

`g_(d,ell)(t)=E exp(i t(d Z^2+2 ell Z)).`

Then

`||g_(d,ell)||_q
 <= C_sq(q) |d|^(-1/q),`                                       (4.1)

where

`C_sq(q)
 =(4*pi)^(1/q) ((q-1)/(q-2))^((q-1)/q).`                            (4.2)

The bound is uniform in `ell` and in the law of `Z` subject only to `f<=1`.

#### Proof

Complete the square. Translation preserves the density cap, and multiplication by the constant phase `exp(-it ell^2/d)` does not alter the norm, so it is enough to treat `d=1`, `ell=0` and scale `t` at the end.

Let `U` have density `f<=1` and let `H` be the density of `U^2`:

`H(w)=[f(sqrt(w))+f(-sqrt(w))]/[2 sqrt(w)]`, `w>0`.                  (4.3)

Put `p=q/(q-1)`, so `1<p<2`. Since `(a+b)^p<=2^(p-1)(a^p+b^p)`, a change of variables `w=x^2` gives

`int_0^infinity H(w)^p dw
 <= int_R f(x)^p |x|^(1-p) dx
 <= int_R f(x)|x|^(1-p) dx.`                                        (4.4)

Among probability densities bounded by one, the final integral is maximized by placing unit mass where the decreasing weight `|x|^(1-p)` is largest, namely on `[-1/2,1/2]`. Therefore

`int H^p <= 2 int_0^(1/2) x^(1-p) dx
          =2^(p-1)/(2-p).`                                          (4.5)

Thus

`||H||_p <= [2^(p-1)/(2-p)]^(1/p).`                                 (4.6)

With the Fourier convention `hat H(t)=int exp(itw)H(w)dw`, Hausdorff--Young gives

`||hat H||_q <= (2*pi)^(1/q)||H||_p
 =(4*pi)^(1/q)((q-1)/(q-2))^((q-1)/q).`                             (4.7)

Finally replace `t` by `dt` to obtain (4.1). QED.

At `q=3`, (4.1) is exactly the previous B02 estimate

`||g_(d,ell)||_3 <=2(2*pi)^(1/3)|d|^(-1/3).`                        (4.8)

Thus the new family is a strict extension, not a new assumption.

## 5. General-`q` one-sided square plus rank-two Fourier theorem

Use the same physical packet as the previous B02 theorem. Split original coordinates as

`{Z} union I union J union W`,

assume

`d=A_ZZ!=0`, `A[Z,J]=0`,                                            (5.1)

and let the exact-rank-two physical cross block `B=A[I,J]` have nonzero singular values `sigma_1,sigma_2` with

`Delta=sigma_1 sigma_2>0`.                                           (5.2)

For a thin SVD `B=L Sigma R^T`, suppose the two-dimensional marginal projection densities of `L^T X_I` and `R^T X_J` have caps `M_L,M_R`. For cap-one product banks one may take `M_L,M_R<=2` by the standard two-dimensional product-projection density theorem already source-pinned in the predecessor report.

### Theorem 5.1 — `QFORM-ONE-SIDED-SQUARE-RANK2-FOURIER-LQ-v2`

For every `q>2`, define

`R_q=(4*pi)^(1/q)
     [2 (q-1)^2/(q-2)]^((q-1)/q),`                                  (5.3)

`H_q=pi sqrt(M_L M_R) Delta^(-1/2)
     |d|^(-1/q) R_q.`                                                (5.4)

Then the full ambient quadratic form, with arbitrary same-bank quadratic terms and arbitrary outside spectrum/couplings consistent with (5.1), satisfies

`||phi_Q||_1
 <=2(q+1) [H_q/(2q)]^(q/(q+1)),`                                 (5.5)

and consequently has a bounded continuous density with

`boxed(
 ||p_Q||_infinity
 <= C_q (M_L M_R)^(q/[2(q+1)])
    |d|^(-1/(q+1)) Delta^(-q/[2(q+1)])
)`                                                                  (5.6)

where

`C_q=(q+1)/pi * [pi R_q/(2q)]^(q/(q+1)).`                            (5.7)

At `q=3`, `C_3=16/6^(3/4)` and (5.6) exactly recovers the predecessor theorem.

#### Proof

Condition on `W=w`, disintegrate the two rank-two banks as in the predecessor proof, and let `A_w(t)` denote the `L^2` norm of the left projected complex amplitude after the scalar `Z` integral is kept inside it. Jensen and the cap `p_P^2<=M_L p_P` give

`A_w(t)^2 <= M_L E_X |g_(d,ell_w(X))(t)|^2`.                         (5.8)

Because `q/2>1`, Minkowski in `L^(q/2)` and Lemma 4.1 imply

`||A_w||_q
 <=sqrt(M_L) C_sq(q)|d|^(-1/q).`                                 (5.9)

This bound is uniform in `w`; averaging in `W` preserves it. Rank-two bilinear Plancherel is unchanged from the predecessor and yields

`|phi_Q(t)|
 <= pi sqrt(M_R) Delta^(-1/2)|t|^(-1) Abar(t)`.                     (5.10)

Let `q'=q/(q-1)`. For `T>0`, Holder gives

`int_(|t|>T) |t|^(-1) Abar(t) dt
 <=||Abar||_q
   [2 int_T^infinity t^(-q') dt]^(1/q')
 =||Abar||_q [2(q-1)]^((q-1)/q) T^(-1/q).`                          (5.11)

Combining (5.9)--(5.11) gives the tail `H_q T^(-1/q)`. On `|t|<=T`, use `|phi_Q|<=1`, obtaining

`||phi_Q||_1 <=2T+H_q T^(-1/q).`                                    (5.12)

The optimum is

`T=[H_q/(2q)]^(q/(q+1))`,                                           (5.13)

and at that point the right side is exactly (5.5). Fourier inversion gives a continuous density and division by `2*pi` gives (5.6). QED.

## 6. New near-isotropic corollary: only logarithmic loss

The value of the `q`-family is not mainly a constant improvement at `q=3`; it lets the exponent move when the physical square coefficient is tiny.

Rewrite the coefficient factor in (5.6) as

`|d|^(-1/(q+1)) Delta^(-q/[2(q+1)])
 =Delta^(-1/2) (sqrt(Delta)/|d|)^(1/(q+1)).`                         (6.1)

For `q>=4`, the elementary bounds

`(4*pi)^(1/q)<1.9`,
`(q-1)^2/(q-2)=q+1/(q-2)<=9q/8`,
`q+1<=5q/4`

imply

`C_q<=3q`.                                                           (6.2)

For cap-one product banks, `M_L,M_R<=2`, so the projection-cap factor in (5.6) is at most `2`.

Set

`L=log_+(sqrt(Delta)/|d|)`,
`q=max(4,L)`.                                                        (6.3)

Then

`(sqrt(Delta)/|d|)^(1/(q+1))<=e`,                                   (6.4)

and (5.6) yields the scale-invariant logarithmic estimate

`boxed(
 ||p_Q||_infinity
 <=6 e max{4, log_+(sqrt(Delta)/|d|)} Delta^(-1/2).
)`                                                                  (6.5)

Thus on this physical packet the previous fixed-`q=3` near-isotropic cost `|d|^(-1/4)` is replaced by a logarithm as `|d|/sqrt(Delta)->0`. This does **not** remove the one-sided isolation (5.1) and therefore is not a full-target closure, but it substantially weakens the quantitative obstruction created by a small scalar pivot.

## 7. Actual partner application: general-`q` low/high frequency hybrid

Assume, in addition to Theorem 5.1, that the ambient form contains a nonsingular physical `3x3` block `D` with an exact zero diagonal. The designated account04/B02 theorem gives (2.2). Hence, by Cauchy--Schwarz on `[-T,T]`,

`int_(|t|<=T)|phi_Q(t)|dt <= A_D T^(1/2)`,                           (7.1)

where

`A_D=2^(1/3) sqrt(12*pi) |det D|^(-1/6).`                            (7.2)

Combine this with the new tail from Section 5:

`||phi_Q||_1 <= A_D T^(1/2)+H_q T^(-1/q).`                           (7.3)

Optimizing gives

`T=[2H_q/(q A_D)]^(2q/(q+2))`                                       (7.4)

and therefore

`boxed(
 ||p_Q||_infinity
 <= (q+2)/(4*pi) A_D
    [2H_q/(q A_D)]^(q/(q+2)).
)`                                                                  (7.5)

At `q=3` this reduces to the predecessor's partner-hybrid estimate. Equation (7.5) is a genuinely new continuum of partner-assisted inequalities and can be optimized against the relative sizes of the zero-diagonal determinant, the square coefficient, and the rank-two cross determinant.

The partner's direct bound (2.1) remains available; on any concrete overlap one should take the minimum of (2.1), (5.6), and (7.5).

## 8. What this run settles and what remains unpaid

### Settled in this run

1. The obvious two-sided extension of the predecessor through a one-parameter Gabor-line `L^2` restriction is rigorously false; the failure occurs even with cap-one probability-amplitude moduli and exactly quadratic chirps.
2. The shifted physical-square estimate is upgraded from one `L^3` point to every `L^q`, `q>2`, with explicit constants.
3. The one-sided square/rank-two packet acquires the full tradeoff (5.6), and its small-square cost improves from a power to the logarithmic bound (6.5).
4. The completed account04/B02 `L^2` result is applied to produce the hybrid family (7.5).

### Not settled

The universal conjecture remains **OPEN**. I have no exact-target counterexample to `int|phi_Q|<infinity`, so that stronger criterion remains neither proved nor refuted globally.

The first unpaid B02 implication is still the genuinely two-sided case (1.1), but Section 3 narrows what can work: a proof must retain more than `L^2` bank norms after the rank-two Plancherel step. Viable next interfaces are:

- a translation-uniform **fractional trace** that uses the cap-one product provenance before the Gabor-line restriction;
- a coupled `L^q` estimate on the full three-variable square/cross packet, rather than a restricted STFT estimate;
- or an exhaustive product-preserving structural reduction routing the two-sided configuration into the completed full-matrix indefinite-pair, ridge-window, grouped-coordinate, or zero-diagonal branches.

The exact zero/near-zero pivot remains distinct: the logarithmic estimate is for `d!=0`; exact `d=0` must use a valid zero-diagonal/product-geometry theorem such as the designated partner when its determinant hypothesis holds.

## 9. Correction compliance

No step uses law-uniform pointwise quadratic-phase decay, post-rotation independence, an arbitrary-joint coarea theorem, a positive conditional projection-height moment, an unrestricted fiber supremum, a fixed-good-minor implication from `s_3(A)>=1`, or the false idea that a conditional density cap substitutes for independence. The Gabor-line failure is recorded as an intermediate-mechanism correction only. All product-projection uses remain marginal-density statements, and the full-target status stays OPEN.
