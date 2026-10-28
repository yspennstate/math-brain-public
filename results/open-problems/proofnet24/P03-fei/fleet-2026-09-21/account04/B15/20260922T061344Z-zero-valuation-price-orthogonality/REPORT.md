# account04/B15 — zero valuation can coexist with indispensable coordinate-price KL

**Run:** `20260922T061344Z-b15-310d366b`  
**Classification:** `CANDIDATE_REFUTED / SOURCE_PRICE_CREDIT_SEPARATED / PRIME-GATE_STRESS`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.

## 0. Change summary and live scope


The newest completed account02/B15 result consumed is

`proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T054027Z-packet-price-kl-numaro/REPORT.md`,

report blob `8f6afebd4c7f6ba33533a660e380fd06aefe6488`.

For a balanced Boolean source with spectral sample `S`, level `K=|S|`, level law `W_k`, influence marginals `j_i=Pr(i in S)`, total influence `I=sum_i j_i`, and normalized occurrence law `q_i=j_i/I`, that report proves the exact identity

\[
\boxed{
H(f)=H(K)+C_{\rm coll}(f)-D_{\rm pp}(f),
}
\tag{0.1}
\]

where

\[
C_{\rm coll}=I H_2(q)+\mathbb E\log_2 e_K(q),
\tag{0.2}
\]

and

\[
D_{\rm pp}=D_{\rm lev}
=\sum_k W_kD_{\rm KL,2}(\pi_k\|\nu_k).
\tag{0.3}
\]

Here

\[
\pi_k(A)=\frac{\widehat f(A)^2}{W_k},\qquad
\nu_k(A)=\frac{\prod_{i\in A}q_i}{e_k(q)}.
\tag{0.4}
\]

The same source proves that the statistic

\[
T_k(A)=\left(|\widehat f(A)|,\prod_{i\in A}q_i\right)
\tag{0.5}
\]

is sufficient for the entire KL in (0.3), and splits it exactly as

\[
\boxed{D_{\rm pp}=D_{\rm mag}+D_{\rm price\mid mag}.}
\tag{0.6}
\]

Thus on the balanced-uniform slice of the live all-gate center `C_*=6.5218512`, the exact expression being paid is

\[
\boxed{
H(K)+C_{\rm coll}-D_{\rm mag}-D_{\rm price\mid mag}
\le C_*[I-1].
}
\tag{0.7}
\]

No positive part is taken and no KL term is dropped.  On the Numaro source the price-within-packet credit is indispensable: the predecessor certifies that magnitude KL alone leaves the normalized defect below `-0.032131617677`, whereas restoring the price credit gives the true positive normalized defect only about `5.49e-6`.

The second exact input retained is account02/B15's valuation majorization theorem.  If `r_a` is the signed physical valuation of magnitude packet `a`, then for every nonnegative coordinate cost vector `c`,

\[
\mathbb E_a\,\sigma_{r_a}(c)\le2\sum_i c_iq_i^{\rm fold},
\tag{0.8}
\]

and in particular every valuation-depth tail is influence-paid.  This report asks the sharp next question: **can that valuation information itself force the coordinate-price KL credit that the Numaro calculation needs?**  The answer is no, already on a four-variable composition-prime Boolean gate.

## 1. Exact price-dispersion identity inside a magnitude packet

Fix a level `k` and a nonzero Fourier magnitude `m`, and let

\[
\mathcal C=\{A:|A|=k,\ |\widehat f(A)|=m\}
\tag{1.1}
\]

be a nonempty packet/level cell.  Conditional on `C`, the actual source law is uniform because all squared Fourier coefficients in the cell are equal.  Put

\[
L(A)=\prod_{i\in A}q_i.
\tag{1.2}
\]

The reference law inherited from `nu_k`, further conditioned on the same magnitude cell, is therefore

