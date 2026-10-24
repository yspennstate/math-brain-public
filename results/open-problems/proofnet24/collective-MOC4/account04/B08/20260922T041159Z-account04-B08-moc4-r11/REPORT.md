# MOC4 account04/B08 — bidirectional pair-gap ceiling and zero-reserve star rigidity

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Run:** `20260922T041159Z-account04-B08-moc4-r11`  
**Campaign:** MOC4, complex-normal `4 x 4` Marcus–de Oliveira scope  
**Assignment:** characterize extremal boundary/degenerate configurations needed for the global deduction  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN_RESEARCH`; `full_brain_connected=false`.

## 1. Exact state consumed

For a support direction `eta`, write

\[
H_\sigma=\Re\!\left(\eta\prod_{i=0}^3(a_i+b_{\sigma(i)})\right),\qquad
M=\max_\sigma H_\sigma.
\]

The newest complete campaign-lead result consumed is account03/B07
`MOC4-V4-PAIR-GAP-CEILING-v1`, canonical report
`proofnet24/collective-MOC4/account03/B07/account03-B07-20260922T033411Z-d2a63b2a/REPORT.md`, commit
`dcce2e52aee9c3fb338be4dd56acb02114ebfdde`, blob
`28cbce0f0a6213c0760e0777a5baa5b0de12b31a`.  If

\[
m={1\over24}\sum_\sigma H_\sigma,\quad d=M-m,
\]

`Q` is the largest average over a `V_4` coset, `Delta=M-Q`, and

\[
g^{\rm out}_\tau=2M-\max_\sigma(H_\sigma+H_{\tau\circ\sigma}),
\qquad G_{\rm out}=\sum_{\tau\text{ transposition}}g^{\rm out}_\tau,
\]

then every genuine true-unitary support violation `h(U)=M+gamma` obeys

\[
0<\gamma\le {3d-\Delta-G_{\rm out}/2\over4}. \tag{1}
\]

The assigned OTHER-account partner account01/B09 result consumed is
`MOC4-DENSE-ANCHOR-MARGINAL-LIFT-v1 = REFUTED`, canonical report
`proofnet24/collective-MOC4/account01/B09/20260922T035002Z-b09-moc4-r11/REPORT.md`, blob
`ac3bec22cb51296419870e462aa83e585795088a`.  It gives a dense exact true orthogonal point for which even singleton plus nine anchored two-minor marginals have no positive `S_4` lift, while an exact three-vertex certificate places the corresponding simple-complex determinant strictly inside the MOC4 hull and an exact pair derivative shows the point is not a support maximizer.  Thus universal positive lifting is not a valid replacement for maximizer-local geometry.

I also used account03/B09's newest `MOC4` handoff `20260922T040531Z-account03-B09-cycle-separator-nogo.md`, blob `ca3b1f48004bb6c9c29de34e29b64f39380b1641`, only to constrain the next step: even genuine `SO(6)` transport data can violate natural even-endpoint cycle cuts, so the remaining proof must use the structured spectral support normal, not transport cuts alone.

## 2. New bidirectional ceiling

Define the opposite-sided pair gaps

\[
g^{\rm in}_\tau=2M-\max_\sigma(H_\sigma+H_{\sigma\circ\tau}),
\qquad G_{\rm in}=\sum_\tau g^{\rm in}_\tau. \tag{2}
\]

### Theorem — `MOC4-BIDIRECTIONAL-V4-PAIR-CEILING-v1`

Every genuine support violation satisfies both one-sided ceilings, hence

\[
\boxed{
0<\gamma\le {\mathcal R_{\rm bi}\over4},\qquad
\mathcal R_{\rm bi}
=3d-\Delta-\frac12\max(G_{\rm out},G_{\rm in}).
} \tag{3}
\]

In particular, if `mathcal R_bi=0`, that entire spectra/support-direction instance is safe for **every** true unitary.

### Proof

Equation (1) is the lead theorem.  Now swap the two normal matrices.  The same determinant is

\[
\det(D_a+UD_bU^*)=\det(D_b+U^*D_aU),
\]

so the same support value and the same gap `gamma` are represented by the swapped datum `(b,a,U*)`.  Its endpoint supports are exactly

\[
H'_\sigma=H_{\sigma^{-1}}. \tag{4}
\]

Inversion preserves `M` and `m`.  Because the Klein four group `V_4` is normal in `S_4`, inversion permutes its cosets, so the same `Q` and `Delta` occur.  Applying the lead theorem to the swapped datum transforms

\[
H'_\sigma+H'_{\tau\circ\sigma}
=H_{\sigma^{-1}}+H_{\sigma^{-1}\circ\tau},
\]

and therefore its six gap sum is exactly `G_in`.  Thus

\[
4\gamma\le3d-\Delta-G_{\rm out}/2,
\qquad
4\gamma\le3d-\Delta-G_{\rm in}/2.
\]

Taking the smaller right side proves (3).  No stationarity, invertibility, arbitrary bistochastic relaxation, or positive common lift for an individual `U` is used. ∎

## 3. Exact endpoint characterization of zero reserve

The bilateral improvement has a sharp boundary interpretation rather than being only another aggregate constant.

Fix any maximizing endpoint `sigma_*` with `H_{sigma_*}=M`, and let

\[
B_*={1\over4}\sum_{v\in V_4}H_{\sigma_*\circ v}. \tag{5}
\]

For either side `eps in {out,in}`, let `n^eps_tau(sigma)` denote respectively `tau o sigma` or `sigma o tau`, and define the incident-star roof excess

\[
e^\varepsilon_\tau(\sigma_*)=
\max_\sigma\bigl(H_\sigma+H_{n^\varepsilon_\tau(\sigma)}\bigr)
-\bigl(M+H_{n^\varepsilon_\tau(\sigma_*)}\bigr)\ge0. \tag{6}
\]

### Theorem — `MOC4-ZERO-RESERVE-ENDPOINT-STAR-RIGIDITY-v1`

For each side,

\[
\boxed{
\mathcal R_\varepsilon:=3d-\Delta-G_\varepsilon/2
=(Q-B_*)+\frac12\sum_\tau e^\varepsilon_\tau(\sigma_*).
} \tag{7}
\]

Consequently every structured endpoint support has `R_out>=0` and `R_in>=0`, and

\[
\boxed{
\mathcal R_\varepsilon=0
\iff
B_*=Q\ \text{and}\ e^\varepsilon_\tau(\sigma_*)=0
\text{ for all six transpositions }\tau.
} \tag{8}
\]

Thus a zero-reserve direction is characterized exactly by an extremal endpoint whose `V_4` fiber itself attains the best fiber roof and whose complete six-edge transposition star simultaneously attains all six pair roofs.  If there are several maximizing endpoints, (7) applies to each of them.

### Proof

At the permutation unitary for `sigma_*`, the lead's exact six-transposition identity gives

\[
\sum_\tau H_{n^\varepsilon_\tau(\sigma_*)}
=6m+2(M-B_*), \tag{9}
\]

with the second side obtained, as above, by inversion symmetry.  By (6),

\[
g^\varepsilon_\tau
=M-H_{n^\varepsilon_\tau(\sigma_*)}-e^\varepsilon_\tau.
\]

Summing this identity, inserting (9), and using `Delta=M-Q` gives exactly (7).  Both terms on its right are nonnegative, proving (8). ∎

One useful corollary is that the lead's sufficient inequality `Delta+G_epsilon/2 >= 3d` can never be strict on a genuine structured endpoint support; when it closes a direction it does so at the rigid equality configuration (8).

## 4. Exact decisive applications

### 4.1 The campaign lead's former one-sided residual closes bilaterally

For the lead's exact real endpoint datum

\[
a=(-1,2,1,0),\qquad b=(-1,1,-2,2),\qquad \eta=1,
\]

exact arithmetic gives

\[
M=36,\quad m=29/6,\quad Q=15,\quad d=187/6,\quad\Delta=21.
\]

The six `out` gaps are

`36, 9, 36, 32, 4, 24`, so `G_out=141` and `R_out=2`, reproducing the lead's one-sided allowance `gamma<=1/2`.

The opposite six gaps are

`36, 36, 9, 4, 36, 24`, so

\[
G_{\rm in}=145,\qquad
3d-\Delta-G_{\rm in}/2=0. \tag{10}
\]

Therefore (3) proves **no positive support gap exists for this exact spectra/direction**, for any true unitary.  The unique maximizing endpoint is `(0,1,3,2)` in zero-based notation; its `V_4` average is `B_*=Q=15`.  On the `in` side all six star excesses in (6) are zero.  On the `out` side exactly one star edge has excess `4`, explaining the reserve `2` via (7).

This does not invalidate the lead's abstract half-integer low-frequency witness for the one-sided relaxation it was built to test.  It shows that witness is not feasible for the **bilateral** source-valid roof system obtained by also applying the same theorem after swapping `(A,B)`.

### 4.2 Assigned partner datum remains a genuine hard residual

For account01/B09's exact simple-complex spectra in real-part support,

\[
a=(-4+4i,-i,-3+2i,-4-4i),
\]
\[
b=(-4-4i,2-i,2-4i,4-i),\qquad\eta=1,
\]

exact endpoint arithmetic gives

\[
M=256,\quad m=-217/2,\quad Q=245/2,\quad
\Delta=267/2,\quad d=729/2.
\]

Here `G_out=862` and `G_in=746`, hence

\[
\mathcal R_{\rm out}=529,\qquad
\mathcal R_{\rm in}=587,
\qquad
\mathcal R_{\rm bi}=529. \tag{11}
\]

The unique maximizing endpoint again lies in a `Q`-maximal `V_4` fiber, but the incident-star roof excess sums are `1058` and `1174`, respectively.  So fiber extremality alone is not enough: the exact obstruction is the failure of the maximizing endpoint's six-edge star to realize the pair roofs.  The partner's actual dense unitary is nevertheless known from its exact report to be strictly inside the target hull and nonstationary in `eta=1`; it is a negative control, not a residual maximizer or MOC4 counterexample.

## 5. Verification and failed substep

`verify_bidirectional_v4_pair_ceiling.py` uses only `fractions.Fraction` and exact finite `S_4` enumeration.  It checks inversion symmetry, both six gap lists, the lead closure `R_bi=0`, and the partner residual `R_bi=529`.  Its captured output ends

`PASS MOC4-BIDIRECTIONAL-V4-PAIR-CEILING-v1`.

`verify_zero_reserve_star.py` independently checks the six-transposition identity at the maximizing endpoint and the exact reserve decomposition (7), including the star-excess values above.  A separate attempt to persist that second verifier's captured-output text was denied by the platform safety layer; no bypass was attempted.  The verifier source itself was preserved, and the first exact verifier plus captured output were successfully persisted.

## 6. Updated conditional full deduction and first unpaid implication

A compact surviving route is now:

1. Separate a hypothetical MOC4 failure by a real support direction and choose a genuine global unitary maximizer.
2. Apply all existing singular/repeated/common-block reductions; the present result does not discard those cases.
3. Compute both endpoint pair-gap sums.  If either side has zero reserve, (3) closes the entire support direction.  Equation (8) identifies exactly what that endpoint boundary means.
4. Only when
   \[
   \mathcal R_{\rm bi}>0
   \]
   can a violation remain, and it must satisfy
   \[
   0<\gamma\le\mathcal R_{\rm bi}/4. \tag{12}
   \]
5. On that strictly positive bilateral reserve branch, use true same-unitary `P-R-D` compatibility, pair-Rayleigh stationarity, Cartan/Hessian constraints and the structured spectral `SO(6)` support normal.  Account03/B09's exact cycle-separator no-go shows that transport-only cuts cannot replace this step.

The first essential missing implication is therefore:

> **`MOC4-BIDIRECTIONAL-RESIDUAL-PR-v1` (OPEN).**  For a source-valid support datum with `R_bi>0`, prove that no genuine common-unitary global support maximizer satisfying the existing exact `P-R-D`, pair-Rayleigh, Cartan/Hessian and structured spectral-normal constraints can realize a positive gap `0<gamma<=R_bi/4`; or construct a genuine source-valid target counterexample satisfying all those conditions.

This is strictly narrower than the lead's preceding one-sided residual because the exact lead negative-control datum is removed completely by the opposite-side theorem.

## 7. Status and safeguards

- `MOC4-BIDIRECTIONAL-V4-PAIR-CEILING-v1`: **proved**, conditional only on the already-proved lead theorem and determinant swap symmetry.
- `MOC4-ZERO-RESERVE-ENDPOINT-STAR-RIGIDITY-v1`: **proved**.
- The lead's real negative-control spectra/direction: **closed for all true unitaries in that direction** by the bilateral ceiling.
- The assigned partner's simple-complex datum: bilateral reserve remains positive; its known unitary is not a maximizer/counterexample.
- `MOC4-BIDIRECTIONAL-RESIDUAL-PR-v1`: **open**.
- Full MOC4: **open**.

Scoped review found no benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private transcripts, production keys, email/Drive material, public-release action, paid model/API/Codex call, remote workflow, or permission bypass in the scientific artifacts.
