# MOC4 account04/B07 — exact Spin(6) two-rook convexity and a P-coupled odd-matching payment

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** complex-normal `4 x 4` Marcus-de Oliveira target  
**Worker/run:** account04/B07, `20260922T050458Z-account04-B07-MOC4-r11`  
**Assignment:** representation-theoretic / exterior-algebra proof of the shared mixed-minor constraint, not a stronger untested positivity claim  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact current state consumed

The target remains

\[
\det(A+B)\in\operatorname{conv}\left\{
\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4
\right\}
\]

for every complex normal `4 x 4` pair, including repeated spectra and singular cases.

I read the newest complete campaign-lead version available at the start of this run:
**account03/B07**, `20260922T043708Z-account03-B07-MOC4-r11`, report blob
`c286ea3e5ec5a72902fbff82e94db343f2bbc543`, theorem
`MOC4-TRANSPOSE-SUBGROUP-CUBATURE-v1`.  It gives seven exact true-unitary
subgroup roofs and localizes the remaining target-level problem to
`MOC4-SUBGROUP-RESIDUAL-STATIONARITY-v1`: a positive-gap global maximizer
must satisfy the genuine same-unitary stationarity/Hessian constraints while still lying
below the new subgroup-cubature reserve.  On the lead's hard simple-complex datum the new
endpoint-only ceiling is `gamma <= 289/3`, so a nontrivial residual remains.

The required named OTHER-account result consumed and applied is the newest complete
**account01/B08** run `20260922T044241Z-b08-moc4-r12`, report blob
`f7391a0c2fdeaef6c5fac2bdfbca4513245e5abf`.  It proves
`MOC4-COMPLEX-HADAMARD-COMMON-LIFT-v1`, the projected
`MOC4-V4-BIRKHOFF-GLUE-v1`, and the spectra-independent certificate

\[
8\min_{ij}P_{ij}+\min_{\alpha\beta}R_{\alpha\beta}\ge2
\quad\Longrightarrow\quad \text{MOC4 holds at that relative unitary}.
\]

Its first remaining implication is maximizer-local V4 gluing on the complementary interior
branch.  The present run does **not** assume that gluing always exists.  Instead it derives a
smaller convex representation that is forced separately in each Spin(6) gauge and then turns
that valid local representation into support inequalities.

Two exact dependencies are essential.  My immediate predecessor
`20260922T044421Z-account04-B07-MOC4-r12`, report blob
`edef226995227fc0bff482cf97b6ec722abc8efc`, proved
`MOC4-SPINOR-SINGULAR-VALUE-v1`; account01/B07
`20260922T020412Z-b07-moc4-r11`, report blob
`f569427535050fa80aa4fa079c380b1e3035c68f`, supplies the exact two-channel
support quadratic and complete first-order Spin(6) stationarity equations.

## 2. Exact Spin(6) setup

Use the established real exterior-square realization and identify
`R^6 = C^3`.  Every `O in SO(6)` has the real-linear form

\[
T(z)=Mz+N\bar z,
\qquad
MM^*+NN^*=I,
\qquad
MN^T+NM^T=0.                                      \tag{1}
\]

Put

\[
q^+_{\alpha\beta}=|m_{\alpha\beta}|^2,
\qquad
q^-_{\alpha\beta}=|n_{\alpha\beta}|^2,
\qquad
R=q^++q^-,
\qquad
D=q^+-q^-.                                        \tag{2}
\]

For even bit vectors

\[
\mathcal E=\{000,011,101,110\},
\]

conjugate the selected output and input complex coordinates by `r,c in E`.
The resulting orientation-preserving gauge is

\[
T_{r,c}(z)=M_{r,c}z+N_{r,c}\bar z.                \tag{3}
\]

Entrywise,

\[
|(N_{r,c})_{\alpha\beta}|^2=
\begin{cases}
q^-_{\alpha\beta},&r_\alpha\oplus c_\beta=0,\\
q^+_{\alpha\beta},&r_\alpha\oplus c_\beta=1.
\end{cases}                                      \tag{4}
\]

Identify the four even bit vectors with the four point labels through the tetrahedral
Hadamard basis and write

\[
p_{r,c}:=P_{\iota(r),\iota(c)},\qquad P=(|u_{ij}|^2).
\]

The predecessor theorem gives the **full singular-value statement**

\[
\operatorname{sv}(N_{r,c})=(t,t,0),
\qquad t^2=1-p_{r,c}.                             \tag{5}
\]

It also gives `|det M_{r,c}|=p_{r,c}`.  The earlier report used only the total mass
`||N||_F^2=2t^2` and the determinant-zero phase hexagon.  The present run extracts the exact
linear convex geometry hidden between them.

