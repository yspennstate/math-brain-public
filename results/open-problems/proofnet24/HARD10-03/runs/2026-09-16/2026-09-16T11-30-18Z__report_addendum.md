# HARD10-03 — 2026-09-16T11-22-53Z checkpoint addendum

This append-only file records the exact delivery receipt for the main checkpoint and one further sharpening obtained after the main report was safely committed. It does not overwrite any earlier file.

## 1. Main report delivery receipt

Main report:

`proofnet24/HARD10-03/runs/2026-09-16/2026-09-16T11-22-53Z__report.md`

Create commit:

`b4bb6f2f5c1ab0661d992f8e2d8ed30bb4bdfefe`

Exact-create-commit readback blob:

`cc1946fc6589e138ac780d57bb525a4930449851`

The file was fetched back using that exact commit ref and its opening target/status plus previous-checkpoint section matched. Delivery of the main report is therefore **VERIFIED**.

No transient retry was needed. No approval/security denial occurred. Approval requirement: **NOT EXPOSED**.

---

# 2. NEW-L84 — an elementary off-diagonal endpoint tail

For the rate-one-per-edge continuous-time walk `X_beta`, one may construct the three coordinates as

\[
X_\beta^{(j)}=N_{j,+}(\beta)-N_{j,-}(\beta),
\]

where the six `N_{j,±}` are independent rate-one Poisson processes. Hence

\[
\mathbb E e^{\theta X_\beta^{(j)}}
=
\exp\{2\beta(\cosh\theta-1)\}.
\]

The standard Chernoff optimization (or the elementary Bennett bound for a Skellam variable) gives absolute `c,C>0` such that

\[
\mathbb P(|X_\beta|_2\ge R)
\le
C\exp\left\{-c\frac{R^2}{\beta+R}\right\}.
\tag{2.1}
\]

Therefore, pointwise,

\[
\boxed{
|x-y|_2\ge R
\quad\Longrightarrow\quad
p_\beta(x,y)
\le
C\exp\left\{-c\frac{R^2}{\beta+R}\right\}.
}
\tag{2.2}
\]

This is used only as a crude summable tail; no new external heat-kernel theorem is needed.

---

# 3. NEW-L85 — logarithmic-range connectivity skeleton for an exact finite cycle

Fix any desired power `B>0`. There exists `K_B<infinity` such that the following holds for every `beta>=1` and every integer `n>=2`.

Define

\[
L_n:=\log(en),
\qquad
R_{\beta,n}:=
K_B\bigl(\sqrt{\beta L_n}+L_n\bigr).
\tag{3.1}
\]

The elementary inequality

\[
\frac{R_{\beta,n}^2}{\beta+R_{\beta,n}}
\ge cK_B L_n
\tag{3.2}
\]

holds after changing the absolute `c` (split into `L_n<=beta` and `L_n>beta`). Choose `K_B` so large that (2.2) implies

\[
|x-y|_2>R_{\beta,n}
\quad\Longrightarrow\quad
p_\beta(x,y)\le n^{-(B+3)}.
\tag{3.3}
\]

Now let `A subset Z^3`, `0 in A`, `|A|=n`, and decompose `A` into the connected components

\[
A_1,\ldots,A_m
\]

of the geometric graph that joins two support vertices when their Euclidean distance is at most `R_{beta,n}`.

If `m>=2`, define the total directed inter-component one-period heat

\[
\mathcal H_\beta^{\rm cross}(A)
:=
\sum_{i\ne j}
\sum_{x\in A_i,y\in A_j}p_\beta(x,y).
\tag{3.4}
\]

Every inter-component pair is farther than `R_{beta,n}`, so (3.3) and the trivial `n^2` pair count give

\[
\boxed{
\mathcal H_\beta^{\rm cross}(A)
\le n^{-(B+1)}.
}
\tag{3.5}
\]

On the event `C_{pi_beta}(0)=A`, the root cycle is contained in the union of these `m` blocks and visits every block. Therefore the already archived particle-number-uniform random-cut theorem NEW-L53A applies with `B_i=A_i`. Its first-moment term gives

