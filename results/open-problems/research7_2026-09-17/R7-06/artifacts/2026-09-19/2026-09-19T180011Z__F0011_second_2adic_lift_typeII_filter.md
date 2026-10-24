# F0011 — second 2-adic lift equations and the exact Type-II filter on the maximal Hadamard shadow

Date: 2026-09-19 UTC  
Slot: `R7-06`  
Target: Van H. Vu, *Recent progress in combinatorial random matrix theory*, Conjecture 9.4.  
Methods: **B5 / B17 / B28**.  
Status: **PARTIAL**. Nothing below proves Vu's asymptotic conjecture.

## 1. Starting point recovered from the preceding run

On the two-eigenvalue symmetric-Hadamard core, after diagonal switching and one overall sign, write

\[
\widetilde H=
\begin{pmatrix}
1&\mathbf 1^T\\
\mathbf 1&B
\end{pmatrix},
\qquad
\widetilde H^2=nI.
\]

The integral-spectrum case has `n=4t^2` with an integer `t>=1`. Put

\[
v=n-1=4t^2-1,
\qquad
G=\frac{J+B}{2}\in\{0,1\}^{v\times v}.
\]

The preceding R7-06 run proved the exact design equations

\[
\boxed{
G\mathbf 1=(2t^2-1)\mathbf 1,
\qquad
G^2=t^2I+(t^2-1)J.
}
\tag{1}
\]

Modulo two, the affine first shadow is square-zero. The purpose of this note is to keep the next 2-adic information instead of discarding it.

---

## 2. B5 — exact divided-square lift equations

### Theorem 2.1 — even `t`

Assume `t` is even and define the actual binary matrix

\[
N:=J-G.
\]

Then

\[
\boxed{N\mathbf 1=2t^2\mathbf 1}
\tag{2}
\]

and, over the integers,

\[
\boxed{N^2=t^2(I+J).}
\tag{3}
\]

Consequently, if `a=nu_2(t)>=1`, then

\[
2^{-j}N^2\equiv0\pmod2\quad(0\le j<2a),
\]

whereas the first nonzero divided square is

\[
\boxed{2^{-2a}N^2\equiv I+J\pmod2.}
\tag{4}
\]

In particular

\[
\boxed{N^2/2\equiv0\pmod2,}
\tag{5}
\]

and at the next visible level

\[
\boxed{N^2/4\equiv (t/2\bmod2)(I+J)\pmod2.}
\tag{6}
\]

#### Proof

Equation (2) follows from `J1=v1` and (1):

\[
N\mathbf1=(v-(2t^2-1))\mathbf1=2t^2\mathbf1.
\]

Also `JG=GJ=(2t^2-1)J`, so

\[
\begin{aligned}
N^2
&=(J-G)^2\\
&=J^2-JG-GJ+G^2\\
&=vJ-2(2t^2-1)J+t^2I+(t^2-1)J\\
&=t^2(I+J),
\end{aligned}
\]

because `v=4t^2-1`. This proves (3). Write `t=2^a u` with `u` odd. Dividing (3) by `2^{2a}` gives `u^2(I+J)`, which reduces to `I+J` modulo two. For every smaller power of two the off-diagonal entries remain even. Equation (6) is the special case `a>=1` after one further normalization. ∎

### Corollary 2.2 — exact overlap data in the even branch

Let `R_i` be the support of row `i` of `N`. Then

\[
\boxed{|R_i|=2t^2,\qquad |R_i\cap R_j|=t^2\ (i\ne j).}
\tag{7}
\]

Thus for even `t`, each row has weight divisible by `8`, and each distinct pair intersection is divisible by `4`. More precisely, the 2-adic valuation of every off-diagonal intersection is exactly `2 nu_2(t)`.

This is stronger information than the first shadow `N^2=0` over `F_2`.

---

### Theorem 2.3 — odd `t`

Assume `t` is odd. Let `N` be the binary representative of `G+I (mod 2)`, let

\[
d_i=N_{ii},\qquad D=\operatorname{diag}(d_1,\ldots,d_v),
\qquad E:=I-2D.
\]

Then `G=N+E` exactly, and

\[
\boxed{
N^2+NE+EN=(t^2-1)(I+J).
}
\tag{8}
\]

Equivalently,

\[
\boxed{
\frac{N^2}{2}+N-(ND+DN)
=\frac{t^2-1}{2}(I+J).
}
\tag{9}
\]

Since every odd square is `1 (mod 8)`, the right side of (9) is even entrywise. Hence the first divided-square/Bockstein condition is

