# Closing the keystone's last input via the empirical projector average $\bar P$

Agent note, 2026-06-28. Target: prove unconditionally
```
   E_pair |rho|^2 = o(1),   rho = <u_S,u_T>,  S,T two random (m-1)-row spans of A in F^{n x m},
```
`A` iid mean-0 var-1 bounded density, `n/m -> gamma > 1` (`n` = number of available rows; the
keystone uses `N` or `N-1`, immaterial here). This is the II.B universality upper side / Gumbel
input. Companions (read-only): `keystone_synthesis.md`, `keystone_typical.md`, `keystone_weak_deloc.md`.

The pair `(S,T)` is two INDEPENDENT uniform `(m-1)`-subsets of `[n]`; this includes the random
overlap `r = |S cap T|` (NOT a fixed conditioning on `D` as in the companions). That averaging over
`r` is the whole point of the reformulation, so I track it explicitly.

--------------------------------------------------------------------------------
## 0. The reformulation is EXACT (deterministic identity, verified)

Let `Pi_S = u_S u_S^*` (rank-1 normal projector, phase-free) and
```
   Pbar := (1/C) sum_{|S|=m-1} Pi_S,   C := binom(n, m-1),
```
the empirical average over ALL `(m-1)`-subsets. For a fixed matrix `A`,
```
   tr(Pbar^2) = ||Pbar||_F^2 = (1/C^2) sum_{S,T} |<u_S,u_T>|^2,
```
so taking `E_A` and noting `(S,T)` uniform <=> the `C^2`-fold average,
```
   E_pair|rho|^2 = E[ tr(Pbar^2) ].                                            (0.1)
```
Two deterministic facts: `tr Pbar = 1` (average of trace-1 projectors) and (companion
`keystone_typical.md`, symmetric/circular law) `E[Pi_S] = I_m/m`, hence `E[Pbar] = I_m/m`. Then,
PURELY ALGEBRAICALLY (no expectation needed for the split, since `tr Pbar = 1` always):
```
   tr(Pbar^2) = ||Pbar - I_m/m||_F^2 + 2 tr(Pbar)/m - 1/m
              = ||Pbar - I_m/m||_F^2 + 1/m.                                    (0.2)
```
Taking `E_A` and using (0.1):
```
   E_pair|rho|^2 = 1/m + E|| Pbar - I_m/m ||_F^2.                              (0.3)
```

> **Reduction (verified).** `E_pair|rho|^2 = o(1)` <=> `E||Pbar - I_m/m||_F^2 = o(1)`: the keystone's
> last input is EXACTLY the concentration of the dependent projector average `Pbar` about its mean
> `I_m/m`. (Under a non-symmetric law replace `I/m` by `M = aI+bJ`; `b=O(m^{-3/2})` suffices, see
> `keystone_typical.md` Prop. 1. I take the symmetric/circular case; the route below is law-agnostic.)

--------------------------------------------------------------------------------
## 1. Route (a) Efron-Stein: the per-row effect telescopes to a discrete derivative of `q_r`

`Pbar` is a symmetric function of the `n` iid rows `a_1,...,a_n`. Resample `a_i -> a_i'` (indep
copy), giving `Pbar^{(i)}`; `Delta_i := Pbar - Pbar^{(i)}`. Entrywise (scalar) Efron-Stein summed
over the `m^2` entries:
```
   E||Pbar - I/m||_F^2 = sum_{k,l} Var((Pbar)_{kl}) <= (1/2) sum_{i=1}^n E||Delta_i||_F^2.   (1.1)
```

**Only subsets `S ni i` move.** `u_S` depends only on the rows of `S`, so `Pi_S` is unchanged for
`S not ni i`. There are `K := binom(n-1, m-2)` subsets containing `i`, and `C = (n/(m-1)) K`, so
```
   Delta_i = (1/C) sum_{S ni i} (Pi_S - Pi_S^{(i)}) = ((m-1)/(nK)) T_i,  T_i := sum_{S ni i}(Pi_S - Pi_S^{(i)}).
```
Hence `E||Delta_i||_F^2 = ((m-1)^2/(n^2 K^2)) sum_{S,S' ni i} c(S,S')`, where
```
   c(S,S') := E < Pi_S - Pi_S^{(i)},  Pi_{S'} - Pi_{S'}^{(i)} >_HS                 (1.2)
            = E[ |<u_S,u_{S'}>|^2 - |<u_S^{(i)},u_{S'}>|^2 - |<u_S,u_{S'}^{(i)}>|^2 + |<u_S^{(i)},u_{S'}^{(i)}>|^2 ].
```
This is the MIXED second difference (in resampling `a_i`) of `|<u_S,u_{S'}>|^2`. The mean of
`|<.,.>|^2` cancels in the second difference -- that is the gain over the naive triangle bound
(which gives `||Delta_i||_F <= (m-1)/n * sqrt2 = O(1)`, useless: `sum_i = O(m)`).

