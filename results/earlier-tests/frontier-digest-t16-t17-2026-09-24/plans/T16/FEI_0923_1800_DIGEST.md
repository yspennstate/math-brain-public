# FEI: plan for the next hours

Full FEI in one session is unlikely; the hours go where a proof for every f could come from. Sanity bars for any argument: C ≥ 6.4548 (Hod, lexicographic functions) and, if Numaro's 18-variable K_{3,3} function checks, C ≥ 6.52 through H(g)/(I(g)−1) under recursive composition. Lexicographic functions are LTFs, so the LTF note's constant must be at least their H/I.

## Hours 0–1.5: audit what later work would lean on

1. The ρ_0 lemma (13:37), the only open route in the memory aimed at every f. Redo its computation independently and push it past exhaustive small n.
2. Percolation candidate F0090. The proof I expect: the multiscale chain rule H(S) ≤ log 2 + log 15 · Σ_B Pr[S∩B≠∅] over dyadic boxes, with Pr[S∩B≠∅] = E[Var(f | x outside B)] ≤ Pr[B pivotal] ≲ α_4(r,R) (three half-plane arms near the sides), quasi-multiplicativity and α_4(r) ≥ r^(−2+δ), so the sum is O(R² α_4(R)) = O(E|S|). Check the note against this (boundary and corner boxes too) and check what GPS problem 1 asks.
3. LTF and read-k notes: the constant bar and the irregular (large critical index) case.

## Hours 1.5–10: a one-coordinate restriction step

Let ΔH_i = H(f) − ½[H(f_{i→1}) + H(f_{i→−1})]. Since I(f) = Inf_i(f) + ½[I(f_{i→1}) + I(f_{i→−1})], induction on n gives FEI with constant C once every nonconstant f has some i with ΔH_i ≤ C·Inf_i. (GMP's ρ_0 may be exactly this.) ΔH_i is a sum over lattice edges (S, S∪i) of ψ(x,y) = φ(x²) + φ(y²) − ½[φ((x+y)²) + φ((x−y)²)], with x = f̂(S), y = f̂(S∪i), φ(t) = t log(1/t). ψ ≥ 0, is homogeneous of degree 2, vanishes if either coefficient does, is O(y²) unless |y| ≪ |x|, and is then ≈ y²[log(x²/y²) + 3]. So the drop term is everything: D_i f's spectrum must not sit, on average, where E_i f's is much heavier. For Boolean f the two have disjoint supports (the pivotal region of i, of measure Inf_i, and its complement): the setting of hypercontractive small-set bounds (level-k inequality, Talagrand's L1–L2). Majority gives ΔH_i = 0 exactly (odd levels only); rough hand checks give bounded ratios for biased thresholds and tribes.

Numerics first: the maximum over f of min_i ΔH_i/Inf_i, and of Σ_i ΔH_i/I (the averaged form), over all f with n ≤ 5 up to NPN and structured families to n = 22 (thresholds at every bias, recursive majority, tribes, lexicographic, read-once formulas, Numaro's function, random DNFs), plus a local search pushing the minimum up. A valid step constant is a valid FEI constant, hence ≥ 6.4548: small-n maxima below that prove nothing. A bounded sup means a proof attempt; a family where it grows kills the route, recorded as failed with its witness.

## Hours 10–20: decided by that result

If the step holds, the proof attempt continues. If it fails, test whether the witness also pumps H/(I−1) under composition, with the verified gate reformulation as the engine (gates of arity ≤ 4 exhaustively, plus graph-property gates like Numaro's); a ratio growing with arity would be the first real evidence against FEI. If the witness does not pump it, take the multiscale bound to other structured classes; it also gives FEI for majority (balanced tree, level sums ≍ √(n/b)).

## Avoid

Level counting and subadditivity Σ h(Inf_i): they stop at I log n. Attacking KKLMS's log I factor head-on: the step inequality, if true, bypasses it. Redoing composition or read-once: done (sharp at 6.4548 numerically), and the gate reformulation at unbounded arity is FEI restated. The multiscale bound as a general proof: on tribes of random overlapping parities it pays about log n per element while H ≪ I.

## First step

Read claim_dc05672a84f74b44a1f15207c0cf86e0 and GMP's statement of the key inequality. Then one script: a fast Walsh–Hadamard transform per function, ΔH_i straight from f̂ through the edge formula (O(n 2^n)), coefficients checked exactly for n ≤ 10, laptop CPU only, printing both ratios for the families above. Every result, dead routes included, goes to the math memory as it lands, marked verified or provisional.
