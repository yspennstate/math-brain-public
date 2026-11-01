Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime model/effort receipt or binding selector is exposed.**

# H0008 admission-feasibility mathematics: cycle-balanced reversible slice, exit induction, and a branch-renewal compactification

Status: **PENDING_ADMISSION / H0008 NOT OWNED BY R7-07**.  The canonical path `operations/claims/H0008.md` already exists and is an immutable released R14 history, so R7-07's create-only acquisition rule forbids overwriting it.  The results below are therefore bounded admission-feasibility mathematics, not an exclusive-source claim.

Date: 2026-09-19 UTC.

## 1. Source law and inherited notation

The outside source remains Achyut Kumar (2026), *Threshold cascades of interacting diffusions on unimodular random trees: a conditional branching-process universality theorem, the annealed pressure, and the dimension of the failed boundary*, arXiv:2608.15987v1 (17 Aug 2026), Section 12.3 open problem (6), **Boundary fluctuations**.  In the finite-type failed-cluster reduction, a type-`i` parent has a common potential-child count `nu`; every potential child receives type `j` with probability `q_j` and transmits with probability `p_ij`.  Put

\[
 a_{ij}=q_jp_{ij},\qquad
 t_i=\sum_j a_{ij},\qquad
 M_{ij}=m_*a_{ij},\qquad m_*=E\nu.
\]

The source finite-type regime used by R14 has finite type set, `q_j>0`, `p_ij>0`, irreducible supercritical `M`, and the source moment hypotheses already recorded in the H0008 history.

For a surviving descendant tree `T`, let `B(T)` be the probability that simple random walk started at its root never hits an artificial parent.  With child escape probabilities `B_u`,

\[
 B(T)=\frac{\sum_uB_u}{1+\sum_uB_u},
 \qquad
 H_T(u)=\frac{B_u}{\sum_vB_v}.
\]

The preceding R7-07 run conjugated the two-spine density transfer to

\[
 (Tg)_j(b)
 =(1-b)^2m_*q_j\sum_i p_{ij}
 E\big[g_i(F_b(R_i))\big],
 \qquad
 F_b(r)=\frac{b+r}{1+b+r},
\]

and isolated the exact pipe Jacobian

\[
 J_{ij}=G'(1-t_i)q_jp_{ij},\qquad \rho(J)<1.
\]

This run uses the planned nonrepeating methods **B1 / B29 / B13**.

---

# 2. Method B1 — change category: from the harmonic transfer equation to Altok's reversible multitype environment

The direct fixed-point equation is not the only way to construct a stationary harmonic environment.  The one-type Lyons--Pemantle--Peres proof first constructs a stationary/reversible environment for ordinary simple random walk, then induces the path shift on last-exit points.  Serdar Altok's 2013 theorem gives exactly the multitype reversible-environment criterion needed to test whether that construction ports to the H0008 failed genealogy.

## 2.1 Exact transmitted-child type kernel

### Lemma 2.1 (conditional multinomial law)

For a type-`i` parent, conditional on the **total number `d` of transmitted failed children**, the transmitted child types are multinomial with `d` trials and probabilities

\[
 \boxed{\pi_{ij}=\frac{q_jp_{ij}}{t_i}}.
 \tag{2.1}
\]

These probabilities do not depend on `d`.

### Proof

Conditional on `nu=N`, every potential child independently falls in one of `|D|+1` categories:

- transmitted type `j`, with probability `a_ij=q_jp_ij`;
- not transmitted, with probability `1-t_i`.

Hence for a transmitted-child count vector `c=(c_j)` with `|c|=d<=N`,

\[
 P_i(C=c\mid\nu=N)
 =\frac{N!}{(N-d)!\prod_jc_j!}
 (1-t_i)^{N-d}\prod_ja_{ij}^{c_j}.
\]

Conditional on `|C|=d`, the factor depending on `N` cancels and

\[
 P_i(C=c\mid |C|=d,\nu=N)
 =\frac{d!}{\prod_jc_j!}\prod_j
 \left(\frac{a_{ij}}{t_i}\right)^{c_j}.
\]

