Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# F0012 recovery 1 — nilpotent sign matrices: filtration entropy and a complete square-zero count

Target context: Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797, Section 9, Conjecture 9.5. The literal source conjecture is already REFUTED by the earlier R7-07 fixed-shear family. This note follows the STUCK1-selected recovery action: attack the simplest prescribed-characteristic-polynomial fiber

\[
N_0(n):=\#\{A\in\{\pm1\}^{n\times n}:\chi_A(x)=x^n\}.
\]

The source metric remains

\[
u_{GI}=\liminf_{n\to\infty}\frac{-\log_2\Pr(E_n)}{n^2},\qquad 0\le u_{GI}\le\frac12,
\]

and does **not** move in this note. The purpose is to isolate and solve a genuine subproblem of the matching-half-exponent upper-bound route.

## Idea before code

Nilpotence supplies a canonical object that arbitrary Gaussian-integral spectrum does not: the filtration

\[
0=K_0\subset K_1\subset\cdots\subset K_s=\mathbf R^n,
\qquad K_j=\ker A^j.
\]

Instead of summing over arbitrary rational complete flags, first freeze this canonical filtration and count the linear space of maps that lower it. Then test whether a sequential row/column reveal can control at least the first nontrivial nilpotency stratum, `A^2=0`. Only after deriving the formulas do we run a small exact census to see which Jordan/kernel profiles remain outside the solved stratum.

## B18 — say nilpotence in the language of the canonical kernel filtration

Let `A` be nilpotent and let

\[
b_j:=\dim K_j-\dim K_{j-1}\quad (1\le j\le s).
\]

### Lemma 1: the kernel increments are nonincreasing

For every `j<s`, the map induced by `A`,

\[
\bar A_j:K_{j+1}/K_j\longrightarrow K_j/K_{j-1},
\]

is injective. Indeed, if `x in K_{j+1}` and `Ax in K_{j-1}`, then `A^j x=A^{j-1}(Ax)=0`, so `x in K_j`. Therefore

\[
b_{j+1}\le b_j,
\]

and `b=(b_1,...,b_s)` is the conjugate-partition data of the nilpotent Jordan type. In particular

\[
\sum_{j=1}^s b_j=n.
\]

### Lemma 2: exact dimension of a fixed filtration-lowering space

Fix any filtration

\[
0=K_0\subset K_1\subset\cdots\subset K_s=\mathbf R^n
\]

with increments `b_j`. Define

\[
\mathcal L(K_\bullet):=\{T\in M_n(\mathbf R):T K_j\subset K_{j-1}\ \text{for every }j\}.
\]

Then

\[
\boxed{\dim \mathcal L(K_\bullet)
=\sum_{j=1}^s b_j\dim K_{j-1}
=\sum_{\ell<j}b_\ell b_j
=\frac12\left(n^2-\sum_{j=1}^s b_j^2\right).}
\tag{1}
\]

**Proof.** Choose complements `E_j` with `K_j=K_{j-1}\oplus E_j` and `dim E_j=b_j`. A map `T` lies in `\mathcal L(K_\bullet)` exactly when the restriction `T|_{E_j}` is an arbitrary linear map from `E_j` to `K_{j-1}`. These choices are independent over `j`, giving

\[
\sum_j (\dim E_j)(\dim K_{j-1})
=\sum_j b_j\sum_{\ell<j}b_\ell
=\sum_{\ell<j}b_\ell b_j.
\]

Using `(\sum_j b_j)^2=\sum_jb_j^2+2\sum_{\ell<j}b_\ell b_j` gives (1). QED.

Every nilpotent `A` with canonical kernel filtration `K_\bullet` belongs to `\mathcal L(K_\bullet)`, since `A K_j\subset K_{j-1}`.

### Lemma 3: hypercube section bound

If `L` is a `D`-dimensional real linear subspace of `\mathbf R^N`, then

\[
|L\cap\{\pm1\}^N|\le 2^D.
\tag{2}
\]

**Proof.** The coordinate functionals restricted to `L` span `L^*`. Choose `D` coordinates whose restrictions form a basis of `L^*`. Projection to these `D` coordinates is injective on `L`, while a sign vector has only `2^D` possible projected sign patterns. QED.

Combining (1) and (2), for a **fixed canonical kernel filtration** of profile `b`,

\[
\boxed{
\#\bigl(\mathcal L(K_\bullet)\cap\{\pm1\}^{n\times n}\bigr)
\le
2^{(n^2-\sum_j b_j^2)/2}.
}
\tag{3}
\]

This improves the earlier fixed-Borel estimate by forcing the diagonal to vanish and by retaining the complete Jordan-profile defect `\frac12\sum b_j^2`.

