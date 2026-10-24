Model: GPT-5.6 Sol. Reasoning: UNVERIFIED runtime level; GPT-6 / maximum was requested in prompt text, but the exposed scheduler has no model-family or reasoning-effort selector, so GPT-6 / maximum is not verified or claimed. Metric movement: `11 -> 12` distinct nontrivial discrete model classes with complete author-side proofs under the frozen equivalence convention. Section-B moves actually tried: **#16 (compute every small case), #18 (say it in another language), #26 (hunt the sporadic/boundary case)**.

Problem/source: David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3 (18 April 2025), **Open Problem 18**, intake `I0054`. Overall campaign status remains **PARTIAL**, not CLOSED: the new claim `R11-I0054-C012` below has a complete author-side convergence proof and exact finite self-check, but the source-intent/prior-art judgment and the required P26 plus second OTHER-track end-to-end audits are still absent.

# R11 I0054 — a harmonic Pólya-urn peeling hierarchy with full CTCS(infinity) limit

Run ID: `2026-09-17T03-40-00Z_i0054-harmonic-polya-regenerative-c012-b3e1`
Repository / branch: `yspennstate/math-open-problems` / `master`
Dated source/literature check: 2026-09-17

No Gmail/email, Drive, public posting, purchase, workflow execution, permission change, scheduler change, shared-root edit, or peer-track edit was performed.

---

## 1. Continuity, source, ownership, and control state

I continued from the newest immutable R11 report

`runs/R11/2026-09-17T02-41-27Z_i0054-permutation-cycles-subordinator-u002-c011-7a6e.md`

rather than restarting. That report moved the fixed metric `10 -> 11` and prescribed the nonrepeating method triple `#16/#18/#26`, which is the triple actually used here.

Before new mathematics I read or searched:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and the current owner directive;
- `operations/claims/I0054.md`;
- targeted I0054/intake/source hits and the retained R11 history;
- the newest neighbouring P13/I0051 clade report, `proofnet24/P13-closure-clades/runs/2026-09-16/2026-09-16_19-04-03__run-report.md`;
- repository-wide I0054/audit searches.

The current claim file still records R11 as the provisional exclusive owner of I0054 and still says `PENDING_ADMISSION, not READY`. `QUEUE.md` still lists I0054 as a closable candidate, and the posted/settled indexes do not list Open Problem 18 as closed or posted. P13 remains on the distinct Open Problem 9 clade-covariance problem and is not reassigned here. The old planar-SAW route remains retired from this slot with its immutable earlier reports preserved.

The repository's compact shared `RESULTS.md` still contains an old R-series placeholder row for the former SAW assignment and explicitly warns that newer complete reports must be recovered before replacing old values. I therefore preserve the actual R11 baseline from the immutable current-target report: metric 11, status PARTIAL.

### Model/runtime control

This worker actually identifies as **GPT-5.6 Sol**; reasoning level is **UNVERIFIED**. The exposed automation interface offers prompt/title, schedule, enablement, and timing mode. It exposes no model-family selector and no reasoning-effort selector. Thus “GPT-6 / maximum” remains a prompt request only.

The current operations record also preserves the fact that `You cannot modify this task` errors are permission/context dependent: some native jobs, including P26, were later editable from an authorized context after denial elsewhere, while the R-series edits were rejected in another context. The legitimate remedy is an authorized task/account/workspace-owner interface that owns the native job and exposes those controls, or a platform/support change. Cloning or bypassing a denied task is not an acceptable workaround. This run made no scheduler modification.

---

## 2. Exact source target and topology

The current v3 PDF, dated 17/18 April 2025, says in Section 6.3:

> Open Problem 18 Are there superficially different discrete models whose limit is the same CTCS(infinity)?

and immediately explains that the characteristic feature to look for may be the subordinator approximation.

The limiting object is not merely a tagged-leaf law. Aldous--Janson Part III formalizes `CTCS(infinity)` as the entire consistent exchangeable partition process
\[
(\Pi(t),t\ge 0)
\]
on `N`, where two labels remain in the same block until their branchpoint time. Its finite restriction to `[k]` is a finite-state homogeneous fragmentation.

