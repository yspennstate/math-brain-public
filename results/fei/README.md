# The Fourier entropy-influence conjecture

Friedgut and Kalai (1996) conjectured that there is a universal constant C such that every Boolean function f : {-1,1}^n → {-1,1} satisfies

    H(f) ≤ C · I(f),

where H(f) = Σ_S f̂(S)² log₂(1/f̂(S)²) is the entropy of the Fourier weights and I(f) is the total influence. The conjecture is open. This folder holds the record of a campaign on it in September and October 2026: proofs, counterexamples, exhaustive and annealed searches, and the code that produced them.

## The reduction

Write p(S) = f̂(S)², π(S) = Σ_{T ⊇ S} p(T), and U(f) = Σ_S p(S) log₂(π(S)/p(S)).

- **Theorem G.** For every Boolean f, H ≤ 2(I − Var f) + 2U ≤ 2I + 2U. Since U ≤ H, FEI holds if and only if U/I is bounded.
- **Restriction identity.** Let Δ_i U = U(f) − (U(f_{i,+}) + U(f_{i,−}))/2 and G(f) = Σ_i Δ_i U(f). Then Δ_i U = B_i − Γ_i + K_i, where
  - B_i = H(S_i | S − i);
  - Γ_i = Σ_{S ∋ i} p(S) log₂(π(S − i)/π(S));
  - K_i = U(law of S − i) − (U(f_{i,+}) + U(f_{i,−}))/2 ≥ 0, a sum of binary Kullback-Leibler terms in the restriction asymmetries.
- **Sufficiency.** If G ≤ a·I + b·U with b < 1, then H ≤ (2 + 2a/(1 − b))·I.

All three are proved and were confirmed by an independent check; none has been refereed by a journal.

## The open step (GU)

Show that G(f) = Σ_i Δ_i U(f) ≤ K·I(f) for every Boolean f, with one K independent of n.

- The largest ratio G/I found is 3.090, on maj₃ composed with a five-variable function g₅. Other searches give smaller ratios:
  - every function on n ≤ 4 variables: 2.75;
  - annealing at n = 5 to 8: 2.8203;
  - tribes: at most 2.19;
  - threshold functions: at most 2.21;
  - random functions at n = 12: about 1.0.
- K = 3.09 would give FEI with C ≤ 8.18.
- The coordinatewise form, Δ_i U ≤ K·Inf_i(f) for every i, is not supported: annealed selector pairs reach ratios of 4.78, 5.11, 5.48 and 6.15 at n = 6, 7, 8 and 9, driven by the Kullback-Leibler term. A proof has to sum over i, or choose a good i.
- Slote's quantum obstruction does not block statements about U, because U vanishes on those examples.

## Results on classes of functions

These are in `opus-routes-2026-10-11/`: one folder per route, with its notes, claims, code and an independent referee's report. `SYNTHESIS.md` there reads them together. None of them proves FEI, and several have not been checked against the literature.

- **Two spectral addresses (A2).** On the class K2, where every conditional row law is a product, H ≤ 4I. The optimal constant on K2 is 16/3 − (3/2) log₂ 3 ≈ 2.95589, attained by AND on three variables; the proof has a computer step, certified twice by different rigorous algorithms. An agent of the Codex fleet reached the same constant independently.
- **Biased thresholds (BT).** For every weighted threshold function and every product measure μ, E_μ ≤ Var·ln(1/Var) + A₀·I_μ with A₀ < 9.21 nats, where E_μ and I_μ are the spectral entropy and total influence under μ. The level-wise reference conjecture is refuted by a new family, anti-diagonal tribes thresholds.
- **Selector interference (SEL).** An exact cost identity for multiplexers, cost(F) = H(S|T) + I(X;Y), with closure constant K(1/2) = 4. The sharp orthogonal-leaf bound SEL-8 is refuted, with 60-digit interval arithmetic. The Schmidt-entropy defect conjecture SEL-13, with constant κ₀ = 0.756151564, is open; searches in double precision or at 30 digits produce values above κ₀ that vanish at 60 digits.
- **Witness cost (W).** H ≤ 10.38·I on selector trees; H ≤ 16.99·I on selector trees with regular leaves on fresh blocks; H ≤ 26.71·I on term decision lists with a common output mean. A reduction, H ≤ 23.55·I + 2.4·R(f) for any subcube partition of a level set, would give FEI from a bound R ≤ K·I on its rank term. The read-once part is close to known work, O'Donnell and Tan's composition theorem.
- **Universal reductions (U).** Theorem G, the restriction identity and the GU reduction above, with several equivalent forms of FEI.
- **Level two (L2)** has candidate theorems waiting for an independent referee. **Read-k trees (K)** have their targets set and no work yet.

## Where everything is

| Folder | Contents |
|---|---|
| `scheduled-tasks/full-fei-only-2026-10-12/` | the current work order (`ORDER.md`) and the GU route |
| `scheduled-tasks/fei-all-team-2026-09-22/`, `fei-joint-proof-2026-09-21/`, `brain-benchmark-fei-2026-09-21/` | the September rounds |
| `scheduled-fleet-2026-10-11/` | the October plan, claim and obstruction registries, and the runs of the scheduled fleet |
| `codex-100-agents-2026-10-11/` | 100 Codex agents in 20 streams: one folder per agent (`agents/A001` to `A100`) with its status, work log and runs, the stream leads' notes (`claude/B01` to `B20`), the team board (`BOARD.md`) and the campaign summary (`summary/`) |
| `opus-routes-2026-10-11/` | the class routes above and `SYNTHESIS.md` |
| `BRAIN_INDEX.md` | an index of the campaign records |

Related work elsewhere in this repository: the earlier attempt in `results/open-problems/proofnet24/P03-fei/`, and the paper *Fourier entropy of threshold functions and their compositions* in `papers/public/fourier-entropy-threshold-functions/`.

The records are kept as the agents wrote them. Some of them link to two repositories, `math-research-brain` and `math-open-problems`, which are private working repositories and cannot be opened from here. The working files behind those links were not published, so read each record for what it says itself.
