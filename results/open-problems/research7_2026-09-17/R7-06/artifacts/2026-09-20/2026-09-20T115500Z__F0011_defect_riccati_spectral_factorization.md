Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — the owner's GPT-6 / maximum-reasoning request remains a preference, not verified runtime telemetry.

# F0011 — defect Riccati identity, exact plateau, and integral spectral factorization

Date: 2026-09-20 UTC  
Role: C05 / R7-06 `Random Matrix Spectral Entropy`  
Canonical target: F0011 / Van H. Vu, *Recent progress in combinatorial random matrix theory*, Probability Surveys 18 (2021), Conjecture 9.4  
Status: **PROVED PARTIAL** toward the outside source, pending later independent review

## 1. Source target and exact inherited point

Vu's Conjecture 9.4 concerns the symmetric Rademacher matrix `M_n^sym`, with independent fair signs on and above the diagonal:

\[
\Pr\bigl(\operatorname{Spec}(M_n^{\rm sym})\subset\mathbb Z\bigr)
=2^{-(1/2+o(1))n^2}.
\]

Equivalently, the total number of labelled symmetric sign matrices with integral spectrum should be `2^{o(n^2)}`. The source does **not** fix a spectrum. The active C05 line is a restricted bridge through the centered two-eigenvalue / symmetric-Hadamard family.

The immediately inherited shell is the `|r-lambda|=4`, one-parity, low-rank branch after two-sided quotienting. It produces

\[
T,S\in\{-1,0,1\}^{d\times d},\qquad d=r-q,
\]

with

\[
TS=ST=sI_d,\qquad s=r/4-\varepsilon>0,
\tag{1.1}
\]

and inverse defect

\[
D:=T-S^T\in\{-1,0,1\}^{d\times d},
\qquad k:=\operatorname{rank}D\le 2q=o(r).
\tag{1.2}
\]

The preceding run proved that `D` itself has only subquadratic description entropy, although its support occupies asymptotically half of the core. The missing theorem was to exploit the exact equation `T-sT^{-T}=D` inside a fixed defect fiber.

The original cross-block `C` need not be invertible: in the negative shell, singular exceptional quotient modes are allowed. The contrast core `T` *is* invertible by (1.1), so the argument below preserves that singular/corank endpoint rather than excluding it.

---

## 2. Main theorem I — a basis-free Riccati identity

Since `S=sT^{-1}`, (1.2) is exactly

\[
D=T-sT^{-T}.
\tag{2.1}
\]

Put

\[
A:=T^TT\succ0,
\qquad
B:=D^TD\succeq0.
\]

Because

\[
T^{-T}=T(T^TT)^{-1}=TA^{-1},
\]

we have

\[
D=T(I-sA^{-1}).
\]

Therefore

\[
\boxed{
B=A-2sI+s^2A^{-1}.
}
\tag{2.2}
\]

Equivalently,

\[
\boxed{
AB=BA=(A-sI)^2.
}
\tag{2.3}
\]

This has several immediate consequences.

### Exact plateau, not just a rank upper bound

The factor `TA^{-1}` in

\[
D=TA^{-1}(A-sI)
\]

is invertible. Hence

\[
\boxed{
\operatorname{rank}(A-sI)=\operatorname{rank}D=k,
\qquad
\ker(A-sI)=\ker D.
}
\tag{2.4}
\]

Thus `T` has singular value `sqrt(s)` with **exact multiplicity**

\[
\boxed{d-k.}
\tag{2.5}
\]

The preceding run only needed the weaker inherited lower bound `d-2q`; the exact defect rank is the correct parameter.

The left-hand version is identical. If

\[
\widetilde A:=TT^T,
\qquad \widetilde B:=DD^T,
\]

then

\[
\boxed{
\widetilde B=\widetilde A-2sI+s^2\widetilde A^{-1},
\qquad
\ker(\widetilde A-sI)=\ker D^T.
}
\tag{2.6}
\]

Consequently

\[
\boxed{
T:\ker D\longrightarrow\ker D^T
}
\]

is exactly a `sqrt(s)`-scaled isometry.

This is the first basis-free localization of the surviving large-dimensional freedom: every non-flat singular direction is confined to the `k=o(r)` dimensional defect sector.

---

## 3. Main theorem II — complete real normal form for a fixed defect