For a current visible block `C` of size `b>=2` and a particular unordered nontrivial split
\[
A\mid C\setminus A,\qquad |A|=i,\quad |C\setminus A|=j=b-i,
\]
the CTCS generator rate is
\[
\boxed{
q_b(A\mid C\setminus A)=B(i,j)
=\frac{(i-1)!(j-1)!}{(b-1)!}.
}
\tag{2.1}
\]
Summing over all unordered nontrivial splits of a `b`-block gives
\[
\frac12\sum_{i=1}^{b-1}\binom bi B(i,b-i)=H_{b-1}.
\tag{2.2}
\]

As in the preceding R11 reports, convergence below is proved in the projective finite-restriction Skorokhod topology, for example with
\[
d_{\rm proj}(\omega,\eta)
=
\sum_{k\ge1}2^{-k}
\bigl(1\wedge d_{J_1,k}(\omega^{[k]},\eta^{[k]})\bigr),
\tag{2.3}
\]
where the finite-state `J_1` metrics are taken on the partition-valued restrictions. Thus the claim is a whole-genealogy convergence theorem, not a one-dimensional marginal limit.

---

## 3. Current literature and prior attempts

A dated current-literature screen was repeated on 2026-09-17.

Primary/current items checked include:

1. Aldous--Janson, arXiv:2303.02529v3, whose Section 6.3 and Appendix E still list Open Problem 18.
2. Aldous--Janson Part III, arXiv:2412.09655, which gives the exchangeable-partition representation and binary dislocation measure `dx/[x(1-x)]` on `[1/2,1)`.
3. Iksanov--Nikitin--Yakymiv, *An infinite balls-in-boxes approach to the critical beta-splitting tree: some central limit theorems*, Electron. Commun. Probab. 31 (2026), article 15, DOI `10.1214/26-ECP766`. That paper explicitly develops the Iksanov connection between critical beta-splitting leaf heights, a subordinator, and an infinite balls-in-boxes/occupancy model.
4. Gnedin--Pitman, *Regenerative Composition Structures* and *Regenerative partition structures*, for the general subordinator/regenerative-composition language.
5. Chorbadzhiyska--Minchev--Savov, arXiv:2608.18320 (18 August 2026), which treats the beta-splitting family via homogeneous fragmentations and regenerative-composition methods and resolves a height-related Aldous--Janson open problem, not Open Problem 18.
6. Heng Ma's 13 September 2026 papers arXiv:2609.14325 and arXiv:2609.14329. The latter explicitly resolves Aldous--Janson Open Problem 4 (discrete tree height); the former studies extremal separation times and clade-count dynamics. Neither advertises a different finite discrete model converging to CTCS(infinity).

Targeted searches included combinations of `critical beta-splitting`, `CTCS`, `Pólya urn`, `Polya urn`, `regenerative composition`, `balls-in-boxes`, `discrete model`, and `Open Problem 18`. I found the classical tagged/subordinator and occupancy connections above, but did not locate the full finite hierarchy constructed below or a theorem that its complete exchangeable-partition genealogy converges to CTCS(infinity).

This is a **bounded negative search, not a novelty certificate**. The subordinator, regenerative-composition machinery, beta-binomial/Pólya-urn representation, and the geometric-series identity used below are classical. The potentially new item is the particular finite hierarchy and its full partition-process convergence argument.

---

## 4. Move #18 — translate the CTCS subordinator into harmonic Pólya channels

The most useful clue is the exact tagged-fragment subordinator already displayed in the source. Its Lévy density is
\[
\kappa_Y(dy)
=
\frac{e^{-y}}{1-e^{-y}}\,dy,\qquad y>0.
\tag{4.1}
\]

Put
\[
U=e^{-Y}\in(0,1).
\]
Since `dy=du/u` in absolute value, (4.1) becomes
\[
\boxed{
\kappa_U(du)=\frac{du}{1-u}.
}
\tag{4.2}
\]
Now use the elementary but decisive spectral decomposition
\[
\frac1{1-u}
=
\sum_{r=1}^\infty u^{r-1}.
\tag{4.3}
\]
The density `r u^{r-1}` is `Beta(r,1)`. Therefore (4.2) can be read as:

> channel `r` rings at rate `1/r`; when it rings, sample a `Beta(r,1)` survival fraction.

That already converts the continuous subordinator into countably many elementary channels. The further step is to make **every finite model discrete**: a `Beta(r,1)` paintbox on finitely many labels is exactly the two-color Pólya urn with `r` initial “stay” balls and one initial “peel” ball.

