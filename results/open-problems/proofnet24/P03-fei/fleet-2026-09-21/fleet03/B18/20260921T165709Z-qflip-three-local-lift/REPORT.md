# B18 FEI proof integration: arbitrary q-flip three-local sensitivity lift

**Date:** 21 September 2026  
**Scope:** `fleet03 / B18`, full-FEI proof integration  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact universal local theorem and a source-exact interface repair; no novelty or publication-priority claim.

## 0. Why this is the next missing implication

This run read the owner-mandated `TASKS_2026-09-21.md`, then `REPORT.md`, then `APPROACHES.md` before substantive work. It then integrated two newest compatible fleet03 results rather than auditing either of them:

1. B12 proved that for **physical coordinate triples** the projected spectral-sample law and the physical sensitivity-set law have identical one- and two-coordinate marginals, differ by one cubic scalar, and obey the sharp local transport bound
   \[
   W_1^{\mathrm{Ham}}\le \frac23 I_B.
   \]
2. B16 reduced the all-order selector-refinement defect to a double-resolvent integral of **third finite differences along actual q-flip generators**, but explicitly left open the geometry bridge because a q-flip generator need not be a single physical coordinate.

The exact statement attempted here is therefore:

> **QFLIP-THREE-LOCAL LIFT.** Does B12's sharp three-local spectral/sensitivity coupling remain valid for an arbitrary triple of translations \(u,v,w\in\mathbb F_2^n\), including linearly dependent triples, when spectral “membership” is replaced by spectral parity under those flips?

The answer is **yes**, with the same sharp constant \(2/3\). This removes the coordinate-basis obstruction in B16 §8. It does **not** by itself pay B16's compiler-game curl; the remaining map is now operator-specific rather than geometric.

---

## 1. Setup

Let
\[
f:\mathbb F_2^n\to\{-1,+1\},
\qquad
\widehat f(\xi)=2^{-n}\sum_x f(x)(-1)^{\langle \xi,x\rangle}.
\]
Let \(\Xi\) be the spectral sample in frequency-vector form,
\[
\Pr(\Xi=\xi)=\widehat f(\xi)^2,
\]
and let \(X\) be uniform on \(\mathbb F_2^n\).

For an arbitrary translation \(u\in\mathbb F_2^n\), define the spectral parity bit
\[
A_u:=\langle \Xi,u\rangle\pmod2
\]
and the physical q-flip sensitivity bit
\[
B_u:=\mathbf 1\{f(X)\ne f(X+u)\}.
\]
Write
\[
c_u:=\mathbb E[f(X)f(X+u)],
\qquad
I_u:=\Pr(B_u=1)=\frac{1-c_u}{2}.
\]

For a triple \(u,v,w\), define
\[
\tau_{u,v,w}:=
\mathbb E[f(X)f(X+u)f(X+v)f(X+w)].
\]

---

## 2. PROVED: exact one- and two-q-flip law equality for arbitrary translations

Introduce the sign encodings
\[
\alpha_u:=(-1)^{A_u},
\qquad
\beta_u:=(-1)^{B_u}=f(X)f(X+u).
\]

Fourier expansion gives
\[
\mathbb E\alpha_u
=
\sum_\xi \widehat f(\xi)^2(-1)^{\langle \xi,u\rangle}
=
c_u.
\]
Also, for arbitrary \(u,v\),
\[
\mathbb E[\alpha_u\alpha_v]
=
c_{u+v}.
\]
On the physical side,
\[
\mathbb E\beta_u=c_u
\]
and translation invariance gives
\[
\mathbb E[\beta_u\beta_v]
=
\mathbb E[f(X+u)f(X+v)]
=
c_{u+v}.
\]

Thus the two sign vectors have the same constant, first, and second Walsh moments. Therefore
\[
\boxed{
\operatorname{Law}(A_u,A_v)
=
\operatorname{Law}(B_u,B_v)
}
\tag{2.1}
\]
for every pair of translations, with no independence or basis assumption.

This is the q-flip form of B12's two-local identity.

---

## 3. PROVED: every triple discrepancy is one cubic scalar

For a triple \(u,v,w\),
\[
\mathbb E[\alpha_u\alpha_v\alpha_w]
=
c_{u+v+w},
\]
while
\[
\mathbb E[\beta_u\beta_v\beta_w]
=
\tau_{u,v,w}.
\]

All Walsh coefficients of the two 3-bit laws of order \(0,1,2\) are therefore identical; only the order-three coefficient can differ. If
\[
q:=\Pr(A_u=A_v=A_w=1),
\qquad
s:=\Pr(B_u=B_v=B_w=1),
\]
then direct three-bit inversion gives
\[
\boxed{
d_{u,v,w}:=q-s
=
\frac{\tau_{u,v,w}-c_{u+v+w}}{8}.
}
\tag{3.1}
\]

