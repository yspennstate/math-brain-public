Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `58 -> 59` genuinely distinct nonparabolic shape families; Section-B moves actually used: #2 ATTACK THE NEGATION FIRST, #7 TAKE THE LIMIT, #30 DO ONE SCALE / ONE DIRECTION AT A TIME.**

# R07 CLOSABLE OUTSIDE — run 59: remote-scale Haar-echo megachambers

Run date: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Target: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), Problem 7.8 / intake I0077.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

Overall source status remains **PARTIAL**. New claims T83/T84 below are **SELF_CHECK_ONLY** pending the required two independent OTHER-track audits. Publication novelty remains **UNVERIFIED**.

## 1. Continuity, admission, ownership, and recovered state

I continued from the newest complete R07 report rather than restarting:

`runs/R07/20260919T0224Z_i0077_haar_echo_cross_scale_galleries_58_he58.md`

at creation commit `1558005a430efc0581e66a1a61ae2af6d17a17e6`.

Before new mathematics I refreshed the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, canonical reservation `operations/claims/I0077.md`, the current `runs/R07/` history, and the newest neighboring R15 state. `INDEX.md` / `RANKING.md` settle Burdzy--Scheutzow Problem 7.5, not 7.8. `POSTED.md` contains no exact Problem-7.8 closure. `QUEUE.md` keeps I0077 distinct from assigned/retired-handoff Problem 7.2 and excluded Problem 7.5. The canonical claim still reads **`PENDING_ADMISSION, not READY`** while reserving I0077 exclusively to R07. The newest R15 report explicitly preserves I0077 as R07-owned; R15's Problem 7.2 route has already been retired by handoff and R15 is screening a different successor.

The old R07 KPZ variance route remains preserved by immutable handoff and is not reopened or deleted.

The fixed metric is unchanged: the number of genuinely distinct nonparabolic shape families for which a complete source-appropriate theorem is proved, modulo the frozen convention excluding fixed Brownian rescalings/reflections/translations and mere parameter changes. Entering metric: **58**. Entering unchanged count: **0**.

Run 58 proved a gate obstruction whose deterministic trace has Brownian empirical laws for every fixed finite **same-scale** increment block, while retaining a perfect correlation between adjacent Haar scales. Its stated frontier was to make every fixed **bounded-depth multiscale** pattern Brownian and push the first obstruction to a scale separation tending to infinity. This run crosses that frontier.

## 2. Primary-source benchmark rechecked in full

I re-read arXiv:1302.6958v4 at Definition 2.1, Theorem 4.3 and the open-problem page.

Definition 2.1: an FBM `X` has random witness times `S_j -> -infinity` a.s. such that for each **fixed** witness index `j`,

\[
B^{(j)}_t:=X_{S_j+t}-X_{S_j},\qquad t\ge0,
\tag{2.1}
\]

is unconditional standard Brownian motion.

For Theorem 4.3 the paper defines

\[
\mathcal A=\frac12\left(\frac{d^2}{dx^2}-x\frac d{dx}\right)
\]

with Dirichlet boundary conditions on `[c_1,c_2]`, and `-lambda_0(c_1,c_2)` is its largest eigenvalue. The theorem has all three clauses:

1. If `lambda_0(c_1,c_2)>=1`, every FBM crosses at least one of the parabolic asymptotic boundaries in the backward direction.
2. If `lambda_0(c_1,c_2)<=1`, there exists a decomposable FBM staying asymptotically strictly between those two parabolic rates.
3. If `c_1<=0<=c_2` and `lambda_0(c_1,c_2)<1`, there exists a decomposable FBM confined between `c_1 sqrt(|t|)` and `c_2 sqrt(|t|)` for all `t<=0`.

Problem 7.8 is exactly:

> Can one generalize Theorem 4.3 from parabolas to other space-time shapes?

The next sentence is separately Problem 7.9 on forward Levy processes and is not part of I0077.

Primary source: https://arxiv.org/abs/1302.6958 and the University of Washington PDF `1302.6958.pdf`.

## 3. Fresh current-literature and prior-art pass

