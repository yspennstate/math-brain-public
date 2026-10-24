# B18 FEI synthesis: prefix-total-correlation refund and all-witness near-subcube payment

**Status:** full uniform-cube Friedgut--Kalai Fourier entropy--influence (FEI) remains **OPEN / NOT PROVED**.

**Route:** APPROACH 11 (sequential/prefix coding) + APPROACH 12 (restricted potential), integrated with the current physical near-subcube restriction programme.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. No authenticated brain retrieval/context was available or claimed. No novelty/publication-priority claim is made.

## 1. Exact predecessor results actually consumed

This derivation uses, rather than merely lists, the following completed other-account artifacts.

1. `proofnet24/P03-fei/fleet-2026-09-21/account03/B12/20260921T194351Z-curvature-palm-nonreuse/REPORT.md`, report blob `ddf8baf96385418c56a91c48f62c04168633faaa`. It gives the exact uniform-prefix/Palm insertion law, `D_seq = I I_2(L;P)`, and for a Boolean spectral sample
   \[
   \alpha_{ik}:=\Pr(k\in P\mid L=i)=\frac{\kappa_{ik}}{8p_i}\quad(i\ne k),
   \qquad \alpha_{ii}=0,
   \qquad \beta_k:=\Pr(k\in P)=\frac{d_k}{2I}.
   \]
   Here `p_i=Inf_i(f)`, `d_k=sum_{j ne k} Pr(j,k in S)`, and `kappa_ik` is the signed mixed-curvature quantity from the joint derivative-row programme.

2. `proofnet24/P03-fei/fleet-2026-09-21/account04/B14/20260921T184113Z-posterior-crossing-budget/REPORT.md`, report blob `c974b249c6cc513019bd0e58e7711ad808c80844`. It identifies the exact physical folded-drift crossing refund `D_A=I_A+C_A` and supplies the current restriction-potential interface.

3. `proofnet24/P03-fei/fleet-2026-09-21/account02/interactive/20260921T192650Z-joint-fei-subcube-peeling/ADDENDUM.md`, blob `baa3155a268d936d6b191667ee71a6df84969292`. Its Theorem C.1 gives the genuine physical block step `Delta_Z H <= 12 I_Z` when a maximum/average-controlled pivot is within `2^-r/(16r)` of a codimension-`r` sensitivity subcube. The companion fixed-relative obstruction is retained: a mere relative `1/16` row approximation does not by itself pay the defining block.

The point of the present report is to remove the **one-witness bottleneck** in the Palm code by charging dependence to one explicit total-correlation potential, so that all low-congestion transverse witnesses can be used simultaneously without pairwise reuse.

## 2. Uniform-prefix notation

Let `S` be the Fourier spectral sample,
\[
\Pr(S=A)=\widehat f(A)^2,
\qquad K=|S|,
\qquad I=\mathbb E K=\sum_i p_i,
\qquad p_i=\Pr(i\in S).
\]
Assume `I>0`; constants are trivial.

Use the exact uniform-prefix edge law of the account03/B12 predecessor: sample a terminal set with the size-biased law, take a uniformly random ordering and a uniformly random insertion edge. Let `P` be the unordered prefix and `L` the next inserted label. Put
\[
Y_k=1_{\{k\in P\}},
\qquad
\alpha_{ik}=\Pr(Y_k=1\mid L=i),
\qquad
\beta_k=\Pr(Y_k=1).
\]
Then
\[
\Pr(L=i)=\frac{p_i}{I},
\qquad
D_{\rm seq}:=I\,I_2(L;P).
\]
All entropies and KL divergences below are in bits.

Define the prefix total correlation and its conditional version by
\[
\operatorname{TC}(P)=\sum_k H_2(Y_k)-H_2(P),
\]
\[
\operatorname{TC}(P\mid L)=\sum_k H_2(Y_k\mid L)-H_2(P\mid L).
\]
The conditional quantity is the average total correlation of the prefix bits after the insertion label is known, hence is nonnegative.

## 3. PROVED: exact TC-refunded all-witness tensorization

### Theorem 3.1
For the uniform-prefix edge law of **every** random subset distribution,
\[
\boxed{
D_{\rm seq}+I\operatorname{TC}(P)
=
I\sum_k I_2(L;Y_k)+I\operatorname{TC}(P\mid L)
\ge
\sum_{i,k}p_i\,d_2(\alpha_{ik}\|\beta_k).
}
\tag{3.1}
\]
In fact the last displayed right side equals `I sum_k I_2(L;Y_k)` exactly.

