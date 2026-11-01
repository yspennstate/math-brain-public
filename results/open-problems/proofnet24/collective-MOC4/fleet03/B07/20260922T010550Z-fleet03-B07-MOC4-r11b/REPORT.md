# MOC4 fleet03/B07 r11b — Drury-facet / determinantal-cylinder reduction

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex normal 4-by-4 Marcus–de Oliveira determinant hull  
**Worker:** fleet03/B07 lead  
**Candidate:** `MOC4-DRURY-UPPER-FACET-v1`  
**Outcome:** `ESSENTIAL_STEP_APPLIED` — the current continuous unitary support problem is reduced to a finite family of explicit purely spectral upper-facet inequalities from Drury's exact n=4 Saxl cone. The full MOC4 target remains **OPEN / NOT PROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Source-exact target and later owner control

The effective owner control is revision `2026-09-22.2`, which supersedes this slot's former benchmark assignment and assigns fleet03/B07 to lead MOC4. No new benchmark work is performed here; all old benchmark artifacts remain untouched.

For complex normal 4-by-4 matrices `A,B` with spectra `a_1,...,a_4` and `b_1,...,b_4`, the target is

\[
\det(A+B)\in\operatorname{conv}\left\{
 v_\sigma(a,b):=\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4
\right\}.
\]

Primary-source recovery in this run included:

- S. W. Drury, *The external vertices conjecture in case n=4*, Electronic Journal of Linear Algebra 11 (2004), 180–191, DOI `10.13001/1081-3810.1131`. The paper states that full n=4 Marcus–de Oliveira remains open, proves the n=4 External Vertices Conjecture, gives the exact determinant quasidistribution/cylinder identity used below, and computes the facet structure of the Saxl cone.
- N. Bebiano and J. P. da Providência, *Revisiting the Marcus–de Oliveira Conjecture*, Mathematics 13 (2025), 711, DOI `10.3390/math13050711`, which surveys the still-open conjecture.
- J. I. Mulero-Martínez, *A variational framework for determinantal inequalities of normal matrices: Successes and obstructions*, Linear Algebra and its Applications 740 (2026), 19–38, DOI `10.1016/j.laa.2026.03.019`, retained as the current variational-obstruction input rather than treated as a solution.

The assigned OTHER-account partner result consumed directly is **fleet04/B08 `MOC4-GENERIC-STRICT-SUPPORT-v1`**, scientific commit `61aba8fc1d9eb46d6ae05b3f61a2706aad194a7f`: every genuine counterexample can be perturbed to simple nonzero spectra, a unique exposed permutation vertex, nonzero 1x1/2x2 unitary minors, strict compound inequalities and no common reducing subspace. Hence it is legitimate to attack only the generic strict-support case and recover boundaries by continuity.

I also use the exact current campaign reductions from fleet01/B07 (`MOC4-MIXED-ASSIGNMENT-v1`) and fleet04/B09 (`MOC4-PR-JOINT-LIFT-v1 = REFUTED`). The latter is important because it forbids silently replacing the unitary problem by an unrestricted positive common `(P,R)` permutation lift.

## 2. Determinantal quasidistribution and cylinder marginals

Normalize the coupling unitary to `U in SU(4)`; scalar phase does not change `UD_bU*`. Define

\[
\mu_\sigma(U):=\operatorname{sgn}(\sigma)\prod_{i=1}^4u_{i,\sigma(i)}.
\tag{1}
\]

Then

\[
\sum_{\sigma\in S_4}\mu_\sigma=\det U=1.
\tag{2}
\]

For equal-cardinality subsets `I,J subset [4]`, let

\[
P_{IJ}(\sigma)=\mathbf 1\{\sigma(I)=J\}.
\]

The exact cylinder identity is

\[
\boxed{
\sum_{\sigma:\sigma(I)=J}\mu_\sigma(U)=|\det U[I,J]|^2\ge0.
}
\tag{3}
\]

For completeness, summing determinant monomials over permutations taking `I` onto `J` factors into the two complementary minors. Jacobi complementarity for an `SU(4)` unitary turns the complementary minor into the conjugate of the first with the same shuffle sign, giving the squared modulus. This is the identity used by Drury (via Merikoski–Virtanen); it is not claimed new here.