\[
\boxed{
Q_1(N):=\frac{N^2}{2}\equiv N+ND+DN\pmod2.
}
\tag{10}
\]

If `b=nu_2(t^2-1)>=3`, then the residual

\[
R(N):=\frac{N^2}{2}+N-(ND+DN)
\]

satisfies

\[
\boxed{
2^{-(b-1)}R(N)\equiv I+J\pmod2,
}
\tag{11}
\]

with all shallower divided residuals zero modulo two.

#### Proof

Off the diagonal `N=G`; on the diagonal `N_{ii}=1-G_{ii}`, so `G=N+I-2D=N+E`. Since `E^2=I`, substituting in (1) gives

\[
N^2+NE+EN+I=t^2I+(t^2-1)J,
\]

which is (8). Since `E=I-2D`,

\[
NE+EN=2N-2(ND+DN),
\]

and division by two gives (9). Because `t^2-1` is divisible by `8`, `N^2` is even entrywise and reduction of (9) modulo two yields (10). Writing `(t^2-1)/2=2^{b-1}u` with `u` odd gives (11). ∎

### Corollary 2.4 — local parity law in the odd branch

For every row support `R_i`,

\[
\boxed{
|R_i|=2(t^2-1+d_i).
}
\tag{12}
\]

For `i\ne j`,

\[
\boxed{
|R_i\cap R_j|
=t^2-1-2N_{ij}(1-d_i-d_j).
}
\tag{13}
\]

Therefore

\[
\boxed{
\frac{|R_i|}{2}\equiv d_i\pmod2,
\qquad
\frac{|R_i\cap R_j|}{2}
\equiv N_{ij}(1+d_i+d_j)\pmod2.
}
\tag{14}
\]

The odd branch therefore carries a nontrivial diagonal-colored half-intersection law which is invisible in `N^2=0 (mod 2)`.

---

## 3. B17 — code geometry forced on a maximal-rank even shadow

Return to even `t`. Put

\[
m=\frac{v-1}{2}=2t^2-1,
\qquad
W=\mathbf1^\perp\le \mathbb F_2^v.
\]

The previous run showed that `W` is a nondegenerate symplectic space of dimension `2m` and that every square-zero shadow has isotropic image. Suppose now that the exact binary matrix `N` from Theorem 2.1 has maximal possible binary rank

\[
\operatorname{rank}_{\mathbb F_2}N=m.
\tag{15}
\]

Let

\[
U:=\operatorname{im}_{\mathbb F_2}N.
\]

### Theorem 3.1 — Type-II extension

Under (15):

1. `U` is a Lagrangian subspace of `W`.
2. Every word of `U` has Hamming weight divisible by `4`.
3. The length-`n=v+1` code

\[
\boxed{
C_U:=\{(u,0):u\in U\}
+\langle(\mathbf1,1)\rangle
}
\tag{16}
\]

is a binary **Type-II (doubly-even) self-dual code**.
4. The `v` columns of any row-basis generator of `U` are nonzero and pairwise distinct; equivalently, `U` is projective.

#### Proof

Since `N^2=0` modulo two and `N\mathbf1=0` modulo two, `U\subset W` and `U` is totally isotropic. Its dimension is `m=dim(W)/2`, so it is Lagrangian.

On `W`, define

\[
q(x)=\frac{\operatorname{wt}(x)}2\pmod2.
\]

For even-weight `x,y`,

\[
q(x+y)=q(x)+q(y)+x\cdot y,
\]

so `q` is a quadratic refinement of the symplectic dot product. By (7), every generating row `r_i` of `N` has

\[
q(r_i)=t^2\equiv0\pmod2
\]

and every pair of generating rows has zero dot product modulo two. Hence `q` vanishes on their span `U`; all words of `U` have weight divisible by four.

The code (16) has dimension `m+1=n/2`. The first summand is self-orthogonal, every `u\in U` has `u\cdot\mathbf1=0`, and

\[
(\mathbf1,1)\cdot(\mathbf1,1)=v+1=n\equiv0\pmod2.
\]

Thus `C_U` is self-orthogonal of half dimension and hence self-dual. Words `(u,0)` have weight divisible by four; words `(u+\mathbf1,1)` have weight `n-wt(u)`, also divisible by four because even `t` makes `n=4t^2` divisible by `16`. Therefore `C_U` is Type II.

Finally, a column of `N` cannot vanish because every column sum is `2t^2>0`. Two distinct columns cannot be equal: if columns `i,j` were equal, their integer inner product would equal their common weight `2t^2`, but (3) says the off-diagonal inner product is only `t^2`. Passing to any basis of the row space preserves zero/repeated-column equivalence, proving projectivity. ∎

