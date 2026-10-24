# B12 FEI creative attempt: curvature-to-Palm compression and an exact nonreuse dichotomy

**Status:** full uniform-cube Fourier entropy-influence (FEI) remains **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. No authenticated brain retrieval or receiver-context use occurred in this run.  
**Route:** APPROACHES #1 (spectral-sample sequential compression) joined to #3 (physical sensitivity), and to the current joint-interface B mixed-derivative stability programme.  
**Provenance:** no novelty or publication-priority claim. This is a private proof-route artifact.

Before substantive work this run read `TASKS_2026-09-21.md`, then the read-once `REPORT.md`, then `APPROACHES.md`, and then the current joint four-account FEI order/state. It consumed the completed other-account artifact

`proofnet24/P03-fei/fleet-2026-09-21/account04/B18/20260921T191147Z-mixed-curvature-global-rigidity/REPORT.md`

at scientific snapshot `f19e92d5facf03f83458aebaad175100f5f322c5` (the joint research-state index records report blob `0e8c2cc28da81af8843b565cb47285684b164480`). The point here is to use that mixed-curvature conservation inside B12's existing Palm insertion code, not merely cite it.

The current external lower-bound correction is retained: unrestricted FEI already has a published/recovered lower bound above `6.521845710923046575`; no sharp-constant claim is made here.

## 1. Exact universal statement attempted

Let

\[
  \mu(A)=\widehat f(A)^2,\qquad S\sim\mu,
  \qquad j_i=\Pr(i\in S)=\operatorname{Inf}_i(f),
  \qquad I=\sum_i j_i=\mathbb E|S|.
\]

B12's preceding Palm-insertion report defined the exact normalized insertion-edge law. If `L` is the inserted coordinate and `P` the predecessor prefix, then

\[
  D_{\rm seq}=I\,I_2(L;P)
\]

is exactly the KL saving of the true sequential predictor over the global influence-profile code. For `i\ne k`, if

\[
  q_{ik}:=\Pr(i,k\in S),
\]

then that report proved

\[
\alpha_{ik}:=\Pr(k\in P\mid L=i)=\frac{q_{ik}}{2j_i},
\qquad
\beta_k:=\Pr(k\in P)=\frac{1}{2I}\sum_{r\ne k}q_{rk},
\tag{1.1}
\]

with `alpha_ii=0`, and for any chosen witness coordinate `g(i)`

\[
D_{\rm seq}\ge \sum_i j_i\,d_2(\alpha_{i,g(i)}\|\beta_{g(i)}).
\tag{1.2}
\]

Here `d_2` is binary relative entropy in bits.

The exact universal statement attempted in this run was:

> **CURVATURE-TO-CODE TARGET.** Can the account04 mixed-derivative curvature bank be represented *exactly* as observables of the Palm insertion predictor, so that congestion can be paid without summing the same pair information repeatedly?

The answer is yes at the normalized predictor level. A stronger hope that the whole raw derivative-depth bank can be paid by `D_seq` with a fixed constant is then refuted, even in the folded-influence regime, by odd majority.

## 2. PROVED: spectral co-inclusion = physical co-sensitivity = one quarter of signed mixed curvature

For each active coordinate `i`, write the Boolean derivative row

\[
  g_i=D_i f\in\{0,\pm1\}.
\]

For `k\ne i`, account04/B18 defines

\[
\kappa_{ik}=\mathbb E\bigl(g_i(y)-g_i(y+e_k)\bigr)^2
            =b_{ik}+4o_{ik},
\tag{2.1}
\]

where `b_ik` is support disagreement and `o_ik` is opposite-sign overlap. Its theorem also gives `kappa_ik=kappa_ki`.

Parseval on the derivative row gives a direct bridge to the spectral sample:

\[
\begin{aligned}
\|D_k g_i\|_2^2
&=\sum_{A\supseteq\{i,k\}}\widehat f(A)^2\\
&=q_{ik}.
\end{aligned}
\tag{2.2}
\]

But by the normalization of the discrete derivative used in the peer report,

\[
  \kappa_{ik}=4\|D_k g_i\|_2^2.
\]

Therefore

\[
\boxed{
q_{ik}
=\Pr(i,k\in S)
=\Pr(i,k\in\operatorname{Sens}_f(X))
=\frac{\kappa_{ik}}4
=\frac{b_{ik}+4o_{ik}}4.
}
\tag{2.3}
\]

The middle equality is the preceding B12 exact two-local spectral/sensitivity theorem. Equation (2.3) is the desired exact three-way identification: the same pair mass is simultaneously a Fourier co-inclusion, a physical co-sensitivity probability, and signed mixed-derivative curvature.

Define the derivative depth

\[
  d_i:=\sum_{k\ne i}\|D_k g_i\|_2^2.
\]

Then (2.2) yields

\[
\boxed{d_i=\sum_{k\ne i}q_{ik}}
\tag{2.4}
\]

and hence the Palm predecessor occupancy from (1.1) is exactly

\[
\boxed{\beta_i=\frac{d_i}{2I}.}
\tag{2.5}
\]

Physically,

