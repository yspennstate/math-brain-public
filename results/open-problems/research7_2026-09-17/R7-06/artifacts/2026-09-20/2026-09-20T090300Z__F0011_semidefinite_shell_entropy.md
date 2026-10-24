Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated binding model/effort selector or runtime telemetry is exposed.

# F0011 — semidefinite arithmetic-shell rigidity and subquadratic Gram-skeleton entropy

Date: 2026-09-20 UTC  
Role: C05 / R7-06, current registry native ID `6aabe827777c8191a43330b4a87d481d`  
Canonical target: F0011 / Van H. Vu, *Recent progress in combinatorial random matrix theory*, Conjecture 9.4  
Status: **PROVED PARTIAL** toward the source conjecture, pending later independent review. No source-level closure or external novelty claim.

## 1. Source target and inherited low-rank reduction

Vu's Conjecture 9.4 states for the symmetric Rademacher matrix `M_n^sym` (independent fair signs on and above the diagonal, completed by symmetry)

\[
\Pr\bigl(\operatorname{Spec}(M_n^{\rm sym})\subset\mathbb Z\bigr)
=2^{-(1/2+o(1))n^2}.
\]

Equivalently, the total number of labelled symmetric sign matrices with integral spectrum is `2^{o(n^2)}`. The source statement does not fix a spectrum. The project reduction to fixed spectral fibers is legitimate at the exponent scale because only `2^{O(n)}` integral spectra are possible, but the active C05 work below remains only a restricted two-eigenvalue bridge.

The active restricted family is

\[
H=H^T\in\{\pm1\}^{N\times N},\qquad H^2=NI,
\]

on the integral branch `sqrt(N) in Z`. Write `N=2r` and take a balanced cut

\[
H=\begin{pmatrix}P&C\\ C^T&D\end{pmatrix}.
\]

The preceding C05 runs proved that an entropy-near-extremal fixed-half-rowspace fiber has

\[
K:=CC^T=\lambda I+R,
\qquad q:=\operatorname{rank}R=o(r),
\]

with

\[
|\lambda-r|\le \frac{rq}{r-q},
\qquad 0\preceq K\preceq 2rI,
\]

and, once `q<r-2`, the exact parity theorem gives

\[
\lambda\in4\mathbb Z.
\]

Put

\[
\delta:=r-\lambda=R_{ii}.
\]

Because `2r` is an even perfect square on this branch, `r` is even. The goal of this note is to understand the first arithmetic shells `|delta|=2,4` **in all dimensions**, without assuming `C` invertible and without excluding the singular/corank endpoint.

---

## 2. Universal two-class mod-four skeleton

For row `i` of `C`, let `b_i in {0,1}^r` mark its `-1` entries and put

\[
w_i:=|b_i|\pmod2.
\]

The exact identity from the previous run is

\[
\frac{K}{2}
\equiv
\left(\frac r2\bmod2\right)J
+w\mathbf1^T+\mathbf1w^T
\pmod2.
\]

Because `lambda/2` is even, the same formula holds for `R/2`:

\[
\boxed{
\frac{R}{2}
\equiv
\left(\frac r2\bmod2\right)J
+w\mathbf1^T+\mathbf1w^T
\pmod2.
}
\tag{2.1}
\]

Let `A={i:w_i=0}` and `B={i:w_i=1}`. Then:

- if `r=0 (mod 4)`, `R_ij/2` is odd exactly when `i,j` lie in opposite parity classes;
- if `r=2 (mod 4)`, `R_ij/2` is odd exactly when `i,j` lie in the same parity class.

Equivalently,

\[
\boxed{
\begin{array}{ll}
r\equiv0\pmod4:&R_{ij}\equiv2\pmod4\iff i,j\text{ are in opposite classes},\\[1mm]
r\equiv2\pmod4:&R_{ij}\equiv2\pmod4\iff i,j\text{ are in the same class}.
\end{array}}
\tag{2.2}
\]

This is an all-dimensional, exact, two-block congruence skeleton for every low-rank defect in the inherited branch.

---

## 3. A basis-free covariance packing lemma

The following lemma is useful independently of sign matrices.

### Lemma 3.1

Let `x_1,...,x_a,y_1,...,y_b` be vectors in a real inner-product space such that

