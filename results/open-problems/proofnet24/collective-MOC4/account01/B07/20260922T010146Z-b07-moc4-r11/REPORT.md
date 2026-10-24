# MOC4 account01/B07 r11 — assignment-dual / Plücker strengthening of the exact mixed-minor reduction

**Programme:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Target:** Marcus–de Oliveira determinant hull for all complex normal `4 x 4` pairs  
**Worker:** account01/B07  
**Candidate:** `MOC4-DUAL-PLUCKER-FLOOR-v1`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; MOC4 remains **OPEN / NOT PROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Source-exact target and peer inputs actually used

After diagonalizing one member of the normal pair, the source-exact target is

\[
D_U(a,b):=\det(D_a+UD_bU^*)\in
\operatorname{conv}\{v_\sigma(a,b):\sigma\in S_4\},
\qquad
v_\sigma=\prod_{i=1}^4(a_i+b_{\sigma(i)}),
\]

for every `a,b in C^4` and every `U in U(4)`, including singular sums and repeated spectra.

This run directly consumes the assigned OTHER-account partner **account02/B08**, candidate
`MOC4-BOUNDARY-CORE-AND-COLLAR-v1`, scientific commit
`05ac3fec5e80a9471306a892a397d744faf20f50`.  That result proves, using its preceding
`MOC4-DOUBLE-EIGENVALUE-LIFT-v1`, the repeated-spectrum and common-reducing-block
boundaries, and proves the exact gauge

\[
(A,B)\mapsto(A+tI,B-tI)
\]

preserves both `A+B` and every one of the 24 comparison vertices.  Consequently full MOC4 is
reduced without approximation to the simple-spectrum, individually-invertible, irreducible
core (while `A+B` itself may remain singular).  Its strict repeated-face collar also shows that
a counterexample cannot hide generically on a repeated-eigenvalue face.

I also use the exact account03/B20 scalar reduction and its newest strengthening,
`20260922T005133Z-B20-r11b`, scientific commit
`8f013e4309d6c5f87b16a28e8f2d665bda5e3b95`.  In the notation recalled below, it proves

\[
\text{MOC4 support inequality}\iff A(U)+S(U)\ge \Delta,
\]

and, for a unique parity-bad maximizing pair-class assignment, the universal floor

\[
A(U)+S(U)\ge 2\min\{m,\kappa\}.
\]

The new result below is a strict refinement of the mechanism behind that floor: it does not
collapse all nonmaximal assignment gaps to the single number `kappa`, and it converts every
surplus reduced cost into a positive complementary-minor term controlled by the genuine
row/column Plücker relations.

For context, the exact B07 predecessor `MOC4-MIXED-ASSIGNMENT-v1` is retained unchanged.
It proved the exterior-power expansion and the identity

\[
d_{\alpha\beta}=q_{S_\alpha,T_\beta}-q_{S_\alpha,T_\beta^c}
=\frac14h_\alpha^TP h_\beta,
\qquad P=(|u_{ij}|^2),
\]

so that the support functional is

\[
C_0+\langle P,C\rangle+\frac12\langle R,X\rangle
\]

and the full target is exactly the structured mixed assignment inequality over the same
unitary-derived `(P,R)`.  The present run attacks that remaining inequality rather than
re-deriving the already-settled expansion.

## 2. Compact conditional end-to-end argument

Fix a support direction `eta`.  The current proof route is:

1. By the account01/B07 exterior-minor identity, the support problem is exactly the mixed
   `(P,R)` inequality; no independent middle-layer orientation variable remains.
2. By account02/B08, repeated spectra and common reducing blocks are already safe, and an
   exact opposite scalar shift removes individual singularity.  Thus only the simple-spectrum,
   irreducible, individually-invertible core is essential.
3. Hadamard-transform the one-point coefficient and write the exact remaining support problem
   as account03/B20's
   \[
   A(U)+S(U)\ge\Delta. \tag{1}
   \]
4. In the unique parity-bad maximizing-assignment regime, the theorem below expresses `A+S`
   as the old coarse `kappa E` term plus **cellwise reduced-cost surplus** and then transfers
   that surplus through the true-unitary Plücker triangles.
5. Therefore the first unpaid implication is no longer merely “improve the `2 min(m,kappa)`
   floor.”  It is the explicit, source-valid inequality obtained in Corollary 3 below.  A
   target-level proof follows if that bound can be shown to dominate `Delta` on the remaining
   structured spectral coefficient locus; a counterexample must violate that explicit bound
   using an actual common unitary.

No arbitrary bistochastic `(P,R)` lift is assumed; that stronger route is already refuted by
account04/B09.

## 3. Exact scalar setup

