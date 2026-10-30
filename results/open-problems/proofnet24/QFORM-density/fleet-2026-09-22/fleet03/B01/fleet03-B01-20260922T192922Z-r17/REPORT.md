# QFORM fleet03/B01 — translation-uniform averaged Fresnel theorem

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `fleet03-B01-20260922T192922Z-r17`  
Assignment: `Oscillatory replacement`  
Status: `PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN / WITHOUT_VERIFIED_BRAIN`

## 1. Target and live correction state

The parent target remains open: for arbitrary `n`, independent real coordinates `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove that `Q=X^T A X` has an essentially bounded density with one universal constant, or produce a valid target counterexample. Continuity is tracked separately.

Fresh owner control at the start of this run was revision `2026-09-22.14`, with QFORM as the sole research target. I preserve the live corrections: there is no law-uniform pointwise quadratic-phase decay over cap-one densities; arbitrary spectral rotations destroy coordinate independence; unrestricted joint-coarea and positive conditional-fiber-moment shortcuts are invalid. Nothing below uses those premises.

The new mechanism is an **averaged-in-frequency replacement** for the false pointwise Fresnel estimate. It is translation-uniform, has an explicit optimal exponent range, and yields an actual signed-Fejer/density closure whenever three original independent quadratic pivots can be exposed without mutual cross terms, even with arbitrary couplings to all conditioned outside coordinates.

## 2. Mandatory phase-aligned counterexample is preserved

Fix any `s!=0` and `delta>0`. The set

`E(s,delta)={x: dist(s x^2,2 pi Z)<=delta}`

has infinite Lebesgue measure. Choose a measurable subset `E` of measure one and let `f=1_E`. Then `f` is a probability density with `0<=f<=1` and

`Re int exp(i s x^2) f(x) dx >= cos(delta)`.

Therefore no estimate of the form `|E exp(i t X^2)| <= C |t|^{-alpha}` with `alpha>0` can hold uniformly over all cap-one input laws. The theorem below replaces pointwise decay by a uniform `L^p(dt)` estimate.

## 3. Sharp averaged one-dimensional theorem

### Theorem 3.1 — `QFORM-TRANSLATED-FRESNEL-LP-v1`

Let `X` have probability density `f` on `R` with `0<=f<=1`. Let `a!=0` and `b,c` be arbitrary reals. Define

`F_(a,b,c)(t)=E exp(i t (a X^2+b X+c))`.

For every `p>2`,

`||F_(a,b,c)||_(L^p(R_t)) <= C_p |a|^(-1/p)`,                (3.1)

where

`C_p=[4 pi (p-1)]^(1/p) * [(p-1)/(p-2)]^((p-1)/p)`.          (3.2)

Equivalently,

`||F_(a,b,c)||_p^p <= 4 pi (p-1) [(p-1)/(p-2)]^(p-1) / |a|`. (3.3)

The estimate is uniform in the translation parameter `b/(2a)` and in the additive phase `c`.

The endpoint `p=2` is impossible uniformly, already for `X~Unif[-1/2,1/2]` and phase `X^2`: in that example `F` is not in `L^2(R)`.

#### Proof

Complete the square:

`a X^2+bX+c = a (X-m)^2 + c'`,

with `m=-b/(2a)`. The constant phase `exp(i t c')` does not affect any `L^p` norm, so it suffices to study `Y=(X-m)^2`.

Let `q` be the density of `Y`. For `y>0`,

`q(y)=[f(m+sqrt(y))+f(m-sqrt(y))]/[2 sqrt(y)]`.              (3.4)

Fix `1<r<2`. Substituting `y=x^2` and using

`(u+v)^r <= 2^(r-1)(u^r+v^r)`

gives the exact convenient majorization

`||q||_r^r
 <= int_R f(u)^r |u-m|^(1-r) du`.                         (3.5)

Because `f^r<=f`, for any `R>0`,

