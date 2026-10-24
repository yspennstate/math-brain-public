TASK: B13 ACCOUNT: account02 RUN: 2026-09-21T18:59:20.883780Z — harmonic spectral marking, a Boolean derivative hypercontractive payment, and the inverse-size Palm residual

MODEL: GPT-5.6 Sol (self-report)  
THINKING LEVEL: UNKNOWN; source=not_exposed; requested=maximum actually supported  
THINKING USAGE: reasoning tokens NOT_EXPOSED; provider thinking time NOT_EXPOSED; coverage=unavailable  
RESEARCH EXECUTION: WITHOUT_VERIFIED_BRAIN. No authenticated brain retrieval or receiver-side brain context was consumed.

# Status

**Full uniform-cube Friedgut--Kalai Fourier entropy--influence remains OPEN / NOT PROVED.**

This run follows the live direct seven-FEI owner order and `FEI-FULL-PROOF-PROGRESS-2026-09-21-174421Z`. It does not use the stale provisional B13 benchmark row as its scientific assignment. The scientific route is B13 Booleanity / affine-block influence and correlation profiles.

The new result is a materially different payment mechanism from the preceding three B13 runs. It introduces a uniformly marked coordinate of the spectral sample, proves an exact inverse-size Palm entropy decomposition, and then uses the **actual Boolean first derivative** `g_i in {0,+/-1}` plus Bonami--Beckner hypercontractivity to pay the entire marked-coordinate entropy by influence. The exact first-marker / root-branch term that had remained inside the earlier ordered-prefix information residual is therefore universally paid.

The remaining object is an inverse-size-tilted Palm residual. No universal bound for that residual is claimed here.

No novelty or publication-priority claim is made.

# 1. Fresh state and mandatory comparison with the last three substantive B13 reports

The run consumed the live control packet, the current continuation order and research handoff, the current P03 FEI entry material, the required read-once packet, and current neighboring B12/B14/B16/B18 work before deriving the result below.

The last three completed substantive B13 reports were:

1. `20260921T180326Z-sign-stability-defect/REPORT.md`, blob `b4812f3ae22e7f98596f4b1abcb284dc2d180457`: exact four-bank derivative sign-defect identity and dimension-free signed-Palm/unsigned-support TV transfer. Its unpaid step was terminal-to-prefix Shannon payment after row-shape stability.
2. `20260921T172807Z-affine-block-basis-profile/REPORT.md`: exact affine minimum-basis formulation, basis exchange constraints and a diffuse-collision payment. Its unpaid sector was high collision plus low optimal first shell.
3. `20260921T165419Z-derivative-block-complementarity/REPORT.md`: exact physical/spectral collision complementarity and mixed-axis signed bank. It proved that unsigned/support-only collision bookkeeping cannot close the spectral-row entropy.

The current interactive handoff additionally rules out treating sign-free parity/cylinder profiles as sufficient Boolean realizability data, and rules out global phase/rank/l1 template payment as a full route.

## FULL-PROBLEM CHANGE

**Before:** none of the preceding three B13 mechanisms paid a globally identified Shannon term in the full spectral-sample entropy decomposition. They localized hard sectors, transferred low-defect row shape, or conserved collision banks, while the universal entropy payment remained open.

**After:** for every Boolean `f`, the entropy of the empty/nonempty flag plus the entropy of a uniformly marked spectral coordinate is now paid by

\[
\boxed{
H(1_{S\ne\varnothing})+
\Pr(S\ne\varnothing)H(M\mid S\ne\varnothing)
\le
\left(2+\frac{2+e^{-1}}{\ln2}\right)I(f)
}
\]

with numerical coefficient

\[
5.416127927200970\ldots.
\]

Equivalently, the **root branch mutual-information term** of the earlier ordered-prefix decomposition is paid by `(2+e^{-1})/ln 2 = 3.4161279272...` times influence. Full FEI is reduced to a specific inverse-size harmonic-Palm residual described below; that residual is not yet paid.

## MECHANISM CHANGE

**Before:** local edge-isoperimetric sign slack, affine minimum-basis exchange/collision profiles, and reduced-state collision complementarity.