\[
\|x_i\|^2=\|y_j\|^2=d,
\]

all distinct `x_i` are mutually orthogonal, all distinct `y_j` are mutually orthogonal, and

\[
|\langle x_i,y_j\rangle|\ge c>0
\quad\text{for every }i,j.
\]

Then

\[
\boxed{\max(a,b)\le (d/c)^2.}
\tag{3.1}
\]

#### Proof

Let `E` be the `a x b` cross-Gram matrix. The full Gram matrix is

\[
G=\begin{pmatrix}dI_a&E\\E^T&dI_b\end{pmatrix}\succeq0.
\]

Hence every singular value of `E` is at most `d`. On the other hand,

\[
\|E\|_F^2\ge abc^2.
\]

Since `rank(E)<=min(a,b)`,

\[
\|E\|_{op}^2
\ge \frac{\|E\|_F^2}{\min(a,b)}
\ge c^2\max(a,b).
\]

Combining `||E||_op<=d` proves (3.1). ∎

For the shell `|delta|=4` below, `d=2,c=1`, so each side has at most four distinct directions whenever both parity classes occur.

---

## 4. Exact semidefinite shell `|delta|=2`: no higher-rank branch exists

Assume `|delta|=2` and the defect is semidefinite with the sign of its diagonal; i.e.

\[
S:=\frac{\operatorname{sgn}(\delta)}2R\succeq0.
\]

Then `S` is an integral PSD matrix with diagonal `1`. Write

\[
S_{ij}=\langle x_i,x_j\rangle,
\qquad \|x_i\|=1.
\]

Every `S_ij` is an integer in `[-1,1]`, hence belongs to `{-1,0,1}`. Thus

- `S_ij=+-1` means `x_i=+-x_j`;
- `S_ij=0` means `x_i` and `x_j` are orthogonal.

Because `lambda in 4Z` and `|delta|=2`, necessarily `r=2 (mod 4)`. By (2.2), `S_ij` is odd exactly when `i,j` have the same row-parity label. Therefore all rows in one parity class lie on a single line, while the two parity classes, if both nonempty, are orthogonal.

Consequently

\[
\boxed{\operatorname{rank}R\le2.}
\tag{4.1}
\]

For the inherited nonzero dangerous branch and `r>2`, the trace/spectral-cap bound already forces rank at least two, so in fact

\[
\boxed{q=2.}
\tag{4.2}
\]

After simultaneous switching and permutation,

\[
R=+2\operatorname{diag}(J_a,J_b)
\]

in the positive shell and

\[
R=-2\operatorname{diag}(J_a,J_b)
\]

in the negative shell. The preceding run's determinant and PSD argument then recovers the exact block-size restrictions: `a=b=r/2` in the positive branch and `|a-b|<=2` in the negative branch, including its singular endpoint.

Thus the `|delta|=2` semidefinite shell is **completely exhausted** by the previously identified defect-two D-optimal/Ehlich--Wojtas layer. There is no hidden higher-rank semidefinite family at the same arithmetic distance from the scalar Gram point.

### Gram-skeleton entropy

The labelled defect matrix is determined by the parity class of each row and one switching sign per row. Hence this entire shell has at most

\[
\boxed{2^{O(r)}}
\tag{4.3}
\]

possible Gram defects. This counts Gram skeletons, not sign roots of an individual Gram matrix.

---

## 5. Exact semidefinite shell `|delta|=4`: orthogonal blow-ups or a rank-four two-cloud core

Assume now `|delta|=4` and again

\[
S:=\frac{\operatorname{sgn}(\delta)}2R\succeq0.
\]

Then `S` is integral PSD with diagonal `2`. Write

\[
S_{ij}=\langle x_i,x_j\rangle,
\qquad \|x_i\|^2=2.
\]

Because `lambda in 4Z` and `|delta|=4`, necessarily `r=0 (mod 4)`. By (2.2), `S_ij` is odd exactly across the two row-parity classes.

### 5.1. Geometry inside and across parity classes

If `i,j` lie in the same parity class, then `S_ij` is even. Since `|S_ij|<=2`,

\[
S_{ij}\in\{-2,0,2\}.
\]

Thus two same-class vectors are either parallel/antiparallel or orthogonal.