`int f(u)^r |u-m|^(1-r) du
 <= int_(|u-m|<=R) |u-m|^(1-r) du
    + R^(1-r) int_(|u-m|>R) f(u)du`
` <= 2 R^(2-r)/(2-r) + R^(1-r)`.                             (3.6)

The right side is minimized at `R=(r-1)/2`. Substitution yields

`||q||_r^r <= ((r-1)/2)^(1-r)/(2-r)`.                        (3.7)

Now set `r=p/(p-1)`, so `p=r/(r-1)>2`. With the Fourier convention

`hat q(t)=int_R exp(i t y) q(y)dy`,

Riesz-Thorin between `L^1->L^infinity` (norm one) and Plancherel `L^2->L^2` (norm `(2 pi)^(1/2)`) gives

`||hat q||_p <= (2 pi)^(1/p) ||q||_r`.                        (3.8)

Scaling `Y` by `a` multiplies the `L^r` norm of its density by `|a|^(1/r-1)=|a|^(-1/p)`. Combining (3.7)-(3.8), then using

`r-1=1/(p-1)`, `2-r=(p-2)/(p-1)`,

produces exactly (3.1)-(3.3).

For the endpoint obstruction, take `X~Unif[-1/2,1/2]`. Then the density of `X^2` is

`q(y)=y^(-1/2) 1_(0,1/4)(y)`,

which is not in `L^2`. If its Fourier transform belonged to `L^2`, the converse Plancherel theorem would force `q` to agree almost everywhere with an `L^2` function, a contradiction. Hence `||F||_2=infinity`. QED.

### Explicit cubic case

At `p=3`,

`C_3=(32 pi)^(1/3)=4.649789406...`,                         (3.9)

and therefore

`||F_(a,b,c)||_3^3 <= 32 pi / |a|`.                           (3.10)

This is the exact exponent needed for a three-factor absolute-time closure.

## 4. A fully coupled ambient branch from three uncoupled physical pivots

### Theorem 4.1 — `QFORM-THREE-PHYSICAL-INDEPENDENT-PIVOTS-v1`

Let `X_1,...,X_n` be independent with densities bounded by one, and let `A` be any real symmetric matrix. Suppose there are three distinct original-coordinate indices `i,j,k` such that

`A_ij=A_ik=A_jk=0`,                                           (4.1)

and

`a_i=A_ii`, `a_j=A_jj`, `a_k=A_kk`

are all nonzero. No restriction is imposed on any other entry of `A`: the three selected coordinates may couple arbitrarily to every outside coordinate, and the outside block may have arbitrary rank and signature.

Then `Q=X^T A X` has a **continuous** density and

`||p_Q||_infinity <= 16 |a_i a_j a_k|^(-1/3)`.                (4.2)

In particular, if the three selected diagonal magnitudes are at least one, then

`||p_Q||_infinity <=16`.                                      (4.3)

#### Proof

Condition on all original coordinates outside `S={i,j,k}`. For every fixed outside configuration `z`, (4.1) gives

`Q = c(z)
   + [a_i X_i^2 + l_i(z) X_i]
   + [a_j X_j^2 + l_j(z) X_j]
   + [a_k X_k^2 + l_k(z) X_k]`.                               (4.4)

The three selected coordinates remain independent under this conditioning. Hence the conditional characteristic function factors:

`phi_z(t)=exp(i t c(z)) F_i(t;z) F_j(t;z) F_k(t;z)`.           (4.5)

Theorem 3.1 with `p=3` is uniform in every linear coefficient `l_s(z)`, so

`||F_s(.;z)||_3 <= (32 pi)^(1/3)|a_s|^(-1/3)`.                (4.6)

Hölder in the time variable gives

`int_R |phi_z(t)| dt
 <= product_(s in S) ||F_s(.;z)||_3
 <= 32 pi |a_i a_j a_k|^(-1/3)`.                              (4.7)

Averaging over the outside coordinates and using Tonelli/triangle inequality,

