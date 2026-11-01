# fleet04/B04 — all-bias closure from source-certified interior gate inequalities

Run: `20260922T111423Z-fleet04-B04-fei-allbias-r1`  
Programme: `FEI-ALL-TEAM-20260922T095941Z`  
Assignment: `FEI-20260922-fleet04-B04`  
Outcome: `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 0. Scope and source pins

This report proves a continuum-extension theorem for one fixed finite Boolean gate and one common potential. It does not certify any currently unproved potential for all gates, and hence does not prove FEI.

The coherent owner/control bundle was read at `yspennstate/math-research-brain@a870806cdbbd41bd0bdf4d6926674e4ca4df1b10`, revision `2026-09-22.3`. The live correction inbox had no pending event at that read. The mathematical inputs actually used are:

1. Gate defect and composition formulation: `yspennstate/math-open-problems@f5946fb64d336ed7369de279159643944efc47af`, `proofnet24/P03-fei/continuations/2026-09-22-gate-reformulation/REPORT.md`, Section 1.
2. Exact selector packet and child-defect recursion: `yspennstate/math-open-problems@4ccd51ad517f425a529daa52c3352905b86ea69d`, `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B12/20260922T091546Z-uniform-selector-debit-and-safe-lift/REPORT.md`, Sections 2--4. The refuted scalar candidate from its Section 5 is not used.
3. Assigned partner fleet01/B04: `yspennstate/math-open-problems@494affa18df748849cbf9e584d71a9ec474fb0dd`, `proofnet24/P03-fei/fleet-2026-09-22/fleet01/B04/20260922T104606Z-fleet01-B04-fei/REPORT.md`, especially Theorem 2.1 and Corollary 3.1. Its signed vanishing-selector functional is applied in Section 6 below.
4. A universally safe added direction, used only as an example of a potential with an explicit common modulus: `yspennstate/math-open-problems@c50e06733fc1e7f109e20dbb1a0013d67aa71dc7`, `proofnet24/P03-fei/fleet-2026-09-21/fleet04/B13/20260922T0954Z-nearoptimal-singleton-repair/REPORT.md`, Theorem 2.1. Universality of the repaired base potential remains open.

The safe-cone floor remains `NEEDS_REVALIDATION`; no child slack is deleted here.

## 1. Desingularized physical form of the gate defect

Let `G:{0,1}^k -> {-1,1}` be a Boolean gate and let `p=(p_1,...,p_k)` lie in the closed cube. Put

\[
 V_x=4x(1-x),\qquad A_\Gamma(x)=\Gamma(x)+h_2(V_x).
\]

For each original input coordinate define its genuine disagreement probability

\[
 d_i(p_{-i})=\Pr_{p_{-i}}\bigl(G(0,X_{-i})\ne G(1,X_{-i})\bigr).
\tag{1.1}
\]

On the open cube the biased spectral occurrence mass satisfies the exact physical identity

\[
 \operatorname{It}_i(G;p)=V_{p_i}d_i(p_{-i}).
\tag{1.2}
\]

Hence the gate defect can be written without division by a vanishing variance:

\[
\boxed{
 D_\Gamma(G;p)=
 \sum_{i=1}^k d_i(p_{-i})A_\Gamma(p_i)
 -\Gamma(q_G(p))-\widetilde H_G(p),
}
\tag{1.3}
\]

where `q_G(p)=Pr_p(G=1)` and `Htilde_G` is the full biased spectral entropy. Formula (1.3) uses the original physical coordinates and one unchanged potential `Gamma`; it is not a reweighted face potential.

Assume throughout that `Gamma:[0,1]->R` is continuous, symmetric, finite, and endpoint normalized:

\[
\Gamma(0)=\Gamma(1)=0.
\tag{1.4}
\]

Then (1.3) defines the unique continuous extension of the interior gate defect to the closed bias cube.

## 2. Exact face contraction, including zero variance

For disjoint sets `Z,O` of coordinates, let `G_{Z,O}` be the gate obtained by fixing inputs in `Z` to zero and inputs in `O` to one. Let `F_{Z,O}` be the corresponding face of the bias cube.

### Theorem 2.1 — `FEI-B04-EXACT-FACE-CONTRACTION-v1`

For every `p in F_{Z,O}`,

\[
\boxed{
D_\Gamma(G;p)=D_\Gamma(G_{Z,O};p_{[k]\setminus(Z\cup O)}).
}
\tag{2.1}
\]

This includes the case in which the contracted gate is constant: both sides are exactly zero.

#### Proof

If `p_i` is zero or one, the product source fixes that input almost surely. The biased Fourier coefficient vector has zero coordinates on all spectral sets containing `i`; on sets avoiding `i` it is exactly the coefficient vector of the corresponding restriction. Thus the output probability and spectral entropy equal those of the restricted gate. For `j!=i`, the physical disagreement probability (1.1) becomes the disagreement probability of the restricted gate. The missing coordinate contributes

\[
d_i(p_{-i})A_\Gamma(p_i)=d_i(p_{-i})[\Gamma(p_i)+h_2(0)]=0
\]

by endpoint normalization. Iterating over all fixed coordinates proves (2.1). If the restriction is constant, its spectrum is a point mass at the empty set, every surviving disagreement probability is zero, and `Gamma(0)=Gamma(1)=0`; hence the defect is zero. `QED`.

This is the required zero-variance rule. No `0/0` convention is used.

## 3. Explicit all-bias continuity enclosure

Define the modulus of the common potential

\[
\omega_\Gamma(r)=\sup_{|x-y|\le r}|\Gamma(x)-\Gamma(y)|
\]

and set `M=||Gamma||_infinity+1`. For `0<=r<=1`, put

\[
\eta(r)=h_2(\min\{4r,1/2\}).
\tag{3.1}
\]

For two bias vectors `p,p'`, write