If `i,j` lie in opposite parity classes, then `S_ij` is odd, hence

\[
\boxed{S_{ij}=+-1.}
\tag{5.1}
\]

Collapse parallel/antiparallel vectors to unoriented direction classes. Let there be `a` distinct directions in parity class `A` and `b` in parity class `B`. Choosing representatives gives the finite core Gram matrix

\[
G_{a,b}(E)=
\begin{pmatrix}
2I_a&E\\E^T&2I_b
\end{pmatrix},
\qquad E\in\{+-1\}^{a\times b}.
\tag{5.2}
\]

If one parity class is empty, the remaining distinct directions are pairwise orthogonal. Hence after switching and permutation

\[
\boxed{
S=2\operatorname{diag}(J_{a_1},\ldots,J_{a_q})
}
\tag{5.3}
\]

for a set partition `a_1+...+a_q=r`. This is an exact orthogonal-block blow-up with arbitrary rank `q`.

If both parity classes are nonempty, Lemma 3.1 with `d=2,c=1` gives

\[
\boxed{a,b\le4.}
\tag{5.4}
\]

There is a further rank collapse.

### Theorem 5.1 — the two-parity core has rank at most four

If `a,b>0` and (5.2) is PSD, then

\[
\boxed{\operatorname{rank}G_{a,b}(E)\le4.}
\tag{5.5}
\]

#### Proof

Assume `a>=b`. PSD is equivalent to every singular value of `E` being at most `2`.

If `a=4`, then

\[
\|E\|_F^2=4b.
\]

There are at most `b` singular values and each has square at most `4`; equality of the sums forces all `b` singular values to equal `2`. Each such singular value contributes one zero eigenvalue to the block Gram matrix, so

\[
\operatorname{rank}G=4+b-b=4.
\]

If `a<=2`, then `a+b<=4` and the claim is immediate. It remains to take `a=3`.

For `b=1`, again `a+b=4`.

For `b=2`, the column Gram has the form

\[
E^TE=\begin{pmatrix}3&c\\c&3\end{pmatrix},
\]

where `c` is odd. The spectral bound `||E||_op<=2` gives `3+|c|<=4`, so `|c|=1`. Thus the squared singular values are `4,2`; one singular value equals `2`, and

\[
\operatorname{rank}G=5-1=4.
\]

For `b=3`, every off-diagonal column inner product is odd and, by the same two-column argument, has absolute value one. Write

\[
E^TE=3I+A,
\]

where `A` is a `3 x 3` zero-diagonal sign matrix. If the product of its three upper-triangular signs is `+1`, then `A` is switching-equivalent to `J-I` and has eigenvalues `2,-1,-1`, which would give `lambda_max(E^TE)=5`, impossible. Hence the sign product is `-1`; then `A` has eigenvalues `1,1,-2`, so `E^TE` has eigenvalues `4,4,1`. Two singular values of `E` equal `2`, and

\[
\operatorname{rank}G=6-2=4.
\]

This exhausts all cases. ∎

For `r>12`, semidefiniteness and `tr R=+-4r` also force `q>=4`; therefore any nonempty two-parity branch has exactly

\[
\boxed{q=4}
\tag{5.6}
\]

for all sufficiently large inherited orders.

### 5.2. Uniform Gram-skeleton entropy of the `|delta|=4` shell

The shell has only subquadratic Gram-skeleton complexity.

- **One parity class.** Equation (5.3) says the defect is a signed blow-up of an orthogonal set. A labelled set partition of `[r]` into at most `r` blocks and one sign per row specify the matrix. Crude counting gives at most
  \[
  r^r2^r=2^{O(r\log r)}
  \]
  possibilities.

- **Both parity classes.** There are at most four direction classes on each side. The parity label, direction label, and switching sign of every row use only `O(1)` bits per row, and the finite cross-core `E` has at most `2^{16}` possibilities. Hence this part has only
  \[
  2^{O(r)}
  \]
  possible defects.

Therefore

\[
\boxed{
\#\{R:\ R\text{ is a semidefinite sign-Gram defect with }|\delta|=4\}
\le 2^{O(r\log r)}
=2^{o(r^2)}.
}
\tag{5.7}
\]

Again, this is a **Gram-skeleton** count. It does not bound the number of sign roots `C` sharing one such Gram matrix.

