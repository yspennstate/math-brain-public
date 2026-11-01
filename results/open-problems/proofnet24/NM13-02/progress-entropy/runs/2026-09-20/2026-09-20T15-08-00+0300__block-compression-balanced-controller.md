Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.** No authenticated GPT-6 / maximum-effort metadata is exposed in this runtime.

# NM13-02 T01 — physical block allocation compression and a signed-rigid connected-core application

## 0. Parent scope/bound versus mechanism gain

**Parent problem.** Friedgut–Kalai Fourier entropy–influence (FEI): prove a finite universal constant `C` such that

\[
H(\widehat f^{\,2})\le C I(f)
\]

for every Boolean function on every finite uniform cube.

**Parent status before -> after:** **OPEN -> OPEN**.

**Universal finite constant before -> after:** **UNKNOWN -> UNKNOWN**.

No finite-dimensional computation, fresh-control theorem, or restricted stopping class below is promoted to full FEI.

**Mechanism gain in this run.** P03's newest substantive report proves, as a peer result pending later independent review, that dependent-branch recombination is pointwise dominated by hereditary allocation, and therefore sharpens the live obstruction to a single ledger:

\[
\text{find a universal }K<\infty\text{ so every Boolean }f
\text{ has a full physical tree }\mathcal T\text{ with }R_\mathcal T\le K I(f).
\]

This run proves a universal block theorem directly on that ledger. If a physical block `A` is completely queried before any coordinate outside `A`, in **any adaptive order**, then the entire accumulated hereditary allocation in that prefix is bounded by the one-shot spectral conditional entropy

\[
\boxed{R_{\mathcal T_A}(f)\le H(S_A\mid S_{A^c}).}
\tag{0.1}
\]

Here `S` is the random Fourier subset with law `Pr[S=T]=\widehat f(T)^2`. The queried physical influence of the same complete block is exactly

\[
\boxed{Q_{\mathcal T_A}=\sum_{i\in A}\operatorname{Inf}_i(f).}
\tag{0.2}
\]

Thus any useful block selector `H(S_A|S_Ac)<=K I_A(f)` is physically realizable with **no additional hereditary depth/recombination surcharge**. This strengthens the older P03 block-restriction framework specifically at the hereditary-allocation level: its one-shot conditional term is not merely an entropy-decrement surrogate; it upper-bounds the actual sequential allocation paid while realizing the whole block.

The theorem is then applied to an explicit all-dimensional family of signed-translation-rigid, single-connected, unbounded-degree ANF cores. A large dependent controller block can be removed in one allocation budget, and after grafting the inherited one-point-defect certificate the full physical tree satisfies

\[
\boxed{R_{\mathcal T}(F_{d,m})<4I(F_{d,m})\qquad(d,m\ge1).}
\tag{0.3}
\]

The phase degree is `2^d+m`, so the certificate is independent of degree and controller depth on this family. This is a demonstrated mechanism gain on P03's exact remaining signed-rigid connected-core geometry, not an unrestricted FEI proof.

---

## 1. Current dependencies and compact handoff

Controlling policy: `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`. LIVE20 assigns NM13-02 to T01 hereditary entropy/recombination theory paired with P03.

Essential current project dependencies consumed:

1. Newest P03 substantive report `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T14-29-48+0300__fei-recombination-dominated-by-allocation.md`, blob `b8eae04b83f3518bdb9dc87e33734e616f2988e0`. It reports the universal local theorem `J_i^rec<=B_i`, hence `S_T<=R_T`, and identifies the exact remaining full-scope obstruction as the universal full-tree allocation bound `R_T<=K I`. That theorem is a peer claim; the new block-compression proof below does not assume it.
2. P03's earlier `proofnet24/P03-fei/solo-2026-09-17/BLOCK_RESTRICTION_IDENTITY_2026-09-18.md`, blob `5a6790b95c7d44c85fa5507623f3129e1c48ede9`. For a physical block `A` with complement `C`, it proves
   \[
   H(f)-\mathbb E_xH(f_x)=H(S_A\mid S_C)+I(X;D),
   \]
   with the channel payment `I(X;D)<=(2/ln2)I_A(f)`, and leaves a useful proper-block selector unpaid. The present theorem addresses the distinct question of how much **hereditary allocation** is paid by physically realizing such a block.
3. Latest preceding NM13-02 report `proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20__endpoint-character-child-cross-fibre.md`, preserving the exact character-child endpoint payment and the existing one-point perturbation hereditary constant
   \[
   C_\chi=2+\frac1{\sqrt e\ln2}=2.875038774914527\ldots .
   \]

