# ProofNet24 R19 — separable free-group-factor isomorphism

**Run:** `2026-09-16_13-04-33_UTC__R19__free-shift-tor-obstruction`  
**Repository / branch:** `yspennstate/math-open-problems` / `master`  
**Target:** decide whether the separable II_1 factors `L(F_m)` and `L(F_n)` are isomorphic for distinct `2 <= m,n <= infinity`, first `L(F_2)` versus `L(F_3)`.  
**Status:** **OPEN. NO CLOSURE CLAIM.**

## 0. Repository continuity and scope

Before doing mathematics I read directly from `master`:

- root `README.md`, blob `9d18531dff608e0165fe4434614d8c9121903c4c`;
- `proofnet24/HOURLY20_PROTOCOL_2026-09-16.md`, blob `47be24f8b98068e74eee3e21b703ad58fa371c5c`.

The protocol assigns R19 to `proofnet24/R19-free-group-factors` and requires a new immutable report plus run-specific artifacts.

The assigned target folder did **not** yet exist on `master`: a direct contents lookup returned 404, and repository code search found the path only in the hourly protocol, not an existing target report. Therefore this run creates the canonical GitHub target folder. I do **not** import off-repository chat/Drive state as if it were repository proof state.

Because there was no pre-existing GitHub claim ledger for this target, this report starts a GitHub-local stable claim namespace `R19-GH-*`. Later GitHub runs should retain these IDs.

Useful repository research actually read:

1. `proofnet24/P20-kernel-hard-edge/runs/2026-09-15/2026-09-15_19-50-10__run-report.md`, blob `00f07dd0df2029d64bccf7d6457be3559b741cfc`;
2. `proofnet24/P13-fourth-moment-RMT/runs/2026-09-15/2026-09-15_19-02-20__run-report.md`, blob `98929dcdbcf16379bf490f658a78bbc157fa4a8e`;
3. Shmalo hard-edge material in `paper19/`, including `paper19/extremal_hard_edge.tex` and `paper19/PLAN.md`.

The expected new-protocol R02/R03 target folders were not present under their assigned paths when queried. Missing peer state is nonblocking; I did not invent peer outputs.

---

# 1. Current primary-literature status

## `R19-GH-K001` — Dykema/Rădulescu all-or-none reduction

**Status: KNOWN / VERIFIED.**

Dykema, *Interpolated free group factors*, Pacific J. Math. 163 (1994), constructs `L(F_r)`, `1<r<=infinity`, with the amplification law

\[
L(\mathbb F_r)^t\cong
L\!\left(\mathbb F_{1+(r-1)/t^2}\right).
\tag{1.1}
\]