For a fixed assignment of `s` nonanchor labels to “stay” and `d` labels to “peel”, this urn gives
\[
\Pr_r(\text{that assignment})
=
\frac{(r)_s(1)_d}{(r+1)_{s+d}}
=
rB(r+s,d+1).
\tag{4.4}
\]
Thus no continuous beta variable is required in the definition of the finite model. The beta variable is only a proof representation of a standard discrete Pólya urn law.

This is the route that was missing from the preceding examples: it translates the authors' tagged subordinator hint through regenerative-composition/occupancy language and back into a genuinely discrete hierarchical urn process.

---

## 5. Definition of C012: harmonic-channel Pólya-urn peeling hierarchy

For each global size `N>=2`, set
\[
R_N=N,\qquad \delta_N=N^{-3}.
\tag{5.1}
\]

Start from one block `[N]`. At each raw generation, update every current nonsingleton block `B` independently as follows.

### One block update

Let `m=|B|`.

1. Choose a uniform **anchor** `a` in `B`.
2. For each channel `r=1,\ldots,R_N`, independently activate channel `r` with probability
   \[
   p_{N,r}=\frac{\delta_N}{r}.
   \tag{5.2}
   \]
3. Give all active channels independent continuous priorities and process them in priority order. (The priorities only generate a uniform random order and can equivalently be generated by a random permutation of the active channels.)
4. Suppose the current survivor block containing the anchor is `S`. At active channel `r`, run a two-color Pólya urn with `r` initial stay balls and one initial peel ball, once for each label of `S\setminus\{a\}`. Labels drawing peel form `D`; labels drawing stay remain with the anchor. If `D` is nonempty, record `D` as a child and remove it from `S`.
5. After all active channels, the final survivor set `S` containing the anchor is the last child.

All children recorded in one raw generation are viewed as the simultaneous refinement of `B`. A raw generation has physical duration
\[
\delta_N.
\tag{5.3}
\]

Because more than one channel can activate, the finite model is genuinely multifurcating. It is not an Euler sampler with an imposed CTCS binary transition.

Every nonsingleton block has positive probability of a proper peel in every generation, so the finite hierarchy absorbs into singletons almost surely.

Call this class the **harmonic Pólya-urn peeling hierarchy**, `C012`.

---

## 6. Move #16 — exact small cases reveal the beta telescoping identity

Before doing an asymptotic proof, I computed the finite channel laws symbolically.

Let a visible sampled block `C` have size `b`, with a specified split
\[
A\mid A^c,\qquad |A|=i,\quad |A^c|=j=b-i.
\]
Suppose `C` lies inside a hidden current block `B` of size `m>=b`.

Consider first a raw step with exactly one active channel `r`. There are three anchor cases.

### 6.1 Anchor lies in `A`

The other `i-1` visible labels of `A` must stay and the `j` visible labels of `A^c` must peel. By (4.4), after multiplying by the channel activation coefficient `1/r`, the rate coefficient is
\[
B(r+i-1,j+1).
\]
Summing channels `r=1,\ldots,R`,
\[
\sum_{r=1}^{R}B(r+i-1,j+1)
=
\boxed{B(i,j)-B(i+R,j)}.
\tag{6.1}
\]

### 6.2 Anchor lies in `A^c`

Similarly,
\[
\sum_{r=1}^{R}B(r+j-1,i+1)
=
\boxed{B(i,j)-B(j+R,i)}.
\tag{6.2}
\]

### 6.3 Anchor is hidden

Now either the visible labels in `A` peel and `A^c` stay, or vice versa. The summed coefficient is
\[
\boxed{
B(j+1,i)-B(j+R+1,i)
+
B(i+1,j)-B(i+R+1,j).
}
\tag{6.3}
\]
The infinite-`R` part collapses because
\[
B(j+1,i)+B(i+1,j)
=
B(i,j).
\tag{6.4}
\]

The finite telescoping identity behind (6.1)--(6.3) is
\[
\boxed{
\sum_{r=1}^{R}B(a+r-1,c+1)
=
B(a,c)-B(a+R,c).
}
\tag{6.5}
\]
It follows either from the beta integral and the finite geometric sum or directly from
\[
B(x,y)-B(x+1,y)=B(x,y+1).
\]

The exact checker verifies (6.5) on a broad integer grid and verifies the Pólya normalization before any asymptotic inference is made.

