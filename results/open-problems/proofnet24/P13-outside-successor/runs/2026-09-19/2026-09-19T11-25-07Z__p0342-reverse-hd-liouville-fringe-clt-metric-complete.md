Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. MOVEMENT: `M_P0342 = 1/2 -> 2/2`; the remaining frozen `FRINGE` obligation is proved for the same single functional `Theta=Psi+Phi`, so both source-faithful obligations are now established on P13's page. Campaign closure remains pending the required independent audits and final prior-art gate. Methods actually tried: B1, B11, B25.**

# P13 / P0342 — reverse-HD Liouville theorem, leaf-fringe ergodicity, and positive-variance fringe CLT

UTC run time: 2026-09-19T11:25:07Z  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Native slot: `6aa7b253b37c8191b693d8dc79298d37`  
Own root: `proofnet24/P13-outside-successor/`

## 1. Continuity, ownership, exclusions, and recovered baseline

I continued the current exclusive P13 successor `P0342`; I did not restart a stale scheduler title.

The controlling canonical claim is

`operations/claims/P0342.md`.

It names this exact native slot and freezes one functional `Theta=Psi+Phi` and one denominator-two metric. The immediately preceding immutable P13 report is

`proofnet24/P13-outside-successor/runs/2026-09-19/2026-09-19T10-04-09Z__p0342-finite-failure-density-reduction-movement.md`.

That report proved the `FINITE-FAILURE` obligation and moved the metric

`M_P0342 : 0/2 -> 1/2`.

Its exact remaining obligation was the positive-variance `FRINGE` CLT, reduced there to one density law for complete size-three clades in the stationary fringe process. The previous method triple was B3/B18/B30, so it is not repeated here.

The former P13 I0051 / Aldous--Janson Open Problem 9 clade-covariance target remains **RETIRED** and was not reopened. C0021 reached its mandated six-unchanged-run terminal handoff and was not reopened. The owner's mandatory first-successor lead I0054 remains exclusively occupied by R11. The newest R11 report recovered before this research is

`runs/R11/2026-09-19T10-42-39Z_i0054-positive-compact-u045-c066-a91c.md`,

which moves R11's own author-side metric `65 -> 66` and explicitly keeps I0054 PARTIAL at source/campaign level. P13 did not touch I0054 or any peer claim.

I reread the controlling new-methods policy, campaign INDEX/RANKING, root POSTED/RESULTS/QUEUE, the P0342 claim and predecessor, the newest relevant R11 neighbor, and repository searches for P0342 ownership/audits before the proof below. No shared-root ledger or peer file is modified by this run.

## 2. Exact source and fresh status check, 2026-09-19 UTC

Source: David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3 (v3 dated 18 April 2025), Open Problem 12, §4.10, printed p.44 and list p.68.

Primary URLs checked:

- https://arxiv.org/abs/2303.02529v3
- https://arxiv.org/pdf/2303.02529v3
- https://arxiv.org/abs/2412.09655
- https://arxiv.org/pdf/2412.09655
- https://www.stat.berkeley.edu/~aldous/Papers/me52.pdf

The source states Open Problem 12 in the literal form: if a CLT is known for a given functional along the stationary fringe process, must the CLT also hold for the corresponding DTCS(n) leaf sum? On printed p.44 the source labels the leaves by `Z`, re-roots at leaf `i` to obtain a stationary process `(T_i)`, and says only that “arguing as in [3] one could show that this fringe process is ergodic.” That sentence is not a supplied proof; the proof below fills exactly that missing input for this model.

The required page-image checks succeeded this run: I visually inspected source printed p.44, Part III printed pp.24--25, and Aldous (1991) pp.252 and 262. Thus there is no source-PDF screenshot failure in this invocation.

Later author paper: Aldous--Janson, *The Critical Beta-splitting Random Tree III: The exchangeable partition representation and the fringe tree*, arXiv:2412.09655. Its Theorem 3.1 gives the occupation limits

