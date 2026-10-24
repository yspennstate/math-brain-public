# B19 independent proof-chain review: B12 uniform coherent-kernel envelope

## Verdict

**Primary packet:** A094 (Proof-chain challenger).  
**Reviewed packet/claim:** B12 / A057, `B12-A057-UNIFORM-COHERENT-KERNEL-ENVELOPE-v1`.  
**Stable gap:** `WEIGHTED_LOCAL_TC`, changing-coherent-witness sub-obligation.  
**Prior status:** `AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW`.  
**New status:** `INDEPENDENTLY_ACCEPTED_AT_DECLARED_SCOPE` for the scalar kernel, exact one-node identity, and fixed-source adaptive hierarchy only.  
**Full FEI:** **OPEN**.

I independently reconstructed the proof and the finite calculation.  The B12 theorem is correct with its stated fixed-source quantifier.  It is a useful all-depth theorem, not a full closure theorem: when the outer coherent pair changes from node to node, its source cost becomes

\[
  \sum_v w_v\alpha_v^2 M(a_v,b_v),
\]

and B12 supplies no dimension-independent single-use bound for this quantity.  This is the first unsupported universal step.  In particular, one may not replace it by `sup_v M(a_v,b_v)` without separately proving that supremum is universal, and one may not charge `M(a_v,b_v)` afresh at every node.

## Source pins and exact scope reviewed

The original reviewed bundle is the B12 run

`reports/fei-2026-10-11/runs/B12/20261012T032618Z-account01-B12-uniform-kernel-envelope/`

at canonical commit `80054872e190524ffdea413d8f96e07919c35c62`.  I read its `REPORT.md`, `CLAIMS.json`, `UNIFORM_KERNEL_PAYMENT.tex`, `ALPHA_LOG_CONTROLS.md`, `HANDOFF.md`, checker, and output.  I also read the predecessor identity package

`reports/fei-2026-10-11/runs/B12/20261012T022322Z-account01-B12-biased-coherent-hierarchy/`

at commit `4fa89c32748c17c91aeca56c55c7a054b760ba6e`, including `BIASED_COHERENT_IDENTITY.tex`, `ADAPTIVE_LOG_PAYMENT.tex`, and `REPORT.md`.

The B12 theorem uses natural logarithms.  Conversion to the campaign's base-2 entropy divides every entropy payment by `ln 2`; this changes constants only and creates no dependence on dimension, depth, or bias.

## Frozen statement

Let

\[
 \psi(x)=x^2\ln(1/x^2),\qquad
 K(x,y)=\psi(x)+\psi(y)-\frac{\psi(x+y)+\psi(x-y)}2,
\]

with `psi(0)=0`.  Let `g_+,g_-:{-1,1}^m->{-1,1}` be fixed, put

\[
 a=(g_++g_-)/2,\qquad b=(g_+-g_-)/2,
\]

and write their Walsh coefficients as `a_T,b_T`.  Let

\[
 q=\sum_T b_T^2,
 \qquad
 M(a,b)=2\sum_{T:b_T\ne0}b_T^2\ln_+\frac{|a_T|}{|b_T|}.
\]

For an arbitrary Boolean child `h:{-1,1}^n->{-1,1}`, a node whose current restriction is `h_v`, and a fresh queried physical coordinate `i`, set

\[
 \mu_v=\widehat h_v(\varnothing),\qquad
 \alpha_v=\widehat h_v(\{i\}).
\]

The reviewed theorem asserts:

1. The exact remainder after subtracting `q` times the child's split decrement is

   \[
   R_{\mu}(\alpha)=
   \sum_{T:b_T\ne0}b_T^2
   \left[K\!\left(\frac{a_T}{b_T}+\mu,\alpha\right)-K(\mu,\alpha)\right].
   \]

2. At one node,

   \[
   R_\mu(\alpha)
   \le q\psi(\alpha)+(4+2\ln2)q\alpha^2+M(a,b)\alpha^2.
   \tag{1}
   \]

3. For every finite adaptive restriction tree on the physical inputs of `h`, with no coordinate repeated on a root-leaf path and with the same outer pair `(a,b)` at every node,

   \[
   \sum_vw_v R_{\mu_v}(\alpha_v)
   \le
   \left[M(a,b)+\left(4+2\ln2+\frac2e\right)q\right]I(h).
   \tag{2}
   \]

This has no restriction on the depth, bias `mu_v`, stopping rule, branch-dependent coordinate choice, or Boolean terminal cores.  Its essential hypothesis is that the same outer source `(a,b)` is used throughout.

## Independent analytic reconstruction

### 1. Scalar kernel

