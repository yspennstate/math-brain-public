# FEI: plan for the next few hours

From the 09-22 22:00 digest. Verified: FEI with constant C is equivalent to one inequality over gates of every arity with a symmetric, measure-only potential (d7e78e). Provisional: for read-once AND/OR/NOT formulas the sharp constant is numerically 6.4547837, Hod's β(1/2) (061ad9), with region 1 of its certificate verified (3fc42b); the GMP restriction step has sup ρ_0 ≥ C_FEI (162b16). Unverified: the percolation claim (eb59a4).

## Why restriction first, despite 162b16

An arity-n gate fed by dictators is an arbitrary function, so the gate equivalence restates FEI rather than reducing it; composition never touches shared variables, the real obstacle, and restriction does. Splitting f on a coordinate k into restrictions f_1, f_{-1} gives two exact identities:

    H(f) = ½[H(f_1) + H(f_{-1})] + J_k + ε_k,    I(f) = ½[I(f_1) + I(f_{-1})] + Inf_k,

since S∖{k} is distributed as the even mixture of the spectral laws of f_1 and f_{-1}. Here J_k, the Jensen–Shannon divergence of those laws, is at most (4/ln 2)·Inf_k because ‖f̂_1 − f̂_{-1}‖² = 4 Inf_k, and ε_k = H(1[k∈S] | S∖{k}) is the erasure entropy of k. By induction on n, FEI holds with C = c + 4/ln 2 once every Boolean function has a relevant coordinate with ε_k ≤ c·Inf_k; Han's inequality, Σ_k ε_k ≤ H(S), gives such a coordinate with c = C_FEI. So the best restriction step lies within 4/ln 2 of C_FEI, consistent with 162b16; its whole difficulty sits in ε_k, and one good coordinate per function suffices. Up to an additive O(Inf_k), ε_k = Inf_k · E[log(1 + f̂(S∖k)²/f̂(S)²) | k ∈ S]: deleting k from a typical spectral set containing it must not raise the coefficient by more than a constant factor, on log-average. For majority on an odd number of bits ε_k = 0: all weight sits on odd levels. These were derived while planning and are checked first.

## First concrete step (hour 1)

Verify both identities to machine precision on random functions with n ≤ 12 (fast Walsh–Hadamard). Then tabulate min_k ε_k/Inf_k and its minimizer for tribes, recursive MAJ3, Hod's lexicographic functions, random DNFs and random read-once formulas up to n ≈ 20. Does a simple rule (largest influence, first variable of the formula) find a good coordinate? How does the best step ratio (J_k + ε_k)/Inf_k behave along Hod's family, where its average over the recursion must approach 6.4547837? A family where every coordinate's ratio is unbounded is, by Han, a candidate counterexample, checked exactly first.

## Hours 1–3

Prove the lemma directly for read-once formulas with an explicit coordinate. Han plus O'Donnell–Tan already gives existence there, so only a direct proof tests the route. Then monotone functions: the derivative ∂_k f ≥ 0 and the average over x_k live on the complementary pivotal and non-pivotal sets, FKG is available, and restrictions stay monotone, so the lemma there would give FEI for monotone functions.

Meanwhile, stress-test the read-once potential Γ* on the 14 NPN classes of 3-input gates and the 222 of 4-input gates, over biased inputs. A gate that makes the enlarged value iteration diverge at 6.4547837 gives a composed family above Hod's bound, confirmed by brute-force transforms of an explicit function before being called a lower bound. Finish the certificate regions in the cancellation-keeping form of 3fc42b.

At hour 4 the numbers decide which route gets the remaining hours.

## What I would avoid

- Hypercontractive level-k arguments alone: they give the 2^{O(I log I)} concentration of Kelman–Kindler–Lifshitz–Minzer–Safra and no way past the log I.
- Coding S coordinate by coordinate independently (cost Σ Inf_i log(1/Inf_i), a log factor too much on majority), and decision-tree or subcube-partition bounds (Wan–Wright–Wu; Chakraborty–Kulkarni–Lokam–Saurabh), which exceed I polynomially on majority.
- Treating unbounded-arity composition as a reduction (d7e78e).
- Exhaustive search for large H/I at small n: extremizers need depth, which value iteration already reaches.
- Building on eb59a4 unchecked. A quadtree code (at each scale, which subsquares of each hit square are hit), with P(S∩B ≠ ∅) ≲ α_4(r,R) and α_4(1,r) ≥ r^{−2+δ}, appears to give O(R²α_4(R)) directly; I would test the note against that argument.

Nothing is marked verified until an independent computation reproduces it.