\[
a(i)=\lim_{n\to\infty} a(n,i)
 = \frac{6H_{i-1}}{\pi^2(i-1)},\qquad i\ge2,
\qquad a(1)=1,
\tag{2.1}
\]

where `a(n,i)` is the probability that the downward harmonic-descent chain started at `n` ever visits `i`. Its Theorem 5.1 gives the reverse-HD fringe construction: if `Q=q^up`, then

\[
Q(i,j)=\frac{a(j)}{a(i)}q^*(j,i),\qquad i<j,
\tag{2.2}
\]

and at each upward transition `i -> j` an independent `DTCS(j-i)` sibling clade is attached, independently across steps, on a fair random left/right side. The downward discrete HD kernel is

\[
q^*(m,i)=\frac{1}{H_{m-1}(m-i)},\qquad 1\le i<m.
\tag{2.3}
\]

The same paper's §5.3 says that a typical fringe leaf belongs to a size-`i` clade with probability `a(i)`.

Classical bridge: David Aldous, *Asymptotic Fringe Distributions for General Families of Random Trees*, Ann. Appl. Probab. 1 (1991), 228--266. Proposition 12 says that a Markov kernel has no nonconstant bounded harmonic functions iff chains from every two starting states admit a shift-coupling. Theorem 13 says that if the ancestor chain in a reduced Markov description of an invariant sin-tree has that property, the invariant sin-tree law is extreme. Section 7.3 explicitly says ordered trees are handled by marks, so the left/right structure used here is within that framework.

Fresh bounded queries included exact combinations of `Open Problem 12`, `fringe process`, `critical beta-splitting`, `ergodic`, `reverse HD`, `shift coupling`, and `harmonic descent`, as well as the later author and citing papers. I recovered Brandenberger--Chin--Mossel, arXiv:2505.24821, which proves finite-DTCS clade-count CLTs, and Chorbadzhiyska--Minchev--Savov, arXiv:2608.18320 (18 August 2026), which resolves a different critical-beta open problem. I did **not** find a checked later primary source explicitly resolving Open Problem 12 or stating the reverse-HD Liouville argument below. This is bounded negative evidence only, not a worldwide openness or novelty certificate.

## 3. Frozen witness and exact surviving obligation

The canonical claim freezes

\[
\Theta=\Psi+\Phi.
\]

`Phi` is the historical bounded continuous global finite-tree perturbation from

`probability_campaign_2026_09/codex_20h_20260906/proofs/P0342_beta_tree_fringe_transfer_scope_counterexample.md`.

For a finite tree with `n>=9`, with `R_n` the smaller original root-clade size, `r_n=floor(sqrt(n))`,

\[
B_n=1_{\{R_n\le r_n\}},\qquad
p_n=P(B_n=1),
\]

and

\[
\Phi(T)=n^{-1/4}(B_n(T)-p_n),
\]

while `Phi=0` on infinite fringe trees (and on the small finite cases as fixed historically).

`Psi` is the bounded local size-three orientation mark: for a distinguished leaf it is `+1` if that leaf is the singleton **left** child in a size-three clade, `-1` if it is the singleton **right** child, and `0` otherwise.

The denominator-two metric is frozen:

1. `FRINGE`: the centered stationary fringe sums of this same `Theta` have a `sqrt(m)` Gaussian CLT with strictly positive limiting variance;
2. `FINITE-FAILURE`: the centered finite `DTCS(n)` sums do not have that same CLT.

The preceding run proved item 2 and left item 1 equivalent to

\[
\frac{K_m}{m}\xrightarrow{p}\lambda_3,
\qquad
\lambda_3=\frac{3}{2\pi^2},
\tag{3.1}
\]

where `K_m` counts complete size-three clades contained in fringe leaves `0,...,m-1`.

This run does not rename the metric or change the witness.

## 4. B1 — change category: from a fringe CLT to Liouville theory