\[
Q_{\mathcal C}(A)=\frac{L(A)}{\sum_{B\in\mathcal C}L(B)},
\qquad
P_{\mathcal C}(A)=\frac1{|\mathcal C|}.
\tag{1.3}
\]

### Theorem 1 — price KL is exactly an AM/GM gap

For every such cell,

\[
\boxed{
D_{\rm KL,2}(P_{\mathcal C}\|Q_{\mathcal C})
=
\log_2\frac{\operatorname{AM}_{\mathcal C}(L)}
{\operatorname{GM}_{\mathcal C}(L)}.
}
\tag{1.4}
\]

Equivalently, with `X(A)=-log_2 L(A)`,

\[
\boxed{
D(P_{\mathcal C}\|Q_{\mathcal C})
=\mathbb E_{P_{\mathcal C}}X
+\log_2\mathbb E_{P_{\mathcal C}}2^{-X}.
}
\tag{1.5}
\]

### Proof

Let `M=|C|` and `Z=sum_C L`.  Then

\[
\begin{aligned}
D(P_C\|Q_C)
&=\frac1M\sum_{A\in C}
\log_2\frac{1/M}{L(A)/Z}\\
&=\log_2\frac ZM-rac1M\sum_{A\in C}\log_2L(A)\\
&=\log_2\frac{\mathrm{AM}(L)}{\mathrm{GM}(L)}.
\end{aligned}
\]

This is exact.  In particular the coordinate-price credit vanishes **iff** the occurrence price is constant inside the cell.  No packet integrality or probability-law relaxation is used.

This reformulates account04/B17's exact price-hazard ladder as a geometric dispersion: the ladder is one chain-rule expansion of the same AM/GM gap.

## 2. A four-variable Boolean prime gate with every valuation equal to zero but positive price KL

Let

\[
f:\{0,1\}^4\to\{-1,+1\}
\]

be `-1` exactly on

\[
\boxed{\{0,1,2,3,4,5,6,8\}},
\tag{2.1}
\]

using the usual integer labels with coordinate `0` least significant.  The gate is balanced.  Its exact unnormalised Walsh vector is

\[
\boxed{
(0,-4,-4,0,-4,0,0,-4,-12,0,0,4,0,4,4,0).
}
\tag{2.2}
\]

Hence there are only two nonzero magnitude packets, raw magnitudes `4` and `12`.  The influence vector and total influence are

\[
\boxed{
(j_0,j_1,j_2,j_3)=\left(\frac14,\frac14,\frac14,\frac34\right),
\qquad I=\frac32,
}
\tag{2.3}
\]

so

\[
\boxed{
q=\left(\frac16,\frac16,\frac16,\frac12\right).
}
\tag{2.4}
\]

### 2.1 Every signed magnitude-packet valuation is zero

The raw-magnitude-`12` packet is a singleton Fourier character.  Its signed physical packet sum is therefore `+/-1` pointwise, so its valuation is zero.

The raw-magnitude-`4` packet contains seven frequencies.  Its signed physical packet sum at every physical point is a sum of seven numbers from `{+1,-1}`.  It is therefore odd and in particular never divisible by two.  Thus its valuation is also zero.

Consequently

\[
\boxed{r_4=r_{12}=0,\qquad R=\sum_ap_ar_a=0,}
\tag{2.5}
\]

and **every** positive valuation-depth tail in account02/B15's theorem is identically zero on this source.

### 2.2 The coordinate-price KL is nevertheless strictly positive

The nonzero `(level,magnitude)` cells are

\[
(1,4):\{1,2,4\},\qquad
(1,12):\{8\},\qquad
(3,4):\{7,11,13,14\}.
\tag{2.6}
\]

The first two cells have constant occurrence price, hence zero price KL by Theorem 1.  In the `(3,4)` cell the four occurrence prices are

\[
\boxed{
\left(\frac1{216},\frac1{72},\frac1{72},\frac1{72}\right).
}
\tag{2.7}
\]

The source law in this cell is uniform, while the reference law is proportional to these prices:

\[
\boxed{
P=\left(\frac14,\frac14,\frac14,\frac14\right),
\qquad
Q=\left(\frac1{10},\frac3{10},\frac3{10},\frac3{10}\right).
}
\tag{2.8}
\]

Therefore the within-cell KL is exactly

\[
\boxed{
D_{\rm cell}
=\log_2 5-1-\frac34\log_2 3
=0.133206219346495\ldots>0.
}
\tag{2.9}
\]

The positivity is exact: multiplying by four, it is equivalent to

\[
5^4>2^4 3^3,
\]

i.e. `625>432`.

The spectral mass of this cell is exactly `1/4`.  Hence the entire price-within-magnitude credit is

\[
\boxed{
D_{\rm price\mid mag}
=\frac14\log_2 5-\frac14-\frac3{16}\log_2 3
=0.033301554836624\ldots>0.
}
\tag{2.10}
\]

Thus the all-cost valuation bank (0.8) supplies **zero** positive information on this gate while the exact source has a nonzero coordinate-price KL credit.  The valuation-tail theorem therefore cannot, by itself, recover or certify any positive portion of the price credit required in (0.7).  Direct coordinate-price dispersion/hazard information is genuinely additional source data.

This is the precise obstruction requested by Interface D.  It does **not** say valuation tails are useless: they still pay the signed arithmetic valuation reserve.  It says that reserve and the price-within-packet relative entropy are different currencies and cannot be identified.

## 3. Converse separation: arbitrarily deep valuation with zero price KL

The separation also goes the other way.  Let `m` be even and let `b_m` be any `m`-variable Boolean bent function.  Its Fourier magnitude is constant,

\[
|\widehat b_m(S)|=2^{-m/2}
\]

for every frequency.  Thus it has one magnitude packet.  The signed packet inverse Walsh sum is `2^{m/2}b_m(x)` up to the normalisation convention, so the physical valuation is

\[
\boxed{r=m/2.}
\tag{3.1}
\]

On the other hand the squared spectral law is uniform over all `2^m` subsets.  Hence every coordinate has occurrence probability `1/2`, total influence is `m/2`, and the normalized occurrence law is

\[
q_i=\frac1m.
\tag{3.2}
\]

At every fixed level `k`, every set has identical coordinate price

\[
L(A)=m^{-k}.
\tag{3.3}
\]

Theorem 1 therefore gives

\[
\boxed{D_{\rm price\mid mag}(b_m)=0}
\tag{3.4}
\]

for arbitrarily large packet valuation `r=m/2`.

Together (2.5),(2.10) and (3.1),(3.4) show a genuine two-way orthogonality:

* zero valuation depth does **not** force zero coordinate-price information;
* arbitrarily large valuation depth does **not** force positive coordinate-price information.

Any surviving Interface-D payment must therefore keep the two structures separate until a source-valid coupling is proved.

## 4. The four-bit witness is composition-prime, but very safe for the live all-gate inequality

The owner target asks specifically whether the extremal gate must be decomposable.  The witness above is relevant because it is not hiding this arithmetic effect inside an obvious disjoint composition.

For a coordinate subset `A`, consider the truth-table row obtained by fixing `x_A` and varying the complement.  If a Boolean gate admitted a nontrivial disjoint composition with a child block on `A`, where `2<=|A|<=3`, then those rows could take at most two distinct values, because they would depend on `x_A` only through the one output bit of the child gate.

The exact checker enumerates every such subset.  The numbers of distinct rows are

\[
\begin{array}{c|cccccc}
|A|=2 & 01&02&03&12&13&23\\ \hline
\#\text{ rows}&3&3&4&3&4&4
\end{array}
\tag{4.1}
\]

and for all four three-coordinate subsets the row count is `3`.  Hence no nontrivial block of size two or three can be compressed to one Boolean child, and the gate is composition-prime in the disjoint gate sense used by the current programme.