---

## 7. Exact hidden-label projection

Average (6.1)--(6.3) over the uniform anchor. The probability the anchor is in `A`, in `A^c`, or hidden is respectively
\[
\frac{i}{m},\qquad\frac{j}{m},\qquad\frac{m-b}{m}.
\]

Define the coefficient `q_R(m,b,i)` for a particular visible split under the one-channel first-order kernel. Then
\[
\boxed{
\begin{aligned}
q_R(m,b,i)
={}&B(i,j)
-\frac{i}{m}B(i+R,j)
-\frac{j}{m}B(j+R,i)\\
&-\frac{m-b}{m}
\bigl[
B(j+R+1,i)+B(i+R+1,j)
\bigr].
\end{aligned}
}
\tag{7.1}
\]

This formula is the main invariant of the run.

First, all four subtracted terms are nonnegative, so
\[
q_R(m,b,i)\le B(i,j).
\]
Second, for positive integer arguments
\[
B(R+a,c)\le \int_0^1u^{R+a-1}\,du\le \frac1{R+1}.
\]
The anchor weights multiplying the four tails sum to at most `2`, hence uniformly over **every hidden size `m>=b`**
\[
\boxed{
0\le B(i,j)-q_R(m,b,i)\le \frac{2}{R+1}.
}
\tag{7.2}
\]
Therefore
\[
\boxed{
q_R(m,b,i)\longrightarrow B(i,b-i)
}
\tag{7.3}
\]
uniformly in the hidden block size.

This hidden-size uniformity is what upgrades the tagged subordinator idea to the whole sampled genealogy.

---

## 8. Move #26 — the endpoint singleton split is the genuine truncation bottleneck

The exact small-case data showed a sharp boundary effect rather than an accidental finite anomaly.

For the two-label visible block,
\[
b=2,\qquad i=j=1,\qquad m=b,
\]
(7.1) gives the exact truncation deficit
\[
\boxed{
B(1,1)-q_R(2,2,1)=\frac1{R+1}.
}
\tag{8.1}
\]
Thus no finite channel cutoff `R` gives the exact CTCS rate, and the convergence cannot be improved beyond order `1/R` uniformly over all visible split shapes.

By contrast, if both sides have size at least `2`, every beta tail in (7.1) is `O(R^{-2})`; the exact checker verifies the simple uniform finite-grid inequality
\[
B(i,j)-q_R(m,b,i)
\le
\frac{4}{(R+1)(R+2)}
\quad(i,j\ge2)
\tag{8.2}
\]
over the tested range, while the factorial beta formula gives the general `O_{b}(R^{-\min(i,j)})` behavior.

So the slow approximation is genuinely concentrated on the sporadic boundary class of singleton-vs-rest splits. This is useful information for any future faster discrete approximation of the CTCS dislocation law.

---

## 9. One-step kernel comparison with CTCS

Fix a restriction `[k]` and condition on the **complete hidden history** up to one raw generation. Every visible block is contained in a unique hidden block.

For one hidden block, the total channel activation mass is
\[
\sum_{r=1}^{R}\frac{\delta}{r}
=
\delta H_R.
\tag{9.1}
\]
By a union bound over active channel pairs,
\[
\Pr(\text{at least two channels activate})
\le
\frac12\delta^2H_R^2.
\tag{9.2}
\]

Moreover, for a fixed channel `r`,
\[
\left|
\Pr(\text{only channel }r\text{ activates})
-\frac{\delta}{r}
\right|
\le
\frac{\delta}{r}\,\delta H_R.
\]
Summing over `r` gives a total one-channel-vs-categorical discrepancy at most
\[
\delta^2H_R^2.
\tag{9.3}
\]

A single active channel produces at most one visible binary split in each hidden block. Multiple visible jumps, multifurcations produced by sequential peels, or nonlinear interactions require at least two active channels and are therefore covered by (9.2).

Combining (7.2), (9.2), and (9.3), and noting that a `[k]` restriction touches at most `k` hidden blocks, yields a constant `C_k<infinity` such that, uniformly over the complete hidden filtration,
\[
\boxed{
\sup_{\rho}
\left\|
P_{N}^{(k)}(\rho,\cdot)
-
\bigl(I+\delta_N Q^{(k)}\bigr)(\rho,\cdot)
\right\|_{\rm TV}
\le
C_k
\left(
\frac{\delta_N}{R_N+1}
+
\delta_N^2H_{R_N}^2
\right).
}
\tag{9.4}
\]