For every pattern \(a=(a_1,a_2,a_3)\in\{0,1\}^3\),
\[
\boxed{
\Pr(A=a)-\Pr(B=a)
=
(-1)^{3-|a|}d_{u,v,w}.
}
\tag{3.2}
\]

Hence the four surplus vertices and four deficit vertices are opposite parity classes of the 3-cube. Matching the two parity classes along any perfect matching of cube edges transports exactly \(|d|\) across four unit edges. Since total variation is a lower bound for Hamming \(W_1\),
\[
\boxed{
W_1^{\rm Ham}(\operatorname{Law}A,\operatorname{Law}B)
=
\|\operatorname{Law}A-\operatorname{Law}B\|_{\rm TV}
=
4|d_{u,v,w}|
=
\frac12|\tau_{u,v,w}-c_{u+v+w}|.
}
\tag{3.3}
\]

This identity is valid even when \(u,v,w\) are linearly dependent.

---

## 4. PROVED: the sharp \(2/3\) local transport bound survives arbitrary q-flips

### Theorem 4.1

For every Boolean \(f:\mathbb F_2^n\to\{\pm1\}\) and every \(u,v,w\in\mathbb F_2^n\),
\[
\boxed{
|d_{u,v,w}|
\le
\frac{I_u+I_v+I_w}{6}.
}
\tag{4.1}
\]
Equivalently,
\[
\boxed{
W_1^{\rm Ham}(\operatorname{Law}(A_u,A_v,A_w),
              \operatorname{Law}(B_u,B_v,B_w))
\le
\frac23(I_u+I_v+I_w).
}
\tag{4.2}
\]
Equivalently again,
\[
\boxed{
|\tau_{u,v,w}-c_{u+v+w}|
\le
\frac43(I_u+I_v+I_w).
}
\tag{4.3}
\]

The constant \(1/6\) in (4.1), hence \(2/3\) in (4.2), is sharp.

### Proof

Let
\[
H=\operatorname{span}_{\mathbb F_2}\{u,v,w\}
\]
and \(r=\dim H\le3\). Partition the ambient cube into cosets of \(H\).

#### Rank \(r=3\)

On each coset \(y+H\), use \(u,v,w\) as the coordinate basis and define
\[
g_y(a,b,c)=f(y+au+bv+cw).
\]
B12's exact three-cube lemma applies to each \(g_y\):
\[
|q_3(g_y)-s_3(g_y)|
\le
\frac16 I(g_y).
\tag{4.4}
\]

Averaging over cosets preserves all three quantities exactly:

* the averaged local top Fourier weight is
  \[
  \mathbb E_y q_3(g_y)
  =
  \sum_{\xi:\langle\xi,u\rangle=\langle\xi,v\rangle=\langle\xi,w\rangle=1}
  \widehat f(\xi)^2
  =q;
  \]
  this is Parseval on the quotient/coset decomposition;
* the averaged local all-three-sensitive probability is \(s\);
* the averaged local total influence is \(I_u+I_v+I_w\).

Thus Jensen's inequality for absolute value and (4.4) give
\[
|q-s|
\le
\mathbb E_y|q_3(g_y)-s_3(g_y)|
\le
\frac16(I_u+I_v+I_w).
\]

#### Rank \(r=2\)

If one direction is zero or two directions coincide, the 3-bit vector is determined by at most two bits on both the spectral and physical sides. By (2.1) the complete 3-bit laws are then identical, so \(d=0\).

The only nontrivial rank-two case has \(u,v,w\) equal to the three distinct nonzero elements of a two-dimensional subspace, hence
\[
u+v+w=0.
\]
For every coset of that 2-space, the spectral parity vector obeys
\[
A_u\oplus A_v\oplus A_w=0,
\]
so \(q=0\) locally. A Boolean truth table on that 2-cube has an all-three-sensitive vertex iff one vertex has the minority sign, equivalently iff the product of the four vertex signs is \(-1\). In that case there is exactly one all-three-sensitive vertex, so
\[
s=\frac14,
\]
and each of the three nonzero translation directions has influence \(1/2\), giving
\[
I_u+I_v+I_w=\frac32.
\]
Therefore
\[
|d|=\frac14=\frac16\cdot\frac32.
\]
If the four-sign product is \(+1\), then \(s=0=d\). Averaging over cosets proves (4.1).

#### Rank \(r\le1\)

At least two direction bits are repetitions or zeros. The full 3-bit vectors are determined by their at-most-two distinct nonzero components, whose laws agree by (2.1). Hence \(d=0\).

This proves the theorem. Sharpness already occurs in the rank-two minority-vertex example above. \(\square\)

---

## 5. A useful dual form for the B16 transport interface

By Kantorovich--Rubinstein duality on the three-bit Hamming cube, every \(L\)-Lipschitz observable
\[
\phi:\{0,1\}^3\to\mathbb R
\]
satisfies
\[
\boxed{
\left|
\mathbb E\phi(A_u,A_v,A_w)
-
\mathbb E\phi(B_u,B_v,B_w)
\right|
\le
\frac{2L}{3}(I_u+I_v+I_w).
}
\tag{5.1}
\]

