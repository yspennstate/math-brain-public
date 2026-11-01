# F0012 recovery 3 — rank-core projection removes the integer-state log loss

Target: Vu Conjecture 9.5 recovery after the source-level refutation.  
Restricted recovery object: sign matrices with controlled `rank(A)` and `rank(A^2)`, with special attention to `A^3=0`.  
Methods: **B11 dualize / B28 replace for-all by a localized typical-profile regime / B24 find the extremal object**.

The original source conjecture is already refuted by the earlier R7-07 block-shear family. The fixed source metric remains `0 <= u_GI <= 1/2`. This note attacks the post-STUCK1 recovery target: prove the candidate half exponent inside progressively larger nilpotent fibers.

The preceding run bounded cube-zero matrices by first exposing an integer middle matrix `G=RC`. That introduced an artificial `(n+1)^{2rs-s^2}` cost and only handled `rank(A^2)=o(n/log n)`. The new idea is to **dualize the numerical middle state into its rank core and a projection**, so the remaining columns are counted directly as sign vectors in affine kernels. This removes the entire `log n` loss.

## 1. Setup

For `0 <= s <= r <= n`, define

\[
\mathcal R_n(r,s)
=
\{A\in\{\pm1\}^{n\times n}:\operatorname{rank}A=r,\ \operatorname{rank}A^2=s\}.
\]

For an actual member, Sylvester's rank inequality gives

\[
s=\operatorname{rank}(A^2)\ge 2r-n,
\]

so

\[
t:=n-2r+s\ge0.
\tag{1}
\]

Choose index sets `I,J subset [n]`, each of size `r`, such that

\[
B=A_{I,J}
\]

is nonsingular, and put

\[
R=A_{I,*}\in\{\pm1\}^{r\times n},
\qquad
C=A_{*,J}\in\{\pm1\}^{n\times r}.
\]

Then

\[
A=C B^{-1}R,
\tag{2}
\]

and with

\[
G:=RC
\tag{3}
\]

we have

\[
A^2=C B^{-1}G B^{-1}R.
\]

Because `C` has full column rank and `B^{-1}R` has full row rank,

\[
\operatorname{rank}G=\operatorname{rank}A^2=s.
\tag{4}
\]

The preceding run enumerated the entries of `G`. The present run never does that.

## 2. B11 — rank-core projection theorem

### Theorem 2.1 (binary rank-core bound)

For every `n,r,s`,

\[
\boxed{
|\mathcal R_n(r,s)|
\le
\binom nr^2\binom rs^2
2^{\,2nr-2r^2+2rs-s^2}.
}
\tag{5}
\]

This theorem does **not** assume `A^3=0`; it applies to every sign matrix with the indicated two ranks.

### Proof

Fix `A in mathcal R_n(r,s)` and one choice of `I,J` as above. Since `rank G=s`, choose `P,Q subset [r]`, each of size `s`, such that the rank core

\[
H:=G_{P,Q}=R_P C_Q
\tag{6}
\]

is nonsingular. There are at most `binom(r,s)^2` choices.

Expose all of `R`. This costs at most `2^{rn}` choices. Then `B=R_{*,J}` is already fixed.

Next expose the `s` columns `C_Q`. Their coordinates on `I` are prescribed by

\[
C_{I,*}=B,
\tag{7}
\]

so these `s` columns cost at most

\[
2^{s(n-r)}
\tag{8}
\]

choices.

Now define the exact rank-core projection

\[
\Pi
:=
I_n-C_QH^{-1}R_P.
\tag{9}
\]

Because `H=R_PC_Q`,

\[
R_P\Pi=0,
\qquad
\Pi C_Q=0,
\qquad
\Pi^2=\Pi.
\tag{10}
\]

Let `\bar P=[r]\setminus P` and `\bar Q=[r]\setminus Q`.
The Schur-complement identity for the rank-`s` matrix `G` is

\[
G_{\bar P,\bar Q}
=
G_{\bar P,Q}H^{-1}G_{P,\bar Q}.
\]
Using `G=RC`, this is exactly