The previous report reduced the probabilistic CLT to an empirical density. Instead of estimating pair covariances directly, B1 changes category twice:

`clade-density LLN -> leaf-shift ergodicity -> extremality of a vertex-Palm sin-tree -> Liouville/shift-coupling of the reverse HD ancestor kernel`.

The key gain is that the only quantitative input needed for the Liouville step is already a proved source theorem, the pointwise occupation convergence `a(n,i)->a(i)`.

## 5. B11/B25 — reverse-HD overshoots forget the starting state

For integers `l>=i`, write

\[
a(l,i):=P_l^{\downarrow}(\text{the downward HD chain ever hits }i).
\]

Thus Theorem 3.1 gives, for every fixed `i`,

\[
a(l,i)\longrightarrow a(i)>0
\quad(l\to\infty).
\tag{5.1}
\]

Let `(Y_r)` be the upward chain with transition kernel `Q` in (2.2).

### Lemma 1 (exact path-reversal hitting identity)

For `1<=i<=l`,

\[
P_i^{\uparrow}(\text{ever hit }l)
=\frac{a(l)}{a(i)}a(l,i).
\tag{5.2}
\]

#### Proof

For `l=i` both sides are one. For `l>i`, sum over all strictly increasing finite paths

\[
i=x_0<x_1<\cdots<x_r=l.
\]

Using (2.2), the probability of such an upward path is

\[
\prod_{s=1}^r Q(x_{s-1},x_s)
=
\prod_{s=1}^r
\frac{a(x_s)}{a(x_{s-1})}q^*(x_s,x_{s-1})
=
\frac{a(l)}{a(i)}
\prod_{s=1}^r q^*(x_s,x_{s-1}).
\]

The factors in the final product are exactly the probability of the reversed strictly decreasing HD path from `l` to `i`. Because the downward chain is strictly decreasing, summing over all reversed paths ending at `i` gives precisely `a(l,i)`. This proves (5.2). `square`

For `N>i` define the first upward crossing

\[
\tau_N:=\inf\{r:Y_r\ge N\}.
\]

Since the chain increases by at least one each step, `tau_N<=N-i` almost surely. Let

\[
\mu_i^N(k):=P_i(Y_{\tau_N}=k),\qquad k\ge N.
\]

### Lemma 2 (exact overshoot formula)

Put

\[
r_i(l)=
\begin{cases}
0,&l<i,\\
a(l,i)/a(i),&l\ge i.
\end{cases}
\tag{5.3}
\]

Then for every `k>=N`,

\[
\mu_i^N(k)
=a(k)\sum_{l=1}^{N-1}r_i(l)q^*(k,l).
\tag{5.4}
\]

For `i=1`, since the downward chain always reaches `1`, `a(l,1)=a(1)=1`; hence

\[
\nu_N(k):=\mu_1^N(k)
=a(k)\sum_{l=1}^{N-1}q^*(k,l).
\tag{5.5}
\]

#### Proof

The event `{Y_{tau_N}=k}` has a unique last state `l<N`. Because the chain is strictly increasing, that state is visited at most once. Therefore

\[
\mu_i^N(k)
=\sum_{l=i}^{N-1}
P_i(\text{hit }l)Q(l,k).
\]

Apply Lemma 1 and then the reversal relation (2.2):

\[
P_i(\text{hit }l)Q(l,k)
=
\frac{a(l)}{a(i)}a(l,i)
\frac{a(k)}{a(l)}q^*(k,l)
=
a(k)\frac{a(l,i)}{a(i)}q^*(k,l).
\]

This is (5.4). The `i=1` formula follows immediately. `square`

### Theorem 3 (overshoot universality in total variation)

For every fixed starting state `i`,

\[
\|\mu_i^N-\nu_N\|_{TV}\longrightarrow0
\qquad(N\to\infty).
\tag{5.6}
\]

