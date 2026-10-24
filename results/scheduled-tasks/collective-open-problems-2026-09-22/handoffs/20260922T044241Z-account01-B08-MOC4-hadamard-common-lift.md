# MOC4 handoff — account01/B08 exact complex-Hadamard common lift

Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Run: `20260922T044241Z-b08-moc4-r12`  
Outcome: `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

Source-bound scientific artifact:
- private repository: `yspennstate/math-open-problems`
- report: `proofnet24/collective-MOC4/account01/B08/20260922T044241Z-b08-moc4-r12/REPORT.md`
- report blob: `f7391a0c2fdeaef6c5fac2bdfbca4513245e5abf`
- exact verification blob: `68eec174432c6acc0fa923ae65315f13715cda7f`

Named OTHER-account partner consumed: account02/B09 `MOC4-ZERO-FIBER-HAAR-LIFT-v1`, run `20260922T034112Z-account02-B09-MOC4-r14`, report blob `20a1ea240bb65b81b880cad265e4db5f225d2a8a`.

## New full-common-lift theorem on the complex-Hadamard locus

For

`U(z)=1/2 [[1,1,1,1],[1,z,-1,-z],[1,-1,1,-1],[1,-z,-1,z]]`, `|z|=1`, `r=Re z`, define zero-based permutation sets

`S+={0231,0312,1203,1320,2013,2130,3021,3102}`,

`S-={0132,0213,1023,1302,2031,2310,3120,3201}`.

Put

`nu_z(pi)=(1+r)/16` on `S+`, `(1-r)/16` on `S-`, and `0` otherwise.

Then for **every** equal-cardinality subset pair `I,J` and every exterior degree `k=0,...,4`, exactly

`|det U(z)[I,J]|^2 = Pr_{pi~nu_z}[pi(J)=I]`.

Hence for arbitrary complex spectra, including repeated/singular cases,

`det(D_a+U(z)D_bU(z)^*) = sum_pi nu_z(pi) prod_j(a_{pi(j)}+b_j)`.

The proof uses: uniform one-point marginals of both 8-state endpoint laws; every normalized two-minor is one of `0,1/4,(1+r)/8,(1-r)/8`; exact endpoint checks at `r=+1,-1`; affine interpolation in `r`; complementary-minor duality for degree 3; and Cauchy-Binet. By the standard order-four complex-Hadamard classification and monomial-equivalence invariance, this closes the entire `4 x 4` complex-Hadamard relative-unitary class.

The exact verifier checks all compound degrees for the nontrivial phase `z=3/5+4i/5`: weights are eight `1/10`, eight `1/40`, eight zero, and a generic Gaussian-integer spectra test gives exact determinant `-466/5+143i/5` from the same law.

## General determinant-relevant V4 glue

Let `P=|U|^2` and `R` be the exact complementary-pair doubly stochastic channel. Choose Birkhoff decompositions

`P=sum_pi lambda_pi P_pi`, `R=sum_rho mu_rho R_rho`,

where `rho:S4->S3` is the quotient by `V4`, and let `theta_rho=sum_{rho(pi)=rho}lambda_pi`. Then

`nu_pi=lambda_pi+(mu_{rho(pi)}-theta_{rho(pi)})/4`.

If every `nu_pi>=0`, these weights preserve `P`, replace the quotient-fiber totals by exactly `mu`, hence match the same true unitary's determinant-relevant `(D,R)` channels and give an exact positive 24-vertex determinant representation for all spectra. This is deliberately **not** claimed to reproduce every individual two-minor outside the complex-Hadamard theorem above.

With `p=min_ij P_ij` and `q=min_ab R_ab`, uniform-baseline Birkhoff decompositions give the explicit source-valid sufficient certificate

`8p+q >= 2  =>  MOC4 holds for this U for every complex spectra pair`.

Thus any strict-interior target counterexample must satisfy `8p+q<2` in addition to the lead's positive V4/pair reserve and all stationarity/odd-Weyl/biorientation constraints.

First unpaid implication: `MOC4-MAXIMIZER-V4-GLUE-v1` — on the remaining positive-reserve global-maximizer branch, either choose Birkhoff decompositions of the same true unitary's `(P,R)` making all canonical glued weights nonnegative, or close the support bound directly from the existing maximizer constraints. An arbitrary independent-bistochastic or generic fixed-unitary common-minor no-go does not count.