### Prior-art boundary

The broad Hadamard/design/code connection is classical. Relevant references include:

- M. Munemasa and H. Tamura, *The codes and the lattices of Hadamard matrices*, European J. Combin. 33 (2012), 519–533, DOI `10.1016/j.ejc.2011.11.007`.
- S. T. Dougherty, *The neighbor graph of binary self-dual codes*, Designs, Codes and Cryptography 90 (2022), 409–425, DOI `10.1007/s10623-021-00985-2`.

I do **not** claim the existence of Type-II codes or the standard mass formulas as new. The useful point for F0011 is the exact placement of the maximal-rank first shadow inside this classical code geometry.

---

## 4. B28 — a typical maximal first shadow fails the Type-II filter, but only by a linear exponent

The preceding theorem gives a necessary condition for a maximal-rank even-`t` shadow to lift to an exact symmetric-Hadamard design. This condition can be counted exactly.

### Theorem 4.1 — exact survival fraction of the image-space filter

Let `U` be chosen uniformly from the Lagrangian subspaces of `W`. The number of choices is

\[
L_m=\prod_{i=1}^{m}(2^i+1).
\tag{17}
\]

The number for which the extension `C_U` in (16) is Type II is

\[
T_m=2\prod_{i=1}^{m-1}(2^i+1).
\tag{18}
\]

Therefore

\[
\boxed{
\Pr(C_U\text{ is Type II})
=\frac{2}{2^m+1}
=2^{-m+1+o(1)}.
}
\tag{19}
\]

Equivalently, the necessary Type-II condition removes exactly

\[
\boxed{
\log_2\frac{L_m}{T_m}
=\log_2\frac{2^m+1}{2}
=m-1+o(1)
}
\tag{20}
\]

bits of entropy — **linear**, not quadratic, in the matrix dimension.

#### Proof

The Lagrangian count (17) is standard for a `2m`-dimensional symplectic binary space and was rederived in the preceding R7-06 run. The map

\[
U\longmapsto C_U
\]

is a bijection between Lagrangians `U\le W` and binary self-dual codes of length `n=2(m+1)`: every binary self-dual code is even and hence contains the all-one vector, and shortening in the last coordinate recovers `U`. Under this bijection, `q|_U=0` is precisely the Type-II condition.

For `8|n`, the standard binary Type-II mass formula gives exactly

\[
2\prod_{i=1}^{n/2-2}(2^i+1)
=2\prod_{i=1}^{m-1}(2^i+1)
\]

labeled Type-II self-dual subspaces. Dougherty (2022), cited above, states the same count as the number of vertices of the Type-II neighbor graph. Dividing by (17) gives (19), and taking base-two logarithms gives (20). ∎

### Corollary 4.2 — the same fraction for maximal `(U,S)` square-zero shadows

For each Lagrangian image `U`, the maximal-rank square-zero symmetric matrices with image `U` are parametrized by the same number `h_m` of invertible symmetric `m x m` binary matrices `S` through `N=XSX^T`. Therefore the Type-II image filter removes the **same** fraction `2/(2^m+1)` from the entire entropy-maximizing `(U,S)` stratum.

Thus B28 succeeds in one literal sense:

> a uniformly random entropy-maximizing first shadow fails a necessary exact-lift condition with probability `1-2^{-Theta(n)}`.

But it fails at the scale needed for Vu:

> the surviving family still has the same quadratic leading entropy as the ambient maximal-rank square-zero family.

So the Type-II filter alone cannot yield `2^{o(n^2)}`.

---

## 5. A third-order obstruction: maximal exact lifts cannot be triply even

The even-`t` exact design has more divisibility than Type II at the level of its distinguished rows: by (7), row weights are multiples of eight and pair intersections are multiples of four. The next obstruction is genuinely cubic.

### Lemma 5.1 — no nonzero binary self-dual code is triply even

There is no nonzero binary self-dual linear code all of whose codeword weights are divisible by eight.

#### Proof

Assume `C=C^perp` is triply even. Then it is even, so the all-one vector belongs to `C`. For `x,y\in C`, comparing the weights of `x`, `y`, and `x+y` shows that `|supp(x) cap supp(y)|` is divisible by four. For `x,y,z\in C`, inclusion-exclusion for `wt(x+y+z)` then shows that every triple intersection

\[
|\operatorname{supp}(x)\cap\operatorname{supp}(y)\cap\operatorname{supp}(z)|
\]

is even.