**After:** a uniform random spectral marker, an exact `1/|S|` Palm tilt, a continuous noise parameter, and Bonami--Beckner applied to the **flat-magnitude Boolean derivative** `g_i in {0,+/-1}`. The crucial inequality is not valid for an arbitrary subset law with the same marginals; it uses physical Boolean realizability through the derivative.

This is therefore not another sign-free profile or a renamed version of the previous hard sector.

# 2. Creative moves used

This run used three `FLEET_RULES` moves different from the preceding local-stability run:

- **#5 ADD A PARAMETER AND DIFFERENTIATE / INTEGRATE IN IT:** `1/(|S|)` is represented exactly as an integral of derivative noise energies.
- **#18 SAY IT IN ANOTHER LANGUAGE:** encode the spectral sample by first choosing one uniformly random marked element and then an inverse-size Palm residual set.
- **#25 COUNT THE SAME THING TWICE:** compute the joint entropy of `(S,M)` first from `S`, then from the marker, obtaining an exact decomposition with no entropy inequality yet.

A fourth diagnostic move, **#20 FIND WHY THE ALGORITHM FAILS**, identifies the remaining obstacle precisely: after the first marker, the conditional inverse-size Palm row is no longer itself the squared spectrum of a Boolean function, so the same flat-derivative argument does not recursively reapply for free.

# 3. Setup and the harmonic marker

Let

\[
f:\{0,1\}^n\to\{-1,+1\},\qquad
\mu(S)=\widehat f(S)^2,
\]

with normalized Walsh transform. Draw `S~mu` and put

\[
K=|S|,\qquad I=\mathbb E K,\qquad
\tau=\Pr(K>0)=1-\widehat f(\varnothing)^2.
\]

For each coordinate define the **harmonic inclusion weight**

\[
\boxed{
r_i:=\sum_{S\ni i}\frac{\mu(S)}{|S|}
=\mathbb E\!\left[\frac{1_{i\in S}}K;K>0\right].
}
\tag{3.1}
\]

Then

\[
\sum_i r_i=\tau.
\tag{3.2}
\]

Condition on `K>0` and choose `M` uniformly from the elements of `S`. Thus

\[
\Pr(M=i\mid K>0)=\frac{r_i}{\tau}.
\tag{3.3}
\]

For `r_i>0`, define the inverse-size Palm row

\[
\boxed{
Q_i(S):=\Pr(S\mid M=i)
=\frac{\mu(S)}{|S|r_i},\qquad S\ni i.
}
\tag{3.4}
\]

Let

\[
\kappa_i:=\mathbb E_{Q_i}(|S|-1).
\tag{3.5}
\]

There is an exact one-charge identity:

\[
\boxed{
r_i(1+\kappa_i)=p_i:=\Pr(i\in S)=\operatorname{Inf}_i(f).}
\tag{3.6}
\]

Consequently

\[
\boxed{
\sum_i r_i\kappa_i=I-\tau.
}
\tag{3.7}
\]

Unlike ordinary coordinatewise entropy subadditivity, (3.7) does **not** charge a spectral set once for every one of its elements: the inverse-size marker makes the total residual mean exactly one copy of `I-tau`.

# 4. Exact entropy decomposition

Adjoin a symbol `bot` and put `M_*=bot` when `S=empty`, while for `S!=empty` let `M_*=M` as above. Count `H(S,M_*)` in two ways.

Conditioning on `S`, the only randomization is the uniform marked coordinate, so

\[
H(S,M_*)=H(S)+\mathbb E[1_{K>0}\log_2 K].
\tag{4.1}
\]

Conditioning first on `M_*`,

\[
H(M_*)=h_2(\tau)+\tau H\!\left((r_i/\tau)_i\right)
\tag{4.2}
\]

and

\[
H(S\mid M_*)=\sum_i r_i H(Q_i).
\tag{4.3}
\]

Therefore:

### Theorem B13-HARMONIC-MARKER-CHAIN

\[
\boxed{
H(f)
=h_2(\tau)
+\tau H\!\left((r_i/\tau)_i\right)
+\sum_i r_iH(Q_i)
-\mathbb E[1_{K>0}\log_2K].
}
\tag{4.4}
\]

Define the remaining harmonic Palm residual

\[
\boxed{
R_{\rm harm}(f)
:=\sum_i r_iH(Q_i)-\mathbb E[1_{K>0}\log_2K].
}
\tag{4.5}
\]

