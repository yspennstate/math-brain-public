# QFORM research plan (2026-09-25 session)

**Aim.** A full proof this session is unlikely. Target: reduce the open core to one sharp lemma with every reduction proved, then attack that lemma. House results are unrefereed and get checked before use.

**Memory.** Claimed: three hubs; two hubs whose remainder crosses a split; spread hubs; free blocks; curved marginals. Open: a single hub on spread frames. Dead: the (L,P) maximal functional (Ex. 5.2), frame norms and twisted integrals (they grow), hub-sees-P (a few per cent).

**Try first: use only the Schur complement.** If A₁₁ = a ≥ c (otherwise use −Q), then Q = a(X₁+L/a)² + W with W = X′ᵀSX′ and S = A′−bbᵀ/a. Conditioning on X′ and using only f₁ ≤ 1:

  f_Q(t) ≤ a^{-1/2}·E(t−W)₊^{-1/2} ≤ a^{-1/2}(1 + ½∫₀¹ s^{-3/2}ψ_W(s)ds),  where ψ_W(s) := sup_t P(W∈(t−s,t]).

S⁻¹ is a principal block of A⁻¹, so Cauchy interlacing leaves W with at least two eigenvalues of modulus ≥1. *Why first:* Ex. 5.2 shows the joint law of (L,P) can blow up while every curved marginal stays bounded. This route needs only the 1-D law of W. It also gives a three-level induction on the number of large eigenvalues, not on n, so the constants cannot compound:

- **H1** (≥1 large eigenvalue ⇒ ψ ≲ s^{1/4−}): with a diagonal hub, condition directly and get √s. Otherwise decouple: P⁴ ≤ P(|2Z_IᵀA_IJZ_J| ≤ 4ε) ≲ ε log(1/ε), since a small diagonal forces ‖A_IJ‖ ≳ 1 for some split.
- If W has a diagonal hub, then ψ_W ≲ s^{3/4−} by H1 at the vertex. That is enough.
- Bilinear hub (|A_jk| ≥ 2c with a small diagonal, so the 2×2 block is indefinite): conditional small ball ≲ s·log(e/s) and conditional density ≲ 1+log(1/|t−vertex|), uniformly in the vertex (**to verify**). With H1 this settles W, and it settles Q itself at level 3.

What remains are entrywise-small forms (‖A‖_max < 2c):
- **S2**: two eigenvalues ≥1 ⇒ ψ ≲ s^{1/2+η}. Even √s·log^{−1−δ}(e/s) would suffice.
- **S3**: three eigenvalues ≥1 ⇒ bounded density.

The house core should be S2. One decoupling step should already give √s there, so the real obstruction is a **square-root barrier**: gaining a factor of log^{1+δ}.

**Steps.**
1. (~45 min) Write out and check, with constants:
   - the Schur bound;
   - interlacing (perturb if A is singular);
   - the bilinear-hub bounds, uniformly in t (no moments are assumed, so watch for heavy tails);
   - H1.

   Then read the open-core note and verify Thms 6.3, 6.5 and Props 3.13–3.15, 5.1, 6.9. Check whether they already give S3. If they do, everything reduces to S2.
2. (~45 min) Numerics. The density is multilinear in the fᵢ, so by the bathtub principle each Xᵢ can be taken uniform on a measure-one set. Search for worst cases of ψ_W for the Schur complements of the Ex. 5.2 frame and of the spread frames. I expect a slope of about 1 (with a log). A slope near ½ kills this route, and the fallback is the joint (L,W) law.
3. (~2 h) Attack S2 by two routes.
   (a) Block hub: find a coordinate block whose conditional form has one dominant direction, and prove the hub profile P(∈(u−ε,u]) ≲ min(√ε, ε/√u) via Props 6.9/5.1. Averaging against H1 at the vertex then gives s^{3/4−}.
   (b) Decoupling that keeps the event: in the (U_J,V_J)-plane, E∧E′ is a strip of width ε/|w| crossing a hyperbolic shell. Transversality should give ε²·polylog instead of ε. The risk is the small-eigenvalue remainder.
4. Then S3 via block hub + S2. Record every outcome in memory with an honest status, failures included.

**Build on:**
- the Livshyts–Paouris–Pivovarov, Ball and Rogozin marginal bounds;
- P(|UV−t|≤ε) ≲ ε log(e/ε) for independent U, V;
- Costello–Tao–Vu decoupling;
- the Banks–Garza-Vargas–Kulkarni–Srivastava rank-two bilinear density (check the citation);
- Haynsworth inertia;
- house Props 5.1, 6.9 and Thms 6.3, 6.5, once checked.

**Avoid:**
- (L,P) maximal functionals: Ex. 5.2 already shows they can blow up.
- Frame-norm pairings: they grow numerically.
- Tuning hub-sees-P: a few per cent at best.
- Fourier decay: bounded densities give no pointwise decay, and the uniform claim was withdrawn.
- Decoupling as the *final* step: it loses exactly the critical √.
- Moment, CLT or operator-norm tools: there is no moment hypothesis.
- The row-submatrix thread: off the path and partly refuted.
- Coarea with 2-D densities alone: hyperbolic shells have infinite area.

**First concrete step:** prove the Schur bound and the interlacing lemma with explicit constants. Then restate the house's open core in Schur form and confirm that it is S2.
