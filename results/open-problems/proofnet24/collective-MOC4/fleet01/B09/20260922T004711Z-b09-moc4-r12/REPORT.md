# MOC4 fleet01/B09 r12 — exact nonmonomial bi-Rayleigh maximum at a singular sum

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex-normal 4-by-4 Marcus–de Oliveira target  
**Worker:** fleet01/B09  
**Candidate:** `MOC4-BIRAYLEIGH-MONOMIAL-RIGIDITY-NOGO-v1`  
**Outcome:** `CANDIDATE_REFUTED` for the stronger monomial-rigidity route; parent MOC4 remains OPEN  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact peer input and conditional end-to-end argument

This run directly consumes **fleet02/B07, `MOC4-BIRAYLEIGH-ORBIT-v1`**, shared handoff commit
`1fa3c78f9ae8ff776d345ad5d6d84f4b700e2c87`, with scientific report
`proofnet24/collective-MOC4/fleet02/B07/20260922T003238Z-fleet02-B07-MOC4-r11/REPORT.md`.
That result proves, without using an inverse, that every genuine two-column or two-row
`U(2)` slice of
\[
D(U)=\det(D_a+UD_bU^*)
\]
has an exact two-dimensional Hermitian Rayleigh-quotient support form. Consequently,
a global maximizer of
\[
h_\eta(U)=\Re(\eta D(U))
\]
satisfies six column-pair and six row-pair top-eigenvector conditions. The peer calls the
remaining implication `BR4`: on the generic strict-support locus, show that those twelve
conditions force
\[
h_\eta(U)\le M_\eta(a,b):=\max_{\sigma\in S_4}
\Re\!\left(\eta\prod_i(a_i+b_{\sigma(i)})\right).
\]
Together with the already justified strict-gap perturbation for repeated spectra and
singular sums, `BR4` would close MOC4.

The tempting strengthening
\[
\text{all twelve pair-top conditions}\quad\Longrightarrow\quad U\text{ is monomial}
\tag{MR}
\]
would imply `BR4`, but fleet02/B07 explicitly warned that `(MR)` was unproved.
The construction below shows `(MR)` is false, using an actual rational orthogonal
matrix and exact rational spectra. Therefore a proof of `BR4` must use the *height*
of the support value and cross-pair/global coupling; local pair maximality alone
does not classify the unitary as a permutation.

## 2. Exact source-valid construction

Take the rational orthogonal matrix
\[
U=\begin{pmatrix}
-220/243&71/243&-62/243&14/81\\
-61/243&-220/243&-68/243&-16/81\\
68/243&62/243&-215/243&-22/81\\
-16/81&14/81&22/81&-25/27
\end{pmatrix},
\]
and the real (hence complex-normal/Hermitian) simple spectra
\[
a=\left(\frac{410}{81},\frac{15388}{1539},-\frac{2603}{21276},
\frac{1267}{984}\right),\qquad
b=(-4,-2,3,-1).
\]
Set
\[
X=D_a+UD_bU^T.
\]

The exact verifier proves all sixteen entries of `U` are nonzero, `U^TU=I`,
every `2x2` minor of `U` is nonzero, and every two-by-two compression
discriminant used by the team's genericity checker is nonzero. The spectra
`a,b` are simple and nonzero, all sixteen sums `a_i+b_j` are nonzero,
and all 24 permutation products are distinct. Also every off-diagonal entry
of `UD_bU^T` is nonzero, so with simple diagonal `D_a` there is no common
coordinate reducing split.

The key exact algebraic feature is
\[
\operatorname{rank}X=2.
\tag{1}
\]
Indeed every one of the sixteen `3x3` minors of `X` vanishes, while every
one of its thirty-six `2x2` minors is nonzero. Hence
\[
D(U)=\det X=0,\qquad \operatorname{adj}(X)=0.
\tag{2}
\]

## 3. Why this is a genuine bi-Rayleigh maximum in all twelve pair slices