**The four terms collapse to `q_r` by overlap-counting.** Let `r = |S cap S'| >= 1` (both contain
`i`). Resampling row `i` to a FRESH independent `a_i'` makes `a_i'` an ordinary private row, so it
no longer counts toward the shared rows of any normal built from `a_i'`. Tracking the actual shared
rows of each of the four pairs (all other private/shared rows are iid and independent):
```
   (u_S , u_{S'})            share S cap S' (incl. i):  overlap r   -> E = q_r
   (u_S^{(i)}, u_{S'}^{(i)}) share (ScapS')\{i} + a_i' = r:        -> E = q_r
   (u_S^{(i)}, u_{S'})       share (ScapS')\{i}  (a_i' != a_i): r-1 -> E = q_{r-1}
   (u_S , u_{S'}^{(i)})      share (ScapS')\{i}:           r-1      -> E = q_{r-1}
```
where `q_r := E[ |<u_S,u_T>|^2 | |S cap T| = r ]` is the conditional overlap moment (`= E_E tr(M_E^2)`,
`D = m-r`, of the companions). Therefore, EXACTLY,
```
   c(S,S') = q_r - q_{r-1} - q_{r-1} + q_r = 2 ( q_r - q_{r-1} ),   r = |S cap S'|.   (1.3)
```

**Assemble.** `sum_{S,S' ni i} c(S,S') = K^2 * E_r[ 2(q_r - q_{r-1}) ]` with `r` the overlap of two
random `(m-1)`-subsets each containing `i` (so `r-1 ~ Hypergeometric`, `E[r] ~ 1+(m-2)^2/n`). Thus
```
   E||Delta_i||_F^2 = ((m-1)^2/n^2) * 2 E_r[q_r - q_{r-1}],
   (1/2) sum_{i=1}^n E||Delta_i||_F^2 = ((m-1)^2/n) * E_r[ q_r - q_{r-1} ],
```
and Efron-Stein (1.1) gives the clean

> **Reduction (rigorous, NEW).**
> ```
>    E|| Pbar - I_m/m ||_F^2  <=  ((m-1)^2 / n) * E_r[ q_r - q_{r-1} ],            (1.4)
> ```
> `r` = overlap of two random `(m-1)`-subsets sharing one forced index; typical `r-1 ~ (m-2)^2/n`,
> i.e. typical `D = m-r ~ m(gamma-1)/gamma = Theta(m)`. The global concentration is controlled by a
> SINGLE discrete derivative (increment) of the conditional overlap moment `q_r` at TYPICAL overlap.

Since `q_r` is nondecreasing in `r` (more shared rows => more aligned normals), the RHS is `>= 0`,
consistent with `E||.||^2 >= 0`.

**Why Efron-Stein is the RIGHT tool (not lossy).** The resampling bound equals exactly the
degree-weighted Hoeffding sum `sum_k k V_k` (`V_k` = order-`k` ANOVA variance, `Var = sum_k V_k`).
Numerically (1.4) is tight up to the constant `gamma/(gamma-1)` (= average ANOVA order), so the
variance is carried by LOW-order (few-row) interactions and (1.4) loses only a constant. The naive
triangle bound, by contrast, loses a factor `~m`. So the only question is the increment `delta_r`.

--------------------------------------------------------------------------------
## 2. Numerics: every step of Section 1 confirmed (F=R, gauss/exp/rad/unif)

Scripts `scratchpad/pbar_check.py`, `qr_check.py`. All consistent with Sections 0-1.

**(0.3) identity, exact.** `E||Pbar-I/m||_F^2` and `E[tr(Pbar^2)-1/m]` agree to all digits (they are
deterministically equal), full enumeration of `Pbar`, `m<=8`.

**Truth value `= Theta(1/m)`** (decaying, the keystone holds): `m * E||Pbar-I/m||_F^2` is bounded,
`~0.6` at `gamma=2`, `~0.4` at `gamma=3` (`m=4..8`). Equivalently `E_pair|rho|^2 = 1/m + Theta(1/m)`.

