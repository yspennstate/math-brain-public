TASK: B13 ACCOUNT: fleet02 RUN: 2026-09-21T19:29:06.213374Z — harmonic-cardinality payment, exact layer-incidence residual, and a majority obstruction to the local Palm closure

MODEL: GPT-5.6 Sol (self-report)  
REQUESTED EFFORT: maximum actually supported  
CONFIGURED / KNOWN REASONING LEVEL: UNKNOWN / NOT_EXPOSED  
PROVIDER REASONING USAGE: null / NOT_EXPOSED  
EXECUTION: WITHOUT_VERIFIED_BRAIN

# Status

**Full uniform-cube Friedgut--Kalai Fourier entropy--influence remains OPEN / NOT PROVED.**

This run follows `FEI-FULL-PROOF-PROGRESS-2026-09-21-174421Z` and the live seven-FEI owner assignment. It does not use the stale provisional benchmark role for B13. No novelty or publication-priority claim is made.

The run first attacks the exact local target left by B13's preceding harmonic-marker report,

\[
H(Q_i)\stackrel{?}{\le} A+B\,\kappa_i
\tag{0.1}
\]

with universal finite `A,B`. A genuine Boolean derivative family (odd majority) refutes **every** such pair of constants: `H(Q_i)` grows at least logarithmically while `kappa_i<=3` uniformly. Thus the local inverse-size Palm closure is false, not merely unproved.

The run then executes a different mechanism rather than tuning (0.1). The harmonic row is split by its residual cardinality. The entire residual-cardinality entropy is paid **exactly at one influence charge** using the maximum-entropy law on the nonnegative integers and the harmonic one-charge identity. What remains is a canonical **layer-incidence residual**

\[
\mathcal R_{\rm inc}(f)
=\tau\,[H(S\mid K,K>0)-H(M\mid K,K>0)],
\tag{0.2}
\]

where `S` is the spectral sample, `K=|S|`, and `M` is a uniformly marked element of a nonempty `S`. Combining this new payment with the previous harmonic-marker theorem gives the exact full-problem reduction

\[
\boxed{
H(f)\le
\left(3+\frac{2+e^{-1}}{\ln2}\right)I(f)
+\mathcal R_{\rm inc}(f)
}
\tag{0.3}
\]

with paid coefficient

\[
3+\frac{2+e^{-1}}{\ln2}
=6.416127927200970\ldots.
\tag{0.4}
\]

This is **not** a proof of FEI. The remaining universal implication is a dimension-independent Boolean/signed payment of `R_inc`. The continuation packet's template-collapse and parity-profile counterexamples are preserved: (0.2) is a localization of the debt, not a claim that sign-free layer incidence is sufficient Boolean data.

# 1. Required comparison with the last THREE completed substantive B13 reports

The last three completed B13 reports on the current scientific lineage are:

1. `20260921T185920Z-harmonic-marker-payment/REPORT.md`. It introduced the uniform spectral marker, the inverse-size Palm rows `Q_i`, proved the Boolean derivative hypercontractive bound on harmonic weights, and paid the empty/nonempty flag plus root-marker entropy by `5.4161279272... I`. Its explicit next target was (0.1).
2. `20260921T180326Z-sign-stability-defect/REPORT.md`. It proved the exact derivative sign-defect decomposition and a dimension-free signed-Palm to support-Palm TV transfer, but left terminal-to-prefix information unpaid.
3. `20260921T172807Z-affine-block-basis-profile/REPORT.md`. It gave the exact affine minimum-basis reformulation, basis-exchange constraints and a diffuse collision payment, leaving the high-collision/low-first-shell sector unpaid.

The current continuation handoff additionally records two failures that remain binding here: the global phase/rank/l1 template collapses to an uncontrolled Fourier `l1` quantity, and sign-free parity/cylinder profiles admit non-Boolean unbounded-ratio square laws. Nothing below reopens either failed sufficiency claim.

## FULL-PROBLEM CHANGE

**Before:** the best B13 harmonic reduction was

\[
H(f)\le
\left(2+\frac{2+e^{-1}}{\ln2}\right)I(f)
+R_{\rm harm}(f),
\]

with

\[
R_{\rm harm}
=\sum_i r_iH(Q_i)-\mathbb E[1_{K>0}\log_2K].
\]

