# MOC4 fleet02/B07 — exact generic true-unitary refutation of `MOC4-PARITY-SLACK-v1`

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex normal 4-by-4 Marcus–de Oliveira target  
**Worker:** fleet02/B07  
**Run:** `20260922T013439Z-b07-moc4-r11a`  
**Outcome:** `CANDIDATE_REFUTED` for the lead's sufficient intermediate `MOC4-PARITY-SLACK-v1`; the parent MOC4 statement remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Source-exact target and current proof state consumed

The target is: for every complex normal 4-by-4 pair `A,B`, with spectra `a_1,...,a_4` and `b_1,...,b_4`, prove

\[
\det(A+B)\in\operatorname{conv}\left\{\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\}.
\]

This run read the current team lead fleet03/B07 complete r12 report, candidate `MOC4-PARITY-SLACK-v1`. It also directly consumed the named partner fleet03/B08 `MOC4-PERMUTATION-TANGENT-v1`, fleet01/B07 `MOC4-MIXED-ASSIGNMENT-v1`, and fleet04/B09's exact no-go for an unrestricted common `(P,R)` lift.

The lead's exact standard-representation reduction is as follows. For a true unitary `U`, let `P=(|u_ij|^2)`, let `D` be the 3-by-3 mean-zero Hadamard block of `P`, and let `R` be the 3-by-3 complementary-pair transport. For the structured real support coefficient block `K` and middle-layer block `X`, the full support inequality is exactly

\[
\langle D,K\rangle+\frac12\langle R,X\rangle
\le \max_{\sigma\in S_4}\left\{
\langle S_\sigma,K\rangle+\frac12\langle |S_\sigma|,X\rangle
\right\}. \tag{SR}
\]

The six `S_3` fibers have costs

\[
F_\rho(K)=\max_{\epsilon_1\epsilon_2\epsilon_3=1}
\sum_i\epsilon_i K_{i,\rho(i)}.
\]

For a Birkhoff decomposition `R=sum lambda_rho R_rho`, put

\[
m_\rho(K)=0
\quad\hbox{if }\prod_iK_{i,\rho(i)}\ge0,
\]

and otherwise `m_rho(K)=min_i |K_{i,rho(i)}|`. The lead isolated the sufficient condition

\[
2\sum_\rho\lambda_\rho m_\rho(K)
\le
\sum_{ij}\bigl(R_{ij}|K_{ij}|-D_{ij}K_{ij}\bigr). \tag{PS}
\]

The proposed implication `MOC4-PARITY-SLACK-v1` asserted existence of such a decomposition for every generic strict-support MOC4 datum. The exact construction below refutes that implication while preserving the actual true-unitary model and the structured spectral origin of `K`.

## 2. Construction: perturb the exact coupled-lift separator into the generic unitary locus

Start from the exact rational orthogonal matrix used in fleet04/B09's coupled `(P,R)` no-go:

\[
U_0=\begin{pmatrix}
492/625&-31/625&-48/125&12/25\\
-9/25&12/25&-4/5&0\\
-36/125&48/125&9/25&4/5\\
-256/625&-492/625&-36/125&9/25
\end{pmatrix}.
\]

Its separator is a boundary example because one entry is zero. Apply the exact rational rotation in the first two rows with parameter `t=1/1000`,

\[
c=\frac{1-t^2}{1+t^2}=\frac{999999}{1000001},\qquad
s=\frac{2t}{1+t^2}=\frac{2000}{1000001},
\]

and

\[
Q=\begin{pmatrix}c&-s&0&0\\s&c&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},
\qquad U=Q U_0.
\]

Then `U` is exactly real orthogonal, hence a true unitary. Exact Fraction arithmetic verifies:

- every entry of `U` is nonzero;
- every 2-by-2 minor of `U` is nonzero;
- every tested 2-by-2 compression discriminant used in the named partner's genericity check is nonzero.

Thus the old separator is not merely being used at its zero-entry boundary; its obstruction survives an explicit true-unitary perturbation into the strict compound-minor locus.