Consequently for any fixed `i,j`,

\[
\|\mu_i^N-\mu_j^N\|_{TV}\longrightarrow0.
\tag{5.7}
\]

#### Proof

From (5.4)--(5.5) and the triangle inequality,

\[
\begin{aligned}
\|\mu_i^N-\nu_N\|_1
&\le
\sum_{k\ge N}a(k)
\sum_{l<N}|r_i(l)-1|q^*(k,l)\\
&=
\sum_{l<N}|r_i(l)-1|
\sum_{k\ge N}a(k)q^*(k,l).
\end{aligned}
\tag{5.8}
\]

Using `a(k)q^*(k,l)=a(l)Q(l,k)`, the right side is

\[
\sum_{l<N}|r_i(l)-1|a(l)Q(l,[N,\infty)).
\tag{5.9}
\]

The same reversal identity and (5.5) show that

\[
\sum_{l<N}a(l)Q(l,[N,\infty))
=
\sum_{k\ge N}\nu_N(k)=1.
\tag{5.10}
\]

Fix `epsilon>0`. By (5.1), choose `L>=i` so that

\[
|r_i(l)-1|\le\epsilon\qquad(l\ge L).
\]

The contribution to (5.9) from `L<=l<N` is at most `epsilon` by (5.10). For the finitely many `l<L`, each `Q(l,.)` is a probability distribution on the integers, so

\[
Q(l,[N,\infty))\to0.
\]

Hence the finite low-`l` contribution tends to zero. Taking `limsup` in (5.9) gives at most `epsilon`; since `epsilon` is arbitrary, the `L1` distance tends to zero, and therefore so does total variation. The pairwise statement follows by the triangle inequality. `square`

This is B25's “count the crossing twice” step: the same first-crossing law is counted through its last sub-`N` upward state and through the reversed downward path. The occupation limit makes the starting-state distortion disappear.

### Theorem 4 (reverse HD is Liouville)

Every bounded `Q`-harmonic function on the positive integers is constant.

#### Proof

Let `h` be bounded and `Qh=h`. Since `tau_N<=N-i`, elementary optional stopping for the bounded martingale `h(Y_r)` gives

\[
h(i)=E_i[h(Y_{\tau_N})].
\tag{5.11}
\]

For fixed `i,j`, therefore

\[
|h(i)-h(j)|
\le
2\|h\|_\infty
\|\mu_i^N-\mu_j^N\|_{TV}.
\]

Theorem 3 sends the right side to zero as `N->infinity`. Thus `h(i)=h(j)` for every pair `i,j`. `square`

By Aldous (1991), Proposition 12, Theorem 4 is equivalent to shift-coupling of the reverse-HD ancestor chain from every pair of starting states.

## 6. The vertex-Palm fringe law and why Aldous Theorem 13 applies exactly

The source fringe is sampled at a uniform **leaf**, whereas Aldous (1991) is formulated for the standard uniform-vertex fringe. Rather than silently identify the two, I now build the standard vertex-Palm law and then condition it back to a leaf.

Let `V_n` be a uniformly chosen vertex of the full binary tree `DTCS(n)`. There are exactly `2n-1` vertices. Let `S_n` be the number of descendant leaves below `V_n`.

For `i=1`, exactly `n` vertices are leaves, so

\[
P(S_n=1)=\frac{n}{2n-1}\to\frac12.
\tag{6.1}
\]

For `i>=2`, let `N_n(i)` be the number of clades of size `i`. Part III equation (3.14) gives

\[
E N_n(i)=\frac{n}{i}a(n,i).
\]

Hence

\[
P(S_n=i)
=\frac{E N_n(i)}{2n-1}
\longrightarrow
\pi_i:=\frac{a(i)}{2i}.
\tag{6.2}
\]

These limits have total mass one. Indeed, putting `k=i-1` and using (2.1),