### Proof
For any random vector `P=(Y_1,...,Y_n)`,
\[
\begin{aligned}
\sum_k I_2(L;Y_k)-I_2(L;P)
&=\sum_k[H(Y_k)-H(Y_k\mid L)]-[H(P)-H(P\mid L)]\\
&=\operatorname{TC}(P)-\operatorname{TC}(P\mid L).
\end{aligned}
\]
Rearrange and multiply by `I`. Since `D_seq=I I_2(L;P)` and conditional total correlation is nonnegative,
\[
D_{\rm seq}+I\operatorname{TC}(P)
\ge I\sum_k I_2(L;Y_k).
\]
Finally, conditioning on `L=i` gives a Bernoulli law with parameter `alpha_ik`, while the unconditional bit has parameter `beta_k`; therefore
\[
I I_2(L;Y_k)
=\sum_i p_i d_2(\alpha_{ik}\|\beta_k).
\]
Sum over `k`. QED.

### Boolean curvature form
For a Boolean Fourier spectrum the consumed account03/B12 identities substitute directly into (3.1):
\[
\boxed{
D_{\rm seq}+I\operatorname{TC}(P)
\ge
\sum_i p_i\left[
\log_2\frac1{1-d_i/(2I)}
+
\sum_{k\ne i}
 d_2\!\left(
 \frac{\kappa_{ik}}{8p_i}
 \middle\|
 \frac{d_k}{2I}
 \right)
\right].
}
\tag{3.2}
\]
Rows with `p_i=0` are omitted. The first term is the self-exclusion witness `alpha_ii=0`.

This is the key change from the preceding one-witness theorem: **every transverse bit can now contribute simultaneously**. The exact price for avoiding false pairwise reuse is not an uncontrolled multiplicity factor but the single prefix-dependence potential `I TC(P)`. No independence assumption is made.

## 4. PROVED: robust near-subcube rows now receive a linear-in-codimension code refund

Take any family `R` of derivative rows satisfying the robust near-subcube hypotheses used in the account03/B12 transfer from account04/B18: row `i` is within relative support error
\[
\varepsilon_i\le \rho p_i
\]
of a coordinate subcube with transverse coordinate set `F_i`, and the inherited geometric argument gives, for every `k in F_i`,
\[
\alpha_{ik}\ge a_\rho:=\frac{1-2\rho}{4}.
\tag{4.1}
\]
Fix `tau<a_rho` and define the low-congestion transverse set
\[
F_i^{\rm lo}(\tau)=\{k\in F_i:\ \beta_k\le\tau\}.
\]
Since binary KL is minimized on `alpha>=a_rho`, `beta<=tau<a_rho` at `(a_rho,tau)`, Theorem 3.1 yields
\[
\boxed{
D_{\rm seq}+I\operatorname{TC}(P)
\ge
c_{\rho,\tau}
\sum_{i\in R}p_i\,|F_i^{\rm lo}(\tau)|,
\qquad
c_{\rho,\tau}:=d_2(a_\rho\|\tau)>0.
}
\tag{4.2}
\]
This is a genuine `r p_i`-scale refund when a positive fraction of the `r=|F_i|` transverse controls are low-congestion.

At the current relative threshold `rho=1/16`,
\[
a_\rho=\frac7{32}.
\]
Taking `tau=1/8` gives
\[
\boxed{c_{1/16,1/8}=0.04887550460410142\ldots.}
\tag{4.3}
\]
Thus if at least a fraction `theta` of an `r`-control robust row is low-congestion,
\[
D_{\rm seq}+I\operatorname{TC}(P)
\ge 0.0488755\,\theta\,r p_i
\]
from that row's witnesses before using any other positive terms.

Conversely, if fewer than `theta r` controls are low-congestion, more than `(1-theta)r` controls satisfy
\[
\beta_k>\frac18,
\qquad\text{equivalently}\qquad d_k>\frac I4.
\tag{4.4}
\]
So the old binary low-congestion/high-depth dichotomy becomes a **quantitative fraction dichotomy**: either the corrected sequential bank pays linearly in the codimension, or a linear fraction of the defining controls belongs to the high-depth cluster.

## 5. Integration with the genuine physical near-support block theorem

For a maximum-influence pivot whose sensitivity support is compared with a codimension-`r` subcube of measure `q=2^-r`, the account02 Theorem C.1 gives the first branch
\[
\varepsilon\le\frac{q}{16r}
\quad\Longrightarrow\quad
\Delta_ZH\le12I_Z.
\tag{5.1}
\]
Hence a centered physical-restriction-critical core of ratio `>12` cannot enter branch (5.1).

In the larger **relative** near-subcube regime, where a fixed-relative block estimate is known to be false, (4.2) gives a different resource. For any chosen `theta in (0,1)` one now has the following honest three-way alternative:

1. **very close row:** (5.1) holds and the actual physical control block is paid with coefficient 12;
2. **many low-congestion controls:** at least `theta r` transverse coordinates satisfy `beta_k<=1/8`, and the corrected sequential bank pays at least `0.0488755 theta r p_i`;
3. **high-depth cluster:** more than `(1-theta)r` transverse coordinates satisfy `d_k>I/4`.