## 3. Structured spectral normal, not an arbitrary 3-by-3 test matrix

Use the following exact Gaussian-rational simple spectra and nonzero support normal:

\[
\begin{aligned}
a={}&(1.592617+1.165031i,\;-0.401554-0.577389i,\\
&\qquad 1.144510-0.779167i,\;-0.717378-1.054671i),\\
b={}&(0.961905+0.657334i,\;0.652386+0.406944i,\\
&\qquad -0.796717+0.234805i,\;-0.730534-0.372247i),\\
\eta={}&248743/250000+(2003/20000)i.
\end{aligned}
\]

Every displayed decimal is exactly the corresponding integer divided by `10^6`. The verifier reconstructs `K` from the **actual fleet01/B07 support formulas**: `W`, the signed middle-layer contribution `Y`, the induced `Z`, `C=W+Z`, and finally the lower-right Hadamard block of `H C H^T`. No arbitrary bistochastic or arbitrary `K` surrogate is inserted.

The resulting exact structured block is numerically

\[
K\approx\begin{pmatrix}
2.7771486352\!\times10^{-6}&0.999999973734&5.8791079741\!\times10^{-7}\\
-0.999999768046&-1.5975435943\!\times10^{-6}&4.8719530812\!\times10^{-7}\\
2.3598469284\!\times10^{-7}&1.9342359523\!\times10^{-7}&0.999999902414
\end{pmatrix}.
\]

It is a rationally certified structured perturbation of the signed separator direction, not a postulated coefficient array.

## 4. Exact failure of every Birkhoff choice in `(PS)`

Order the six permutations of `S_3` lexicographically. For this exact `R`, every Birkhoff decomposition is the one-parameter family

\[
\lambda(\tau)=\lambda^{(0)}+\tau(-1,1,1,-1,-1,1),
\]

where

\[
\lambda^{(0)}=\left(
\frac{31495970140431264}{390625781250390625},
\frac{76729246309676961}{390625781250390625},
\frac{90656333152091136}{390625781250390625},
\frac{256768270592256}{625001250000625},
\frac{31264}{390625},0\right).
\]

The verifier checks that the 9-by-6 permutation-incidence matrix has rank five, so this is the complete affine solution family. Nonnegativity forces `tau>=0` because the sixth weight is `tau`. The exact slope of the parity-penalty objective is

\[
\frac{31249944158225517901963516829}
{31250000000000000000000000000}>0,
\]

so its minimum over **all** Birkhoff decompositions is attained at `tau=0`.

At that minimum,

\[
\sum_\rho\lambda_\rho m_\rho(K)
=
\frac{283301151522996118193100170881025531966840283}
{1220705566407470703125000000000000000000000000},
\]

whereas the exact orientation slack is

\[
\sum_{ij}(R_{ij}|K_{ij}|-D_{ij}K_{ij})
=
\frac{42595712914330631701635472543756766978812179687}
{97656445312597656250000000000000000000000000000}.
\]

Therefore

\[
\boxed{
\text{slack}-2\min_\lambda\sum_\rho\lambda_\rho m_\rho(K)
=
-\frac{2732471329348747209260554797207318135882265593}
{97656445312597656250000000000000000000000000000}<0.}
\]

Numerically the failure margin is about `-0.027980450451602287`. Hence **no Birkhoff decomposition of this true-unitary `R` can satisfy `(PS)`**. This is an exact refutation of `MOC4-PARITY-SLACK-v1` as stated on the generic structured locus.

## 5. Strict-support and source-validity checks; this is not an MOC4 counterexample

The same exact certificate verifies:

- both spectra are simple and nonzero;
- all sixteen `a_i+b_j` are nonzero;
- all 24 permutation products are distinct;
- the support functional has a unique maximizing permutation `(1,3,4,2)` (one-based), with exact gap

\[
\frac{361590000477033578484063}{250000000000000000000000000000}>0;
\]

- with `B=U diag(b) U^*`, every off-diagonal entry of `B` is nonzero, so with simple diagonal `A` there is no coordinate common reducing split.

