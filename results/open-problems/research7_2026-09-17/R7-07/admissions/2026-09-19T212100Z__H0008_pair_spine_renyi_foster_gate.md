Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime model/effort receipt or binding selector is exposed.**

# H0008 admission-feasibility mathematics: exact Rényi interpolation for the harmonic two-spine and a Foster–Lyapunov gate

Status: **PARTIAL / SOURCE OPEN / R7-07 still PENDING_ADMISSION**.  This file does not create or imply an H0008 ownership claim.  The canonical path `operations/claims/H0008.md` already exists as the released R14 claim-history record, so R7-07's create-only assignment rule forbids overwriting it.

## 1. Purpose and inherited setting

The source is Achyut Kumar (2026), *Threshold cascades of interacting diffusions on unimodular random trees: a conditional branching-process universality theorem, the annealed pressure, and the dimension of the failed boundary*, arXiv:2608.15987v1, Section 12.3 open problem (6), **Boundary fluctuations**.  R14 and the earlier R7-07 runs already reduced the still-open harmonic-measure clause to the construction/integrability of a stationary harmonic-descendant environment.  In particular, earlier R7-07 work established the electrical and two-spine identities used below.

Fix one realized transient rooted tree.  Let its positive-conductance children be indexed by `u=1,...,N`.  Write

\[
B_u\in(0,1],\qquad
S:=\sum_{u=1}^N B_u,\qquad
B:=\frac{S}{1+S},\qquad
V:=\frac1B=1+\frac1S.
\tag{1.1}
\]

The harmonic probability of choosing child `u` is

\[
p_u:=\frac{B_u}{S},\qquad \sum_u p_u=1.
\tag{1.2}
\]

For two independent harmonic rays, while they have not yet split, the sub-Markov common-spine kernel is

\[
(P_2f)(T)
:=\sum_u p_u^2 f(T_u).
\tag{1.3}
\]

Its lost mass `1-P_2 1` is exactly the one-step probability that the two rays split.

The preceding R7-07 two-spine run proved the endpoint identities

\[
P_2V=V-1,
\qquad
P_2V^2=N(V-1)^2.
\tag{1.4}
\]

The goal here is to interpolate *exactly* between those endpoints and ask whether a superlinear Lyapunov moment can control the second moment of the common-spine lifetime.

---

## 2. B2 — negate the tempting positive-speed and uniform-power shortcuts first

### 2.1 Physical positive speed is not available from multitype transience alone

A classical deterministic two-type Galton–Watson example, the binary tree with attached unary pipes, has transient simple random walk but zero speed because the expected time spent in a visited pipe is infinite.  Thus the implication

\[
\text{multitype transience}\Longrightarrow\text{positive physical speed}
\]

is false.  Any attempt to prove the H0008 exit-level regeneration roof finite merely by importing a generic physical-speed theorem is therefore structurally invalid.

This does **not** refute H0008.  The old pipe example has a degenerate type mechanism and does not satisfy the full positive finite-type H0008 regime used in the R14/R7-07 reductions.  In H0008 the already-certified extinction Jacobian has spectral radius below one, so the exact sole-positive-child pipe channel is subcritical.  The example only kills an over-strong route.

### 2.2 A uniform pointwise `V^(1+epsilon)` Foster inequality also fails on the local electrical class

Take a deterministic local branch with two equal positive child conductances `b,b`.  Then

\[
B=\frac{2b}{1+2b},\qquad p_1=p_2=\frac12.
\tag{2.1}
\]

For every `epsilon>0`, the exact calculation in Section 3 below gives

\[
\frac{P_2 V^{1+\epsilon}}{V^{1+\epsilon}}
=2^\epsilon (1-B)^{1+\epsilon}
=\frac{2^\epsilon}{(1+2b)^{1+\epsilon}}.
\tag{2.2}
\]

Hence this ratio is **larger than one** whenever

\[
0<b<\frac{2^{\epsilon/(1+\epsilon)}-1}{2}.
\tag{2.3}
\]

Therefore no theorem based only on the local electrical recursion can assert a uniform pointwise contraction