Homogeneity is exact:

\[
 K(\lambda x,\lambda y)=\lambda^2K(x,y).
\]

The terms proportional to `lambda^2 ln(1/lambda^2)` cancel because

\[
x^2+y^2=\frac{(x+y)^2+(x-y)^2}{2}.
\]

Let `G(t)=t^2 ln t` for `t>=0`, with `G(0)=0`, and

\[
 k(r)=K(r,1)=G(r+1)+G(|r-1|)-2G(r),\qquad r\ge0.
\]

The function is even before restricting to `r>=0`.  It is nonnegative and nondecreasing.  For `0<r<1`, writing `k'(r)=2u(r)` gives

\[
 u(r)=(1+r)\ln(1+r)-(1-r)\ln(1-r)-2r\ln r,
\]
\[
 u'(r)=\ln\frac{1-r^2}{r^2}.
\]

Thus `u` increases and then decreases, with `u(0+)=0` and `u(1-)=2 ln 2`, so `u>=0`.  For `r>1`, `k'(r)` is the centered second difference of `G'`; since `G'''(r)=2/r>0`, `G'` is convex and `k'(r)>=0`.

The triangular second-difference representation, with `T` having density `1-|t|` on `[-1,1]`, is

\[
 k(r)=3+2\mathbb E\ln|r+T|.
\]

Jensen and `E|r+T|<=r+1` give

\[
 k(r)\le 2\ln(1+r)+3.
\]

For the lower bound, monotonicity suffices on `0<=r<=1/2` because `2 ln(1+r)-1<0`, and on `1/2<=r<=1` because `k(r)>=k(1/2)>2 ln2-1`.  For `r>=1`, convexity of `x -> 1/x` in the derivative representation gives `k'(r)>=2/r>2/(r+1)`; the inequality at `r=1` then propagates.  Consequently

\[
 2\ln(1+|r|)-1\le k(r)\le2\ln(1+|r|)+3.
\]

Combining the two sides and using

\[
 \frac{1+|r|}{1+|s|}\le1+|r-s|
\]

yields the uniform difference estimate

\[
 k(r)-k(s)\le4+2\ln(1+|r-s|).
\tag{3}
\]

This proof includes `r=0`, `r=1`, `s=0`, and collision limits by continuity.

### 2. Exact Fourier remainder

Write a current child as

\[
h_v=\mu+\alpha x_i+\sum_{R\ne\varnothing,\ i\notin R}
\left(\widehat h_v(R)+x_i\widehat h_v(R\cup\{i\})\right)\chi_R.
\]

For `F=a+h_v b`, the Fourier pair at outer frequency `T` and child frequency `R=empty` is

\[
 (a_T+\mu b_T,\alpha b_T),
\]

while every `R nonempty` pair is `b_T` times the corresponding pair of `h_v`.  The split decrement is the sum of `K` over these pairs.  Homogeneity cancels every nonconstant child-frequency term against `q` times the child decrement, leaving exactly the displayed formula for `R_mu(alpha)`.  This also proves the endpoint cases `b_T=0`, `alpha=0`, and `q=0` without division.

### 3. One-node envelope

For `beta=|alpha|>0`, set

\[
 r_T=\frac{a_T/b_T+\mu}{\beta},\qquad s=\frac\mu\beta.
\]

Homogeneity and (3) give

\[
 b_T^2\bigl[K(a_T/b_T+\mu,\alpha)-K(\mu,\alpha)\bigr]
 \le b_T^2\beta^2
 \left(4+2\ln\left(1+\frac{|a_T|}{\beta|b_T|}\right)\right).
\]

Using

\[
\ln(1+u)\le\ln2+\ln_+u,
\qquad
\ln_+\frac{|a_T|}{\beta|b_T|}
\le\ln_+\frac{|a_T|}{|b_T|}+\ln\frac1\beta,
\]

and summing gives (1).  If `beta=0`, both sides are zero by `K(x,0)=0`.

The source term is always finite for Boolean branches.  Indeed `|a_T|<=1`, hence

\[
 M(a,b)\le\sum_T b_T^2\ln(1/b_T^2),
\]

with the zero terms omitted.  This comparison is useful but does not make `M/q` universally bounded.

### 4. Physical-input ledger and hierarchy

At a Boolean node,

\[
 |\alpha_v|=|\mathbb E D_i h_v|\le\mathbb E|D_i h_v|
 =\operatorname{Inf}_i(h_v).
\]

For `0<=u<=1`,

\[
 u^2\ln(1/u^2)\le(2/e)u,
 \qquad u^2\le u.
\]

