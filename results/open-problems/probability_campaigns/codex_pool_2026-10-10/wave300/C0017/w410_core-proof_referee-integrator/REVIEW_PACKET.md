# C0017 referee packet — w410, 2026-10-10

## Scope and source status

Working target: Bernoulli bond percolation on square-lattice edges at p=1/2, in Dobrushin domains, with convergence of the exploration path to chordal SLE6 and Cardy crossing limits. This is the historical C0017 intake formulation, not a certified current open problem. Wang Zhou, arXiv:2409.03235v6, Theorem 2 and Corollary 1.1, explicitly claim the single-interface result under Caratheodory domain convergence and Condition C. The older Tsai–Yam–Zhou arXiv:1112.2017v5 explicitly calls itself preliminary after critical comments. Ioan Manolescu, arXiv:2502.08394, Conjecture 5.1, presents the stronger full-plane nested CLE limit as conjectural and Theorem 5.2 establishes rotational invariance. Current resolution of the narrower target remains UNKNOWN here: neither the 2024 preprint proof nor a full 2026 status survey has been refereed in this packet.

The original Garban–Steif note, arXiv:1102.5761, Chapter II Section 4, PDF page 26 (P25), calls conformal invariance on square-lattice p_c=1/2 a challenge. It does not give the intake's combined Cardy/SLE6 wording in that sentence. The intake is a sharpened working target, and Zhou's Theorem 2 gives its narrower single-interface primary claim.

## Verdicts

| Peer item | Verdict | Independent reproduction | Limit |
| --- | --- | --- | --- |
| w408-S1.1 source-status | KEEP | arXiv:2409.03235v6 abstract and PDF Theorem 2 indeed make the claim, with Condition C. | A proof claim is not a checked proof or accepted resolution. |
| w408-S1.2 local L1 | KEEP | `D f=C'(u)(1-u)/y`, `D²f=-(2/3)C'(u)(1-u²)/(u y²)`, `A f=-3D²f`; inversion of one martingale gives semimartingale W. The two signed-measure identities subtract to `(1/Y1-1/Y2)(dQ-6dt)=0`, hence `dQ=6dt` and `dV=0` on separated stops. | No square-lattice Cardy approximation or path tightness is supplied. |
| w408-S1.2 global wording | FIX | Replace 'a countable covering family' by explicit stopping times `tau_n` for marks `(n,2n,3n)` with `tau_n -> infinity` a.s. For example, stop at time n or when `|W|=n/4`, any marked gap is `n/2`, or `Y2=4n`. Continuity of W and the real Loewner ODE show that for each finite T, all conditions survive to T for large n. An increasing localization can be obtained from tail infima of `tau_n`. | The underlying conditional result survives; its global localization should be stated as a stopping-time argument, not a future-dependent pathwise choice. |
| w408 L2 residual identities | KEEP | With `r_i=dR_i/D_i` and `q=dQ-6dt`, Ito gives `r_i=-dV-(s_i/3)q`. Solving the two equations gives exactly the formulas in ATTEMPT.md; the total-variation inequalities follow from `D_i>=d_min`, `s_i<=s_max`, and `s_1-s_2>=lambda`. | Actual lattice drift-measure control is absent; uniform small observable error does not imply small drift variation. |
| w408 L3 transfer | KEEP with stated assumptions | Bounded martingale increments times bounded continuous cylinder functions of the joint past have zero expectation; joint uniform-law convergence passes this to the limit, and a monotone class gives the natural-filtration martingale property. | Stopping-time convergence, curve/driver compatibility and the Cardy approximation are prerequisites. |
| w409-C0017-001 scalar functions | KEEP | For `h_alpha(r)=1/(1+r^alpha)`, direct substitution gives `h_alpha(r)+h_alpha(1/r)=1`; derivative is negative, and `h_1(2)=1/3`, `h_2(2)=1/5`. | These are abstract scalar functions, not percolation laws. |
| w409-C0017-002 cell defect | KEEP | For an oriented counterclockwise square cell, trapezoidal integration of `f(z)=conjugate(z)` is exact on each edge and gives `2i delta²`. There are `delta^-2` cells, so their sum and the exterior contour integral are `2i`; the uniform limit is not holomorphic. | This diagnoses an invalid local-to-global inference only; no percolation observable is modeled. |
| w409-C0017-003 contour reduction | KEEP | Exact interior-edge telescoping turns the summed defects into the boundary integral. Compact-uniform nodal convergence and bounded perimeter pass to each rectangle. Vanishing rectangle integrals give a local primitive by horizontal-then-vertical path integration; its derivative is `f`, so `f` is holomorphic. | The signed summed-defect estimate for the actual square-bond observable is absent. |
| w408 L4 wrong-variance one-test family | KEEP | Local SDE coefficients are smooth away from collisions. For bracket `kappa dt`, Ito gives residual divided by `Df` equal to `-beta+(6-kappa)(1/X+1/Y)/3=0`; the second mark has residual `(6-kappa)(1/Z-1/Y)/3`, nonzero on separation. | This is a counterexample to using only one test, not to C0017. w410-S1.2 is an independently derived explicit `kappa=0` subcase. |
| w408 L5/L6 diagnostic counterexamples | KEEP | Alternating `1/n` errors across `n²` steps have total variation `2n`; for `W_t=Zt` with fair sign, the sign is revealed at any `s>0`, giving nonzero conditional drift. | Neither is a percolation model. |

## Single hardest load-bearing input

Produce two square-lattice Dobrushin crossing/exit Doob martingales, corresponding to distinct right boundary marks, that converge jointly and uniformly on separated stopped slit domains to the appropriate Cardy functions of the Loewner cross-ratios. The event orientation and boundary convention must be fixed. Joint driver/marked-point tightness, filtration compatibility and curve-to-driver passage are also required. This input contains the conformal information. RSW, rotational invariance, and product independence do not themselves establish it. A KEEP for w408's conditional reduction does not solve C0017.

## Corrected prior attempt

C0017-A001 at `probability_1000_intake_claude_20260907/attempts.jsonl:17` states q=1 parafermionic spin `sigma=2/3`. Duminil-Copin, arXiv:1208.3787, Definition 3, defines the standard convention by `sin(sigma*pi/2)=sqrt(q)/2` with `sigma in [0,1]`. Substituting q=1 gives `sigma=1/3`. Zhou's arXiv:2409.03235v6 equation (1) likewise has `exp(i W/3)`. Verdict: FIX the source row by the supplied one-occurrence diff. This is a notation-level factual correction and carries no proof of the parent problem.

## New referee request

w413 should independently check w410-S1.2 in ATTEMPT.md. Test the initial conditions, both real Loewner ODEs, `X/Y=u`, the time restriction `T<ab/4`, and the deterministic driver's nonzero drift and zero quadratic variation. The claim is a proved special-case counterexample pending independent review, and is not a percolation counterexample.

## Reproduction pointers

- w408: `~/brain_workers/w408/ATTEMPT.md`, Lemmas L1–L3 and its missing-input section.
- w409: `~/brain_workers/w409/ATTEMPT.md`, independent scalar and cell-defect obstructions.
- Own calculation: `ATTEMPT.md` in this folder.
- Primary statements: https://arxiv.org/pdf/2409.03235 (PDF page 6); https://arxiv.org/abs/1112.2017 (author notice); https://arxiv.org/html/2502.08394 (Conjecture 5.1 and discussion after Theorem 5.2).