## 3. New theorem: the anti-linear squared channel is exactly in the two-rook polytope

Let `M_2` denote the 18 incidence matrices of size-two matchings in `K_{3,3}`: matrices with
exactly two `1`s, in distinct rows and distinct columns.

### Theorem 1 — `MOC4-SPINOR-TWO-ROOK-v1`

For every true unitary and every even-even gauge `(r,c)`, put

\[
B^{r,c}_{\alpha\beta}:=|(N_{r,c})_{\alpha\beta}|^2,
\qquad p=p_{r,c}.
\]

If `p<1`, then

\[
\boxed{
\frac{B^{r,c}}{1-p}\in\operatorname{conv}(\mathcal M_2).
}                                                   \tag{6}
\]

If `p=1`, then `B^{r,c}=0`.
Equivalently, for every real weight matrix `W`,

\[
\boxed{
(1-p)\min_{M\in\mathcal M_2}\langle W,M\rangle
\le \langle W,B^{r,c}\rangle
\le
(1-p)\max_{M\in\mathcal M_2}\langle W,M\rangle .
}                                                   \tag{7}
\]

Moreover, as a statement about **linear functions of the squared anti-linear entries at one
fixed gauge**, this convex hull is sharp: every two-rook vertex is realized by a rank-two
partial-isometry anti-linear block satisfying the Bogoliubov equations, hence by an `SO(6)`
point and therefore by the `SU(4) -> SO(6)` exterior-square cover.

### Proof

From `(5)`,

\[
N_{r,c}N_{r,c}^*\le t^2I,
\qquad
N_{r,c}^*N_{r,c}\le t^2I.
\]

Therefore every row sum and every column sum of `B=B^{r,c}` is at most `t^2`, while

\[
\sum_{\alpha,\beta}B_{\alpha\beta}
=\|N_{r,c}\|_F^2=2t^2.                            \tag{8}
\]

For `t>0`, set `S=B/t^2`.  Then `S>=0`, all row/column sums are at most one, and its total
mass is exactly two.  Let

\[
a_i=1-\sum_jS_{ij},\qquad b_j=1-\sum_iS_{ij};
\]

both deficit vectors have total one.  The augmented matrix

\[
\widetilde S=
\begin{pmatrix}
S&a\\
b^T&0
\end{pmatrix}                                      \tag{9}
\]

is `4 x 4` doubly stochastic.  By Birkhoff's theorem it is a convex combination of permutation
matrices.  Because its bottom-right entry is zero, every permutation carrying positive weight
avoids that entry.  Restricting such a permutation to the upper-left `3 x 3` block leaves
**exactly two** ones in distinct rows and columns.  Projecting the Birkhoff decomposition of
`(9)` therefore gives `(6)`.  Equation `(7)` is immediate.

For sharpness of the one-gauge linear hull, start from the canonical pair

\[
M_0=\operatorname{diag}(\sqrt p,\sqrt p,1),
\qquad
N_0=\sqrt{1-p}
\begin{pmatrix}0&1&0\\-1&0&0\\0&0&0\end{pmatrix}.
\]

It obeys `(1)`, and row/column unitary changes move the two nonzero squared entries of `N_0`
to any prescribed two-rook matching.  Thus every vertex of `(6)` is realized. `QED`

### Consequence: there is no missing single-gauge *linear* mass inequality

The theorem classifies the complete convex hull seen by a linear functional of
`|N_{r,c}|^2` if one uses only the exact singular-value information `(5)`.  Therefore another
single-gauge linear inequality in those nine squared masses cannot be the decisive missing
mechanism: any further gain must couple gauges, retain phase/nonlinear information, or use
maximizer stationarity.  This is useful negative information for the current team route.

## 4. New exact support roof from the two-rook theorem

The account01/B07 support quadratic is

\[
Q_{K,X}(O)=\langle D,K\rangle+\frac12\langle R,X\rangle.   \tag{10}
\]

For a gauge `(r,c)`, put

\[
s_\alpha=(-1)^{r_\alpha},\qquad t_\beta=(-1)^{c_\beta},
\qquad
C^{r,c}_{\alpha\beta}=s_\alpha t_\beta K_{\alpha\beta}.    \tag{11}
\]

By `(4)`, cellwise

\[
D=(s t^T)\circ(R-2B^{r,c}).                                \tag{12}
\]

Hence exactly

\[
Q_{K,X}(O)
=\left\langle R,\frac X2+C^{r,c}\right\rangle
-2\langle B^{r,c},C^{r,c}\rangle.                         \tag{13}
\]

Define the two-rook minimum