`int_R |phi_Q(t)|dt
 <= E_z int_R |phi_z(t)|dt
 <=32 pi |a_i a_j a_k|^(-1/3)`.                               (4.8)

Thus `phi_Q in L^1`. Fourier inversion supplies a continuous density in `C_0(R)` and

`||p_Q||_infinity
 <=(1/(2 pi)) ||phi_Q||_1
 <=16 |a_i a_j a_k|^(-1/3)`.                                  (4.9)

QED.

### General independent-set version

The same argument works for any set `S` of pairwise uncoupled original coordinates (`A_rs=0` for distinct `r,s in S`). If exponents `p_s>2` satisfy

`sum_(s in S) 1/p_s =1`,

then

`||p_Q||_infinity
 <=(1/(2 pi)) product_(s in S) [ C_(p_s) |A_ss|^(-1/p_s) ]`.  (4.10)

The restriction `p_s>2` shows analytically why at least three one-dimensional averaged Fresnel factors are required by this route: two factors would force an unavailable uniform `L^2` endpoint.

## 5. Designated partner fleet04/B01 applied to an actual inequality

The designated partner's completed theorem `QFORM-SIGNED-FEJER-EXACT-INTERFACE-v1` defines

`D_T mu(y)=(1/(2 pi)) int_(-T)^T (1-|t|/T)
             Re(exp(-ity) phi_mu(t)) dt`

and proves

`||p_mu||_infinity = sup_(T>0,y) D_T mu(y)`

for laws with bounded density, with the converse implication as well. Canonical partner source:

`yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79:proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B01/20260922T141507Z-b01-qform-fejer-r1/REPORT.md`.

Applying that result to (4.2) gives the genuine averaged-frequency bound

`sup_(T>0,y) D_T law(Q)(y)
 <=16 |a_i a_j a_k|^(-1/3)`.                                  (5.1)

This is a direct application to a newly proved target-level branch, not a citation-only mention. The same bound also follows from (4.8) by the absolute majorant, but the partner theorem identifies the exact signed-Fejer quantity with the density norm and cleanly separates essential boundedness from continuity.

## 6. Why this is relevant but not a full solution

The full QFORM conjecture is **not** proved here. Three large spectral eigenvalues do not force three original coordinates satisfying both `|A_ii|>=1` and pairwise zero physical couplings. A dense rotated rank-three matrix can have all physical coordinates mutually coupled and every diagonal entry small.

What is paid is the precise averaged-frequency substitute for the false pointwise route:

1. every single cap-one quadratic phase is uniformly in `L^p(dt)` for every `p>2`, uniformly over arbitrary linear translations;
2. `p=2` is genuinely unavailable, so this cannot be repaired by pretending a two-factor Plancherel endpoint exists;
3. three independent original-coordinate factors close absolutely in time at `p=3` even when they retain arbitrary couplings to the conditioned outside variables;
4. the remaining structural debt is therefore to create or emulate three such product-preserving factors in the genuinely rotated/dense case, rather than to seek a false pointwise stationary-phase estimate.

This matches the live proof-first priority: a future grouped-coordinate/ridge reduction can use (3.1) as a dimension-free local module provided it preserves enough original-coordinate product structure to obtain three time factors.

## 7. Constants and finite arithmetic check

The formula gives

`C_3=(32 pi)^(1/3)=4.649789406038505...`

and

`C_3^3/(2 pi)=16`.

These are algebraic consequences of the proof, not numerical evidence for the parent conjecture.

## 8. Next unpaid implication

The highest-value next step is a **product-preserving three-factor extraction theorem**: from the bare hypothesis that `A` has at least three eigenvalues of modulus at least one, either expose a controlled branch already covered by existing localized/ridge theorems, or construct three grouped original-coordinate oscillatory factors to which Theorem 3.1 can be applied without rotating away independence. Any such extraction must survive dense rank-three frames and the known singleton-plus-two-banks obstruction.