Let `\mathfrak F_b(n)` be the set of canonical kernel filtrations with increment profile `b` that are actually realized by nilpotent sign matrices. Then

\[
\boxed{
N_b(n)
\le
|\mathfrak F_b(n)|\,
2^{(n^2-\sum_j b_j^2)/2}.
}
\tag{4}
\]

There are only `p(n)=\exp(O(\sqrt n))` possible profiles `b`, so the Jordan-profile sum itself costs only `2^{o(n^2)}`. The unresolved quantity has therefore become **realized-filtration entropy**, not Jordan-profile entropy. A uniform bound

\[
\log_2|\mathfrak F_b(n)|
\le \frac12\sum_j b_j^2+o(n^2)
\tag{5}
\]

would prove `N_0(n)\le2^{n^2/2+o(n^2)}`. The stronger but simpler sufficient condition `|\mathfrak F_b(n)|=2^{o(n^2)}` for every profile would also suffice.

### Sharpness test: the nilpotent fiber itself already has half entropy

The previous fixed-shear construction used, for `n=2m`,

\[
M=\begin{pmatrix}A&B\\ C&D\end{pmatrix},\qquad
S=\begin{pmatrix}I&0\\ I&I\end{pmatrix},
\]

with

\[
S^{-1}MS=
\begin{pmatrix}
A+B&B\\ C+D-A-B&D-B
\end{pmatrix}.
\]

Impose `C+D=A+B`, make `A+B` upper triangular and `D-B` lower triangular as before, and now additionally force the diagonal entries of **both** diagonal blocks to be zero. At each off-diagonal scalar position there are exactly four sign quadruples, as in the original family. At a diagonal position the equations

\[
a+b=0,\qquad d-b=0,\qquad c+d=a+b
\]

have exactly two sign solutions. Hence there are exactly

\[
4^{m(m-1)}2^m
=2^{2m^2-m}
=2^{n^2/2-n/2}
\tag{6}
\]

matrices in this subfamily. After reversing the lower block order, `S^{-1}MS` is strictly upper triangular, so every one of them is nilpotent. Thus

\[
\boxed{N_0(2m)\ge2^{2m^2-m}.}
\tag{7}
\]

The desired upper exponent `1/2` for the nilpotent fiber is therefore **best possible at quadratic scale**. Also, `N_0(n)=0` for odd `n`, because nilpotence forces `tr(A)=0`, while a sum of an odd number of `\pm1` diagonal entries cannot vanish.

## B19 — make the reveal algorithm explicit: complete square-zero upper bound

The first nontrivial nilpotency-index stratum can be counted directly.

For `1\le r\le n/2`, define

\[
\mathcal Z_{n,r}
:=\{A\in\{\pm1\}^{n\times n}:A^2=0,\ \operatorname{rank}A=r\}.
\]

### Theorem 4: square-zero rank-r count

\[
\boxed{
|\mathcal Z_{n,r}|
\le
\binom nr^2\,2^{2r(n-r)}.
}
\tag{8}
\]

Consequently

\[
\boxed{
\#\{A\in\{\pm1\}^{n\times n}:A^2=0\}
\le 2^{n^2/2+O(n)}.
}
\tag{9}
\]

**Proof.** Fix `A in \mathcal Z_{n,r}`. Choose row and column index sets `I,J`, each of size `r`, such that the minor

\[
B:=A_{I,J}
\]

is nonsingular. There are at most `\binom nr^2` choices of `(I,J)`.

Expose the `r` basis rows

\[
R:=A_{I,*}\in\{\pm1\}^{r\times n}.
\]

There are at most `2^{rn}` possibilities. Since `B` is nonsingular, `R` has rank `r`.

Now expose the `r` basis columns `c_j=A_{*,j}` for `j in J`. From `A^2=0`, for every `i in I` and every `j`,

\[
0=(A^2)_{ij}=R_i\cdot c_j,
\]

so every `c_j` lies in `\ker R`, an `(n-r)`-dimensional subspace of `\mathbf R^n`.

The coordinates of `c_j` on `I` are already fixed: `\pi_I(c_j)=A_{I,j}`, the `j`th column of `B`. Because the `r` columns of `B` span `\mathbf R^r`, if any completion exists then the restricted coordinate projection

\[
\pi_I|_{\ker R}:\ker R\to\mathbf R^r
\]

must have full rank `r`. Therefore each fiber

\[
\{x\in\ker R:\pi_I(x)=A_{I,j}\}
\]

is either empty or an affine subspace of dimension

\[
(n-r)-r=n-2r.
\]

