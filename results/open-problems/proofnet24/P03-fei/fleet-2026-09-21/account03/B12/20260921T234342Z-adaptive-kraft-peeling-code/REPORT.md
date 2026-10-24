# B12 Campaign-B result — explicit Kraft spectral code, adaptive fine peeling, and the surviving singleton-router obstruction

**Date:** 2026-09-21 UTC  
**Scope:** `account03 / B12`, full uniform-cube Fourier entropy-influence conjecture, Campaign B under `FEI-PROOF-EXECUTION-20260921T230620Z`.  
**Execution:** **WITHOUT_VERIFIED_BRAIN**. No authenticated mathematical-brain retrieval or receiver-context use occurred.  
**Outcome:** **AUXILIARY_ONLY with one natural universal coverage candidate REFUTED. Full unrestricted FEI remains OPEN / NOT PROVED.**

## 0. Live assignment and source-bound peer results

The post-reset B12 assignment is: **construct a decodable version of the common spectral code and price coordinate labels and exceptions.** At scientific master `b8ec7bac7d60432840ec2539b877fde3058510d8`, no post-reset account03/B18 Campaign-B lead report was yet present; the newest visible B18 report remained `20260921T230034Z-character-parent-gauge-null`, which predates the reset. Per the reset fallback rule, this run therefore binds to the smallest explicit common Campaign-B target already completed by builders/adversary.

Two completed peer artifacts are consumed substantively.

1. **account02/B17**, `20260921T231240Z-recursive-majority-hierarchical-code/REPORT.md`, Git blob `be4735ca18bda8d3598708324565ac16f912a280`. It proves the hierarchical ordered-code inequality
   \[
   H(S)\le h_2(\tau_{\rm root})+\sum_{v\ \operatorname{internal}}\tau_v U_v,
   \]
   together with exact branch-surplus conservation
   \[
   \sum_v\tau_v(\mu_v-1)=I-\tau_{\rm root},
   \]
   and refutes every finite one-level ordered-envelope constant using recursive ternary majority. Its remaining named obstruction is **singleton routing**.

2. **account01/B12**, `20260921T231256Z-conditional-count-code/REPORT.md`, Git blob `cbeaa0cba209474fe720c24c3eb80611a92d5468`. It proves the universal component-count collapse
   \[
   H(Y\mid T)\le H(N\mid T)+\sum_C(E_C-Q_C),
   \tag{0.1}
   \]
   and on each fine closed reciprocal Palm component the bounds
   \[
   E_C-Q_C\le c_0P_C,
   \qquad c_0=2\log_2e+\frac1{16}=2.9478900817779268\ldots,
   \tag{0.2}
   \]
   \[
   H(K_C)\le c_{\rm count}P_C,
   \qquad c_{\rm count}=\frac{17}{16}(2+\log_2e)=3.6578634809445236\ldots .
   \tag{0.3}
   \]
   Thus a fully fine closed sector costs
   \[
   C_{\rm robust}=c_0+c_{\rm count}=6.605753562722450\ldots
   \tag{0.4}
   \]
   per expected spectral coordinate. Its remaining issue is how to handle non-fine/scale-escape coordinates without repeatedly repaying their labels.

`applied_to_claim`: turn the hierarchical Shannon envelope into a genuine source code, then show that **arbitrarily many adaptive fine/escape stages do not themselves create repeated coordinate-label debt**. This attacks the exact scale-escape bookkeeping gap of the peer result. Then test whether fine peeling could be the whole singleton-routing solution.

## 1. PROVED: each ordered local envelope is a Kraft-valid code, not just an entropy upper bound

Let a decoder-visible node have finite child set `J`. Conditional on the node being active, let `D` be the number of active children, let
\[
\pi_k=\Pr(D=k),\qquad \mu=\mathbb E D,
\]
and let
\[
r_j=\Pr(j\text{ active}),\qquad q_j=r_j/\mu,\qquad \sum_jq_j=1.
\]
For every nonempty active-child subset `A subseteq J`, define
\[
W(A):=\pi_{|A|}\,|A|!\prod_{j\in A}q_j.
\tag{1.1}
\]

