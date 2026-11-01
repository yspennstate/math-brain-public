# FEI plan — 2026-09-25 session

**Aim.** A full proof in a few hours is unlikely. I will aim for one rigorous, checkable step on the real bottleneck: functions that are not compositions and whose influences are all small. Before spending proof effort on any idea, I will try to falsify it numerically.

**Main route: an edge-local form of FEI.** Fix a coordinate j. Let S ~ f̂² be the spectral sample and f± = f with x_j fixed to ±1. Two identities hold exactly:
- H(f) − ½[H(f+)+H(f−)] = JS(f̂+², f̂−²) + H(1[j∈S] | S∖j)
- I(f) − ½[I(f+)+I(f−)] = Inf_j(f)

Also JS ≤ (4/ln2)·Inf_j, by triangular discrimination.

For one direction, erasure entropy gives Σ_j H(1[j∈S] | S∖j) ≤ H(S). For the other, pick j greedily and induct on restrictions. This should give the following, with constants shifting by at most about 7.2 bits:

**FEI ⇔ DRI:** E_S Σ_{j∈S} log(1 + f̂(S∖j)²/f̂(S)²) ≤ C·I(f).

In words: steep down-edges of the spectral measure are rare.

A sharper target that still suffices is the **square-root law (SRL)**: the spectral mass of pairs (S, j∈S) with f̂(S∖j)² ≥ e^t·f̂(S)² is at most K·e^{−t/2}·I(f).
- Back-of-envelope estimates suggest AND_k, tribes and biased majority all hit the exponent ½ exactly.
- Level-1 edges satisfy SRL with K=1, because |f̂({j})| ≤ Inf_j.
- Any uniform integrable tail would also be enough, so SRL can be weakened if it fails.

**Why this first.**
- It is local. Each edge pairs the spectra of D_j f and E_j f. Both are {−1,0,1}-valued with disjoint supports, so level-k and hypercontractive bounds apply directly to D_j f, whose support is small.
- It gives the small-influence reduction for free, since each restriction step costs at most 2 bits.
- It is cheap to test.

**Steps**
0. (15 min) Read three memory notes in full: claim_dc05672a (GMP ρ_0), claim_201fffce (small-influence reduction) and claim_3c3de428 (monotone status). GMP's key inequality may be the best-variable restriction step. If so, the argument above gives sup ρ_0 ≤ C_FEI + O(1), so the key inequality is equivalent to FEI itself, and I will record that.
1. (45 min) Write the FEI ⇔ DRI proof with explicit constants, checking every line.
2. (1.5 h) Write a Walsh–Hadamard script that computes H, I, the JS_j terms, the erasure terms and the down-edge tail M_f(t).
   - Test functions: all n≤4, monotone n≤5, NPN samples at n=5–6, AND_k, tribes, biased majority and LTFs, recursive majority, address, Hod's recursive family, and Numaro's 18-variable record (claim_dc791b32, claim_3765d933).
   - Report sup_t e^{ct}·M_f(t)/I for c=½ and for smaller c. Deep compositions are where K is most likely to grow.
   - If the ratio stays bounded, attack SRL. If some family is unbounded, analyse it, record it, and fall back to the integrated DRI.
3. (rest of the session) Proof attempts, easiest first:
   - Symmetric functions: coefficients are constant on each level, so DRI becomes an inequality on level weights. It must recover O'Donnell–Wright–Zhou.
   - Monotone functions, where D_j f = 1_{Piv_j} ≥ 0.
   - General edges, using level-k bounds on D_j f.

**Build on.**
- Literature:
  - tensorization, which removes additive constants;
  - edge-isoperimetry, KKL/Talagrand, and hypercontractive level-k inequalities;
  - O'Donnell–Tan composition (to see how DRI and SRL behave under composition) and O'Donnell–Wright–Zhou;
  - KKLMS 2020, which proves FEI up to a log I factor in concentration form;
  - Hod's lower bound of 6.4548.
- House: Numaro's 6.5218 function as the stress test, used only after checking it.

**Avoid.**
- The percolation / Kalai Conjecture 8 candidate proof: it was withdrawn after its citation was refuted.
- Any restriction-step inequality with a constant below 6.52: impossible, because sup ρ_0 ≥ C_FEI.
- Bias-only potentials, and the all-arity gate inequality beyond read-once formulas: at unbounded arity every function is a gate, so this only restates FEI.
- More special classes (DNF variants, read-k, LTFs): they avoid the small-influence core, and several house claims in this area have no proof on file.
- Trying to remove KKLMS's log I factor head-on: well-trodden, and the losses come from working across many scales.
- Invariance-principle arguments: they see how mass is spread across levels, not how it spreads within a level, which is what H measures.

**First concrete step.** Read claim_dc05672a in full. Then, before writing any code, write out the two identities and the erasure/greedy argument with explicit constants.
