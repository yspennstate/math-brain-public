# Normalized signed-convolution tariffs: tensor obstruction, code-support loss, and a Boolean surgery repair

30 September 2026, interactive FEI continuation. **Full Friedgut–Kalai FEI remains OPEN.**

## Result first

This report proves three scoped facts and one constructive repair. It does not prove a universal entropy–influence inequality.

1. The unnormalized logarithmic all-shift tariff proposed in the September 22 source cannot satisfy its all-source KL lower-payment target with any fixed positive coefficient and any additive `O(I)` error. An explicit three-variable Boolean factor makes the tariff exponential under disjoint tensor products while the exact KL and influence stay linear.
2. Dividing the tariff by its total squared-convolution mass makes it exactly additive on tensor amplitude vectors. This normalization preserves the earlier sparse-suspension calibration, including its coefficient `1/4`.
3. Conditioning the reference on the actual Fourier support before computing this normalized tariff can lose an unbounded fraction of the indispensable shape KL. Paired-coordinate lifts of one-point defects give `T_conditioned/I -> 0` but `K_shape/I -> infinity`. The exact support refund is only `O(I)`.
4. For that same family, retaining the unconditioned product reference and completing zero Fourier signs by `+1` restores the missing scale: `T_completed/4 - K_shape = o(I)`. The completed signs are not fictional: they are exactly the signs of the Boolean function obtained by flipping its negative value at the origin. A general sign-completion lemma establishes this realization for every Boolean function with spectral zeros in dimension at least two.

The broad normalized transfer is still unproved. Moreover, its low-influence full-support form carries the full FEI difficulty; it must not be advertised as an easier solved subproblem. The separate local-erasure work of the concurrent continuation proves this admission implication and is not used as a premise of any theorem here.

## 1. Setup, exact source, and scope

Use signs on the uniform cube. For a Boolean function `g`, put

\[
a_S=\widehat g(S),\qquad P(S)=a_S^2,\quad
\alpha_i=\sum_{S\ni i}P(S),\quad I(g)=\sum_i\alpha_i.
\]

Let `Q` be the product Bernoulli law with marginals `alpha_i`, and let `A=supp(P)`. Write

\[
K_{\rm full}=D_2(P\Vert Q)=\sum_i h_2(\alpha_i)-H(P),
\]
\[
K_{\rm supp}=-\log_2 Q(A),\qquad
K_{\rm shape}=D_2(P\Vert Q(\cdot\mid A))
=K_{\rm full}-K_{\rm supp}.
\tag{1.1}
\]

The old-coordinate functions `g` in the explicit families below have positive interior coordinate marginals. A later fresh dictator suspension has one deterministic marginal, handled explicitly in the suspension paragraph; none of the formulas condition on an event of zero probability.

There are two reference amplitude vectors, never silently interchanged:

* **Support-conditioned:** `b_S=sgn(a_S) sqrt(Q(S)/Q(A))` on `A`, and zero otherwise.
* **Completed unconditioned:** choose signs `epsilon_S=sgn(a_S)` on `A` and explicit signs in `{−1,+1}` on its complement, and put `b_S=epsilon_S sqrt(Q(S))` everywhere.

Both have squared norm one. Define the XOR autocorrelation and its tariffs by

\[
C_b(U)=\sum_S b_S b_{S\triangle U},\qquad v_b(U)=C_b(U)^2,
\]
\[
Z_b=\sum_Uv_b(U),\qquad
L_b=\sum_Uv_b(U)\log_2\frac1{v_b(U)},\qquad T_b=\frac{L_b}{Z_b}.
\tag{1.2}
\]

Here `C_b(empty)=1`, `|C_b(U)|<=1` by Cauchy–Schwarz, and `0 log(1/0)=0`. Thus including the empty shift changes neither `L` nor the source's nonempty-shift definition. Crucially, `v_b` is generally **not** a probability distribution. The law `mu_b=v_b/Z_b` satisfies

\[
T_b=H(\mu_b)-\log_2 Z_b.
\tag{1.3}
\]

The direct predecessor is account04/B15's [critical logarithmic all-shift tariff](https://github.com/yspennstate/math-open-problems/blob/0336e6fd68a55ed75f92633e80ba668bdf124290/proofnet24/P03-fei/fleet-2026-09-21/account04/B15/20260922T101332Z-log-convolution-critical-tariff/REPORT.md), blob `03fbfa09b30b816137f344d926732a9ac794e193`. Its Section 4 calibrates `L/4` on sparse one-point suspensions; Section 6 asks for a support-conditioned all-source lower payment. That calibration remains correct. We refute an all-source extension, not its proved family theorem and not a version explicitly restricted to composition-prime sources.