The right side does not depend on `N`, so averaging over `nu` leaves the same conditional law.  This is exactly (2.1).  QED.

This puts H0008 precisely inside the vertex-label specialization of Altok, Theorem 4.1, *Unimodularity for multi-type Galton-Watson trees*, Bernoulli 19(3) (2013), 780--802, arXiv:1307.5962.

## 2.2 The source-specific reversible-cycle criterion

Altok's Theorem 4.1 says that for a strongly connected vertex-type MGW law whose conditional offspring-type law is multinomial with degree-independent parameters `pi_ij`, a reversible rooted-tree law for simple random walk exists exactly when the type kernel has symmetric support and satisfies the Kolmogorov cycle condition

\[
 \prod_{s=1}^{m-1}\frac{\pi_{i_s i_{s+1}}}{\pi_{i_{s+1}i_s}}=1
 \tag{2.2}
\]

for every allowed cycle `i_1,...,i_m=i_1`.

For the H0008 thinning law, all `q` and row-normalization factors telescope.

### Theorem 2.2 (H0008 reversible slice = transmission cycle balance)

Assume the transmitted-type support is symmetric.  Then the Altok reversible-environment criterion for the H0008 failed genealogy is equivalent to

\[
 \boxed{
 \prod_{s=1}^{m-1}p_{i_si_{s+1}}
 =
 \prod_{s=1}^{m-1}p_{i_{s+1}i_s}
 }
 \tag{2.3}
\]

for every type cycle.

Equivalently, the stochastic kernel `Pi=(pi_ij)` is reversible.  In particular, the criterion is independent of the base type weights `q_j` and of the row totals `t_i`.

### Proof

From (2.1),

\[
 \frac{\pi_{ij}}{\pi_{ji}}
 =
 \frac{q_jp_{ij}/t_i}{q_ip_{ji}/t_j}
 =
 \frac{q_jt_j}{q_it_i}\frac{p_{ij}}{p_{ji}}.
\]

Multiplying around a cycle, every `q_i` and every `t_i` occurs once in numerator and once in denominator, so they cancel.  Therefore (2.2) is exactly (2.3).  QED.

### Corollary 2.3 (every irreducible two-type positive-transmission source is in the reversible slice)

For two types with both cross transitions positive, every irreducible `2 x 2` stochastic kernel is reversible, so (2.3) is automatic.  Hence **every two-type H0008 source with positive cross transmission admits Altok's reversible augmented environment**.

This is materially broader than the previously solved one-block/lumpable slice: the two type rows can have different total transmission probabilities and the unlabelled genealogy can remain genuinely multitype.

## 2.3 Exact R14 non-lumpable test case

The terminal R14 handoff retained

\[
 \nu\equiv2,\qquad q=(1/2,1/2),\qquad
 P=\begin{pmatrix}3/4&3/4\\1/2&1/4\end{pmatrix}.
\]

Here

\[
 t_1=3/4,\qquad t_2=3/8,
\]

and therefore

\[
 \boxed{
 \Pi=\begin{pmatrix}1/2&1/2\\2/3&1/3\end{pmatrix}.
 }
\]

The unique reversible root-type weights from Altok satisfy

\[
 \frac{\mu(1)}{\mu(2)}
 =\frac{\pi_{21}}{\pi_{12}}=\frac43,
\]

so

\[
 \boxed{\mu=(4/7,3/7)}
\]

and indeed

\[
 \mu(1)\pi_{12}=\mu(2)\pi_{21}=2/7.
\]

Thus the smallest non-lumpable diagnostic retained by R14 is not merely tractable numerically: it lies exactly in a classical reversible multitype category.

## 2.4 Exit induction gives a harmonic-stationary environment on the cycle-balanced slice

The following is the key structural result of this run.  It is an adaptation of the architecture of Lyons--Pemantle--Peres (1995), Section 8, using Altok in place of ordinary augmented Galton--Watson measure.

### Theorem 2.4 (cycle-balanced exit-stationarity theorem)

