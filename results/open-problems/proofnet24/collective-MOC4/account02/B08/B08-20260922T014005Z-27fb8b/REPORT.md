# MOC4 account02/B08 — minimal repeated-face lift and sharper safe collar

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex normal `4 x 4` Marcus–de Oliveira target  
**Worker:** account02/B08  
**Run:** `B08-20260922T014005Z-27fb8b`  
**Candidate:** `MOC4-REPEATED-MINIMAL-LIFT-v2`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact scope and inputs consumed

The source-exact target is: for every pair of complex normal `4 x 4` matrices `A,B`, with eigenvalues `a_1,...,a_4` and `b_1,...,b_4`, prove

\[
\det(A+B)\in\operatorname{conv}\left\{\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\}.
\]


This run read and applies:

1. **Campaign lead account03/B07 r12**, `MOC4-PARITY-SLACK-v1`, canonical report `proofnet24/collective-MOC4/account03/B07/20260922T012650Z-account03-B07-MOC4-r12/REPORT.md`, report blob `5e5e58b067d5e546e34a97119893ebe5a7198881`. It compresses the generic simple-spectrum mixed support problem to an exact six-fiber signed-permutation inequality and isolates the scalar parity-slack payment `(PS)` as the first sufficient generic gate.
2. **Named partner account03/B09 r11**, `MOC4 complementary-minor orientation rigidity and 6κ support certificate`, canonical run `proofnet24/collective-MOC4/account03/B09/20260922T011607Z-account03-B09-MOC4-r11/`. It keeps the complementary `2 x 2` minors as genuine `Lambda^2 U / SO(6)` invariants and proves a nonlinear synchronization constraint; no arbitrary bistochastic or common-lift surrogate is valid.
3. **This worker's preceding boundary result**, `MOC4-BOUNDARY-CORE-AND-COLLAR-v1`, run `B08-20260922T004041Z-moc4-r11`. It gave an exact opposite-scalar gauge reduction to the simple-spectrum, individually-invertible, irreducible core and a generic repeated-face collar under the stronger assumptions that all unitary entries and all six designated compound minors are nonzero.
4. The established `n<=3` Marcus–de Oliveira result, used only for the already-recorded common-reducing-block reduction. Drury's 2004 n=4 paper explicitly distinguishes the settled `3 x 3` case from the open `4 x 4` case and proves only a weakened n=4 result.

The new proof below materially strengthens item 3. It uses the partner's insistence on genuine common-unitary compound-minor data, but exploits the coefficient collision created by a repeated eigenvalue so that a much smaller marginal lift suffices. No `P,R` joint Birkhoff lift is assumed.

## 2. Compact conditional end-to-end route

The current all-pairs chain is:

1. Repeated-spectrum pairs are proved directly below; common-reducing-block pairs remain proved by factorization into dimensions at most three.
2. The exact gauge `(A,B)->(A+tI,B-tI)` from the preceding run leaves `A+B` and every one of the 24 comparison vertices unchanged and removes individual singularity. Thus only the simple-spectrum, individually-invertible, irreducible core remains for a global proof.
3. On that core, account03/B07 r12 reduces the generic support problem to the exact six-fiber standard-representation inequality and the structured parity-slack gate.
4. The new theorem below shows that a repeated-spectrum boundary point has an open MOC4-safe collar under strictly weaker conditions than previously known: zeros in the repeated rows and zero designated compound minors are allowed. Consequently a counterexample sequence approaching a repeated spectral discriminant must force either a zero in one of the two *nonrepeated* rows, or a collapse of the supported permutation vertices to a line.

Thus this run closes more of the boundary needed by the lead's generic simple-spectrum route. It does not prove the lead's parity-slack implication on the remaining core.

## 3. Exact determinant expansion

Diagonalize `A` and write

\[
A=\operatorname{diag}(a_1,a_2,a_3,a_4),\qquad
B=U\operatorname{diag}(b_1,b_2,b_3,b_4)U^*.
\]

For row and column sets `I,J` of the same size put

\[
Q_{I,J}=|\det U[I,J]|^2,
\qquad a_{I^c}=\prod_{i\notin I}a_i,
\qquad b_J=\prod_{j\in J}b_j.
\]