Compact prior NM13-02 mathematics preserved: exact quadratic rank telescopes and quadratic hereditary constant one; exact queried-influence/max-splicing budgets; one-point perturbations of arbitrary quadratic phases with constant `C_chi`; character-child allocation; oblique-derivative approximate quotient peeling; variance-paid separators; quadratic-normalized Wiener control; two-affine-flat control; guarded derivative selectors; and cross-fibre endpoint rescue. Fresh-control results remain restricted because they append variables and do not imply fixed-domain FEI. The false pointwise erasure shortcut, fixed-coefficient affine drift, Han absolute-overlap selector, derivative-degree scalar schedule, blind root-curvature payment, fixed-`s<2` Renyi payment, root marginal-entropy replacement, and arbitrary-orthogonal-involution relaxation remain retired.

### Primary-source status checked 20 September 2026

A bounded fresh source check still finds González–MacManus–Pereyra, arXiv:2606.00246 (submitted 29 May 2026), explicitly stating universal FEI as a conjecture and explaining that their restriction inequality would prove it if universal. Li–Han, arXiv:2512.03117 (submitted 2 December 2025), sharpens Han's general inequality but retains the coordinate-profile correction `sum_i I_i log(1/I_i)`. No source-matching universal FEI proof was recovered. Publication priority for the theorem below is **UNVERIFIED**.

---

## 2. Definitions

Let `f:{-1,1}^n->{-1,1}` and let `S` denote its spectral random set:

\[
\Pr(S=T)=\widehat f(T)^2.
\]

For one physical coordinate `i`, write

\[
B_i(f):=H(S_i\mid S_{[n]\setminus\{i\}}).
\]

For a nonempty block `A subset [n]`, write `C=A^c` and define

\[
B_A(f):=H(S_A\mid S_C).
\tag{2.1}
\]

A **complete physical `A`-prefix** is an adaptive physical restriction tree which, on every branch, queries each coordinate of `A` exactly once, queries no coordinate of `C`, and stops immediately after all of `A` is fixed. The order may depend arbitrarily on the values observed earlier on that branch. Its hereditary allocation is

\[
R_{\mathcal T_A}(f)
:=\sum_{v\in\mathcal T_A^{\rm int}}w_v B_{i(v)}(f_v),
\tag{2.2}
\]

where `w_v` is the physical cylinder probability of reaching node `v`.

---

## 3. Universal block allocation compression

### Theorem 3.1
For every Boolean `f`, every nonempty physical block `A`, and every complete adaptive physical `A`-prefix,

\[
\boxed{R_{\mathcal T_A}(f)\le B_A(f)=H(S_A\mid S_{A^c}).}
\tag{3.1}
\]

The theorem has no fresh variables, symmetry, degree, sparsity, or branch-independence hypothesis.

### Proof
Induct on `|A|`. The case `|A|=1` is equality by definition.

Assume `|A|>=2`. Let the root query coordinate `i in A`, put `A'=A\setminus\{i\}`, and let the two Boolean children be `g=f^{i=0}` and `h=f^{i=1}`. The two descendant trees are complete adaptive `A'`-prefixes, so by induction their average allocation is at most

\[
\frac12 B_{A'}(g)+\frac12 B_{A'}(h).
\tag{3.2}
\]

We now identify the relevant mixture law exactly. For each residual Fourier label `T subset [n]\setminus\{i\}`, write

\[
u_T=\widehat f(T),\qquad v_T=\widehat f(T\cup\{i\}).
\]

Up to the harmless convention for the two physical signs, the child Fourier coefficients are

\[
\widehat g(T)=u_T+v_T,
\qquad
\widehat h(T)=u_T-v_T.
\]

Therefore

\[
\frac12\widehat g(T)^2+\frac12\widehat h(T)^2
=u_T^2+v_T^2.
\tag{3.3}
\]

The right side is exactly the parent spectral law after forgetting the bit `S_i`. Hence the equal mixture of the two child spectral laws on `(S_{A'},S_C)` is the parent marginal law of `(S_{A'},S_C)`.

Conditional Shannon entropy is concave as a function of the joint law. Applying concavity to that mixture gives

