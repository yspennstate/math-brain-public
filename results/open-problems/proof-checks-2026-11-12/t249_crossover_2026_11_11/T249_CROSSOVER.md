# T249: the NTK between the ordered phase and the critical line (double scaling)

an agent, 11 Nov 2026. Status: derived by hand two ways, checked numerically (tanh, sin, erf), literature searched (list below). Audited once: an agent re-derived g(t) and their own tanh code agrees to 0.3 pct at eps = 0.0025 (11 Nov 02:32Z, brain main 852e1e14), and read PROOF_UNIFORM.md line by line (02:37Z, f92fbef7). A second independent audit is owed before anything is claimed.

## Setting
Infinite-width fully connected net, activation phi (tanh in the check), weight variance sw2, bias variance sb2 > 0,
inputs on the fixed-point sphere (q = q*). chi_1 = sw2 E[phi'(sqrt(q*) z)^2] = 1 - eps, ordered side, eps -> 0 with sb2 fixed.
Depth L = t / eps, t fixed. xi = 1/eps is the depth scale of Schoenholz et al. (-1/log chi_1 to leading order).

## Claim
For any n distinct inputs,
    (eps / q*) Theta_L  ->  g(t) I + (1 - e^-t - g(t)) 11^T,
    g(t) = e^-t (2t - 3 + 4 e^-t - e^-2t) / (1 - e^-t)^2.
So the n-1 eigenvalues on 1-perp all equal (q*/eps) g(t), the top one is (q*/eps)[n(1 - e^-t) - (n-1) g(t)], and
    cond(Theta_L) = n (1 - e^-t)^3 / (e^-t (2t - 3 + 4e^-t - e^-2t)) - (n - 1).
The limit does not depend on the inputs, and depends on the activation only through q*.
Ends: t -> 0 gives g ~ 2t/3, i.e. lambda_perp = (2/3) q* L and cond -> (n+2)/2, the critical-line values;
t -> infinity gives g ~ 2t e^-t, i.e. lambda_perp ~ 2 q* L chi_1^L and cond ~ n e^t / (2t), the ordered-phase shape
(to be matched against the constant kappa lambda_perp(-A) of the posted T249 note as eps -> 0).

## Derivation (sketch)
delta = 1 - c for a pair. The correlation map has f'(1) = chi_1, f''(1) = beta > 0, so with s = eps l
    d delta/dl = -eps delta - (beta/2) delta^2   =>   beta delta / eps = 2 e^-s / (1 - e^-s) =: r(s),  whatever delta_0 is.
NTK: Theta_{l+1} = K_{l+1} + Kdot_{l+1} Theta_l, K = q* c, Kdot = f'(c) = chi_1 - beta delta + ...
Diagonal: Theta_d = (q*/eps)(1 - e^-s). With D = Theta_d - Theta_o = (q*/eps) g:
    g' = -(1 + r) g + r (1 - e^-s) = -(1 + r) g + 2 e^-s,   g(0) = 0.
Integrating factor e^s (1 - e^-s)^2:  (e^s (1-e^-s)^2 g)' = 2 (1 - e^-s)^2, which integrates to the formula. beta cancels.
The first correction is O(eps / delta_0) per pair (the memory of the initial angle), which is what splits the n-1 eigenvalues.

## Numeric check (tanh, sb2 = 0.05, n = 8 random unit inputs in R^5, Gauss-Hermite 120)
At t = 1 (g = 0.30951, predicted cond/n for n = 8: 1.0423 + 0.125 = 1.1673):
    eps    lam_min*eps/q*  lam_(n-1)*eps/q*  cond/n
    0.04   0.1159          0.6056            3.130
    0.02   0.1802          0.4876            1.994
    0.01   0.2346          0.4133            1.521
    0.005  0.2705          0.3677            1.318
The bracket [lam_min, lam_(n-1)] closes on g from both sides (log-width 1.65, 0.99, 0.57, 0.31) and cond/n - 1.1673
falls by 0.42-0.43 per halving. Same picture at t = 0.5, 2, 4, 6, 8 (full table in crossover_check.out).
Not yet a proof of the rate; eps = 0.0025 and 0.00125 and a second activation would settle it.

## What it would give the row
The row asks where trainability stops in L / xi. In the kernel regime gradient flow needs ~ cond steps, so the step
count per sample is h(L/xi) with h(t) = (1 - 2t e^-t - e^-2t) / (e^-t (2t - 3 + 4e^-t - e^-2t)): flat (1/2) for L << xi,
e^t/(2t) for L >> xi, and the "c" of Schoenholz et al. becomes the solution of n h(c) = step budget rather than a constant.
This is infinite-width kernel regime only; the trained finite-width statement stays open.

## Before anything is claimed
1. Literature: Xiao-Pennington-Schoenholz 1912.13053 (do they give the crossover or only the two regimes?), Hayou-Doucet-Rousseau
   1905.13654, Seleznova-Kutyniok, Roberts-Yaida-Hanin (near-critical), Doshi-He-Gromov 2111.12143.
2. Proof with an error term: uniform control of delta_l for l up to t/eps, error O(eps log(1/eps)) or O(eps/delta_0).
3. Second derivation by a different route (resolvent / Koenigs function of the posted note in the limit eps -> 0).
4. Two independent audits (one Codex, one Claude peer), then decide whether it is a section added to the posted note or its own note.

## 11 Nov 00:45 additions
Finer runs (check2_tanh.out, n = 8, predicted cond/n now carries the finite-n term):
    eps      t=1 bracket [lam_min, lam_(n-1)]*eps/q*   g      cond/n   predicted
    0.0025   [0.2905, 0.3412]                          0.3095  1.2303   1.1673
    0.00125  [0.3006, 0.3265]                          0.3095  1.1927   1.1673
cond/n - predicted: 1.96, 0.83, 0.354, 0.151, 0.063, 0.025 for eps = 0.04 ... 0.00125 (ratio about 0.41 per halving, so the error
is a little faster than O(eps) over this range). Same at t = 0.5, 2, 4, 8. erf and sin not yet run (crossover_check2.py erf|sin <eps list>).
arXiv API searches (NTK with "edge of chaos", "ordered phase", "correlation length", "near criticality", "scaling function", condition number):
only Seleznova-Kutyniok 2202.00553 and Terjek-Gonzalez-Sanchez 2501.13225 / 2501.14724 (a s + b|s| activations AT the EOC) came back.
None states a crossover function. NOT yet read: Xiao-Pennington-Schoenholz 1912.13053 in full, Hayou et al. 1905.13654, Martens et al.
(Deep Kernel Shaping, 2110.01765), Li-Nica-Roy (neural covariance SDE, 2206.02768). The last two work in a per-layer-deviation ~ 1/L
regime, which is this scaling in other clothes for the forward kernel; check whether their NTK statements cover it.

## 11 Nov 00:47 literature, first two papers read as text (lit/)
Xiao-Pennington-Schoenholz 1912.13053: ordered, critical and chaotic phases are treated one at a time (their Table 1/2 and Sec. on
each phase); no statement with chi_1 -> 1 and depth ~ 1/(1 - chi_1) together, no interpolating function. Their xi_1 = -1/log chi_1
appears only as the ordered-phase depth scale in the experiments.
Hayou-Doucet-Rousseau 1905.13654: results AT the EOC and away from it; no near-EOC scaling window.
Still unread: Martens et al. 2110.01765, Li-Nica-Roy 2206.02768, Roberts-Yaida-Hanin (book, near-critical perturbation), Seleznova-Kutyniok 2202.00553.
So far the crossover formula is not in the literature I have read. It stays a candidate.

## 11 Nov 00:50 literature, three more read as text
Martens et al. 2110.01765 (Deep Kernel Shaping), Sec. 24.5-24.6: the overall NTK is estimated in three separate cases -
C'(1) < 1: K ~ E/(1 - C'(1)) (rank one, leading order only); C'(1) = 1: K ~ D(I + mu(E - I)) with mu = 1/3 (observed, conjectured);
C'(1) > 1 exploding. The mu = 1/3 line is the t -> 0 end of the formula here (g = 2t/3). Under DKS itself (activations reshaped
toward linear, slope zeta fixed) Theorem 27 only bounds each layer's NTK against the data Gram, and the text says "We leave the
problem of accurately estimating the value of cond(K) under DKS to future work." No interpolating formula for a fixed activation.
Li-Nica-Roy 2206.02768: NTK appears only in the introduction and references. Seleznova-Kutyniok 2202.00553: ReLU, finite
depth-to-width ratio, moments of the NTK; "close to the EOC" only as a remark on Figure 1. Neither has the crossover.
Five papers read, none states it. Still unread: Roberts-Yaida-Hanin (2106.10165), Terjek 2501.13225 (EOC only by its abstract).
Novelty is therefore "not found in the closest five", no more. The derivation is short, so treat it as a section for the posted
T249 note (the row's L/xi question), not a separate paper, unless the trained-network half moves.

## 11 Nov 00:53 second route: the posted ordered-phase law in the limit eps -> 0 (koenigs_check.py / .out)
Posted law: lambda_perp ~ kappa k L chi_1^L, kappa = q* + beta T*/chi_1, T* = q*/(1 - chi_1), k = lim delta_l / chi_1^l (Koenigs value).
From the quadratic flow, k(delta_0) = eps delta_0 / (eps + beta delta_0 / 2) -> 2 eps / beta, and kappa ~ beta q* / eps, so kappa k -> 2 q*:
the same 2 q* L e^-t as the t -> infinity end of g. Measured (tanh, sb2 = 0.05), kappa k / (2 q*):
    delta_0   eps 0.02   0.01    0.005
    1.0       1.036      1.042   1.034
    0.5       0.885      0.958   0.989
    0.2       0.643      0.796   0.895
    0.05      0.282      0.448   0.624
and k beta / (2 eps) against 1 / (1 + 2 eps / (beta delta_0)): 0.6115 vs 0.6095 at delta_0 = 0.05, eps = 0.005 (agreement to 0.3 pct for small
delta_0; for delta_0 of order one the transient outside the quadratic regime shifts it by a few pct, still -> 1).
Two things this fixes in the claim: (a) the limit is NOT uniform in the inputs - a pair with 1 - c_0 of order eps / beta or smaller has not
reached the universal value, so the statement is for fixed distinct inputs, with relative error of order eps / (beta min delta_0);
(b) the first correction is explicit: per pair, replace 2 e^-s / (1 - e^-s) by the flow started at delta_0, which is what splits the n-1 eigenvalues.
Status: formula derived two ways, both checked numerically for tanh. A depth-uniform version with an error term is written out in PROOF_UNIFORM.md (one author, numerics in uniform_tanh*.out); numerics for tanh, sin and erf in uniform_*.out; the Theorem there has now been read by two independent readers (see its status line).

## More papers read (11 Nov, after the proof)

- Terjek and Gonzalez-Sanchez, arXiv 2501.13225, "MLPs at the EOC: Spectrum of the NTK": activations a s + b |s|, exactly at
  the edge of chaos; entries approximated by inverse cosine distances, condition-number limits in depth. No smooth
  activation, no off-critical parameter, so no crossover in eps L.
- Roberts, Yaida and Hanin, arXiv 2106.10165: kernels and NTK are analysed at criticality; off criticality only the
  exponential behaviour is described; the "double-scaling limit" there (text search) is depth against width, not
  depth against distance to criticality. Checked by keyword search of the full text, not by reading the NTK chapters.

- Jacot, Gabriel, Ged and Hongler, arXiv 1907.05715, "Order and chaos: NTK eigenvalue decomposition and its
  application to the freeze and chaos phases": the two phases are treated separately through a characteristic value
  r, with r < 1 ordered ("freeze") and r > 1 chaotic; at r = 1 it records Theta(x, x) = L. The transition between
  the phases is not resolved in a joint limit of depth and distance to r = 1.

Eight papers checked in all; none states g(t) or the depth-uniform formula F_L of PROOF_UNIFORM.md.
