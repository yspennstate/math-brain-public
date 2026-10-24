# account03/B07 MOC4 handoff — Drury upper-facet reduction

Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Status: **ESSENTIAL_STEP_APPLIED / MOC4 OPEN**  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

## Canonical scientific artifact

`proofnet24/collective-MOC4/account03/B07/20260922T010550Z-account03-B07-MOC4-r11b/REPORT.md`

Report commit: `d88d24810cbff886676fd38134b24233050c0314`  
Report blob on readback: `3671449a3da3b009195454dedc4489e678c1dfd1`  
Archive head observed after report/verifiers: `245eb4f12482729fa2773f77d846e10e71314a71`.

Exact verifiers in the same run directory:
- `verify_determinantal_cylinder.py` / `VERIFICATION.txt`
- `verify_drury_orbit.py` / `DRURY_ORBIT_VERIFICATION.txt`

## Exact reduction

For `U in SU(4)` define

`mu_sigma = sgn(sigma) product_i u_{i,sigma(i)}`.

Then `sum mu_sigma=1`, and for every equal-cardinality `I,J`,

`sum_{sigma(I)=J} mu_sigma = |det U[I,J]|^2 >= 0`.

Also

`det(D_a+U D_b U*) = sum_sigma mu_sigma v_sigma`.

Let `F(sigma)=Re(eta v_sigma)`, `M=max F`, `g=M-F`. Drury's Proposition 4.1 gives the exact n=4 cylinder cone `Gamma`; its only non-coordinate facets are the left-right orbit of one exceptional functional `u`. Since `g>=0`, all coordinate facets are automatic. Therefore a sufficient condition for full MOC4 is the purely spectral finite family

`u(F_{rho1,rho2}) <= M` for every `rho1,rho2 in S4`.

There are exactly 288 distinct coefficient functionals in this 576-pair orbit. If these inequalities hold, `g` is a nonnegative cylinder combination, so

`M-Re(eta det)=sum t_IJ |det U[I,J]|^2 >= 0`

for every unitary. No common positive `(P,R)` lift is used.

One explicit form is

`3u(f)=f(2134)+f(3214)+f(1432)+f(4321)-f(1234)`.

## Historical placement

Drury (2004) proves the lower exceptional-facet inequality under a positive lower normalization, which yields preservation of half-spaces excluding the origin and his radial-hull corollary. The unpaid statement above is the complementary upper-max facet inequality needed in the origin-containing support regime. This cleanly isolates why the 2004 theorem stops short of full n=4 MOC4.

## Exact no-go boundary

The nonnegative Saxl function

`s = 1_{sigma(1)=2}+1_{sigma(2)=4}-1_{sigma({1,3})={2,3}}+1_{sigma({1,4})={3,4}}`

has values `0,1,2` with counts `13,10,1`, is an extreme ray of the full nonnegative identity-vanishing Saxl cone, yet the account04/B09 rational orthogonal unitary gives exact determinantal expectation `-224/15625`. Therefore arbitrary nonnegative Saxl functions are not enough; the OM spectral structure of the upper-facet inequality is essential.

## Next exact implication

Attack `MOC4-DRURY-UPPER-FACET-v1`: for every complex spectra/support direction prove `u(F_{rho1,rho2}) <= max_sigma F(sigma)` for the 288 distinct exceptional facet representatives. Use Drury's ten equivalent formulas and OM-root/cross-ratio factorizations; do not reintroduce the refuted unrestricted common `(P,R)` lift.

Assigned partner result consumed in this run: account04/B08 `MOC4-GENERIC-STRICT-SUPPORT-v1`.
