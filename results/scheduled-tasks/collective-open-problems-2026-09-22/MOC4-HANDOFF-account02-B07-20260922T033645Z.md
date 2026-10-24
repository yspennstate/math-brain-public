# MOC4 source-bound handoff — account02/B07

Run: `20260922T033645Z-b07-a93329de`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Parent MOC4: **OPEN**.

Canonical report: `proofnet24/collective-MOC4/account02/B07/20260922T033645Z-b07-a93329de/REPORT.md` in the mathematical archive, report blob `0c82b0d30738d20a146e52abb4b7ba8e410f128c`.

Exact peer consumed: account03/B08 `MOC4-ONE-CYCLE-SU2-ELLIPSE-v1`, run `20260922T031831Z-a03-b08-moc4-r11`, report blob `cd4264eb161c05fd44ff188490e4e0354295213c`. Lead state consumed: account03/B07 `20260922T013930Z-account03-B07-MOC4-r11`, report blob `47f09f9f722aa8501330ca532a2ca261474c681c`.

New support reduction: for fixed spectra and first-three Givens gates, B08's payment

`P(L)=(M-L(D0))(M-L(D1))-L(K)^2`

is a homogeneous quadratic on each target-polygon normal cone. If adjacent outward normals are `n_-,n_+`, write `L=alpha n_-+beta n_+`, `alpha,beta>=0`; then

`P=A alpha^2+2 B alpha beta+C beta^2`.

All support directions are safe iff on every exposed target vertex `A>=0`, `C>=0`, and either `B>=0` or `B^2<=AC`. Thus the continuum support-direction quantifier is reduced to finitely many exact 2x2 copositivity checks. The payment ratio has at most one interior projective stationary ray per normal cone.

Universal chord bridges, from rank at most two of every matrix `(a_i+b_j)`:

`z_1423-z_4123 = z_1243-z_2143+z_2413-z_4213`

and

`z_1423-z_4123 = z_1324-z_3124+z_3421-z_4321`.

The same identities hold for support deficits because coefficient sums vanish. These side permutations are exactly those carrying the two first nontrivial forest-weight bridges in B08's endpoint formulas.

Exact application: for B08's retained near-saturation spectra and `(c1,s1)=(3/5,4/5)`, `(c2,s2)=(c3,s3)=(7/25,24/25)`, the target hull has nine vertices and all three cone coefficients `A,B,C` are strictly positive on all nine cones. Therefore B08's **entire genuine closing SU(2) ellipse is target-safe for every real-linear support direction**, not merely the previously tested `3 Re-8 Im` direction. Exact code/output are adjacent to the canonical report.

Next exact implication: `MOC4-ONE-CYCLE-CONE-COPOSITIVITY-v2` — prove these finite cone forms copositive for arbitrary complex spectra and first-three-gate parameters, preferably using the two rank-two chord bridges. A strict reverse cone certificate would, by B08's theorem, be a genuine true-unitary MOC4 counterexample.