Assume:

1. the H0008 finite-type failed genealogy is strongly connected, irreducible and supercritical;
2. the source is nonsingular in the branching sense (the surviving skeleton is not deterministically one child forever; this is automatic in the nontrivial supercritical H0008 regimes used here);
3. the transmission support is symmetric and satisfies the cycle balance (2.3);
4. the source moment assumptions ensure local finiteness and transience on survival.

Then there exists a probability law `mu_H` on surviving rooted typed failed trees which is stationary for the one-generation **harmonic-descendant shift**.  Moreover `mu_H` is absolutely continuous with respect to, and under the standard irreducible nonsingular backbone hypothesis equivalent to, the source MGW law conditioned on survival.

The construction does **not** require a finite-mean fresh-edge regeneration roof.

### Proof

**Step 1: reversible augmented multitype law.**  Lemma 2.1 and Theorem 2.2 verify Altok's Theorem 4.1.  Hence there is a reversible rooted-tree probability `mu_A` for simple random walk.  Conditional on root type and degree, neighbor types are iid with kernel `Pi`; deleting one distinguished neighbor leaves exactly the H0008 source offspring law in the remaining forward direction.  Altok also gives the root-type weights by detailed balance

\[
 \mu_A(i)\pi_{ij}=\mu_A(j)\pi_{ji}.
\]

**Step 2: condition on the unrooted tree being infinite.**  The event `I={T is infinite}` is invariant under rerooting.  Therefore conditioning a reversible law on `I` preserves reversibility: for every bounded test `f(T,o,x)` on an oriented adjacent pair,

\[
 E_{\mu_A}[1_I f(T,o,X_1)]
 =E_{\mu_A}[1_I f(T,X_1,o)]
\]

because `1_I` is unchanged by swapping the root across an edge.  After division by `mu_A(I)>0`, the conditioned law `mu_A^infty` remains reversible and stationary for simple random walk.

**Step 3: two-sided stationary path measure.**  Under `mu_A^infty`, use reversibility to construct the stationary two-sided simple-random-walk path law on pairs `(T,(X_n)_{n in Z})`.  The time shift is measure preserving.

**Step 4: induce on last-exit points.**  Define `Exit` exactly as in Lyons--Pemantle--Peres: at time zero the edge from `X_{-1}` to `X_0` separates the past limiting end from the future, and the future walk never crosses back to `X_{-1}`.  Transience makes `Exit` positive measure and almost every two-sided trajectory meets it in the future.  The induced transformation from one occurrence of `Exit` to the next preserves the normalized conditional path measure.

On a tree, successive induced exit vertices are consecutive vertices of the future limiting ray: before the walk can have a permanent exit through a deeper edge, it must make its final departure from the current vertex through the unique child on that ray.  Consequently the projected transition from the forward tree at one exit point to the forward tree at the next exit point is exactly the harmonic child rule `H_T`.

It follows immediately that the projected forward-tree law `mu_H` is stationary for the harmonic-descendant shift.

**Step 5: absolute continuity.**  Before conditioning on `Exit`, the Altok neighbor-subtree property says that, after deleting the incoming neighbor, the forward typed descendants have the H0008 source MGW law, with only finite positive type/root weights changed.  Conditioning on `I` and then on the positive-probability event `Exit` can only multiply this law by a finite nonnegative Radon--Nikodym density.  Therefore

\[
 \mu_H\ll P^{\rm surv}:=\sum_i\alpha_i P_i(\cdot\mid\mathrm{survival})
\]

for any strictly positive type mixture `alpha`.

**Step 6: source-chain ergodicity and equivalence.**  The one-type LPP Proposition 5.2 uses only branching independence plus positivity of the flow on every infinite child.  The finite-type analogue follows from the standard backbone fixed-point argument, which is short enough to record here.

Let `A` be harmonic-shift invariant and put, under the unconditioned type-`i` source law,

\[
 e_i=P_i(\mathrm{extinction}),\qquad
 x_i=P_i(A\cap\mathrm{survival}).
\]