The proposed one-charge completion `H(Q_i)<=A+B kappa_i` was open.

**After:** that proposed local completion is rigorously false even for a derivative row that is itself Boolean (odd majority). Nevertheless the entire **cardinality part** of every `Q_i` is universally paid by exactly `I(f)`, leaving only the within-layer incidence term (0.2). Hence the paid coefficient moves from `5.4161279272...` to `6.4161279272...` while the named residual becomes strictly more structured: it contains no row-cardinality entropy.

No finite bound on the remaining `R_inc/I` is proved.

## MECHANISM CHANGE

**Before:** try to close each inverse-size Palm row independently by its one-charge mean `kappa_i`.

**After:** first **refute** row-local mean control with odd majority, then abandon row-local closure and reassemble all rows into the global joint law `(S,M,K)`. The new payment is an exact conditional-cardinality code, while the surviving debt is a layerwise hypergraph incidence entropy. This is different from the previous sign-stability, affine-collision, and scalar harmonic-row mechanisms.

# 2. Setup and the previous harmonic marker

Let

\[
f:\{-1,+1\}^n\to\{-1,+1\},\qquad
\mu(S)=\widehat f(S)^2,
\]

and draw `S~mu`. Put

\[
K=|S|,\qquad I=\mathbb EK,\qquad
\tau=\Pr(K>0).
\]

Conditioned on `K>0`, choose a marker `M` uniformly from the elements of `S`. Define the subprobability harmonic marker masses

\[
r_i:=\Pr(K>0,M=i)
=\sum_{S\ni i}\frac{\mu(S)}{|S|}.
\tag{2.1}
\]

Then

\[
\sum_i r_i=\tau.
\tag{2.2}
\]

For `r_i>0`, let `Q_i` be the law of `S` conditioned on `M=i`:

\[
Q_i(S)=\frac{\mu(S)}{|S|r_i},\qquad S\ni i.
\tag{2.3}
\]

Let

\[
L_i:=K-1\quad\text{under }Q_i,
\qquad
\kappa_i:=\mathbb E_{Q_i}L_i.
\tag{2.4}
\]

Writing

\[
p_i=\Pr(i\in S)=\operatorname{Inf}_i(f),
\]

the harmonic one-charge identity is exact:

\[
\boxed{r_i(1+\kappa_i)=p_i.}
\tag{2.5}
\]

Indeed

\[
r_i(1+\kappa_i)
=r_i\,\mathbb E_{Q_i}K
=\sum_{S\ni i}\mu(S)=p_i.
\]

Consequently

\[
\boxed{\sum_i r_i\kappa_i=I-\tau.}
\tag{2.6}
\]

The previous report also proved, using the actual `{0,+/-1}` Boolean derivative and Bonami--Beckner hypercontractivity,

\[
\tau H(M\mid K>0)
\le
C_{\rm mark}I,
\qquad
C_{\rm mark}:=\frac{2+e^{-1}}{\ln2}
=3.416127927200970\ldots,
\tag{2.7}
\]

and the empty/nonempty payment

\[
h_2(\tau)\le2I.
\tag{2.8}
\]

Those are inputs here, not re-proved.

# 3. PROVED: the local harmonic-Palm mean closure is false

The preceding report proposed testing whether finite constants `A,B` might satisfy

\[
H(Q_i)\le A+B\kappa_i
\tag{3.1}
\]

for every Boolean-origin harmonic row. This section refutes (3.1) with a genuine Boolean family.

Let `n=2m+1` be odd and let

\[
g_n(y)=\operatorname{Maj}_n(y)\in\{-1,+1\}.
\]

Realize `g_n` as an actual first Boolean derivative by adding one variable `x_0` and setting

\[
F_n(x_0,y)=x_0g_n(y)
\]

in the `{-1,+1}` convention. Then the derivative of `F_n` in coordinate `0` is exactly `g_n`, and

\[
\widehat F_n(\{0\}\cup A)=\widehat g_n(A).
\]

Thus the harmonic row at marker `0` is precisely

\[
Q(A)=\frac{\widehat g_n(A)^2}{(|A|+1)r},
\qquad
r=\sum_A\frac{\widehat g_n(A)^2}{|A|+1},
\tag{3.2}
\]

with

\[
\kappa=\mathbb E_Q|A|=\frac1r-1,
\tag{3.3}
\]