**`q_r ~ 1/D` and increment `~ 1/(D(D+1)) = O(1/D^2)`** (`D = m-r`), `m in {12,20,30}`, gauss:
```
   r/D:   D=18        D=11       D=6        D=2
   q_r:   .0816(1/D=.0833)  .1105(.1111)  .1634(.1667)  .5004(.5000)
   q_r-q_{r-1}: ~ 1/(D(D+1)) throughout (e.g. D=8: .0116 vs 1/72=.0139; D=2: .174 vs .167).
```
So at typical `D = Theta(m)` the increment is `O(1/m^2)`, with room under the needed `o(1/m)`.

**(1.4) is tight up to `gamma/(gamma-1)`.** `ES_RHS = ((m-1)^2/n) E_r[q_r-q_{r-1}]` vs truth
`E||Pbar-I/m||_F^2`: ratio `1.47, 1.52, ~2` for `m=12,20,30` at `gamma=2` (`->` predicted
`gamma/(gamma-1)=2`). Efron-Stein is NOT the lossy step.

**The SOFT ceiling is exactly `O(1)` (the wall).** Using only the soft facts available without
(DELOC-EXP) -- `delta_r >= 0`, monotone in `r`, `sum_{r} delta_r = 1-1/m` -- one gets only
`delta_{r_typ} <= (1-1/m)/(D_typ-1) = O(1/D_typ) = O(1/m)`, hence `Var <= (m-1)^2/n * O(1/m) ->
1/(gamma-1) = O(1)`. Verified (`gamma=2`): `ES_soft = .82, .91, .95 -> 1` for `m=20,40,80`, while
`ES_true` (true `O(1/m^2)` increment) `= .048, .028, .026 ~ 2/m -> 0`. The soft route tops out at a
constant `1/(gamma-1)`, NOT `o(1)` -- the SAME barrier as `keystone_weak_deloc.md` Conclusion 1
(`1-1/C'`).

--------------------------------------------------------------------------------
## 3. Routes (b) martingale/Hoeffding and (c) direct 2nd moment land on the same input

**(b) Hoeffding / Hajek projection.** The order-1 ANOVA term is computable exactly. With
`Phi(a_1) := E[Pi_S | a_1]` (`S ni 1`, average over the other `m-2` rows),
`E[Pbar|a_1] = I/m + ((m-1)/n)(Phi(a_1) - I/m)`, so
```
   V_1 = sum_i E||P_i||_F^2 = ((m-1)^2/n) * ( E tr Phi(a_1)^2 - 1/m ) = ((m-1)^2/n)(q_1 - 1/m),
```
because `E tr Phi(a_1)^2 = E[|<u_S,u_{S'}>|^2 | share only row 1] = q_1` (overlap `r=1`, `D=m-1`).
So the FIRST-order term is the conditional overlap moment at `D=m-1` -- conditioning on a SINGLE
row, `E = span(a_1)` one-dimensional, the mildest possible conditioning. But (i) `V_1` alone is not
the variance (`Var = sum_k V_k`; the degree-weighted sum is (1.4)), and (ii) `q_1 - 1/m = o(1/m)`
is itself (DELOC-EXP) at `D=m-1`. Conditioning on one delocalized row reduces `(m,n) -> (m-1, .)`
in `a_1^perp` with projected-iso (not coordinate-symmetric) rows: the SAME obstruction, self-similar
one dimension down. So route (b) localizes the input to the most favorable `D=m-1` but does not
remove it.

**(c) Direct 2nd moment via the cofactor representation.** `u_S = w_S/||w_S||`, `w_S` = generalized
cross product (vector of signed `(m-1)x(m-1)` minors), `|rho|^2 = |<w_S,w_T>|^2/(||w_S||^2 ||w_T||^2)`.
Numerator `<w_S,w_T>` is a clean Cauchy-Binet/Plucker polynomial, but the normalizers
`||w_S||^2 = det(A_S A_S^*)` sit in the denominator and are coupled to it; `E[ratio]` does not
factor. This is exactly the hard-edge / determinant-ratio (small-ball) difficulty. Same wall.

--------------------------------------------------------------------------------
## 4. The precise residual obstruction

All three routes collapse the GLOBAL concentration to one local quantity:

> **(INC).** The conditional overlap moment `q_r = E[|rho|^2 | |S cap T|=r]` has increment
> ```
>     q_r - q_{r-1} = o(1/m)   at typical overlap r  (i.e. D = m-r = Theta(m)),
> ```
> equivalently `q_r = (1+o(1))/D` is Lipschitz in the overlap with slope `o(1/m)` there.

