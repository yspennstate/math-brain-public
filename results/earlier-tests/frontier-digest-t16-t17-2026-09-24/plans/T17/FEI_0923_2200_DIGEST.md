# FEI: plan for the next few hours

**Framing.** The best general result (KKLMS 2020) still loses a log I factor. A proof within hours is unlikely; I attack the bottleneck with one machine-checkable step inequality, built to fail fast.

**Bottleneck.** Splitting on x_i is exact bookkeeping: H(f) = avg H(f_±) + JS(p₊,p₋) + H(1_{i∈S} | S∖i), with each extra term ≤ 1 bit, while I drops by exactly Inf_i. So variables with Inf_i ≥ δ₀ peel off at C ≥ 2/δ₀ (house note 201fffce), leaving small-influence functions, whose restrictions share variables. Composition methods (O'Donnell–Tan, the house's gate potential) never face this.

**Main line: two-sided restriction step.** For a cut [n] = J ⊔ Jᶜ and spectral sample S, the chain rule gives

```
H(S)   = E_z H(f_{Jᶜ|z}) + E_w H(f_{J|w}) + Δ_f(J)
Δ_f(J) = MI(z; S∩Jᶜ) + MI(w; S∩J) − MI(S∩J; S∩Jᶜ)
```

(z = x_J, w = x_{Jᶜ}; the first MI couples z with the spectral sample of f_{Jᶜ|z}, and likewise for the second). Influences add exactly: E_z I(f_{Jᶜ|z}) + E_w I(f_{J|w}) = I(f). Suppose every f has a cut with

```
(★)  Δ_f(J) ≤ C·[E_z Γ(μ_z) + E_w Γ(μ_w) − Γ(μ)],   μ_z = E[f | x_J = z],
```

for a symmetric Γ with Γ(±1) = 0 and 0 ≤ Γ ≤ 1. Then induction on n gives H ≤ C(I − Γ(Ef)), hence FEI.

Hand checks:
- For odd f (Maj₃ included), single-variable cuts have Δ = 0.
- AND₂ has Δ = 2 and forces Γ(½) ≤ 1 − 2/C. So Γ = Var needs C ≥ 8; use the house's measure-only potential instead (d7e78ede).

Why start here:
- It engages shared variables directly.
- Its |J| = 1 case is "split on the most influential variable", which settled threshold gates (50aaad84).
- It can be checked function by function.

Failure kills the route, not FEI. (★) may be the house's ρ₀ inequality (dc05672a: sup ρ₀ ≥ C_FEI). If so, the open question is whether it is finite, not its constant.

**Build on:**
- KKL/Talagrand and Bonami hypercontractivity on derivatives: Booleanity enters as ‖D_i f‖_p^p = Inf_i.
- The iterated-composition bound C ≥ H(g)/(I(g)−1) for balanced g.
- House notes 201fffce, d7e78ede, 50aaad84 once re-derived (no proofs on file).
- Hod's lexicographic functions and Numaro's K₃,₃ function as stress tests.

**Avoid:**
- Percolation/Kalai Conj. 8: the candidate proof died on a misremembered citation; special case anyway.
- Leaning on arXiv:2606.00246 or the ρ₀ notes before verifying them: the attribution drifted (Gopalan–Mek… → Gonzalez–MacManus–Pereyra) and two versions were withdrawn.
- Pivotal-set entropy proxies: false in general (for OR_n, H(Piv)/I ≈ n/2).
- Arguments valid for real-valued f: FEI fails there (flat level-1 function: H = log n, I = 1).
- Any lemma implying C < 6.45 (Hod), or < 6.52 if Numaro's result holds: it's false.
- More special classes or better lower bounds: they don't touch the core.

**Schedule**
1. (0–45 min) Read dc05672a, 201fffce, d7e78ede, 50aaad84 and the withdrawn ρ₀ versions in full, and verify the citation. Decide whether (★) = ρ₀ and reuse any step-constant data. Re-derive the identity and the 2-bit split.
2. (45 min–2.5 h) Go/no-go computation of R_n = max_f min_J Δ/budget:
   - exhaustive for n ≤ 4, local search for n = 5–8;
   - exact level formulas for Maj_n up to n ≈ 61;
   - Tribes, recursive Maj₃, Hod's and Numaro's functions and their compositions.

   Record the minimizing cuts.
3. If R_n grows: pin the family down analytically and record it as a refutation of the step route. Then pivot to removing the log I in the KKL-tight regime (I ≤ K·log(1/max Inf)).
4. If R_n stays bounded: read a cut rule off the data (heaviest variable when Inf ≥ δ₀, random balanced cut otherwise). Then try to prove (★) for small influences by bounding E_J Δ_f(J) with hypercontractivity on cross-cut derivatives.

**First concrete step:** a script that, for every f on ≤ 4 variables and every cut, computes both restricted entropies, Δ_f(J), and the budget under Γ = Var and under the d7e78ede Γ. It asserts the identity to 1e−12 and lists the worst cuts.