\[
P_2V^{1+\epsilon}\le \kappa V^{1+\epsilon},\qquad \kappa<1,
\tag{2.4}
\]

through all sufficiently small balanced branch conductances.  Any successful proof must use the *rarity* and dynamics of those states, rather than rule them out pointwise.

This is precisely compatible with the earlier source-tail estimate

\[
P_i(0<B\le x)\le C e^{-c/x}:
\tag{2.5}
\]

small conductance is extremely rare under the source law, but it is not removed from the compactification merely by local algebra.

---

## 3. B5 — add a Rényi/Lyapunov exponent and differentiate it

The interpolation parameter is a real `epsilon` with `-1<=epsilon<=1`.  The exponent `1+epsilon` runs from `0` to `2`.

### Theorem 3.1 — exact pair-spine Rényi identity

For every `epsilon in [-1,1]`,

\[
\boxed{
P_2V^{1+\epsilon}
=(V-1)^{1+\epsilon}
Z_\epsilon(p),
}
\tag{3.1}
\]

where

\[
\boxed{
Z_\epsilon(p):=\sum_{u=1}^N p_u^{1-\epsilon}.
}
\tag{3.2}
\]

#### Proof

By definition of `P_2`, `p_u=B_u/S`, and `V(T_u)=1/B_u`,

\[
\begin{aligned}
P_2V^{1+\epsilon}
&=\sum_u\frac{B_u^2}{S^2} B_u^{-1-\epsilon}\\
&=\frac1{S^2}\sum_u B_u^{1-\epsilon}\\
&=\frac1{S^2}\sum_u (S p_u)^{1-\epsilon}\\
&=S^{-1-\epsilon}\sum_u p_u^{1-\epsilon}.
\end{aligned}
\]

Since `V-1=1/S`, this is (3.1).  `square`

### Corollary 3.2 — the two endpoint inequalities are one family

For `-1<=epsilon<=0`, the exponent `1-epsilon>=1`, so

\[
Z_\epsilon(p)=\sum_up_u^{1-\epsilon}\le1.
\]

Hence

\[
\boxed{P_2V^{1+\epsilon}\le(V-1)^{1+\epsilon}.}
\tag{3.3}
\]

For `0<=epsilon<=1`, concavity of `x^(1-epsilon)` gives

\[
Z_\epsilon(p)\le N^\epsilon,
\]

and therefore

\[
\boxed{P_2V^{1+\epsilon}\le N^\epsilon(V-1)^{1+\epsilon}.}
\tag{3.4}
\]

At `epsilon=0`, (3.1) is the exact identity `P_2V=V-1`.  At `epsilon=1`, it is the exact identity `P_2V^2=N(V-1)^2`.

Thus the **entire obstruction to crossing from the exactly solvable first moment into a superlinear moment is the Rényi partition function `Z_epsilon(p)` of the harmonic child distribution.**

### Theorem 3.3 — exact derivative at the critical exponent one

Let

\[
H(p):=-\sum_up_u\log p_u
\tag{3.5}
\]

be the Shannon entropy of the harmonic child distribution.  Differentiating (3.1) at `epsilon=0` yields

\[
\boxed{
P_2(V\log V)
=(V-1)\bigl[\log(V-1)+H(p)\bigr].
}
\tag{3.6}
\]

#### Proof

Directly,

\[
\begin{aligned}
P_2(V\log V)
&=\sum_u\frac{B_u^2}{S^2}\frac1{B_u}\log\frac1{B_u}\\
&=\frac1{S^2}\sum_u B_u\log\frac1{B_u}.
\end{aligned}
\]

Since `B_u=S p_u`,

\[
\sum_u B_u\log\frac1{B_u}
=S\left[\log\frac1S+H(p)\right].
\]

Divide by `S^2` and use `1/S=V-1`.  `square`

Equation (3.6) is the exact differential form of the branch obstruction.  The pipe case has `H(p)=0`; genuine branching injects positive entropy.

---

## 4. The exact local Feynman–Kac potential

Conjugate the pair kernel by `V^(1+epsilon)`:

\[
(\widehat P_\epsilon f)(T)
:=V(T)^{-1-\epsilon}
P_2\bigl(V^{1+\epsilon}f\bigr)(T).
\tag{4.1}
\]

By Theorem 3.1 its row mass is

\[
\boxed{
\widehat P_\epsilon 1
=(1-B)^{1+\epsilon}Z_\epsilon(p).
}
\tag{4.2}
\]

Indeed `(V-1)/V=1-B`.

Taking logarithms gives the exact local Feynman–Kac potential

\[
\boxed{
\Gamma_\epsilon(T)
:=(1+\epsilon)\log(1-B)
+\log Z_\epsilon(p).
}
\tag{4.3}
\]

At the exactly solvable exponent `epsilon=0`,

\[
\Gamma_0(T)=\log(1-B)<0,
\tag{4.4}
\]

but the gap degenerates as `B downarrow 0`.  Its first derivative is

\[
\boxed{
\left.\partial_\epsilon\Gamma_\epsilon(T)\right|_{\epsilon=0}
=\log(1-B)+H(p).
}
\tag{4.5}
\]

Thus the first-order competition is explicit:

- escape contributes the negative term `log(1-B)`;
- harmonic branching contributes the positive Shannon entropy `H(p)`.

This formula also explains the balanced-small-branch obstruction (2.2): when `B` is tiny but `H(p)` is order one, a positive superlinear exponent initially points in the wrong direction *locally*.

---

## 5. B21 — import the correct Foster–Lyapunov/Feynman–Kac criterion

The pointwise contraction killed in Section 2 is stronger than necessary.  The correct object is the Green operator of `widehat P_epsilon`.

Let `tau>=1` denote the common-prefix lifetime of two independent harmonic rays, with the convention

\[
P_T(\tau>n)=P_2^n1(T),\qquad n\ge0.
\tag{5.1}
\]

Write

\[
G:=\sum_{n\ge0}P_2^n
\tag{5.2}
\]

in the extended nonnegative sense.

### Theorem 5.1 — exact first- and second-lifetime Green identities

On every transient tree in this setting,

\[
\boxed{V=G1=E_T\tau,}
\tag{5.3}
\]

and

\[
\boxed{
GV
=\frac12E_T[\tau(\tau+1)],
\qquad
E_T\tau^2=2GV-V.
}
\tag{5.4}
\]

#### Proof

The identity `P_2V=V-1` is equivalent to `(I-P_2)V=1`.  The earlier electrical-energy identity identifies `V` as the nonnegative Green potential `G1`, proving (5.3).

Then

\[
GV=G^2 1
=\sum_{n,m\ge0}P_2^{n+m}1
=\sum_{k\ge0}(k+1)P_2^k1.
\]

Using (5.1) and the elementary tail identity

\[
\frac{r(r+1)}2=\sum_{k=0}^{r-1}(k+1),\qquad r\in\mathbb N,
\]

monotone convergence gives the first equality in (5.4); the second follows from `tau(tau+1)=tau^2+tau` and (5.3).  `square`

### Theorem 5.2 — a sufficient superlinear spectral/Green criterion

Fix any `epsilon>0`.  If

\[
\boxed{
\sum_{n\ge0}\widehat P_\epsilon^n1(T)<\infty,
}
\tag{5.5}
\]

then

\[
\boxed{E_T\tau^2<\infty.}
\tag{5.6}
\]

#### Proof

Because `V>=1`, `V<=V^(1+epsilon)`.  By conjugation,

\[
P_2^n V^{1+\epsilon}
=V^{1+\epsilon}\widehat P_\epsilon^n1.
\tag{5.7}
\]

Therefore

\[
GV
=\sum_nP_2^nV
\le
V^{1+\epsilon}\sum_n\widehat P_\epsilon^n1<\infty.
\]

Apply (5.4).  `square`

This is the useful imported criterion: **do not seek a uniform one-step power contraction.  Seek transience / spectral radius below one for the Feynman–Kac transform whose exact potential is (4.3).**