Expansion by principal minors followed by Cauchy–Binet gives the exact identity

\[
\boxed{
\det(A+B)=\sum_{I,J:\,|I|=|J|} a_{I^c}b_J Q_{I,J}.
}\tag{1}
\]

For a permutation `sigma`,

\[
v_\sigma:=\prod_i(a_i+b_{\sigma(i)})
=\sum_{I\subset[4]}a_{I^c}b_{\sigma(I)}.
\tag{2}
\]

Hence a probability law `mu` on `S_4` represents the determinant if, after grouping row sets having equal coefficients `a_{I^c}`, its image-set probabilities reproduce the corresponding grouped `Q` coefficients.

## 4. A weighted orientation lemma from the actual unitary

Assume after relabeling that

\[
a_1=a_2=\alpha.
\tag{3}
\]

Define the designated top-pair law and its Jacobi-complement bottom-pair law by

\[
q_J:=Q_{\{1,2\},J},\qquad
r_K:=Q_{\{3,4\},K}=q_{K^c},\qquad |J|=|K|=2.
\tag{4}
\]

The equality in (4) is Jacobi's complementary-minor identity for a unitary matrix. Also put

\[
p_j:=|u_{3j}|^2.
\tag{5}
\]

View `r_{jk}` as edge weights of a weighted graph on the four column labels. Cauchy–Binet gives

\[
\sum_{j<k}r_{jk}=1,
\qquad
\sum_{k\ne j}r_{jk}=|u_{3j}|^2+|u_{4j}|^2.
\tag{6}
\]

### Lemma 1 — bottom-pair fractional orientation

There exist nonnegative numbers `z_{j->k}` for ordered distinct columns such that

\[
z_{j\to k}+z_{k\to j}=r_{jk},
\qquad
\sum_{k\ne j}z_{j\to k}=|u_{3j}|^2.
\tag{7}
\]

#### Proof

A weighted edge can be split between its two endpoints with prescribed endpoint totals `p_j` iff the standard max-flow/Hall inequalities

\[
r(E(S))\le p(S):=\sum_{j\in S}p_j
\tag{8}
\]

hold for every `S subset [4]`, together with equality of total masses. The totals are both one. It remains to verify (8) from the actual unitary.

For `|S|=1`, the left side is zero. For `S={j,k}`, the squared determinant bound gives

\[
r_{jk}
=|u_{3j}u_{4k}-u_{3k}u_{4j}|^2
\le (|u_{3j}|^2+|u_{3k}|^2)(|u_{4j}|^2+|u_{4k}|^2)
\le p_j+p_k.
\tag{9}
\]

For `S=[4]\setminus\{ell\}`, (6) yields

\[
r(E(S))
=1-(|u_{3\ell}|^2+|u_{4\ell}|^2)
\le 1-|u_{3\ell}|^2=p(S).
\tag{10}
\]

The empty and full sets are trivial. Thus the flow criterion gives (7). `QED`

This is not an arbitrary bistochastic construction: every edge weight in (7) is the squared modulus of an actual `2 x 2` minor of the same unitary `U`.

## 5. Minimal permutation lift on the repeated face

Given any orientation `z` from Lemma 1, define a probability law on `S_4` by

\[
\boxed{
\mu(\sigma)=\frac12 z_{\sigma(3)\to\sigma(4)}.
}\tag{11}
\]

For a fixed ordered pair `(sigma(3),sigma(4))` there are exactly two orders of the two remaining top columns, hence (7) and `sum_j p_j=1` show that `mu` has total mass one.

The law has precisely the marginals needed after the coefficient collision `a_1=a_2`:

\[
\Pr_\mu(\sigma(3)=j)=|u_{3j}|^2,
\qquad
\Pr_\mu(\sigma(4)=j)=|u_{4j}|^2,
\tag{12}
\]

where the second equality follows from (6), and

\[
\Pr_\mu(\{\sigma(1),\sigma(2)\}=J)=q_J.
\tag{13}
\]

Consequently

\[
\Pr_\mu(j\in\{\sigma(1),\sigma(2)\})
=\sum_{J\ni j}q_J
=|u_{1j}|^2+|u_{2j}|^2.
\tag{14}
\]