### Lemma 1.1 — local Kraft inequality

\[
\boxed{\sum_{\emptyset\ne A\subseteq J}W(A)\le1.}
\tag{1.2}
\]

**Proof.** For each `k`,
\[
\sum_{|A|=k}k!\prod_{j\in A}q_j
=k!e_k(q).
\]
The left side is the total weight of ordered `k`-tuples of **distinct** children. It is therefore at most the weight of all ordered `k`-tuples:
\[
k!e_k(q)\le\left(\sum_jq_j\right)^k=1.
\]
Multiplying by `pi_k` and summing over `k` proves (1.2). QED.

Thus the ideal lengths
\[
\ell(A)=-\log_2W(A)
\tag{1.3}
\]
are Kraft-valid. Their expected length under the actual child-subset law is exactly
\[
\begin{aligned}
\mathbb E\ell(A)
&=H(D)+\sum_jr_j\log_2\frac1{q_j}-\mathbb E\log_2(D!)\\
&=H(D)+\mu H(q)-\mathbb E\log_2(D!)\\
&=U_v.
\end{aligned}
\tag{1.4}
\]
So the account02/B17 quantity `U_v` is the expected length of an explicit subprobability code. **All child/coordinate identities are inside the `q_j` symbols; there is no hidden external name field.**

### Corollary 1.2 — fixed hierarchical tree is genuinely decodable

Take the product of the local weights (1.1) over all active internal nodes of a known rooted coordinate partition tree, together with the true root-activity probability. Recursive summation from the leaves upward and (1.2) give a global subprobability `W_T(S)` with
\[
\sum_SW_T(S)\le1
\]
and
\[
\mathbb E[-\log_2W_T(S)]
=h_2(\tau_{\rm root})+\sum_v\tau_vU_v
=\operatorname{Code}_T(S).
\tag{1.5}
\]
Hence the common hierarchical code is not merely an entropy metaphor: it is a Kraft code from which the terminal spectral set is reconstructed exactly because the tree and every previously decoded branch are decoder-visible.

For literal integer-bit prefix coding, apply the same construction to `m` independent spectral samples and use lengths `ceil(-log_2 prod_a W_T(S_a))`. The entire `m`-sample block has at most one extra bit, so the overhead is at most `1/m` per sample and vanishes as `m to infinity`. No `+1` is charged per tree node.

## 2. PROVED: adaptive fine peeling has exact nonreuse across arbitrarily many escape levels

The account01 result (0.1)-(0.4) was stated for a fixed partition. The next issue was whether repeatedly discovering fine blocks after conditioning would repay coordinate identities or count entropy at every scale. It does not.

Consider any finite random spectral-set law `Y`, with arbitrary already-known side information `T`. A **decoder-visible peeling policy** is deterministic from information already decoded. At a context `c`, it chooses disjoint coordinate blocks
\[
\mathcal F(c)=\{C_1,\ldots,C_s\}
\]
inside the current residual universe, removes them permanently, and continues on the remaining coordinates. The next context may depend on the decoded counts and subsets. Assume:

1. each coordinate is removed at most once;
2. with probability one, every nondeterministic coordinate is eventually removed (a deterministic terminal residual costs zero entropy);
3. for every block `C` at every context `c`, **the conditional law at that context** satisfies the same two fine-component hypotheses used by account01/B12: reciprocal Palm TV at most `1/(16m_C)` and the corresponding physical density relation. Thus (0.2)-(0.3) apply conditionally.

### Theorem 2.1 — adaptive fine-peeling code

Under these hypotheses,
\[
\boxed{
H(Y\mid T)\le C_{\rm robust}\,\mathbb E|Y|,
\qquad
C_{\rm robust}=6.605753562722450\ldots .
}
\tag{2.1}
\]
The bound is independent of the number of peeling/escape stages.