\[
\begin{aligned}
\sum_{i=2}^\infty \frac{a(i)}{i}
&=\frac6{\pi^2}
\sum_{k=1}^\infty \frac{H_k}{k(k+1)}\\
&=\frac6{\pi^2}
\sum_{r=1}^\infty\frac1r
\sum_{k=r}^\infty\left(\frac1k-\frac1{k+1}\right)\\
&=\frac6{\pi^2}\sum_{r=1}^\infty\frac1{r^2}=1.
\end{aligned}
\tag{6.3}
\]

Thus

\[
\pi_1=\frac12,
\qquad
\pi_i=\frac{a(i)}{2i}\quad(i\ge2)
\tag{6.4}
\]

is a probability distribution and no root-size mass escapes to infinity.

Next condition on a selected size-`i` vertex. The expected number of parent-child incidences in which the child has `i` descendant leaves and its parent has `j>i` descendant leaves equals

\[
E N_n(j)\,[q(j,i)+q(j,j-i)].
\]

Dividing by `E N_n(i)` gives the conditional parent-size transition

\[
\frac{i\,a(n,j)}{j\,a(n,i)}
[q(j,i)+q(j,j-i)].
\tag{6.5}
\]

Because the critical split law is symmetric, this equals

\[
\frac{a(n,j)}{a(n,i)}q^*(j,i),
\tag{6.6}
\]

which is exactly the finite reverse kernel `q_n^up(i,j)` in Part III equations (5.6)--(5.8). For fixed `i,j`, it converges to `Q(i,j)`.

Conditional on the transition `i->j`, Markov branching gives a fresh sibling subtree with law `DTCS(j-i)` independent of the current child subtree; the selected child is on the left/right side with the corresponding symmetric orientation. This is precisely the reduced Markov construction of the extended fringe: the ancestor state is the clade size, and the side-branch mark attached at `i->j` is an independent ordered `DTCS(j-i)` tree.

The root-state law is tight by (6.4), the finite-dimensional ancestor transitions converge to `Q`, and the side branches at every fixed collection of transitions have fixed finite DTCS laws. Therefore the extended fringe around `V_n` converges locally to a unique invariant sin-tree law `mu` with root-size distribution `pi`, ancestor kernel `Q`, and those independent side branches. This is the standard uniform-vertex asymptotic fringe object to which Aldous (1991) applies.

Aldous (1991), §7.3, handles ordered trees by adding marks, so the left/right order here does not invalidate Theorem 13. Theorem 4 gives Proposition 12's shift-coupling hypothesis for `Q`. Therefore Aldous (1991), Theorem 13, yields:

\[
\boxed{\mu\text{ is an extreme invariant sin-tree law}.}
\tag{6.7}
\]

No modification of Theorem 13 for “uniform leaves” has been assumed here; the theorem has been applied only to the standard uniform-vertex law for which it was designed.

## 7. From vertex-Palm extremality to ergodicity of the source's leaf process

Let `nu` be the law of the source's leaf-rooted fringe tree. In each finite full binary tree, conditioning a uniform vertex to be a leaf makes it a uniform leaf. Since the event “the root is a leaf” is local and its probability tends to `1/2`, (6.1) gives

\[
\nu=\mu(\,\cdot\mid \text{root is a leaf}\,).
\tag{7.1}
\]

The ordered leaves of a `nu`-tree are indexed by `Z`, and rerooting at leaf `i` gives the source's stationary process `(T_i)_{i\in Z}`.

### Theorem 5 (the source fringe process is ergodic)

The stationary process `(T_i)_{i\in Z}` is ergodic under the leaf shift.

#### Proof

Let `A` be a measurable event in the leaf-rooted tree space invariant under the shift `T_i -> T_{i+1}`. Hence, on every realization outside a null set, `A` has the same truth value no matter which leaf is chosen as distinguished root.