Dykema explicitly records the resulting dichotomy (and Rădulescu's independent construction): either all finite-rank free group factors are mutually isomorphic, or no two distinct ranks are isomorphic.

For the first case,

\[
1+\frac{2-1}{(1/\sqrt2)^2}=3,
\]
so

\[
\boxed{L(\mathbb F_2)^{1/\sqrt2}\cong L(\mathbb F_3).}
\tag{1.2}
\]

Thus `L(F_2) ~= L(F_3)` is exactly a nontrivial self-amplification question for `L(F_2)`, but (1.2) is **not** itself the desired isomorphism.

Primary source: Dykema, arXiv `funct-an/9211012` / Pacific J. Math. 163 (1994).

## `R19-GH-K002` — BDIP scope

**Status: KNOWN / VERIFIED SCOPE.**

Boutonnet--Drimbe--Ioana--Popa, GAFA 34 (2024), DOI `10.1007/s00039-024-00669-8`, prove the analogue for a **non-separable** diffuse abelian von Neumann algebra `A`: the free powers `A^{*n}` are mutually non-isomorphic. Their introduction explicitly singles out `A=L(Z)` as the separable classical free-group-factor case and does not claim to solve it.

A decisive barrier to transplanting their cardinal core unchanged is their Remark 2.7: the ordinary singular-abelian rank has cardinality `c` for every separable II_1 factor, so bare counting of disjoint singular MASAs cannot distinguish `L(F_2)` from `L(F_3)`.

## `R19-GH-K003` — newest directly relevant isomorphism theorem checked

**Status: KNOWN / VERIFIED SCOPE.**

D. Shlyakhtenko, *On the II_1 Factors of Fuchsian Groups*, arXiv:2609.11074, submitted 10 September 2026, proves

\[
L(\pi_1\Sigma_g)\cong L(\mathbb F_{2g-1})
\]

for closed orientable surface groups and, crucially,

\[
L(\mathbb F_2)=W^*(w)*W^*(v),
\qquad
w=ABA^{-1}B^{-1},
\tag{1.3}
\]

for a Haar unitary `v` free from the commutator `w`. This is a strong new free-complementation theorem, but it compares a specified surface/Fuchsian factor with a specified free rank; it does not compare two distinct free ranks.

No public source found in this run closes the usual separable problem.

---

# 2. A rigorous obstruction to normalizing divergent approximate-relation Jacobians

## `R19-GH-C001` — escape-to-infinity normalization lemma

**Status: PROVED.**

Let `(N,tau)` be a finite von Neumann algebra. Let `T_n >= 0` be positive affiliated operators such that

\[
\forall R<\infty,\qquad
\tau(1_{[0,R]}(T_n))\longrightarrow 0.
\tag{2.1}
\]

Thus `T_n -> infinity` in measure. Let `a_n in N` satisfy

\[
\sup_n\|a_n\|_\infty\le C<\infty,
\qquad
\sup_n\|a_nT_n\|_2\le K<\infty.
\tag{2.2}
\]

Then

\[
\boxed{\|a_n\|_2\longrightarrow0.}
\tag{2.3}
\]

### Proof

Fix `R>0` and put

\[
e_{n,R}=1_{[0,R]}(T_n),\qquad f_{n,R}=1-e_{n,R}.
\]

The low-slope part satisfies

\[
\|a_ne_{n,R}\|_2
\le C\,\tau(e_{n,R})^{1/2}.
\tag{2.4}
\]

On `f_{n,R}`, the inverse `T_n^{-1}f_{n,R}` is bounded with operator norm at most `R^{-1}`. Since this inverse is a Borel function of `T_n`,

\[
a_nf_{n,R}
=
(a_nT_nf_{n,R})(T_n^{-1}f_{n,R}),
\]

so

\[
\|a_nf_{n,R}\|_2
\le \frac{K}{R}.
\tag{2.5}
\]

Hence

\[
\limsup_n\|a_n\|_2
\le \frac K R
\]

by (2.1). Let `R -> infinity` to get (2.3). QED.

### Application to the universal smoothing idea

Suppose one tries to approximate an arbitrary `y in W^*(X)` by algebraic `p_n(X)` and uses approximate graph relations

\[
q_n(X,y)=y-p_n(X)\to0.
\tag{2.6}
\]

The Jacobian row is schematically

\[
(-Jp_n,\ 1).
\]

For a one-row relation put

\[
T_n=(Jp_n(Jp_n)^*)^{1/2}.
\]

If `T_n` escapes to infinity in measure, then any uniformly bounded left normalizers `a_n` for which the old-variable row `a_nJp_n` stays `L^2`-bounded satisfy

\[
\|a_n\|_2\to0.
\]

Therefore the normalized coefficient of the **new** variable `y` disappears in `L^2`, and hence weakly. The approximate relation can lose exactly the rank direction it was supposed to certify.

This gives a rigorous reason the naive Ornstein--Uhlenbeck / polynomial-smoothing route cannot establish universal W*-monotonicity merely by normalizing exploding Jacobians.

**Important scope.** C001 requires (2.1), a uniform `L^infty` bound on the row normalizers, and an `L^2` bound on the normalized old Jacobian. It does not say every approximation has slope escape; it identifies what happens when it does.

---

# 3. Homological reformulation: scalar extension can create a kernel

## `R19-GH-C002` — Tor controls loss of injectivity after scalar extension

**Status: PROVED ALGEBRAIC LEMMA.**

Let `R` be a ring and let

\[
0\longrightarrow S_B\xrightarrow{r}S_A\longrightarrow C\longrightarrow0
\tag{3.1}
\]

be an exact sequence of right `R`-modules. Let `Q` be a left `R`-module. Then the long exact Tor sequence gives

\[
\operatorname{Tor}_1^R(C,Q)
\xrightarrow{\partial}
S_B\otimes_RQ
\xrightarrow{r\otimes1}
S_A\otimes_RQ,
\tag{3.2}
\]

with

\[
\boxed{
\ker(r\otimes1)=\operatorname{im}\partial.
}
\tag{3.3}
\]

Thus an algebraically injective restriction map can acquire a kernel after scalar extension precisely through a first-Tor defect.

The run-specific checker includes the elementary model

\[
0\to\mathbb Z\xrightarrow{\times2}\mathbb Z\to\mathbb Z/2\to0.
\]

Tensoring with `Z/2` turns multiplication by two into the zero map; the new kernel is exactly accounted for by

\[
\operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/2,\mathbb Z/2)
\cong \mathbb Z/2.
\]