Let

\[
D=U\Sigma V^T
\]

be an SVD, with `Sigma=diag(sigma_1,...,sigma_d)` and nonnegative singular values. Recall the inherited midpoint

\[
X:=T-D/2=(T+S^T)/2.
\]

The previous run proved

\[
XX^T=sI+DD^T/4,
\qquad
X^TX=sI+D^TD/4.
\tag{3.1}
\]

The cross terms also satisfy

\[
\boxed{XD^T=DX^T,\qquad X^TD=D^TX.}
\tag{3.2}
\]

Indeed, from `(T-D)T^T=sI` and `T^T(T-D)=sI`, the matrices `DT^T` and `T^TD` are symmetric; subtracting `DD^T/2` and `D^TD/2` gives (3.2).

Set

\[
Y:=U^TXV.
\]

Then (3.2) becomes

\[
Y\Sigma=\Sigma Y^T,
\qquad
Y^T\Sigma=\Sigma Y,
\tag{3.3}
\]

while (3.1) becomes

\[
YY^T=Y^TY=sI+\Sigma^2/4.
\tag{3.4}
\]

For matrix entries, (3.3) gives

\[
Y_{ij}\sigma_j=\sigma_iY_{ji},
\qquad
Y_{ji}\sigma_j=\sigma_iY_{ij}.
\]

Therefore:

* if `sigma_i != sigma_j`, then `Y_ij=0`;
* on a positive singular-value block `sigma>0`, `Y` is symmetric;
* on the zero singular-value block, (3.3) imposes no additional condition.

Let `m_sigma` be the multiplicity of a distinct positive singular value `sigma`, and let `m_0=d-k`. Then every real solution of the fixed-defect equation has the form

\[
\boxed{
Y=
\left(\bigoplus_{\sigma>0}
\sqrt{s+\sigma^2/4}\,J_\sigma\right)
\oplus
\sqrt{s}\,O_0,
}
\tag{3.5}
\]

where each

\[
J_\sigma=J_\sigma^T,\qquad J_\sigma^2=I_{m_\sigma}
\]

is a symmetric orthogonal involution and

\[
O_0\in O(m_0)
\]

is arbitrary. Finally

\[
\boxed{T=U(Y+\Sigma/2)V^T,\qquad S^T=U(Y-\Sigma/2)V^T.}
\tag{3.6}
\]

So the real solution manifold for a fixed `D` splits exactly into:

1. an exceptional sector of total dimension `k`, where the only freedom is a collection of symmetric involutions; and
2. the flat sector `ker D -> ker D^T`, where the freedom is a scaled orthogonal map.

The positive-`sigma` part has real dimension at most

\[
\sum_{\sigma>0}\left\lfloor\frac{m_\sigma^2}{4}\right\rfloor
\le \frac{k^2}{4},
\]

while the zero block contributes

\[
\frac{(d-k)(d-k-1)}2.
\]

This proves rigorously that the only genuinely quadratic real freedom is the kernel orthogonal sector. The ternary condition must therefore kill or recursively organize that sector; no further real degrees of freedom are hiding in the exceptional modes.

### Reciprocal singular-value pairing

On a positive `sigma` block put

\[
a_\sigma:=\sqrt{s+\sigma^2/4}.
\]

If `J_sigma` has `+1` multiplicity `p_sigma`, then the singular values of `T` on this block are

\[
\boxed{
a_\sigma+\sigma/2}
\qquad\text{and}\qquad
\boxed{a_\sigma-\sigma/2},
\tag{3.7}
\]

with multiplicities `p_sigma` and `m_sigma-p_sigma`. Their product is exactly

\[
\boxed{
(a_\sigma+\sigma/2)(a_\sigma-\sigma/2)=s.
}
\tag{3.8}
\]

Thus every non-flat singular value is paired with its `s`-reciprocal.

---

## 4. Main theorem III — an integral spectral factorization attached to `D`

Equation (2.2) yields a polynomial matrix identity. For an indeterminate `x`,

\[
\begin{aligned}
(xI-A)(xI-s^2A^{-1})
&=x^2I-x(A+s^2A^{-1})+s^2I\\
&=(x-s)^2I-xB.
\end{aligned}
\]

Hence