To identify these quantities with the earlier nonempty I-projection convention, suspend any `g` by a fresh sign `y`: `F(y,x)=y g(x)`. Its spectral law has `y` deterministically present. Consequently every law with the required marginals is already nonempty, the maximum-entropy law is exactly the product `Q` on the old coordinates, and `K_occ(F)=K_full(g)`. Support conditioning gives exactly (1.1). Also `I(F)=1+I(g)`.

## 2. Tensor law and a definitive all-source obstruction

### Theorem 2.1. Exact tensor identities

For normalized real amplitude vectors `b` and `c` on disjoint coordinates,

\[
C_{b\otimes c}(U,V)=C_b(U)C_c(V),\quad Z_{b\otimes c}=Z_bZ_c,
\]
\[
L_{b\otimes c}=Z_cL_b+Z_bL_c,\qquad
T_{b\otimes c}=T_b+T_c.
\tag{2.1}
\]

**Proof.** The correlation sum factors. Squaring gives `v_b tensor v_c`; summing gives the partition-function identity. Expand `log(1/(v_b v_c))=log(1/v_b)+log(1/v_c)` and sum. Zero entries contribute zero by continuity. Divide by `Z_b Z_c`. No Booleanity is needed for this identity. QED.

In particular,

\[
L_{b^{\otimes k}}=kZ_b^{k-1}L_b,\qquad T_{b^{\otimes k}}=kT_b.
\tag{2.2}
\]

The support-conditioned amplitude for an actual Boolean tensor product is the amplitude tensor: supports, product reference laws, conditioning probabilities and nonzero signs all factor. For completed unconditioned amplitudes this assertion requires choosing the **product of the factor completions**. A rule assigning `+` to every zero of an arbitrary product need not make this choice. We do not claim otherwise.

### Theorem 2.2. Explicit exponential failure of the raw tariff target

Let `g_3` be minus one at the origin of three bits and plus one elsewhere. Its Fourier coefficients are `3/4` at the empty set and `−1/4` at the other seven sets. All coordinate influences are `1/4`. For its sign-aligned product reference, the squared nonempty correlations at shift weights 1, 2, and 3 are respectively

\[
\frac3{256},\quad\frac9{256},\quad\frac{27}{256}.
\]

Consequently

\[
Z=\frac{319}{256}>1,\quad
L=\frac{9\log_2(256/3)+27\log_2(256/9)+27\log_2(256/27)}{256}>0,
\]
\[
K=2-\frac98\log_2 3,\qquad I(g_3)=\frac34.
\tag{2.3}
\]

For the genuine balanced Boolean family

\[
F_k=y\prod_{j=1}^k g_3(x^{(j)}),
\]

the exact quantities are

\[
K_{\rm occ}(F_k)=kK,\quad I(F_k)=1+\frac{3k}4,
\quad L(F_k)=kZ^{k-1}L.
\tag{2.4}
\]

Its product reference has exactly the same support as its actual spectrum, so support conditioning makes no change. For every fixed `theta>0` and every finite `kappa`,

\[
K_{\rm occ}(F_k)<\theta L(F_k)-\kappa I(F_k)
\]

for sufficiently large `k`. Thus no positive fixed coefficient on the raw all-shift tariff yields the proposed universal KL lower payment, even with an arbitrary additive influence error.

**Proof.** Equations (2.3) follow either by direct eight-entry correlation or by Lemma 3.1 below. Actual entropy, marginal entropy and influence add under the disjoint tensor product. The fresh suspension is deterministic in Fourier space. Apply (2.2); exponential growth dominates all linear terms. QED.

The exact-rational logarithm checker certifies `(L_k/4-K_k)/I(g_3^tensor k)>328` at `k=32`. For the balanced suspended family the corresponding ratio is greater than 315. This finite number is illustrative; the proof rules out every constant, not only those numbers.

### Normalization retains the earlier successful calibration

For the original one-point family below with reference parameter `t=p`, the source proves `L/(4mp)=m-3+o(1)`. The elementary bound in Section 5 gives `Z<=exp(4mp)=1+O(mp)`. Hence `L-T=O(m^3p^2)=o(mp)`. Normalizing by `Z` therefore changes neither the critical coefficient `1/4` nor the source's additive-`I` asymptotic correction.

## 3. A paired-support Boolean family and an exact correlation formula

Let

\[
p=2^{1-m},\quad g_m(x)=1-2\mathbf1_{\{x=0\}},\quad m\ge2.
\]