**Proof.** For a peeled block `C` in context `c`, first encode its count `K_C`. Given `K_C=k`, encode the actual subset `A=Y cap C` using the fixed-count Kraft weight
\[
W_{C,c}(A\mid k)=k!\prod_{i\in A}q_i(c),
\qquad
q_i(c)=\frac{\Pr(i\in Y\mid c)}{P_C(c)}.
\tag{2.2}
\]
For fixed `k`,
\[
\sum_{|A|=k}W_{C,c}(A\mid k)=k!e_k(q(c))\le1,
\]
so this is decodable. Its conditional expected internal length is exactly
\[
E_C(c)-Q_C(c)\le c_0P_C(c).
\tag{2.3}
\]

Encode the whole adaptive count transcript with its true conditional distribution. Because the policy is a deterministic function of already decoded information, **no partition identifier is transmitted**. By the chain rule and conditional subadditivity, the count-transcript entropy is at most
\[
\sum_c\Pr(c)\sum_{C\in\mathcal F(c)}H(K_C\mid c)
\le c_{\rm count}\sum_c\Pr(c)\sum_{C\in\mathcal F(c)}P_C(c).
\tag{2.4}
\]
The internal subset code contributes at most the same sum multiplied by `c_0`.

Finally, permanent removal gives the exact nonreuse identity
\[
\sum_c\Pr(c)\sum_{C\in\mathcal F(c)}P_C(c)
=\mathbb E[\text{number of spectral coordinates eventually peeled}]
\le\mathbb E|Y|.
\tag{2.5}
\]
Under complete nondeterministic coverage it is equality. Combining (2.3)-(2.5) proves (2.1). QED.

**Consequence.** `scale escape` by itself is no longer a coding obstruction: a coordinate can survive an arbitrary number of contexts for free and is charged exactly once, when it is finally placed in a fine block. The remaining problem is **existence/coverage**, not repeated coordinate naming.

## 3. EARLY ADVERSARY: universal fine-only coverage is REFUTED by three-bit majority

The tempting next statement would be:

> every Boolean spectral source admits an adaptive peeling policy satisfying the fine reciprocal-Palm hypotheses until deterministic termination.

This is **false already for**
\[
M(x_1,x_2,x_3)=\operatorname{Maj}_3(x_1,x_2,x_3).
\]
Its squared Fourier law is uniform on
\[
\{1\},\ \{2\},\ \{3\},\ \{1,2,3\}.
\tag{3.1}
\]
Fix coordinate `1`. Conditional on `1 in S`,
\[
S\setminus\{1\}=\emptyset\quad\text{or}\quad\{2,3\},
\]
each with probability `1/2`.

For the three-coordinate candidate component `C={1,2,3}`, the ideal law on `C\setminus{1}` is uniform on all four subsets of `{2,3}`. Therefore
\[
\operatorname{TV}\!\left(
\tfrac12\delta_\emptyset+\tfrac12\delta_{\{2,3\}},
U_{\{2,3\}}
\right)=\frac12,
\tag{3.2}
\]
whereas the fine threshold is
\[
\frac1{16m}=\frac1{32}.
\]
The density condition also fails: `p_1=1/2` while `2^{-m}=1/4`.

A two-coordinate candidate, e.g. `C={1,2}`, does not repair this: conditional on `1 in S`, half the mass is at `{2,3}`, outside the proposed ideal support `{emptyset,{2}}`, again giving TV at least `1/2`, versus threshold `1/16`. By symmetry no nontrivial fine block covers any coordinate at the root.

Thus **fine peeling alone cannot solve the common singleton-routing implication**. This is a Boolean counterexample to that stronger coverage lemma, not a counterexample to FEI. Indeed the peer account02/B17 report proves recursive majority has true `H/I<4` and a bounded natural hierarchical code.

## 4. PROVED fallback criterion: binary branching pays itself whenever coactivation is not tiny

The majority failure shows that non-fine nodes must sometimes be paid by actual branching rather than Palm-uniformity.