\[
\boxed{R_{\bar P}\Pi C_{\bar Q}=0.}
\tag{11}
\]

The row matrix `R_{\bar P}\Pi` has rank exactly `r-s`. Indeed, the right-kernel of the map

\[
x\mapsto x\Pi
\]

on row vectors is the row space of `R_P`: if `x\Pi=0`, then

\[
x=xC_QH^{-1}R_P,
\]

so `x in row(R_P)`, while `R_P\Pi=0` gives the converse. Since the `r` rows of `R` are independent, the `r-s` rows indexed by `\bar P` remain independent modulo `row(R_P)`, and hence

\[
\operatorname{rank}(R_{\bar P}\Pi)=r-s.
\tag{12}
\]

We now count one remaining column `c_j` of `C`, `j in \bar Q`.
It must satisfy

\[
(c_j)_I=B_{*,j}
\tag{13}
\]

and

\[
R_{\bar P}\Pi c_j=0.
\tag{14}
\]

The `r-s` equations in (14) remain independent after the coordinates in `I` are fixed. To see this, suppose a nonzero row vector `y` in `row(R_{\bar P}\Pi)` were supported entirely on `I`. Equation (10) gives `yC_Q=0`, while every admissible remaining column satisfies (14), so `yC_{\bar Q}=0`. Therefore

\[
yC=0.
\]
But `y` is supported on `I`, and `C_{I,*}=B` is invertible, so

\[
0=yC=y_I B
\]

forces `y=0`, contradiction. Thus the restriction of `R_{\bar P}\Pi` to the free coordinates `[n]\setminus I` has full row rank `r-s`.

There are `n-r` free coordinates in `c_j`, and `r-s` independent linear equations, so the real affine solution space has dimension exactly

\[
(n-r)-(r-s)=n-2r+s=t.
\tag{15}
\]

An affine `d`-plane meets the sign hypercube in at most `2^d` points. Hence every remaining column has at most

\[
2^t
\tag{16}
\]

choices, and all `r-s` remaining columns together have at most

\[
2^{(r-s)t}
\tag{17}
\]

choices.

Multiplying the choices of `(I,J)`, `(P,Q)`, `R`, `C_Q`, and `C_{\bar Q}` gives

\[
|\mathcal R_n(r,s)|
\le
\binom nr^2\binom rs^2
2^{rn+s(n-r)+(r-s)(n-2r+s)}.
\]
The exponent simplifies to

\[
r n+s(n-r)+(r-s)(n-2r+s)
=2nr-2r^2+2rs-s^2,
\]
which is (5). QED.

### What changed from the preceding run

The preceding estimate paid

\[
(2rs-s^2)\log_2(n+1)
\]

bits for a bounded-integer `G`. The rank-core projection (9) replaces that entire numerical-state enumeration by direct affine-cube counting. There is **no `log n` factor at all** in (5).

This is the main mathematical advance of the run.

## 3. B28 — the cube-zero obstruction shrinks from `o(n/log n)` to `o(n)`

Now assume `A^3=0`. Put

\[
r=\operatorname{rank}A,
\qquad
s=\operatorname{rank}A^2.
\]

The kernel increments are

\[
b_1=n-r,
\qquad
b_2=r-s,
\qquad
b_3=s,
\]

and nilpotency gives

\[
b_1\ge b_2\ge b_3.
\tag{18}
\]

In particular

\[
s\le r/2,
\qquad
r\le(n+s)/2.
\]

The parameter `t` from (1) is exactly

\[
t=n-2r+s=b_1-b_2\ge0.
\tag{19}
\]

The binary exponent in (5) has the exact profile form

\[
\boxed{
2nr-2r^2+2rs-s^2
=
\frac{n^2}{2}+ns-\frac{s^2}{2}-\frac{t^2}{2}.
}
\tag{20}
\]

The binomial prefactor contributes only `O(n)` bits. Therefore:

### Corollary 3.1 (all sublinear second-rank cube-zero matrices)

For every integer sequence `s_n=o(n)`,

\[
\boxed{
\#\{A\in\{\pm1\}^{n\times n}:A^3=0,\ \operatorname{rank}(A^2)\le s_n\}
\le
2^{n^2/2+o(n^2)}.
}
\tag{21}
\]