What is and is not available:
* PROVED soft facts: `q_0 = 1/m` exact; `q_r` nondecreasing; `delta_r := q_r-q_{r-1} >= 0`;
  `sum_r delta_r = q_{m-1}-q_0 = 1-1/m`; conditional isotropy pins `tr M_E = 1` (companions).
* These give ONLY `delta_{r_typ} = O(1/m)` (Section 2 ceiling), hence `Var = O(1)` -- the
  `keystone_weak_deloc.md` Conclusion-1 wall, now re-derived inside Efron-Stein. The numerically
  TRUE rate `delta_{r_typ} = O(1/D^2) = O(1/m^2)` (which yields `Var = O(1/m)`) is strictly sharper
  and is NOT implied by monotonicity + isotropy + the telescoping budget.
* (INC) is a genuine FOURTH-moment object: it correlates `|rho|^2` across the addition of one shared
  row, i.e. it asks how `E[uu^*|E]` flattens as the oblique subspace `E^perp` loses one random
  dimension. The §3.3 witness of `keystone_typical.md` (isotropic, non-Gaussian) makes `q_r` and its
  increments `Omega(1)` at small `D`; only the near-Gaussian SHAPE-REGULARITY of the projected rows
  (uniform in direction, no special axis) forces `q_r ~ 1/D` and `delta_r ~ 1/D^2`. Converting that
  into (INC) is a no-gaps-in-expectation theorem, not a soft CLT step (the map `g |-> u(g)` is
  non-Lipschitz near degeneracy; needs RV-type invertibility regularization).

So (INC) is the SAME residual RMT input as the companions' (DELOC-EXP): identical difficulty class,
merely re-expressed as a discrete derivative of the overlap moment. The reformulation via `Pbar` +
Efron-Stein is genuinely useful -- it is a TIGHT reduction (loses only `gamma/(gamma-1)`), it
pinpoints that low-order interactions dominate, and it shows precisely why every soft route ceilings
at `O(1)` -- but it does not close the keystone unconditionally.

--------------------------------------------------------------------------------
## 5. Verdict

**Proved (rigorous, this note).**
1. The exact reduction (0.3): `E_pair|rho|^2 = 1/m + E||Pbar - I_m/m||_F^2` (deterministic split).
2. The Efron-Stein identity (1.3)-(1.4): the per-row resampling effect telescopes EXACTLY to
   `2(q_r - q_{r-1})`, giving `E||Pbar-I/m||_F^2 <= ((m-1)^2/n) E_r[q_r-q_{r-1}]`, tight up to
   `gamma/(gamma-1)` (Efron-Stein = `sum_k k V_k`, low-order dominated).
3. A rigorous NEGATIVE result: the soft facts (`delta_r>=0`, monotone, `sum = 1-1/m`, isotropy)
   force only `delta_{r_typ}=O(1/m)`, hence `Var <= 1/(gamma-1)+o(1) = O(1)` -- NOT `o(1)`. The
   `O(1)` ceiling of `keystone_weak_deloc.md` is reproduced from a different (global/Efron-Stein)
   direction, confirming it is structural, not an artifact of the polar-cap method.
4. Routes (b) Hajek (`-> q_1`, `D=m-1`) and (c) cofactor/Cauchy-Binet (`-> det`-ratio) reduce to the
   same input.

**Open (named precisely).**
5. (INC): `q_r - q_{r-1} = o(1/m)` at typical `D = Theta(m)` `<=>` (DELOC-EXP) of the companions.
   Numerically TRUE with room (`= O(1/m^2)`), distribution-free (gauss/exp/rad/unif, symmetric or
   not), but provably not deducible from the soft facts; it is the no-gaps-in-expectation /
   fourth-moment theorem the keystone has needed all along.

**Net: PARTIAL (not closed).** Route (a) Efron-Stein, on the clean `Pbar` reformulation, is the
correct and tight machine and reduces the keystone's last input to a single, sharply localized,
numerically-verified increment bound (INC) -- but (INC) is a genuinely new RMT theorem of the SAME
difficulty class as (DELOC-EXP), not a soft consequence of what is proved. So the keystone's last
piece is NOT closed unconditionally here; it requires that theorem, now stated in its most
accessible form (a discrete `r`-derivative of the overlap moment, dominated by low-order
interactions, at the maximally favorable end `D=m-1` for route (b)).