because `g_n` is Boolean and hence has spectral mass one.

## 3.1 A dimension-free lower bound on majority first-level mass

For every coordinate `j`, conditioning on the other `2m` bits gives

\[
\widehat g_n(\{j\})
=a_m:=\frac{\binom{2m}{m}}{4^m}.
\tag{3.4}
\]

A short induction gives

\[
\boxed{a_m\ge\frac1{2\sqrt m}.}
\tag{3.5}
\]

Proof: `a_1=1/2`, and

\[
a_m=\left(1-\frac1{2m}\right)a_{m-1}.
\]

If `a_{m-1}>=1/(2 sqrt(m-1))`, then the square of the ratio between the resulting lower bound and `1/(2 sqrt m)` is

\[
\left(\frac{2m-1}{2m}\right)^2\frac m{m-1}
=1+\frac1{4m(m-1)}\ge1.
\]

Hence (3.5).

Let `W_1` be the level-one spectral mass of majority. Then

\[
W_1=n a_m^2
\ge\frac{2m+1}{4m}
\ge\frac12.
\tag{3.6}
\]

## 3.2 `kappa` remains bounded while `H(Q)` diverges

The level-one part of (3.2) alone gives

\[
r\ge\frac{W_1}{2}\ge\frac14.
\tag{3.7}
\]

Since also `r<=1`, (3.3) yields

\[
\boxed{\kappa\le3.}
\tag{3.8}
\]

Under `Q`, the `n` singleton sets all have equal probability

\[
q_1=\frac{a_m^2}{2r}.
\]

Their total `Q`-mass is

\[
\alpha=nq_1=\frac{W_1}{2r}.
\]

Using `r<=1` and (3.6),

\[
\alpha\ge\frac14.
\tag{3.9}
\]

The singleton atoms alone therefore contribute

\[
H(Q)
\ge n q_1\log_2\frac1{q_1}
=\alpha\log_2\frac n\alpha
\ge\frac14\log_2 n.
\tag{3.10}
\]

Combining (3.8)--(3.10), for any fixed finite `A,B`,

\[
A+B\kappa\le A+3B
\]

while `H(Q)->infinity`. Hence:

### Theorem B13-MAJORITY-HARMONIC-NOGO

There are **no** universal finite constants `A,B` such that

\[
H(Q_i)\le A+B\kappa_i
\]

for all harmonic Palm rows generated by Boolean first derivatives. The failure already occurs when the derivative itself is the genuine Boolean function odd majority.

This is not an FEI counterexample: for `F_n=x_0 Maj_n`, the original influence contains the large higher-level Boolean cost that pays the logarithmic row-label entropy. The theorem says only that the one-charge row mean `kappa_i` does not retain that cross-level resource.

# 4. New exact decomposition: remove all row-cardinality entropy

The failed local target suggests separating **which size** the residual set has from **which coordinates** occur at that size.

For every active marker `i`, apply the entropy chain rule to `Q_i`:

\[
H(Q_i)
=H(L_i)+H(S\mid M=i,L_i).
\tag{4.1}
\]

Insert (4.1) into the exact harmonic-marker chain from the preceding report:

\[
H(f)
=h_2(\tau)
+\tau H(M\mid K>0)
+\sum_i r_iH(Q_i)
-\mathbb E[1_{K>0}\log_2K].
\tag{4.2}
\]

This gives

\[
H(f)
=h_2(\tau)
+\tau H(M\mid K>0)
+\sum_i r_iH(L_i)
+R_{\rm layer},
\tag{4.3}
\]

where

\[
R_{\rm layer}
:=\sum_i r_i H(S\mid M=i,K)
-\mathbb E[1_{K>0}\log_2K].
\tag{4.4}
\]

The next section identifies (4.4) intrinsically, without the Palm rows.

# 5. PROVED: exact layer-incidence identity

Work conditional on `K>0`. Since `M` is chosen uniformly from `S`,

\[
H(M\mid S,K)=\log_2K.
\tag{5.1}
\]

At fixed `K`, count the joint entropy of `(S,M)` in the two orders:

\[
H(S,M\mid K)
=H(S\mid K)+H(M\mid S,K)
\]

and

\[
H(S,M\mid K)
=H(M\mid K)+H(S\mid M,K).
\]

Subtract and average over positive `K`. Multiplying by `tau` gives

