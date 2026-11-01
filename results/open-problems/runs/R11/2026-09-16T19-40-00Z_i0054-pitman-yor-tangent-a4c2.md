Model: GPT-5.6 Sol. Reasoning: UNVERIFIED runtime level; GPT-6 / maximum was requested, but the exposed scheduler has no model-family or reasoning-effort selector, so GPT-6 / maximum was not verified and is not claimed. Metric movement: `3 -> 4` distinct nontrivial discrete model classes with complete author-side CTCS(infinity) limit proofs under the frozen equivalence convention. Section-B moves actually tried: **1 (change category), 17 (look for the numbers somewhere else), 27 (swap the quantifiers)**.

Problem/source: David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3 (18 April 2025), **Open Problem 18**, intake `I0054`. Overall campaign status remains **PARTIAL**: the new claim `R11-I0054-C004` below is author-side **PROVED under the frozen equivalence convention**, but source-intent/prior-art clearance and the two required OTHER-track closure audits are not complete.

# R11 I0054 — a positive-discount Pitman--Yor hierarchy has CTCS(infinity) as its small-parameter accelerated limit

Run ID: `2026-09-16T19-40-00Z_i0054-pitman-yor-tangent-a4c2`  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Dated source/status check: 2026-09-16

No Gmail/email, Drive, public posting, paid compute, workflow execution, permission change, scheduler mutation, peer-file edit, or shared-root edit was performed.

---

## 1. Continuity, whole-repository read, ownership and runtime controls

I continued from the newest complete R11 report rather than restarting:

`runs/R11/2026-09-16T18-41-35Z_i0054-gibbs-dirichlet-tangent-d3f7.md`.

That report proved `R11-I0054-C003` and moved the frozen metric `2 -> 3`. The three retained author-side classes entering this run are:

1. `C001`: harmonic-grid paintbox fragmentation (HGPF);
2. `C002`: small-concentration nested Chinese restaurant process (SC-nCRP);
3. `C003`: near-critical ternary Dirichlet/Gibbs fragmentation (TDGF).