At an active binary tree node let its two child blocks be `L,R`, and define
\[
\gamma=\Pr(S\cap L\ne\emptyset,\ S\cap R\ne\emptyset\mid A_v=1).
\]
Since the active-child subset has only three possible nonempty values,
\[
H(Y_v\mid A_v=1)\le\log_2 3.
\tag{4.1}
\]
For a binary node
\[
\mu_v-1=\gamma.
\tag{4.2}
\]
Therefore, for every `eta>0`,
\[
\boxed{
\gamma\ge\eta
\quad\Longrightarrow\quad
H(Y_v\mid A_v=1)
\le\frac{\log_2 3}{\eta}(\mu_v-1).
}
\tag{4.3}
\]
After multiplication by `tau_v`, these payments sum through the exact branch-surplus telescope from the peer report. Thus all nodes with a dimension-free lower bound on conditional coactivation have an automatic dimension-free routing code. **Only low-coactivation high-routing nodes remain dangerous.**

For the first binary split `{1}` versus `{2,3}` of three-bit majority, the child-state probabilities are `(1/4,1/2,1/4)`, so `gamma=1/4` and the actual node entropy is exactly `1.5` bits. The second split of `{2,3}`, conditional on that block being active, has the three child states equiprobable, so `gamma=1/3`. Hence majority lies on the paid-branch side, exactly as the account02/B17 hierarchy predicted; it is not evidence for universal fine coverage.

## 5. Exact old/new missing implication

**Old missing implication (post-reset Campaign B):** build a genuinely decodable source-admissible hierarchical spectral code and prove a dimension-free payment for singleton routing / exceptions.

**New proved inference:**
- the local ordered envelope is Kraft-valid and therefore gives a genuine decodable hierarchical code;
- coordinate identities are fully accounted for by the local `q` symbols;
- repeated adaptive fine/escape stages create **zero repeated label debt**; every spectral coordinate is charged once when peeled;
- any binary node with coactivation bounded below is paid by exact branch surplus.

**Refuted candidate:** universal coverage using only the existing fine reciprocal-Palm component criterion. Three-bit majority already violates it by TV `1/2` versus `1/32` (or `1/16` for a two-coordinate candidate).

**Remaining universal implication:** prove a Boolean **persistent singleton-router lemma**. One sufficient version is: construct a decoder-visible adaptive binary/fine hierarchy in which every unresolved node either
1. enters a fine block covered by Theorem 2.1;
2. has conditional coactivation at least one universal `eta>0`, hence is paid by (4.3); or
3. terminates in a character/deterministic source with zero residual entropy.

A theorem of this form with universal `eta` would give a finite dimension-independent spectral code (and hence FEI after the standard balanced/tensor reduction). The hard case is now explicit: a long adaptive chain with **high entropy of the unique-child identity but vanishing pair coactivation**, while never becoming fine or character-like.

## 6. Next attack

Attack the persistent singleton-router lemma directly on **addressing and biased sparse-defect Boolean families**, because those can exhibit many possible unique descendants. The next calculation should measure, at each decoder-visible binary split,
\[
\frac{H(\text{child identity}\mid\text{active})}
{\Pr(\text{both children active}\mid\text{active})}
\]
and test whether a long bad chain necessarily creates a fine Palm block, a character certificate, or an information refund at an ancestor. Recursive majority is no longer the binding adversary: it is paid by nontrivial coactivation.

`consumed_peer_artifact`: account01/B12 `20260921T231256Z-conditional-count-code/REPORT.md`, blob `cbeaa0cba209474fe720c24c3eb80611a92d5468`; account02/B17 `20260921T231240Z-recursive-majority-hierarchical-code/REPORT.md`, blob `be4735ca18bda8d3598708324565ac16f912a280`.

`applied_to_claim`: genuine decodability and exact nonreuse for the common Campaign-B hierarchical code; adaptive exception pricing.

`remaining_implication`: universal Boolean persistent-singleton-router lemma / source-admissible hierarchy with finite routing payment.

`next_recipient`: account03/B18 Campaign-B lead and account02/B17 principal adversary; account01/B12 for conditional-count integration.

**Full FEI status:** **OPEN / NOT PROVED.** No novelty or publication-priority claim is made.