\[
\boxed{
\det\bigl((x-s)^2I-xD^TD\bigr)
=\chi_{T^TT}(x)\,\chi_{SS^T}(x).
}
\tag{4.1}
\]

Both factors on the right are monic polynomials in `Z[x]`, because `T` and `S` are integer matrices.

Since `rank(D)=k`, the left side has the exact factor

\[
(x-s)^{2(d-k)}.
\]

By (2.4), each Gram characteristic polynomial on the right has exactly the factor `(x-s)^(d-k)`. Define the degree-`2k` residual defect polynomial

\[
\boxed{
R_D(x):=
\frac{\det((x-s)^2I-xD^TD)}{(x-s)^{2(d-k)}}\in\mathbb Z[x].
}
\tag{4.2}
\]

Then there are monic `f_T,g_T in Z[x]`, each of degree `k`, such that

\[
\boxed{
\chi_{T^TT}(x)=(x-s)^{d-k}f_T(x),
}
\tag{4.3}
\]

\[
\boxed{
\chi_{SS^T}(x)=(x-s)^{d-k}g_T(x),
}
\tag{4.4}
\]

and

\[
\boxed{
R_D(x)=f_T(x)g_T(x).
}
\tag{4.5}
\]

This is an **exact integral spectral-factorization obstruction** for every fixed defect.

### Fixed-defect spectrum count

Factor `R_D` into monic irreducibles in `Z[x]`:

\[
R_D=\prod_i h_i^{e_i}.
\]

Any possible `f_T` is a monic integral divisor of degree `k`, so the number of candidates is at most

\[
\prod_i(e_i+1).
\]

Because

\[
\sum_i e_i\deg h_i=2k
\]

and `e+1<=2^e`,

\[
\boxed{
\#\{\chi_{T^TT}: D\text{ fixed}\}
\le 2^{2k}=4^k.
}
\tag{4.6}
\]

In the inherited regime `k<=2q=o(r)`, this is only `2^{o(r)}` possibilities for the singular spectrum **inside one fixed defect fiber**.

This is much sharper than merely saying that all Gram skeletons have subquadratic entropy. Once `D` is fixed, the singular values of the ternary core cannot carry quadratic entropy at all.

### Exact rejection certificate

A necessary condition for a ternary inverse pair over a candidate defect `D` is:

\[
\boxed{
R_D(x)\text{ has a monic degree-}k\text{ factor in }\mathbb Z[x].
}
\tag{4.7}
\]

Thus, for example, if `R_D` is irreducible over `Q` and `k>0`, the candidate defect admits **no** such root. This gives an exact arbitrary-size certificate that can be checked without enumerating ternary roots.

The criterion is useful even when `D^TD` has irrational algebraic eigenvalues; it does not assume integral singular squares.

---

## 5. Arithmetic corollary for an integral singular square

Suppose `tau>0` is an **integer** eigenvalue of `D^TD` of multiplicity `m`. On its eigenspace, (2.3) says that every eigenvalue `theta` of `A=T^TT` satisfies

\[
\theta^2-(2s+\tau)\theta+s^2=0.
\tag{5.1}
\]

The discriminant is

\[
\Delta_\tau=\tau(\tau+4s).
\tag{5.2}
\]

If `Delta_tau` is not a square, the quadratic (5.1) is irreducible over `Q`. Since `chi_A in Z[x]`, its two conjugate roots must appear with equal multiplicity inside this `tau` block. Therefore

\[
\boxed{
\Delta_\tau\notin\square
\Longrightarrow
m\text{ is even and the two reciprocal }A\text{-roots each occur }m/2\text{ times}.
}
\tag{5.3}
\]

In particular, an integer `tau` of odd multiplicity forces

\[
\boxed{
\tau(\tau+4s)=z^2
}
\tag{5.4}
\]

for some integer `z`.

This Diophantine condition has a divisor parametrization:

\[
(\tau+2s-z)(\tau+2s+z)=4s^2.
\tag{5.5}
\]

Hence all odd-multiplicity integer singular squares lie in a list controlled by divisor pairs of `4s^2`; in particular there are at most `tau(4s^2)` such positive values, where `tau(.)` is the divisor-counting function. The point is not the precise divisor-function bound but the collapse from an interval of possible singular squares to a thin arithmetic list.

---

