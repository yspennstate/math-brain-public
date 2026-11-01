# FEI plan — session of 2026-09-24

**Aim for these hours.** FEI has been open for 30 years, so a full proof in a few hours is unlikely. The deliverables are:
- (a) re-checked versions of the frontier claims I would lean on;
- (b) one local reformulation, made rigorous and checked by machine;
- (c) a focused attack on the regular case.

Every output will be labelled proved, numerical or open.

**What I build on (after re-checking it)**
- The verified equivalence between FEI and a gate inequality with a potential (d7e78…).
- A structural fact: the extremal families are deep read-once compositions, so they are highly *regular*. These are Hod's recursion and Numaro's K_{3,3} + coins, where H/(I−1) → 6.5218.
- The house reduction to small-influence functions (201fff…, no proof). Also the Gonzalez–MacManus–Pereyra (GMP) restriction step (dc05…), where sup ρ₀ ≥ C_FEI. I will re-derive both rather than cite them.
- From the literature: the O'Donnell–Tan composition theorem, KKLMS 2020, and the fact that tensorization removes additive constants.

**What I try first: an exact one-coordinate splitting identity.** Notation:
- S ~ f̂², with law p;
- p± are the spectra of f_{i→±1};
- τ_i(S) = S Δ {i}.

I conjecture the following identity (checked by hand on AND₂ and Maj₃):

  H(f) − ½[H(f_{i→1}) + H(f_{i→−1})] = JS(p₊, p₋) + [1 − JS(p, p∘τ_i)].

The bracket equals the erasure term Er_i = H(1[i∈S] | S∖{i}) ≤ h(Inf_i). If the identity holds, two things follow.

1. **The JS term is linear in influence.** A Hellinger bound gives JS(p₊,p₋) ≤ (1/(2 ln 2))·‖f̂₊ − f̂₋‖² = (2/ln 2)·Inf_i.
   - So splitting on coordinate i costs at most (log₂(1/Inf_i) + 4.33)·Inf_i.
   - The small-influence reduction then costs log(1/δ) instead of 1/δ.
   - Splitting any coordinate with Inf ≥ ¼ already costs less than 6.52.
2. **FEI becomes a local "erasure" inequality.** Fix the variables one at a time in a uniformly random order.
   - The splitting costs add up to H(f).
   - The influences, each taken when its variable is fixed, add up to I(f).
   - Erasure entropy is at most entropy. So FEI is equivalent, with C shifted by at most 2/ln 2, to

     Σ_i H(1[i∈S] | S∖{i}) ≤ K·E|S|.

   - This statement is local on the edges of the Fourier cube. Only pairs with f̂(T∪i)² ≪ f̂(T)² cost more than O(Inf_i). Those pairs are exactly the log(1/Inf) loss that every splitting argument runs into.

*Why this comes first:* it is cheap to verify exactly, and it loses nothing, since it is equivalent to FEI up to an additive constant. It also pins the whole difficulty to one local term.

**Steps**
1. **First concrete step (~45 min).**
   - Read notes 201fff…, d7e78… and dc05… in full.
   - Write a fast Walsh–Hadamard checker. With it, verify the identity, the JS bound and the telescoping sum exactly on all 2¹⁶ functions of 4 variables. Also run it on random and structured functions (Maj, Tribes, AND/OR recursions, LTFs) up to n ≈ 14.
   - Record the largest values of Σ_i EI_i/I and Er/I, where EI_i is the splitting cost on the left-hand side of the identity.
   - Check whether the GMP ρ₀ step is this local inequality. If it is, then sup ρ₀ ≤ C_FEI + 2/ln 2 as well.
2. **Write proofs.** Write rigorous proofs of the identity, the sharpened reduction and the erasure equivalence, marked house/unrefereed.
3. **Calibrate.**
   - Derive how Er behaves under composition. I expect it to behave like H: Er(g∘f) ≈ I(g)·Er′(f) + a gate term.
   - Compute K_Er, the best K in the erasure inequality, on Hod's and Numaro's families.
   - This shows how the 6.52 splits between the JS part and the erasure part, and which bad pairs carry it.
4. **Attack (rest of the session): prove the erasure inequality for δ-regular f.**
   - Set α = Ê_i f and β = D̂_i f. E_i f and D_i f have disjoint supports and (E_i f)² + (D_i f)² = 1, so α∗β = 0 and α∗α + β∗β = δ_∅.
   - The bad term is Σ_{β_T² < α_T²} β_T² log(α_T²/β_T²).
   - One tool is Donsker–Varadhan with level or noise test functions.
   - Another is the potential Γ(μ) from the gate formulation, which is now needed only per coordinate. I will search for a single Γ that certifies every gate of arity ≤ 4 (222 NPN classes, meaning classes up to negating or permuting inputs and negating the output) on a grid of product measures, and sample gates of arity 5.
   - A failure is still useful: it shows which structure forces the log.

**What I avoid, and why**
- **Decision-tree and level-counting bounds** (Σ h(Inf_i), log C(n,k)). They lose a log n factor exactly on regular functions, and that is where the extremal functions live.
- **KKLMS-style hypercontractive concentration.** Its log I loss appears built into level-d estimates, and there is no known fix.
- **The percolation / Kalai Conjecture 8 thread and the withdrawn ρ₀ notes.** The candidate proof in that thread was refuted, and the thread is off target anyway.
- **Improving the 6.52 lower bound.** It does not bring a proof closer.
- **Building on house claims that have no proof** (LTFs, read-k DNFs, threshold gates) before reconstructing them. Until then they are test cases only.