It need not be nonnegative; for a deterministic nonempty spectral set the ordering entropy makes it negative. An equivalent exact form is

\[
\boxed{
R_{\rm harm}(f)
=
\sum_{S\ne\varnothing}\mu(S)
\log_2\frac{
\left(\prod_{i\in S}r_i\right)^{1/|S|}}
{\mu(S)}.
}
\tag{4.6}
\]

Equation (4.6) is useful because it exhibits the remaining problem as a **joint coefficient surprise relative to the geometric mean of the realizable harmonic inclusion weights**, not as a marginal-entropy surrogate.

# 5. The genuinely Boolean inequality: harmonic inclusion is controlled by derivative hypercontractivity

Fix `i` and form the additive Boolean derivative on the remaining cube,

\[
g_i(y)=\frac{f(0,y)-f(1,y)}2\in\{0,\pm1\}.
\tag{5.1}
\]

Its Walsh coefficients are

\[
\widehat g_i(A)=\widehat f(A\cup\{i\}),
\tag{5.2}
\]

and its squared `L^2` norm is exactly

\[
\|g_i\|_2^2=p_i=\operatorname{Inf}_i(f).
\tag{5.3}
\]

Because

\[
\frac1{|A|+1}=\int_0^1t^{|A|}\,dt,
\]

(3.1) becomes the exact noise-semigroup identity

\[
\boxed{
r_i
=\int_0^1\|T_{\sqrt t}g_i\|_2^2\,dt.
}
\tag{5.4}
\]

Bonami--Beckner with target exponent `2`, source exponent `1+t`, and noise parameter `sqrt(t)` gives

\[
\|T_{\sqrt t}g_i\|_2\le\|g_i\|_{1+t}.
\tag{5.5}
\]

Here is where exact Booleanity enters. Since `|g_i|` is the indicator of the sensitive `i`-fibres,

\[
\|g_i\|_{1+t}^2=p_i^{2/(1+t)}.
\tag{5.6}
\]

Thus every Boolean spectral law satisfies the joint realizability constraint

\[
\boxed{
r_i\le U(p_i):=\int_0^1p_i^{2/(1+t)}\,dt.}
\tag{5.7}
\]

For an arbitrary distribution on subsets, even one matching all one-coordinate marginals, there is no physical `{0,+/-1}` derivative and no reason for (5.7) to hold.

Put `L=ln(1/p)`. The substitution `s=(1-t)/(1+t)` gives

\[
U(p)=2p\int_0^1\frac{e^{-Ls}}{(1+s)^2}\,ds.
\tag{5.8}
\]

In particular, for `L>=2`,

\[
U(p)\le\frac{2p}{L}.
\tag{5.9}
\]

# 6. Paying the marked-coordinate entropy

Let `phi(x)=x ln(1/x)`. From (5.7)--(5.9) one obtains the following uniform scalar consequence.

### Lemma B13-HARMONIC-MARKER-PAYMENT

For every Boolean `f` and coordinate `i`,

\[
\boxed{
r_i\ln\frac1{r_i}\le(2+e^{-1})p_i.}
\tag{6.1}
\]

### Proof

If `p<=e^{-2}`, then `L>=2` and `r<=2p/L<e^{-1}`. Since `phi` is increasing on `[0,e^{-1}]`,

\[
\phi(r)
\le\phi(2p/L)
=2p\left(1+\frac{\ln(L/2)}L\right).
\]

For `L>=2`, the maximum of `ln(L/2)/L` occurs at `L=2e` and equals `1/(2e)`. Hence this is at most `(2+e^{-1})p`.

If `e^{-2}<=p<=e^{-1}`, then `r<=p<=e^{-1}` and

\[
\phi(r)\le\phi(p)=pL\le2p.
\]

If `p>=e^{-1}`, simply use `phi(r)<=e^{-1}<=p`. This proves (6.1). `QED`

Changing to base-two logarithms and summing,

\[
\sum_i r_i\log_2\frac1{r_i}
\le
\frac{2+e^{-1}}{\ln2}I(f).
\tag{6.2}
\]

Since