Before new research I read/searched the required current state:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/claims/I0054.md`;
- the I-intake ledger hit for I0054 and repository-wide I0054 ownership/attempt hits;
- the newest R11 report;
- the newest neighboring P13 Open Problem 9 / I0051 report, which remains a distinct clade-covariance problem.

The current claim file still records R11 as the provisional exclusive I0054 owner, native task `6aa7b68c70c481919b1a131eb67b6b24`, with status `PENDING_ADMISSION, not READY`. I found no competing I0054 owner and no posted/settled exclusion. I did not mutate the coordinator-owned claim file.

The retired planar-SAW R11 history remains preserved in older immutable reports and is not reopened here.

### Actual model/scheduler controls

The actual runtime identifies this worker as GPT-5.6 Sol. Reasoning effort is not exposed, so it is `UNVERIFIED`.

The scheduler/update schema exposed to this context has fields for task title/prompt, schedule, enabled state, and timing mode. It has **no model-family field and no reasoning-effort field**. Therefore putting `GPT-6 / maximum` in prompt text requests those settings but does not install or verify them.

The current repository operations record also documents context-dependent `You cannot modify this task` failures. It specifically records historical probes against P26/P01/P03 and, in another context, denials for the R-series. P26 was later successfully updated in an authorized context, so a denial is not an account-wide theorem about the task; it is a permission/context failure. The permitted workaround is to use an authorized account/workspace/task-owner interface that owns the existing task, or platform support that exposes/repairs those controls. Cloning or bypassing the task is not an allowed workaround. No scheduler change was attempted in this run.

---

## 2. Exact source target and convergence object

The current v3 source still states Open Problem 18 in Section 6.3:

> Are there superficially different discrete models whose limit is the same CTCS(infinity)?

and immediately asks whether the source model's subordinator approximation can arise in another discrete tree model.

The source's limit object is not merely a tagged fragment. Aldous--Janson's exchangeable-partition representation formalizes CTCS(infinity) by the entire nested partition process

\[
(\Pi(t),t\ge 0)
\]

on the positive integers. On a finite restriction, the partition path records every clade split and its time. Ignoring irrelevant left/right child order, these consistent finite restrictions determine the complete CTCS(infinity) genealogy.

I therefore retain the explicit strong convergence convention from C001--C003. For each finite restriction use Skorokhod `J_1`; assemble restrictions with

\[
d_{\rm proj}(\omega,\eta)
=
\sum_{k\ge1}2^{-k}
\left(1\wedge d_{J_1,k}(\omega^{[k]},\eta^{[k]})\right).
\tag{2.1}
\]

This name/topology is R11's explicit formalization; I do not attribute the phrase "projective J_1" to Aldous--Janson.

For a particular binary partition of an \(m\)-label block into \(A\) and \(A^c\), with \(|A|=i\), the CTCS generator rate is

\[
q_{A|A^c}
=
B(i,m-i)
=
\frac{(i-1)!(m-i-1)!}{(m-1)!},
\tag{2.2}
\]

and the total split rate of an \(m\)-block is \(H_{m-1}\).

---

## 3. Dated current-literature and prior-attempt screen

On 2026-09-16 I refreshed bounded searches including:

- `"Open Problem 18" CTCS Aldous Janson discrete models`;
- `"Poisson-Dirichlet" CTCS "critical beta-splitting"`;
- `"Pitman-Yor" CTCS beta-splitting`;
- `"Gibbs fragmentation trees" Poisson-Dirichlet alpha theta`;
- recent 2026 critical-beta-splitting / homogeneous-fragmentation papers;
- repository-wide I0054, CTCS(infinity), and audit searches.

The current source v3 still prints Open Problem 18.

Recent papers located include Chorbadzhiyska--Minchev--Savov (arXiv:2608.18320), which embeds the full beta-splitting family in homogeneous fragmentations and studies heights/potential theory, and Heng Ma's September 2026 work on extremal separation/clade dynamics and discrete height. I found no claim in those papers that a positive-discount Pitman--Yor discrete hierarchy converges to CTCS(infinity) as an answer to Open Problem 18.

The decisive older prior art is McCullagh--Pitman--Winkel, *Gibbs fragmentation trees* (Bernoulli 14 (2008), arXiv:0704.0945). Their multifurcating Gibbs family is associated with two-parameter Poisson--Dirichlet partitions, including the positive-parameter range \(0\le\alpha\le1\), \(\theta\ge-2\alpha\). Thus the finite partition family used below is emphatically **known**. Positive-discount Pitman--Yor models are also standard in Bayesian nonparametrics and language modeling, where the discount parameter produces power-law cluster frequencies.

I did **not** find, in this bounded search, the simultaneous small-\((\alpha,\theta)\), accelerated-depth CTCS(infinity) limit theorem proved below. That negative search is not a worldwide novelty certificate. The mathematical tangent mechanism is elementary once one looks at the correct EPPF, so independent prior-art review remains essential.

---

## 4. Move 1 — CHANGE CATEGORY: from random trees to Bayesian nonparametric species-sampling partitions

C002 used the ordinary Chinese restaurant process, i.e. the zero-discount Ewens/Dirichlet partition law. The natural broader model in Bayesian nonparametrics is the positive-discount Pitman--Yor process.

For parameters

\[
0\le\alpha<1,\qquad \theta>-\alpha,
\]

the induced exchangeable partition of an \(m\)-set has EPPF

\[
\boxed{
p_{\alpha,\theta}(n_1,\ldots,n_r)
=
\frac{\prod_{j=1}^{r-1}(\theta+j\alpha)}
     {(\theta+1)_{m-1}}
\prod_{\ell=1}^{r}(1-\alpha)_{n_\ell-1}.
}
\tag{4.1}
\]

Here \((x)_s=x(x+1)\cdots(x+s-1)\).

The sequential seating rule is equally concrete. Given \(m\) seated labels in \(r\) tables with table sizes \(n_j\),

- the next label joins table \(j\) with probability \((n_j-\alpha)/(m+\theta)\);
- it starts a new table with probability \((\theta+\alpha r)/(m+\theta)\).

For \(\alpha=0\) this is the usual CRP underlying C002. For every \(\alpha>0\) it is the standard positive-discount Pitman--Yor mechanism with genuinely different reinforcement and power-law partition behavior.

The new discrete tree model recursively applies this seating/partition mechanism at every level of a hierarchy.

---

## 5. The discrete positive-discount Pitman--Yor hierarchy

Let \((\alpha_N,\theta_N)\) satisfy

\[
\alpha_N\ge0,\qquad \theta_N\ge0,\qquad
\delta_N:=\alpha_N+\theta_N\downarrow0.
\tag{5.1}
\]

For the concrete counted class I use

\[
\boxed{
\alpha_N=\theta_N=\frac1{2N},
\qquad
\delta_N=\frac1N.
}
\tag{5.2}
\]

For each \(N\), construct an infinite consistent hierarchy as follows.

Start with the single block \(\mathbb N\). At raw depth \(r=1,2,\ldots\), every current block is independently refined according to a fresh Poisson--Dirichlet/Pitman--Yor partition with parameters \((\alpha_N,\theta_N)\). Singleton blocks stay singleton. Sampling consistency gives a well-defined exchangeable hierarchy on \(\mathbb N\).

The **finite \(N\)-leaf discrete model** is the restriction of this hierarchy to labels \([N]\). Give every raw level length \(\delta_N\), and suppress consecutive no-change levels/degree-one stretches in the observed finite genealogy.

Write \(\Pi_N(r)\) for the partition after raw depth \(r\), and define the rescaled path

\[
\widehat\Pi_N(t)
=
\Pi_N\!\left(\left\lfloor t/\delta_N\right\rfloor\right).
\tag{5.3}
\]

For the concrete choice (5.2), raw level length is \(1/N\).

This is a discrete-depth model; its finite vertices can have arbitrarily large degree. The continuous branch lengths arise only after the rare-event scaling limit.

---

## 6. Move 17 — LOOK FOR THE NUMBERS SOMEWHERE ELSE: CTCS beta rates are the universal first derivative of the Pitman--Yor EPPF

This is the main calculation.

Set

\[
\delta=\alpha+\theta.
\]

The key fact is that the first derivative at the degenerate corner \((\alpha,\theta)=(0,0)\) does **not** depend on the direction from which that corner is approached inside the positive quadrant.

### 6.1 No split

For a block of size \(m\),

\[
p_{\alpha,\theta}(m)
=
\frac{(1-\alpha)_{m-1}}{(1+\theta)_{m-1}}
=
\prod_{j=1}^{m-1}\frac{j-\alpha}{j+\theta}.
\]

For fixed \(m\),

\[
\log p_{\alpha,\theta}(m)
=
\sum_{j=1}^{m-1}
\left[
\log(1-\alpha/j)-\log(1+\theta/j)
\right]
=
-\delta H_{m-1}+O_m(\delta^2).
\]

Hence

\[
\boxed{
p_{\alpha,\theta}(m)
=
1-\delta H_{m-1}+O_m(\delta^2).
}
\tag{6.1}
\]

### 6.2 A particular binary split

For one particular set partition \(A|A^c\), \(|A|=i\),

\[
p_{\alpha,\theta}(i,m-i)
=
(\theta+\alpha)
\frac{(1-\alpha)_{i-1}(1-\alpha)_{m-i-1}}
     {(1+\theta)_{m-1}}.
\]

Since the leading factor is exactly \(\delta\),

\[
\boxed{
p_{\alpha,\theta}(A|A^c)
=
\delta\,B(i,m-i)+O_m(\delta^2).
}
\tag{6.2}
\]

The coefficient is exactly the CTCS particular binary split rate (2.2).

### 6.3 Three or more blocks

For \(r\ge3\), the numerator in (4.1) contains

\[
(\theta+\alpha)(\theta+2\alpha).
\]

Under \(\alpha,\theta\ge0\), each factor is \(O(\delta)\). For fixed \(m\), all remaining factors stay bounded near the origin. Thus, uniformly over all particular \(r\ge3\) partitions of an \(m\)-set,

\[
\boxed{
p_{\alpha,\theta}(n_1,\ldots,n_r)
=
O_m(\delta^2).
}
\tag{6.3}
\]

Equations (6.1)--(6.3) say that the *entire positive Poisson--Dirichlet quadrant has the same CTCS first-order tangent* at the degenerate corner.

This is the number-pattern found by changing fields: the beta-function split weights of CTCS are literally the first derivative coefficients of the standard Pitman--Yor EPPF.

---

## 7. Move 27 — SWAP THE QUANTIFIERS: prove one theorem for every positive approach to the corner

Rather than tune one sequence of parameters, prove the stronger universal tangent statement.

### `R11-I0054-C004` — universal positive-Pitman--Yor tangent to CTCS(infinity)

**STATUS: PROVED author-side under the frozen equivalence convention; campaign remains PARTIAL pending independent audits and final source-intent/prior-art clearance.**

#### Theorem

Let \(\alpha_N,\theta_N\ge0\) and

\[
\delta_N=\alpha_N+\theta_N\downarrow0.
\]

Construct the recursive Pitman--Yor hierarchy of Section 5 and give each raw level length \(\delta_N\). Let \(\widehat\Pi_N\) be its rescaled exchangeable partition path.

Then, for every fixed \(k\),

\[
\boxed{
\widehat\Pi_N^{[k]}
\Longrightarrow
\Pi^{[k]}
}
\tag{7.1}
\]

in Skorokhod \(J_1\), where \(\Pi\) is the Aldous--Janson CTCS(infinity) exchangeable partition process.

Moreover,

\[
\boxed{
\widehat\Pi_N
\Longrightarrow
\Pi
}
\tag{7.2}
\]

in the projective metric (2.1).

In particular, the concrete positive-discount model

\[
\alpha_N=\theta_N=\frac1{2N}
\]

has the whole CTCS(infinity) genealogy as its limit.

### Proof

#### Step 1. Fixed restrictions are finite-state time-homogeneous Markov chains

Fix \(k\). By sampling consistency of the Poisson--Dirichlet/Pitman--Yor partition, the restriction of a fresh \((\alpha_N,\theta_N)\) partition to any finite block has exactly EPPF (4.1) with the same parameters.

At a raw depth, distinct current blocks are refined independently. Therefore \(\Pi_N^{[k]}(r)\) is a time-homogeneous Markov chain on the finite set of partitions of \([k]\).

#### Step 2. Uniform generator expansion

Let \(P_N^{(k)}\) be its one-raw-step transition matrix.

For a current state \(\rho\), every current block \(B\) of size \(m\le k\) remains intact with probability

\[
1-\delta_N H_{m-1}+O_k(\delta_N^2)
\]

by (6.1).

If \(\rho'\) is obtained from \(\rho\) by splitting exactly one current block \(B\) according to one particular binary partition \(A|B\setminus A\), then (6.2), multiplied by the no-change probabilities of all other current blocks, gives

\[
P_N^{(k)}(\rho,\rho')
=
\delta_N
B(|A|,|B\setminus A|)
+
O_k(\delta_N^2).
\tag{7.3}
\]

Every other strict transition either contains a refinement into at least three blocks or simultaneous visible refinements of two or more current blocks. By (6.3) and block independence, each such transition has probability \(O_k(\delta_N^2)\).

Because the state space is finite, all errors are uniform. Thus

\[
\boxed{
P_N^{(k)}
=
I+\delta_N Q^{(k)}+O_k(\delta_N^2),
}
\tag{7.4}
\]

where \(Q^{(k)}\) has exactly the CTCS particular binary rates (2.2). Its diagonal at state \(\rho\) is

\[
-\lambda(\rho),
\qquad
\lambda(\rho)
=
\sum_{B\in\rho}H_{|B|-1}.
\tag{7.5}
\]

This \(Q^{(k)}\) is the finite-restriction CTCS generator.

#### Step 3. Holding times converge

At a nonabsorbing visible state \(\rho\), let \(s_N(\rho)\) be the probability that a raw generation changes the visible partition. From (7.4),

\[
s_N(\rho)
=
\delta_N\lambda(\rho)+O_k(\delta_N^2).
\tag{7.6}
\]

While the visible state remains \(\rho\), each raw depth uses fresh independent Pitman--Yor refinements. Hence the number \(G_N\) of raw generations to the next visible change is geometric with parameter \(s_N(\rho)\).

For every \(t\ge0\),

\[
\begin{aligned}
\Pr(\delta_N G_N>t)
&=
(1-s_N(\rho))^{\lfloor t/\delta_N\rfloor+O(1)}
\\
&\longrightarrow
e^{-\lambda(\rho)t}.
\end{aligned}
\tag{7.7}
\]

Therefore

\[
\delta_N G_N
\Longrightarrow
{\rm Exp}(\lambda(\rho)).
\tag{7.8}
\]

#### Step 4. The jump chain converges and higher multifurcations vanish

For every CTCS-admissible next state \(\rho'\),

\[
\Pr(
\rho_{\rm next}=\rho'
\mid \text{visible change at }\rho
)
\longrightarrow
\frac{Q^{(k)}(\rho,\rho')}{\lambda(\rho)}.
\tag{7.9}
\]

The unconditional probability of a multifurcation or simultaneous visible refinements is \(O_k(\delta_N^2)\). Dividing by (7.6), its conditional probability given a visible change is \(O_k(\delta_N)\to0\).

Thus the next visible jump becomes binary with precisely the CTCS jump kernel.

#### Step 5. Couple the entire finite path

At every matched state, couple the geometric waiting time and the limiting exponential waiting time by a common uniform quantile; by (7.8) the scaled holding times converge.

Couple the finite next-state distributions by a common uniform. By (7.9) and the vanishing bad-transition mass, the next states agree with probability tending to one.

Every visible refinement increases the number of blocks. Starting from one block on \(k\) labels, both processes therefore have at most \(k-1\) visible jumps before absorption into singletons.

Inducting over those at most \(k-1\) jumps and taking a finite union bound gives a coupling on which the complete visible state sequences agree with probability tending to one and all corresponding jump times converge.

For càdlàg paths in a finite discrete state space, this is enough for Skorokhod \(J_1\) convergence. Hence (7.1) holds.

#### Step 6. Projective convergence

Fix \(\eta>0\). Choose \(K\) so that

\[
\sum_{k>K}2^{-k}<\eta/2.
\]

Use the Step-5 coupling for the \([K]\)-restriction. Every smaller restriction is a deterministic restriction of the same \([K]\) path, so all coordinates \(k\le K\) converge simultaneously. The deterministic contribution of \(k>K\) to (2.1) is below \(\eta/2\).

Thus

\[
d_{\rm proj}(\widehat\Pi_N,\Pi)\to0
\]

in probability under the coupling, proving (7.2).

#### Step 7. Recover the tree

For labels \(a,b\), their branchpoint height is the first time at which the partition path separates them. The consistent finite restriction paths record every split and split time. Therefore convergence of the whole exchangeable partition path is convergence of the source's complete CTCS(infinity) genealogical representation, not merely of a tagged fragment.

This completes the proof.

---

## 8. Strict finite non-equivalence of the counted concrete class

The frozen equivalence convention identifies only deterministic leaf relabelings and multiplication of all edge times by one deterministic positive scalar. The concrete class (5.2) is strictly different from the three retained classes under finite distributional invariants.

### 8.1 Against original CTCS and binary HGPF

At \(N=4\),

\[
\alpha_N=\theta_N=\frac18.
\]

For the particular partition of all four labels into four singleton blocks, (4.1) gives

\[
\begin{aligned}
p_{1/8,1/8}(1,1,1,1)
&=
\frac{(1/4)(3/8)(1/2)}
     {(9/8)(17/8)(25/8)}
\\
&=
\boxed{\frac{8}{1275}}>0.
\end{aligned}
\tag{8.1}
\]

Thus the finite Pitman--Yor hierarchy has a degree-four root with positive probability. Original CTCS/DTCS and HGPF are binary. Relabeling and global time rescaling preserve vertex degree, so they cannot identify these models.

### 8.2 Against the ternary Gibbs/Dirichlet class C003

C003 has maximum outdegree \(3\) deterministically. Equation (8.1) gives positive outdegree \(4\) probability here. Therefore C004 is not frozen-equivalent to C003.

### 8.3 Against SC-nCRP C002

Both C002 and C004 can have arbitrarily large finite degree, so use a shape-ratio invariant.

For the positive-discount model at \(N=4\),

\[
\frac{
p_{1/8,1/8}(1,3)
}{
p_{1/8,1/8}(2,2)
}
=
\frac{2-\alpha}{1-\alpha}
=
\boxed{\frac{15}{7}}.
\tag{8.2}
\]

For SC-nCRP at \(N=4\), \(\alpha=0,\theta=1/4\), the same ratio is

\[
\boxed{2}.
\tag{8.3}
\]

A deterministic leaf relabeling preserves split-size classes, and multiplication of all edge times by a constant cannot alter the conditional combinatorial split-shape ratio. Since \(15/7\ne2\), C004 is not frozen-equivalent to C002.

I count all positive-discount sequences satisfying the theorem as **one** Pitman--Yor/Gibbs class. The universal quantifier in C004 is a theorem strength, not metric inflation.

---

## 9. What the three new-method moves accomplished

### Move 1 — change category

Viewing the problem through Bayesian nonparametric species-sampling led from ordinary CRP to its canonical positive-discount Pitman--Yor generalization. This supplies a named external model family with a different reinforcement law and power-law partition behavior.

### Move 17 — look for the numbers somewhere else

The CTCS beta-function rate

\[
B(i,m-i)
\]

appears exactly as the first derivative coefficient of a particular binary partition in the Pitman--Yor EPPF. Simultaneously, \(H_{m-1}\) is the negative first derivative of the one-block probability. These two coefficients identify the whole finite CTCS generator.

### Move 27 — swap the quantifiers

Instead of tuning one ray, the proof shows that **every** positive approach

\[
(\alpha_N,\theta_N)\to(0,0),
\qquad
\delta_N=\alpha_N+\theta_N,
\]

has the same accelerated CTCS tangent. This both simplifies the proof and shows that the limit is robust inside a two-parameter class.

---

## 10. Prior-art and source-intent assessment

This run improves the mathematical metric but does not justify claiming Open Problem 18 closed.

### Known

- Two-parameter Poisson--Dirichlet/Pitman--Yor partitions are classical.
- McCullagh--Pitman--Winkel (2008) already associate multifurcating Gibbs fragmentation trees with this family over a broad parameter range that includes \(\alpha\ge0\).
- Positive-discount Pitman--Yor models are standard in Bayesian nonparametrics; they are not an R11-invented finite model.

### Potentially new / not located in bounded searches

I did not locate the explicit theorem that as \(\alpha,\theta\downarrow0\), raw hierarchical Pitman--Yor refinements accelerated by \(1/(\alpha+\theta)\) converge, as a whole partition-valued path, to Aldous--Janson CTCS(infinity).

### Source-intent warning

C004 is mathematically distinct under the frozen finite-equivalence convention, but it is arguably *less* persuasive as a "superficially different" source-level answer than a model from an unrelated combinatorial domain, because CRP, Pitman--Yor and Gibbs fragmentation are neighboring exchangeable-partition families.

Accordingly:

- the frozen metric moves;
- `R11-I0054-C004` is author-side proved;
- the overall source/campaign label remains **PARTIAL**;
- no paper package is created;
- independent auditors should specifically assess whether this class is sufficiently different for the informal intent of Open Problem 18 and whether the tangent theorem is already implicit in general fragmentation convergence theory.

---

## 11. Independent audit state

Repository search still finds the distinct R10 audit

`R10-AUDIT-R11-I0054-C002-GENERATOR-20260916`

with verdict PASS for the mathematical generator/convergence core of **C002 only**, explicitly excluding prior-art/source-intent clearance.

I found no completed independent audit of C003 or C004, and no P26 end-to-end audit of the I0054 package.

Therefore closure requirements are not met.

---

## 12. Exact finite self-check

Executed exact checker:

`artifacts/R11/2026-09-16T19-40-00Z_i0054-pitman-yor-tangent-a4c2_checker.py`

Creation/readback commit:

`d1b7527c57981d1a065022c9f7b3e9c386d20447`.

Archived clean stdout:

`artifacts/R11/2026-09-16T19-40-00Z_i0054-pitman-yor-tangent-a4c2_checker_output.txt`

Creation/readback commit:

`fc73d64fe9dcd6ee6ff778caed8d1ee14ad35c2a`.

Executed-output SHA-256:

`71c40bd0b43e1c3faf20639877d93b8a72c62a8e1ad62515073ccdc0c2132512`.

The checker uses exact `Fraction` arithmetic and verifies:

1. exact EPPF normalization on 4,620 labelled-partition instances through \(n=7\) for four rational parameter pairs;
2. 1,485 exact first-order directional identities at five approach directions, including the universal one-block derivative, the binary CTCS beta coefficient, and zero first derivative for ternary partitions;
3. the exact CTCS harmonic total-rate identity through \(m=30\);
4. the four-way witness \(8/1275\);
5. the positive-discount shape ratio \(15/7\) versus the Ewens/SC-nCRP ratio \(2\).

The checker explicitly does not prove the asymptotic theorem; Sections 6--7 do.

---

## 13. Metric and status

Under the frozen equivalence convention, the metric moves

\[
\boxed{3\longrightarrow4.}
\]

The four counted classes are:

1. HGPF / C001 — harmonic-grid binary paintbox fragmentation;
2. SC-nCRP / C002 — small-concentration nested ordinary Chinese restaurant process;
3. TDGF / C003 — near-critical fixed-arity ternary Dirichlet/Gibbs fragmentation;
4. **SPYH / C004 — small-parameter positive-discount Pitman--Yor hierarchy**, with the universal positive-quadrant tangent theorem above.

Stable new claim:

`R11-I0054-C004 = PROVED author-side under frozen equivalence`.

Overall source/campaign status:

`PARTIAL`.

The next nonrepeating Section-B triple, if research continues before audits arrive, is:

**8 (discretize), 12 (find what is conserved), 19 (make it an algorithm).**

A high-value next goal is to leave the exchangeable-fragmentation/Gibbs ecosystem entirely: find a finite combinatorial or allocation algorithm whose induced genealogy has the same infinitesimal beta split rates for a structural reason, not because its one-step law was selected from a known partition family.

---

## 14. Structured `ledger_delta`

```yaml
ledger_delta:
  track: R11
  intake: I0054
  source:
    authors: [David J. Aldous, Svante Janson]
    title: "The Critical Beta-splitting Random Tree II: Overview and Open Problems"
    arxiv: "2303.02529v3"
    source_date: "2025-04-18"
    locator: "Open Problem 18, section 6.3"
  target: "A genuinely different discrete tree model whose whole limit object is CTCS(infinity)"
  metric: "number of distinct nontrivial discrete model classes with complete proof of the required CTCS(infinity) limit, modulo deterministic relabeling and global deterministic time rescaling only"
  before: 3
  after: 4
  movement: true
  unchanged_count: 0
  mathematical_status: PARTIAL
  methods: [1, 17, 27]
  claims:
    retained:
      - id: R11-I0054-C001
        model_class: "harmonic-grid paintbox fragmentation (HGPF)"
        status: "PROVED author-side under frozen equivalence"
      - id: R11-I0054-C002
        model_class: "small-concentration nested Chinese restaurant process (SC-nCRP)"
        status: "PROVED author-side under frozen equivalence"
      - id: R11-I0054-C003
        model_class: "near-critical ternary Dirichlet/Gibbs fragmentation (TDGF)"
        status: "PROVED author-side under frozen equivalence"
    new:
      id: R11-I0054-C004
      model_class: "small-parameter positive-discount Pitman-Yor hierarchy (SPYH)"
      status: "PROVED author-side under frozen equivalence; audits/prior-art/source-intent clearance pending"
      concrete_parameters: "alpha_N=theta_N=1/(2N), raw level length=1/N"
      stronger_theorem: "all alpha_N,theta_N>=0 with delta_N=alpha_N+theta_N->0 have the same CTCS tangent after raw-level scaling by delta_N"
      limit: "whole exchangeable-partition path in projective Skorokhod topology"
  exact_evidence:
    - "artifacts/R11/2026-09-16T19-40-00Z_i0054-pitman-yor-tangent-a4c2_checker.py @ d1b7527c57981d1a065022c9f7b3e9c386d20447"
    - "artifacts/R11/2026-09-16T19-40-00Z_i0054-pitman-yor-tangent-a4c2_checker_output.txt @ fc73d64fe9dcd6ee6ff778caed8d1ee14ad35c2a"
    - "checker stdout sha256 71c40bd0b43e1c3faf20639877d93b8a72c62a8e1ad62515073ccdc0c2132512"
  audit_ids:
    existing_scoped:
      - "R10-AUDIT-R11-I0054-C002-GENERATOR-20260916: PASS generator/convergence core only"
    c004: []
    required_missing:
      - "P26 end-to-end audit"
      - "one complete distinct OTHER-track audit of source match / newest package"
  prior_art:
    known_model_family:
      - "McCullagh--Pitman--Winkel (2008), Gibbs fragmentation trees: multifurcating Gibbs trees associated with two-parameter Poisson--Dirichlet models"
      - "Pitman--Yor positive-discount partitions are standard Bayesian nonparametric/species-sampling models"
    bounded_search_result: "no explicit small-positive-parameter accelerated CTCS(infinity) whole-path theorem located"
    novelty_certificate: false
    source_intent_risk: "positive-discount Pitman--Yor remains adjacent to the exchangeable-partition/Gibbs ecosystem"
  ownership:
    repository_claim: "R11 provisional exclusive I0054 reservation; PENDING_ADMISSION not READY"
    competing_owner_found: false
  next_methods: [8, 12, 19]
```
