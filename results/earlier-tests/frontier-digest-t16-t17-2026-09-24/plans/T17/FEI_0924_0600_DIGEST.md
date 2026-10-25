# Research plan — FEI session, 25 Sep 2026

**Target.** A full proof in a few hours is unlikely. I'll attack the open core the memory marks "not yet": FEI for all monotone functions. That class holds the record examples (Hod's read-once iterates at 6.4548, Numaro's monotone K_{3,3} function at 6.5218). Deliverables: verified lemmas, one serious attack, an honest failure record. Entropies are in bits.

**Build on**
- Composition identities (O'Donnell–Tan; Hod): for balanced inner h, H(g∘h) = H(g) + I(g)H(h) and I(g∘h) = I(g)I(h).
- House gate/potential equivalence (d7e78…) and the read-once Γ value iteration: a template for induction carried by a potential.
- House small-influence reduction (201fff…). It's provisional with no proof on file, so I'll re-derive it first.
- Monotone facts: Inf_i = f̂({i}), D_i f = 1_{Piv_i} ≥ 0, KKL/Talagrand.
- Benchmarks any argument must reproduce: OWZ's symmetric functions (level profile) and Wan–Wright–Wu's encodings (clustering).

**Steps**
1. *Audit (45 min).* No relevant house claim has a proof on file, so this comes first. Read 3c3de… (why monotone stalled), 201fff…, d7e78… and 27527…, and record the exact inequality where the monotone attempt broke.
2. *Self-improvement lemma (45 min).* It's cheap, and it fixes which losses I can afford.
   - Claim: if H ≤ A·I + E for all f, with E = o(I) along iterated self-compositions (e.g. E = O(log n)), then FEI holds with constant A.
   - Why: iterating a balanced g gives H(g) ≤ A(I(g)−1). The lift y·f(x) is balanced, keeps H and adds 1 to I.
   - Consequence: additive and sublinear losses are free, but multiplicative log losses can never be bootstrapped.
   - Check it on Hod's and Numaro's iterates, or cite d7e78… if it already contains the lemma.
   - Caveat: y·f isn't monotone, so unbalanced monotone f needs the biased Γ framework.
3. *Main attack: split induction with a spectral potential.* Why this route: every house success (read-once formulas, threshold gates) is an induction carried by a potential, and the chain rule below isolates a single obstruction.
   - Split f on x_i. Let T be the spectral sample and P_± the spectral laws of f_±. The chain rule gives
     H(f) = ½ΣH(f_±) + JS(P_+,P_−) + H(1_{i∈T} | T∖i),  I(f) = ½ΣI(f_±) + Inf_i.
   - My derivation (to recheck) gives JS ≤ 4·Inf_i. So the only obstruction is *thin membership*: E h(q_S) against E q_S = Inf_i, where q_S = f̂(S∪i)²/(f̂(S)²+f̂(S∪i)²).
   - Goal: a potential Ψ ≤ C′·I + o(I) that pays for this term, built from spectral statistics beyond the mean. Levers: monotone positivity and an adaptive choice of split variable.
   - Test every candidate before any proof attempt: exhaustively on monotone f with n ≤ 5 (n = 6 if fast), on random n = 7 samples, and on majority, tribes and the record functions.
   - *Hour 3 decision:* if nothing survives, or step 1 shows this route already failed, switch to the fallback. It encodes T by naming one element (≤ log n bits, free by step 2), then pays O(1) bits per further element, combining level profile and clustering.
4. *Write-up* with honest status tags.

**Avoid**
- *GMP restriction step:* sup ρ₀ ≥ C_FEI ≥ 6.52. The step needs a constant at least FEI's own, so it moves the difficulty instead of reducing it.
- *Split steps bounded only by Inf_i or the mean:* flip a bent g on a random set of density ε. Thin membership is then ≈ ε·log(1/ε) (heuristic, to recheck).
- *Subadditivity Σh(Inf_i) and level counting:* the first loses a factor log n on majority, the second on tribes. Step 2's trick can't remove multiplicative losses.
- *Percolation F0090* (refuted citation) and lower-bound hunting.
- *Unproved house claims* (LTFs, read-k DNFs, bounded-width monotone DNFs): not to be built on before I reconstruct them.

**First concrete step.**
1. Run math_note.py on claim_3c3de428c9ff4925a747a789a2e8c7ff and claim_201fffcee2604bcb9b42ffcc83185769, and re-derive the small-influence reduction by hand.
2. Write a numpy script that computes JS, H(1_{i∈T}|T∖i) and Inf_i for every monotone f with n ≤ 5 and every i. This shows what a potential must pay.