Its coefficient at the empty set is `1-p` and every other coefficient is `−p`. Put

\[
H_m=-(1-p)^2\log_2(1-p)^2-(2^m-1)p^2\log_2p^2.
\tag{3.1}
\]

Then `I(g_m)=mp` and `H_m/(mp)->4`.

Define its pair lift in sign coordinates by

\[
f_m(x_1,\ldots,x_{2m})
=g_m(x_1x_2,x_3x_4,\ldots,x_{2m-1}x_{2m}).
\tag{3.2}
\]

The support `A_m` consists exactly of unions of the `m` designated pairs. The coefficients on this support equal those of `g_m`. Thus

\[
H(f_m)=H_m,\qquad I(f_m)=2mp,\qquad \alpha_i=p\ (1\le i\le2m).
\tag{3.3}
\]

For the product reference `Q=Ber(p)^tensor 2m`, define

\[
d=(1-p)^2+p^2,\qquad Q(A_m)=d^m,\qquad \beta=\frac{p^2}{d}.
\tag{3.4}
\]

Conditioned on `A_m`, the `m` pair-inclusion indicators are independent Bernoulli `beta`. Therefore

\[
K_{\rm shape}=2mh_2(p)-H_m+m\log_2 d,
\quad K_{\rm supp}=-m\log_2d.
\tag{3.5}
\]

### Lemma 3.1. One-point sign pattern at any reference parameter

For any `0<t<1`, give the product `Ber(t)^tensor m` amplitudes a positive sign at the empty set and negative signs elsewhere. At a nonempty shift of size `r`, its squared correlation is

\[
v_r=t^r(1-t)^r[2^r-4(1-t)^{m-r}]^2.
\tag{3.6}
\]

**Proof.** Put `a=sqrt(1-t)`, `b=sqrt(t)`. The inverse Walsh transform of this amplitude is `B(x)=2a^m-product_i(a+bx_i)`. Squaring it, the coefficient at a nonempty shift of size `r` is `(2ab)^r-4a^(2m-r)b^r`. Factor `(ab)^r` and square. QED.

For the support-conditioned pair-lift amplitude, correlations outside `A_m` vanish, while the other correlations are given by (3.6) with `t=beta`. Its full tariff is therefore computable from `m` shells with multiplicity `binomial(m,r)`.

## 4. Support conditioning loses the necessary scale

### Theorem 4.1. Unbounded shape-KL under-recovery

For the family (3.2),

\[
\frac{K_{\rm supp}}{I(f_m)}\longrightarrow\frac1{\ln2},\qquad
\frac{K_{\rm shape}}{I(f_m)}=m-3+o(1),
\tag{4.1}
\]

whereas its support-conditioned normalized tariff satisfies

\[
T_{\rm conditioned}=4m\beta\left[\log_2\frac1{4\beta}+o(1)\right],
\]
\[
\frac{T_{\rm conditioned}}{I(f_m)}\sim4mp\longrightarrow0.
\tag{4.2}
\]

In particular no finite constants `A,B` can make

\[
K_{\rm shape}(f_m)\le A T_{\rm conditioned}(f_m)+B I(f_m)
\]

hold for every `m`. The same is true with the raw conditioned tariff `L`, since its `Z` tends to one. This is an under-recovery obstruction, distinct from Theorem 2.2's false lower payment. It does not by itself refute a lower bound `K_shape>=T/4-kappa I`.

**Proof.** Taylor expansion at zero gives `−log₂d=2p/ln2+O(p²)` and `beta=p²(1+O(p))`. Also

\[
H_m=4mp+(-4+2/\ln2)p+O(mp^2).
\tag{4.3}
\]

Using `h₂(p)=p log₂(1/p)+p/ln2+O(p²)` in (3.5) and dividing by `2mp` proves (4.1), since `log₂(1/p)=m-1`.

For the tariff, the singleton formula (3.6) is `v_1=4beta[1+O(m beta)]`. Its `m` singleton shifts contribute `4m beta[log₂(1/(4beta))+o(1)]`; the additive `o(1)` uses `m beta log(1/beta)->0`.

For every real unit amplitude with product magnitudes `Ber(beta)`, the bound in Section 5 gives `v_U<=(4beta)^{|U|}`. For sufficiently large `m`, `x log₂(1/x)` is increasing on `[0,(4beta)^2]`. Hence all shells `r>=2` together contribute at most

\[
\log_2(1/(4\beta))\sum_{r\ge2}\binom mr r(4\beta)^r
=O(m^2\beta^2\log(1/\beta))=o(m\beta).
\]

