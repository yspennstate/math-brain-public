# account04/B13 — arbitrary-bias antipodal defects are repelled on every fixed rare-corner ray

**Outcome:** `ESSENTIAL_STEP_APPLIED` to the current all-gate adversarial programme. Full uniform-cube FEI remains **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Exact candidate and newest peer input

The active owner target is the all-gate inequality
\[
D_\Gamma(G;p):=\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
  \bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
 -\Gamma(p_{\rm out})-\widetilde H_G(p)\ge0,
\qquad V_u=4u(1-u).
\tag{G}
\]
A finite symmetric nonnegative potential satisfying `(G)` for every Boolean gate/product bias would imply full FEI.

The newest compatible other-account result consumed here is **account03/B17**, `20260922T0304Z-biased-eq-boundary/REPORT.md`, blob `1da6fe7259cf4a560dd703f42947bd90060e73bd`. It proved exact equal-bias formulas for the antipodal sparse core
\[
\operatorname{EQ}_d=1_{\{0^d,1^d\}},
\]
and proved that for a potential with positive small-bias linear-log coefficient, the **equal-bias** extreme boundary is safe. Its explicit remaining issue was genuinely nonuniform bias. The present result changes that argument by removing every fixed-ratio nonuniform approach to the rare corner, not only the diagonal `p_1=\cdots=p_d`.

The stable candidate in that peer report is `LIMIT-PRIME-GATE-LIFT-v1`,
\[
\Gamma_*(p)=\Gamma_{\rm RO}(p)+a_*p(1-p),
\qquad a_*=0.2682048,
\]
with centre constant about `6.5218512`. The quadratic lift changes only the linear term of the small-bias expansion, not its `p log(1/p)` coefficient.

## 1. Exact arbitrary-bias spectrum

Let `d>=3`. Put independent input biases
\[
p_i\in(0,1),\qquad q_i=1-p_i,
\]
and use the sign convention `f=-1` on `0^d,1^d` and `f=+1` elsewhere. Define
\[
P=\prod_i p_i,\qquad Q=\prod_i q_i,\qquad r=P+Q.
\]
For the normalized biased basis
\[
\varphi_i(1)=\sqrt{q_i/p_i},\qquad
\varphi_i(0)=-\sqrt{p_i/q_i},
\]
the empty coefficient is
\[
\widehat f(\emptyset)=1-2r.
\tag{1.1}
\]
For every nonempty `S`, the constant part contributes zero and only the two exceptional corners remain, so
\[
\boxed{
\widehat f(S)=-2\left[
P\prod_{i\in S}\sqrt{q_i/p_i}
+(-1)^{|S|}Q\prod_{i\in S}\sqrt{p_i/q_i}
\right].
}
\tag{1.2}
\]
Hence `\widetilde H_EQ(p_1,...,p_d)` is explicit from the `2^d` squared masses in (1.1)-(1.2); no product-symmetric bias assumption is needed.

Coordinate `i` changes the output exactly when the remaining `d-1` bits are all zero or all one. Therefore
\[
\boxed{
{\operatorname{It}_i\over V_{p_i}}
=P_{-i}+Q_{-i},
\qquad
P_{-i}:=\prod_{j\ne i}p_j,
\quad Q_{-i}:=\prod_{j\ne i}q_j.
}
\tag{1.3}
\]
Substitution into `(G)` gives the exact arbitrary-bias reduction
\[
\boxed{
D^{\rm EQ_d}_\Gamma(p_1,\ldots,p_d)
=
\sum_i(P_{-i}+Q_{-i})
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\widetilde H_{\rm EQ_d}(p)-\Gamma(r).
}
\tag{1.4}
\]
The Poincare currency also has a closed form. Since
\[
p_iq_iP_{-i}=Pq_i,
\qquad p_iq_iQ_{-i}=Qp_i,
\]
we obtain
\[
\boxed{
W(p):={I\over4}-r(1-r)
=P\sum_iq_i+Q\sum_i p_i-r(1-r).
}
\tag{1.5}
\]
Equations (1.2), (1.4), and (1.5) are the nonuniform analogue of the scalar equal-bias reduction in account03/B17.