This strictly improves the preceding threshold `s_n log n=o(n)` to the optimal sublinear scale `s_n=o(n)` for this method.

### Proof

For every `s<=s_n`, (20) gives

\[
2nr-2r^2+2rs-s^2
\le
\frac{n^2}{2}+ns
\le
\frac{n^2}{2}+ns_n.
\]
The binomial factors cost `O(n)` bits and there are at most `n^2` rank pairs. Since `ns_n=o(n^2)`, summing (5) over the cube-zero feasible profiles proves (21). QED.

### Corollary 3.2 (a complete profile wedge)

For one fixed cube-zero profile `(r,s)`, let `t=n-2r+s`. Then

\[
\log_2|\mathcal N_3(n;r,s)|
\le
\frac{n^2}{2}
+
\left(ns-\frac{s^2}{2}-\frac{t^2}{2}\right)
+O(n).
\tag{22}
\]

Hence every profile satisfying

\[
\boxed{t^2\ge 2ns-s^2+o(n^2)}
\tag{23}
\]

already has the candidate half exponent.

In normalized variables

\[
\beta=s/n,
\qquad
\tau=t/n,
\]

a sequence can exceed the half exponent by a fixed positive amount only inside the explicit macroscopic wedge

\[
\boxed{
\beta>0,
\qquad
\tau^2<2\beta-\beta^2.
}
\tag{24}
\]

Thus a hypothetical cube-zero counterfamily to the candidate `1/2` exponent must have **linear second rank and comparatively balanced first two kernel increments**. The previous run only knew that `s` had to be at least order `n/log n`; now every `s=o(n)` is eliminated.

**B28 outcome:** successful localization. The full for-all statement is still open, but the exceptional profile set has been reduced to a concrete linear-rank balanced wedge.

## 4. B24 — sharp extremal gap for affine cube fibers

The remaining-column estimate (16) uses the universal bound `2^t`. We now classify exactly when this maximum can be approached.

### Lemma 4.1 (one affine form has a `3/4` gap)

Let

\[
\phi(x)=b+\sum_{k=1}^d a_kx_k,
\qquad x\in\{\pm1\}^d.
\]

Either

\[
\phi\equiv 1,
\quad
\phi\equiv-1,
\quad
\phi= x_j,
\quad\text{or}\quad
\phi=-x_j
\tag{25}
\]

for some `j`, in which case `|\phi(x)|=1` for every cube point, or else

\[
\boxed{
\#\{x\in\{\pm1\}^d:|\phi(x)|=1\}
\le 3\cdot2^{d-2}.
}
\tag{26}
\]

### Proof

If at least two coefficients, say `a_i,a_j`, are nonzero, condition on all other coordinates. On the remaining two-dimensional square there are four values

\[
c\pm a_i\pm a_j.
\]

All four cannot lie in `{+1,-1}`: if they did, the square of the affine form would equal the constant `1` on all four points, but its `x_ix_j` Fourier coefficient is `2a_i a_j\ne0`. Thus at most three of the four points survive. Averaging over the conditioned coordinates gives (26).

If exactly one `a_j` is nonzero, then the two values are `b+a_j` and `b-a_j`. If both have absolute value one, solving the four possible sign equations shows `b=0` and `a_j=\pm1`; otherwise at most half the cube survives. If all `a_k=0`, either `b=\pm1` or no cube point survives. QED.

### Theorem 4.2 (sharp affine-plane cube gap)

Let `L subset R^N` be an affine subspace of affine dimension `d`. Then exactly one of the following holds:

1. `|L cap {+1,-1}^N|=2^d`; after choosing `d` pivot coordinates, every remaining coordinate on `L` is either a constant `+/-1` or `+/-` one pivot coordinate;
2. 
   \[
   \boxed{|L cap {+1,-1}^N|\le 3\cdot2^{d-2}.}
   \tag{27}
   \]

### Proof