Because harmonic weight is positive on every infinite child, on survival the root is in `A` iff every infinite child is in `A` (equivalently, iff any one infinite child is in `A`).  If `F_i` is the multitype offspring pgf, branching independence gives

\[
 x_i=F_i(e+x)-F_i(e).
\tag{2.4}
\]

Writing `s_i=1-e_i` and `a_i=x_i/s_i`, equation (2.4) says that `a` is a fixed point of the pgf of the surviving backbone.  That backbone has no zero-child state.  For an irreducible nonsingular finite-type process its only fixed points in `[0,1]^D` are `0` and `1`: if `0<a_*:=max_i a_i<1` and `a_i=a_*`, then every offspring product is at most `a_*`, and equality in the pgf average forces almost surely exactly one backbone child, always of a type whose `a`-value is `a_*`; strong connectivity propagates this deterministic-one-child property through every type, contradicting nonsingularity.  Boundary coordinates `0` or `1` propagate through strong connectivity in the same way.  Hence the harmonic descendant chain started from the source is ergodic.

The standard Markov-chain consequence used in LPP Proposition 5.2 now applies: an absolutely continuous stationary probability for this ergodic positive flow chain is equivalent to the source law, and its stationary chain is ergodic.  Therefore `mu_H~P^surv`.  QED.

### What this theorem does and does not prove

It discharges the **existence/stationarity/equivalence** obstruction on the entire cycle-balanced transmission slice.  It does not claim that every H0008 transmission matrix satisfies (2.3).  For three or more types, the cycle defect can be nonzero, and then Altok's reversible category is genuinely unavailable.

The theorem also does not claim that Altok's mechanism or the LPP exit induction is new.  Both are prior art.  The new campaign-level content is the exact source reduction (2.1)--(2.3), the observation that all two-type H0008 laws fall into the reversible category, and the resulting source-specific stationary-environment slice.  External novelty remains **UNVERIFIED**.

## 2.5 Dimension drop on the reversible slice

R14 already proved the multitype PF--KL identity conditional on an equivalent stationary harmonic environment and proved the equality rigidity: `H_T=U_T` source-a.s. iff `nu` is deterministic `k>=2` and every `p_ij=1`.

The exit construction above supplies the missing stationary equivalent environment on the cycle-balanced slice.  The remaining integrability can be obtained without assuming `log W in L^1` by the same coboundary lemma used by LPP.  If `W` is the multitype Perron/Kesten--Stigum limit and `U_T` the PF limit-uniform split, then

\[
 \log\frac1{U_T(u)}
 =\log\rho+\log W(T)-\log W(T_u),
\]

while the branching recursion `W(T)=rho^{-1}\sum_uW(T_u)` implies

\[
 \log W(T)-\log W(T_u)\ge-\log\rho.
\]

For a stationary shift, a finite a.s. coboundary whose negative part is bounded has mean zero by truncation.  Hence the mean PF cross-entropy is `log rho` even when `log W` itself is not integrable.  Local harmonic entropy is bounded by `log(1+N)`, and the source finite-second-moment hypothesis plus the exit construction's bounded conditioning density give its integrability.

Therefore the R14 PF--KL argument yields the following source slice.

### Corollary 2.5 (strict harmonic dimension drop on the cycle-balanced slice)

Under Theorem 2.4 and the source Kesten--Stigum/moment hypotheses,

\[
 \boxed{
 \dim_H\mathrm{HARM}_T
 =\log\rho(M)
 -E_{\mu_H}D_{KL}(H_T\Vert U_T).
 }
\]

Unless the failed genealogy is the deterministic regular no-thinning case

\[
 \nu\equiv k\ge2,\qquad p_{ij}=1\ \forall i,j,
\]

one has

\[
 \boxed{\dim_H\mathrm{HARM}_T<\log\rho(M)}
\]

for source-a.e. surviving tree.

In particular this proves the harmonic dimension-drop clause for **every irreducible two-type positive-transmission H0008 failed genealogy** satisfying the source hypotheses, including R14's smallest retained non-lumpable diagnostic.