\[
\sum_i r_i H(S\mid M=i,K)
-\mathbb E[1_{K>0}\log_2K]
\]

\[
=\tau\,[H(S\mid K,K>0)-H(M\mid K,K>0)].
\tag{5.2}
\]

Define

\[
\boxed{
\mathcal R_{\rm inc}(f)
:=\tau\,[H(S\mid K,K>0)-H(M\mid K,K>0)].
}
\tag{5.3}
\]

Then the exact decomposition is

\[
\boxed{
H(f)
=h_2(\tau)
+\tau H(M\mid K>0)
+\sum_i r_iH(L_i)
+\mathcal R_{\rm inc}(f).
}
\tag{5.4}
\]

`R_inc` is a **within-layer incidence residual**. Conditional on one spectral level `K=k`, `S` is a random `k`-uniform hyperedge and `M` is a uniformly sampled vertex of that edge. The debt is precisely hyperedge-label entropy minus the entropy of one uniformly sampled incident vertex. It can have either sign: for a deterministic nonempty set, the residual is `-log_2 k`; for diffuse families it can be positive.

This is not a sign-free closure theorem. The dyadic square-profile obstruction in the continuation packet shows that an eventual universal payment cannot be justified from arbitrary nonnegative layer/incidence data alone; the fact that `mu=fhat^2` comes from a jointly signed Boolean Fourier vector must re-enter.

# 6. PROVED: the entire cardinality term costs at most one influence

Fix an active row and write `kappa=E L` for its nonnegative-integer residual size. Among all laws on `{0,1,2,...}` with mean `kappa`, entropy is maximized by the geometric distribution

\[
G_\kappa(\ell)
=\frac1{1+\kappa}
\left(\frac\kappa{1+\kappa}\right)^\ell.
\]

Indeed `D(P_L||G_kappa)>=0` gives

\[
H(L)
\le
(1+\kappa)\log_2(1+\kappa)
-\kappa\log_2\kappa
=:g(\kappa).
\tag{6.1}
\]

The key scalar observation is exact:

\[
\frac{g(\kappa)}{1+\kappa}
=h_2\!\left(\frac1{1+\kappa}\right)
\le1.
\tag{6.2}
\]

Therefore

\[
H(L_i)\le1+\kappa_i.
\tag{6.3}
\]

Multiply by `r_i` and use the harmonic one-charge identity (2.5):

\[
r_i H(L_i)
\le r_i(1+\kappa_i)
=p_i.
\]

Summing all markers gives the new universal payment

\[
\boxed{
\sum_i r_iH(L_i)\le I(f).
}
\tag{6.4}
\]

No dimension, source-family parameter or hidden repeated influence appears. The constant `1` in this argument is the trivial best possible scalar constant for (6.2), attained at `kappa=1`; whether Boolean harmonic rows can asymptotically saturate the aggregate inequality is not needed here.

# 7. Universal paid decomposition and transfer to ordinary FEI

Combine (5.4), (2.7), (2.8), and (6.4):

### Theorem B13-LAYER-INCIDENCE-REDUCTION

For every Boolean function on the uniform cube,

\[
\boxed{
H(f)
\le
C_{\rm layer}I(f)+\mathcal R_{\rm inc}(f),
}
\tag{7.1}
\]

where

\[
\boxed{
C_{\rm layer}
:=3+\frac{2+e^{-1}}{\ln2}
=6.416127927200970\ldots.
}
\tag{7.2}
\]

Consequently, any finite universal constant `C_inc` satisfying

\[
\mathcal R_{\rm inc}(f)\le C_{\rm inc}I(f)
\tag{7.3}
\]

for every Boolean `f` would prove the original, unrestricted FEI inequality with

\[
H(f)\le(C_{\rm layer}+C_{\rm inc})I(f).
\tag{7.4}
\]

No affine orbit change is required for this transfer: (7.1) already holds for the original function and original influence. If one elects to work in an affine-minimizing Boolean representative from the earlier B13 theorem, entropy invariance and `I_aff<=I` make the same kind of final transfer legitimate, but no affine-minimum identity is counted as payment here.

The owner-corrected current lower-bound scale `C_FEI>6.521845710923046575` is consistent with (7.1): it merely certifies that some hard Boolean instances must carry positive layer-incidence debt after the first three terms are evaluated. It does not identify or bound that debt.