\[
\mathbb P(C_{\pi_\beta}(0)=A)
\le
\frac{\mathcal H_\beta^{\rm cross}(A)}m
\le n^{-B}.
\tag{3.6}
\]

More precisely, with

\[
s_m=\left\lceil\frac{m-1}{4}\right\rceil,
\]

symmetry of the one-particle kernel and NEW-L53A give the stronger many-component estimate

\[
\boxed{
\mathbb P(C_{\pi_\beta}(0)=A)
\le
\min\left\{
 n^{-B},
 2\left(
 \frac{e n^{-(B+1)}}{2s_m}
 \right)^{s_m}
\right\}
\qquad(m\ge2).
}
\tag{3.7}
\]

Thus:

### Theorem NEW-L85 — PROVED

For every `B>0`, after choosing `K_B`, every deterministic `n`-point exact cycle support `A` obeys the following dichotomy:

* either `A` is connected in the geometric graph of range
  \[
  R_{\beta,n}=K_B(\sqrt{\beta\log(en)}+\log(en)),
  \]
* or
  \[
  \boxed{\mathbb P(C_{\pi_\beta}(0)=A)\le n^{-B},}
  \]
  with the stronger `m`-component power in (3.7).

This is the first checkpoint in this track that turns the primitive one-cycle requirement into a **support-connectivity skeleton at an explicit near-diffusive logarithmic range** without introducing growing tagged-particle constants.

### Scope

The result is still fixed-support and therefore does not justify summing `n^{-B}` over all spatially arbitrary disconnected sets. Its use is structural: any support not already paying an arbitrarily high polynomial cross-heat penalty must admit an `R_{beta,n}`-range spanning tree.

A rooted `R`-connected `n`-point set has a finite geometric encoding (for example by a rooted spanning tree whose edges are lattice vectors of norm at most `R`), so NEW-L85 isolates the remaining entropy problem to a concrete near-diffusive skeleton class. A naive count of all such trees is still too large to close the conjecture; the next missing ingredient is a transitivity/primitive-return cost along that skeleton, not another deterministic leakage estimate.

---

## 4. Combined deterministic certificate

For the canonical diffusive components from NEW-L80, a fixed support already satisfies

\[
\mathbb P(C_{\pi_\beta}(0)=A)
\le e^{-c\Phi_\beta(A)}.
\]

For any coarser partition of `A` into mutually separated blocks, NEW-L53A simultaneously gives a cross-heat certificate. In particular, for the `R_{beta,n}` components of NEW-L85,

\[
\boxed{
\mathbb P(C_{\pi_\beta}(0)=A)
\le
\min\left\{
 e^{-c\Phi_\beta(A)},
 n^{-B},
 2\left(
 \frac{e n^{-(B+1)}}{2s_m}
 \right)^{s_m}
\right\}
}
\tag{4.1}
\]

whenever `m>=2` (with `Phi_beta` computed from the finer canonical diffusive decomposition).

So candidate finite supports are now forced into a precise fork: **large leakage/fragmentation cost, tiny cross-heat connectivity cost, or a near-diffusive logarithmic spanning skeleton.** The unresolved branch is the last one.

---

## 5. Post-write self-review

1. The Poisson-coordinate construction uses the same rate convention as the interchange tagged particle: each of the six oriented nearest-neighbor directions rings at rate one for the tagged walk.
2. (2.1) is a tail bound; using it to upper-bound a single endpoint probability in (2.2) is in the correct direction.
3. In the component decomposition, distinct components have every cross pair farther than `R_{beta,n}` by definition of connected components in the threshold graph.
4. The `n^2` cross-pair bound in (3.5) is deliberately crude but sufficient after choosing `K_B`.
5. NEW-L53A is applied only to deterministic blocks `A_i` for a fixed deterministic candidate support. On the exact-cycle event the cycle both stays in their union and visits every block, exactly matching the theorem's event.
6. No monotonicity in `beta`, no independence of permutation arrows, and no chronological-path/cycle identification is used.

The full `d=3` target remains **OPEN / PARTIAL**.