Extend `A` to an event `A_hat` on the support of the vertex-rooted law `mu` as follows. Given a vertex-rooted sin-tree, choose any leaf by a fixed measurable rule (for example a nearest leaf, ties resolved by the planar order), reroot there, and declare `A_hat` to hold exactly when the resulting leaf-rooted tree lies in `A`. Because `A` is invariant under every integer leaf shift, a different selected leaf gives the same answer. Thus `A_hat` depends only on the underlying ordered sin-tree, not on which vertex is designated as root.

Consequently conditioning `mu` on `A_hat` (when it has positive probability) preserves the invariant-sin-tree property, and the same is true for the complement. If

\[
0<\mu(A_{hat})<1,
\]

then `mu` is the nontrivial convex combination

\[
\mu=\mu(A_{hat})\,\mu(\cdot\mid A_{hat})
+[1-\mu(A_{hat})]\,\mu(\cdot\mid A_{hat}^c),
\]

of two distinct invariant sin-tree laws. This contradicts the extremality (6.7). Therefore

\[
\mu(A_{hat})\in\{0,1\}.
\]

Since `A_hat=A` whenever the root is a leaf, conditioning on the positive-probability leaf event in (7.1) leaves the same zero-or-one value:

\[
\nu(A)\in\{0,1\}.
\]

That is exactly ergodicity of the stationary leaf-reroot process. `square`

This supplies the proof that the source only described as “arguing as in [3] one could show”.

## 8. Birkhoff gives the exact size-three density

For the stationary leaf process let

\[
L_j:=1_{\{j\text{ is the left endpoint of a size-three clade}\}}.
\]

This is a bounded local observable of `T_j`. Let

\[
M_j:=1_{\{j\text{ lies in a size-three clade}\}}.
\]

A size-three clade occupies three consecutive leaves and a leaf belongs to at most one clade of exactly that size, so

\[
M_0=L_0+L_{-1}+L_{-2}.
\tag{8.1}
\]

By stationarity,

\[
E L_0=\frac13 E M_0.
\tag{8.2}
\]

Part III §5.3 identifies `E M_0=a(3)`. From (2.1),

\[
a(3)=\frac{6H_2}{2\pi^2}=\frac9{2\pi^2},
\]

so

\[
\lambda_3:=E L_0=\frac3{2\pi^2}>0.
\tag{8.3}
\]

By Theorem 5 and Birkhoff's ergodic theorem,

\[
\frac1m\sum_{j=0}^{m-1}L_j
\longrightarrow\lambda_3
\qquad\text{almost surely}.
\tag{8.4}
\]

If `K_m` is the number of size-three clades wholly contained in the leaf block `{0,...,m-1}`, then exactly

\[
K_m=\sum_{j=0}^{m-3}L_j.
\]

The omitted two boundary indices contribute `O(1/m)`, hence

\[
\boxed{
\frac{K_m}{m}\longrightarrow\frac3{2\pi^2}
\quad\text{almost surely}.
}
\tag{8.5}
\]

This is stronger than the in-probability density law left open by the preceding run.

## 9. The positive-variance fringe CLT for the frozen mark

The preceding immutable P13 report proved the following source-specific decomposition, which I use rather than re-proving completed work.

For the block of leaves `{0,...,m-1}`, conditional on the unoriented size-three-clade scaffold,

\[
\sum_{i=0}^{m-1}\Psi(T_i)
=
\sum_{r=1}^{K_m}\varepsilon_r+R_m,
\qquad |R_m|\le2,
\tag{9.1}
\]

where the `epsilon_r` are conditionally independent Rademacher signs. Thus for fixed real `t`, conditional on the scaffold,

\[
E\left[
\exp\left(
\frac{it}{\sqrt m}\sum_{r=1}^{K_m}\varepsilon_r
\right)
\mid\text{scaffold}
\right]
=
\cos(t/\sqrt m)^{K_m}.
\tag{9.2}
\]

Uniformly for `0<=K_m<=m/3`,

