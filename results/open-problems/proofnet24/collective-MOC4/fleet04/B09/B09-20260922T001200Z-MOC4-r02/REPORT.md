# MOC4 fleet04/B09 r02 — coarsened `(P,R)` lift obstruction and structured-coefficient discriminant

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex normal 4-by-4 Marcus–de Oliveira target  
**Worker:** fleet04/B09  
**Outcome:** `CANDIDATE_REFUTED + AUXILIARY_EXACT_STRUCTURE`. The tempting next proof mechanism “the exact B07 variables `(P,R)` always have one common permutation lift” is false. A second exact calculation identifies a Vandermonde/Bezout-type algebraic restriction on the *structured* support coefficients that survives this no-go. The MOC4 target itself remains open.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and exact peer state consumed

The active target is: for all complex normal 4-by-4 matrices `A,B`, with spectra `a_1,...,a_4` and `b_1,...,b_4`, prove

\[
\det(A+B)\in\operatorname{conv}\left\{\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\}.
\]

This run consumes the exact completed fleet01/B07 result `MOC4-MIXED-ASSIGNMENT-v1` (scientific commit `d97eb4e3ad5b467c9494293292e5a78256599c53`). That result starts with

\[
A=\operatorname{diag}(a_1,\dots,a_4),\qquad
B=U\operatorname{diag}(b_1,\dots,b_4)U^*,
\]

puts

\[
p_{ij}=|u_{ij}|^2,
\qquad q_{S,T}=|\det U[S,T]|^2,
\]

and uses the three oriented complementary pairs

\[
S_1=T_1=12,\quad S_2=T_2=13,\quad S_3=T_3=14.
\]

It defines

\[
r_{\alpha\beta}=q_{S_\alpha,T_\beta}+q_{S_\alpha,T_\beta^c},
\qquad
 d_{\alpha\beta}=q_{S_\alpha,T_\beta}-q_{S_\alpha,T_\beta^c},
\]

with `P=(p_ij)` doubly stochastic and `R=(r_{alpha beta})` doubly stochastic, and proves the exact identity

\[
\boxed{d_{\alpha\beta}
=\sum_{i\in S_\alpha,\,j\in T_\beta}p_{ij}-1.}
\tag{1}
\]

Equivalently, `D=(d_{alpha beta})` is the mean-zero Hadamard block of `P`. The full support problem is then reduced exactly to a mixed assignment inequality involving only `(P,R)` and coefficient arrays structured by the spectra and support direction. This run attacks the most obvious remaining unitary-orbit shortcut: perhaps the coarsened pair `(P,R)` itself always admits a common classical permutation coupling.

I also use my earlier exact fleet04/B09 obstruction `MOC4-U-LIFT-v1` (scientific commit `ee33c17ceed673859063d8e53d0ecd9b05fd9fa5`) and the fleet04/B08 generic strict-support reduction (`MOC4-GENERIC-STRICT-SUPPORT-v1`, scientific commit `61aba8fc1d9eb46d6ae05b3f61a2706aad194a7f`). No benchmark material or answer key is used.

## 2. The coarsened joint-lift candidate

For each permutation `sigma in S_4`, let `P_sigma` be its 4-by-4 permutation matrix and let `R_sigma` be the 3-by-3 permutation matrix induced by the action of `sigma` on the three complementary pair classes

\[
\{12,34\},\quad\{13,24\},\quad\{14,23\}.
\]

A very attractive strengthening of the B07 reduction would be

> **`MOC4-PR-JOINT-LIFT-v1`.** For every `U in U(4)`, the unitary-derived pair `(P,R)` belongs to
> \[
> \operatorname{conv}\{(P_\sigma,R_\sigma):\sigma\in S_4\}.
> \]

If true, every linear mixed assignment inequality in `(P,R)` would follow immediately, so in particular the B07 support inequality would hold for *all* coefficient arrays, not merely the structured arrays coming from spectra.

This candidate is false.

## 3. Exact pure-`(P,R)` separating inequality

For any probability law on `S_4`, my previous run proved the pointwise inequality

\[
P_{12}+P_{24}-Q_{\{1,3\},\{2,3\}}
+Q_{\{1,4\},\{3,4\}}\ge0.
\tag{2}
\]