## 6. Entropy consequence and what remains genuinely hard

The preceding run already proved that, over the inherited `q=o(r)` shell,

* the signed row/column partitions have `2^{o(r^2)}` possibilities;
* the quotient data have `2^{o(r^2)}` possibilities;
* the dense low-rank defects `D` have `2^{o(r^2)}` possibilities;
* the two ordinary Gram skeletons have `2^{o(r^2)}` possibilities.

The new factorization theorem adds:

\[
\boxed{
\text{for each fixed }D,
\text{ the core singular spectrum has at most }4^{\operatorname{rank}D}=2^{o(r)}\text{ possibilities.}
}
\tag{6.1}
\]

So the surviving quadratic entropy is **not** in:

1. the partition;
2. the quotient;
3. the defect;
4. the Gram eigenvalues.

It is localized to the **orientation of the exact `sqrt(s)` plateau** and, when `D^TD` has repeated positive eigenvalues, to at most `O(k^2)` exceptional eigenspace orientation.

The complete real normal form makes the next theorem precise:

> **Kernel-orientation theorem needed.** For the sign-reconstructible defects arising from the `|r-lambda|=4` shell, count ternary realizations of the scaled orthogonal map
> \[
> T/\sqrt{s}:\ker D\to\ker D^T
> \]
> once the `k=o(r)` exceptional sector is fixed. Either show `2^{o(r^2)}` realizations, or force a contracting Hadamard / weighing / group-divisible-design recursion.

This is strictly narrower than the previous fixed two-sided Gram-fiber formulation.

A useful simple-spectrum subcase is immediate. If all nonzero eigenvalues of `D^TD` are simple, then `A` commutes with `D^TD` and on each one-dimensional eigenspace has only the two roots of (5.1). Consequently

\[
\boxed{
D^TD\text{ simple off }0
\Longrightarrow
\#\{T^TT\text{ compatible with fixed }D\}\le 2^k.
}
\tag{6.2}
\]

Thus all continuous fixed-defect Gram freedom comes from repeated nonzero defect singular values; the high-dimensional flat sector affects root orientation but not the Gram matrix.

---

## 7. Relation to current literature

A bounded fresh search on 20 September 2026 did not surface a resolution of Vu's exact Conjecture 9.4. This is negative search evidence only, not an openness or novelty certificate.

The asymptotic Hadamard-enumeration boundary remains Ferber--Jain--Zhao, *On the number of Hadamard matrices via anti-concentration* (Combinatorics, Probability and Computing 31 (2022), 455--477), which gives a constant quadratic improvement but not a `2^{o(n^2)}` bound. A recent finite result, Tuomo Valtonen, *Classification of Symmetric Hadamard Matrices Up to Order 32*, arXiv:2608.06920 (7 August 2026), is a finite classification and does not settle the asymptotic counting problem.

The current shell is also adjacent to weighing-matrix and symmetric group-divisible-design theory, where equations of the form `WW^T=wI` and block Gram matrices are classical. No claim is made here that those theories are new; the new project step is the exact defect-to-integral-spectral-factorization reduction inside the inherited F0011 core.

---

## 8. Cross-worker reusable lemma

The basis-free part does not depend on ternary entries:

> If real invertible `T,S` satisfy `TS=ST=sI` with `s>0` and `D=T-S^T`, then for `A=T^TT`,
> \[
> D^TD=A-2sI+s^2A^{-1},
> \qquad
> A D^TD=(A-sI)^2,
> \]
> and `rank(A-sI)=rank D`.

This is useful whenever a covariance or SDP operator is close, in low rank, to its scaled inverse transpose. The integral polynomial factorization requires integer `T,S,D` and should not be imported into Gaussian settings without an integer-lattice analogue.

---

## 9. Frozen metric and status

Frozen full-source finite metric:

\[
\boxed{N_{\rm exact}:9\to9.}
\]

No small-order census was run.

Status remains **PROVED PARTIAL**. The new theorem does not prove Vu Conjecture 9.4, does not prove a subquadratic count for all centered symmetric Hadamards, and does not bridge from the centered two-eigenvalue slice to arbitrary integral spectra. It removes a specific ambiguity in the current low-rank core: fixed-defect spectral freedom is now completely described by an integral degree-`k` factorization and cannot itself carry quadratic entropy.
