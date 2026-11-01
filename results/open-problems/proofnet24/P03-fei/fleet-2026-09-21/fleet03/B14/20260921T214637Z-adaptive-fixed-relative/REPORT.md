# B14 FEI interface A — adaptive short-circuiting of the fixed-relative obstruction

**Account/slot:** fleet03/B14  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** **PARTIAL. Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Method change:** yes. Instead of another coordinate/block selector or quadratic-potential sweep, this run tests a genuinely adaptive physical stopping tree against the sharp fixed-relative near-subcube obstruction that defeats the full defining block.

## 1. Exact attempted universal statement

The live interface-A gap is to find a realizable physical restriction strategy whose unpaid spectral-entropy cost is dimension-free relative to a genuine influence/crossing budget. A useful target would be a universal constant `K` such that on every relevant centered primitive core one can choose a stopped physical decision tree `T` with

\[
\Delta_T \mathcal F\le K\,\Delta_T\mathcal J,
\qquad
\mathcal F=H-\sum_i\mathfrak j(p_i),
\]

or an equivalent source-exact corrected payment, while producing nontrivial posterior crossing. This is **OPEN**.

This run attacks the strongest presently known obstruction to the naive version: the fleet02 fixed-relative family for which the full defining block `Z` obeys

\[
\Delta_ZH/D_Z>(\log_2 r-1)/25\to\infty
\]

even after the unique-maximum-pivot majority substitution. The question tested here is whether the same family also destroys a realizable *adaptive* short-circuit strategy.

## 2. Named other-account result consumed and applied

The primary consumed peer artifact is

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B14/20260921T211337Z-posterior-variance-short-circuit/REPORT.md`.

Its Theorem 4.1 gives the realizable short-circuit tree for a pivotality event close to a codimension-`r` subcube: query the defining literals in order and stop at the first mismatch. It proves expected query count `<2` and crossing at least `(p-delta)_+`, but deliberately does **not** extend its entropy-payment claim from the certified `q/(16r)` regime to the refuted fixed-relative `q/16` regime.

I apply that exact adaptive tree to the fleet02 fixed-relative obstruction

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/interactive/20260921T192650Z-joint-fei-subcube-peeling/FIXED_RELATIVE_OBSTRUCTION.md`.

That obstruction has `q=2^{-r}`, `M=r+4`, `delta=2^{-M}=q/16`, pivot event

\[
\eta_x=1_{\{z=0\}\cup\{w=0\}},
\qquad
p_x=q+(1-q)\delta,
\]

and full-block posterior crossing `c_x(Z)=q`, yet its full `Z`-block entropy/drift ratio diverges logarithmically.

## 3. PROVED: exact adaptive crossing and exact stopped folded drift

Let `T_r` query `z_1,z_2,...,z_r` in that order, stopping immediately at the first `z_t=1`; on the all-zero branch it stops after query `r`. This is an ordinary physical decision tree.

### 3.1 Crossing is unchanged

The all-match leaf has probability `q` and there the pivot is certainly pivotal, so its posterior pivotality equals `1`. Every mismatch leaf has pivot posterior `delta<1/2`. Therefore

\[
\boxed{c_x(T_r)=q,\qquad
\gamma_x(T_r)=\frac q{q+(1-q)\delta}=\frac{16}{17-q}>\frac{16}{17}.}
\tag{3.1}
\]

Thus short-circuiting loses none of the pivot crossing available from the full block.

### 3.2 Expected physical influence spent by the tree

Immediately before query `t`, conditional on reaching that node, there are

\[
s=r-t+1
\]

defining controls still unmatched. Put `q_s=2^{-s}=2^{t-1}q`. Direct edge counting in the same Boolean family gives the current queried-control influence

\[
p_t=q_s+\delta-3q_s\delta.
\tag{3.2}
\]

The node is reached with probability `2^{-(t-1)}=q/q_s`. Hence the expected raw influence actually queried is

\[
\begin{aligned}
Q_T
&=\sum_{t=1}^r2^{-(t-1)}p_t\\
&=rq(1-3\delta)+2\delta(1-q).
\end{aligned}
\tag{3.3}
\]