There is also the exact endpoint representation

\[
\boxed{
\det(D_a+UD_bU^*)=\sum_{\sigma\in S_4}\mu_\sigma(U)v_\sigma(a,b).
}
\tag{4}
\]

Indeed

\[
\sum_\sigma\operatorname{sgn}(\sigma)
\prod_i u_{i,\sigma(i)}(a_i+b_{\sigma(i)})
=\det(D_aU+UD_b)
=\det(D_a+UD_bU^*)
\]

because `det U=1`.

Thus `mu` is a signed/complex quasidistribution whose complete set-image cylinder marginals are genuine nonnegative squared minors.

## 3. Drury's exact n=4 Saxl cone

Let `Saxl_4` be the 14-dimensional real space spanned by all cylinder functions `P_{IJ}`. Drury's Proposition 4.1 considers

\[
\Gamma=\left\{f\in\mathrm{Saxl}_4:
 f=\sum_{|I|=|J|}t_{IJ}P_{IJ},\ t_{IJ}\ge0\right\}.
\tag{5}
\]

Its facets are exactly of two types:

1. coordinate facets `f(\sigma)\ge0`;
2. the left-right `S_4 x S_4` orbit of one exceptional linear functional `u`, normalized by `u(1)=1`.

One of Drury's ten equivalent formulas is

\[
3u(f)=
 f(2134)+f(3214)+f(1432)+f(4321)-f(1234).
\tag{6}
\]

The left-right action is `f_{\rho_1,\rho_2}(\sigma)=f(\rho_1\sigma\rho_2^{-1})`.

## 4. New finite reduction of the remaining support problem

Fix a unit support direction `eta` and define

\[
F(\sigma)=\Re\bigl(\eta v_\sigma(a,b)\bigr),
\qquad
M=\max_{\sigma\in S_4}F(\sigma),
\qquad
g(\sigma)=M-F(\sigma).
\tag{7}
\]

`F` and `g` lie in `Saxl_4`, and by definition

\[
g(\sigma)\ge0\quad\forall\sigma.
\tag{8}
\]

Therefore **all coordinate facets of `Gamma` are automatic**. Drury's facet theorem gives the exact equivalence

\[
\boxed{
g\in\Gamma
\iff
u(g_{\rho_1,\rho_2})\ge0
\text{ for every }\rho_1,\rho_2\in S_4,}
\tag{9}
\]

where `nu=u` is the single exceptional functional above. Since `u(1)=1`,

\[
u(g_{\rho_1,\rho_2})
=M-u(F_{\rho_1,\rho_2}).
\tag{10}
\]

Hence the entire sufficient cylinder-cone condition is reduced to the finite purely spectral family

\[
\boxed{
 u(F_{\rho_1,\rho_2})\le M
 \quad(\rho_1,\rho_2\in S_4).
}
\tag{UF}
\]

There are 576 ordered `(rho_1,rho_2)` pairs but only **288 distinct coefficient functionals** in this orbit (stabilizer size two); this finite orbit count is elementary and can be checked exactly.

### Why `(UF)` closes full MOC4

If `(UF)` holds, then `g in Gamma`, so write

\[
g=\sum_{I,J}t_{IJ}P_{IJ},\qquad t_{IJ}\ge0.
\tag{11}
\]

Using (2)–(4),

\[
\begin{aligned}
M-\Re\bigl(\eta\det(D_a+UD_bU^*)\bigr)
&=\Re\sum_\sigma\mu_\sigma g(\sigma)\\
&=\sum_{I,J}t_{IJ}
\sum_{\sigma:\sigma(I)=J}\mu_\sigma\\
&=\sum_{I,J}t_{IJ}|\det U[I,J]|^2\\
&\ge0.
\end{aligned}
\tag{12}
\]

This is exactly the support inequality. Since `eta` was arbitrary, proving `(UF)` for every complex spectra closes MOC4. No positive common permutation lift is asserted or needed.

Thus the first indispensable gap can be stated without any unitary variable:

> **`MOC4-DRURY-UPPER-FACET-v1`.** For every complex spectra `a,b`, every support direction `eta`, and every `rho_1,rho_2 in S_4`, if `M=max_sigma Re(eta v_sigma)`, then `u(F_{rho_1,rho_2})<=M`.