## `R19-GH-R001` — conditional Stein/Tor bridge

**Status: CONDITIONAL REDUCTION, NOT A THEOREM YET.**

For the free group algebra

\[
A_0=\mathbb C[\mathbb F_2],
\]

the natural coefficient ring for derivations is

\[
R=A_0\otimes A_0^{op}
\cong \mathbb C[\mathbb F_2\times\mathbb F_2],
\tag{3.4}
\]

whereas the completed coarse coefficient algebra is

\[
N=L(\mathbb F_2)\bar\otimes L(\mathbb F_2)^{op}
\cong L(\mathbb F_2\times\mathbb F_2).
\tag{3.5}
\]

Actual Stein derivations form algebraic `R`-modules, while free Stein dimension is measured after an `N`-Hilbert-module closure. This strongly suggests that the vertical completion kernel should be expressible as an image of a Tor defect for scalar extension `R -> N`.

The missing theorem is an identification, up to Murray--von Neumann dimension zero, between the actual closed Stein module and the appropriate dimension-completion of

\[
S_A\otimes_RN.
\]

If such an identification is proved compatibly for `A subset B`, then C002 would give

\[
\kappa_A(B)
\le
\dim_N\operatorname{Tor}_1^R(C,N)
\tag{3.6}
\]

for the Stein restriction cokernel `C` (more precisely, `kappa` would be the dimension of the image of the boundary map in (3.2)).

I do **not** claim (3.6) unconditionally in this run.

### Why blanket dimension-flatness is not available

Lueck proved dimension-flatness of `C Gamma -> L Gamma` for amenable groups. Kyed--Petersen, *A groupoid approach to Lueck's amenability conjecture* (arXiv:1205.1930), prove converse dimension-flatness characterizations for natural **groupoid / group-measure-space** inclusions associated to actions of nonamenable groups, including explicit positive first-Tor obstructions. Their paper also carefully distinguishes these action-ring inclusions from the bare group-ring inclusion in places where a natural nonflatness statement is unavailable.

Since `F_2 x F_2` is nonamenable, no amenable flatness theorem applies to (3.4)--(3.5). This route therefore needs an honest module-specific theorem; one cannot erase the completion obstruction by citing generic flatness.

This is a useful narrowing rather than a solution.

---

# 4. Constructive route: a very close internal `L(F_2)` complement that fails one mixed moment

Shlyakhtenko's new theorem (1.3) makes it natural to try to thicken the abelian complement `W^*(v)` into an internal copy of `L(F_2)` while keeping freeness from `W^*(w)`.