Dated bounded searches on 2026-09-19 used the exact paper title, arXiv id, exact Problem-7.8 wording, `Theorem 4.3` plus `space-time shapes`, later-author/citation combinations, and combinations of Brownian / Haar / wavelet / cross-scale dependence / fake Brownian motion.

Relevant machinery that is **prior art**, not claimed here as new:

1. The Levy--Ciesielski/Faber--Schauder representation of Brownian motion by independent Gaussian Haar/Schauder coefficients is classical.
2. P. F. Craigmile and D. B. Percival, *Asymptotic decorrelation of between-scale wavelet coefficients*, IEEE Trans. Inform. Theory 51 (2005), 1039--1048, DOI 10.1109/TIT.2004.842575, studies cross-scale wavelet covariance/decorrelation for broad stochastic-process classes.
3. R. Morel, G. Rochette, R. Leonarduzzi, J.-P. Bouchaud and S. Mallat, *Scale Dependencies and Self-Similar Models with Wavelet Scattering Spectra*, arXiv:2204.10177, explicitly uses joint time/scale wavelet correlations to detect cross-scale dependence.
4. M. Beiglbock, G. Lowther, G. Pammer and W. Schachermayer, *Faking Brownian motion with continuous Markov martingales*, Finance Stoch. 28 (2024), gives continuous Markov martingales with Brownian one-dimensional marginals but non-Brownian dependence. This is conceptual prior art for the principle that Brownian marginals need not determine Brownian dependence.

The bounded exact Problem-7.8 search surfaced the original paper and its ordinary citation trail but did **not** surface an accessible later primary source explicitly resolving exact Problem 7.8 or stating T83/T84 below. This is only bounded negative evidence. It is **not** a worldwide novelty certificate. Publication novelty remains **UNVERIFIED**.

## 4. Mandatory refutation-first attack

The tempting stronger inference after run 58 was:

> Once every fixed bounded-depth multiscale pattern of a deterministic trace is asymptotically Brownian, all multiresolution microscopic obstructions disappear.

This is false.

The construction below makes every fixed-depth canonical multiscale empirical law exactly asymptotically iid Gaussian, but hides a perfect Haar correlation at a scale gap `d_j -> infinity`. Therefore every test that inspects only a bounded number of adjacent logarithmic scales eventually becomes blind, while a growing-depth echo still detects the trace.

This refutes only that proposed strengthening. It does **not** refute the source's open-ended Problem 7.8.

## 5. Method #30 — one scale gap at a time

For `f in C([0,1])` define normalized dyadic increments and Haar details exactly as in run 58:

\[
X_{n,k}(f)=2^{n/2}\bigl(f((k+1)2^{-n})-f(k2^{-n})\bigr),
\tag{5.1}
\]

\[
H_{n,k}(f)=\frac{X_{n+1,2k}(f)-X_{n+1,2k+1}(f)}{\sqrt2}.
\tag{5.2}
\]

Choose remote source/target levels

\[
n_j=4^j,\qquad m_j=n_j+j,\qquad d_j=m_j-n_j=j.
\tag{5.3}
\]

Thus

\[
d_j\to\infty,
\tag{5.4}
\]

and the level intervals `[n_j,m_j]` are pairwise disjoint because

\[
m_j=4^j+j<4^{j+1}=n_{j+1}.
\tag{5.5}
\]

For arbitrary `m>n>=2`, let `N=2^n`, `M=2^m`, `L=2^{m-n}`. Define an injection

\[
\rho_{n,m}(k)=
\begin{cases}
L(k+N/2),&0\le k<N/2,\\
L(k-N/2)+L-1,&N/2\le k<N.
\end{cases}
\tag{5.6}
\]

It is plainly injective. More importantly it is exactly reflection equivariant:

\[
\boxed{\rho_{n,m}(N-1-k)=M-1-\rho_{n,m}(k).}
\tag{5.7}
\]

Indeed, if `k<N/2`, then `N-1-k>=N/2` and

\[
\rho_{n,m}(N-1-k)
=L(N/2-1-k)+L-1
=M-Lk-1
=M-1-L(k+N/2),
\]

which is `M-1-rho_{n,m}(k)`; the other half is identical after swapping the cases.