# 8. What the majority obstruction says about the new residual

For `F_n=x_0 Maj_n`, the failed local row closure is caused by many equally plausible singleton residual labels in the marker-0 row while the harmonic mean residual size stays bounded. The resource that pays this in the full Boolean function lives in higher spectral levels of majority; it is erased when a row is summarized by `kappa_i`.

The new `R_inc` deliberately keeps **layer labels globally coupled** rather than forcing every marker row to pay itself. Thus the majority family does not refute (7.3); instead it is a mandatory stress test for any future signed incidence inequality.

In particular, a future proof cannot rely on either of the following already-failed simplifications:

1. `H(Q_i)` controlled by residual mean alone — refuted here by majority.
2. arbitrary sign-free incidence/parity profiles — refuted by the continuation packet's non-Boolean dyadic square family.

A viable B13 next step must use signed Boolean convolution/autocorrelation or a genuine affine/restriction operation to show that a large positive `R_inc` forces a globally nonreused influence payment elsewhere.

# 9. Coordination with neighboring current mechanisms

The current neighboring reports were checked for claim overlap.

- **B12** owns the physical erasure-information budget of derivative Palm rows. The present result does not claim that its physical DTC budget pays `R_inc`; majority shows why a row-local depth mean is insufficient.
- **B14** now owns adaptive physical/affine restriction budgets, including exact centered pair-parity influence drops. `R_inc` is a spectral-layer incidence quantity, not a restriction selector; the natural future interface is to ask whether a parity restriction lowers `R_inc` by an amount chargeable to B14's telescoping centered budget.
- **B15** has moved to self-XOR/Hellinger negative-credit slice payments. This report does not replace the negative credits by unsigned incidence.
- **B16** owns the genuine post-cancellation parent-mask current and projective incidence bank. This report does not touch the signed compiler coefficients.
- **B17** owns the canonical self-XOR difference/Hellinger representation and its joint-correlation obstruction. Majority is already a stress family there as well; the present no-go concerns a different local harmonic-Palm mean closure.
- **B18** owns affine-subspace plaquette/mask payments after signed compilation. The present hyperedge incidence residual is upstream of any such compiler and is not claimed to satisfy the B18 mask hypotheses.

Thus the nonoverlapping B13 target after this run is: **derive a signed Boolean or affine-restriction decrement for `R_inc` itself**, rather than another scalar profile of its marginals.

# 10. Verification

`check_layer_incidence.py` is standard-library only.

It exhaustively enumerates all Boolean functions modulo global output sign through `n=4` and checks:

- the harmonic one-charge identities;
- the exact row-cardinality / within-layer split;
- the equality between the row form of `R_inc` and the direct conditional-on-`K` form;
- the exact full entropy decomposition (5.4), numerically to floating tolerance;
- the universal cardinality payment (6.4).

It processed **32,906** sign-normalized Boolean functions and recorded **393,474** decomposition/cardinality checks.

Separately, exact `Fraction` arithmetic verifies for `m=1,...,500` the two central-binomial inequalities used in the majority proof, for **1,000 exact rational checks**. Small odd majorities through `n=15` are transformed directly as a diagnostic; their actual harmonic-row entropy grows while `kappa` remains near `1.6` (for `n=15`, `H(Q)=5.551079689989...`, `kappa=1.611276524157...`). These finite values are checks only; the theorem is the analytic lower-bound argument in Section 3.

Final checker status: **PASS**.

# 11. Next exact target

Full FEI remains **OPEN**.

The next B13 target is no longer the false local inequality (3.1). It is the global signed layer-incidence implication

\[
\mathcal R_{\rm inc}(f)\le C I(f)
\]

or a telescoping affine/restriction decomposition that pays its positive part. A useful first nontrivial subproblem is the `K=2` layer, where `R_inc` becomes weighted entropy of a random Fourier edge minus entropy of a uniformly sampled endpoint. Any proposed payment must survive both opposite stress regimes:

- `x_0 Maj_n`, where a broad low layer is paid only by higher-level Boolean structure;
- one-point defects, where the support/incidence rank is huge but the spectral mass and influence are exponentially small.

The signed Boolean convolution identity `f^2=1` or B14's exact affine pair restriction budget is expected to be necessary; a sign-free hypergraph entropy inequality by itself is not enough.