## `R19-GH-C003` — conjugate-complement near miss

**Status: PROVED.**

Let `u,v` be free Haar unitaries and

\[
M=W^*(u)*W^*(v)\cong L(\mathbb F_2).
\]

Put

\[
v_0=v,
\qquad
v_1=uvu^*.
\tag{4.1}
\]

Then:

1. `v_0` and `v_1` are free Haar unitaries;
2. therefore
   \[
   P:=W^*(v_0,v_1)\cong L(\mathbb F_2);
   \tag{4.2}
   \]
3. `W^*(u) vee P=M` because `v=v_0 in P`;
4. nevertheless `W^*(u)` and `P` are **not free**.

### Proof of 1

Identify `u,v` with the canonical group unitaries `a,b` in `L(F(a,b))`. The kernel of the exponent-sum map

\[
F(a,b)\to\mathbb Z,
\qquad a\mapsto1,\quad b\mapsto0,
\]

has Schreier free basis

\[
\{a^kba^{-k}:k\in\mathbb Z\}.
\tag{4.3}
\]

Thus `b` and `aba^{-1}` freely generate `F_2`, proving that `v_0,v_1` are free Haar.

### Proof of 4: exact alternating-moment obstruction

The four elements

\[
u,\quad v,\quad u^*,\quad v_1^*
\]

are centered and alternate between `W^*(u)` and `P`. If those two algebras were free, their product would have trace zero. But

\[
uv u^*v_1^*
=uvu^*(uvu^*)^*
=1,
\]

so

\[
\boxed{\tau(uv u^*v_1^*)=1.}
\tag{4.4}
\]

Hence they are not free.

### Consequence for Shlyakhtenko's commutator complement

Take `u=w=[A,B]` and the Haar complement `v` supplied by arXiv:2609.11074. Then

\[
P=W^*(v,wvw^*)\cong L(\mathbb F_2)
\]

is an internal rank-two free group factor and

\[
W^*(w)\vee P=L(\mathbb F_2),
\]

but (4.4) proves that it is **not** a free complement. Thus the most obvious way of thickening Shlyakhtenko's abelian complement fails by one explicit centered alternating moment.

This is a constructive near miss, not merely a dimension count.

---

# 5. Exact crossed-product/free-shift reformulation of all finite ranks

## `R19-GH-C004` — free-shift crossed-product model

**Status: PROVED (group-theoretic / standard).**

Write

\[
\mathbb F_n
=\langle a,b_1,\ldots,b_{n-1}\rangle,
\qquad n\ge2,
\]

and let

\[
\pi_n:\mathbb F_n\to\mathbb Z,
\qquad
\pi_n(a)=1,
\quad
\pi_n(b_i)=0.
\]

The kernel `K_n=ker pi_n` has Schreier free basis

\[
\boxed{
\{a^k b_i a^{-k}:
 k\in\mathbb Z,\ 1\le i\le n-1\}.
}
\tag{5.1}
\]

Hence `K_n ~= F_infinity`, and

\[
\mathbb F_n=K_n\rtimes\langle a\rangle.
\tag{5.2}
\]

On von Neumann algebras,

\[
\boxed{
L(\mathbb F_n)
\cong
L(\mathbb F_\infty)\rtimes_{\alpha_{n-1}}\mathbb Z,
}
\tag{5.3}
\]

where `alpha_{n-1}` shifts the integer index `k` in each of the `n-1` Schreier orbits.

Grouping the `n-1` generators at each integer gives

\[
L(\mathbb F_\infty)
\cong
*_{k\in\mathbb Z} B_k,
\qquad
B_k\cong L(\mathbb F_{n-1})
\tag{5.4}
\]

(with `B_k ~= L(Z)` when `n=2`), and `alpha_{n-1}(B_k)=B_{k+1}`. Thus `alpha_{n-1}` is the free-product/free-Bernoulli shift with base `L(F_{n-1})`.

