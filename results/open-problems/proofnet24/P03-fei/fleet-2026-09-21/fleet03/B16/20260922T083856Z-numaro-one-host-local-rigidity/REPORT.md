# B16 — exact one-host local rigidity around the 18-input Numaro seed

**Classification:** `AUXILIARY_ONLY / EXACT_ADVERSARIAL_FAMILY_EXCLUDED`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Version/change summary

The live owner message at control revision `2026-09-22.2` supersedes the older Campaign-C half-band assignment and directs every FEI worker to the all-gate formulation.  I therefore do **not** revive the retired positive-current/NET shortcut.  The source-exact target is the gate defect

\[
D_\Gamma(G;p)=\sum_i\frac{\operatorname{It}_i(G;p)}{V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)-\Gamma(p_{\rm out})-\widetilde H_G(p),
\]

with normalized additional margin

\[
c_G(p)=-\frac{D_{\Gamma_{\rm RO}}(G;p)}{M(G;p)},\qquad
M(G;p)=\frac14\sum_i\operatorname{It}_i(G;p)-p_{\rm out}(1-p_{\rm out}).
\]

The universal implication is still: find one finite scalar lift (or another symmetric potential) that pays **every composition-prime Boolean gate at every product bias**.  The currently used stable quadratic lift is approximately

\[
a_*=0.268204856,\qquad
\Gamma_*(p)=\Gamma_{\rm RO}(p)+a_*p(1-p),
\]

with center cap about `6.521851214`.

This run executes a materially different adversarial method: an exact sparse deformation of the source 18-input Numaro gate itself.  It proves that the near-binding source gate is sharply isolated against **every one-host-pair replacement** in its exact core/host representation.  This does not settle the universal quantifier, hence the conservative `AUXILIARY_ONLY` label.

## 1. Named peer results consumed and applied

### 1.1 fleet02/B17 — exact composition cocycle

Consumed:

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B17/20260922T004442Z-gate-composition-cocycle/REPORT.md`, blob
`8b59fbde81f8b194347452d0102f7f625ef85b89`.

It proves exactly that gate slack and the Poincare denominator compose with the same nonnegative weights.  Hence normalized margin is a weighted average of factor margins.  In particular **disjoint tensor products, recursive compositions and biased disjoint compositions cannot amplify `c_G` beyond a primitive factor**.  I use that result here to retire the tensor/asymptotic branch of the assigned adversarial search: any new falsifier must come from genuinely composition-prime/shared-coordinate interference, not disjoint tensoring of already tested seeds.

### 1.2 fleet02/B16 — source-exact Numaro reconstruction

Consumed:

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B16/20260922T011313Z-arity10-composition-prime/check_b16_arity10_composition_prime.py`, blob
`b6f34ebad4481301ddbc3abeb70e5818242b9fe1`.

That source reconstructs the inherited balanced 18-input Numaro truth table with SHA-256

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`.

Its representation exposes a 9-bit core and nine disjoint two-point host sets.  I use **that exact representation**, rather than an approximate or independently guessed version.

### 1.3 fleet04/B16 — current stable-lift comparison

Consumed:

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B16/20260922T071429Z-n18-first-cell-baseline-resolution/HANDOFF.md`, blob
`5ea5dc363765c811acbdfe2ab518458b5c69200a`.

It records the current comparison scale `a_*=0.268204856` and shows that a coherent off-center test at `u=1/5000` raises the source margin but still remains below that lift.  The theorem below applies directly to the same stable candidate at the uniform center.

## 2. Exact source family

Let `c:{0,1}^9->{-1,+1}` be the source core.  Its sum is

\[
\sum_x c(x)=18,
\]

so it has 265 positive cells and 247 negative cells.  The source host pairs are

\[
\begin{aligned}
&(78,79),(113,121),(228,484),(170,186),(149,151),\\
&(338,466),(284,316),(291,295),(393,457).
\end{aligned}
\]

All eighteen host vertices are positive core cells, the nine pairs are disjoint, and every source pair is a Hamming edge.

For any nine disjoint pairs `E=(e_1,...,e_9)` of positive core cells define the 18-input Boolean function

\[
F_E(x,y)=
\begin{cases}
 c(x),&x\notin\bigcup_j e_j,\\
 (-1)^{y_j},&x\in e_j.
\end{cases}
\tag{2.1}
\]