This is a **PARTIAL source theorem**, not closure of H0008: generic `|D|>=3` transmission matrices need not be cycle-balanced, and the source open problem also contains broader fluctuation/multifractal content already treated separately by R14.

---

# 3. Method B29 — add the compactification point explicitly: exact pipe resolvent and genuine-branch reset

The preceding run proposed a quasi-compact attack on the conjugated two-spine operator.  In the coordinate

\[
 u=1/b\in[1,\infty),\qquad x_i(u)=g_i(1/u),
\]

one has the exact map

\[
 \Phi_r(u)
 :=\frac1{F_{1/u}(r)}
 =1+\frac{u}{1+ru}.
\tag{3.1}
\]

Thus

\[
 (\widetilde T x)_j(u)
 =\left(\frac{u-1}{u}\right)^2
 m_*q_j\sum_ip_{ij}E[x_i(\Phi_{R_i}(u))].
\tag{3.2}
\]

## 3.1 Exact pipe dynamics

For a sole-surviving-child pipe, `R=0`, so

\[
 \Phi_0(u)=u+1.
\]

The pipe part is

\[
 (\widetilde T_0x)_j(u)
 =\left(\frac{u-1}{u}\right)^2
 \sum_iJ_{ij}x_i(u+1).
\tag{3.3}
\]

### Theorem 3.1 (closed form for every pipe iterate)

For every `n>=1`,

\[
 \boxed{
 (\widetilde T_0^n x)_j(u)
 =\left(\frac{u-1}{u+n-1}\right)^2
 \sum_i(J^n)_{ij}x_i(u+n).
 }
\tag{3.4}
\]

### Proof

The matrix coefficients multiply to `J^n`.  The scalar factors telescope:

\[
 \prod_{k=0}^{n-1}
 \left(\frac{u+k-1}{u+k}\right)^2
 =\left(\frac{u-1}{u+n-1}\right)^2.
\]

This proves (3.4).  QED.

Choose a positive vector `ell` and `r_J<1` with

\[
 \ell^TJ\le r_J\ell^T.
\]

In the weighted sup norm `||x||_ell=max_i sup_u |x_i(u)|/ell_i`,

\[
 \boxed{\|\widetilde T_0^n\|_\ell\le r_J^n.}
\tag{3.5}
\]

Hence the exact pipe Green operator exists:

\[
 \boxed{
 G_0=(I-\widetilde T_0)^{-1}
 =\sum_{n\ge0}\widetilde T_0^n,
 \qquad
 \|G_0\|_\ell\le\frac1{1-r_J}.
 }
\tag{3.6}
\]

## 3.2 Genuine branches reset the point at infinity

For `r>0`,

\[
 1<\Phi_r(u)\le1+\frac1r,
 \qquad
 \Phi_r'(u)=\frac1{(1+ru)^2}.
\tag{3.7}
\]

Thus any genuine branch sends `u=infinity` to the finite point `1+1/r`.  More quantitatively, for `U>1`,

\[
 \Phi_r(u)>U
 \quad\Longrightarrow\quad
 r<\frac1{U-1}.
\tag{3.8}
\]

The preceding R7-07 run proved, for the source Palm sibling law,

\[
 P(0<R_i\le s)\le C_R e^{-c_R/s}
\]

for small `s`.  Substituting `s=1/(U-1)` gives the uniform reset-tail estimate

\[
 \boxed{
 \sup_{u\ge1}
 P(\,R_i>0,\ \Phi_{R_i}(u)>U\,)
 \le C_R e^{-c_R(U-1)}.
 }
\tag{3.9}
\]

Therefore a genuine branch can imitate escape toward the compactification boundary only through an exponentially rare near-pipe sibling configuration.

## 3.3 Exact branch-renewal factorization

Write

\[
 \widetilde T=\widetilde T_0+\widetilde T_+,
\]

where `T_+` contains `R>0`.  Since `I-T_0` is invertible by (3.6),