Choose `d` coordinate functionals whose linear parts form a basis of the dual of the direction space of `L`. Projection to those coordinates is an affine isomorphism `L -> R^d`. Any sign point of `L` therefore projects injectively to a point of `{+1,-1}^d`. Every remaining coordinate is an affine form `\phi_j` of the pivot variables.

If one `\phi_j` is not one of the four cube-compatible forms in (25), Lemma 4.1 cuts the possible pivot cube to at most `3/4` of its points, proving (27). If every remaining coordinate is cube-compatible, every one of the `2^d` pivot sign assignments lifts to a sign point of `L`, giving equality. QED.

### Application to the rank-core fibers

For fixed exposed `(R,C_Q,P,Q)`, every remaining column of `C` lies in an affine space of dimension exactly

\[
t=n-2r+s.
\]

All those affine spaces have the same direction space

\[
D
=
\{h\in\mathbf R^n:h_I=0,\ R_{\bar P}\Pi h=0\}.
\tag{28}
\]

If `D` is not of signed-partition/cube type, Theorem 4.2 applies to **every** remaining-column fiber, yielding the improved factor

\[
\left(\frac34\right)^{r-s}
\tag{29}
\]

relative to (5).

If a remaining-column fiber has more than `3/4` of the maximal `2^t` sign points, it must in fact have all `2^t`, and `D` has the exact signed-partition form: after selecting `t` pivot free coordinates, every other free coordinate direction is either zero or `+/-` one pivot direction. Equivalently, the annihilator of `D` is generated by coordinate constraints and signed pair-identification constraints.

This is a sharp structural description of the extremal row-space prefixes.

However, (29) saves only `O(n)` bits because there are only `r-s=O(n)` remaining columns. It therefore does **not** alter the quadratic exponent. In the most dangerous balanced regime `t=0`, the direction space is automatically a zero-dimensional cube subspace, so the B24 stability mechanism cannot close the remaining wedge by itself.

**B24 outcome:** exact extremal classification and a useful no-go. Any further quadratic-scale improvement must reduce the entropy of the exposed `R` and core columns `C_Q`, or exploit the additional cube-zero equation, rather than only sharpen the final affine-fiber bound.

## 5. Where `A^3=0` has and has not been used

Theorem 2.1 only uses `rank A=r` and `rank A^2=s`; it is therefore a general rank-pair counting theorem for sign matrices.

The cube-zero hypothesis enters in Section 3 through the monotone kernel increments

\[
b_1\ge b_2\ge b_3,
\]

which identify the recovery profile and its balanced wedge. The proof still does **not** exploit the full operator equation

\[
A^3=0
\]

beyond these rank consequences. In rank-core variables the unused content is the square-zero relation for

\[
T=B^{-1}G:
\qquad T^2=0.
\tag{30}
\]

If `H=G_{P,Q}` is the chosen rank core and

\[
U=G_{*,Q},
\qquad
V=G_{P,*},
\]

then the rank factorization is

\[
G=UH^{-1}V,
\]

and `G B^{-1}G=0` is equivalent, because the outer factors have rank `s`, to the explicit `s x s` orthogonality constraint

\[
\boxed{V B^{-1}U=0.}
\tag{31}
\]

Equation (31) is the most concrete unused quadratic-scale information left by this run.

The next successful route must extract `Theta(n^2)` entropy from (31) in the linear-`s`, balanced-`t` wedge. Merely improving one affine column fiber cannot suffice.

## 6. Relation to the source metric

The source-level fixed metric remains

\[
0\le u_{GI}\le\frac12.
\]

No theorem here changes that interval. The source conjecture remains mathematically REFUTED by the earlier all-`n` block-shear family; the corrected `1/2` exponent is a recovery question, not part of Vu's original statement.

The substantive movement is restricted but real:

- previous cube-zero theorem: half exponent for `rank(A^2)=o(n/log n)`;
- present cube-zero theorem: half exponent for **every `rank(A^2)=o(n)`**, plus all macroscopic profiles satisfying (23);
- exact remaining obstruction: linear `s` inside the balanced wedge (24), with unused relation (31).

Novelty of these restricted counting statements is **UNVERIFIED** pending broader prior-art review.