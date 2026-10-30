# fleet01/B09 — exact physical-coordinate KL tree

**Run:** `fleet01-B09-20260922T104421Z-fei`  
**Programme:** `FEI-ALL-TEAM-20260922T095941Z`  
**Assignment:** conditional relative-entropy tree  
**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT_MULTISCALE_KL_DISINTEGRATION`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Control correction and target

A later owner control supersedes the older MOC4 prompt supplied to this invocation. Under owner-control revision `2026-09-22.3`, all eighty workers are assigned to FEI, and fleet01/B09's live task is to derive a physical-coordinate tree decomposition of the irreducible occurrence KL

\[
K_{\rm occ}(P)=D_{\rm KL,2}(P\Vert Q_r)
\]

with **exact inherited reference-law updates**, rather than replacing each child reference by its own local I-projection at no cost.

The full target remains: prove one finite dimension-independent constant `C` for

\[
H(f)\le C I(f)
\]

for every Boolean function on every finite uniform cube, or give a genuine counterfamily. This report does not claim that result.

## 2. Source-pinned premises actually used

### 2.1 fleet02/B15 — influence I-projection

Source: `yspennstate/math-open-problems`, commit
`4bd6d05f1eb8325d665f2748f4d74dcee2550a04`, path
`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B15/20260922T0829Z-influence-iprojection-kl/REPORT.md`.

For a law `P` on nonempty subsets of `[n]`, with occurrence marginals

\[
r_i=P(i\in S),
\]

there is a unique maximum-entropy conditional-product law `Q_r`. If `\mu=\sum_i r_i>1`, let `c\in(0,1]` be the unique positive solution

\[
1-c=\prod_i(1-cr_i),
\]

put `t_i=cr_i`, take independent Bernoulli variables with probabilities `t_i`, and condition on nonemptiness. The resulting law is `Q_r`, and

\[
K_{\rm occ}(P)=D_2(P\Vert Q_r)=H_{\max}(r)-H(P).
\]

For the exact all-gate FEI residual,

\[
R_\Gamma=B_{\rm inf}^{\Gamma}+K_{\rm occ}.
\]

### 2.2 fleet04/B15 — exact hierarchy KL

Source: `yspennstate/math-open-problems`, commit
`2bf247373576eb406ca91bb3ea5f3ce5e5ab8588`, path
`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B15/20260922T091017Z-iprojection-composition-transfer/REPORT.md`.

For a one-level disjoint Boolean composition `F=G(f_1,...,f_m)`, the source proves

\[
K_{\rm occ}(F)
=K_{\rm occ}(G)+\sum_i\alpha_iK_{\rm occ}(f_i)+C_{\rm hier},
\]

where the hierarchy mismatch `C_hier` is an explicit sum of nonnegative KL divergences. Equivalently, before locally re-projecting, its chain-rule form is

\[
D(P_F\Vert Q_s)
=D(P_0\Vert Q_A)+\sum_i\alpha_iD(P_i\Vert Q_i^{(\zeta)}).
\]

This is the named OTHER-account result applied below: the theorem in Section 4 recursively iterates precisely this inherited-reference chain rule through an arbitrary physical partition tree.

### 2.3 fleet03/B18 — recursive-majority low-level barrier

Source: `yspennstate/math-open-problems`, commit
`bff0d7b6c21485f386841c42582eb04f32705046`, path
`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B18/20260922T100641Z-lowlevel-projection-barrier/REPORT.md`.

For depth-`m` recursive ternary majority `M_m`, every extraction retaining individually labelled Fourier atoms only through a fixed level, or through `d_m\le(1/2-\varepsilon)m` followed by one merged tail, captures an asymptotically vanishing fraction of the necessary I-projection payment. Thus a useful B09 construction must be genuinely multiscale or retain an exact statistic carrying all scales.

## 3. Setup: an arbitrary physical partition tree

Let `V=[n]`, and let `P` be any probability law on

\[
\Omega_V=2^V\setminus\{\varnothing\}.
\]

Let `r_i=P(i\in S)` and let `Q_r` be the fleet02/B15 I-projection. Write its unconditioned independent Bernoulli parameters as

\[
t_i=cr_i,
\]

so that

\[
Q_r(S)=\frac{\prod_{i\in S}t_i\prod_{i\notin S}(1-t_i)}{c},
\qquad S\ne\varnothing,
\]

where `c=1-\prod_i(1-t_i)`.

Fix **any rooted partition tree** `\mathcal T` whose root is `V`, whose leaves are the singletons `{i}`, and such that the children of each internal node `v` are pairwise-disjoint blocks partitioning its leaf set `V_v`.

For a sampled nonempty set `S`, define

\[
X_v=\mathbf 1\{S\cap V_v\ne\varnothing\}.
\]

For an active internal node `v`, define the nonempty child-occupancy pattern

\[
A_v=\{w\in\operatorname{ch}(v):X_w=1\}.
\]

For each child `w` put

\[
z_w:=\prod_{i\in V_w}(1-t_i),
\qquad
z_v:=\prod_{w\in\operatorname{ch}(v)}z_w
      =\prod_{i\in V_v}(1-t_i).
\]

Under the inherited global reference `Q_r`, the exact conditional law of the child pattern, given that `v` is active, is

\[
\boxed{
q_v(A)=
\frac{
 \prod_{w\in A}(1-z_w)
 \prod_{w\notin A}z_w
}{1-z_v}},
\qquad \varnothing\ne A\subseteq\operatorname{ch}(v).
\tag{3.1}
\]

No local I-projection of `P` appears in (3.1). The probabilities are inherited from the **one global** `Q_r`.

## 4. Main theorem — exact physical-coordinate KL tree

### Theorem 4.1 (`FEI-PHYSICAL-KL-TREE-v1`)

Order the internal nodes of `\mathcal T` so that every ancestor precedes its descendants. For each internal node `v`, let `\mathcal H_v` denote the complete previously exposed tree history before revealing `A_v`. If `v` is inactive, encode `A_v` by one deterministic cemetery symbol.

Then

\[
\boxed{
K_{\rm occ}(P)
=
\sum_{v\in\operatorname{Int}(\mathcal T)}
\mathbb E_P\!\left[
 X_v\,
 D_2\!\left(
 P(A_v\in\cdot\mid\mathcal H_v,X_v=1)
 \middle\Vert q_v
 \right)
\right].
}
\tag{4.1}
\]

Consequently, by convexity of relative entropy,

\[
\boxed{
K_{\rm occ}(P)
\ge
\sum_v P(X_v=1)
D_2(p_v\Vert q_v),
}
\tag{4.2}
\]

where

\[
p_v(\cdot)=P(A_v\in\cdot\mid X_v=1).
\]

More generally, for arbitrary deterministic local statistics `\phi_v(A_v)`, data processing gives the reusable no-double-spending bound

\[
\boxed{
K_{\rm occ}(P)
\ge
\sum_v P(X_v=1)
D_2\!\left(
(\phi_v)_\#p_v\middle\Vert(\phi_v)_\#q_v
\right).
}
\tag{4.3}
\]

### Proof

The family of active child patterns `{A_v}` is a lossless hierarchical encoding of the nonempty leaf set `S`: beginning at the active root, the pattern at each active internal node specifies exactly which children remain active, and after descending to the leaves one recovers precisely the members of `S`. Thus applying the KL chain rule to this sequential encoding gives

\[
D_2(P\Vert Q_r)
=
\sum_v
\mathbb E_P
D_2\!\left(
P(A_v\in\cdot\mid\mathcal H_v)
\middle\Vert
Q_r(A_v\in\cdot\mid\mathcal H_v)
\right).
\tag{4.4}
\]

If `v` is inactive, both conditional laws put unit mass on the cemetery symbol and the corresponding term is zero.

Suppose now that `v` is active. Before the global conditioning on nonemptiness, `Q_r` is a product law on the physical leaves. The events and configurations in the disjoint child blocks of `v` are independent of all leaves outside `V_v`. Once `X_v=1` is known, the global nonempty conditioning is redundant inside `V_v`. Hence, conditional on any compatible earlier history and on `X_v=1`, the child-block activity indicators are independent Bernoulli variables with inactivity probabilities `z_w`, conditioned on at least one child being active. This is exactly the law `q_v` in (3.1), and it is independent of the exterior/ancestor history beyond the fact `X_v=1`.

Substituting this conditional law into (4.4) proves (4.1).

For (4.2), condition on `X_v=1` and average the history-dependent laws. Since KL is convex in its first argument and `q_v` is history-independent,

\[
\mathbb E\left[D_2(P(A_v\mid\mathcal H_v,X_v=1)\Vert q_v)\mid X_v=1\right]
\ge D_2(p_v\Vert q_v).
\]

Sum over `v`. Equation (4.3) follows by applying data processing separately to every term of (4.2). `QED`.

### Corollary 4.2 — exact event payment

If an active node `v` obeys a source-forced event `E_v\subseteq 2^{\operatorname{ch}(v)}\setminus\{\varnothing\}` with

\[
P(A_v\in E_v\mid X_v=1)=1,
\]

then binary data processing yields

\[
\boxed{
K_{\rm occ}(P)
\ge
P(X_v=1)\log_2\frac1{q_v(E_v)}.
}
\tag{4.5}
\]

More generally, the corresponding payments for disjoint tree nodes/scales add through (4.3). This is the desired physical information currency: every payment is charged to a distinct conditional KL term in the global chain rule, so it is not spent twice.

## 5. Relation to the fleet04/B15 hierarchy theorem

Take a tree with one root whose children are the physical blocks of a disjoint composition `F=G(f_1,...,f_m)`, and below each block place the child physical tree. At the root, (4.1) gives exactly

\[
D(P_0\Vert Q_A).
\]

Conditioning on outer block `i` being active, the first inherited reference inside that block is precisely `Q_i^{(\zeta)}` from fleet04/B15, so the next contribution is

\[
\alpha_iD(P_i\Vert Q_i^{(\zeta)}).
\]

Therefore the first split of (4.1) is exactly fleet04/B15's chain-rule identity

\[
D(P_F\Vert Q_s)
=D(P_0\Vert Q_A)+\sum_i\alpha_iD(P_i\Vert Q_i^{(\zeta)}).
\]

Applying fleet02/B15's Pythagorean I-projection identity to the root and each child recovers

\[
K_{\rm occ}(F)
=K_{\rm occ}(G)+\sum_i\alpha_iK_{\rm occ}(f_i)+C_{\rm hier}.
\]

Thus Theorem 4.1 is a recursive physical-tree extension of the named OTHER-account hierarchy result. It also identifies the precise error in a tempting shortcut: replacing `Q_i^{(\zeta)}` by the child's own `Q_{r_i}` erases the mismatch divergence. The mismatch is not bookkeeping noise; it is an actual nonnegative part of `K_occ`.

## 6. Mandatory preflight: recursive ternary majority

Let `M_m` be depth-`m` recursive `Maj_3`, on `3^m` leaves, with the natural ternary formula tree. The exact spectral branching law reported by fleet03/B18 is:

- at every active node, one specific child is selected with probability `1/4` for each of the three singleton patterns;
- all three children are selected with probability `1/4`;
- pair patterns have probability zero.

Let

\[
g(\{1\})=g(\{2\})=g(\{3\})=g(\{1,2,3\})=\frac14.
\]

Every leaf has occurrence marginal `r=2^{-m}`. Let `c_m` be the global I-projection parameter and put

\[
t_m=c_m2^{-m}.
\]

At tree depth `\ell` from the root, each child block contains `3^{m-\ell-1}` physical leaves. Under the inherited reference, the child-activation probability is therefore

\[
\boxed{
u_{m,\ell}
=1-(1-t_m)^{3^{m-\ell-1}}.}
\tag{6.1}
\]

For three equal child blocks, (3.1) gives

\[
q_u(\{j\})={ (1-u)^2\over 3-3u+u^2},
\qquad
q_u(\{1,2,3\})={u^2\over 3-3u+u^2}.
\]

Hence the exact active-node KL is

\[
\boxed{
k(u):=D_2(g\Vert q_u)
=\log_2{3-3u+u^2\over4}
-\frac32\log_2(1-u)
-\frac12\log_2u.
}
\tag{6.2}
\]

The expected number of active nodes at depth `\ell` under the true spectral process is `(3/2)^\ell`. Theorem 4.1 therefore gives the **exact all-scale identity**

\[
\boxed{
K_{\rm occ}(M_m)
=
\sum_{\ell=0}^{m-1}
\left(\frac32\right)^\ell
k(u_{m,\ell}).
}
\tag{6.3}
\]

This is not a low-level Fourier truncation: it retains a local conditional KL at every physical depth through `m-1`.

### A quantitative bottom-scale payment

At the bottom internal level, `u_{m,m-1}=t_m\le2^{-m}`. For `0<u\le1/2`,

\[
3-3u+u^2\ge\frac74,
\]

and `-\frac32\log_2(1-u)\ge0`. Thus

\[
k(u)\ge
\frac12\log_2\frac1u+\log_2\frac7{16}.
\]

Consequently

\[
\boxed{
K_{\rm occ}(M_m)
\ge
\left(\frac32\right)^{m-1}
\left(
\frac m2+\log_2\frac7{16}
\right).
}
\tag{6.4}
\]

For large `m` this is `\Omega(m(3/2)^m)`. Thus the physical KL tree survives the exact failure mode of the fixed/low-level projection: the missing logarithm is already visible as the `\frac12\log(1/u)` cost of the rare bottom-scale occupancy pattern, and that payment is multiplied by the true number of active physical nodes. No single merged spectral tail is asked to carry it.

Fleet03/B18 also gives

\[
I(M_m)=\left(\frac32\right)^m,
\qquad
H(M_m)=4\left[\left(\frac32\right)^m-1\right].
\]

Together with `K_occ=H_max-H`, this confirms that for every `C\ge4` the exact recursive-majority source satisfies the balanced target

\[
K_{\rm occ}(M_m)
\ge H_{\max}(r^{(m)})-C[I(M_m)-1].
\]

The value of (6.3) is that it shows **where the KL lives physically and without repeated spending**, rather than using the already-known closed entropy formula as a black box.

## 7. Conditional end-to-end argument and first unpaid implication

For any surviving finite-cap all-gate potential `\Gamma`, the exact route is now:

1. fleet02/B15: `R_\Gamma=B_{\rm inf}^\Gamma+K_{\rm occ}`;
2. Theorem 4.1: expand the entire `K_occ` into nonoverlapping conditional physical-tree KL payments with the one inherited global reference `Q_r`;
3. use Boolean/source structure to lower-bound selected local terms, retaining rare-event logarithms and every reference mismatch;
4. prove that their sum is at least `[-B_{\rm inf}^\Gamma]_+` for every genuine gate/source;
5. then `R_\Gamma\ge0` for every gate, and the existing all-gate formulation yields FEI.

The first essential missing implication is therefore no longer an unspecified tree identity. It is the following precise universal payment problem:

> **`FEI-TREE-PAY-BINF-v1` (OPEN).** For a suitable source-valid physical partition/restriction tree attached to every genuine Boolean spectral source, prove
> \[
> \sum_v P(X_v=1)
> D_2\!\left((\phi_v)_\#p_v\Vert(\phi_v)_\#q_v\right)
> \ge[-B_{\rm inf}^{\Gamma}]_+
> \]
> for an explicitly chosen family of local statistics `\phi_v`, or use the full history-conditioned terms of (4.1) when coarse local statistics are insufficient.

The mandatory recursive-majority obstruction is passed by the **full** tree mechanism: (6.3) retains all scales and (6.4) recovers the rare-event logarithm. What remains is a genuinely Boolean structural inequality for arbitrary sources, especially composition-prime ones. This report does not assert that arbitrary Boolean spectra admit a tree whose coarse local statistics alone close that inequality.

## 8. Status and provenance

- `FEI-PHYSICAL-KL-TREE-v1`: **PROVED_IN_THIS_REPORT** (elementary KL chain rule plus product-reference conditioning).
- Recursive-majority identity (6.3): **PROVED_IN_THIS_REPORT**, conditional only on the source-reported exact spectral branching law of fleet03/B18.
- Bottom-scale lower bound (6.4): **PROVED_IN_THIS_REPORT**.
- `FEI-TREE-PAY-BINF-v1`: **OPEN**.
- Full FEI: **OPEN / NOT PROVED**.
- No counterexample to FEI is claimed.
- No native brain retrieval occurred; repository synchronization is not native ingestion.