Finally `1<=Z<=(1+4beta)^m=1+O(mbeta)`, so normalization changes this result by `o(mbeta)`. Substitute `beta~p²` and `log₂(1/(4beta))=2m-4+o(1)`. QED.

The FEI ratio of this family tends to **two**, by (3.3). It is emphatically not a counterexample to FEI. A fresh dictator suspension identifies (4.1) with the older nonempty I-projection convention; asymptotic errors are measured against the old-coordinate influence, as in the source sparse-suspension calibration.

## 5. Constructive recovery by an unconditioned Boolean-compatible sign completion

Retain `Q=Ber(p)^tensor 2m`. Give its amplitudes a negative sign precisely at nonempty members of `A_m`, and a positive sign everywhere else. This matches every actual nonzero Fourier sign of `f_m`.

### Theorem 5.1. Exact two-shell formula

For a shift `U`, let `s` be the number of pairs containing exactly one coordinate of `U`, and `t` the number containing both. For nonempty `U`, put `k=s+2t`. Its squared correlation is

\[
v_{s,t}=[p(1-p)]^k\begin{cases}
[4^t-4(1-p)^{2m-2t}]^2,&s=0,\\
[2^{s+2t}-4\,2^t d^{m-s-t}+4(1-p)^{2m-s-2t}]^2,&s>0.
\end{cases}
\tag{5.1}
\]

The number of such shifts is `binomial(m,s) binomial(m-s,t) 2^s`.

**Proof.** With `a=sqrt(1-p)`, `b=sqrt(p)`, let

\[
A(x)=\prod_{i=1}^{2m}(a+bx_i),\quad
V(x)=\prod_{j=1}^m(a^2+b^2x_{2j-1}x_{2j}),\quad c=a^{2m}.
\]

The completed amplitude has inverse transform `B=A-2V+2c`. Expand

\[
B^2=A^2+4V^2+4c^2-4AV+4cA-8cV.
\]

In one pair, the coefficients of `AV` at occupancies zero, one, two are `d`, `ab`, `2a²b²`. The nonconstant coefficients of `V` and `V²` vanish on singly occupied pairs. If `s>0`, only `A²`, `−4AV`, and `4cA` remain; factor `(ab)^k` to obtain (5.1). If `s=0,t>0`, the `4V²` and `−4AV` coefficients cancel, and `4cA−8cV` supplies the stated remaining term. The zero shift is one by normalization. QED.

### Theorem 5.2. The completed tariff recovers the lost shape KL

For this explicit unconditioned completion,

\[
\frac{T_{\rm completed}}{4I(f_m)}=m-3+o(1),
\qquad
\boxed{\ T_{\rm completed}/4-K_{\rm shape}=o(I(f_m)).\ }
\tag{5.2}
\]

**Proof.** At a singleton physical shift, (5.1) gives

\[
C(e_i)=2\sqrt{p(1-p)}
\left[1-2d^{m-1}+2(1-p)^{2m-1}\right],
\]

so `v(e_i)=4p[1+O(mp)]`. There are `2m` such shifts. Their total contribution to `L` is therefore

\[
8mp[m-3+o(1)].
\tag{5.3}
\]

Here the cumulative relative-error contribution, divided by `mp`, is `O(m²p)=o(1)`.

For completeness, any sign vector with product reference magnitudes satisfies the sign-independent Hellinger cap

\[
|C(U)|\le\sum_S\sqrt{Q(S)Q(S\triangle U)}
=\prod_{i\in U}2\sqrt{\alpha_i(1-\alpha_i)}.
\tag{5.4}
\]

For this family, `v(U)<=(4p)^{|U|}` and `Z<=(1+4p)^(2m)=1+O(mp)`. The same monotonicity and binomial-tail calculation as above bounds the entropy from shifts of size at least two by `O(m³p²)=o(mp)`. Normalization changes (5.3) by another `O(m³p²)`. Divide by `4I=8mp` and compare (4.1). QED.

This supplies an explicit successful repair on the very family that defeats support conditioning. It does not establish the general transfer, and it does not show that the completed tariff always recovers the full needed Bellman deficit.

### Theorem 5.3. One-point surgery realizes the zero-sign completion

Let `f` be Boolean on `n>=2` bits and suppose some Fourier coefficient is zero. For any physical point `x0`, flip just the value `f(x0)` to obtain `f'`. Then every Fourier coefficient of `f'` is nonzero; the signs of all previously nonzero coefficients are unchanged; and at every previous zero the new sign is