Here `Q^{(k)}` is the exact finite CTCS generator with particular split rates (2.1). Diagonal entries follow by row sums.

For the concrete choice
\[
R_N=N,\qquad \delta_N=N^{-3},
\]
the right side is
\[
O_k(N^{-4})+O_k(N^{-6}\log^2N)
\]
per raw step.

---

## 10. Full finite-restriction path convergence

Let
\[
K_N^{(k)}=I+\delta_NQ^{(k)}.
\]
For fixed `k` and all sufficiently large `N`, this is a stochastic matrix because the finite CTCS state space has bounded exit rate.

Use conditional maximal coupling at each raw generation between the actual `[k]` restriction and the Euler chain `K_N^{(k)}`. Up to a fixed physical time `T`, there are at most `T/\delta_N+1` generations. Therefore (9.4) gives
\[
\Pr(\text{coupling fails by time }T)
\le
C_{k,T}
\left(
\frac1{R_N+1}
+
\delta_NH_{R_N}^2
\right)
+o(1).
\tag{10.1}
\]
For `R_N=N`, `delta_N=N^{-3}`,
\[
\frac1{R_N+1}
+
\delta_NH_{R_N}^2
\longrightarrow0.
\tag{10.2}
\]

It remains only to identify the Euler limit. At visible state `rho`, write
\[
\lambda(\rho)=-Q^{(k)}(\rho,\rho).
\]
The Euler chain waits a geometric number `G_N` of raw steps with parameter
\[
\delta_N\lambda(\rho),
\]
so
\[
\delta_NG_N
\Longrightarrow
{\rm Exp}(\lambda(\rho)).
\tag{10.3}
\]
Conditioned on jumping,
\[
\Pr(\rho\to\rho')
=
\frac{Q^{(k)}(\rho,\rho')}{\lambda(\rho)},
\tag{10.4}
\]
exactly the CTCS jump chain.

A fragmentation of `k` labels makes at most `k-1` visible proper refinements before absorption. Thus the entire sequence of jump states and holding times can be coupled, giving
\[
\boxed{
\widehat\Pi_N^{[k]}
\Longrightarrow
\Pi_{\rm CTCS}^{[k]}
}
\tag{10.5}
\]
in Skorokhod `J_1`, for every fixed `k`.

Finally, use the projective metric (2.3). For a given error tolerance choose `K` so that the deterministic coordinate tail `sum_{k>K}2^{-k}` is small, then use the coupling for the finite set of restrictions up to `K`. Therefore
\[
\boxed{
\widehat\Pi_N
\Longrightarrow
\Pi_{\operatorname{CTCS}(\infty)}
}
\tag{10.6}
\]
for the complete exchangeable-partition genealogy.

This is the required source-level convergence object, not a tagged-leaf marginal.

---

## 11. The subordinator is recovered exactly from the channel language

The construction also explains the source's heuristic at the one-spine level without using it as a substitute for the full proof.

If one follows the anchor/tagged survivor, channel `r` has first-order intensity `1/r`, and its latent survival factor is `U_r~Beta(r,1)`. Hence the first-order survival-factor intensity is
\[
\sum_{r\ge1}\frac1r\,[r u^{r-1}\,du]
=
\sum_{r\ge1}u^{r-1}\,du
=
\frac{du}{1-u}.
\]
Under `y=-log u`, this becomes
\[
\frac{e^{-y}}{1-e^{-y}}\,dy,
\]
exactly the Aldous--Janson tagged CTCS Lévy density.

Thus the model arose by **discretizing the Lévy spectrum into Pólya urn channels**, while Sections 7--10 prove that the entire genealogy, not only the tag, converges.

---

## 12. Exact finite non-equivalence certificate

The finite model is not just a rescaling or relabelling of the original binary CTCS/DTCS model.

At `N=3`,
\[
R=3,\qquad\delta=\frac1{27}.
\]
Fixing the uniform anchor leaves two nonanchor labels.

For an ordered list of active channels `r_1,\ldots,r_\ell`, the beta representation of the Pólya urn gives independent `U_t~Beta(r_t,1)`. A nonanchor label is peeled first at channel `t` with conditional mass
\[
p_t=(1-U_t)\prod_{h<t}U_h,
\]
and survives with the anchor with mass
\[
q=\prod_tU_t.
\]
The two nonanchor labels form two different peeled children precisely when they are both peeled but not in the same channel. Conditional probability:
\[
(1-q)^2-\sum_tp_t^2.
\tag{12.1}
\]

Averaging (12.1) exactly over all active subsets of `{1,2,3}`, their activation probabilities `delta/r`, and the uniform channel order gives
\[
\boxed{
P(\text{raw degree-3 root refinement})
=
\frac{21521}{127545840}.
}
\tag{12.2}
\]
The exact no-visible-split probability is
\[
\boxed{
P(\text{no visible split})
=
\frac{3406559}{3542940}.
}
\tag{12.3}
\]
Therefore, after suppressing waiting generations,
\[
\boxed{
P(\deg(\text{first visible root})=3)
=
\frac{21521}{4909716}
\approx0.00438334926093.
}
\tag{12.4}
\]

The retained degree-three witnesses from the prior R11 classes are

\[
\begin{array}{c|c}
\text{class}&P(\deg(\text{first visible root})=3)\text{ at }N=3\\ \hline
C001&0\\
C002&1/10\\
C003&1/22\\
C004&1/6\\
C005&1/728\\
C006&1/7\\
C007&1/71\\
C008&1/71\\
C009&0\\
C010&0\\
C011&2/105\\
C012&21521/4909716
\end{array}
\]
(`C007` and `C008` were already separated from each other by their retained `N=4` witness.)

The C012 value differs from every previous value. Root degree distribution is unchanged by deterministic label relabelling or global branch-length rescaling. Hence C012 is a genuinely distinct finite class under the frozen equivalence convention.

Therefore the fixed metric moves
\[
\boxed{11\longrightarrow12}.
\]

Stable author-side mathematical label:
\[
\boxed{\texttt{R11-I0054-C012 = PROVED under frozen equivalence}.}
\]

---

## 13. Why this class is more source-facing than another inverse-profile compiler

Several preceding R11 examples obtained the beta kernel by explicitly correcting a discrete skeleton's size profile. C012 is different in mechanism.

- It starts from the **source's own subordinator hint**.
- The harmonic channel rates `1/r` are forced by the geometric-series decomposition of the exact CTCS Lévy density.
- Each channel is realized by a classical **discrete Pólya urn**, not by assigning a hand-chosen edge weight.
- The modern balls-in-boxes/regenerative-composition literature already shows that this subordinator has a natural discrete occupancy interpretation for tagged heights.
- The new step is to lift those channels to a full recursive labelled hierarchy and prove the uniform hidden-label projection needed for whole-tree convergence.

That makes C012 a stronger candidate for the authors' informal word “superficially different” than a purely profile-corrected tree. But that phrase is intentionally informal, and the construction is still mathematically reverse-engineered from the CTCS subordinator. I therefore do not upgrade the source itself to CLOSED without independent source-intent review.

---

## 14. Exact finite self-check

New substantive artifacts:

- `artifacts/R11/2026-09-17T03-40-00Z_i0054-polya-regenerative-c012_checker.py`
  - creation commit `5c426429afd2f597b5bee722e6803d598be56240`
  - local SHA-256 `2f40e599383b90fb04b5a186c20334f838b369e1e555ce2a20a99b9ed2b8561b`
- `artifacts/R11/2026-09-17T03-40-00Z_i0054-polya-regenerative-c012_checker.out`
  - creation commit `08e93b323d82cb1385cc3e6c6776a4eea3de9878`
  - local SHA-256 `2c4fa2dc368c6600e7bf992d2206e6d3d507a66a0024967810a24d35ea6f98f5`

The checker records **24,782 exact rational checks**, including:

- Pólya-urn normalization and exact beta-binomial representation;
- the beta telescoping identity (6.5);
- the direct channel sum versus the closed hidden-label projection (7.1);
- the uniform truncation bound (7.2);
- the CTCS harmonic total-rate identity;
- the exact singleton boundary deficit `1/(R+1)`;
- faster balanced-split truncation on a broad exact grid;
- the complete `N=3` no-split and degree-three witness calculation;
- separation of the new witness from every retained previous witness;
- the chosen dyadic approximation/error scale.

The archived output ends

`ALL_EXACT_CHECKS_PASS`.

This is explicitly a **self-check**. It certifies the finite algebra and witness; it does not replace the written asymptotic coupling proof in Sections 9--10.

---

## 15. Audit and closure status

A fresh repository audit search still finds scoped R10 passes for older C002--C007 components. It does not find:

- a P26 end-to-end audit of the current I0054 package;
- a second independent OTHER-track end-to-end audit;
- an independent C011 audit;
- an independent C012 audit.

Accordingly:

- `C012` is **PROVED author-side** under the frozen convention;
- the fleet/source status remains **PARTIAL**;
- no `paper_<name>/` package is created;
- Open Problem 18 is **not** called CLOSED.

The canonical I0054 claim file also remains `PENDING_ADMISSION, not READY`; this worker does not edit that coordinator-owned control file.

---

## 16. What the three methods actually did

### #16 — COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE

Exact small `R,b,i,m` computations exposed the telescoping beta identity, the hidden-size cancellation, the exact singleton deficit `1/(R+1)`, and the new `N=3` degree-three witness. This moved the metric.

### #18 — SAY IT IN ANOTHER LANGUAGE

The CTCS tagged subordinator was translated into regenerative-composition/occupancy language:
\[
\frac{e^{-y}}{1-e^{-y}}dy
\leftrightarrow
\frac{du}{1-u}
=
\sum_{r\ge1}u^{r-1}du.
\]
Each term is a `1/r`-rate `Beta(r,1)` channel, and each finite beta-binomial paintbox is exactly a two-color Pólya urn. This produced the new discrete model.

### #26 — HUNT THE SPORADIC CASE

The exceptional boundary split `1|(b-1)` is exactly where finite channel truncation is slow. The simplest `b=2` case has deficit exactly `1/(R+1)`, while balanced splits decay at least quadratically in `R`. This identified the actual approximation bottleneck rather than hiding it inside an `o(1)` term.

---

## 17. Next nonrepeating research moves

The next triple should not repeat `#16/#18/#26`. I record:

- **#6 — deform to a point you can solve:** vary the harmonic channel spectrum away from `1/r` and classify which deformations still have CTCS as first-order limit after one scalar renormalization;
- **#21 — ask who else has this shape:** search species-sampling, preferential-allocation, split-merge, and population-genetics urn mechanisms for the same harmonic spectrum without reverse-engineering it from CTCS;
- **#30 — one scale at a time:** replace the hard cutoff `R_N=N` by sparse/dyadic channel sets and determine the minimal channel complexity needed for full CTCS convergence.

The highest-value next objective is a **naturally occurring urn/allocation model** in which the `1/r` channel spectrum is intrinsic, rather than chosen because it expands the CTCS Lévy density.

---

```yaml
ledger_delta:
  track: R11
  intake: I0054
  source: "Aldous--Janson, arXiv:2303.02529v3, Open Problem 18, Section 6.3"
  target: "genuinely different discrete models with the full CTCS(infinity) exchangeable-partition limit"
  metric_name: "number of distinct nontrivial discrete model classes with a complete source-topology convergence proof under the frozen equivalence convention"
  before: 11
  after: 12
  movement: true
  new_claim: R11-I0054-C012
  new_class: "harmonic-channel Polya-urn peeling hierarchy"
  mathematical_status: "PROVED author-side under frozen equivalence"
  campaign_status: PARTIAL
  source_closed: false
  admission_status: "PENDING_ADMISSION, not READY"
  unchanged_count: 0
  methods_used: [16, 18, 26]
  next_methods: [6, 21, 30]
  finite_checker: "artifacts/R11/2026-09-17T03-40-00Z_i0054-polya-regenerative-c012_checker.py"
  finite_output: "artifacts/R11/2026-09-17T03-40-00Z_i0054-polya-regenerative-c012_checker.out"
  exact_checks: 24782
  audit_status:
    p26_end_to_end: missing
    second_other_track_end_to_end: missing
    c012_independent: missing
  prior_art_status: "bounded dated search; regenerative compositions, balls-in-boxes, Polya/Beta-binomial and CTCS subordinator are known; no full C012 hierarchy/whole-path theorem located"
  topology: "projective finite-restriction Skorokhod J1 for the complete exchangeable partition process"
  scheduler_model_selector: absent
  scheduler_reasoning_selector: absent
  actual_model: "GPT-5.6 Sol"
  actual_reasoning: UNVERIFIED
```
