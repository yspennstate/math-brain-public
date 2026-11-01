# T262: a localized inverse-angle generator calculation

2026-10-23. This is a proof of a **one-step, compact-state lemma**, not a proof of the full T262 limit. It supplies the rare sign-flip contribution with an explicit error. The entrance from a fixed input angle, compact containment over `O(n)` layers, and the joint norm coordinate are separate obligations. The model is exactly the `rows/T262/DOSSIER.md` and `rows/T244/DOSSIER.md` He-ReLU angle chain: in one layer, for `a_i,h_i` iid standard Gaussians,

```
b_i=cos(θ)a_i+sin(θ)h_i,   X_i=(a_i)_+,   Y_i=(b_i)_+,
Θ=angle(X,Y),             u=1/(nθ),      u'=1/(nΘ).
```

The zero-output event is exponentially unlikely for the compact regime below. To avoid integrating an undefined/infinite inverse angle on that event, the lemma uses a clipped one-step transition `u^*=u'` on a specified good event and `u^*=u` otherwise. The good event fails with probability at most `C_{δ,K,p}n^{-p}` for every fixed `p`, uniformly on the compact state interval; therefore over `O(n)` steps the clipped and original angle chains agree with probability tending to one **provided the chain is stopped in that compact interval**.

## Proposition (localized generator)

Fix `0<δ<K<∞`. For `u∈[δ,K]` set `θ=(nu)^{-1}`. There is a choice of good event `B_n(θ)` below and constants `C=C(δ,K)`, `n₀(δ,K)` such that for all `n≥n₀`, writing `Δ=u^*−u`,

```
|n E_θ Δ − (2u+1/(3π))| ≤ C n^{-1/2},
|n E_θ Δ² − 2u²|         ≤ C n^{-1/2},
n E_θ |Δ|³               ≤ C n^{-1/2}.
```

Consequently, for each `f∈C_b³` and `u∈[δ,K]`,

```
n E_θ[f(u^*)−f(u)]
 = (2u+1/(3π)) f'(u) + u² f''(u) + O_{δ,K}(||f||_{C³} n^{-1/2}).
```

The candidate diffusion on compact subintervals of `(0,∞)` is thus `du=(2u+1/(3π))dt−√2 u dB`. The sign of its Brownian coefficient is immaterial for the scalar generator, but matters for coupling it to the norm coordinate.

## Proof

All constants in moment estimates below are uniform for `c=nθ=1/u∈[1/K,1/δ]`. In particular `θ≤C/n`. Put `A={i:a_i>0}`, `k=|A|`, `q=||X||²`. Define `P=I−XXᵀ/q` and `V=||P h_A||²` only when `q>0` and `k≥2`; give them arbitrary values elsewhere, since they are used only on `B_n`, where `q>0` and `k≥n/3`. Also define

```
Z_i=(b_i−a_i)1_A(i),       r_i=Y_i−X_i−Z_i,
D=||P Z||²=sin²(θ)V       (on q>0,k≥2),
J=Σ_i (b_i−a_i)² 1_{F_i},  F_i={a_i b_i≤0}.
```

Here `r` vanishes off the flip set `F`. On `F`, `|r_i|≤|b_i−a_i|`, and whenever `X_i r_i≠0` also `|a_i|≤|b_i−a_i|`; hence `|⟨X,r⟩|≤J` and `|2⟨Z,r⟩+||r||²|≤3J`. With `ρ_i²=a_i²+h_i²`, the rotation identity gives `|b_i−a_i|≤θρ_i`. The polar angle of `(a_i,h_i)` is independent of `ρ_i` and `P(F_i)=θ/π` exactly. Thus for `S=Σ_i ρ_i²1_{F_i}` we have `J≤θ²S` and, for every fixed integer `p≥1`,

```
sup_{n, c∈[1/K,1/δ]} E S^p <∞.                  (1)
```

Indeed the factorial-moment expansion of the independent rare indicators has terms bounded by constants times `(nθ)^j`, `j≤p`, while all radial moments are finite.

Conditional on `k`, `q~χ²_k` and `V~χ²_{k−1}` are independent; the latter is the Gaussian tangent component orthogonal to `X`. If `H=⟨X,h_A⟩`, then conditional on `X`, `H~N(0,q)` and is independent of `V`. Define `B_n` by

```
n/3≤k≤2n/3,  n/4≤q,V≤n,  S≤n/1000,  |H|≤n.
```

Chernoff/chi-square/Gaussian tails and (1) imply `P(B_n^c)≤C_{δ,K,p}n^{-p}` for every fixed `p`; the constant `1000` may be replaced by a larger fixed number if needed. On `B_n`, `q,V` are comparable to `n`, the flip perturbation below has magnitude `<1/2` for large `n`, and `Θ>0`. Set `u^*=u` on `B_n^c`.

**Exact flip expectation.** Let `N₀=2⟨Z,r⟩+||r||²=||Y−X||²−||Z||²`. The two-dimensional Gaussian ReLU covariance is

```
E X_iY_i = [sin θ+(π−θ)cos θ]/(2π),
E (Y_i−X_i)² = 1−[sin θ+(π−θ)cos θ]/π,
E Z_i² = 1−cos θ.
```

Consequently, **without a Poisson approximation or an independence assumption about the denominator**,

```
E N₀ = n[θ cos θ−sin θ]/π
     = −n θ³/(3π)+O(nθ⁵).                         (2)
```