\[
\frac12H_g(S_{A'}\mid S_C)
+\frac12H_h(S_{A'}\mid S_C)
\le H_f(S_{A'}\mid S_C).
\tag{3.4}
\]

The root itself costs

\[
B_i(f)=H_f(S_i\mid S_{A'},S_C).
\tag{3.5}
\]

Combining the root cost, (3.2), and (3.4), then using the conditional entropy chain rule,

\[
\begin{aligned}
R_{\mathcal T_A}(f)
&\le H_f(S_i\mid S_{A'},S_C)+H_f(S_{A'}\mid S_C)\\
&=H_f(S_A\mid S_C)=B_A(f).
\end{aligned}
\]

This closes the induction. QED.

### Remarks

1. The inequality can be strict: physical restriction reveals branch information, and the child spectra can become easier than the unconditional spectral block.
2. The theorem is genuinely adaptive. After the root, the next queried coordinate may be chosen differently in the two children; induction is applied separately to those two adaptive subtrees.
3. Taking `A=[n]` gives only `R_T<=H(f)`, so allowing the whole cube does **not** solve FEI. The mathematical content needed for universal closure is still a useful influence-paid proper block or another summable stopping mechanism.

---

## 4. Exact influence payment for the same adaptive block

### Lemma 4.1
For every complete adaptive physical `A`-prefix,

\[
\boxed{
Q_{\mathcal T_A}:=
\sum_{v}w_v\operatorname{Inf}_{i(v)}(f_v)
=\sum_{i\in A}\operatorname{Inf}_i(f)=:I_A(f).
}
\tag{4.1}
\]

### Proof
Fix `i in A`. Before the tree queries `i`, its decisions depend only on already observed coordinates in `A\setminus\{i\}`. Hence the collection of nodes at which `i` is queried partitions the physical `i`-edges of the original cube: the two endpoints of an `i`-edge have identical previously observed bits, so they arrive at the same node. The weighted restricted influence at those nodes is exactly the fraction of all original `i`-edges on which `f` changes. Thus their total contribution is `Inf_i(f)`. Sum over `i in A`. QED.

### Corollary 4.2 — paid block splicing
If

\[
B_A(f)\le K_A I_A(f)
\tag{4.2}
\]

and, after fixing `A`, each leaf `f_x` has a full hereditary certificate

\[
R_{\mathcal T_x}(f_x)\le K_0 I(f_x),
\tag{4.3}
\]

then the tree obtained by first completing `A` and then grafting the leaf trees satisfies

\[
\boxed{R_{\mathcal T}(f)\le\max\{K_A,K_0\}I(f).}
\tag{4.4}
\]

Indeed Theorem 3.1 and (4.2) pay the prefix by `K_A I_A(f)`, while the exact restriction influence identity gives

\[
I(f)=I_A(f)+\mathbb E_x I(f_x).
\tag{4.5}
\]

This is the hereditary version of the useful-block program: once a block conditional entropy is paid, physically realizing the block does not create a hidden extra allocation bill.

---

## 5. Balanced-controller block theorem

The block theorem is useful when a complicated controller determines which of two residual functions is active.

### Theorem 5.1
Let `h:{-1,1}^A->{-1,1}` be balanced, and let `g_+,g_-:{-1,1}^Y->{-1,1}` be arbitrary Boolean functions on a disjoint residual block. Define

\[
f(a,y)=
\begin{cases}
g_+(y),&h(a)=+1,\\
g_-(y),&h(a)=-1.
\end{cases}
\tag{5.1}
\]

Put

\[
\alpha:=\Pr_y[g_+(y)\ne g_-(y)].
\tag{5.2}
\]

Then

\[
\boxed{B_A(f)\le h_2(\alpha)+\alpha H(\widehat h^{\,2}),}
\tag{5.3}
\]

\[
\boxed{I_A(f)=\alpha I(h),}
\tag{5.4}
\]

and

\[
\boxed{I_Y(f)=\frac{I(g_+)+I(g_-)}2.}
\tag{5.5}
\]

Hence any complete adaptive query of all controller variables has hereditary allocation at most the right side of (5.3).

### Proof
Write

\[
c=\frac{g_++g_-}{2},\qquad d=\frac{g_+-g_-}{2}.
\]

Then `f=c+hd`, `cd=0` pointwise, `||d||_2^2=alpha`, and `||c||_2^2=1-alpha`. Since `h` is balanced, `\widehat h(emptyset)=0`. Fourier factorization on the product cube gives

\[
\widehat f(S,T)=
\begin{cases}
\widehat c(T),&S=\varnothing,\\
\widehat h(S)\widehat d(T),&S\ne\varnothing.
\end{cases}
\tag{5.6}
\]

Therefore the controller-frequency marginal has the exact law

\[
\Pr(S_A=\varnothing)=1-\alpha,
\qquad
\Pr(S_A=S)=\alpha\widehat h(S)^2\quad(S\ne\varnothing).
\tag{5.7}
\]

Its entropy is

\[
H(S_A)=h_2(\alpha)+\alpha H(\widehat h^{\,2}).
\tag{5.8}
\]

Conditioning cannot increase entropy, so `B_A(f)=H(S_A|S_Y)<=H(S_A)`, proving (5.3).

For a controller coordinate `i`, flipping it changes `f` iff `h` changes and the two residual branches disagree. The two events live on disjoint variable blocks, hence

\[
\operatorname{Inf}_i(f)=\alpha\operatorname{Inf}_i(h),
\]
which sums to (5.4). For a residual coordinate `j`, conditioning on the balanced controller chooses `g_+` and `g_-` with equal probability, giving

\[
\operatorname{Inf}_j(f)=\frac{\operatorname{Inf}_j(g_+)+\operatorname{Inf}_j(g_-)}2.
\]
Summing gives (5.5). QED.

This theorem is not a universal selector: the ratio in (5.3)/(5.4) still depends on the controller's own Fourier entropy/influence ratio. Its value is that all controller coordinates can be paid **jointly once**, rather than one dependent branch at a time.

---

## 6. Application: a signed-translation-rigid connected high-degree core with `R<4I`

Let `h_d` be recursive ternary majority of depth `d`: `h_0(x)=(-1)^x` and `h_{d+1}` is majority of three independent copies of `h_d`. It has `N_d=3^d` inputs and is balanced. The base three-bit majority has four equal nonzero squared Fourier masses, so entropy two, and each of its three coordinate influences is `1/2`. The standard disjoint-block composition calculation therefore gives

\[
I(h_d)=\left(\frac32\right)^d,
\qquad
H(h_d)=4\left[\left(\frac32\right)^d-1\right].
\tag{6.1}
\]

Let `u_m` be the one-point defect on `m` residual bits: `u_m(0)=-1` and `u_m(y)=+1` otherwise. Set

\[
\alpha=2^{-m}
\]

and define the controlled function

\[
F_{d,m}(a,y)=
\begin{cases}
1,&h_d(a)=+1,\\
u_m(y),&h_d(a)=-1.
\end{cases}
\tag{6.2}
\]

Equivalently, if `h_d=(-1)^{P_d}` in `F_2` phase notation,

\[
F_{d,m}(a,y)=(-1)^{P_d(a)\delta_0(y)},
\qquad
\delta_0(y)=\prod_{j=1}^m(1+y_j).
\tag{6.3}
\]

### 6.1 Exact influence

Theorem 5.1 and the one-point influence give

\[
I_A(F_{d,m})=\alpha\left(\frac32\right)^d,
\tag{6.4}
\]

and, since `I(u_m)=m2^{1-m}=2m\alpha`,

\[
I_Y(F_{d,m})=m\alpha.
\tag{6.5}
\]

Thus

\[
\boxed{
I(F_{d,m})=\alpha\left[\left(\frac32\right)^d+m\right].
}
\tag{6.6}
\]

### 6.2 Controller allocation

Theorem 3.1 and Theorem 5.1 give a complete controller prefix with

\[
R_{\rm prefix}
\le h_2(\alpha)
+4\alpha\left[\left(\frac32\right)^d-1\right].
\tag{6.7}
\]

After the controller is fixed, half the physical leaves are constant and half are `u_m`. The inherited NM13-02 one-point certificate gives weighted residual allocation at most

\[
\frac12 C_\chi I(u_m)=C_\chi m\alpha.
\tag{6.8}
\]

Hence the grafted full tree satisfies

\[
R_{\mathcal T}(F_{d,m})
\le h_2(\alpha)
+4\alpha\left[\left(\frac32\right)^d-1\right]
+C_\chi m\alpha.
\tag{6.9}
\]

For `alpha=2^{-m}`,

\[
h_2(\alpha)
=\alpha m+(1-\alpha)\log_2\frac1{1-\alpha}
\le\alpha\left(m+\frac1{\ln2}\right),
\tag{6.10}
\]

because `-ln(1-alpha)<=alpha/(1-alpha)`. Therefore

\[
R_{\mathcal T}
\le\alpha\left[
4\left(\frac32\right)^d-4
+(1+C_\chi)m+\frac1{\ln2}
\right].
\tag{6.11}
\]

Comparing with `4I` from (6.6),

\[
4I(F_{d,m})-R_{\mathcal T}(F_{d,m})
\ge\alpha\left[
4-\frac1{\ln2}+(3-C_\chi)m
\right]>0,
\tag{6.12}
\]

since `C_chi<3`. Thus

\[
\boxed{R_{\mathcal T}(F_{d,m})<4I(F_{d,m})}
\qquad\text{for all }d,m\ge1.
\tag{6.13}
\]

For fixed `m` and `d to infinity`, the displayed certificate ratio approaches four from below; the theorem is uniform but this particular proof is not claiming a smaller universal constant for the family.

### 6.3 Why this hits P03's current geometric obstruction

The phase polynomial of recursive majority satisfies

\[
P_{d+1}=P_d^{(1)}P_d^{(2)}+P_d^{(1)}P_d^{(3)}+P_d^{(2)}P_d^{(3)},
\]
so

\[
\deg P_d=2^d.
\tag{6.14}
\]

Equation (6.3) has phase degree

\[
\boxed{\deg(P_d\delta_0)=2^d+m,}
\tag{6.15}
\]

which is unbounded.

Its degree-at-least-three ANF interaction hypergraph is a single connected component. For `d=1`, the controller phase is `ab+ac+bc`; multiplying by every singleton term `y_j` from `delta_0` creates cubic hyperedges such as `{a,b,y_j}`, `{a,c,y_j}`, `{b,c,y_j}`, connecting all controller and residual variables. For `d>=2`, the degree-at-least-three monomials of `P_d` already connect all three recursive controller blocks inductively, and multiplying any such monomial by `y_j` attaches every residual variable to that connected controller core.

The family also has no nonzero signed translation symmetry. Its negative set is

\[
E=\{a:h_d(a)=-1\}\times\{0\}.
\]

Because `h_d` is balanced, `E` has density `2^{-m-1}<1/2`; a negative signed translation would have to map `E` to its complement and therefore would force density `1/2`, impossible. If a positive translation `(u,v)` preserved `E`, its residual projection `{0}` forces `v=0`. Then `h_d(a+u)=h_d(a)`. Every controller coordinate has nonzero singleton Fourier coefficient (for recursive monotone majority its magnitude equals its coordinate influence `2^{-d}`), and translation invariance would force every Fourier coefficient on a set having odd dot product with `u` to vanish. Applying this to the singleton coefficients gives `u=0`.

Thus `F_{d,m}` is an explicit signed-translation-rigid, one-connected, unbounded-degree core family of exactly the type left after P03's symmetry quotienting. The new theorem shows that this geometry alone is not an allocation obstruction: a high-complexity dependent controller can have its entire physical realization compressed into one spectral block budget.

This does not assert that no prior restricted theorem happens also to cover special members of the family, and publication novelty is not claimed.

---

## 7. Relation to the newest P03 proof

P03's newest report removes dependent recombination as a separate ledger by its peer theorem `J_i^rec<=B_i`, then asks for a universal full-tree hereditary allocation bound. The present result is complementary rather than duplicative:

- P03 controls what happens **after** a local allocation `B_i` is known.
- Theorem 3.1 controls how a **whole dependent physical block** can be realized without paying more than its one-shot spectral conditional entropy.
- On `F_{d,m}`, individual sequential decisions may keep both branches nontrivial for many levels, but block compression avoids an additive depth loss and produces the uniform `<4` hereditary certificate.

Theorem 3.1 itself does not rely on P03's newest `J_i^rec<=B_i`. If that peer theorem survives later independent review, then any hereditary certificate obtained here converts to the corresponding direct FEI certificate with the reported factor-two comparison. That project-level implication is **CONDITIONAL ON PEER REVIEW**; it is not used to label FEI solved here.

---

## 8. What remains open and failed extension in this run

The block theorem does **not** prove a universal useful-block selector. In particular, `A=[n]` makes `B_A(f)=H(f)` and simply restates the original difficulty. The live universal target is now sharper:

> choose, along every unresolved signed-rigid core, a proper physical block `A` for which `B_A(f)` is bounded by a constant times `I_A(f)`, or prove another influence-summable stopping rule that reaches already certified leaves.

The balanced-controller theorem succeeds because the two residual branches separate as `c+h d` and the controller spectrum has one exact shared disagreement mass `alpha`. I attempted to drop balancedness immediately; then `\widehat h(emptyset)\widehat d(T)` collides coherently with `\widehat c(T)` in the zero controller frequency, and the clean marginal law (5.7) disappears. No dimension-free replacement for that collision was proved in this run. This extension is **UNPROVED**, not silently assumed.

Likewise, no claim is made that arbitrary quadratic twisting of the controller family preserves the `<4` certificate: a general quadratic twist mixes Fourier coordinates by rank-dependent blocks rather than by a simple frequency permutation. The earlier quadratic-normalized results remain separate restricted tools.

All previously recorded false-lemma corrections remain in force.

---

## 9. Executed sanity check

The preserved checker is

`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T15-08-00+0300__check_block_allocation_compression.py`.

Its archived output is

`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T15-08-00+0300__block_allocation_compression_check.json`.

The run reports `PASS`. It checks:

- all Boolean functions modulo global sign through dimension three, every nonempty block, and every fixed order of that block: **1,954** order cases;
- **600** deterministic dimension-four functions, every nonempty block and every fixed order: **38,400** additional order cases;
- maximum observed `R_prefix-B_A = 5.551115123125783e-17` and maximum positive `R_prefix/B_A = 1.0000000000000002` (floating-point roundoff);
- direct Walsh calculations on the explicit depth-one controller family for `m=1,...,5`, including the block bound, influence identity, and grafted `<4` certificate;
- the analytic certificate formula on `1<=d<=30`, `1<=m<=40`, whose largest sampled ratio is `3.999984329793932` at `(d,m)=(30,2)`.

These computations are sanity checks only. The all-dimensional results are proved analytically in Sections 3–6.

Checker creation commit: `da3e231ae1da6cc512a84b61f5dbf228f0662204`, blob `0a236951da8dabbd8645cdb25ee650a6fd226181`.

Output creation commit: `d94999596d483b009f8dd8815f1905ac91808a52`, blob `78a3e8b4659ca3cdbc82b8f99eae10bd919e1f24`.

---

## 10. Next nonredundant attack

The next target is the smallest genuinely **two-hard-block** analogue of Theorem 5.1: control `B_A(f)` when a balanced controller selects two nontrivial residual branches whose Fourier pieces collide in the same residual labels. The right object should be a joint square-mass/Hellinger budget invariant under the complete-block concavity step, not another coordinatewise marginal surcharge. A successful inequality would let Theorem 3.1 turn it immediately into a physical hereditary tree. If two consecutive attempts at that collision problem fail, the fallback is a distinct FEI subproblem: prove a proper-block selector for bounded controller entropy/influence ratio under arbitrary physical restrictions, preserving the present block-compression theorem as the transfer engine.

---

```yaml
ledger_delta:
  parent_problem: "T01 Friedgut-Kalai Fourier entropy-influence"
  owner: "NM13-02"
  companion: "P03"
  source_status_before: "OPEN"
  source_status_after: "OPEN"
  universal_constant_before: "UNKNOWN"
  universal_constant_after: "UNKNOWN"
  theorem_scope: "all Boolean functions; every physical block; every complete adaptive physical realization of that block"
  mechanism_gain: "proved R_prefix <= H(S_A|S_Ac), with exact queried influence Q_prefix=I_A; block conditional entropy is a valid one-shot hereditary allocation budget"
  application: "balanced recursive-majority controller selecting constant versus one-point defect; signed-translation-rigid connected ANF core of degree 2^d+m"
  application_gain: "constructed a full physical tree with R_T < 4 I uniformly for every d,m>=1"
  parent_problem_closed: false
  fresh_variables_used: false
  peer_claims_taken_over: false
  p03_dependency_status: "new block theorem independent of P03's reported J_rec<=B; factor-two direct-FEI conversion remains peer-review conditional"
  false_routes_preserved:
    - "pointwise erasure shortcut"
    - "all-constant resolvent/interpolation"
    - "fixed-coefficient affine drift"
    - "Han absolute-overlap selector"
    - "derivative-degree scalar schedule"
    - "blind curvature/query payment"
    - "fixed-s<2 Renyi payment"
    - "root marginal-entropy replacement"
    - "arbitrary orthogonal-involution relaxation"
  failed_extension: "unbalanced controller has coherent zero-frequency c + hhat(empty)d collision; no dimension-free replacement proved"
  residual_obstruction: "universal useful proper-block selector or other influence-summable full-tree allocation on arbitrary signed-rigid cores"
  checker_status: "PASS"
  checker_coverage: "1954 exhaustive fixed-order block cases through dimension 3; 38400 deterministic dimension-4 fixed-order cases; explicit controller family plus formula scan"
  independent_review: "PENDING"
  publication_priority: "UNVERIFIED"
```

**End of immutable substantive report.**