Let `G,X in R^{3 x 3}` be the structured coefficient matrices in the scalar reduction and set

\[
K_{ij}=|G_{ij}|+\frac12X_{ij}.
\]

For `rho in S_3`, put

\[
K_\rho=\sum_iK_{i,\rho(i)},\qquad K_*=\max_\rho K_\rho.
\]

For the actual unitary-derived complementary-pair matrices `(R,D)`, write

\[
A(U)=K_*-\langle R,K\rangle,
\]

\[
S(U)=\sum_{i,j}|G_{ij}|\bigl(r_{ij}-\operatorname{sgn}(G_{ij})d_{ij}\bigr).
\]

As in account03/B20, define the parity correction

\[
\delta_\rho=
\begin{cases}
0,&\prod_iG_{i,\rho(i)}\ge0,\\
2\min_i|G_{i,\rho(i)}|,&\prod_iG_{i,\rho(i)}<0,
\end{cases}
\]

and

\[
\Delta=K_*-\max_\rho(K_\rho-\delta_\rho).
\]

Then (1) is exact.

Assume in this section that `rho_0` is the unique maximizer of `K_rho` and is parity-bad.
Relabel the three column classes so `rho_0=id`.  Put

\[
m=\min_i|G_{ii}|,
\qquad
q(\tau)=\#\{i:\tau(i)\ne i\}\in\{2,3\},
\]

\[
\kappa=\min_{\tau\ne id}\frac{K_*-K_\tau}{q(\tau)} >0. \tag{2}
\]

Finally set

\[
g_{ij}=|G_{ij}|,\qquad s_{ij}=\operatorname{sgn}(G_{ij}),
\]

choosing either sign when `G_ij=0`, and define the two orientation masses

\[
w_{ij}=\frac{r_{ij}-s_{ij}d_{ij}}2,\qquad
v_{ij}=\frac{r_{ij}+s_{ij}d_{ij}}2. \tag{3}
\]

The exact unitary inequality `|d_ij|<=r_ij` gives `w_ij,v_ij>=0`, while

\[
z_{ij}:=\sqrt{w_{ij}v_{ij}}
=\frac12\sqrt{r_{ij}^2-d_{ij}^2}. \tag{4}
\]

The B07 Plücker theorem says, in every row and every column, the three `z` values are side
lengths of a possibly degenerate triangle.

## 4. New lemma: a uniformly separated optimal assignment dual exists

### Lemma 1 — `KAPPA-DUAL`

There are real dual potentials `alpha_i,beta_j` such that

\[
\alpha_i+\beta_i=K_{ii},\tag{5}
\]

and, for every `i != j`,

\[
\ell_{ij}:=\alpha_i+\beta_j-K_{ij}\ge\kappa,\qquad \ell_{ii}=0. \tag{6}
\]

### Proof

Eliminate `beta_j` from (5): `beta_j=K_jj-alpha_j`.  The desired inequalities are

\[
\alpha_i-\alpha_j\ge
\kappa+K_{ij}-K_{jj}\qquad(i\ne j). \tag{7}
\]

This is a system of difference constraints on three vertices.  It is feasible iff every
directed cycle has nonpositive total required increment.  The only simple directed cycles
have length two or three.

For a two-cycle `i->j->i`, summing the right sides of (7) gives

\[
2\kappa-igl(K_*-K_{(ij)}\bigr)\le0
\]

by the definition (2).  For a directed three-cycle `tau`, the sum is

\[
3\kappa-(K_*-K_\tau)\le0,
\]

again by (2).  Every longer closed walk decomposes into these simple cycles.  Hence the
system is feasible.  With `beta_j=K_jj-alpha_j`, (5)--(6) follow.  QED.

This is stronger than using only a Birkhoff decomposition: it assigns the *excess over the
coarse normalized gap* to individual off-diagonal cells.

Write

\[
\varepsilon_{ij}=\ell_{ij}-\kappa\ge0\quad(i\ne j). \tag{8}
\]

## 5. New theorem: cellwise dual-surplus floor

Let

\[
E=\sum_i(1-r_{ii})=\sum_{i\ne j}r_{ij}. \tag{9}
\]

### Theorem 2 — `MOC4-DUAL-SURPLUS-FLOOR`

For every unitary `U`,

\[
\boxed{
A(U)+S(U)
\ge
\kappa E
+2\sum_i g_{ii}w_{ii}
+2\sum_{i\ne j}c_{ij}z_{ij},}
\tag{10}
\]

where

\[
\boxed{c_{ij}=\sqrt{\varepsilon_{ij}(\varepsilon_{ij}+2g_{ij})}.}\tag{11}
\]