\[
 \boxed{
 I-\widetilde T
 =(I-\widetilde T_0)(I-\mathcal R),
 \qquad
 \mathcal R:=G_0\widetilde T_+.
 }
\tag{3.10}
\]

This is an exact algebraic identity, not a heuristic.  Consequently every unit-spectral obstruction of the full two-spine transfer is transferred to the **branch-renewal operator** `mathcal R`; the infinite sequence of exact pipes has already been summed out.

Moreover, if `x` is supported on `u>U`, then (3.8)--(3.9), finiteness of the type set, and (3.6) give

\[
 \boxed{
 \|\mathcal R(1_{u>U}x)\|_\ell
 \le C_*e^{-c_*(U-1)}\|x\|_\ell
 }
\tag{3.11}
\]

for source-dependent finite constants `C_*,c_*>0`.  The branch skeleton therefore has exponentially small access to the compactification tail.  This is strictly weaker than compactness of `mathcal R`, which is **not claimed**; it is the exact tail estimate needed for a Doeblin--Fortet or tightness proof.

The general `|D|>=3` obstruction is now localized to the finite-conductance branch core rather than to long exact pipes or uncontrolled escape at `B=0`.

---

# 4. Method B13 — find what only increases: cumulative two-spine branch hazard

At a vertex `v` let the harmonic child probabilities be `p_v(u)`.  Two independent harmonic rays remain together for one more generation with probability

\[
 s_v=\sum_up_v(u)^2,
 \qquad
 \Delta_v=1-s_v.
\]

Conditional on remaining together, their common child is chosen with probability

\[
 \widehat p_v(u)=\frac{p_v(u)^2}{s_v}.
\]

Let `X_k` be this conditional common-spine chain and define

\[
 A_n:=\sum_{k=0}^{n-1}-\log s_{X_k}.
\tag{4.1}
\]

Then `A_n` is pathwise nondecreasing and exact pipes contribute **zero** increment.

### Theorem 4.1 (exact Feynman--Kac survival identity)

For every fixed surviving tree,

\[
 \boxed{
 P_T(\tau>n)
 =E_T^{(2)}[e^{-A_n}],
 }
\tag{4.2}
\]

where `tau` is the common-prefix lifetime of two independent harmonic rays and `E^(2)` denotes the conditional common-spine chain.

### Proof

For a depth-`n` path `v_0,...,v_n`, its probability under the conditional common-spine chain is

\[
 \prod_{k=0}^{n-1}\frac{p_{v_k}(v_{k+1})^2}{s_{v_k}}.
\]

Multiplying by `e^{-A_n}=prod_k s_{v_k}` leaves exactly

\[
 \prod_{k=0}^{n-1}p_{v_k}(v_{k+1})^2,
\]

which is the probability that two independent harmonic rays choose that same path.  Summing over depth-`n` paths proves (4.2).  QED.

Now distinguish the chosen common child, with conductance `b`, from sibling conductance sum `R`.  Its harmonic mass is `p=b/(b+R)`.  Since the squared sibling masses sum to at most `(1-p)^2`,

\[
 \Delta
 =1-\sum_up_u^2
 \ge 1-p^2-(1-p)^2
 =2p(1-p)
 =\frac{2bR}{(b+R)^2}.
\tag{4.3}
\]

Therefore every genuine branch contributes the deterministic hazard lower bound

\[
 \boxed{
 -\log s
 \ge \Delta
 \ge\frac{2bR}{(b+R)^2}.
 }
\tag{4.4}
\]

In particular, if the branch is balanced at scale `epsilon`,

\[
 \epsilon\le R/b\le\epsilon^{-1},
\]

then

\[
 -\log s\ge
 \frac{2\epsilon}{(1+\epsilon)^2}>0.
\tag{4.5}
\]

Thus long two-spine survival can occur only by accumulating a long sequence of exact pipes or extremely imbalanced genuine branches.  The exact-pipe sequence is already summable through `J` and Theorem 3.1; the small-`R/b` near-pipe side has the superexponential sibling tail proved in the previous R7-07 run; and the large-`R/b` side makes the chosen child's pair weight `p^2=(1+R/b)^{-2}` itself small.  This is the correct monotone quantity for the next general-slice attack.

