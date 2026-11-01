# Plan: QFORM session, 2026-09-25

**Reading of memory.** All house results are unrefereed. I re-derive each one before I use it. What is claimed:
- Three hubs are bounded for any remainder (Thm 6.3).
- The single hub without diagonal is bounded for fixed m. It is at most C log m, uniformly in eps (3.17).
- The curved marginal U+cV² has density at most 8|c|^{-1/2} (5.1(a)).
- Hölder pairing reduces the single hub to an L^p(ds) mixed norm (p<2) of ρ_s, the density given X_0=s (5.3).
- A hub that sees P is bounded on window laws (5.5/5.6).
- The hub-diagonal lemma is unproved.

Gaps:
- (i) the log m factor;
- (ii) the hub diagonal (the "twist");
- (iii) the 0-hub and 2-hub cases. Their status is not visible in the 18 newest notes.

**What I try first, and why.** Make the single-hub bound uniform in m.
- Condition on X_0=s and complete the square inside the light block. Translation preserves "density ≤ 1", so ρ_s is the density of a translated light form plus a linear term. In the Gaussian limit, its singularities lie on an explicit critical curve u=u_s.
- Model: 2WsL+βL²+μV², with block [[0,W],[W,β]]⊕μ. With W=2, β=1, μ=−1 the eigenvalues are 2.56, −1.56, −1, so the model is admissible.
- In this model sup_u ρ_s=∞, because βμ<0 gives a log singularity at u_s. So no bound uniform in u exists. This may be what 3.17 pays log m for.

Target lemma, uniform in m:

  ρ_s(u) ≤ g(s)·(1 + log⁺ 1/|u−u_s|),  with ‖g‖_{L^p(ds)} ≤ C for some p∈(1,2).

The Gaussian limit predicts g ≲ min(|s|^{-1/2}, |s|^{-1}).
- The pairing integrates along u=t−as², where a is the hub diagonal (possibly 0). Boundedness then becomes transversality of that parabola to the critical curve.
- The three-eigenvalue hypothesis should quantify this. Near resonance, [[a,W],[W,β]] is nearly singular. Then the third large eigenvalue must come from a second transverse curvature, which smooths the log.
- This one framework covers both (i) and (ii), and generalizes 5.1(a).

**Build on.**
- Ball/Rogozin: 1-D marginals ≤ √2.
- Livshyts–Paouris–Pivovarov: k-dim marginals ≤ 2^{k/2}.
- Rudelson–Vershynin: linear images.
- Haynsworth inertia and interlacing, to count the large eigenvalues that survive Schur complements.
- House results 5.1(a), 5.3, 3.17 and 6.3, once re-derived.

Independent check of 6.3 by a "half-derivative ladder":
- A Schur pivot a≥1 gives sup_t E|Q−t|^{-α} ≲ a^{-1/2} sup_t E|S−t|^{-(α−1/2)}.
- Three rungs, with a log at α=½, reach a bounded density.
- Two pivot-hubs reduce in the same way to a log-potential bound for a light form with one large eigenvalue. That is my way into the 2-hub case.

The BGKS rank-two result is filed without proof. Check it before citing it.

**Avoid.**
- L¹ bounds on characteristic functions. Comb laws have density ≤1 but transforms that do not decay. The Fourier method was withdrawn, and the twisted frame integrals grow.
- The 2-D maximal functional of (L,P). It is unbounded on a spread frame (Ex. 5.2).
- Arguments that use only the joint density of the eigencoordinates. A bounded-density vector can sit on a thin shell at large radius, so the product structure must enter.
- Lindeberg, fourth-moment and random-submatrix routes. No moments are assumed, and angular decorrelation is still open.
- Discrete quadratic Littlewood–Offord. It was misquoted, and it gives small-ball bounds, not densities.
- Tuning the "hub that sees P" constants. Numerics show only a few per cent gain.
- Reducing to window laws. BLL does not cover quadric level sets, so the window-law results are evidence, not reductions.

**Schedule.**
- 0:00–0:45, audit. Read the proofs of 3.17, 5.1, 5.3 and 6.3, and the 40 older notes. Fix the case map by hub count, and find where log m enters.
- 0:45–2:30, target lemma. Do rank-one transverse R first (5.1(a) plus translation), then general light R.
- 2:30–3:30, resonance. Turn "three eigenvalues ≥1" into a lower bound on transversality.
- Then file provisional claims, including failures.
- Fallback, if comb laws break the pointwise-in-u form: bound ‖ρ_s(t−as²)‖_{L^p(ds)} directly, splitting on |sL| against the scale of R.

**First concrete step.** Take Q = aX_0²+2WX_0L+βL²+μV²+μ′V′², with L, V, V′ unit, spread and orthonormal.
1. By hand, compute u_s and ρ_s near u_s. Check the target lemma and the transversality integral against A's eigenvalues.
2. In parallel, evaluate ρ_s numerically with comb laws on the Example 5.2 frame.
3. Then read the proof of 3.17 to confirm where log m arises.

Realistic aim: either a uniform single-hub theorem or a sharp obstruction. The full conjecture would still need the 0-hub and 2-hub cases after that.