\[
\tau H((r_i/\tau)_i)
=
\sum_i r_i\log_2\frac1{r_i}+\tau\log_2\tau
\le
\sum_i r_i\log_2\frac1{r_i},
\]

we have the universal marker payment

\[
\boxed{
\tau H(M\mid K>0)
\le
C_{\rm mark}I(f),
\qquad
C_{\rm mark}:=\frac{2+e^{-1}}{\ln2}
=3.416127927200970\ldots.
}
\tag{6.3}
\]

## Relation to the earlier random-prefix residual

At the root of the uniformly ordered spectral-prefix process, conditional on `K>0`, the first coordinate is exactly `M`, and given `S` it is uniform on `S`. Therefore the root branch mutual information is

\[
\tau I(M;S\mid K>0)
=\tau H(M\mid K>0)-\mathbb E[1_{K>0}\log_2K].
\tag{6.4}
\]

Hence the previously unpaid root-branch term now has the direct Boolean payment

\[
\boxed{
\tau I(M;S\mid K>0)\le C_{\rm mark}I(f).
}
\tag{6.5}
\]

This is an actual payment of a named component of the old prefix information residual, not a new profile definition.

# 7. Paying the empty/nonempty atom

Let

\[
a=\min\{\Pr(f=1),\Pr(f=-1)\}\le\tfrac12.
\]

Then

\[
\tau=1-(\mathbb Ef)^2=4a(1-a).
\tag{7.1}
\]

The cube edge-isoperimetric inequality in the present influence normalization gives

\[
I(f)\ge2a\log_2\frac1a.
\tag{7.2}
\]

We also have

\[
\boxed{h_2(4a(1-a))\le4a\log_2(1/a).}
\tag{7.3}
\]

For `a<=1/4`, in natural logarithms use `h(x)<=x ln(e/x)`, monotonicity of `x ln(e/x)` on `[0,1]`, and `4a(1-a)<=4a`:

\[
h(\tau)\le4a\ln\frac e{4a}
=4a[\ln(1/a)+1-\ln4]
\le4a\ln(1/a).
\]

For `a in [1/4,1/2]`, `h_2(\tau)<=1` while `4a log_2(1/a)>=2`, so (7.3) is immediate. Combining (7.2)--(7.3),

\[
\boxed{h_2(\tau)\le2I(f).}
\tag{7.4}
\]

# 8. Universal paid decomposition and transfer back to ordinary FEI

Substituting (6.3) and (7.4) into the exact chain (4.4) gives:

### Theorem B13-HARMONIC-PAID-DECOMPOSITION

For every uniform-cube Boolean function,

\[
\boxed{
H(f)
\le
C_{\rm paid}I(f)+R_{\rm harm}(f),
\qquad
C_{\rm paid}=2+\frac{2+e^{-1}}{\ln2}
=5.416127927200970\ldots.
}
\tag{8.1}
\]

This is **not** a proof of FEI because no dimension-independent upper bound on `R_harm` has been established.

There is, however, an exact one-charge sufficient target. If constants `A,B<infinity` could be proved for all Boolean-origin harmonic Palm rows such that

\[
H(Q_i)\le A+B\kappa_i,
\tag{8.2}
\]

then by (3.2) and (3.7),

\[
\sum_i r_iH(Q_i)
\le A\tau+B(I-\tau)
\le\max(A,B)I.
\]

Since the logarithmic term in (4.5) is nonnegative before subtraction,

\[
R_{\rm harm}\le\sum_i r_iH(Q_i),
\]

and full FEI would follow with

\[
C=C_{\rm paid}+\max(A,B).
\tag{8.3}
\]

The point-indicator derivative row shows that a pure slope theorem `H(Q_i)<=B(1+kappa_i)` cannot have `B<2`: for `g=1_{\{0\}}` on an `m`-cube,

\[
r=4^{-m}\frac{2^{m+1}-1}{m+1},
\qquad
\mathbb E_Q(|A|+1)=\frac{(m+1)2^m}{2^{m+1}-1}\sim\frac m2,
\]

while `Q` is asymptotically close in entropy scale to the uniform law on `2^m` subsets, so

\[
\frac{H(Q)}{\mathbb E_Q(|A|+1)}\to2.
\tag{8.4}
\]

Thus constant `2` is a genuine boundary for the most optimistic local completion, not an arbitrary numerical guess.

