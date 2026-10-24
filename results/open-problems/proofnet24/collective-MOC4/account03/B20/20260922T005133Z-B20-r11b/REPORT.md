# MOC4 account03/B20 r11b — universal two-slack floor for the unique bad assignment regime

**Programme:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Target:** four-dimensional Marcus–de Oliveira conjecture (`MOC4`)  
**Outcome:** `NEW_UNIVERSAL_CONDITIONAL_THEOREM + STRICT_RESIDUAL_NARROWING`; full MOC4 remains **OPEN / NOT PROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN` (latest owner control suspends new full-brain installation work).

## 1. Exact inputs consumed

This run inherits the exact scalar reduction from account03/B20 r11:

`proofnet24/collective-MOC4/account03/B20/20260922T001447Z-B20-r11/REPORT.md`.

For each structured support direction, that report defines a real `3 x 3` matrix `G`, the pair-class coefficient matrix `X`,

\[
K_{\alpha\beta}=|G_{\alpha\beta}|+\tfrac12X_{\alpha\beta},
\]

and, for the unitary-derived complement-pair matrices `(R,D)`, two nonnegative slacks

\[
A(U)=K_*-\langle R,K\rangle,
\qquad
S(U)=\sum_{\alpha,\beta}|G_{\alpha\beta}|
\bigl(r_{\alpha\beta}-\operatorname{sgn}(G_{\alpha\beta})d_{\alpha\beta}\bigr).
\]

For `rho in S_3`, write

\[
K_\rho=\sum_\alpha K_{\alpha,\rho(\alpha)},
\]

and

\[
\delta_\rho=
\begin{cases}
0,&\prod_\alpha G_{\alpha,\rho(\alpha)}\ge0,\\
2\min_\alpha|G_{\alpha,\rho(\alpha)}|,&\prod_\alpha G_{\alpha,\rho(\alpha)}<0.
\end{cases}
\]

Then

\[
K_*=\max_\rho K_\rho,
\qquad
\Delta=K_*-\max_\rho(K_\rho-\delta_\rho),
\]

and the exact support inequality is equivalent to

\[
\boxed{A(U)+S(U)\ge\Delta.}\tag{1}
\]

I also consumed the newest completed assigned-partner result

`account04/B09/B09-20260922T001200Z-MOC4-r02/REPORT.md`.

That report refutes the tempting unrestricted common `(P,R)` permutation lift and proves that the actual simple-spectrum coefficient matrices satisfy an exact Vandermonde/Bezout structure. Consequently this run does **not** introduce a common classical coupling. It stays inside the structured support reduction (1), exactly where the partner report says a surviving proof must live.

## 2. The residual regime from r11

Suppose `K_rho` has a unique maximizing assignment `rho_0`, and that the selected sign product is negative. Put

\[
m=\min_\alpha |G_{\alpha,\rho_0(\alpha)}|>0.\tag{2}
\]

For every competitor `tau != rho_0`, let

\[
q(\tau)=\#\{\alpha:\tau(\alpha)\ne\rho_0(\alpha)\}\in\{2,3\},
\]

and define

\[
\boxed{\kappa=\min_{\tau\ne\rho_0}
\frac{K_*-K_\tau}{q(\tau)}.}\tag{3}
\]

The previous r11 theorem proved the support inequality whenever `kappa >= m`. The open part therefore included the regime `kappa < m`.

The main observation below is that the same two nonnegative slacks already have a nontrivial universal floor even when `kappa < m`.

## 3. New theorem: the universal two-slack floor

### Theorem

Under the unique parity-bad maximizer assumptions above, for **every** unitary `U`,

\[
\boxed{A(U)+S(U)\ge 2\min\{m,\kappa\}.}\tag{4}
\]

Therefore the MOC4 support inequality in this direction is proved whenever

\[
\boxed{\Delta\le2\min\{m,\kappa\}.}\tag{5}
\]

This strictly extends the r11 criterion: when `kappa >= m`, (5) is automatic because `Delta <= 2m`; when `kappa < m`, (5) can still hold and gives genuinely new coverage.

### Proof

Relabel the three pair classes so that `rho_0` is the identity. Set

\[
E=\sum_{\alpha=1}^3(1-r_{\alpha,\rho_0(\alpha)}).\tag{6}
\]

Take any Birkhoff decomposition

\[
R=\sum_{\tau\in S_3}\mu_\tau P_\tau.
\]

Both `E` and `A` are linear in `R`, hence

\[
E=\sum_\tau\mu_\tau q(\tau),\tag{7}
\]

and

\[
A(U)=\sum_\tau\mu_\tau(K_*-K_\tau)
\ge\kappa E.\tag{8}
\]

Now let

\[
s_\alpha=\operatorname{sgn}(G_{\alpha,\rho_0(\alpha)}).
\]

Because the selected sign product is negative, `(s_1,s_2,s_3)` has odd parity. The exact Hadamard-block identity `D=(HPH^T)_{mean-zero}` and a Birkhoff decomposition of `P` imply the standard parity inequality

\[
\sum_\alpha s_\alpha d_{\alpha,\rho_0(\alpha)}\le1.\tag{9}
\]

Keeping only the three `rho_0` cells in the definition of `S` and using the minimum magnitude `m`,

\[
\begin{aligned}
S(U)
&\ge m\sum_\alpha
\bigl(r_{\alpha,\rho_0(\alpha)}-s_\alpha d_{\alpha,\rho_0(\alpha)}\bigr)\\
&\ge m\bigl((3-E)-1\bigr).
\end{aligned}
\]

Together with `S>=0`, this is

\[
S(U)\ge m(2-E)_+.\tag{10}
\]

Combining (8) and (10),

\[
A(U)+S(U)\ge \kappa E+m(2-E)_+.\tag{11}
\]

For `0<=E<=2`, the right side is

\[
2m+(\kappa-m)E,
\]

whose minimum on that interval is `2m` if `kappa>=m` and `2kappa` if `kappa<m`. For `E>=2`, (8) gives `A>=2kappa`. Hence over all `E in [0,3]`,

\[
A+S\ge2\min\{m,\kappa\},
\]

proving (4). Combining with the exact equivalence (1) proves (5). QED.

## 4. A useful automatic subcase inside `kappa < m`

The new floor immediately settles an important part of the previously uncovered regime.

### Corollary

Assume `rho_0` is the unique bad maximizer. If a competitor `tau` attaining the minimum in (3)

1. differs from `rho_0` in exactly two rows (`q(tau)=2`), and
2. has nonnegative selected `G`-product (`delta_tau=0`),

then the support inequality holds for every unitary, with no assumption that `kappa>=m`.

Indeed,

\[
\Delta
=K_*-\max_\rho(K_\rho-\delta_\rho)
\le K_*-K_\tau
=2\kappa.\tag{12}
\]

If `kappa<m`, equation (4) gives `A+S>=2kappa>=Delta`; if `kappa>=m`, the old `Delta<=2m` argument applies.

Thus a possible failure in the unique-bad-maximizer regime is forced into a sharper corner:

\[
\boxed{\kappa<m,\qquad \Delta>2\kappa,}\tag{13}
\]

and in particular no normalized-gap-minimizing transposition can be parity-good.

This is the first unpaid universal step from the previous B20 report: it removes a genuine subset of the residual `kappa<m` region without assuming the false `(P,R)` joint lift refuted by account04/B09.

## 5. Exact structured example that is newly covered

To verify that the new regime is nonempty for **actual structured spectral coefficients**, take

\[
a=(-1+i,-3,-1-3i,-1-i),
\]

\[
b=(2-2i,-2-i,-3i,-1-i),
\qquad \eta=-1+2i.
\]

All four `a` values and all four `b` values are distinct. Applying the exact coefficient construction from the mixed-minor reduction gives

\[
G=\frac14
\begin{pmatrix}
-111&-351&-301\\
23&119&-99\\
159&239&-51
\end{pmatrix},
\]

and

\[
X=
\begin{pmatrix}
22&18&15\\
108&112&65\\
202&118&155
\end{pmatrix}.
\]

For the six permutations of three pair classes, in lexicographic order,

\[
(K_\rho)=\frac14(859,859,987,1179,1045,1237),\tag{14}
\]

while

\[
(\delta_\rho)=(0,0,0,0,23/2,119/2).\tag{15}
\]

Hence the unique maximizer is

\[
\rho_0=(3,2,1)
\]

in one-based notation, with

\[
m=119/4.\tag{16}
\]

The nearest normalized competitor is the transposition-type assignment

\[
\tau=(2,3,1),
\]

which is parity-good and satisfies

\[
q(\tau)=2,
\qquad
\kappa=\frac{29}{4}<\frac{119}{4}=m.\tag{17}
\]

Thus the old r11 criterion `kappa>=m` fails strongly. Nevertheless

\[
\Delta=\frac{29}{2}=2\kappa
=2\min\{m,\kappa\},\tag{18}
\]

so the new theorem certifies the support inequality for **every** unitary for this spectral direction.

This example also lies on the simple-spectrum generic locus emphasized by account04/B09 r02. Its Vandermonde products are

\[
\Delta_a=240+160i,
\qquad
\Delta_b=-76-168i,
\]

so the peer identity

\[
\det\widetilde G_{complex}
=-\tfrac12\Delta_a\Delta_b
\]

is nonzero (`-4320+26240i`). The new coverage therefore is not merely a repeated-eigenvalue boundary phenomenon.

## 6. What remains and the next attack

Full MOC4 remains **OPEN**. For a unique bad maximizer, only the stricter residual

\[
\kappa<m,
\qquad
\Delta>2\kappa
\]

needs further work. Multiple maximizing assignments with parity loss remain a separate regime.

Equation (11) also identifies precisely why the next input must be genuinely unitary rather than another assignment relaxation: the scalar Birkhoff/parity information bottoms out at `2 min(m,kappa)`. To go beyond (13), the next worker should exploit the row/column Plucker triangle constraints

\[
\sqrt{r_{\alpha\beta}^2-d_{\alpha\beta}^2}
\le
\sqrt{r_{\alpha\gamma}^2-d_{\alpha\gamma}^2}
+
\sqrt{r_{\alpha\xi}^2-d_{\alpha\xi}^2}
\]

(and the column analogues) together with the structured coefficient identities from account04/B09 r02. The target is to prove that, in the residual region `Delta>2kappa`, leakage of `R` toward the closest bad competitor necessarily creates additional wrong-orientation minor mass in `S` beyond the coarse parity floor (10).

No claim of full MOC4, a counterexample, or worldwide novelty is made.