The remaining general theorem is now sharply stated: control the branch-renewal occupation of the two imbalanced regimes strongly enough to force linear growth of `A_n` on surviving branch skeletons, or equivalently a spectral radius strictly below one for `mathcal R` in an appropriate two-norm space.  I do **not** claim that step here.

---

# 5. Status, prior art boundary, and next obligations

### What is proved in this artifact

1. The H0008 transmitted-child type law conditional on total offspring is exactly multinomial with kernel `pi_ij=q_jp_ij/t_i`.
2. Altok's reversible-environment criterion reduces exactly to cycle balance of the transmission matrix `P`; `q` and `t` cancel around cycles.
3. Every irreducible two-type positive-transmission H0008 law satisfies that criterion; the R14 non-lumpable diagnostic has `Pi=[[1/2,1/2],[2/3,1/3]]` and reversible weights `(4/7,3/7)`.
4. On the cycle-balanced slice, Altok's reversible environment plus the LPP last-exit induction yields an equivalent ergodic harmonic-stationary environment under the stated irreducible/nonsingular/transient hypotheses.  Combined with the already-proved R14 PF--KL identity and rigidity, this gives strict harmonic dimension drop except for the deterministic regular no-thinning equality case.
5. For the general slice, the conjugated pipe operator has the explicit iterate (3.4), a bounded exact Green resolvent, and an exact branch-renewal factorization.
6. Genuine branches reset the compactification coordinate with exponential tail (3.9).
7. Two-spine survival has the exact increasing hazard representation (4.2), with deterministic branch hazard lower bound (4.4).

### What is not proved

- No claim is made that generic `|D|>=3` transmission matrices satisfy cycle balance.
- Failure of Altok cycle balance does **not** prove that no harmonic-stationary law exists; it only closes this reversible-environment route.
- The branch-renewal operator is not proved compact or strictly subcritical in the generic nonreversible slice.
- H0008 remains source-open and R7-07 remains PENDING_ADMISSION because the canonical claim path already exists and cannot be overwritten under this slot's acquisition rule.
- External novelty is **UNVERIFIED**.  Altok's reversibility theorem and the LPP exit induction are classical prior art; the source-specialized deductions are campaign mathematics, not a claim that the abstract mechanisms are new.

### Dated source/literature check, 2026-09-19

- Kumar arXiv:2608.15987 remains the 17 Aug 2026 primary source in the bounded check.
- Kumar--Duddala arXiv:2608.21125 (21 Aug 2026) concerns front propagation/Bramson correction and continuous-type limits, not this finite-type harmonic-exit stationarity theorem.
- Altok, arXiv:1307.5962 / Bernoulli 19(3) (2013), Theorem 4.1, supplies the exact reversible multitype criterion used above.
- Lyons--Pemantle--Peres, ETDS 15 (1995), Section 8, Theorem 8.1, constructs the one-type HARM-stationary measure by inducing stationary SRW on last-exit points; the proof architecture is what is ported here.
- Rousselin arXiv:1711.07920 gives the closest one-type regeneration/exit-environment analogue in random environment.
- Bounded searching did not locate a published finite-type theorem already spelling out the H0008 transmission-cycle reduction and harmonic exit consequence.  This is negative search evidence only.

### Next nonrepeating methods if no lawful shard-6 source becomes claimable

Use **B7 / B26 / B14**:

- B7 exploit a hidden conservation law: derive the exact adjoint mass/flux balance of the branch-renewal operator `mathcal R`;
- B26 local-to-global bootstrap: prove a strict contraction on a finite conductance slab and propagate it through the exact pipe resolvent;
- B14 find the group acting: use cycle-space/Hodge decomposition of `log p_ij-log p_ji` to quantify distance from the reversible slice and perturb the exit-stationary construction.

These do not repeat B1/B29/B13 or the immediately preceding B11/B24/B5 triple.
