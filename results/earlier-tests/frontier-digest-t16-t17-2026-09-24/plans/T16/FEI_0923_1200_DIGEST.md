# FEI: plan for the next few hours

FEI has been open since 1996; the memory holds special classes and a reformulation, nothing general. I do not expect a proof in one sitting, so each block ends in something checkable (an audited status, a verified obstruction or a proved lemma), filed back to the math memory with its status, dead routes included.

## 1. Audit before building (up to an hour)

Two provisional claims are extraordinary: FEI for all LTFs (claim_4fdc5a79) and for read-k DNFs, regular functions and their compositions (claim_9d2c6095). As far as I know FEI for LTFs is open (random LTFs only, Chakraborty et al. 2018). I will tag every step: exact; approximation with the discarded part's entropy bounded; approximation without that bound; reliance on another provisional note. The third kind is the standard leak: weight ε dropped in L2 (junta, critical index, Berry-Esseen, level truncation) can carry about ε·n bits. A per-coordinate charge of Inf_i·log(1/Inf_i) is as fatal, since tribes has Σ Inf_i log(1/Inf_i) of order I·log n. Each gap gets a smallest family where it could bite, computed exactly. I also recompute H/(I−1) for Numaro's 18-variable function and fix the log base; every constant below is calibrated against it.

## 2. The pivot step (about two hours)

Disjoint composition is understood: O'Donnell-Tan's composition theorem, and read-once value iteration landing numerically on Hod's 6.4548. Numaro's function, if step 1 confirms it, says the extremizers are not read-once. The verified gate reformulation (claim_d7e78ede), as summarized, has a potential seeing only the inputs' measures, which fits independent inputs; the pivot f = MUX(x_i, f_+, f_−) is a gate whose two inputs share every variable. With P_± the spectral distributions of f_±, a, b their coefficients, M = (P_++P_−)/2 and h binary entropy:

    H(f) = ½[H(f_+)+H(f_−)] + JS(P_+,P_−) + E_{S∼M} h(r_S),  r_S = (a_S−b_S)²/(2(a_S²+b_S²))
    I(f) = ½[I(f_+)+I(f_−)] + Pr[f_+≠f_−]

Plain induction needs, for every f, a coordinate with JS+E h ≤ C·Pr[f_+≠f_−]. That would prove FEI, so I expect it to fail, and the failures are the data. My estimate, to confirm exactly: when f_± differ on a small subcube inside a spread spectrum the left side is about Inf_i·log(1/Inf_i), paid for only by the slack C·I−H such spectra carry. So the object is a potential Ψ ≤ C·I−H, zero on constants, that some pivot preserves. Compute every pivot deficit for all functions on ≤5 variables (up to symmetry) and for tribes, majority, iterated compositions and Numaro's function; then search by LP (MILP when the pivot is free) for the best Ψ in growing families: bias only, bias plus level-1 weight, bias plus maximal influence. If no bias-only Ψ works, that is a verified obstruction, and the failures show what Ψ's second argument must see.

## 3. The GMP key inequality (about an hour)

Its restriction-step constant ρ_0 (claim_56de35f4) goes on the same testbed, next to the random-restriction form of the step, which avoids per-coordinate charges. For a p-random live set J, with S the spectral sample and MI mutual information:

    H(f) = E_z H(f_{J,z}) + MI(Z;S∩J) + H(S∖J|S∩J),  E I(f_{J,z}) = p·I(f)

If the testbed pushes ρ_0 past what the approach needs, the route is closed as it stands and I record why. If it survives, it becomes the main line for the rest of the twenty hours, attacked first where the data show it tight.

## Avoid

L2 approximation without entropy accounting (where Friedgut-type arguments and Kelman-Kindler-Lifshitz-Minzer-Safra stop, at 2^{O(I log I)} concentration); per-coordinate Inf_i·log(1/Inf_i) charges; more read-once or disjoint-composition work, which cannot reach the extremizers; lower-bound hunting, which does not bear on truth; the unverified percolation note as a foundation.

## Build on

O'Donnell-Wright-Zhou (symmetric functions, read-once decision trees); O'Donnell-Tan; KKLMS; the composition identity H(f∘g) = H(f) + I(f)·H(g) for balanced g (behind Hod's bound; it explains the ratio H/(I−1) and why a bias potential appears); the verified read-once machinery in memory as the search engine.

## First step

Open claim_4fdc5a79 with math_note.py, tag every step as in section 1, and turn the first unbounded leak, if any, into a candidate family with exact H and I.