### Constructive criterion

If the multiplicity-one and multiplicity-two free shifts

\[
\alpha_1,\alpha_2\curvearrowright L(\mathbb F_\infty)
\]

were cocycle conjugate, their crossed products would be isomorphic, yielding

\[
L(\mathbb F_2)\cong L(\mathbb F_3).
\tag{5.5}
\]

The converse does **not** follow without proving that an arbitrary factor isomorphism preserves (or reconstructs) this crossed-product core.

## `R19-GH-X001` — standard dynamical entropy does not distinguish these free shifts

**Status: KNOWN ROUTE OBSTRUCTION / VERIFIED LITERATURE.**

Størmer proved that the free shift on `L(F_infinity)` has trace entropy zero; later free-product entropy results of Choda and Brown--Dykema--Shlyakhtenko show zero entropy for broad free shifts. In particular, the obvious operator-algebra dynamical entropy does not record the number of free base generators in (5.4).

Thus (5.3) is a useful constructive reformulation, but ordinary free-shift entropy is not the missing rank invariant.

References checked:

- E. Størmer, survey *Entropy in operator algebras*, theorem recording `H(alpha)=0` for the free shift on `L(F_infinity)`;
- M. Choda, *Reduced Free Products of Completely Positive Maps and Entropy for Free Product of Automorphisms*, PRIMS 32 (1996);
- N. Brown--K. Dykema--D. Shlyakhtenko, free-product automorphism entropy work.

---

# 6. Hard-edge / microstate implications

The repository's Shmalo hard-edge work is genuinely useful, but only after an invariant target is fixed.

`paper19/extremal_hard_edge.tex` develops precise least-singular-value tails and extremal selection laws for Gaussian/subgaussian matrix families. P20's hard-edge audit shows repeatedly that a scalar or alternating-sector comparison can miss the amplitude/symmetric coupling controlling the endpoint. P13's `P13-MICROJITTER-TRANSFER-30` likewise stresses a scale principle directly relevant here: Weyl transfer is legitimate only when the **entire perturbation** lies below the microscopic target scale.

C001 supplies the analogous operator-algebra warning: if a polynomial graph approximation has derivative slope escaping to infinity, bounded normalization can erase the new-variable coefficient. Therefore a hard-edge calculation on canonical generators cannot be promoted to a W*-invariant unless the approximation theorem controls the full graph, not only moments or relation values.

The next legitimate finite-matrix target is a singular-value statistic for a graph/restriction operator whose zero-mass limit has already been identified with a factor-level module dimension. A raw exponent of `Jp(X)` is not enough.

---

# 7. Independent peer audit actually performed

## P20 exterior-quadratic consequence

Source actually read:

`proofnet24/P20-kernel-hard-edge/runs/2026-09-15/2026-09-15_19-50-10__run-report.md`, blob `00f07dd0df2029d64bccf7d6457be3559b741cfc`.

P20 proves an exact first-moment exterior law

\[
\mathbb E\,|\Omega\rangle\langle\Omega|
=\frac1D I
\tag{7.1}
\]

on an exterior space of dimension `D`, and concludes for every deterministic linear map `A`

\[
\mathbb E\|A\Omega\|^2
=\frac1D\|A\|_{HS}^2.
\tag{7.2}
\]

I independently checked the implication exactly:

\[
\mathbb E\|A\Omega\|^2
=\mathbb E\operatorname{Tr}(A^*A|\Omega\rangle\langle\Omega|)
=\operatorname{Tr}\left(A^*A\frac{I}{D}\right)
=\frac{\|A\|_{HS}^2}{D}.
\]

The run checker additionally performs a finite Haar-sphere Monte Carlo sanity check. The exact trace derivation above is the proof; the Monte Carlo is not being counted as proof.

## P13 methodological check

Source actually read:

`proofnet24/P13-fourth-moment-RMT/runs/2026-09-15/2026-09-15_19-02-20__run-report.md`, blob `98929dcdbcf16379bf490f658a78bbc157fa4a8e`.

The relevant imported lesson, not theorem, is `P13-MICROJITTER-TRANSFER-30`: perturbative transfer at a hard edge needs perturbation below the microscopic target scale. This is consistent with C001 and with the requirement that an R19 finite-matrix compiler control the full graph/restriction operator.

No P13/P20 conjectural closure statement is imported into R19.

---

# 8. Reproducibility artifact

Run-specific checker:

`proofnet24/R19-free-group-factors/artifacts/2026-09-16_13-04-33_UTC__R19__free-shift-tor-obstruction__checks.py`

Seed:

`20260916130433`.

It checks:

1. Dykema's `r=2`, `t=1/sqrt(2)` arithmetic;
2. finite diagonal models for C001;
3. the `Z --x2--> Z` non-flat tensor/Tor toy model for C002;
4. free-group reduction for C003 through reduced words of length eight;
5. finite Schreier/free-shift packets for C004;
6. the P20 exterior-quadratic consequence numerically as a sanity check.

Output certificate SHA-256:

`07a7b966b6d1e9dda9024502fc3befcceaa3fafac934f8ee29f8209b5a51d71f`.

Finite checks are certificates/diagnostics only and are explicitly separated from the proofs.

---

# 9. Cumulative GitHub-local ledger

| ID | Status | Claim |
|---|---|---|
| `R19-GH-K001` | **KNOWN / VERIFIED** | Dykema--Rădulescu interpolation and all-or-none reduction; `L(F2)^(1/sqrt2) ~= L(F3)`. |
| `R19-GH-K002` | **KNOWN / VERIFIED SCOPE** | BDIP solves only the non-separable analogue; separable singular-MASA cardinality collapses. |
| `R19-GH-K003` | **KNOWN / VERIFIED SCOPE** | Shlyakhtenko 2026 Fuchsian theorem and commutator free complement do not compare distinct free ranks. |
| `R19-GH-C001` | **PROVED** | Escape-to-infinity normalization lemma; bounded normalization of exploding graph slopes kills the new-coordinate coefficient. |
| `R19-GH-C002` | **PROVED ALGEBRAIC** | Kernel created by scalar extension is the image of a first-Tor boundary. |
| `R19-GH-R001` | **CONDITIONAL** | Stein vertical completion may be controlled by a Tor defect if the closed Stein module is dimension-identified with scalar extension; this identification remains unproved. |
| `R19-GH-C003` | **PROVED** | `P=W*(v,uvu*) ~= L(F2)` is an internal nonabelian thickening of an abelian complement, but is not free from `W*(u)`; exact alternating moment equals 1. |
| `R19-GH-C004` | **PROVED / STANDARD** | `L(F_n) ~= L(F_infinity) rtimes_{alpha_{n-1}} Z` with `n-1`-orbit free shift. |
| `R19-GH-X001` | **KNOWN ROUTE OBSTRUCTION** | Standard free-shift entropy is zero and does not distinguish the multiplicity in C004. |

## OPEN obligations

1. `L(F_2) ?~= L(F_3)`.
2. A genuinely W*-intrinsic invariant taking different values at free ranks 2 and 3.
3. A proof that a finite-matrix graph/restriction singular statistic converges to such an invariant under arbitrary generator changes and W*-closure.
4. A quantitative **separable** replacement for BDIP's non-separable sans-rank.
5. A constructive thickening of Shlyakhtenko's `W*(w)` complement to an `L(F2)` free complement, avoiding the exact obstruction in C003.
6. The missing dimension-completion theorem needed to turn R001 into an unconditional Tor formula.

---

# 10. Failed routes retained exactly