Most importantly, the actual determinant does **not** violate the target support inequality. Its support is below the unique permutation maximum by

\[
-\frac{97009029696651350211662895983891344033606244217}
{97656445312597656250000000000000000000000000000}
\approx -0.9933704773517618.
\]

Thus this construction refutes only the lead's sufficient parity-slack gate. It is not a counterexample to MOC4 and does not weaken the exact six-fiber inequality `(SR)`.

## 6. Application of the named partner result

The named partner fleet03/B08 `MOC4-PERMUTATION-TANGENT-v1` proves that at a uniquely exposed permutation vertex all nontrivial true-unitary two-plane tangent modes have strictly negative support Hessian, and therefore a generic MOC4 failure cannot be born as an infinitesimal perturbation of that vertex. I use that result here in two ways:

1. its exact strict-generic checklist is enforced on the constructed true unitary (nonzero entries/minors and nondegenerate two-plane compressions); and
2. the construction is deliberately a finite-distance datum whose determinant remains well inside the chosen support half-space, so the parity-slack failure is consistent with the partner's local-support theorem rather than contradicting it.

This sharpens the campaign logic: even on the source-valid generic locus, the scalar convex-roof shortcut `(PS)` can fail while the actual support inequality has large slack.

## 7. Conditional end-to-end argument after this refutation

The smallest surviving chain is now:

1. use the generic strict-support reduction to pass any target violation to simple spectra, irreducible/common-block-free data with a unique maximizing permutation vertex;
2. use fleet01/B07's exact exterior-power formula to reduce the support inequality to the actual-unitary mixed `(P,R)` inequality;
3. use the lead r12 standard representation to rewrite that inequality exactly as `(SR)` over six signed-permutation fibers;
4. **do not** replace `(SR)` by the now-refuted universal parity-slack gate `(PS)`;
5. at a hypothetical global support maximizer, apply fleet02/B07 `MOC4-BIRAYLEIGH-ORBIT-v1`: all twelve row/column true-unitary two-plane restrictions are top-eigenvector conditions, valid even at singular determinant points by adjugates;
6. prove the remaining exact six-fiber support bound under those twelve conditions, or obtain an equivalent exact proof of the lead's Drury upper-facet inequalities.

The first essential missing implication in this route is therefore the sharpened

> **`MOC4-SR-AT-BIRAYLEIGH-v2`.** For every generic strict-support datum `(a,b,eta)` and every `U in U(4)` that is simultaneously top-Rayleigh in all six column and six row two-plane restrictions for `h_eta(U)=Re(eta det(D_a+U D_b U*))`, prove the exact six-fiber inequality `(SR)`.

Unlike `(PS)`, this implication retains the full `X`-dependent fiber maximum and the second-variation information of an actual extremizer. A counterexample to it with support above all 24 vertices would be a genuine MOC4 counterexample; a datum merely failing `(PS)` is not.

## 8. Singular and repeated-spectrum cases

Nothing in the refutation removes the previous singular-safe second-variation formulas. The bi-Rayleigh pair restriction uses `adj(X)` rather than `X^{-1}` and hence is defined at singular determinant points. For target-level closure, a strict support violation persists under small perturbation; repeated spectra can be split, and a zero determinant can be perturbed by `A+tI`, for which the determinant is a degree-four polynomial in `t` and is nonzero away from finitely many small values. Thus the generic extremizer implication above would still transfer to the singular/repeated cases by contradiction and continuity.

## 9. Verification and limitations

`verify_parity_slack_refutation.py` is standard-library-only and uses `fractions.Fraction` throughout the certificate. `VERIFICATION.txt` records its exact output. The numerical solve used only to locate a candidate is not part of the proof: the committed rational data are independently rechecked exactly from scratch.

This report claims no worldwide novelty and no full MOC4 proof. It preserves complex phases, actual normal-matrix/unitary compatibility and the exact 24-vertex hull. No benchmark material, credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive, public posting, paid model/API calls, Codex, remote workflow, or permission bypass was used.
