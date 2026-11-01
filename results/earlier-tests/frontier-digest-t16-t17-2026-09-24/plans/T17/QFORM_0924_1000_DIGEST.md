# QFORM — research plan, session 2026-09-25

**Framing.** The owner wants the full conjecture. It is open, so this session targets the step blocking a complete proof on the house map. Every digest item is house/unrefereed. I treat each as a lead and record nothing as proven until I've checked it line by line.

## Build on (after re-checking the proofs)
- House results:
  - spread case (Lemma 1.1, from the corrected Fourier note);
  - ≥3 hubs, any remainder (Thm 6.3);
  - curved marginals (Prop 5.1(a));
  - a hub that sees P, under window laws / bounded partner coordinates (Props 5.5, 5.6).
- External:
  - Livshyts–Paouris–Pivovarov: rank-2 projections of product laws with densities ≤ 1 have density ≤ 2;
  - Weyl's inequalities;
  - the bathtub principle.

**The obstruction: single hub, no hub diagonal.** It's O(1) for a fixed number m of light coordinates and O(log m) in general (Prop 3.17). The hub-diagonal case has only a provisional lemma with no proof. Two hubs don't appear in the digest. I must confirm that the spread/1/2/≥3-hub split is exhaustive with uniform thresholds; otherwise a "full proof" has a hole.

## Avoid
- **2-D maximal functional of (L,P):** Example 5.2 makes it unbounded on a spread frame while every curved marginal is bounded.
- **Twisted frame integrals:** they grow numerically while the density stays bounded, so they're lossy.
- **Refining "the hub sees P":** only a few per cent once the bias is removed; no route to removing a log.
- **Decoupling / quadratic Littlewood–Offord / Carbery–Wright:** they lose a square root or a power of δ, which is incompatible with a density bound.
- **Fourth-moment row-submatrix line:** the conjecture has no moment hypothesis, and the third-moment weakening is refuted.

## Try first (≈2–3 h): remove the log, the nearest miss
Write Q = X₀L + P with L = ⟨w,X′⟩ and P = X′ᵀBX′. Let f₀ be the density of X₀. Then f_Q(t) = E[f₀((t−P)/L)/|L|], a pencil average of law(L,P) over lines through (0,t). I expect Prop 3.17 pays O(1) for each dyadic scale |L|~δ between 1 and the light-coordinate size. What's needed is summable decay of T_δ = E[f₀((t−P)/L)/|L|; |L|~δ].

T_δ ~ 1 on many scales roughly needs P−t = O(|L|) near {L=0}, i.e. P−t ≈ L·M: the two-eigenvalue product structure. The third eigenvalue forbids this quantitatively:
- With A₀₀ = 0, A = R + (0 ⊕ B′), where rank R ≤ 2 and B′ = Π_{w⊥}BΠ_{w⊥}. Weyl then gives ‖B′‖ ≥ 1.
- On {L=0}, Π_{w⊥}∇P = 2B′X′. So there the Jacobian of (L,P), |w|·|Π_{w⊥}∇P|, degenerates only where B′X′ is small.
- The top eigenvector u′ of B′ is orthogonal to w, so by LPP, Pr(|L|≲δ, |B′X′|≤η) ≲ δη.

Steps:
- (i) Prove a scale lemma: T_δ ≲ δ^α + δ⁻¹Pr(|L|≲δ, |B′X′|≤δ^β). Method: condition outside a block S of light coordinates seeing both w and u′ at scale δ, then use coarea on R^S.
- (ii) By LPP the defect term is ≲ δ^β, so the scales sum.

Step (i) is the whole difficulty: coarea gives fibre integrals, not expectations, and u′ may be thin on S. A failure should show what a counterexample looks like.

## Interleaved falsification (≤1 h)
Pr(Q∈I) is affine in each f_i, so by the bathtub principle each X_i may be taken uniform on a set of measure 1: unions of intervals, not only windows. The recorded numerics are on spread frames. I'll maximise f_Q(t) over (w, B, t, sets) for m = 8…512:
- integrate the hub exactly and check estimator bias (one correction already);
- seed at P−t ≈ L·M, under the three-eigenvalue constraint.

If I see log m growth, I switch to proving a lower bound, i.e. disproving the conjecture. The same reduction might also drop the window-law hypothesis in Props 5.5/5.6, if the relevant conditional kernels have interval super-level sets.

## First concrete step (≈45 min)
Read in full:
- Prop 3.17 and its fixed-m precursor (claim_e212…, claim_36a3…);
- Example 5.2.

Pin down the exact inequality that costs O(1) per scale, and the frame property Example 5.2 exploits. The main line assumes that inequality is the one I expect. If it isn't, I re-plan before anything else.