The source gate is exactly `F_{E_0}` for the nine pairs above.  Because replacing the eighteen positive core values by nine balanced host fibres removes total core sum 18, **every** such `F_E` is balanced.

The sparse adversarial family in this run keeps eight source pairs fixed and replaces the remaining pair by **any other pair of positive core cells disjoint from the retained sixteen vertices**.  The replacement need not be a Hamming edge.  For each of the nine host positions there are

\[
\binom{249}{2}-1=30,875
\]

nonidentity replacements, hence exactly

\[
9\cdot30,875=277,875
\tag{2.2}
\]

source-valid balanced Boolean gates in the tested family.

## 3. Exact Fourier decomposition

Let

\[
g_E(x)=c(x)\,1_{\{x\notin\cup_j e_j\}}.
\]

Averaging over the nine host bits gives the orthogonal decomposition

\[
\widehat F_E(S,\varnothing)=\widehat g_E(S),
\qquad
\widehat F_E(S,\{j\})=\widehat{1_{e_j}}(S),
\tag{3.1}
\]

and every Fourier coefficient involving two or more host bits vanishes.

For a pair `e={a,b}`,

\[
\widehat{1_e}(S)=2^{-9}[\chi_S(a)+\chi_S(b)].
\tag{3.2}
\]

Exactly 256 of these 512 coefficients are nonzero and each nonzero squared mass is `2^-16`.  Therefore **every host pair contributes exactly `1/16` to spectral entropy**.

For influence, if `a,b` are adjacent, the parity condition in (3.2) forces the unique differing coordinate out of `S`, so the mean core Fourier level is 4; including the host singleton gives contribution

\[
\frac5{256}.
\tag{3.3}
\]

If their Hamming distance is at least two, every core coordinate has conditional marginal `1/2` under the parity equation, so the mean core level is `9/2`; including the host singleton gives

\[
\frac{11}{512}.
\tag{3.4}
\]

Consequently, for the source (all nine pairs adjacent),

\[
H(F_{E_0})=H(\widehat g_{E_0}^{\,2})+\frac9{16},
\qquad
I(F_{E_0})=\sum_S |S|\widehat g_{E_0}(S)^2+\frac{45}{256}.
\tag{3.5}
\]

The same formula holds for a one-pair replacement, with the host influence changed by exactly `1/512` when the new pair is nonadjacent.

This decomposition is useful because a replacement only changes the 9-bit integer Walsh transform by

\[
W_E(S)=W_{E_0}(S)+\chi_S(a_0)+\chi_S(b_0)-\chi_S(a)-\chi_S(b),
\tag{3.6}
\]

where `{a_0,b_0}` is the removed source pair and `{a,b}` the new pair.  Thus the entire 277,875-member family can be certified using exact 512-entry integer transforms; no 18-cube truth-table enumeration is needed.

## 4. New theorem: strict one-host local rigidity

### Theorem 4.1

For the exact source Numaro gate,

\[
\boxed{
\frac{H(F_{E_0})}{I(F_{E_0})-1}>6.52184.
}
\tag{4.1}
\]

For **every** nonidentity one-host-pair replacement described in Section 2,

\[
\boxed{
\frac{H(F_E)}{I(F_E)-1}<6.48279.
}
\tag{4.2}
\]

Hence the source gate is separated from the entire one-host replacement family by the rigorous gap

\[
\boxed{
\frac{H(F_{E_0})}{I(F_{E_0})-1}
-
\sup_{E\text{ one-host replacement}}
\frac{H(F_E)}{I(F_E)-1}
>\frac{781}{20000}=0.03905.
}
\tag{4.3}
\]

At the uniform balanced bias, where

\[
c_G=4\left(\frac{H(G)}{I(G)-1}-6.4548\right),
\tag{4.4}
\]

this becomes

\[
\boxed{c_{F_{E_0}}>0.26816},
\qquad
\boxed{c_{F_E}<0.11196\text{ for every nonidentity one-host replacement}.}
\tag{4.5}
\]

Therefore **none of these 277,875 sparse source deformations comes remotely close to falsifying the current stable lift `a_*=0.268204856`**.  The near-saturation of the original Numaro source is not stable under a single host relocation.

### Proof/certificate

