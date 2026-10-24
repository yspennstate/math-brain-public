# account04/B12 — exact two-step Poincare refund on the arity-10 gate

**Run:** `B12-20260922T011808Z-r43`  
**Outcome:** `ESSENTIAL_STEP_APPLIED / UNIVERSAL_BOUND_STILL_OPEN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** **WITHOUT_VERIFIED_BRAIN**. Fresh repository control and peer mathematics were consumed directly; no native/authenticated cognitive-brain retrieval entered the proof.

## 0. Live target and the peer theorem actually consumed

Fresh owner control revision `2026-09-22.2` supersedes the older row-coding task for substantive work and tells the FEI fleet to converge on the all-gate `Gamma` reformulation. The former decomposable/AND-extremality claim for the read-once potential has already been rigorously refuted by source-valid balanced gates, so this run does not repeat that dead route.

The named newest compatible **other-account** result actually consumed is account02/B16:

`proofnet24/P03-fei/fleet-2026-09-21/account02/B16/20260922T010120Z-gate-margin-restriction-martingale/REPORT.md`, blob `335d6ffa58cae84c7b47e742a250a20d2e2bddd4`.

Its exact implication used here is the all-depth Poincare-currency ledger. For a base potential `Gamma_0=0`, along any adaptive restriction path,

\[
L_r=H_t(G_r)-\mathbb E[H_t(G_{r+1})\mid G_r]\ge0,
\qquad
Q_r=P(G_r)-\mathbb E[P(G_{r+1})\mid G_r]\ge0,
\]
with
\[
P(F)=\frac{I(F)}4-q_F(1-q_F),
\]
and for every stopping block `sigma`
\[
L_\sigma=\mathbb E\sum_{r<\sigma}L_r,
\qquad
Q_\sigma=\mathbb E\sum_{r<\sigma}Q_r.
\]
For the scalar quadratic potential
\[
\Gamma_C(p)=4C\,p(1-p),
\]
the corrected block slack is exactly
\[
\boxed{
\mathcal S_C(\sigma)=4C Q_\sigma-L_\sigma
=4Q_\sigma(C-\rho_\sigma),
\qquad
\rho_\sigma:=\frac{L_\sigma}{4Q_\sigma}.
}
\tag{0.1}
\]
Thus `rho_sigma <= C` is the exact signed finite-block condition for this quadratic base. No positive-part replacement and no discarded child continuation is allowed.

The exact gate used below is the 10-input balanced monotone witness isolated by account03/B12 and reconstructed/certified by account04/B13. Its truth-table SHA-256 is

`3168d8fb8ac9f5d6d7dca1d79146392aecb5eb55cc76ccb028395a9e6a62bfb4`,

with
\[
I(G)=257/128,
\qquad
P(G)=\frac{I(G)-1}{4}=129/512,
\]
and certified spectral entropy
\[
6.509836127588151479
< H(G) <
6.509836127588151480.
\tag{0.2}
\]

## 1. New theorem: every two-step adaptive block is safe at C0=6.4548

Let the ten root coordinates be indexed `0,...,9`. Choose a first coordinate `i`. After observing its value `b in {0,1}`, choose any second coordinate `j_b != i`; the second choice is allowed to depend on the first revealed value. This gives `10*9*9=810` legal branch-adaptive depth-two policies.

For a policy
\[
\pi=(i;j_0,j_1),
\]
write the four depth-two descendants as
\[
G_{b,c}^{\pi}=G\big|_{x_i=b,\,x_{j_b}=c}.
\]
Since the input is uniform, exact telescoping in the account02/B16 ledger gives
\[
L_\pi
=H(G)-\frac14\sum_{b,c}H(G_{b,c}^{\pi}),
\tag{1.1}
\]
\[
Q_\pi
=P(G)-\frac14\sum_{b,c}P(G_{b,c}^{\pi}),
\tag{1.2}
\]
and
\[
\rho_\pi=\frac{L_\pi}{4Q_\pi}.
\tag{1.3}
\]

### Theorem 1 — uniform two-step refund

For the exact source gate above, **every one of the 810 branch-adaptive two-step policies** satisfies
\[
\boxed{
\rho_\pi
<6.234880151529528151
<6.4548.
}
\tag{1.4}
\]
More quantitatively,
\[
\boxed{
6.4548-\max_\pi\rho_\pi
>0.219919848470471849.
}
\tag{1.5}
\]
Equivalently, for the quadratic block slack (0.1),
\[
\boxed{
\min_\pi \mathcal S_{6.4548}(\pi)
>0.066335686715153312.
}
\tag{1.6}
\]

This is stronger than existence of one favorable continuation: no matter which first coordinate is used and no matter which legal second coordinate is selected on either first-step branch, the complete two-step signed block is safe at the numerical level `C0=6.4548`.

## 2. The explicit continuation refund: one step fails, two steps repairs it

The same certificate evaluates every first-coordinate block. Nine coordinates already satisfy the one-step quadratic condition. The exceptional coordinate is zero-based coordinate `9`, for which
\[
\boxed{
8.784179008294407775
<\rho_{9}^{(1)}<
8.784179008294407776.
}
\tag{2.1}
\]
Hence the one-step corrected quadratic block slack at `C0=6.4548` is strictly negative on that coordinate. This is a real local failure, not rounding noise.

But after revealing coordinate `9`, **all 81** branch-adaptive legal second-step choices repair the deficit. Their worst depth-two ratio satisfies
\[
\boxed{
\rho_{(9;j_0,j_1)}
<5.958787894233570883
}
\tag{2.2}
\]
for every `j_0,j_1 != 9`, so even the worst second continuation has safety margin
\[
\boxed{
6.4548-\rho_{(9;j_0,j_1)}
>0.496012105766429117.
}
\tag{2.3}
\]
The best certified branch-adaptive choice has
\[
5.769277021914864549
<\rho<
5.769277021914864550.
\tag{2.4}
\]

This is the concrete cancellation mechanism predicted abstractly by account02/B16: a large first residual can be more than repaid by authentic descendant continuation in the same Poincare currency. Discarding the child term would misclassify this root direction.

## 3. What this does and does not say about the potential

The result is **not** a proof that the pure quadratic potential with center cap `6.4548` is universal. In fact the two-input AND gate at uniform bias already calibrates the obstruction sharply: its spectral law has `H=2`, `I=1`, output variance `V_q=3/4`, hence
\[
P=I/4-q(1-q)=1/16,
\qquad
\rho=\frac{H}{4P}=8.
\]
Therefore a pure quadratic potential `Gamma_C(p)=4C p(1-p)` requires at least `C=8` on that gate.

The new information is different and useful: the exact arity-10 gate that refutes the **shape** of the old read-once potential is **not** intrinsically a depth-two entropy/Poincare obstruction. In the `Gamma_0=0` NET coordinates, its unique bad first reveal is uniformly repaired at the next step, with substantial quantitative slack. Thus the current difficulty has two genuinely different pieces:

1. the AND/read-once boundary geometry, which a pure quadratic cap below `8` cannot pay; and
2. the balanced composition-prime center obstruction, for which signed continuation can be strongly favorable even when a one-step residual is bad.

A successful future potential or block proof must reconcile those two geometries rather than force the one-step residual to have one sign everywhere.

## 4. Relation to the previous account04/B12 and B18 interfaces

This calculation does not revoke the previous account04/B12 prime safe-split obstruction for the old read-once base. That theorem used the read-once `Gamma` itself; the present theorem deliberately changes coordinates to the account02/B16 `Gamma_0=0` NET ledger in order to isolate the continuation mechanism. The two statements are compatible.

Likewise nothing here spends, weakens, or rewrites account04/B18's mixed-curvature identity
\[
\kappa_{ik}=\kappa_{ki}=p_{ik}+4o_{ik},
\qquad
\sum_{i\ne k}\kappa_{ik}=4d_k.
\]
The opposite-sign overlap bank remains intact. In particular, this report makes **no** assumption that
\[
\sum_k d_k=O(J),
\]
which remains false as a general inference from the interface-B bookkeeping.

## 5. Exact certificate

`check_two_step_quadratic_block.py` reconstructs the source-valid 18-input parent, verifies its published SHA-256, extracts the exact 10-input gate, verifies the root SHA-256, `I=257/128`, and `P=129/512`, and encloses every Fourier entropy using rational atanh-series intervals.

It checks:

- the root entropy interval (0.2);
- all ten first-coordinate ratios;
- that coordinate `9` is the unique first-coordinate violation at `C0=6.4548`;
- all `810` legal branch-adaptive depth-two policies;
- strict positivity of the corrected block slack for all 810;
- all `81` second-step policies following the bad first coordinate.

Exact checker SHA-256:
`e88b5c92112dffff9013fff2a5038cafaf19772c8e48e53fe50b43122d03178f`.

Captured stdout SHA-256:
`271b7359e1afde99b9fd712debada65373eb0b35202371e3cd5c7f250edeaf51`.

The finite computation certifies the explicit gate statement; the block identities (0.1), (1.1), and (1.2) are analytic consequences of the consumed account02/B16 theorem.

## 6. Status and next implication

**Full FEI remains OPEN / NOT PROVED.** This run closes one concrete uncertainty in the new signed-block programme: the certified arity-10 read-once-potential obstruction does **not** refute depth-two continuation. Quite the opposite, its bad first direction has a uniform second-step refund.

The next source-exact target is therefore to evaluate the same two-step block on the *actual replacement potential* rather than on `Gamma_0=0`, or to derive a universal structural condition forcing a two-step refund from the gate's cofactor geometry. Any such statement must retain the account02/B16 child continuation exactly; one-step sign conditions are already known to be too strong.