For any differentiable matrix perturbation `X(t)` through `X`,
\[
\frac{d}{dt}\det X(t)\big|_{t=0}
=\operatorname{tr}(\operatorname{adj}(X)X'(0))=0
\]
by (2). Thus `U` is first-order stationary for every true unitary direction,
not merely for real rotations.

Now apply the singular-safe exact pair-Rayleigh formula of
`MOC4-BIRAYLEIGH-ORBIT-v1`. On a fixed column pair `(p,q)`, the support
restriction for `eta=1` is a Hermitian `2x2` Rayleigh quotient. Stationarity
makes its off-diagonal entry zero in the current ordered basis. Its two
diagonal values are exactly `h(U)=0` and the support value after swapping
the two `b` labels. Exact rational arithmetic gives, for all six column
pairs,
\[
h(UP_{pq})<0=h(U).
\tag{3}
\]
The closest column swap is already strictly below zero:
\[
\max_{p<q}h(UP_{pq})
=-\frac{642336316178}{59454710503407}<0.
\tag{4}
\]
Therefore the current column is the **strict top eigenvector** in all six
column-pair compressions.

The symmetric row-pair formula gives the same conclusion on all six row
pairs:
\[
h(P_{ij}U)<0=h(U),
\tag{5}
\]
with
\[
\max_{i<j}h(P_{ij}U)
=-\frac{5710049564041}{5872070173176}<0.
\tag{6}
\]
Thus `U` satisfies all twelve strict pair-top conditions appearing in the
peer's `BR4` premise. Yet `U` is manifestly nonmonomial: in fact every
entry is nonzero. This is an exact source-valid counterexample to `(MR)`.

## 4. It is not a counterexample to MOC4

For support direction `eta=1`, the unique maximizing permutation is
\[
\sigma=(3,4,2,1)
\]
in one-based notation, with
\[
M_1(a,b)=
\frac{1089898404806915}{2609808965856}>0.
\tag{7}
\]
The runner-up is `(4,3,2,1)`, and the exact unique-support gap is
\[
\frac{457850522305}{4027482972}>0.
\tag{8}
\]
Since `h(U)=0`, the desired support inequality has large slack.

More strongly, because all permutation vertices are real here, the verifier
gives an exact two-vertex hull certificate for the determinant itself. The
minimum vertex is
\[
m=-\frac{749320711645835}{1304904482928}<0,
\]
and
\[
0=
\frac{299728284658334}{517707965619717}\,M_1+
\frac{217979680961383}{517707965619717}\,m.
\tag{9}
\]
The two positive coefficients sum to one. Hence `D(U)=0` lies in the target
convex hull exactly.

So this construction refutes only the stronger local-rigidity proof route,
not MOC4 and not `BR4`.

## 5. Precise consequence for the shared proof

The first essential unpaid implication remains `BR4`. What has changed is
that one proposed way of proving it is now eliminated:

* Twelve exact pair-top conditions do **not** force a unitary to be
  monomial.
* The failure occurs for a dense true unitary with simple nonzero spectra,
  24 distinct permutation vertices, a unique support-maximizing vertex,
  nonzero 1x1/2x2 unitary minors, nondegenerate two-by-two compression data,
  and no common coordinate reducing split.
* The construction deliberately has `det(A+B)=0`. Therefore it does **not**
  refute a hypothetical *nonsingular-only* monomial-rigidity lemma. The
  team's strict-gap perturbation says a target-level violation can be moved
  off the singular determinant locus, so such a narrower lemma remains
  logically possible.
* Nevertheless, singular pairs are part of the MOC4 target, and the
  fleet02/B07 calculus was designed to be singular-safe. Any end-to-end
  proof that classifies all bi-Rayleigh maxima by monomiality is impossible.

The useful next target is therefore the actual `BR4` height inequality,
using genuinely global information absent from the twelve local conditions:
the 24-label orbit barycenter from fleet02/B07, the exact mixed `(P,R)`
assignment reduction from fleet01/B07, or the structured `SO(6)`/Weyl
form from fleet04/B07.

## 6. Verification and provenance

`verify_birayleigh_nonmonomial.py` uses only Python standard-library
`fractions.Fraction` arithmetic. It checks orthogonality, all stated
genericity conditions, exact rank two, all twelve strict pair-swap
inequalities, the 24 distinct target vertices, the unique support maximum,
and the exact two-vertex hull certificate. No floating-point tolerance is
used for any claim in this report.

No benchmark material, credentials, scheduler identifiers, machine paths,
unrelated private data, email, Drive data, public posting, remote workflow,
paid model/API, or permission change is used.