## 2. Fixed-ray rare-corner theorem

Assume the symmetric potential has
\[
\Gamma(s)=A\,s\log_2(1/s)+Bs+o(s)
\qquad(s\downarrow0),
\tag{2.1}
\]
with `A>0`. Fix a probability vector
\[
w=(w_1,\ldots,w_d),\qquad w_i>0,\quad \sum_iw_i=1,
\]
and approach the rare corner along
\[
p_i=t w_i,\qquad t\downarrow0.
\tag{2.2}
\]
Write
\[
H(w)=-\sum_i w_i\log_2 w_i,
\qquad
S_2(w)=\sum_{i<j}w_iw_j={1-\sum_iw_i^2\over2}.
\]

### Theorem 2.1 — arbitrary fixed-ratio boundary repulsion

For every fixed `d>=3` and every interior ray `w`,
\[
\boxed{
D^{\rm EQ_d}_\Gamma(tw)
=A\,t H(w)+o(t)>0
}
\tag{2.3}
\]
for all sufficiently small `t`, while
\[
\boxed{
W(tw)=S_2(w)t^2+O(t^3).
}
\tag{2.4}
\]
Consequently the required quadratic margin
\[
c^{\rm EQ_d}_\Gamma=-D/W
\]
satisfies
\[
\boxed{
 t\,c^{\rm EQ_d}_\Gamma(tw)
\longrightarrow
-{2A H(w)\over1-\sum_iw_i^2}<0.
}
\tag{2.5}
\]
In particular `c(tw)->-infinity`: this family has growing favorable slack in normalized-margin units at every fixed nonuniform rare-corner direction.

### Proof

From (1.1)-(1.2), the empty spectral mass is
\[
1-4t+O(t^2),
\]
each singleton spectral mass is
\[
4tw_i+O(t^2),
\]
and the total contribution of levels at least two is `O(t^2)`. Therefore
\[
\widetilde H_{\rm EQ_d}(tw)
=\sum_i h_2(4tw_i(1-tw_i))+O(t^2\log(1/t)).
\tag{2.6}
\]
Also `P_{-i}+Q_{-i}=1+O(t)`, so multiplying the binary-entropy terms by these coefficients changes their sum only by `O(t^2 log(1/t))`. Thus the entire entropy part of (1.4) cancels to first order.

For the potential part, `r=P+Q=1-t+O(t^2)` and symmetry gives `Gamma(r)=Gamma(1-r)`. Using (2.1),
\[
\begin{aligned}
\sum_i\Gamma(tw_i)-\Gamma(t+O(t^2))
&=At\left(\sum_iw_i\log_2{1\over w_i}\right)+o(t)\\
&=AtH(w)+o(t).
\end{aligned}
\tag{2.7}
\]
The factors `P_{-i}+Q_{-i}=1+O(t)` change this by only lower order. This proves (2.3).

For (2.4), `P=O(t^d)`,
\[
Q=1-t+S_2(w)t^2+O(t^3),
\]
and (1.5) gives
\[
P\sum q_i+Q\sum p_i=t-t^2+O(t^3),
\]
whereas
\[
r(1-r)=t-(1+S_2(w))t^2+O(t^3).
\]
Subtracting yields `W=S_2t^2+O(t^3)`. Equation (2.5) follows. `QED`.

## 3. A dimension-free leading repulsion coefficient

The elementary inequality `-ln x >= 1-x` implies
\[
H(w)\ge {1-\sum_iw_i^2\over\ln2}.
\tag{3.1}
\]
Hence every fixed interior ray in Theorem 2.1 obeys
\[
\boxed{
\limsup_{t\downarrow0}t\,c^{\rm EQ_d}_\Gamma(tw)
\le -{2A\over\ln2}.
}
\tag{3.2}
\]
The coefficient is independent of arity and of the ray. This does **not** assert a single uniform cutoff over rays whose direction itself degenerates with `t`; it is a leading-coefficient statement for each fixed ray.

The complement corner `p_i->1` is identical by symmetry.