An affine `d`-plane contains at most `2^d` sign vectors by the same injective-coordinate argument as (2). Thus, after `R` is fixed, each basis column has at most `2^{n-2r}` possibilities, and all `r` basis columns together have at most

\[
2^{r(n-2r)}
\]

possibilities.

Finally, a rank-`r` matrix is uniquely determined by its basis rows and basis columns around a nonsingular overlap. Explicitly, with `C=A_{*,J}`,

\[
A=C B^{-1}R.
\]

Hence, for each `(I,J)`, the number of possibilities is at most

\[
2^{rn}2^{r(n-2r)}=2^{2r(n-r)}.
\]

Multiplying by `\binom nr^2` proves (8).

Since `A^2=0` implies `r\le n/2`, and `2r(n-r)\le n^2/2`, summing (8) gives, for example,

\[
\sum_{r\le n/2}|\mathcal Z_{n,r}|
\le
(n+1)2^{2n}2^{n^2/2},
\]

which is (9). QED.

This is the first complete half-exponent upper bound for a nontrivial nilpotent-index stratum obtained in this recovery cycle. It does **not** prove the all-nilpotent target: nilpotency index at least three is not controlled by the square-zero reveal argument.

## B30 — one profile and one nilpotency index at a time

The canonical profile reduction shows exactly how to localize the remaining problem. The exact checker enumerates all sign matrices through `n=4` using only integer matrix multiplication and rational Gaussian elimination. It returns

- `n=1`: no nilpotent sign matrices;
- `n=2`: 4 nilpotent matrices, all profile `(1,1)` and square-zero;
- `n=3`: no nilpotent sign matrices;
- `n=4`: 2064 nilpotent matrices, split as
  - profile `(1,1,1,1)`: 1152;
  - profile `(2,1,1)`: 768;
  - profile `(2,2)`: 96;
  - profile `(3,1)`: 48.

Only the last two profiles are square-zero, for a total of 144. Thus at `n=4`, `1920/2064` nilpotent sign matrices already have nilpotency index at least three. The new square-zero theorem is therefore a genuine solved stratum but not a plausible stand-in for the whole nilpotent fiber.

The smallest unsolved structural class suggested by this census is **nilpotency index three**, beginning with profile `(2,1,1)` at `n=4`. In filtration notation, the next route should freeze

\[
0\subset K_1\subset K_2\subset K_3=\mathbf R^n
\]

and quantify the additional entropy cost of simultaneously satisfying `A K_3\subset K_2`, `A K_2\subset K_1`, and the sign constraints, relative to the solved `K_2=\mathbf R^n` square-zero case.

## Exact finite certificate

Executed checker:

`research7_2026-09-17/R7-07/artifacts/2026-09-19/2026-09-19T041300Z__F0012_nilpotent_recovery_exact_check.py`

Archived output:

`research7_2026-09-17/R7-07/artifacts/2026-09-19/2026-09-19T041300Z__F0012_nilpotent_recovery_exact_check.out`

Terminal line:

`F0012_NILPOTENT_RECOVERY_EXACT_CHECK_PASS`

The checker verifies the `n<=4` census, the local `4/2` fixed-shear counts and formula (6), and finite numerical instances of the rank-summed square-zero bound. The proof of Theorem 4 is on the page and does not depend on the checker.

## What moved and what did not

The **source metric does not move**:

\[
0\le u_{GI}\le\frac12\quad\longrightarrow\quad 0\le u_{GI}\le\frac12.
\]

The recovery subproblem nevertheless advances materially:

1. the all-nilpotent target is proved sharp from below at exponent `1/2` along every even dimension, via (7);
2. every fixed canonical kernel filtration has the exact cube-section exponent (3);
3. the entire square-zero stratum satisfies the desired `1/2` upper exponent, via (9);
4. the remaining obstruction is localized to nilpotency index at least three / realized-filtration entropy.

No claim is made that the full nilpotent fiber satisfies the desired upper bound, and no claim is made that these lemmas are novel in the literature. Novelty remains **UNVERIFIED**.

## Next nonrepeating attack

Use methods not previously used on F0012:

- **B6 — deform to a point you can solve:** deform from the now-solved `A^2=0` stratum to `A^3=0`, freezing one three-step kernel profile and measuring exactly which extra completions appear.
- **B20 — find why the algorithm fails:** identify the exact step in the rank-certificate reveal proof that breaks when `A^2` is nonzero but `A^3=0`; express that defect as a finite-dimensional intermediate map rather than an informal obstruction.
- **B27 — swap the quantifiers:** first prove a uniform half-exponent bound for every fixed three-step dimension profile, then sum the subexponentially many profiles, rather than attempting all nilpotent matrices at once.