Use the B07 identity (1) to eliminate the two `Q` terms. Because `23=T_3^c` and `34=T_1^c`,

\[
Q_{\{1,3\},\{2,3\}}=\frac{R_{23}-d_{23}}2,
\qquad
Q_{\{1,4\},\{3,4\}}=\frac{R_{31}-d_{31}}2.
\]

Moreover

\[
d_{23}=P_{11}+P_{14}+P_{31}+P_{34}-1,
\]

\[
d_{31}=P_{11}+P_{12}+P_{41}+P_{42}-1.
\]

Thus twice (2) is the following inequality involving **only** the exact B07 variables `P` and `R`:

\[
\boxed{
P_{12}+P_{14}+2P_{24}+P_{31}+P_{34}-P_{41}-P_{42}
-R_{23}+R_{31}\ge0.}
\tag{3}
\]

Since (2) is pointwise on every permutation, (3) is also pointwise on all 24 coupled vertices `(P_sigma,R_sigma)`, hence on their convex hull. The companion verifier independently enumerates all 24 permutations; the left side of (3) is always `0`, `2`, or `4`.

Now take the exact rational orthogonal matrix from `MOC4-U-LIFT-v1`,

\[
U=\begin{pmatrix}
 492/625&-31/625&-48/125&12/25\\
 -9/25&12/25&-4/5&0\\
 -36/125&48/125&9/25&4/5\\
 -256/625&-492/625&-36/125&9/25
\end{pmatrix}.
\tag{4}
\]

Construct `P` and `R` from this `U` exactly. Direct `Fraction` arithmetic gives for the left side of (3)

\[
\boxed{-\frac{448}{15625}<0.}
\tag{5}
\]

Therefore

\[
(P,R)\notin\operatorname{conv}\{(P_\sigma,R_\sigma):\sigma\in S_4\}.
\]

So the B07 reduction cannot be finished by proving an unrestricted common permutation lift even after all signed orientation data have been absorbed into `P`. This is a strictly coarser no-go than demanding a lift of the complete 2-subset table `Q`: the obstruction survives after `Q` is compressed to the 3-by-3 complement-pair transport `R`.

**This is not a counterexample to MOC4.** B07 requires the mixed inequality only for coefficient arrays generated by `(a,b,eta)`, and those arrays occupy a proper algebraic subset of all linear functionals on `(P,R)`.

## 4. Exact algebraic restriction on the surviving structured coefficients

The no-go above makes the coefficient structure essential rather than optional. Here is an exact form of that structure before taking a support-direction real part.

Put

\[
A_\alpha^-=a_{S_\alpha^c}-a_{S_\alpha},
\qquad
B_\beta^-=b_{T_\beta^c}-b_{T_\beta},
\]

and define

\[
u_i=\sum_{\alpha:\,i\in S_\alpha}A_\alpha^-,
\qquad
v_j=\sum_{\beta:\,j\in T_\beta}B_\beta^-.
\]

After substituting (1) in the exact exterior-power expansion, one convenient doubly-stochastic gauge for the complex coefficient of `P` is

\[
G_{ij}=a_{i^c}b_j+a_i b_{j^c}+\frac12u_i v_j.
\tag{6}
\]

(The associated change in the constant term is `-\tfrac12(\sum A^-)(\sum B^-)`; row/column gauge changes do not affect the mixed assignment comparison.) Define the gauge-invariant 3-by-3 reduced matrix

\[
\widetilde G_{ij}=G_{ij}-G_{i4}-G_{4j}+G_{44},
\qquad 1\le i,j\le3.
\tag{7}
\]

For `i,j in {1,2,3}`, let `{r,s}={1,2,3}\setminus\{i\}` and `{t,u}={1,2,3}\setminus\{j\}`. Direct simplification of (6) gives

\[
\boxed{
\widetilde G_{ij}
=-\frac12(a_i-a_4)(b_j-b_4)
\left[2a_ra_s-(a_r+a_s)(b_t+b_u)+2b_tb_u\right].}
\tag{8}
\]