The checker reconstructs the exact source hash, forms the 9-bit integer Walsh transform, and uses (3.6).  It enumerates all 277,875 replacements: 7,767 adjacent replacement pairs and 270,108 nonadjacent pairs.

For each integer Walsh amplitude `t`, `log_2 t` is enclosed rigorously using

\[
\log q
=2\sum_{r=0}^{N-1}\frac{y^{2r+1}}{2r+1}+R_N,
\qquad
y=\frac{q-1}{q+1},
\]

with

\[
0\le R_N\le\frac{2y^{2N+1}}{(2N+1)(1-y^2)},
\]

using exact `Fraction` arithmetic, `N=40`, and outward rounding to a `10^{-7}` fixed grid.  Influence numerators are integers.  Every sign decision is then an integer comparison.

The smallest positive integer certificate slack for (4.2) is `953651200000`.  The diagnostic largest ordinary-float ratio is

\[
6.482786486849179,
\]

with `H=6.786667103420234` and `I=2.046875`; the rigorous outward diagnostic upper value is `6.482786525`, still below the certified rational threshold `6.48279`.

The source itself reconstructs

\[
I(F_{E_0})=\frac{261}{128}=2.0390625,
\]

and the same interval machinery proves (4.1).  The familiar diagnostic value is `6.521845710923...`, consistent with the inherited source report, but (4.1) is proved here independently at the weaker rational threshold used for the local-gap theorem.

## 5. Attempted refutation and the dead route

The attempted falsification was deliberately hostile: keep the source core and eight source hosts exactly, then move the ninth host pair **anywhere among the remaining positive core cells**, including nonedges.  This is a much larger perturbation set than changing an edge to a neighboring edge.

It fails decisively.  The best replacement is over `0.03905` below the source ratio in the support-deficit units, and over `0.15624` below the stable scalar lift in `c_G` units.

The tensor/asymptotic continuation of these deformations is also a dead route: fleet02/B17's exact composition cocycle makes the margin of every disjoint tensor/recursive composition a nonnegative weighted average of primitive margins.  Tensoring a `c_G<0.11196` replacement cannot produce a `c_G>0.268204856` falsifier.

This does **not** prove local optimality against simultaneous multi-host moves, shared-core grafts, or off-center product biases.

## 6. Old/new missing implication and next attack

**Old missing implication.** Prove the stable lifted all-gate inequality for every composition-prime Boolean gate and every interior product bias, or find a source-valid prime gate/bias with required margin above the stable lift.

**New result.** The exact 18-input Numaro source is a strict local maximizer against the complete 277,875-member one-host-pair replacement family, with a certified ratio gap `>0.03905`; every such replacement has base margin `<0.11196`.  Disjoint tensor/asymptotic amplification of those replacements is impossible by the consumed composition cocycle.

**Replacement obligation.** A serious adversary must change the source **coherently**: simultaneous multi-host/shared-core interference, the newer shared-graft mechanism, or an off-center bias that changes the gate margin without decomposing into paid factors.  One-host relocation and its disjoint tensor closure should not consume another run.

**Next recipient.** `fleet04/B16`, whose latest source-bound work already studies coherent off-center movement of the same n=18 source.  The suggested next exact test is to combine its bias direction with a two-or-more-host coherent deformation, rather than another one-host or disjoint-tensor perturbation.  `fleet02/B16` remains the structural source/prime-factor partner.

**Full-FEI implication.** Directly useful adversarial elimination, but no universal quantifier has been closed.  Full FEI remains **OPEN / NOT PROVED**.

## 7. Reproducibility and scope

Checker:
`check_b16_numaro_one_host_replacement.py`, committed blob
`4070a39c4a65c25716634a6c541d1ed6c02c6329`.

Captured successful output:
`check_b16_numaro_one_host_replacement_output.json`, committed blob
`a77a81991feead21b87f3fe822720dd2f380cdf3`.

The mathematical subprocess exited `0`.  An unrelated environment spreadsheet-runtime warmup warning appeared on stderr before execution; it is not imported or used by the checker and did not affect its stdout or exit code.

Scoped privacy review: the package contains only FEI mathematics, source-bound hashes, logical role labels, and sanitized verification metadata.  It contains no credentials, scheduler identifiers, machine paths, private transcripts, email/Drive actions, public-posting actions, paid/remote model calls, workflow dispatch, or permission changes.