Under the earlier R7-07 theorem `P_i(0<B<=x)<=C exp(-c/x)`, every source-law moment `E_i V^r` is finite for every finite `r`.  Hence initial integrability of `V^(1+epsilon)` is not the missing step.  The missing step is iteration: control of `widehat P_epsilon` under the dynamically tilted two-spine laws.

---

## 6. What this changes in the H0008 proof programme

The old remaining statement “show the pair/common-spine second moment is finite” can now be replaced by the following sharper gate.

> **Rényi–Foster gate.**  Find some `epsilon>0` for which the positive kernel `widehat P_epsilon` of (4.1), with exact row potential (4.3), has finite Green mass in the source-relevant weighted space; equivalently it is enough to establish a spectral bound strong enough to imply (5.5) for source-a.e. starting tree.

This gate simultaneously captures the three pieces already proved separately:

1. **exact pipes:** `H(p)=0`, and their compactification boundary is controlled by the extinction Jacobian `J` with `rho(J)<1`;
2. **near-pipes:** the sibling-conductance / split defect has superexponentially small source probability;
3. **ordinary branches:** the positive entropy `H(p)` appears explicitly in the Feynman–Kac potential rather than as an unstructured denominator.

It also tells us exactly why the earlier scalar pointwise Lyapunov certificate was too strong: `Gamma_epsilon` can be positive at rare small-`B`, high-entropy branch states even though the *iterated* Feynman–Kac operator may still be transient.

No claim is made here that (5.5) follows automatically from the source hypotheses.  That is the remaining analytic step.

---

## 7. Methods and outcomes

### B2 — ATTACK THE NEGATION FIRST

Outcome: **successful obstruction to two tempting routes, not to H0008.**  Multitype transience need not imply positive physical speed (classical binary-tree-with-pipes example).  Locally, arbitrarily small balanced branches violate every uniform pointwise `V^(1+epsilon)` contraction for `epsilon>0` by (2.2)-(2.3).

### B5 — ADD A PARAMETER AND DIFFERENTIATE

Outcome: **new exact theorem.**  The exponent interpolation (3.1) identifies the harmonic Rényi partition function `Z_epsilon`; differentiating at the critical exponent gives the exact Shannon-entropy drift (3.6) and local potential derivative (4.5).

### B21 — ASK WHO ELSE HAS THIS SHAPE

Outcome: **new exact reduction.**  Recasting the pair spine as a conjugated Feynman–Kac/Foster kernel gives Theorem 5.2: finite Green mass for one positive exponent implies finite second moment of the common-spine lifetime.  This is the correct weaker target after the pointwise criterion fails.

---

## 8. Remaining gaps and next mathematical attack

Still unproved:

1. a source-hypothesis proof of finite Green mass (5.5) for some `epsilon>0`;
2. the final implication from the common-spine/regeneration moment control into all C1-C6 obligations of the H0008 stationary harmonic environment, though earlier R7-07 work already proves the reset law and the tower construction conditional on the exit-level roof;
3. any source-level closure or independent audits.

The most focused next attack is to decompose `Gamma_epsilon` by conductance and entropy scales:

\[
\{B\le x\}\cup
\{B>x,\ H(p)\le h\}\cup
\{B>x,\ H(p)>h\},
\]

use the source `exp(-c/B)` tail on the first region, a deterministic negative potential on the second after choosing `h<-(1+epsilon)log(1-x)/epsilon`, and pair-splitting mass loss on the third.  The difficulty is to make this decomposition stable under the *iterated tilted law*, not merely in one source step.

A nonrepeating next Section-B triple suggested by this derivation is **B12 / B24 / B28**: search for a conserved/compensated entropy-conductance quantity, solve the extremal local `Gamma_epsilon` problem at fixed `(B,Delta)`, and prove a typical-state drift estimate under the two-spine tilt.

## 9. Honest status

- Source: **OPEN** at the full H0008 level.
- This artifact: **PARTIAL**.
- R7-07 target: **PENDING_ADMISSION** because the create-only canonical-claim rule still collides with the released H0008 history path.
- Novelty: **UNVERIFIED**.  The Rényi/Foster algebra above was not found in the bounded source check, but search misses are not novelty certificates.