This does **not** claim that every dangerous row is relatively near a subcube. It also does not claim that branch 3 is already paid. What changes is that the fixed-relative obstruction no longer leaves an undifferentiated bad case: after the true physical `q/(16r)` step is removed, the remaining relative-near-subcube branch is reduced to an explicit global high-depth clustering problem unless the sequential potential already returns the missing logarithmic scale.

## 6. PROVED: the entire prefix stop bank is universally O(I) for Boolean spectra

The earlier account03/B12 uniform-prefix chain proves
\[
H(S)=J_{\rm stop}+\operatorname{Br}-\mathbb E\log_2(K!),
\qquad
J_{\rm stop}\le H(K),
\tag{6.1}
\]
and
\[
\operatorname{Br}=I H_2(L)-D_{\rm seq}.
\tag{6.2}
\]
Here `L` has distribution `p_i/I`.

The scalar stop entropy can in fact be paid by influence with a universal constant.

### Lemma 6.1
For every Boolean `f`,
\[
\boxed{H_2(K)\le5I(f).}
\tag{6.3}
\]
Consequently `J_stop<=5I`.

### Proof
Let
\[
\alpha=\min\{\Pr(f=1),\Pr(f=-1)\}\le\tfrac12,
\qquad
V=\Pr(K>0)=1-\widehat f(\varnothing)^2=4\alpha(1-\alpha).
\]
Conditioned on `K>0`, the positive-integer variable has mean `m=I/V>=1`. Among distributions on `{1,2,...}` with fixed mean `m`, the geometric law maximizes entropy, and its entropy divided by `m` is `h_2(1/m)<=1`. Therefore
\[
V H(K\mid K>0)\le I.
\tag{6.4}
\]
Also `H(K)=h_2(V)+V H(K|K>0)`.

To pay `h_2(V)`, let `B_1,B_2` be independent Bernoulli(`alpha`) and `Q=B_1 xor B_2`, so `Pr(Q=1)=q=2alpha(1-alpha)` and `V=2q`. Concavity of binary entropy and `h_2(0)=0` give `h_2(2q)<=2h_2(q)`, while `H(Q)<=H(B_1,B_2)=2h_2(alpha)`. Thus
\[
h_2(V)\le4h_2(\alpha).
\]
For `0<alpha<=1/2`, the elementary scalar inequality
\[
h_2(\alpha)\le2\alpha\log_2(1/\alpha)
\]
holds (subtract the two sides; the derivative has one interior maximum and the difference vanishes at both limiting endpoints). Edge isoperimetry on the Boolean cube gives
\[
I(f)\ge2\alpha\log_2(1/\alpha).
\]
Hence `h_2(V)<=4I`. Combine with (6.4). QED.

The constant five is intentionally nonsharp; the point is that the whole stop/survival bank is no longer a dimension-dependent obstruction.

## 7. One universal inequality with each refund counted once

Define
\[
\Gamma(f):=\sum_i p_i\left[
\log_2\frac1{1-d_i/(2I)}
+
\sum_{k\ne i}d_2\!\left(\frac{\kappa_{ik}}{8p_i}\middle\|\frac{d_k}{2I}\right)
\right].
\tag{7.1}
\]
Combining (6.1)--(6.3) with Theorem 3.1 gives the source-exact universal bound
\[
\boxed{
H(f)
\le
5I
+I H_2\!\left(\frac{p_1}{I},\ldots,\frac{p_n}{I}\right)
-\Gamma(f)
+\underbrace{I\operatorname{TC}(P)-\mathbb E\log_2(K!)}_{R_{\rm pref}(f)}.
}
\tag{7.2}
\]
No term on the right is counted twice. `Gamma` contains all bitwise signed-curvature predictor savings; `R_pref` is the exact remaining prefix-dependence/factorial remainder created by making those bitwise savings additive.

Equation (7.2) is not FEI closure: neither `I H(L)-Gamma` nor `R_pref` has yet been proved `O(I)` for all Boolean functions. It does, however, isolate the APPROACH-11/12 gap more sharply than the preceding max-witness inequality.

## 8. Killed shortcut and next recipient

A proof must **not** simply drop `I TC(P)` from (3.1). Total correlation is exactly the price of tensorizing all prefix-bit signals; without a separate bound or a telescoping potential argument, doing so would reintroduce the same hidden reuse that the Palm construction was designed to avoid.

The next concrete target is one of the following two statements, each materially narrower than full FEI:

- prove an influence-scale/telescoping bound for the prefix dependence remainder
  \[
  R_{\rm pref}=I\operatorname{TC}(P)-\mathbb E\log_2(K!),
  \]
  on Boolean Fourier spectra; or
- in the high-depth-cluster branch of Section 5, construct a physical block contraction that makes `R_pref` decrease by the same order as the lost `r p_i` branching cost.

Primary recipients are the APPROACH-11 coding workers and the A/B-interface block-selection workers. The exact handoff formula is (7.2), with (4.2) as the robust-row insertion. Full FEI remains **OPEN** until the remaining universal arrows are proved.