This gate is **not** a counterexample to the all-gate conjecture.  Its spectral entropy is

\[
H(f)=4-\frac98\log_2 3
=2.216917186688700\ldots,
\tag{4.2}
\]

while `I-1=1/2`.  At the live balanced center `C_*=6.5218512`,

\[
C_*[I-1]-H
=1.044008413311301\ldots>0.
\tag{4.3}
\]

Using the owner's base read-once center `C_0=6.4548`, the comparable uniform-bias margin is

\[
\boxed{c_G=-8.083862506490402\ldots,}
\tag{4.4}
\]

so it has enormous slack.  Its role is to falsify a proposed **proof transfer**, not to falsify FEI or gate extremality.

## 5. Consequence for the current proof chain

The predecessor's exact Numaro calculation established that `D_price|mag` is indispensable on a near-extremal source.  The present theorem shows that account02's signed valuation tails cannot themselves generate that price credit: there are actual Boolean prime gates on which every valuation-tail payment is zero but the price KL is positive, while bent functions show the reverse mismatch.

Therefore the weakest surviving source-exact decomposition of (0.7) must contain three separately tracked pieces:

1. the signed valuation reserve, paid by account02's all-cost/tail theorem;
2. the magnitude-packet KL;
3. the coordinate-price KL, represented exactly by either the AM/GM cell gap (1.4) or the equivalent nested Bernoulli hazard ladder, with every unspent remainder left as negative conditional KL.

A universal argument may couple these terms, but it cannot substitute valuation depth for coordinate-price information.  This narrows the common proof obligation rather than opening another route.

A concrete next owner-aligned question is now: can the exact price AM/GM gap in composition-prime gates be charged to **children's all-gate slack** or another quantity already present in the gate defect, while retaining the conditional KL?  A pointwise local restriction-margin charge is already known false on bent two-point swaps, so any such coupling must be aggregated/source-consistent rather than a blind local bound.

## 6. Checker and verification scope

`CHECKER.py` uses only the Python standard library and exact `Fraction` arithmetic for the Boolean source.  It verifies:

* the exact truth table and Walsh vector (2.2);
* the exact influences and normalized occurrence law (2.3)-(2.4);
* both signed packet valuations are zero;
* the complete `(level,magnitude)` cell list;
* the exact price vectors and reference law (2.7)-(2.8);
* exact positivity of the KL expression by `625>432`;
* every nontrivial block row-count needed for the composition-prime certificate;
* the displayed entropy, live balanced defect and owner-requested comparable margin numerically as secondary diagnostics.

Checker SHA-256:

`d9940496278c4c3d599e8dbf484df3f64487def0b41a2163b2814e9b0ef28a8f`

Captured-output SHA-256:

`f73651a2253b88f02064bed16f10efd7d467e05a217652bfdf03122476b544da`

The finite checker is implementation/falsification evidence; Theorem 1 and the bent-family separation are analytic.

## 7. Scope and literature

No novelty or publication-priority claim is made.  A fresh primary-source check on this invocation still finds unrestricted FEI open: Potapov's 18 September 2026 paper proves FEI for plateaued Boolean functions (sharp class constant `4`) and partially bent functions (sharp class constant `2`), while González--MacManus--Pereyra's 29 May 2026 paper presents restriction/stopping-tree progress and explicitly states that its key general restriction inequality, if universal, would imply full FEI.

The present result is only a source-exact obstruction/reformulation inside the current proof programme.  It does not prove a new FEI subclass theorem and does not alter the full-problem status.

## 8. Provenance and privacy

This run read only the current FEI control/state and source-bound mathematical artifacts.  The report and checker contain only FEI mathematics, logical fleet labels, public bibliographic metadata, and repository-relative scientific paths.  They contain no credentials, scheduler identifiers, machine paths, benchmark gold, unrelated private data, email/Drive actions, paid or remote model calls, workflows, or permission changes.  No notification setting was enabled or changed.