The important point is that **the individual row-1 and row-2 marginals are unnecessary**. The repeated eigenvalue makes every coefficient in (1) that distinguishes those two rows occur only through their sum.

### Theorem 2 — `MOC4-REPEATED-MINIMAL-LIFT-v2`

If `a_1=a_2`, then the law (11) satisfies

\[
\boxed{
\det(A+B)=\mathbb E_\mu\prod_{i=1}^4(a_i+b_{\sigma(i)}).
}\tag{15}
\]

Therefore MOC4 holds whenever either matrix has a repeated eigenvalue.

#### Proof

Compare (1) with the expectation of (2), grouping equal `a_{I^c}` coefficients.

- `|I|=0,4` are automatic.
- `|I|=1`: rows 3 and 4 match exactly by (12). Rows 1 and 2 have the same coefficient `alpha a_3 a_4`; their sum matches by (14).
- `|I|=2`: the top pair `I=12` matches by (13), and `I=34` matches by (4). The cross pairs occur in equal-coefficient pairs: `13,23` have coefficient `alpha a_4`, and `14,24` have coefficient `alpha a_3`. For every two-column set `T`, a permutation satisfies the exact indicator identity

  \[
  1_{\{\sigma(1),\sigma(3)\}=T}+1_{\{\sigma(2),\sigma(3)\}=T}
  =1_{\sigma(3)\in T}-1_{\{\sigma(3),\sigma(4)\}=T}.
  \tag{16}
  \]

  Taking expectations gives `p_3(T)-r_T`. The corresponding unitary minors obey the same identity

  \[
  Q_{13,T}+Q_{23,T}=\sum_{j\in T}|u_{3j}|^2-Q_{34,T},
  \tag{17}
  \]

  which follows from the rank-two projection onto the columns `T`: the sum of its `2 x 2` principal minors containing row 3 equals its `(3,3)` entry. The row-4 version is identical. Hence both cross-pair aggregates match.
- `|I|=3`: Jacobi complementarity gives `Q_{I,T}=|u_{ij}|^2` when `I^c={i}` and `T^c={j}`. The terms missing rows 3 or 4 match by (12). The two terms missing row 1 or 2 have the common coefficient `alpha` and their aggregate matches by (14).

Every grouped coefficient in (1) therefore equals the corresponding coefficient in `E_mu v_sigma`, proving (15). Swapping `A` and `B` handles a repeated eigenvalue in the `b` spectrum. `QED`

This proof is self-contained at the repeated face and is strictly weaker in its required lift data than the preceding full-one-point-marginal construction.

## 6. Strict support without positive compound minors

The previous collar theorem assumed all sixteen `|u_ij|^2` and all six `q_J` were positive. Neither is necessary.

Let `H_r` be the support graph of the edge weights `r_{jk}`. A strict version of (7),

\[
0<z_{j\to k}<r_{jk}\quad\text{for every edge }r_{jk}>0,
\tag{18}
\]

exists whenever every Hall inequality (8) is strict for each proper `S` crossed by a positive `r`-edge. Indeed choose `epsilon>0` smaller than half every positive edge weight and small relative to every crossed-cut slack. Reserve `epsilon` in **both** orientations of every positive edge. If `d_H(j)` is the support degree, the residual data are

\[
r'_{jk}=r_{jk}-2\epsilon,
\qquad p'_j=p_j-\epsilon d_H(j).
\tag{19}
\]

For a cut `S`,

\[
p'(S)-r'(E(S))
=[p(S)-r(E(S))]-\epsilon|\delta_{H_r}(S)|.
\tag{20}
\]

Thus a sufficiently small `epsilon` preserves all Hall inequalities, the residual orientation exists, and adding the reserved two-sided masses gives (18).

A simple source-valid sufficient condition is

\[
|u_{3j}|>0\quad\text{and}\quad |u_{4j}|>0
\qquad(j=1,2,3,4).
\tag{21}
\]

Under (21), every proper Hall inequality is strict. Singletons are strict because `p_j>0`; three-sets are strict by (10) because `|u_{4\ell}|^2>0`; and for a pair `S`, (9) improves to

\[
r_S\le p_3(S)p_4(S)<p_3(S),
\tag{22}
\]

because row 4 has positive mass outside `S`.