\[
-f(x_0)\chi_S(x_0).
\tag{5.5}
\]

**Proof.** Write `N=2^n` and let `r` be the number of negative truth-table values. For nonempty `S`, the integer Walsh numerator is `−2 sum_(f(x)=−1) chi_S(x)`; at the empty set it is `N−2r`. If `r` were odd, every numerator would be `2 mod 4`, and none could vanish. Thus `r` is even and every numerator is divisible by four. A one-point flip adds `−2f(x0)chi_S(x0)` to every numerator. A nonzero multiple of four cannot change sign under a change of magnitude two, and a zero becomes the indicated nonzero number. Every resulting numerator is `2 mod 4`, so the new spectrum is full. QED.

For `f_m`, the value at the origin is negative and `chi_S(0)=1`; therefore (5.5) is exactly the `+` completion of Theorem 5.2. The reference magnitudes in that theorem are still the product marginals of **the original** `f_m`, not those of `f'_m`. The surgery proves the signs are Boolean-realizable, not that the reference amplitudes themselves are a Boolean spectrum.

## 6. What survives, what fails, and the exact open step

Retain the normalized functional `T=L/Z`, the exact tensor identities, the Hellinger cap, the explicit Boolean surgery completion, and the repaired pair-lift calibration. Retire only the following precise statements:

* `K_occ >= theta L-kappa I` universally for fixed `theta>0`, for the raw all-shift tariff: false by Theorem 2.2.
* A claim that support-conditioned `L` or `T` recovers arbitrary shape KL up to fixed-factor and additive-influence errors: false by Theorem 4.1.

A possible continuation is to choose a source-defined, Boolean-compatible completion of the unconditioned reference and attempt

\[
D_2(P\Vert Q)\ge\tfrac14 T_b-\kappa I(g)
\tag{6.1}
\]

with one finite constant and all quantifiers stated. This report does not prove (6.1), does not establish a dimension-independent remainder beyond the explicit families, and does not establish a globally tensor-compatible completion rule. For full-support sources there is no sign-choice ambiguity, but the small-total-influence regime of (6.1) already implies an FEI bound through rare activation. The simultaneous local-erasure continuation supplied that admission calculation; no claim here depends on treating (6.1) as easier than FEI.

Any proof would also need to connect the extracted tariff to the exact needed entropy payment. A lower bound on KL alone is not enough if the statistic under-recovers on a source. Theorem 4.1 is a concrete demonstration of that distinction.

## 7. Verification and provenance

`python verify.py` uses only the Python standard library. Its committed output records the SHA-256 of its executed bytes. It verifies:

* Actual integer Walsh transforms of the pair-lift Boolean truth tables through `m=6` (12 physical variables), with every coefficient checked.
* Exact rational correlations against (3.6) through `m=6`, and against (5.1) through `m=4`. The square-root factors are divided out symbolically before summation; no floating equality is accepted.
* The three-variable base fractions `3/256`, `9/256`, `27/256`, and `Z=319/256`.
* Rational outward logarithm intervals and the finite tensor obstruction at `k=32`; exact partition-function tensor identities and overlapping certified entropy intervals for tensor powers two and three.
* The Boolean surgery sign lemma on all truth tables in dimensions two through four, for the physical origin.
* Separately labeled floating asymptotic examples. These are illustrations, not certificates or evidence for a universal inequality.

The earlier exploratory script `explore.py` enumerates every Boolean function through four variables and samples 10,000 functions per dimension five through ten, for the support-conditioned normalized lower-payment score. Its floating results neither prove the candidate nor detect the under-recovery obstruction, because a lower-payment score and recovery of the required KL are different tests. This failed diagnostic is retained explicitly.

The first verifier run reached the illustrative floating calculation and stopped on logarithm underflow in a tiny nonzero shell. The logarithm evaluation was corrected to use the rational numerator and denominator separately. The complete final byte version was rerun successfully. That failure did not concern an analytic claim or an exact polynomial comparison.

Sources read before using this route included the Math Brain current FEI checkpoint and correction inbox; the erasure synergy/parity-lift and exact-independence reports; the coded scalar-budget obstruction and its later balanced-substitution correction; and the critical logarithmic-tariff report above. The generalized full-resolvent inequality is already refuted in that later source and is not revived here. Publication novelty has not been established. These are analytic proofs with finite self-checks, not an independent audit and not Lean formalization.

No schedules, shared owner controls, peer artifacts, repository visibility or unrelated personal data are changed. This is the current owner's separately authorized interactive FEI continuation; it does not redirect the scheduled movie-image fleet.