\[
\Delta=\sum_i|p_i-p'_i|,
\qquad
\Theta=\sum_i\left|\arcsin\sqrt{p_i}-\arcsin\sqrt{p'_i}\right|,
\qquad
\tau=\min\{1,2\Theta\}.
\tag{3.2}
\]

For a distribution on `N=2^k` atoms define

\[
F_k(\tau)=
\begin{cases}
h_2(\tau)+\tau\log_2(2^k-1),&0\le\tau\le1-2^{-k},\\
k,&1-2^{-k}<\tau\le1.
\end{cases}
\tag{3.3}
\]

### Theorem 3.1 — `FEI-B04-ALLBIAS-MODULUS-v1`

For every finite Boolean gate and every `p,p' in [0,1]^k`, including different boundary faces,

\[
\boxed{
\begin{aligned}
|D_\Gamma(G;p)-D_\Gamma(G;p')|
\le{}&M(k-1)\Delta
+\sum_{i=1}^k\bigl[\omega_\Gamma(|p_i-p'_i|)+\eta(|p_i-p'_i|)\bigr]\\
&+\omega_\Gamma(\min\{1,\Delta\})+F_k(\tau).
\end{aligned}}
\tag{3.4}
\]

#### Proof

Couple the two product sources coordinatewise. The disagreement event defining `d_i` depends only on coordinates other than `i`, so

\[
|d_i(p_{-i})-d_i(p'_{-i})|
\le\sum_{j\ne i}|p_j-p'_j|.
\tag{3.5}
\]

Also `0<=d_i<=1`, `|A_Gamma|<=M`, and binary entropy continuity plus `|V_x-V_y|<=4|x-y|` gives

\[
|A_\Gamma(x)-A_\Gamma(y)|
\le\omega_\Gamma(|x-y|)+\eta(|x-y|).
\tag{3.6}
\]

Summing (3.5)--(3.6) bounds the coordinate-price difference by the first line of (3.4). The same product coupling gives

\[
|q_G(p)-q_G(p')|\le\Delta,
\tag{3.7}
\]

which pays the output-potential term by `omega_Gamma(min{1,Delta})`.

It remains to control spectral entropy. Put `theta_i=arcsin sqrt(p_i)`. The square-root truth-table state changes in Euclidean norm by at most `sum_i|theta_i-theta'_i|`; the tensor biased-Fourier rotation changes by the same amount. Hence the two normalized Fourier coefficient vectors `a,a'` obey

\[
||a-a'||_2\le2\Theta.
\tag{3.8}
\]

For their squared-coordinate laws `w_S=a_S^2`, `w'_S=(a'_S)^2`, Cauchy--Schwarz gives total variation at most `||a-a'||_2`, hence at most `tau`. The sharp finite-alphabet entropy continuity inequality, obtained by applying the elementary `-x log_2 x` bound to the common and residual masses, gives

\[
|H(w)-H(w')|\le F_k(\tau).
\tag{3.9}
\]

Combining the bounds proves (3.4). `QED`.

There is no hidden singular constant in (3.4). The only dimension appearing is the gate arity `k`, through the entropy of its actual `2^k`-atom spectrum; no descendant dimension appears.

## 4. Dense exact certificates and finite quantitative certificates

### Theorem 4.1 — `FEI-B04-DENSE-TO-CLOSED-CUBE-v1`

Fix one gate `G` and one common potential satisfying (1.4). Let `Q` be any dense subset of the open cube, for example the rational bias vectors. If an exact source-valid certificate proves

\[
D_\Gamma(G;r)\ge0\qquad(r\in Q),
\tag{4.1}
\]

then

\[
\boxed{D_\Gamma(G;p)\ge0\qquad(p\in[0,1]^k).}
\tag{4.2}
\]

Every boundary value in (4.2) is the lower-arity defect in (2.1), including constant zero-variance faces.

#### Proof

For arbitrary `p` choose `r_n in Q` with `r_n->p`. The right side of (3.4) tends to zero because `Gamma` is uniformly continuous and `Delta,Theta->0`. Thus `D(r_n)->D(p)`, and (4.1) implies (4.2). Equation (2.1) identifies the boundary value. `QED`.

This is a continuum theorem, not a finite-grid inference.

### Quantitative finite enclosure

Let `N` be a finite set of exact interior or face nodes. Suppose every target point `p` is assigned a node `r(p)` for which the right side of (3.4), evaluated at `(p,r(p))`, is at most `E(p)`. If exact/interval arithmetic certifies

\[
D_\Gamma(G;r(p))\ge E(p),
\tag{4.3}
\]

then `D_Gamma(G;p)>=0`. In particular, if a cell has uniform bounds `Delta<=delta`, `Theta<=vartheta`, it is enough that the node margin exceed

\[
\boxed{
\Omega_{k,\Gamma}(\delta,\vartheta)
=M(k-1)\delta+k\omega_\Gamma(\delta)
+k\eta(\delta)+\omega_\Gamma(\delta)
+F_k(\min\{1,2\vartheta\}).
}
\tag{4.4}
\]

Here the use of `delta` in the coordinate moduli is a deliberately safe simplification from `|p_i-r_i|<=delta`. A finite grid without (4.3) or an equivalent interval enclosure proves nothing between its nodes.

For polynomial/rational `Gamma`, `omega_Gamma` can be replaced by an exact interval derivative bound. For the safe shape `eta_epsilon` in the source, this is an elementary polynomial bound and the same single shape is used on every face.

## 5. Symmetry and common-potential preservation

Input complementation sends `p_i` to `1-p_i` and restricts the same truth table with labels exchanged. Output complementation sends `q` to `1-q` and leaves the squared spectrum unchanged. Because `Gamma` and `h_2(V_p)` are symmetric, (1.3), (2.1), and (3.4) are invariant under these operations. Thus it is valid to certify one symmetry chamber and reflect it. Crucially, reflection and face contraction never alter `Gamma`, never replace an original coordinate price by a fitted face price, and never discard a child defect.

## 6. Exact tight-face boundary characterization using the assigned partner

The assigned partner fleet01/B04 proves the following source-exact expansion for a selector bias `t downarrow 0`. Let `G_0,G_1` be its two genuine Boolean restrictions, with lower-dimensional defects `D_0,D_1`, output biases `q_0,q_1`, disagreement probability `d`, and signed boundary entropy functional `E_0(u,v)=-8d-Lambda_0(u,v)` as defined in the partner report. If the needed one-sided derivatives of `Gamma` exist, then

\[
D_\Gamma(G;t)=D_0+tF_0+o(t),
\tag{6.1}
\]

where

\[
\boxed{
F_0=(D_1-D_0)+J_\Gamma(q_0,q_1)+d\gamma_0+E_0(u,v).
}
\tag{6.2}
\]

The logarithmic packet singularity has already canceled in (6.1); all child slack is retained.

Combining that result with Theorem 4.1 gives an exact boundary characterization for any claimed dense interior certificate:

* if `D_0<0`, face contraction already refutes the certificate;
* if `D_0=0` and `F_0<0`, (6.1) gives genuine negative interior biases for every sufficiently small positive `t`, so no dense nonnegative certificate can exist;
* therefore every valid dense interior certificate necessarily satisfies
  \[
  \boxed{D_0\ge0,\qquad D_0=0\Longrightarrow F_0\ge0.}
  \tag{6.3}
  \]
* `D_0>0` gives a collar by Theorem 3.1; `D_0=0,F_0>0` gives a sharper linear collar from (6.1); only `D_0=F_0=0` needs second-order analysis.

The opposite endpoint is obtained by swapping the two restrictions and using the partner's `F_1`. Thus (2.1) and (6.3) are the requested exact boundary rules, while (3.4) is the quantitative enclosure connecting them to certified interior cells.

For a constant limiting child, the partner's slope-free specialization becomes

\[
F_0=D_\Gamma(G_1)+\Gamma(d)+E_{\rm const}(d),
\tag{6.4}
\]

with

\[
E_{\rm const}(d)=-8d+4d^2\log_2(4d^2)-(1-2d)^2\log_2((1-2d)^2).
\tag{6.5}
\]

Therefore every valid dense all-bias certificate must satisfy the explicit source-valid inequality

\[
\boxed{D_\Gamma(G_1)+\Gamma(d)+E_{\rm const}(d)\ge0}
\tag{6.6}
\]

for every constant/nonconstant tight boundary pair. This is an actual application of the partner theorem, not a citation-only dependency.

## 7. Consequence and remaining burden

The theorem removes a logical gap in any future exact interior gate certificate: once a single common continuous endpoint-normalized potential has been certified on a dense interior set, no separate informal appeal to boundary continuity is needed. Equations (2.1), (3.4), and (6.3) transfer it rigorously to every bias, including zero-variance gates and entropy-support changes.

What remains unpaid is much larger: no source currently certifies one potential on the dense interior for every Boolean gate and every arity. The current shaped direction is universally safe only as an added direction; the repaired base potential remains unproved. Hence full FEI remains open.

The next recipient `fleet02/B01` should use (3.4) as the enclosure rule for any exact interior Bellman/gate certificate and impose (6.3)--(6.6) as mandatory tight-face conditions. A finite sweep without these bounds is not promoted.

## 8. Verification boundary

The accompanying standard-library checker verifies on exhaustive gates through arity three and rational boundary samples: the physical cancellation `It_i=V_i d_i`, exact face contraction, zero-variance constants, and the numerical validity of the conservative modulus (3.4). These checks are regression evidence only; the displayed proofs establish the theorem.

No full FEI proof, independent end-to-end review, native-brain ingestion, scheduler mutation, email, notification change, public release, paid call, or permission expansion is claimed.