This is a finite spectral inequality, not merely another continuous reformulation: once it is proved, Drury's already-computed cone plus (3) makes every unitary automatic.

## 5. Relation to Drury's 2004 theorem: exact missing side

Drury proved the **lower** exceptional-facet estimate needed for the External Vertices Conjecture: after normalization `F(sigma)>=1` for all `sigma`, one has `u(F)>=1`. That proves determinant preservation of every half-space excluding the origin and yields his radial-hull Corollary 1.2.

The present target requires the complementary **upper** statement `(UF)` for a support maximum. It is not contained in Drury's theorem. When the relevant supporting half-space excludes the origin, the 2004 result already handles it; the unresolved regime is precisely the origin-containing support geometry for which a positive lower normalization is unavailable.

This identifies the historical gap sharply: the current fleet01 mixed `(P,R)` inequality, the fleet02 bi-Rayleigh rigidity condition, and `(UF)` are different encodings of the same remaining interior support obstruction, but `(UF)` removes `U` entirely and leaves a finite orbit of one explicit Saxl facet.

## 6. Exact obstruction to dropping the spectral structure

It would be false to strengthen the argument to “every nonnegative identity-vanishing Saxl function lies in the off-diagonal cylinder cone.” Consider

\[
s(\sigma)=
\mathbf1_{\sigma(1)=2}
+\mathbf1_{\sigma(2)=4}
-\mathbf1_{\sigma(\{1,3\})=\{2,3\}}
+\mathbf1_{\sigma(\{1,4\})=\{3,4\}}.
\tag{13}
\]

Exact enumeration gives values `0,1,2` with multiplicities `13,10,1`, so `s>=0`. The off-diagonal cylinder span has rank 13; restricting to the 13 zero coordinates of `s` has rank 12, so `s` is an extreme ray of the full nonnegative identity-vanishing Saxl cone.

For the exact rational orthogonal matrix already used by fleet04/B09,

\[
\sum_\sigma\mu_\sigma(U)s(\sigma)=-\frac{224}{15625}<0.
\tag{14}
\]

Since every nonnegative cylinder combination has nonnegative `mu` expectation by (3), `s` cannot lie in that cylinder cone. This recovers the peer's coarsened-lift obstruction in a particularly transparent form and proves that the structured OM-vertex geometry in `(UF)` is essential.

The attached standard-library exact verifier checks the 13-dimensional span rank, the rank-12 active-zero condition, all cylinder identities for that rational orthogonal matrix, `sum mu=1`, and (14).

## 7. Exploratory stress test, not proof

As a discovery check only, I generated 10,000 random complex spectral/support instances and evaluated all 288 distinct exceptional `u`-orbit inequalities. No `(UF)` violation was found. Separately, 3,000 random max-gap vectors were tested for nonnegative off-diagonal-cylinder feasibility and all were feasible. These computations are **not** a certificate and are not used as proof of `(UF)`; they only justify making the explicit upper-facet inequality the next attack rather than returning to the refuted unrestricted `(P,R)` lift.

## 8. Compact conditional end-to-end proof and next recipient

The smallest current conditional proof is now:

1. diagonalize `A,B` and normalize `U in SU(4)`;
2. for each support direction form the 24 real OM values `F(sigma)` and maximum `M`;
3. prove the 288-orbit spectral inequalities `(UF)`;
4. Drury Proposition 4.1 then gives `g=M-F in Gamma`;
5. expand `g` with nonnegative cylinder coefficients;
6. apply the exact cylinder identity (3) to obtain (12);
7. conclude every support inequality, hence the full 4-by-4 determinant hull; the partner generic reduction supplies a redundant continuity route for all degenerate boundaries.

The **first unpaid implication is step 3**. A productive next attack should use Drury's explicit ten forms of `u` and the factorization of vertex differences into OM roots/cross-ratio data, but with the sign orientation reversed from Proposition 4.2. It should not assume the false common `(P,R)` lift.

Recommended recipients: fleet04/B08 (assigned partner), fleet01/B07, fleet02/B07, fleet04/B09, and fleet03/B20.

No benchmark gold, held-out answers, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive, public posting, paid model/API/Codex execution, or remote workflow was used.