\[
d_i
=\mathbb E\!\left[
  1_{\{i\in\operatorname{Sens}(X)\}}
  (|\operatorname{Sens}(X)|-1)
\right].
\tag{2.6}
\]

So the account04 depth bank is not merely analogous to B12's predictor congestion: after normalization by `2I` it **is exactly the marginal occupancy of coordinate `i` in the Palm predecessor prefix**.

## 3. PROVED: a signed-curvature nonreuse lower bound for the sequential KL saving

Substitute (2.3)-(2.5) into the one-bit predictor theorem (1.2). For `k\ne i`,

\[
  \alpha_{ik}=\frac{\kappa_{ik}}{8j_i},
  \qquad
  \beta_k=\frac{d_k}{2I},
\tag{3.1}
\]

while the self witness has `alpha_ii=0`.

Therefore

\[
\boxed{
D_{\rm seq}
\ge
\sum_i j_i
\max\left\{
  \log_2\frac1{1-d_i/(2I)},
  \max_{k\ne i}
  d_2\!\left(
    \frac{\kappa_{ik}}{8j_i}
    \middle\|
    \frac{d_k}{2I}
  \right)
\right\}.
}
\tag{3.2}
\]

This is an **exact nonreuse payment**: every label `i` chooses only one observable of its Palm prefix, so the parity-MUX overcount from the preceding B12 run cannot occur. The orientation term `4o_ik` is automatically retained; replacing `kappa_ik` by unsigned support disagreement would lose legitimate predictor signal.

The self-exclusion witness alone gives

\[
\boxed{
D_{\rm seq}
\ge
\sum_i j_i\log_2\frac1{1-d_i/(2I)}
\ge
\frac1{2I\ln2}\sum_i j_i d_i.
}
\tag{3.3}
\]

The last step is `-ln(1-x)>=x`. Thus the sequential code pays a **globally normalized, influence-weighted depth bank** with no dimension factor.

There is also a useful row-heterogeneity form. Pinsker's inequality in bits,

\[
d_2(a\|b)\ge \frac{2}{\ln2}(a-b)^2,
\]

gives, for any choice `g(i)\ne i`,

\[
\boxed{
D_{\rm seq}
\ge
\frac1{2\ln2}\sum_i j_i
\left(
\frac{\kappa_{i,g(i)}}{4j_i}
-
\frac{d_{g(i)}}I
\right)^2.
}
\tag{3.4}
\]

Optimizing `g(i)` independently gives the corresponding rowwise maximum. Hence a signed-curvature row that differs substantially from the global normalized depth profile creates actual sequential-prediction information.

## 4. PROVED: robust near-subcube rows obey a low-congestion predictor / high-depth-cluster dichotomy

Use the exact `rho`-near-subcube setup of the consumed account04/B18 report. Thus row `i` has support `E_i` within symmetric-difference error

\[
  \varepsilon_i\le \rho j_i
\]

of a coordinate subcube `Q_i` of measure `s_i`, with transverse set `F_i`, and for every `k\in F_i`

\[
  b_{ik}\ge 2(s_i-\varepsilon_i),
  \qquad |s_i-j_i|\le\varepsilon_i.
\tag{4.1}
\]

Using `kappa_ik>=b_ik` and (2.3),

\[
q_{ik}
\ge \frac{s_i-\varepsilon_i}{2}
\ge \frac{1-2\rho}{2}j_i.
\]

Consequently every transverse coordinate satisfies

\[
\boxed{
\alpha_{ik}\ge a_\rho:=\frac{1-2\rho}{4}.
}
\tag{4.2}
\]

Fix any `tau<a_rho`. Let `G_tau` be the set of robust rows having at least one transverse coordinate `k\in F_i` with

\[
  \frac{d_k}{2I}\le\tau.
\]

Choose one such `k` as the witness for each `i\in G_tau`. Since binary KL is minimized over `alpha>=a_rho`, `beta<=tau<a_rho` at `(a_rho,tau)`, (3.2) gives

\[
\boxed{
D_{\rm seq}
\ge
d_2(a_\rho\|\tau)
\sum_{i\in G_\tau}j_i.
}
\tag{4.3}
\]

At the peer report's threshold `rho=1/16`,

\[
  a_\rho=\frac7{32}.
\]

Taking `tau=1/8`,

\[
\boxed{
D_{\rm seq}
\ge 0.0488755046041\ldots
\sum_{i\in G_{1/8}}j_i.
}
\tag{4.4}
\]

Every robust row outside `G_{1/8}` has the opposite structural property:

\[
\boxed{
  d_k>I/4\quad\text{for every }k\in F_i.
}
\tag{4.5}
\]

So robust rows now split rigorously into:

1. a **low-congestion branch**, where actual Palm predictor information pays a fixed influence fraction with no pairwise reuse; and
2. a **high-depth cluster branch**, where every transverse coordinate lies in a globally congested derivative-depth region and must be handled by block/factorial or adaptive-elimination structure rather than another sum of pair KL terms.

This does not yet pay the peer report's full restriction entropy, which can contain a `j_i log(1/j_i)` scale. It is a genuine interface reduction, not FEI closure.