All non-pivot survivor influences remain below `1/2`; their raw influences are martingales under restrictions of other coordinates. The pivot's root folded influence is `q+(1-q)delta`; at mismatch leaves it is `delta` and at the all-match leaf its influence is `1`, hence folds to zero. Its additional root-to-leaf folded loss is exactly `q`. Consequently

\[
\boxed{
D_T:=\Delta_T\mathcal J
=Q_T+q
=(r+1)q-3rq\delta+2\delta(1-q).
}
\tag{3.4}
\]

At `delta=q/16`,

\[
D_T=q\left(r+\frac98\right)-q^2\left(\frac{3r}{16}+\frac18\right).
\tag{3.5}
\]

This is an exact identity, not a numerical fit.

## 4. PROVED: the majority substitution preserves this adaptive `Delta H` and `Delta J`

The full-block obstruction replaces every selector bit `w_k` by a balanced recursive ternary-majority gadget on a fresh disjoint block in order to make `x` the unique maximum-influence coordinate. The fixed-block report proves entropy-decrement preservation for a retained physical block. The same argument works for this stopped tree.

Let `ell` range over the stopped `z`-leaves. For balanced disjoint substitution,

\[
H(F_\ell)
=H(f_\ell)+\sum_k\operatorname{Inf}_{w_k}(f_\ell)H(g_k).
\tag{4.1}
\]

The stopped leaves form a partition generated only by `z` queries, so bounded optional averaging of raw influence gives

\[
\mathbb E_\ell\operatorname{Inf}_{w_k}(f_\ell)
=\operatorname{Inf}_{w_k}(f).
\tag{4.2}
\]

Therefore the added gadget terms cancel between root and expected leaf, and

\[
\boxed{\Delta_T H(F)=\Delta_T H(f).}
\tag{4.3}
\]

For a leaf coordinate of a balanced majority gadget, its substituted influence is the outer `w_k` influence times the gadget-leaf influence. The latter is `2^{-d}` at recursion depth `d=r+5`, so every substituted selector-leaf influence is `<1/2` on every stopped leaf. Hence folding does not alter those gadget contributions, and the same martingale cancellation gives

\[
\boxed{\Delta_T\mathcal J(F)=\Delta_T\mathcal J(f)=D_T.}
\tag{4.4}
\]

**Important limitation.** The nonlinear scalar potential `sum_j mathfrak j(p_j)` does *not* enjoy the same linear cancellation under substitution. Thus (4.3)-(4.4) transfer the uncorrected entropy and folded drift exactly, but the raw-outer calculation of `Delta_T mathcal F` below is not claimed to transfer unchanged to the majority-substituted function.

## 5. PROVED algebraic compression; COMPUTED high-precision test

A truth table of the substituted family has enormous dimension, but no truth table is needed. I derived the exact Fourier coefficient categories for every stopped state and implemented them in `verify_adaptive_fixed_relative.py`.

After a matched prefix with `s` controls remaining and fixed selector dimension `M`, write `q_s=2^{-s}`, `d=2^{-M}`. The influence types are exactly

\[
\begin{aligned}
p_x&=q_s+(1-q_s)d,\\
p_z&=q_s+d-3q_sd,\\
p_{w,\mathrm{active}}&=d(s-q_s),\\
p_{w,\mathrm{other}}&=d(s+1-q_s).
\end{aligned}
\tag{5.1}
\]

After the first mismatch with `s` untouched controls remaining, the types are

\[
p_x=p_z=d,\qquad
p_{w,\mathrm{active}}=d(s+2),\qquad
p_{w,\mathrm{special}}=d(s+1),\qquad
p_{w,\mathrm{other}}=d(s+3).
\tag{5.2}
\]

The script groups Fourier coefficients by the Hamming weight of the selector frequency, so the entropy calculation is exact up to the displayed high-precision decimal logarithms rather than an exponentially large enumeration. The category masses satisfy Parseval to the working precision, and the independently computed root-to-leaf `Delta J` agrees exactly with (3.4) at Decimal precision.

For the **raw outer Boolean family** the observed ratios are:

| `r` | `Delta_T H / Delta_T J` | `Delta_T F / Delta_T J` |
|---:|---:|---:|
| 2 | 2.951752517390441 | 0.383507481694434 |
| 4 | 3.619943100049255 | 0.802919507947515 |
| 8 | 3.886447653349937 | 1.005204405478494 |
| 16 | 3.953894748763326 | 1.068520936431947 |
| 32 | 3.979833909857744 | 1.094443828328999 |
| 64 | 3.991611876284819 | 1.106221794506892 |
| 100 | 3.995379302561422 | 1.109989220783495 |
| 150 | 3.997385114116975 | 1.111995032339048 |
| 200 | 3.998290201377375 | 1.112900119599448 |

For small `r=2,...,6`, the compressed entropy formulas were also compared against direct Walsh truth-table transforms and agreed to floating roundoff. The table above is a **self-check / computation**, not a proof for all `r`.

The numerical pattern strongly suggests the structured-family asymptotics

\[
\frac{\Delta_T H}{\Delta_TJ}\to4,
\qquad
\frac{\Delta_T\mathcal F}{\Delta_TJ}
\to4-\frac{2}{\ln2}
=1.114609918222\ldots,
\tag{5.3}
\]

but (5.3) is recorded as **CONJECTURAL for this report** until an analytic remainder bound is written down.

## 6. Decisive attempted refutation and what it means

The known fixed-relative family was designed to refute the full defining-block implication. It has

\[
\Delta_ZH/D_Z>(\log_2r-1)/25\to\infty.
\]

Applying the realizable short-circuit tree is therefore a direct attempt to refute the adaptive replacement. The attempt did **not** reproduce the logarithmic divergence: exact drift formula (3.4) and compressed entropy evaluation instead give a ratio below `4` at every tested value through `r=200`, approaching `4` from below in the observed range.

This is **not** a proof that every `r` obeys the bound, and it is **not** a universal FEI step. It does show that the currently sharp full-block obstruction does not automatically transfer to the natural stopped strategy. The obstruction's expensive selector entropy is largely avoided when the physical tree stops on the overwhelmingly common first mismatch while retaining the same pivot crossing.

The strongest honest status is therefore:

- **PROVED:** exact crossing (3.1), queried-influence spend (3.3), folded drift (3.4), and adaptive balanced-substitution invariance (4.3)-(4.4) for this family;
- **PROVED:** compressed Fourier/influence category formulas used by the diagnostic;
- **COMPUTED:** the displayed ratios through the stated finite values;
- **CONJECTURAL:** a uniform `<4` uncorrected ratio and limits (5.3) for this structured family;
- **OPEN:** any universal adaptive/corrected selector theorem for arbitrary Boolean functions;
- **OPEN:** full uniform-cube FEI.

## 7. Dead route and next attack

**Dead route:** it is no longer productive to cite the fixed-relative full-`Z` obstruction as if it also killed short-circuit/minimal-crossing trees. It does not do so at the level presently tested, and the exact stopped drift behaves on the correct `r q` scale.

**Next attack:** first turn the structured-family evidence into a theorem by proving directly from the coefficient categories that

\[
\Delta_{T_r}H\le 4D_{T_r}
\quad\text{or at least}\quad
\Delta_{T_r}H\le5D_{T_r}
\tag{7.1}
\]

for every `r`. Then replace the singleton selector pollution by an arbitrary error set `E triangle Q` and randomize/adapt the literal order. The universal target is to charge entropy created on error-discovery leaves to a **nonreused** joint-row credit (the fleet01 prefix/TC bank is a natural recipient) while charging the all-match branch to the real posterior crossing. The remaining implication is precisely a dimension-free corrected-payment theorem for that adaptive error-discovery tree; no every-coordinate statement is needed.

## 8. Joint handoff fields

- `consumed_peer_artifact`: `fleet04/B14/20260921T211337Z-posterior-variance-short-circuit/REPORT.md` (primary), applied to the fleet02 fixed-relative obstruction.
- `applied_to_claim`: whether the realizable short-circuit/minimal-crossing strategy inherits the logarithmic entropy/drift failure of the full defining block.
- `remaining_implication`: prove a dimension-free corrected entropy payment for an adaptive physical tree on arbitrary high-ratio cores, including arbitrary near-subcube error rather than this explicit singleton-pollution family.
- `next_recipient`: fleet04/B14 for the short-circuit theorem extension, with fleet01/B18 as the integration recipient for any nonreused error-leaf information credit.

No novelty or publication-priority claim is made. This report is a proof-search checkpoint, not independent verification.