Let `x*y` denote coordinatewise multiplication. For every `z\in C`,

\[
(x*y)\cdot z
=|\operatorname{supp}(x)\cap\operatorname{supp}(y)\cap\operatorname{supp}(z)|
\equiv0\pmod2.
\]

Hence `x*y\in C^perp=C`. Thus `C` is a unital subalgebra of the coordinatewise algebra `F_2^n`.

Every unital subalgebra of `F_2^n` is the algebra of functions constant on the blocks of some partition of the `n` coordinates. If the partition has `r` blocks, its block indicators form a basis, so the algebra has dimension `r`. Since every nonzero block indicator lies in the triply-even code, every block has size at least eight. Therefore

\[
n\ge8r.
\]

Self-duality gives `r=dim C=n/2`, hence `n\ge4n`, impossible for `n>0`. ∎

This is compatible with the classical Gleason–Pierce restriction that divisibility by four is the strongest nontrivial uniform divisibility condition for binary self-dual codes. Triply-even codes themselves are classical objects; see K. Betsumiya and A. Munemasa, *On triply even binary codes*, J. London Math. Soc. 86 (2012), 1–16, DOI `10.1112/jlms/jdr054`.

### Corollary 5.2 — a maximal exact lift has a nonzero triple-overlap tensor

Let `t` be even and suppose the exact `N` has maximal binary rank. Choose generating rows `r_1,...,r_m` for `U`. Since every `r_i` has weight divisible by eight and every pair intersection has size divisible by four, the residue

\[
\frac{\operatorname{wt}(\sum_i a_i r_i)}4\pmod2
\]

is governed, modulo two, by the cubic triple-overlap tensor

\[
\tau_{ijk}:=|R_i\cap R_j\cap R_k|\pmod2.
\]

If all `tau_{ijk}` vanished, then every word of `U` would have weight divisible by eight. Because `n` is divisible by sixteen, the extension `C_U` would then also be triply even and self-dual, contradicting Lemma 5.1. Hence

\[
\boxed{\tau\ne0.}
\tag{21}
\]

So a naive attempt to make the next lift condition `triorthogonality` is pointed in the wrong direction: **every maximal exact lift must contain a genuinely nonzero cubic overlap obstruction**.

---

## 6. What this run actually changes

### B5 outcome

The first shadow has now been lifted to exact divided-square identities. For even `t`, the first nonzero divided square occurs exactly at depth `2 nu_2(t)` and equals `I+J` modulo two. For odd `t`, the Bockstein is the explicit diagonal-colored law (10), with a residual whose first nonzero level is controlled by `nu_2(t^2-1)`.

### B17 outcome

On the entropy-maximizing even branch, exact liftability forces the image Lagrangian to extend to a Type-II self-dual code. The standard code mass formula turns that qualitative statement into an exact count. Triply-even-code theory also shows that the next obstruction cannot be obtained by forcing all triple overlaps to vanish.

### B28 outcome

A typical maximal-rank first shadow indeed fails the Type-II necessary condition: the exact survival fraction is `2/(2^m+1)`. But this saves only `Theta(n)` bits, leaving the quadratic entropy exponent unchanged. Thus the hoped-for `2^{-Omega(n^2)}` typical-lift obstruction is **not** obtained at this layer.

The remaining promising object is no longer just the image `U`; it is the interaction between the invertible symmetric parameter `S` in `N=XSX^T` and the higher divided-square/cubic-overlap constraints. Any next recovery should attack that interaction directly rather than count Type-II image spaces again.

## 7. Source and literature status

- Source target: Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 (2020), Probability Surveys 18 (2021), Conjecture 9.4.
- A bounded 2026-09-19 search did not find a later paper claiming Vu's full `2^{-(1/2+o(1))n^2}` asymptotic. This is negative evidence only, not a certification of openness or novelty.
- Caden Young, *Sharp Exponential Asymptotics for Normal Sign Matrices*, arXiv:2607.15294 (2026), remains the closest recent mod-4/rank-duality methodological analogue.
- Dougherty 2022 supplies the exact Type-II code count used in Theorem 4.1.
- Munemasa–Tamura 2012 and the broader design/code literature establish that Hadamard matrices and self-dual/divisible codes have a long classical connection. The present note does not claim that connection as novel.

## 8. Source-level gap

The frozen source metric does not move: `N_exact=8`. These are restricted structural theorems on the two-eigenvalue Hadamard core. Full F0011 still requires a `2^{o(n^2)}` bound for every exact integral spectral fiber, not only the Hadamard branch, and the necessary Type-II filter above loses only a linear number of bits.