This is the form directly useful for q-flip/Radon transport: once a signed third-curvature term is represented as a bounded-Lipschitz functional of the three q-flip activation bits, its physical payment is dimension-free and source-exact.

For the parity observable \(\phi(a)=(-1)^{a_1+a_2+a_3}\), whose Hamming Lipschitz constant is \(2\), (5.1) is exactly (4.3).

---

## 6. What this closes, and what it does not

B16 §8 correctly warned that the B12 theorem could not simply be inserted because a q-flip generator is generally not a physical coordinate. Theorem 4.1 removes precisely that obstruction:

> **Any three actual \(\mathbb F_2^n\) flip directions, not only coordinate directions, obey the same sharp B12 local spectral/sensitivity transport theorem. Linear dependence does not break the theorem.**

Thus the q-flip-to-physical geometry issue at the level of three-generator local laws is **PROVED**.

What remains is narrower and operator-specific. B16's
\[
\Xi_{ab}(x,y)
\]
is a signed third finite difference of the retained compiler game \(G=E-R_d\), not itself the cubic law defect of the original Boolean function. A complete FEI step still needs an exact Radon/compiler identity expressing the relevant signed part of \(\Xi_{ab}\) as an average of bounded-Lipschitz observables of the q-flip activation triples (or another quantity covered by the original-coordinate banks), with dual-code multiplicities and terminal refunds preserved.

No such identity is asserted here. Consequently full FEI remains **OPEN**.

---

## 7. Decisive refutation of stronger variants

Two tempting stronger statements die immediately.

### REFUTED: exact triple-law equality for arbitrary q-flips

Take a two-dimensional cube and let \(u,v,w=u+v\) be its three nonzero directions. Let \(f\) have one minority vertex. Then
\[
q=0,\qquad s=\frac14,\qquad |d|=\frac14,
\]
so the two 3-bit laws are not equal. In fact
\[
W_1^{\rm Ham}=1.
\]

### REFUTED: any universal local constant smaller than \(2/3\)

For the same example,
\[
I_u=I_v=I_w=\frac12,
\qquad
I_u+I_v+I_w=\frac32,
\]
and therefore
\[
W_1^{\rm Ham}=1
=
\frac23\left(\frac32\right).
\]
So the constant \(2/3\) is already sharp on a linearly dependent q-flip triple.

This also shows that linear dependence cannot provide a better universal constant for B16's q-flip triples.

---

## 8. Exact falsification computation

`verify_qflip_three_local.py` exhausts every Boolean truth table on the minimal quotient ranks \(0,1,2,3\) and every ordered direction triple spanning that quotient. It checks exact rationally:

* equality of all one- and two-bit marginals;
* \(q-s=(\tau-c_{u+v+w})/8\);
* the alternating eight-cell discrepancy formula;
* `TV = 4|d|`;
* \(|d|\le(I_u+I_v+I_w)/6\).

Total exact cases:
\[
43{,}710.
\]

Breakdown:

| quotient rank | exact cases | equality cases for \(1/6\) | maximum \(|d|/\sum I\) |
|---:|---:|---:|---:|
| 0 | 2 | 0 | 0 |
| 1 | 28 | 0 | 0 |
| 2 | 672 | 48 | \(1/6\) |
| 3 | 43,008 | 2,688 | \(1/6\) |

The computation is falsification evidence; the proof is the rank reduction above, using B12's already-certified 3-cube lemma in rank three.

---

## 9. Classification and next attack

**PROVED**
- arbitrary q-flip one-/two-local spectral parity laws equal physical flip-sensitivity laws exactly;
- every arbitrary q-flip triple differs by one cubic scalar \(d=(\tau-c_{u+v+w})/8\);
- `TV = W1 = 4|d|`;
- sharp universal q-flip bound \(W_1\le(2/3)(I_u+I_v+I_w)\);
- bounded-Lipschitz dual payment (5.1).

**REFUTED**
- exact equality of the triple laws;
- any universal q-flip three-local transport constant below \(2/3\).

**OPEN**
- full unrestricted FEI;
- the exact compiler/Radon identity that maps B16's integrated third-curvature current into observables controlled by (5.1) without losing dual-code multiplicity, signs, terminal-band refunds, or a dimension factor.

**Next attack.** Expand one B16 curl term
\[
\Delta_{b\epsilon}\mathcal P_{a0,a1}
\]
through the established q-flip Radon representation and isolate its dependence on the three activation parities. If the resulting local observable has a uniform Lipschitz constant before summing dual-code multiplicities, apply (5.1) inside the double resolvent and only then perform the signed current/Radon summation. If the Lipschitz constant grows with code multiplicity, this route dies and the next mechanism should use B16's minimum-energy current before Radon inversion rather than after it.

No novelty or publication-priority claim is made.