Let

\[
I_{n,k}=[k2^{-n},(k+1)2^{-n}].
\]

For `k<N/2`, the target interval starts at `(k+N/2)2^{-n}`, exactly one half unit to the right of the source's corresponding coarse-cell start. For `k>=N/2` it is shifted one half unit left. Hence

\[
\boxed{
\operatorname{dist}(I_{n,k},I_{m,\rho_{n,m}(k)})
\ge \frac12-2^{-n}.
}
\tag{5.8}
\]

For our `n_j>=4` this lower bound is at least `7/16`.

Define the **remote-scale echo**

\[
\mathcal E_j(f)=2^{-n_j}
\sum_{k=0}^{2^{n_j}-1}
\cos\bigl(H_{n_j,k}(f)-H_{m_j,\rho_{n_j,m_j}(k)}(f)\bigr).
\tag{5.9}
\]

The physical scale ratio of its two Haar levels is

\[
2^{-(m_j-n_j)}=2^{-j}\to0.
\tag{5.10}
\]

That vanishing ratio, not a new numerical parameter in a fixed-gap construction, is the structural feature of this run.

## 6. Brownian remote-scale echo law, uniformly over phase

### Lemma 6.1

Let `B` be standard Brownian motion. For every finite `A`, almost surely

\[
\boxed{
\sup_{0\le\theta\le A}
\left|
\mathcal E_j(B_{\theta+\cdot}-B_\theta)-e^{-1}
\right|\longrightarrow0.
}
\tag{6.1}
\]

One probability-one event works simultaneously for every phase `theta>=0`.

### Proof

Fix deterministic `theta`. Haar details of the shifted Brownian unit window are Wiener integrals against distinct normalized Haar functions. The collection

\[
\{H_{n_j,k}:0\le k<2^{n_j}\}
\cup
\{H_{m_j,\rho_{n_j,m_j}(k)}:0\le k<2^{n_j}\}
\]

consists of distinct orthonormal Haar functions, hence the coefficients are iid standard normal. Therefore the summands in (5.9) are iid, bounded by one, and