Projection onto `X⊥` replaces `N₀` by

```
N=2⟨PZ,Pr⟩+||Pr||²
 =N₀−[2⟨X,Z⟩⟨X,r⟩+⟨X,r⟩²]/q.
```

Write `Ξ=N/D` and `Ξ₀=N₀/(sin²θ V)`. Since `⟨X,Z⟩=(cos θ−1)q+sin θ H`, its fixed-order moments are `O(n^{-1/2})`; `⟨X,r⟩` has fixed-order moments `O(θ²)` by (1). On `B_n`, `D≥c θ² n`; Holder's inequality and (1) therefore yield

```
|| (Ξ−Ξ₀)1_B ||_{L^p}=O_{δ,K,p}(n^{-5/2}),
|| Ξ1_B ||_{L^p}=O_{δ,K,p}(n^{-1})           (3)
```

for each fixed `p`. (The first estimate is deliberately weaker than some of the individual terms.) Moreover `V−n/2` has `L²` norm `O(√n)` and `V≥n/4` on `B_n`, so `||(1/V−2/n)1_B||₂=O(n^{-3/2})`. By (1), `||N₀/sin²θ||₂=O(1)`, and removal of `B_n^c` from its expectation costs an arbitrarily high inverse power of `n`. Cauchy-Schwarz and (2) now give

```
E[Ξ1_B] = (2/n) E[N₀/sin²θ] + O(n^{-3/2})
         = (2/π)[θ cos θ−sin θ]/sin²θ + O(n^{-3/2})
         = −2θ/(3π)+O(n^{-3/2}).                (4)
```

This is the controlled flip contribution. Its random fluctuations have `L²` size `O(n^{-1})`, smaller than the tangent's `O(n^{-1/2})` fluctuation, yet its mean is exactly at the required `1/n` order.

**Angle and reciprocal expansion.** On `B_n`, set `R=√(V/q)` and `M=⟨X,Z+r⟩/q`. The angle identity is exact:

```
tan Θ = [sin θ · R · √(1+Ξ)]/(1+M).
```

By (1) and the Gaussian bound on `H`, `||M1_B||_{L^p}=O_{δ,K,p}(n^{-3/2})`, while `Θ=O(θ)` and `θ/sinθ=1+O(n^{-2})` on `B_n`. Central chi-square concentration and inverse moments give `||(R^{-1}−1)1_B||_{L^p}=O_{δ,K,p}(n^{-1/2})` for every fixed finite `p` used by Hölder (in particular `p=6,12`). Inverting the identity, using `tanΘ/Θ=1+O(n^{-2})` and Taylor expanding `(1+Ξ)^{-1/2}`, gives

```
(Δ/u)1_B = (R^{-1}−1)1_B − (Ξ/2)1_B + E_n,
||E_n||_{L^p}=O_{δ,K,p}(n^{-3/2})            (5)
```

for `p=1,2,3`, with `Δ=0` off `B_n`. The cross term `(R^{-1}−1)Ξ` is `O_{L^p}(n^{-3/2})`; this follows from bounded fixed-order moments of the chi-square ratio and (3), with Holder exponents increased as necessary. Note that (5) is a statement at `θ=c/n`, not uniform over all fixed `θ≤ε`.

Conditional on `k≥4`, the independent chi-square laws give the **exact** identities

```
E[R^{-1}−1 | k]  = 1/(k−2),
E[(R^{-1}−1)²|k]= k/[(k−3)(k−2)].              (6)
```

For `k~Bin(n,1/2)`, average (6) **only over `n/3≤k≤2n/3`**, giving `2/n+O(n^{-2})` in each line. Within that central-`k` event, all fixed high inverse moments of `R` are uniformly bounded for large `n`; Hölder and `P(B_n^c)≤C_p n^{-p}` show that deleting the rest of `B_n^c` changes those truncated expectations by an arbitrarily high inverse power of `n`. We never invoke an untruncated inverse moment at `k≤3`, where it may not exist. Equations (4)–(6) therefore show

```
E Δ = u[2/n+θ/(3π)+O(n^{-3/2})]
    = [2u+1/(3π)]/n+O(n^{-3/2}),
E Δ²= u²[2/n+O(n^{-3/2})],
E|Δ|³=O(n^{-3/2}),
```

uniformly on `[δ,K]`. This proves the three moment assertions and Taylor's formula proves the generator assertion.

## Scope and the next proof obligation

The deterministic drift is not a centered fluctuation: at fixed `θ>0`, `E|log(Θ/θ)|³` is of order `θ³`, so T244's displayed uniform `O(n^{-3/2})` raw third-moment statement for all `θ≤ε` cannot be used to establish entrance. At `θ=c/n` the present calculation avoids that issue. A full T262 target-1 proof still needs a two-region argument: show rapid entry from fixed `θ₀` into small angles, then prove compact containment and entrance at `u=0` using an estimate with the deterministic contribution retained, e.g. `E|Δ log θ|³≤C(n^{-3/2}+θ³)` and the key cancellation `u³θ³=n^{-3}` for inverse-angle increments. The present proposition only grants the martingale problem after stopping in `[δ,K]` and does not establish that the original chain avoids returning toward `u=0` or escaping to infinity. The joint norm/angle covariance in `rows/T262/DOSSIER.md` also requires a separate mixed-moment calculation.