1. **Reduced group C*-algebras.** Irrelevant target: these can be distinguished without solving the W*-problem.
2. **Canonical-generator free entropy / free entropy dimension alone.** No W*-invariance theorem, hence no rank conclusion.
3. **Approximate relations by smoothing alone.** C001 shows a precise rank-loss mechanism when graph slopes escape to infinity.
4. **Bare singular-MASA cardinality.** BDIP Remark 2.7 makes it universal (`c`) in the separable II_1 category.
5. **Thicken Shlyakhtenko's complement by conjugation.** C003 creates an internal `L(F2)` but an explicit alternating moment is 1, so joint freeness fails.
6. **Free-shift entropy.** Zero for the relevant highly noncommutative shifts; it does not detect shift multiplicity.
7. **Blanket scalar-extension flatness.** Amenable dimension-flatness cannot simply be invoked for `F2 x F2`; the Stein-specific Tor/closure identification is still missing.

---

# 11. Next attack

The strongest next two directions are now sharply stated.

## A. Homological completion attack

Prove or disprove a dimension-completion theorem for the canonical map

\[
S_A\otimes_{A^e}N\longrightarrow H_A,
\qquad
A^e=A\otimes A^{op},\quad N=M\bar\otimes M^{op},
\]

where `S_A` is the algebraic Stein-derivation module and `H_A` its closed free-Stein Hilbert module. The goal is to identify the vertical completion kernel for `A subset B` with an explicit image of

\[
\operatorname{Tor}_1^{A^e}(C,N).
\]

For `A=C[F2]`, the coefficient ring is exactly `C[F2 x F2]`. This would convert the W*-completion defect into a homological object with a canonical Murray--von Neumann dimension.

The first subtask is to characterize the kernel of the realization map

\[
S_A\otimes_{A^e}N\to L^2(N)^{|X|}
\]

and determine whether that kernel has zero `N`-dimension for the free group algebra. This is not currently proved.

## B. Constructive free-shift/core attack

Use the exact model

\[
L(F_n)=L(F_\infty)\rtimes_{\alpha_{n-1}}\mathbb Z.
\]

For `n=2,3`, seek an intrinsic W*-characterization of the canonical `L(F_infinity)` normal core, or an invariant of the inclusion/core-action pair that survives arbitrary crossed-product isomorphism. Ordinary entropy is ruled out by X001.

On Shlyakhtenko's side, any candidate second complement produced from `v` by conjugating with `W*(w)` is ruled out by C003. A successful construction must produce genuinely new degrees of freedom, not merely the Schreier conjugate family `w^k v w^{-k}`.

These two directions are logically independent: the first aims for non-isomorphism through an invariant; the second for a constructive isomorphism or a rigid obstruction to one.

**No full solution is claimed.**

---

# Primary references checked this run

- K. Dykema, *Interpolated free group factors*, Pacific J. Math. 163 (1994); arXiv:funct-an/9211012.
- F. Rădulescu, independent interpolated free-group-factor construction and compression formula.
- S. Popa, historical account, *Revisiting On Rings of Operators IV and the problems therein* (2020): https://sorintpopa.wordpress.com/2020/01/16/revisiting-on-rings-of-operators-iv-and-the-problems-therein/
- R. Boutonnet, D. Drimbe, A. Ioana, S. Popa, *Non-isomorphism of A^{*n}, 2<=n<=infinity, for a non-separable abelian von Neumann algebra A*, GAFA 34 (2024), DOI 10.1007/s00039-024-00669-8.
- I. Charlesworth, B. Nelson, *On Free Stein Dimension*, Indiana Univ. Math. J. 74 (2025).
- D. Kyed, H. D. Petersen, *A groupoid approach to Lueck's amenability conjecture*, arXiv:1205.1930.
- D. Shlyakhtenko, *On the II_1 Factors of Fuchsian Groups*, arXiv:2609.11074 (10 Sep 2026).
- E. Størmer; M. Choda; N. Brown--K. Dykema--D. Shlyakhtenko, free-shift/free-product entropy results.