\[
\mu_2(C)=\min_{M\in\mathcal M_2}\langle C,M\rangle.
\]

Theorem 1 now gives sixteen valid true-unitary roofs:

\[
\boxed{
Q_{K,X}(O)
\le
\left\langle R,\frac X2+C^{r,c}\right\rangle
-2(1-p_{r,c})\mu_2(C^{r,c}).
}                                                            \tag{14}
\]

Since `R` is doubly stochastic, a purely coefficient/P version is

\[
\boxed{
Q_{K,X}(O)
\le
\max_{\rho\in S_3}\sum_\alpha
\left(\frac X2+C^{r,c}\right)_{\alpha,\rho(\alpha)}
-2(1-p_{r,c})\mu_2(C^{r,c}).
}                                                            \tag{15}
\]

Taking the minimum over the sixteen gauges preserves validity.  This is a support-specific
same-unitary inequality, not a common positive lift.  Its Birkhoff coefficients are allowed to
depend on the gauge, exactly as forced by the proof.

## 5. New cross-gauge odd-matching constraint

The mass classification becomes stronger when the **same forbidden odd signed matching** is
viewed in all four compatible gauges.

Fix `rho in S_3` and an even bit pattern `delta in E`.  Along the matching `rho`, select
`q^-` when `delta_alpha=0` and `q^+` when `delta_alpha=1`.  Because `delta` has even Hamming
weight, the selected triple contains an odd number of `q^-` channels; these are precisely the
24 odd-orientation matching patterns excluded from permutation endpoints.

For each `r in E`, define `c in E` by

\[
c_{\rho(\alpha)}=r_\alpha\oplus\delta_\alpha.              \tag{16}
\]

This gives a permutation `pi^dagger_{rho,delta}` of the four even-bit labels.  The `6*4=24`
pairs `(rho,delta)` give 24 distinct such shadow permutations.  Define

\[
p_*:=\max_{r\in E}
P_{\iota(r),\iota(c(r))}.                                   \tag{17}
\]

In every one of the four gauges `(r,c(r))`, the same three selected squared moduli occur as a
three-edge matching inside `|N_{r,c}|^2`.  Therefore `(8)` gives

\[
\boxed{
\sum_{\alpha=1}^3
q^{\delta_\alpha}_{\alpha,\rho(\alpha)}
\le2(1-p_*),
}                                                            \tag{18}
\]

where `q^delta` means `q^-` for `delta=0` and `q^+` for `delta=1`.

There is also a strictly nonlinear amplitude refinement.  The nuclear norm of every
`N_{r,c}` is `2\sqrt{1-p_{r,c}}`.  After permuting columns by `rho`, choose diagonal phases so
that the trace is the sum of the three selected absolute diagonal entries.  Trace-norm duality
gives

\[
\boxed{
\sum_{\alpha=1}^3
\sqrt{q^{\delta_\alpha}_{\alpha,\rho(\alpha)}}
\le2\sqrt{1-p_*}.
}                                                            \tag{19}
\]

AM-GM then yields the sharp three-matching product consequence

\[
\boxed{
\prod_{\alpha=1}^3
q^{\delta_\alpha}_{\alpha,\rho(\alpha)}
\le\frac{64}{729}(1-p_*)^3.
}                                                            \tag{20}
\]

The constant `64/729` is sharp already for the rank-two partial-isometry singular-value
class: the scaled rank-two projection with all three selected diagonal magnitudes `2/3`
achieves equality in the amplitude product bound.

## 6. Direct parity-payment corollary for the scalar support reduction

This is the target-facing use of `(18)`.  In the scalar reduction, fix a parity-bad quotient
assignment `rho` and write

\[
g_\alpha=|G_{\alpha,\rho(\alpha)}|,
\qquad
s_\alpha=\operatorname{sgn}G_{\alpha,\rho(\alpha)},
\qquad
m_\rho=\min_\alpha g_\alpha.
\]

Put

\[
v_\alpha=\frac{r_{\alpha,\rho(\alpha)}
+s_\alpha d_{\alpha,\rho(\alpha)}}2,
\qquad
w_\alpha=\frac{r_{\alpha,\rho(\alpha)}
-s_\alpha d_{\alpha,\rho(\alpha)}}2.                       \tag{21}
\]

Here `v` is the coefficient-preferred orientation mass and `w` the wrong-orientation mass.
Parity-bad means the preferred triple contains an odd number of `q^-` channels, so `(18)`
applies to `v`.  Let `p_*^rho` be the corresponding shadow-permutation quantity `(17)` and
write

\[
R_\rho=\sum_\alpha r_{\alpha,\rho(\alpha)}.
\]

Then