## 5. REFUTED: the raw derivative-depth bank cannot be paid by sequential information at a fixed constant

A tempting strengthening of (3.3) is

\[
\tag{FALSE-DEPTH}
D_{\rm seq}\stackrel?\ge c\sum_i d_i
\]

for an absolute `c>0`. This would immediately absorb the account04/B18 global near-subcube payment `13.348 sum_i d_i`. It is false even when every active influence is at most `1/2`.

Take odd majority on

\[
  n=2m+1
\]

variables. Every coordinate has influence

\[
  j=\binom{2m}{m}/2^{2m}\le\frac12,
  \qquad I=nj.
\tag{5.1}
\]

The physical sensitivity set has size `m+1` exactly on the two middle Hamming layers and is empty elsewhere. Therefore

\[
\mathbb E[|\operatorname{Sens}|(|\operatorname{Sens}|-1)]
=mI.
\]

By the exact two-local identity this equals

\[
\sum_i d_i=mI.
\tag{5.2}
\]

On the other hand

\[
D_{\rm seq}=I\,I_2(L;P)\le I H(L)\le I\log_2 n.
\tag{5.3}
\]

Hence

\[
\boxed{
\frac{D_{\rm seq}}{\sum_i d_i}
\le \frac{\log_2(2m+1)}m
\longrightarrow0.
}
\tag{5.4}
\]

So (FALSE-DEPTH) is **REFUTED** for every positive universal `c`.

The numerical upper bounds in (5.4) are already

- `0.13316423` at `n=101`,
- `0.01993445` at `n=1001`,
- `0.00265757` at `n=10001`.

The same family also refutes a fixed payment for the full positive depth-defect bank

\[
\sum_i j_i\delta_i,
\qquad
\delta_i=\frac{d_i}{j_i}-\frac12\log_2\frac1{j_i},
\]

because symmetry gives `d_i=mj_i`, so

\[
\sum_i j_i\delta_i
=I\left(m-\frac12\log_2\frac1j\right),
\]

while (5.3) remains only `I log_2 n`. Their ratio also tends to zero.

This is the decisive dead end of the run: **the raw depth bank that appears after mixed-curvature aggregation is too large to be globally paid by Palm mutual information alone.** The normalization in (3.3) is not a cosmetic proof loss.

## 6. Why this changes the joint proof interface

The consumed account04/B18 result replaces bounded transverse-set incidence by the exact curvature/depth bank. The present run identifies exactly what B12's sequential code can and cannot do with that bank:

- it sees every signed pair curvature exactly through (2.3);
- it converts normalized depth into real Palm predecessor occupancy through (2.5);
- it pays row heterogeneity and low-congestion robust rows without pairwise double counting through (3.2)-(4.4);
- but majority proves that no fixed `D_seq >= c sum d_i` conversion can finish the aggregation.

Thus the remaining joint implication is smaller and more concrete: **eliminate or block-compress the high-depth-cluster branch before trying to spend predictor information.** The raw depth bank must first be converted to a nonreusing influence-scale object; it cannot simply be charged after summation.

## 7. Next attack

For a robust row outside `G_tau`, every `k in F_i` has large normalized depth `d_k/I`. Instead of paying those rows individually, form the graph whose edges are the signed pair masses

\[
  q_{ik}=\kappa_{ik}/4.
\]

The next attack is to construct an **adaptive cluster contraction** of this reversible symmetric graph:

1. low-congestion transverse edges are discharged by (4.3);
2. high-depth coordinates are merged into a block before another label is encoded;
3. the exact prefix factorial rebate is retained inside each merged block;
4. mixed-curvature conservation is used to prove that an edge is consumed at most once when blocks merge.

The first falsification family must be odd majority, because it has huge raw depth but little label information; a valid contraction must collapse its dense near-exchangeable cluster rather than attempt to pay `sum d_i`. The second stress family is the selector-of-parities counterexample from the preceding B12 run, which detects repeated charging of one latent cluster bit.

If a block-contraction lemma yields total low-congestion predictor cost plus cluster-activation/factorial cost `O(I)`, it plugs directly into the existing exact prefix decomposition and gives a dimension-free FEI bound. That lemma is **OPEN**.

## 8. Classification

**PROVED**

- Exact three-way pair identity (2.3): spectral co-inclusion = physical co-sensitivity = one quarter signed mixed curvature.
- Exact depth-to-Palm occupancy identity `beta_i=d_i/(2I)`.
- Signed-curvature nonreuse predictor bound (3.2), weighted normalized-depth payment (3.3), and row-heterogeneity payment (3.4).
- Robust near-subcube low-congestion/high-depth dichotomy (4.3)-(4.5), including the explicit `0.0488755046041...` constant at `rho=1/16`, `tau=1/8`.

**REFUTED**

- Any universal fixed `D_seq >= c sum_i d_i`, `c>0`.
- Any universal fixed `D_seq >= c sum_i j_i delta_i`, `c>0`.

**OPEN**

- The high-depth cluster contraction/nonreuse lemma.
- Conversion of the remaining block cost into `O(I)` while preserving the factorial rebate.
- Full uniform-cube FEI.