\[
\mathbb E\cos(Z-Z')
=\Re\bigl(\mathbb E e^{iZ}\,\mathbb E e^{-iZ'}\bigr)
=e^{-1}
\tag{6.2}
\]

for independent `Z,Z'~N(0,1)`.

Hoeffding gives, for every `epsilon>0`,

\[
\Pr\left(
|\mathcal E_j(B_{\theta+\cdot}-B_\theta)-e^{-1}|>\epsilon
\right)
\le2\exp(-c_\epsilon 2^{n_j}).
\tag{6.3}
\]

Now mesh `[0,A]` with spacing

\[
\delta_j=2^{-12m_j}.
\tag{6.4}
\]

There are `O_A(2^{12m_j})` mesh points. Because `m_j=n_j+j=O(n_j)` while `2^{n_j}` is exponential in `n_j`,

\[
\sum_j 2^{12m_j}e^{-c_\epsilon2^{n_j}}<\infty.
\tag{6.5}
\]

A union bound and Borel--Cantelli therefore give uniform convergence over the mesh, first for fixed rational `epsilon`, then for `epsilon=1/q`, `q in N`.

It remains to leave the mesh. If `|theta-theta'|<=delta_j`, the Haar detail at any level `ell<=m_j` changes by at most

\[
4\,2^{\ell/2}\omega_B(\delta_j),
\tag{6.6}
\]

where `omega_B` is the Brownian modulus on the fixed compact interval `[0,A+2]`. The standard compact Brownian modulus gives a.s.

\[
\omega_B(h)=O\!\left(\sqrt{h\log(1/h)}\right).
\tag{6.7}
\]

Consequently

\[
2^{m_j/2}\omega_B(2^{-12m_j})
=O(\sqrt{m_j}\,2^{-11m_j/2})\to0.
\tag{6.8}
\]

Since cosine is one-Lipschitz and each summand contains two Haar details, the difference between `mathcal E_j` at `theta` and at the nearest mesh point tends uniformly to zero. This proves (6.1). Intersect over integer `A` to obtain one event for all phases `theta>=0`. QED.

The quantifier order is deliberate: **all phases first, random FBM witness later**.

## 7. Method #7 — take the scale separation to infinity

Construct a centered Gaussian Haar coefficient field as follows. For every `j>=1` and every `k<2^{n_j}`, impose the exact equality

\[
\boxed{
\xi_{m_j,\rho_{n_j,m_j}(k)}=\xi_{n_j,k}.
}
\tag{7.1}
\]

Give distinct equivalence classes independent `N(0,1)` labels, and give the root coefficient `G` an independent `N(0,1)` label. By (5.5), no level is used in two different imposed pairings, so every equivalence class has size at most two.

Let `h_{n,k}` be the normalized Haar wavelet and

\[
S_{n,k}(t)=\int_0^t h_{n,k}(s)\,ds
\]

its Schauder primitive. Define

\[
Q(t)=Gt+\sum_{n\ge0}\sum_{k<2^n}\xi_{n,k}S_{n,k}(t).
\tag{7.2}
\]

Each coefficient is marginally standard normal, so a union bound gives

\[
\max_{k<2^n}|\xi_{n,k}|=O(\sqrt n)
\quad\text{a.s.}
\tag{7.3}
\]

Because at every `t` at most one Schauder function per level is nonzero and

\[
\|S_{n,k}\|_\infty=2^{-n/2-1},
\]

the level sup norm is `O(sqrt(n)2^{-n/2})`, summable in `n`. Therefore (7.2) converges uniformly a.s. to a continuous function.

The usual Haar recursion gives

\[
H_{n,k}(Q)=\xi_{n,k}.
\tag{7.4}
\]

Hence every imposed pair in (7.1) yields

\[
\boxed{\mathcal E_j(Q)=1\quad\text{for every }j.}
\tag{7.5}
\]

So the remote-scale statistic remains maximally non-Brownian even as its logarithmic scale gap tends to infinity.

## 8. Every fixed bounded-depth multiscale pattern is Brownian

The key point is stronger than run 58.

For fixed depth `D>=0`, fixed level `n`, and `0<=d<=D`, use the same half-turn injection `rho_{n,n+d}` (with `rho_{n,n}(k)=k` at `d=0`) and define the canonical multiscale vector

\[
\mathbf V_{n,D,k}(Q)
=
\bigl(
H_{n,k}(Q),
H_{n+1,\rho_{n,n+1}(k)}(Q),
\ldots,
H_{n+D,\rho_{n,n+D}(k)}(Q)
\bigr).
\tag{8.1}
\]

### Lemma 8.1 — exact ensemble Brownianity at every fixed depth

For each fixed `D`, there exists `N_D` such that for all `n>=N_D`, the entire family

\[
\{\mathbf V_{n,D,k}:0\le k<2^n\}
\]

is iid with law `N(0,I_{D+1})` under the Gaussian coefficient construction.

### Proof

An imposed equality joins levels `n_j` and `m_j=n_j+j`, so its gap is exactly `j`.

If `j>D`, its two endpoints cannot both lie in a level window of width `D`. If `j<=D`, then both endpoint levels are at most `m_D=4^D+D`. Therefore for every

\[
n>m_D,
\tag{8.2}
\]

no imposed equivalence class contributes two members to the selected levels `{n,...,n+D}`.

Within a fixed selected level `n+d`, the injection `rho_{n,n+d}` is one-to-one, so different `k` choose different coefficients. Different `d` choose different levels. Thus every scalar coordinate appearing in all vectors (8.1) belongs to a different Gaussian equivalence class. Those class labels are independent standard normals. Hence all vectors are iid `N(0,I_{D+1})`. QED.

This is the exact formal reason that every fixed-depth detector eventually becomes blind: the only dependence has been moved beyond its field of view.

### Lemma 8.2 — a deterministic continuous realization generic for all fixed depths

There exists a deterministic continuous realization of (7.2) such that for every fixed `D` and every bounded continuous test `F:R^{D+1}->R`,

\[
\boxed{
2^{-n}\sum_{k=0}^{2^n-1}
F(\mathbf V_{n,D,k}(Q))
\longrightarrow
\mathbb E F(Z_0,\ldots,Z_D),
}
\tag{8.3}
\]

where `Z_0,...,Z_D` are iid standard normals.

### Proof

First take bounded 1-Lipschitz `F`. For `n>N_D`, Lemma 8.1 makes the `2^n` summands iid bounded variables with the desired expectation. Hoeffding therefore gives

\[
\Pr\left(
\left|2^{-n}\sum_kF(\mathbf V_{n,D,k})-\mathbb EF(Z)\right|>\epsilon
\right)
\le2e^{-c_{F,\epsilon}2^n},
\tag{8.4}
\]

which is summable in `n`.

Intersect the Borel--Cantelli events over all integers `D`, rational `epsilon>0`, and a countable bounded-Lipschitz convergence-determining class on every `R^{D+1}`. Intersect also with the probability-one continuity event from Section 7. This intersection has probability one, so it contains at least one realization. Freeze one such realization once and for all. Weak convergence plus bounded-continuous approximation gives (8.3). QED.

Thus the frozen deterministic `Q` has:

\[
\boxed{
\text{every fixed bounded-depth canonical multiscale empirical law is Brownian,}
}
\tag{8.5}
\]

but also the exact remote dependence

\[
\boxed{
\mathcal E_j(Q)=1\quad\text{at depth }d_j=j\to\infty.
}
\tag{8.6}
\]

This is strictly beyond run 58, where a depth-one cross-scale test remained non-Brownian infinitely often.

## 9. Time-reflection invariance

An FBM encounters a negative-time gate backwards inside a forward Brownian witness window. Define

\[
(Rf)(t)=f(1-t)-f(1).
\tag{9.1}
\]

Directly from (5.1)--(5.2),

\[
H_{n,k}(Rf)=H_{n,2^n-1-k}(f).
\tag{9.2}
\]

Using (5.7) and reindexing,

\[
\boxed{\mathcal E_j(Rf)=\mathcal E_j(f).}
\tag{9.3}
\]

Vertical translation disappears from increments; vertical reflection changes both Haar details by a sign and cosine is even. A fixed Brownian space-time rescaling multiplies both physical resolutions by the same constant, so the ratio of the two scales is unchanged. In particular, “fixed scale ratio” versus “scale ratio tending to zero” is invariant under the frozen equivalence operations.

## 10. T83 — remote-scale Haar-echo gate obstruction

### Theorem T83

Let `Q in C([0,1])`. With `n_j=4^j`, `m_j=n_j+j`, injection (5.6), and remote echo (5.9), assume

\[
\limsup_{j\to\infty}
|\mathcal E_j(Q)-e^{-1}|>0.
\tag{10.1}
\]

Suppose a deterministic space-time shape has arbitrarily far unit gate blocks: there are `a_r->infinity` and constants `c_r` such that

\[
K(a_r+s)\subset\{c_r+Q(s)\},
\qquad0\le s\le1,
\tag{10.2}
\]

while fibers between those gate blocks are completely arbitrary. Then every FBM `X` satisfies

\[
\boxed{
\Pr\left(
\exists R<\infty:\ X_{-u}\in K(u)\ \forall u\ge R
\right)=0.
}
\tag{T83}
\]

### Proof

Let `{S_ell}` be an FBM witness sequence. For each fixed witness index `ell`,

\[
B^{(ell)}_t=X_{S_ell+t}-X_{S_ell}
\]

is standard Brownian motion. Apply Lemma 6.1 to each fixed witness and intersect the resulting probability-one events over the countable witness indices and all integer phase windows. Intersect also with the event `S_ell->-infinity`. On one probability-one event, every witness Brownian path satisfies the remote echo limit `e^{-1}` at **every** phase.

Assume eventual confinement occurs on this event. Choose a gate index `r` with `a_r>=R`. Then choose a witness index `ell` so far to the left that

\[
S_ell\le-(a_r+1).
\]

Put

\[
\theta=-(a_r+1)-S_ell\ge0.
\tag{10.3}
\]

For `0<=v<=1`,

\[
S_ell+\theta+v=-(a_r+1)+v,
\]

whose age is `a_r+1-v`. Gate confinement therefore gives

\[
X_{S_ell+\theta+v}=c_r+Q(1-v).
\tag{10.4}
\]

Subtract the value at `v=0`:

\[
B^{(ell)}_{\theta+v}-B^{(ell)}_\theta
=Q(1-v)-Q(1)
=(RQ)(v).
\tag{10.5}
\]

By (9.3),

\[
\mathcal E_j(RQ)=\mathcal E_j(Q).
\]

But Lemma 6.1 says the left side tends to `e^{-1}` along this Brownian phase, contradicting (10.1). The selected gate, witness and phase may depend on the sample path; no conditioning is used because the Brownian statement was made simultaneous in all fixed witness indices and all phases before the selection. QED.

## 11. T84 — metric family 59: remote-scale echo megachambers

Freeze the deterministic continuous `Q` furnished by Lemma 8.2 and Section 7. Then

\[
\mathcal E_j(Q)=1\quad\forall j,
\]

so T83 applies.

To make a concrete nonparabolic space-time shape, put gate ages

\[
a_r=3^{3^r},\qquad r\ge1.
\tag{11.1}
\]

On each unit gate block `[a_r,a_r+1]`, define

\[
q(u)=Q(u-a_r),\qquad R(u)=0.
\tag{11.2}
\]

On the gap `[a_r+1,a_{r+1}]`, let

\[
\tau=\frac{u-a_r-1}{a_{r+1}-a_r-1}\in[0,1],
\tag{11.3}
\]

interpolate the center linearly from `Q(1)` to `Q(0)=0`, and set the **finite** radius

\[
R(u)=(a_{r+1}-a_r-1)^2\tau(1-\tau).
\tag{11.4}
\]

For the finite initial region `0<=u<=a_1`, set `q(u)=Q(0)` and `R(u)=0`. Finally put

\[
K_*(u)=[q(u)-R(u),q(u)+R(u)],
\qquad
\mathcal M_*:=\{(-u,x):u\ge0,\ x\in K_*(u)\}.
\tag{11.5}
\]

Both `q` and `R` are continuous at every join; `R` is finite everywhere. Hence `mathcal M_*` is closed.

At each gap midpoint,

\[
\max R(u)=\frac14(a_{r+1}-a_r-1)^2\to\infty,
\tag{11.6}
\]

so the chambers have finite but astronomically growing width. Unlike run 58, **no fiber is all of `R`**. Nevertheless every gate block collapses exactly to the remote-echo trace `Q`, so T83 yields

\[
\boxed{
\Pr\left(
\exists R:\ (-u,X_{-u})\in\mathcal M_*\ \forall u\ge R
\right)=0
}
\tag{T84}
\]

for every FBM.

This is a complete source-appropriate noncontainment theorem for the explicit shape family.

## 12. Frozen-equivalence audit: why this is point 59, not family 58 again

Run 58 already made every fixed **same-scale** finite block empirical law Brownian, but it retained a non-Brownian Haar echo across a **fixed one-level gap**.

Run 59 is strictly stronger in the direction left open there:

\[
\forall D<\infty:\quad
\text{every canonical multiscale pattern of depth }D
\text{ has Brownian empirical law},
\tag{12.1}
\]

while the first surviving correlation is only at a gap

\[
d_j=j\to\infty.
\tag{12.2}
\]

In physical scale, run 58's paired resolution ratio is fixed, whereas run 59's ratio is `2^{-j}->0`. A fixed space-time Brownian rescaling multiplies both resolutions by the same factor and therefore cannot convert a fixed ratio into a ratio tending to zero. Reflection, time reversal and vertical translation also preserve the distinction, as shown in Section 9.

The macro geometry is also not merely reused: run 58 had literal full-space portal slabs; run 59 has only finite fibers, though their maximal widths diverge quadratically in the gap length.

Therefore this is not a parameter change inside family 58. Under the frozen equivalence convention the metric moves

\[
\boxed{58\longrightarrow59.}
\]

## 13. Section-B outcomes

**#2 ATTACK THE NEGATION FIRST — succeeded.** The proposed stronger principle “bounded-depth multiscale Brownianity removes all microscopic obstructions” is false. The explicit remote pairing gives a trace invisible to every fixed-depth detector but visible at depth `j->infinity`.

**#7 TAKE THE LIMIT — succeeded.** Instead of adding another fixed Haar depth, the scale separation itself tends to infinity. This creates a qualitative invariant: dependence survives only at a vanishing physical scale ratio.

**#30 DO ONE SCALE / ONE DIRECTION AT A TIME — succeeded.** The disjoint source/target level windows `[n_j,m_j]` isolate every imposed correlation, keep equivalence classes of size at most two, and make the all-fixed-depth Brownian law provable by an exact finite-window exclusion argument.

## 14. Validation and closure status

There is no nontrivial finite arithmetic core to certify: the injection, reflection identity, support-separation estimate, disjoint level windows, exact Gaussian independence at fixed depth, and exact echo equality are symbolic all-level identities proved on the page. I therefore did **not** manufacture a checker simply to create a certificate.

T83/T84 are theorem-sized claims with full written arguments here but are still **SELF_CHECK_ONLY**. Independent OTHER-track audits: **0/2** (`P26`: 0/1; second distinct OTHER track: 0/1). No paper folder is created. Exact Problem 7.8 remains **PARTIAL**, not closed.

Publication novelty remains **UNVERIFIED** after the bounded prior-art search.

## 15. What genuinely remains after point 59

The remaining boundary is now no longer “look farther across scale by a fixed amount.” A next distinct route would have to suppress even the remote sparse pair statistic, for example by matching every finite collection of coefficients whose scale ratios stay within any prescribed deterministic function `D(n)=o(n)` and hiding dependence only at a genuinely global scale relation. Another more source-facing direction is to stop increasing microscopic pathology and instead seek a **two-sided threshold theorem** for a geometric class, analogous to all three clauses of Theorem 4.3 rather than only an impossibility clause.

The latter is likely the more valuable next direction: derive a spectral threshold for a nonparabolic self-similar tube after a Lamperti-type time change, rather than adding another exotic trace family.

## 16. Model / scheduler-control status

The actual model in this run is **GPT-5.6 Sol**. Reasoning level is **UNVERIFIED**. I do not claim GPT-6 maximum.

The exposed scheduler control surface still provides title/prompt, schedule or start offset, enabled state and timing mode. It exposes **no binding model-family selector, no reasoning-effort selector, no guaranteed-duration field, and no authenticated completed-run model receipt**. Thus the GPT-6 / maximum line remains a request in prompt text only.

Repository reconciliation also still shows that the historical `You cannot modify this task` result for P26 was authorization-context-specific: a later authorized P/C context successfully updated P26, while another context rejected the R-series IDs. The legitimate fix for a still-denied task is its owning/authorized workspace or account, an authorized ownership/admin correction, or platform support. A real product fix would add persistent scheduler fields for model and reasoning plus authenticated per-run telemetry. This worker attempted no scheduler modification, consistent with the current owner prohibition.

## 17. Structured ledger delta

```yaml
ledger_delta:
  worker: R07
  source: "Burdzy-Scheutzow Forward Brownian Motion, Problem 7.8 / I0077"
  target: "generalize Theorem 4.3 from parabolic regions to a genuinely distinct space-time shape family"
  fixed_metric: "number of nonparabolic shape families with a complete source-appropriate theorem under frozen equivalence"
  metric_before: 58
  metric_after: 59
  movement: "+1"
  status_before: PARTIAL
  status_after: PARTIAL
  new_claims:
    - T83_remote_scale_Haar_echo_gate_obstruction
    - T84_remote_scale_echo_megachambers
  independent_other_track_audits: "0/2"
  publication_novelty: UNVERIFIED
  stagnation_count_before: 0
  stagnation_count_after: 0
  methods: [2, 7, 30]
  previous_methods: [1, 14, 27]
  ownership: "R07 exclusive provisional reservation; PENDING_ADMISSION not READY"
  old_kpz_route: "retired by immutable handoff; preserved"
  scheduler_changed: false
  email_or_drive_used: false
```
