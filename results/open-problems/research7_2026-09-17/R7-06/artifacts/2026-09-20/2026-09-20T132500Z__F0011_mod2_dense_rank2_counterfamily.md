# F0011 — a dense rank-two finite-field counterfamily to the mod-2-only reduction

Date: 2026-09-20 UTC  
Role: C05 / R7-06  
Status: **PROVED PARTIAL / obstruction theorem**, pending later independent review

## 1. Why this theorem is needed

The immediately preceding artifact reduced the `|r-lambda|=4`, `q=o(r)` kernel-orientation problem to one binary matrix `X` and a low-rank defect mask `E`. Modulo `2`, the odd-`s` branch satisfies

\[
X+E=X^{-T},
\qquad
E=X+X^{-T}.
\tag{1.1}
\]

The defect mask inherited from the sign problem has low rank and dense support. It was tempting to hope that these facts alone might make the finite-field orientation family subquadratic.

That intermediate reduction is false. The construction below gives one fixed **zero-diagonal, rank-two, half-dense** defect `E` for which (1.1) has

\[
2^{(1/2+o(1))d^2}
\]

distinct binary solutions.

Thus the integer signed biorthogonality equations and the forced regular common-support factor from the preceding artifact are essential; mod-2 low rank by itself cannot deliver the desired entropy collapse.

---

## 2. The fixed dense rank-two defect

Let

\[
d=2m
\]

with `m` odd. Work over `F_2^d` with the standard symmetric bilinear form

\[
\langle x,y\rangle=x^Ty.
\]

Let

\[
u=(\mathbf1_m,0),
\qquad
v=(0,\mathbf1_m).
\tag{2.1}
\]

Because `m` is odd,

\[
\langle u,u\rangle=\langle v,v\rangle=1,
\qquad
\langle u,v\rangle=0.
\tag{2.2}
\]

Define

\[
\boxed{E=uv^T+vu^T.}
\tag{2.3}
\]

In block form,

\[
\boxed{
E=
\begin{pmatrix}
0&J_m\\
J_m&0
\end{pmatrix}.
}
\tag{2.4}
\]

Therefore:

* `rank_{F_2} E = 2`;
* `E_ii=0` for every `i`;
* `|supp E|=2m^2=d^2/2`.

So this defect has exactly the qualitative features that a mod-2-only attack would try to exploit: tiny rank, zero diagonal, and macroscopic density.

---

## 3. A seed solution

Put

\[
X_0=I+uv^T.
\tag{3.1}
\]

Since `v^Tu=0`,

\[
(uv^T)^2=0,
\]

and hence

\[
X_0^{-1}=I+uv^T=X_0.
\tag{3.2}
\]

Therefore

\[
X_0^{-T}=I+vu^T,
\]

so

\[
\boxed{X_0+X_0^{-T}=uv^T+vu^T=E.}
\tag{3.3}
\]

Equivalently,

\[
X_0(X_0+E)^T=I.
\]

---

## 4. A symplectic family of solutions with the same fixed defect

The plane

\[
L=\operatorname{span}\{u,v\}
\]

is nondegenerate by (2.2). Let

\[
W=L^\perp.
\]

Then

\[
\dim W=d-2.
\]

Moreover `u+v=\mathbf1_d`, so every `w in W` satisfies

\[
\langle w,\mathbf1_d\rangle=0.
\]

Over `F_2`, this means

\[
\langle w,w\rangle=0.
\]

Hence the restriction of the standard form to `W` is alternating. Because `L` is nondegenerate, `W` is also nondegenerate. Thus `W` is a symplectic space of dimension

\[
d-2=2a,
\qquad a=m-1.
\]

For any

\[
R\in\operatorname{Sp}(W),
\]

extend `R` by the identity on `L`; call the resulting orthogonal transformation `Q_R`. Then

\[
Q_Ru=u,
\qquad
Q_Rv=v,
\qquad
Q_R^TQ_R=I.
\tag{4.1}
\]

Set

\[
\boxed{X_R=Q_RX_0.}
\tag{4.2}
\]

Because `Q_R` is orthogonal,

\[
X_R^{-T}=Q_RX_0^{-T}.
\]

Therefore, using that `Q_R` fixes both `u` and `v`,

\[
X_R+X_R^{-T}
=Q_R(X_0+X_0^{-T})
=Q_RE
=E.
\tag{4.3}
\]

Thus every `R in Sp(W)` produces a solution of the **same fixed-defect equation**

\[
\boxed{X_R+X_R^{-T}=E.}
\tag{4.4}
\]

The map `R -> X_R` is injective because `X_0` is invertible.

---

## 5. Quadratic entropy of the counterfamily

For a symplectic space of dimension `2a` over `F_2`,

\[
|\operatorname{Sp}(2a,2)|
=2^{a^2}\prod_{i=1}^a(2^{2i}-1).
\tag{5.1}
\]

Hence

\[
\log_2|\operatorname{Sp}(2a,2)|
=a^2+\sum_{i=1}^a\log_2(2^{2i}-1)
=2a^2+a+O(1).
\tag{5.2}
\]

Since `a=(d-2)/2`,

\[
\boxed{
\log_2|\operatorname{Sp}(W)|
=\frac12d^2-O(d).
}
\tag{5.3}
\]

Therefore the fixed defect (2.4) has at least

\[
\boxed{
2^{d^2/2-O(d)}
}
\tag{5.4}
\]

distinct binary solutions of

\[
X+X^{-T}=E.
\]

This is Hadamard-scale quadratic entropy despite `rank(E)=2`, `diag(E)=0`, and `|supp E|=d^2/2`.

---

## 6. Consequence for the F0011 attack

This is an explicit counterexample to the proposed intermediate statement

> low-rank + dense + zero-diagonal `E`, together with the mod-2 inverse-transpose relation, should force `2^{o(d^2)}` orientations.

It does not satisfy all of the **integer** constraints inherited from the sign-Gram shell, and therefore is not a counterexample to the shell theorem or to Vu's conjecture. Instead it proves that those missing integer constraints are indispensable.

The preceding artifact supplies exactly the extra structure absent here:

1. fixed anchor sign masks `U,V` over the integers;
2. the signed integer equation
   \[
   (V\odot X)(U\odot(X\oplus E))^T=sI;
   \]
3. the common support
   \[
   A=X\odot(1-E)
   \]
   is an **exact `s`-regular bipartite graph**, hence contains `s` edge-disjoint perfect matchings.

The next attack must use at least one of those integer/common-support features. Spending another run on a pure finite-field rank classification would not address the demonstrated symplectic obstruction.

A natural next target is an **integer rigidity theorem over the symplectic plateau**: show that imposing the signed off-diagonal equations plus an `s`-factor in `1-E` collapses the large `Sp(W)` freedom to `2^{o(d^2)}`, or else forces a genuine smaller weighing/Hadamard/group-divisible-design recursion.

The singular/corank endpoint of the original sign problem remains included in the preceding reduction; this finite-field obstruction neither removes nor resolves it.