For a fixed physical coordinate `i`, the nodes at which `i` is queried are incomparable because the tree does not reuse a coordinate on a path.  Their reach cylinders are disjoint and do not themselves fix `i`.  Therefore

\[
 \sum_{v:\,i(v)=i}w_v\operatorname{Inf}_i(h_v)
 \le\operatorname{Inf}_i(h).
\]

Summing over physical coordinates proves

\[
 \sum_vw_v\psi(\alpha_v)\le(2/e)I(h),
 \qquad
 \sum_vw_v\alpha_v^2\le I(h).
\]

Applying these two inequalities to (1) proves (2).  This is genuine all-depth physical-input accounting; no independent entropy payment is charged once per node.

## Independent finite reconstruction

`INDEPENDENT_AUDIT.py` was written independently of the B12 checker.  It:

- reconstructs `F=a+h b` from truth tables and computes the split decrement from a fresh Walsh transform;
- exhausts all 256 ordered pairs of two-bit Boolean outer branches and every Boolean child through three bits, for 205,824 coordinate-split cases;
- independently maximizes the signed B12 charge over **all** adaptive, branch-dependent, nonreusing restriction trees for those roots (70,656 root instances), including optional stopping;
- separately maximizes the `psi(alpha)` and `alpha^2` ledgers; and
- tests the scalar estimates on a deterministic logarithmic/collision grid of 329 points and 108,241 ordered pairs.

Command:

`python3 INDEPENDENT_AUDIT.py`

Result: **PASS**.  The maximum absolute error between the direct truth-table decrement and the closed kernel was `4.441e-16`; no envelope or hierarchy violation occurred.  This is corroboration, not the all-dimensional proof; the proof is the analytic argument above.

## Primary-literature scope comparison

I checked the original O'Donnell--Tan composition theorem (`arXiv:1304.1347`).  Its hypothesis is disjoint child blocks plus an FEI+ bound for the outer gate under the product distribution induced by the child expectations.  It proves read-once bounded-arity closure.  It does not state or imply the missing bound for a restriction hierarchy whose coherent outer witness changes by node.

I also checked Wan--Wright--Wu (`arXiv:1312.3003`).  Their communication argument gives `9k` for read-`k` decision trees and re-proves FEI+ composition.  It supports the importance of physical read accounting, but its constant grows with `k` and it does not supply the B12 source functional or the changing-witness single-use estimate.

Potapov (`arXiv:2609.21563`) proves FEI with sharp constants for plateaued and partially bent classes and gives biased estimates.  Those proper spectral classes do not close an arbitrary coherent hierarchy and do not bound the varying `M(a_v,b_v)` ledger.

Accordingly, this review makes no novelty claim for the scalar calculus.  It certifies the internal theorem and locates its exact boundary relative to known composition and class results.

## Stress-test ledger

- **Addressing/multiplexers:** not covered by (2) when the selected outer witness changes with the address.  The unpaid varying-source sum remains explicit.
- **Rare restrictions / sparse defects:** the `q psi(alpha)` term retains the logarithm and is amortized through physical pivotal events.  No pointwise `O(alpha^2)` replacement is used.
- **Near tensors:** exact disjoint Fourier factorization is used only for the fixed splice; shared-variable interference is outside scope.
- **Prime Boolean gates:** permitted as fixed outer branches, but the theorem is conditional on their finite `M(a,b)` and does not make `M/q` universal.
- **Endpoints:** `alpha=0`, `b_T=0`, `q=0`, `r=0`, and `r=1` are handled explicitly.

## Mathematical delta and next obligation

**PROVED and independently accepted:** For every fixed Boolean outer pair, every Boolean child, and every adaptive nonreusing physical restriction tree of arbitrary depth, the entire signed coherent remainder obeys (2), with a constant independent of depth and node bias.

**OPEN:** Prove a dimension-independent single-use inequality for

\[
 \sum_vw_v\alpha_v^2M(a_v,b_v)
\]

when `(a_v,b_v)` changes coherently through the hierarchy, or construct a genuine Boolean hierarchy showing that no such inequality can hold under the proposed credit.  The next attempt should freeze the exact coherence law relating parent and child witnesses before searching; without that law, arbitrary independent choices of `(a_v,b_v)` trivially permit repeated source charging and are not a meaningful FEI model.

## Configuration and delivery

- Model exposed by this run: Codex; exact runtime version not exposed.
- Reasoning-effort selector: not exposed.
- Subagents: none.
- Random seed: none.
- Scheduler, graph, merge, deployment, email, and public-release actions: none.
- Native Brain ingestion: not claimed; only the authorized immutable handoff mirror is requested.