\[
K_m\log\cos(t/\sqrt m)
=-\frac{t^2}{2}\frac{K_m}{m}+O_t(m^{-1}).
\tag{9.3}
\]

Insert the almost-sure limit (8.5) into (9.3). The conditional characteristic function tends almost surely, hence also in mean by bounded convergence, to

\[
\exp\left(-\frac{t^2}{2}\frac3{2\pi^2}\right).
\]

The boundary term satisfies `R_m/sqrt(m)->0`. Therefore Lévy's theorem and Slutsky give

\[
\boxed{
\frac1{\sqrt m}\sum_{i=0}^{m-1}\Psi(T_i)
\Rightarrow
N\left(0,\frac3{2\pi^2}\right).
}
\tag{9.4}
\]

The variance is strictly positive.

On every infinite fringe tree `Phi=0` identically, so the same statement is the centered fringe CLT for the **frozen single functional** `Theta=Psi+Phi`:

\[
\boxed{
\frac1{\sqrt m}\sum_{i=0}^{m-1}\Theta(T_i)
\Rightarrow
N\left(0,\frac3{2\pi^2}\right).
}
\tag{9.5}
\]

This proves the exact `FRINGE` obligation.

## 10. Source-level counterexample chain and metric movement

The preceding run already proved for the same `Theta` that the centered finite normalized sum

\[
\frac1{\sqrt n}\sum_{i=1}^n\Theta(T_i^{(n)})
\]

is not tight; in fact its absolute value diverges in probability. The proof used the root-split perturbation and only the uniform second-moment bound for the `Psi` term. That is the frozen `FINITE-FAILURE` obligation and is not reopened here.

Combining that completed theorem with (9.5):

- the stationary fringe process has a genuine nondegenerate Gaussian CLT for the bounded continuous functional `Theta`;
- the corresponding finite DTCS(n) centered `sqrt(n)`-normalized sums fail even tightness.

Thus the literal universal implication asked in Aldous--Janson Open Problem 12 has a complete positive-variance counterexample on P13's page.

The frozen metric therefore moves

\[
\boxed{M_{P0342}:1/2\longrightarrow2/2.}
\]

The unchanged-run streak resets to zero.

**Campaign label:** `CLAIMED / METRIC-COMPLETE / SOURCE-REFUTATION-CANDIDATE / AUDITS-PENDING`.

I do **not** call the campaign target CLOSED yet. The owner's closure rule still requires a source-matching end-to-end prior-art gate and two independent OTHER-track audits, one P26 and one distinct research track. The bounded repository search in this run did not recover a P0342 end-to-end PASS from either required outside auditor. P12's directed-audit duty follows this actual successor, but P13 does not create or fabricate that audit.

No novelty claim is made. The Liouville proof combines the already-published occupation limit with Aldous's 1991 shift-coupling/extremality theorem; the exact overshoot argument may or may not already be implicit somewhere outside the bounded search.

## 11. Method accounting

### B1 — CHANGE THE CATEGORY: succeeded

I stopped treating the missing clade-density LLN as a covariance-estimation problem and moved it to ergodic/extremal Markov theory. The category change reduced the source's unproved ergodicity sentence to a concrete Liouville statement for a one-dimensional Markov chain, which could be proved from the occupation theorem.

### B11 — DUALIZE: succeeded

The downward HD occupation probabilities were reversed into the upward ancestor kernel. The time-reversal identity converted the asymptotic `a(l,i)->a(i)` into asymptotic loss of starting-state information for upward first-crossing laws.

### B25 — COUNT THE SAME THING TWICE: succeeded

A first crossing of `[N,infinity)` was counted through the last state below `N` and through the reversed downward path. The resulting exact flux identity gave a normalized reference measure and the total-variation estimate, closing the Liouville step without a quantitative convergence rate.

This triple is distinct from the preceding B3/B18/B30 triple.

## 12. Verification scope