## 4. Application to the read-once tail used by the live lifted candidate

The source read-once fixed-point report gives the normalized AND identity
\[
\Phi(p,q)=G(p)+G(q)-G(pq)-E(p,q),
\qquad G(p)=\Gamma_{\rm RO}(p)/p,
\tag{4.1}
\]
with `E(p,1/2)->8` as `p->0`, and identifies the fresh-variable line `q=1/2` as tight for the fixed-point tail. If
\[
G(p)=A\log_2(1/p)+B+o(1),
\]
then tightness in (4.1) at `q=1/2`, together with `G(1/2)=2C_0`, gives
\[
0=2C_0-A-8,
\qquad
\boxed{A=2(C_0-4).}
\tag{4.2}
\]
At the source centre `C_0=6.4548`,
\[
A=4.9096>0.
\tag{4.3}
\]
Adding the live quadratic lift `a_*p(1-p)` does not change `A`. Therefore the arbitrary-bias boundary theorem applies to `LIMIT-PRIME-GATE-LIFT-v1` on every fixed rare-corner ray. Its dimension-free leading repulsion in (3.2) is
\[
-{2A\over\ln2}<-14.1661.
\tag{4.4}
\]
For the uniform `d=3` ray, (2.5) reduces to the peer formula
\[
p\,c(p)\to-{2A\log_2 3\over2}
=-A\log_2 3\approx-7.78153189354,
\]
while in the scale `t=3p`,
\[
t\,c(tw)\to-23.3445956806.
\]
Thus the peer's equal-bias theorem is recovered as one ray of the multivariate result.

## 5. Exact change to the remaining adversarial search

Before this run, account03/B17 had excluded the equal-bias extreme boundary but explicitly left genuinely nonuniform bias open. Theorem 2.1 now proves:

> A composition-prime `EQ_d` falsifier of the live lifted potential cannot be produced by sending all common corner probabilities to zero (or one) at any fixed unequal ratio.

Therefore the `EQ_d` adversarial search can be localized to:

1. a compact interior bias region; and
2. singular hierarchical boundary regimes in which the bias **ratios themselves degenerate** (one or more coordinates vanish parametrically faster than the total rare mass).

The latter is a narrower mechanism: the gate approaches a lower-dimensional/character-like boundary, and any claimed counterexample there must retain the next-scale terms rather than treating it as the generic rare corner. This is exactly the kind of boundary that should next be compared with the proved gate-composition/decomposable cocycle.

This result does not certify `D>=0` on the compact interior and therefore does not prove the live potential universal. It does not prove FEI.

## 6. Verification

A separate standard-library checker evaluates (1.1)-(1.5) against a direct biased Walsh transform for deterministic unequal-bias cases in dimensions `3,4,5,6`, then checks the asymptotic coefficients on five nonuniform rays for a synthetic potential with the source coefficient `A=4.9096`. It returned `PASS`.

Executed checker SHA-256: `b71f2bdee9168742c29caeff2a5be607bb65008cae953f139f4f8ba6b45532c0`.  
Captured output SHA-256: `d5b896d4a43439f0271601f840b3aa2f93251fa72624226c4bb1ef53a06e1586`.

The computation is only a falsification check of the analytic derivation; the theorem is the algebra/asymptotic proof above.

## 7. Scope preservation

Full uniform-cube FEI remains **OPEN / NOT PROVED**. Account04/B18's earlier mixed-curvature conservation
\[
\kappa_{ik}=\kappa_{ki}=p_{ik}+4o_{ik},
\qquad
\sum_{i\ne k}(p_{ik}+4o_{ik})=4d_k,
\]
and its exact zero-defect classification are neither weakened nor reused as an unsupported shortcut here. They remain valid at their stated source scope; the later owner instruction merely changes the active proof route to the all-gate target.

Manual scoped privacy/provenance review: mathematical formulas and repository-relative source identifiers only; no credentials, machine paths, benchmark gold, unrelated private data, email/Drive action, paid/remote compute, workflow dispatch, permission changes, or notification changes. No novelty or publication-priority claim is made.