\[
\sum_\alpha w_\alpha
=R_\rho-\sum_\alpha v_\alpha
\ge
\left[R_\rho-2(1-p_*^\rho)\right]_+.
\]

Therefore the exact orientation-penalty term satisfies

\[
\boxed{
2\sum_\alpha g_\alpha w_\alpha
\ge
2m_\rho\left[R_\rho-2(1-p_*^\rho)\right]_+.
}                                                            \tag{22}
\]

This is a genuine **P-coupled mixed-minor payment**.  It does not infer a probability law on
24 permutations.  It says instead that a parity-bad preferred `R` assignment cannot carry too
much mass unless the same unitary pays through a specific four-point unistochastic pattern.
That is exactly the type of coupling absent from the lead's endpoint-only subgroup cubature.

## 7. Application of the named partner result and updated conditional chain

The partner's `MOC4-V4-BIRKHOFF-GLUE-v1` remains a valid sufficient global lift when its 24
glued weights are nonnegative, and `8 min P + min R >=2` remains a closed individual-unitary
class.  Outside that class, this run supplies a different valid mechanism:

1. no global common-permutation law is assumed;
2. each of the sixteen Spin(6) gauges has its own exact two-rook convex representation `(6)`;
3. those local representations give the support roofs `(14)`-`(15)`;
4. the four gauges containing any one forbidden odd matching combine to the same-unitary
   payment `(18)`-`(22)`.

Thus the partner's failed-or-unavailable global glue is **not** replaced by another unsupported
positivity assertion.

Combining with the newest lead gives the following compact conditional end-to-end route.
A hypothetical MOC4 failure has a genuine global support maximizer.  The lead's subgroup
cubature places it in the positive residual branch.  At that same maximizer, account01/B07's
stationarity equations, the predecessor's determinant hexagons, the partner's V4/interior
certificates, and the sixteen new two-rook roofs all hold simultaneously.  If their structured
coefficient combination forces the parity-bad payments `(22)` plus the existing assignment-gap
terms to dominate the lead's residual reserve, then the support gap is nonpositive and MOC4
follows; all repeated/singular cases remain covered because these identities use no spectral
division.

The first essential missing implication is now concrete:

> **`MOC4-TWO-ROOK-RESIDUAL-STATIONARITY-v1` (OPEN).**  At a genuine
> positive-reserve global maximizer for a structured spectral coefficient pair `(K,X)`, combine
> the six complex Spin(6) stationarity balances with the sixteen exact roofs `(14)` and the
> P-coupled parity payments `(22)` to prove that the lead's subgroup-cubature residual is paid.
> A refutation must use actual spectra, one support direction and one true unitary satisfying
> the maximizer conditions; an arbitrary `(P,R)` point or independently chosen gauge
> decompositions do not count.

This is narrower than another common-lift conjecture and keeps the target on the genuine
same-unitary maximizer locus.

## 8. Exact verification

`verify_two_rook.py` uses only standard-library `Fraction` arithmetic and the exact rational
true unitary from account01/B08 `20260922T024227Z-account01-B08-MOC4-r12`.  It reconstructs
`Lambda^2 U`, all sixteen Bogoliubov gauges, verifies the row/column/total conditions in
Theorem 1, performs an exact Birkhoff decomposition of each `4 x 4` augmentation `(9)`, and
checks the 24 cross-gauge odd-matching mass/product inequalities.

Captured output:

```text
PASS MOC4-SPINOR-TWO-ROOK-CROSS-GAUGE-v1
det_U = 1
gauges_checked = 16
max_exact_birkhoff_terms = 9
odd_signed_matchings_checked = 24
distinct_shadow_permutations = 24
max_odd_mass_ratio = 29053648/43405625
max_odd_product_ratio = 1806991191020961/2827514326000000
sharp_product_constant = 64/729
```

The computation is a regression check; the general theorems are proved above.

## 9. Status and non-claims

**Status:** `ESSENTIAL_STEP_APPLIED`.

Paid in this run:

- exact convex-hull classification of each gauge's anti-linear squared channel as a scaled
  size-two bipartite matching polytope;
- the corresponding 16 support roofs for the exact Spin(6) quadratic;
- a cross-gauge P-coupled mass/amplitude/product bound for every forbidden odd signed matching;
- the explicit parity-payment inequality `(22)` for the scalar support reduction.

Not paid:

- the lead's full positive-reserve stationarity implication;
- a global 24-state common lift;
- a full MOC4 proof or counterexample.

No benchmark material, held-out answers, credentials, scheduler identifiers, machine-local
paths, unrelated private data, email/Drive material, public posting, paid model/API/Codex call,
remote workflow, permission change, or notification enabling was used.