The argument never assumes `K` invertible. In particular the negative-semidefinite branch may contain zero eigenvalues of `K`; the singular/corank endpoint is retained rather than discarded.

---

## 6. Combined low-shell theorem and what it changes

Combining Sections 4 and 5:

### Theorem 6.1 — first two semidefinite arithmetic shells have subquadratic skeleton entropy

In the inherited F0011 low-rank branch (`q<r-2`, hence `lambda in 4Z`), suppose `R=CC^T-lambda I` is semidefinite with the sign of its constant diagonal `delta=r-lambda` and `|delta|<=4`. Then:

1. `delta=0` forces `R=0`;
2. `|delta|=2` forces `q=2` and is exactly the saturated Ehlich--Wojtas/D-optimal defect-two layer (with the already classified negative singular endpoint);
3. `|delta|=4` is either an orthogonal block blow-up (one parity class) or a rank-four two-cloud core (both parity classes);
4. across all these cases the number of labelled Gram defects is
   \[
   \boxed{2^{O(r\log r)}=2^{o(r^2)}}.
   \]

This is an actual source-scale entropy statement for the **intermediate Gram skeleton**. It removes one possible obstruction: quadratic entropy cannot come from merely choosing a semidefinite defect matrix in the first two arithmetic shells.

What remains is the harder root-fiber entropy. The exact scalar shell `R=0` is Hadamard-hard; the `|delta|=2` shell contains saturated D-optimal root fibers; and the `|delta|=4` one-parity branch asks for sign roots of mutually orthogonal equidistant row blocks. A proof of Vu's source conjecture still needs a `2^{o(r^2)}` control on those root multiplicities or a recursive reduction that contracts squared dimensions.

Thus the current bottleneck is now cleanly separated into two pieces:

- **skeleton entropy:** solved at source scale for semidefinite `|delta|<=4`;
- **root multiplicity:** still open and already contains classical Hadamard/D-optimal counting hardness.

For higher shells (`|delta|>=6` in the `r=2 mod 4` case, `|delta|>=8` in the `r=0 mod 4` case), or for indefinite defects, the above small-norm geometry no longer collapses to unit/root directions and a new argument is required.

---

## 7. Literature boundary checked this run

Fresh bounded checks on 20 September 2026 recovered:

- Van H. Vu, *Recent progress in combinatorial random matrix theory*, Probability Surveys 18 (2021), Conjecture 9.4 / arXiv:2005.02797 — the exact outside target above.
- Asaf Ferber, Vishesh Jain and Yufei Zhao, *On the number of Hadamard matrices via anti-concentration*, Combinatorics, Probability and Computing 31 (2022), arXiv:1808.07222 — the best relevant general counting framework in this line still gives a positive quadratic exponent rather than `2^{o(n^2)}`.
- Richard P. Brent, *Finding D-optimal designs by randomised decomposition and switching* (Australasian Journal of Combinatorics 55, 2013) — fixed maximal Gram matrices can support many inequivalent sign decompositions, so a skeleton count is not a root-fiber count.

A bounded fresh search did not surface a later paper resolving Vu's exact Conjecture 9.4 or a general subquadratic count for saturated D-optimal sign roots. This is negative search evidence only, not an openness or novelty certificate.

---

## 8. Next mathematical attack

The strongest next step is **root-fiber recursion for the low shells**, not another finite census.

For the one-parity `|delta|=4` branch, after switching and permutation one has

\[
CC^T=(r-4)I+4\operatorname{diag}(J_{a_1},\ldots,J_{a_q})
\]

or the negative-shell analogue. Hence the rows of `C` split into mutually orthogonal groups with an exactly prescribed equidistant Gram inside each group. The next target is to prove that the number of sign roots of all such block-Gram matrices is `2^{o(r^2)}` whenever the squared block sizes contract, or else extract an explicit embedding of a smaller Hadamard/D-optimal root problem from a noncontracting block.

A parallel route is to treat the first indefinite shell. The mod-four parity partition (2.2) survives there, but the PSD vector collapse does not. A useful theorem would turn low real rank plus the exact two-class residue pattern into a bounded-complexity signed-bilinear core, or construct a genuine high-type counterfamily showing that such a reduction is false.
