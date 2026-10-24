# account03/B09 MOC4 handoff — external Saxl facets + spinor exclusion

Run: `20260922T051640Z-account03-B09-moc4-external-facets`  
Control revision: `2026-09-22.2` / `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Assignment: complementary `2 x 2` minor inequality applied to the lead determinant-support expression  
Named partner consumed: `account04/B07`, run `20260922T044421Z-account04-B07-MOC4-r12` (`MOC4-SPINOR-SINGULAR-VALUE-v1`, gaugewise `det N=0`)  
Status: `ESSENTIAL_STEP_APPLIED`; full MOC4 remains OPEN. `WITHOUT_VERIFIED_BRAIN`.

## New exact result

For a true `U in SU(4)`, the determinant support functional `ell_U` is normalized and nonnegative on every subset-assignment indicator `P_{I,J}` because `ell_U(P_{I,J})=|det U[I,J]|^2`. Drury 2004 Proposition 4.1 classifies the facets of the corresponding `Saxl_4` cone: the normalized dual base therefore has exactly the 24 evaluation functionals plus 48 distinct left-right translates of his external functional `u`.

In B09 `P-R-D` coordinates, the 48 non-Weyl functionals are indexed by `tau in S4` and either of the two pair-class permutations `rho'` deranging `rho_tau`:

`P_ext=(J-P_tau)/3`,  
`D_ext=E^T P_ext E / 4 = -W_tau/3`,  
`R_ext=R_{rho_tau}/3 + 2 R_{rho'}/3`.

If `B_rho(f)` is the four-point Klein-fiber mean, their exact action on any `Saxl_4` function is

`e_{tau,rho'}(f) = (2/3)(B_{rho_tau}(f)+B_{rho'}(f)) - (1/3) f(tau)`.

The Fraction verifier checks equality of these 48 signatures with the complete Drury-`u` orbit on all 53 `k=0,1,2` subset-indicator generators.

Hence every true-unitary support value satisfies

`h_eta(U) <= max( max_sigma f_eta(sigma), max_external e(f_eta) )`.

So any support direction with all 48 external values below its endpoint maximum is completely closed without stationarity/Hessian work.

## Direct application to current lead hard datum

For the lead's exact datum

`a=(-4+4i,-i,-3+2i,-4-4i)`,  
`b=(-4-4i,2-i,2-4i,4-i)`, `eta=1`,

the endpoint maximum is `M=256`, while the largest of the 48 external values is exactly `178`. Thus the support direction is closed for every true unitary with exact margin `78`. This removes the lead's previous `289/3` residual on that datum.

## Named-partner phase use

Applying account04/B07's gaugewise `det N=0` theorem to the 48 coordinate extremes: every external point has exactly 12 gauge/matching instances in which one determinant monomial has squared magnitude `1/27` and the other five are zero. Thus none of the 48 external normalized-Saxl extremes can be a genuine `Lambda^2 SU(4)` point. This is a true phase obstruction, not `P>=0` or arbitrary bistochastic data.

## Next exact obligation

`MOC4-EXTERNAL-SPINOR-PAYMENT-v1`: for a structured support datum where one or more external functionals exceed `M`, quantify the loss forced by the gaugewise `det N=0` equations so that no genuine point can retain enough mass near the exposed external face to exceed `M`. A genuine normal/unitary counterexample also resolves the branch; an arbitrary `(P,R)` or `SO(6)` mass witness does not.

Scientific artifact: `proofnet24/collective-MOC4/account03/B09/20260922T051640Z-account03-B09-moc4-external-facets/REPORT.md` in `yspennstate/math-open-problems`. Exact verifier and recorded output are adjacent.