No positivity of the entries in rows 1,2 is required, and **no positivity of all six `q_J` is required**.

## 7. Sharper open collar and boundary stratification

Define the supported permutation set

\[
\Sigma_q:=\{\sigma\in S_4:q_{\{\sigma(1),\sigma(2)\}}>0\}.
\tag{23}
\]

Under (18), (11) satisfies

\[
\mu(\sigma)>0\quad\text{for every }\sigma\in\Sigma_q,
\qquad
\mu(\sigma)=0\quad\text{outside }\Sigma_q.
\tag{24}
\]

### Corollary 3 — `MOC4-SHARP-REPEATED-COLLAR-v2`

Assume `a_1=a_2`, condition (21), and that the supported vertices

\[
\{v_\sigma:\sigma\in\Sigma_q\}\subset\mathbb C
\tag{25}
\]

are not collinear. Then `det(A+B)` lies in the ordinary interior of the full 24-vertex hull. Hence an open neighborhood of `(a,b,U)`, including perturbations that split the repeated eigenvalue, satisfies MOC4.

#### Proof

By (15) and (24), the determinant is a convex combination with strictly positive weight on every supported vertex. Therefore it lies in the relative interior of the convex hull of those supported vertices. Noncollinearity makes that hull two-dimensional, so the point has a positive Euclidean distance from its boundary and hence is also an interior point of the full 24-vertex hull. Continuity of the determinant and of the finitely many permutation vertices gives the claimed open collar. `QED`

### Corollary 4 — sharper necessary degeneration for a counterexample sequence

Let genuine counterexamples converge to data with exactly the repeated pair `a_1=a_2`. Then at the limit at least one of the following holds:

1. some entry in one of the **nonrepeated rows** 3 or 4 vanishes; or
2. the supported vertex set (25) is collinear.

In particular, a zero entry in a repeated row 1 or 2 and a vanishing designated minor `q_J` are **not by themselves** boundary obstructions. This removes two degeneracies that the preceding collar theorem had conservatively listed.

The symmetric statement holds for any repeated pair after relabeling, and for repetition in the `b` spectrum after swapping `A,B`.

## 8. Application to the lead and named partner

The account03/B09 r11 partner result shows why one cannot discard the true-unitary coupling of one- and two-minor data in the generic problem. The present proof stays on that source-valid data: `r_{jk}` are actual squared compound minors and (6), (9), (10), (17) are unitary projection/Jacobi identities. The coefficient collision `a_1=a_2` then shows that only one oriented bottom-pair marginal is needed, rather than a global `(P,R)` permutation lift.

For account03/B07 r12, this supplies a sharper boundary closure around the spectral discriminant. The unresolved `MOC4-PARITY-SLACK-v1` remains a generic simple-spectrum implication, but a violating sequence cannot escape toward a repeated face except through the explicit zero-nonrepeated-row or supported-hull-collinearity strata above. This interfaces directly with account04/B08's independent zero-entry boundary branch: near a repeated eigenvalue, the only zero-entry branch still needing separate treatment can be localized to the rows complementary to the repeated eigenspace.

## 9. Common-block boundary and what is not new here

The preceding B08 result already proves every pair with a nontrivial common reducing subspace by block factorization and the known dimensions at most three. Its nonmonomial `2+2` open-collar criterion remains valid. This run does not claim a new common-block theorem beyond that established boundary result; the substantive advance is the minimal repeated-face lift and the strictly larger repeated-face collar.

## 10. Remaining obligation and failure modes

Full MOC4 is not proved. The first generic obligation remains the lead's structured six-fiber/parity-slack inequality on the simple-spectrum irreducible core, or a true-unitary counterexample to that sufficient gate followed by work on the exact six-fiber inequality. On the B08 boundary side, any counterexample accumulation at spectral repetition is now forced into the two explicit strata of Corollary 4.

No decisive numerical computation was used in this proof; there is therefore no code-derived certificate to promote. The argument is analytic and uses only finite-dimensional max-flow, Cauchy–Binet, Jacobi complementarity, projection-minor identities and convexity/continuity.

No benchmark gold, held-out answer material, credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive, public posting, paid model/API calls, Codex, remote workflow, or permission change was used.