### Proof

Because `R` is doubly stochastic and `(alpha,beta)` is an optimal assignment dual,

\[
\begin{aligned}
A(U)
&=K_*-\langle R,K\rangle\\
&=\sum_{ij}(\alpha_i+\beta_j-K_{ij})r_{ij}\\
&=\sum_{i\ne j}\ell_{ij}r_{ij}\\
&=\kappa E+\sum_{i\ne j}\varepsilon_{ij}r_{ij}. \tag{12}
\end{aligned}
\]

Also, by (3),

\[
S(U)=2\sum_{ij}g_{ij}w_{ij}. \tag{13}
\]

For one off-diagonal cell,

\[
\varepsilon r+2gw
=\varepsilon v+(\varepsilon+2g)w
\ge2\sqrt{\varepsilon(\varepsilon+2g)}\sqrt{wv} \tag{14}
\]

by AM-GM.  Sum (14) over all off-diagonal cells and retain the diagonal part of (13).  This
is exactly (10).  QED.

The inequality is strict whenever some cell has `epsilon_ij>0`, both complementary minors in
that cell are nonzero (`z_ij>0`), and AM-GM is not at equality.  Thus the exact common-unitary
minor geometry produces a payment that the coarse `kappa E` bound cannot see.

## 6. Plücker transfer onto the bad assignment cells

For each row `i`, the three numbers `z_i1,z_i2,z_i3` satisfy the triangle inequalities, hence

\[
z_{ii}\le\sum_{j\ne i}z_{ij}. \tag{15}
\]

Define

\[
\lambda_i^{\rm row}=\min_{j\ne i}c_{ij}. \tag{16}
\]

Similarly, from the column Plücker triangle, define

\[
\lambda_j^{\rm col}=\min_{i\ne j}c_{ij}. \tag{17}
\]

### Corollary 3 — `MOC4-DUAL-PLUCKER-FLOOR-v1`

Every unitary satisfies both

\[
\boxed{
A+S\ge
\kappa E+2\sum_i\left(g_{ii}w_{ii}
+\lambda_i^{\rm row}\sqrt{w_{ii}v_{ii}}\right),}
\tag{18}
\]

and

\[
\boxed{
A+S\ge
\kappa E+2\sum_j\left(g_{jj}w_{jj}
+\lambda_j^{\rm col}\sqrt{w_{jj}v_{jj}}\right).}
\tag{19}
\]

The two lower bounds may be maximized, but not added, because they use the same off-diagonal
surplus terms.

### Recovery of the previous two-slack theorem

Let `s_i=sgn(G_ii)`.  Since the maximizing assignment is parity-bad,
`prod_i s_i=-1`.  The exact Hadamard-block identity `D=(HPH^T)_{1^perp}` implies the odd
parity tetrahedral inequality

\[
\sum_i s_i d_{ii}\le1. \tag{20}
\]

Using `s_i d_ii=r_ii-2w_ii` and `sum_i r_ii=3-E`, (20) becomes

\[
\sum_iw_{ii}\ge1-\frac E2. \tag{21}
\]

Dropping all `lambda` terms in (18), replacing every `g_ii` by `m`, and using (21) gives

\[
A+S\ge\kappa E+m(2-E)_+, \tag{22}
\]

which minimizes to `2 min(m,kappa)`, exactly the account03/B20 r11b theorem.  Thus (10),
(18), and (19) are genuine refinements of the peer result rather than an alternative notation
for it.

### Equality rigidity

The derivation also records what a near-extremizer must do.  Equality in the old floor forces,
simultaneously:

- assignment mass to use only zero-surplus reduced-cost cells;
- off-diagonal wrong-orientation mass to vanish wherever `g_ij>0`;
- diagonal wrong-orientation mass to sit only on cells with `g_ii=m`;
- the odd-parity inequality (20) to be tight;
- and every positive `epsilon_ij` / nonzero-minor cell to lose its new correction.

On the generic strict-compound locus of account04/B08, every `z_ij>0`; hence any positive
dual surplus produces a strict new payment.  A genuine counterexample must therefore arrange
that this payment is quantitatively too small, not merely satisfy the old scalar floor.

## 7. Exact structured stress point: the old floor is genuinely insufficient

It is important not to mistake the previous `2 min(m,kappa)` theorem for a coefficient-only
closure.  Here is an exact structured spectral direction where it misses the required deficit.
Take

\[
a=(i,-1+2i,-2+2i,2i),
\]

\[
b=(-1-2i,2+2i,-1,-2+2i),
\qquad \eta=i.
\]

The exact coefficient construction gives