No new code was written after the idea because the new finite/infinite statements are proved symbolically on the page and introduce no finite enumeration claim requiring an exact-arithmetic core.

The existing P0342 exact self-check from the earlier run remains relevant only to the previously certified finite combinatorics/constants. It enumerated the recorded finite cases and ended

`ALL_EXACT_P0342_POSITIVE_VARIANCE_CHECKS_PASS`.

I do not relabel that self-check as an independent audit and do not use it as evidence for the analytic Liouville/extremality proof above.

The new idea was written **before** this proof report at

`proofnet24/P13-outside-successor/artifacts/2026-09-19/2026-09-19T11-19-51Z__p0342_b1_b11_b25_idea.md`.

It was created at commit

`4b22ed029ac8c249f4d3db1da569ca534d832c92`

and read back at that exact commit with blob

`eed82d90ba3ab179925ad63d5c346365b9e0d77a`.

## 13. Exact residual closure work

The mathematical denominator-two metric is complete. The remaining work is **not** another P13 source attack and must not be disguised as metric movement.

Before campaign closure:

1. P26 must perform an independent end-to-end audit of the literal Open Problem 12 counterexample, including the reverse-HD overshoot proof, the use of Aldous Theorem 13, the vertex-to-leaf conditioning step, and the already-proved finite non-tightness;
2. one distinct OTHER track must perform an independent end-to-end audit (the owner's directed P12 duty follows this successor);
3. the prior-art review must be refreshed specifically for the complete positive-variance construction and its ergodicity/Liouville mechanism; a bounded negative search does not certify novelty.

Only after those gates pass should a `paper_<name>/` package be created and the campaign status promoted to closure. Source-exact completed work should not be reopened while waiting for audits.

## 14. Structured `ledger_delta` for P26

```yaml
ledger_delta:
  track: P13
  native_slot: 6aa7b253b37c8191b693d8dc79298d37
  canonical_id: P0342
  source: Aldous-Janson arXiv:2303.02529v3 Open Problem 12 section 4.10
  lane: CLOSABLE_OUTSIDE
  witness: Theta=Psi+Phi
  metric_name: M_P0342
  metric_denominator: 2
  metric_before: 1
  metric_after: 2
  movement: true
  obligations:
    FRINGE: PROVED_THIS_RUN
    FINITE_FAILURE: PROVED_PREVIOUS_RUN
  new_core_theorems:
    - reverse-HD first-crossing laws from fixed starts merge in total variation
    - reverse-HD kernel has no nonconstant bounded harmonic functions
    - uniform-vertex DTCS fringe sin-tree is extreme by Aldous 1991 Theorem 13
    - stationary leaf-reroot fringe process is ergodic
    - K_m/m -> 3/(2*pi^2) almost surely
    - frozen Theta has fringe CLT N(0,3/(2*pi^2))
  source_consequence: literal Open Problem 12 implication has a complete positive-variance counterexample on P13 page
  campaign_status: METRIC_COMPLETE_SOURCE_REFUTATION_CANDIDATE_AUDITS_PENDING
  unchanged_run_streak_after: 0
  methods: [B1, B11, B25]
  prior_art_scope: bounded_2026-09-19_search_no_checked_exact_resolution; not_global_novelty_certificate
  audit_requirements_remaining:
    - P26 independent end-to-end source audit
    - one distinct OTHER-track end-to-end source audit; P12 directed duty follows current P13 successor
  self_check_status: prior P13 exact checker retained; no new finite-core checker needed for analytic proof
  shared_root_edits: none
```

## 15. Final status for this invocation

`P0342 = CLAIMED / METRIC-COMPLETE / SOURCE-REFUTATION-CANDIDATE / AUDITS-PENDING`.

No I0051 restart, C0021 restart, I0054 takeover, peer edit, shared-root ledger overwrite, scheduler modification, email/Drive action, public post, paid compute, permission change, workflow execution, force-push, or external contact was performed.