## Affine/block transfer

Let `g` be a character/linear-change representative attaining the earlier exact affine minimum `I_aff(f)`. Fourier entropy is invariant and

\[
I(g)=I_{\rm aff}(f)\le I(f).
\]

Applying (8.1) to this actual Boolean representative gives

\[
\boxed{
H(f)
\le C_{\rm paid}I_{\rm aff}(f)+R_{\rm harm}(g).
}
\tag{8.5}
\]

Therefore any universal bound

\[
R_{\rm harm}(g)\le C_R I_{\rm aff}(f)
\]

proved specifically in an affine-minimizing gauge transfers immediately to the original problem:

\[
H(f)\le(C_{\rm paid}+C_R)I(f).
\]

This is the requested transfer back to ordinary entropy/influence. The affine minimum-basis identity is used only as a legitimate gauge reduction; it is not counted as the proof step itself.

# 9. Decisive sanity checks and one preserved false start

`check_harmonic_marker.py` is standard-library only. It exhausts all Boolean functions modulo global output sign through dimension four and checks:

- the exact entropy chain (4.4);
- the exact geometric-mean residual form (4.6);
- the exact one-charge mean identity (3.7);
- the coordinatewise marker payment (6.1) after conversion to bits;
- the aggregate atom and marker payments.

The final run passed:

- sign-normalized Boolean functions: **32,906**;
- nonconstant functions: **32,902**;
- active coordinate rows: **130,933**;
- total recorded checks: **328,357**;
- maximum entropy-chain discrepancy: `8.882e-16`;
- maximum residual-form discrepancy: `8.882e-16`;
- maximum one-charge-mean discrepancy: `4.441e-16`;
- maximum coordinate marker-payment excess: `-1.872e-01`.

The finite search is a regression test, not proof of the analytic theorem.

A first diagnostic run failed at the `m=16` point-indicator stress case because it summed 65,536 equal-level probabilities one atom at a time and imposed an unnecessarily tight `2e-12` floating equality to a closed-form mean. That failed stdout/stderr and exit code `1` are preserved in `CHECK_OUTPUT_FAILED.txt`. The theorem was not implicated. The diagnostic was repaired by summing each Hamming level with `binom(m,k)`; the final run exited `0`.

Point-indicator harmonic-row ratios `H(Q)/E_Q(K+1)` were

- `m=4`: `1.497148347282`;
- `m=8`: `1.753384714104`;
- `m=12`: `1.836159133154`;
- `m=16`: `1.876814355945`,

consistent with the proved limit `2` in (8.4).

As a deliberate non-Boolean obstruction check, an abstract product-set law with fixed expected size `lambda=4` has a uniformly located marked coordinate; the marked-coordinate entropy per mean rises from `1.4759` at `n=64` to `2.9452` at `n=4096` and diverges like `log n`. This is **not** an FEI counterexample. It demonstrates that the derivative-flatness/hypercontractive input is doing substantive Boolean work rather than proving an inequality for arbitrary subset laws.

# 10. Coordination and next exact target

- **B12:** continues physical erasure / sequential prediction. B13's `Q_i` is an inverse-size Palm object with the exact one-charge mean (3.7); no claim is made that B12's ordinary Palm row bound transfers automatically.
- **B14:** currently owns centered restriction drift and posterior threshold-crossing/non-affine-face budgets. This report does not duplicate restriction selection.
- **B16/B18:** currently own signed transport / ordered-flag / phase-curvature compilers. This report does not re-open the refuted global phase/rank/l1 payment.
- **B13:** owns the harmonic marker/inverse-size Palm residual and its affine/block stress tests.

**Next exact target:** decide the Boolean-origin harmonic-Palm inequality

\[
H(Q_i)\stackrel{?}{\le}A+B\mathbb E_{Q_i}(|S|-1)
\]

with finite dimension-independent `A,B`, starting with the sharp point-indicator boundary `B>=2` and attempting to refute `B=2` on genuine ternary derivatives before proving anything. If `B=2` fails, preserve the Boolean counterexample and identify the additional signed/block statistic needed. A proof for any finite `A,B` would close full FEI through (8.3); a finite experiment alone would not.

Full FEI remains **OPEN**.