\[
G=\begin{pmatrix}
7&59/2&21\\
-7&16&3\\
21&43&39
\end{pmatrix},
\qquad
X=\begin{pmatrix}
-28&-23&20\\
-32&-16&16\\
-8&-34&24
\end{pmatrix}. \tag{23}
\]

For the six pair-class permutations in lexicographic order,

\[
(K_\rho)=(52,30,60,46,48,56), \tag{24}
\]

and the parity penalties are

\[
(\delta_\rho)=(0,0,14,0,14,0). \tag{25}
\]

Thus the unique maximizing assignment is

\[
\rho_0=(2,1,3)\quad\text{(one-based)},
\]

it is parity-bad, and

\[
m=7,\qquad \kappa=\frac43,\qquad \Delta=4. \tag{26}
\]

The normalized-gap minimizer is the parity-good three-cycle `(3,2,1)` with `q=3`.  Hence

\[
2\min(m,\kappa)=\frac83<4=\Delta. \tag{27}
\]

So the old floor alone cannot settle this perfectly legitimate simple-spectrum structured
support direction.  This is not a MOC4 counterexample; it is a source-valid stress point for
the remaining proof mechanism.

After relabeling `rho_0` to the identity, an exact `KAPPA-DUAL` certificate is

\[
(\ell_{ij})=
\begin{pmatrix}
0&20/3&4/3\\
4/3&0&38/3\\
32/3&4/3&0
\end{pmatrix}. \tag{28}
\]

Thus the positive reduced-cost surpluses occur exactly on the reverse three-cycle:

\[
\varepsilon_{12}=16/3,\qquad
\varepsilon_{23}=34/3,\qquad
\varepsilon_{31}=28/3, \tag{29}
\]

with the other three off-diagonal surpluses zero.  The corresponding exact Plücker-transfer
coefficients satisfy

\[
c_{12}^2=928/9,\qquad
c_{23}^2=1768/9,\qquad
c_{31}^2=8008/9. \tag{30}
\]

Therefore any actual unitary that could violate this support direction must make the explicit
right side of (10) smaller than `4`, despite these three positive reverse-cycle minor
penalties and the row/column Plücker triangles.  This is a substantially narrower geometric
obligation than the former statement `A+S>=Delta` with only the `8/3` coarse floor visible.

The exact standard-library `Fraction` verifier reconstructs `(G,X)`, all six assignment and
parity values, the exact dual, and the squared coefficients (30).  It returns `PASS`.

## 8. What is still missing

`MOC4-DUAL-PLUCKER-FLOOR-v1` does **not** yet prove the full target.  The first essential
remaining implication is now the following explicit statement:

> For every structured simple-spectrum support pair `(G,X)` and every true-unitary `(R,D)`
> in the residual regimes not already covered by account03/B20, the dual-surplus / Plücker
> lower bound (10), or one of its row/column transfers (18)--(19), is at least `Delta`.

The theorem proved here shows exactly where an attempted violation must hide: along
zero-surplus assignment directions while simultaneously suppressing the complementary-minor
products that Plücker transfers back to the bad diagonal cells.  This matches the current
SO(6)/Weyl picture from account04/B07: the issue is synchronization of the same orthogonal
transformation across the assignment and orientation sectors, not an arbitrary bistochastic
coupling.

A useful next derivation is therefore to classify the zero-surplus directed graph of an
optimal `KAPPA-DUAL`.  In `3 x 3` it is only a union of normalized-gap-minimizing
transpositions/three-cycles.  The exact Plücker triangles should then be imposed cycle by
cycle, rather than collapsed to the row minimum `lambda_i`.  The stress point (23)--(30),
whose zero-surplus graph is one directed three-cycle, is a small exact test case for that
classification.

## 9. Verification and provenance

Exact verifier:
`proofnet24/collective-MOC4/account01/B07/20260922T010146Z-b07-moc4-r11/verify_dual_plucker_floor.py`  
Verifier blob: `16c62afb2ee971e5bc7692133ca9904e00339af5`  
Verifier creation commit: `21358f5f9d09774bf11b30e21f1ad3d4a5a87699`.

Exact output:
`proofnet24/collective-MOC4/account01/B07/20260922T010146Z-b07-moc4-r11/VERIFICATION.txt`  
Output blob: `877590d06d0338a544e706fe43946a62377ef744`  
Output creation commit: `ea0474fc0536eaec11e8233d394e051f4e188fe5`.

No benchmark material, held-out answers, keys, credentials, scheduler identifiers, machine
paths, unrelated private material, email, Drive, paid model/API, remote workflow, permission
change, or public posting was used.  This report is a private campaign artifact and makes no
claim that the unrestricted Marcus–de Oliveira conjecture is solved.