This formula immediately shows that `det(\widetilde G)` vanishes whenever any two `a`'s coincide or any two `b`'s coincide: if one of the first three equals the fourth, a row/column vanishes; if two of the first three coincide, the corresponding two rows/columns coincide. Every entry has total degree four, so `det(\widetilde G)` has total degree twelve. Hence it is divisible by the two degree-six Vandermonde products and the quotient is a constant. Evaluating, for example, at

\[
a=(0,1,2,3),\qquad b=(4,5,6,7)
\]

gives `det(\widetilde G)=-72`, while both Vandermonde products are `12`. Therefore

\[
\boxed{
\det\widetilde G
=-\frac12
\prod_{1\le i<j\le4}(a_i-a_j)
\prod_{1\le i<j\le4}(b_i-b_j).}
\tag{9}
\]

Thus on the simple-spectrum locus isolated by fleet04/B08, the *complex* reduced `P` coefficient is automatically invertible. The repeated-spectrum theorem of fleet02/B08 lies exactly on the algebraic discriminant where (9) vanishes.

There is also an explicit inverse formula. When both spectra are simple, for `i,j in {1,2,3}`,

\[
\boxed{
(\widetilde G^{-1})_{ji}
=-\frac{(a_i-b_j)^2}
{\left(\prod_{k\ne i}(a_i-a_k)\right)
 \left(\prod_{\ell\ne j}(b_j-b_\ell)\right)}.}
\tag{10}
\]

One proof is to compute the `(i,j)` cofactor from (8):

\[
\operatorname{cof}_{ij}(\widetilde G)
=\frac{(-1)^{i+j}}2(a_i-b_j)^2
\Delta(a_{\widehat i})\Delta(b_{\widehat j}),
\]

and divide by (9). Equation (10) exhibits a Cauchy/Bezout-type restriction on the coefficient matrix. An arbitrary separating normal for the false `(P,R)` joint polytope need not satisfy this restriction.

## 5. What the remaining unitary-orbit step now really is

The following route is now rigorously ruled out:

1. reduce MOC4 to the B07 mixed `(P,R)` inequality;
2. forget the spectral structure of the coefficients;
3. prove `(P,R)` lies in the convex hull of the 24 coupled permutation pairs.

Step 3 is false by (3)–(5).

The surviving obligation is genuinely more specific:

> **`MOC4-MIXED-ASSIGNMENT-STRUCTURED-v2`.** Prove the B07 mixed assignment inequality only for support normals generated by complex spectra and a support direction, using the exact unitary constraints on `(P,R)` *together with* the coefficient identities such as (8)–(10).

This is consistent with the fleet04/B08 generic-strict-support reduction: any genuine failure can be assumed to have simple nonzero spectra and strict compound inequalities, so (9) allows the generic problem to be studied with an invertible complex coefficient gauge. Conversely, the repeated-spectrum boundary remains covered by fleet02/B08 and should not be re-proved through a singular limiting inversion.

A concrete next step is to combine the B07 constraints

\[
|d_{\alpha\beta}|<r_{\alpha\beta}<\frac{1+d_{\alpha\beta}^2}{2}
\]

and the row/column Plücker triangle inequalities with the structured-normal identities (8)–(10), rather than with arbitrary `(C,X)` facets. A counterexample to another unrestricted joint-transport statement would no longer advance the target unless its separating normal can be realized by actual spectra/support data.

## 6. Verification and status

`verify_pr_coarsening.py` uses only Python standard-library exact `Fraction` arithmetic. It checks:

- exact orthogonality of (4);
- the mixed-minor difference identity used in the elimination;
- inequality (3) on all 24 permutation vertices;
- the exact violation `-448/15625` for the unitary-derived `(P,R)`;
- the determinant identity (9) and inverse formula (10) on several exact rational/simple-spectrum test tuples.

The finite checks support the algebra; the proof of (3) and the polynomial proof of (9) are given above and do not depend on floating-point optimization.

**Parent target status:** open; neither proved nor disproved here.  
**New candidate status:** `MOC4-PR-JOINT-LIFT-v1 = REFUTED`.  
**New structural lemma:** equations (8)–(10), exact.  
**Recommended recipients:** fleet03/B07 lead, fleet01/B07 mixed-assignment worker, fleet04/B08 generic-boundary worker, fleet03/B20 integrator.
