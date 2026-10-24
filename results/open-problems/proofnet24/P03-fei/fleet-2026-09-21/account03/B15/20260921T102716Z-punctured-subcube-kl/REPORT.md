# B15 — punctured-subcube obstruction: the residual normalizer still needs the KL credit

**Status: OPEN / PARTIAL. Full uniform-cube FEI is not proved here.**  
**Execution context: WITHOUT_VERIFIED_BRAIN.** No authenticated brain retrieval/context was used in this mathematics.

This run followed the live B15 spectral-remainder assignment. It first attacked the large-bias residual-normalizer target left by the packet free-energy handoff, then switched to APPROACHES route 4 (mass-weighted coefficient depth) when that target was rigorously refuted. No novelty claim is made.

## 1. Inherited exact packet identity

For a Boolean function `f`, group equal nonzero Fourier magnitudes `a`. Let

- `A_a={S: |fhat(S)|=a}`,
- `p_a=|A_a| a^2`,
- `V_a=sum_{S in A_a} sign(fhat(S)) chi_S`,
- `r_a=min_{V_a(x)!=0} nu_2(V_a(x))`,
- `b_a=a 2^{r_a}`,
- `N_a=|A_a| 4^{-r_a}=p_a/b_a^2`.

The inherited spectral-lattice continuation proves

`H(f)=2 sum_a p_a r_a + 2 D(f)`, where `D(f)=sum_a p_a log2(1/b_a)`.

The immediately preceding B15 handoff rewrites

`2D = log2 N - D_KL,2(p||q)`, `N=sum_a N_a`, `q_a=N_a/N`.

When `m=|Ef|>1/2`, the constant packet is isolated. Put `v=1-m^2`, let `N_perp` denote the sum over nonconstant packets, and normalize the nonconstant distributions by

`p~_a=p_a/v`, `q~_a=N_a/N_perp`.

Then, exactly (not merely by log-sum),

`2D = m^2 log2(1/m^2) + v[ log2(N_perp/v) - D_KL,2(p~||q~) ].`   (1)

Dropping the negative KL term gives the inherited sufficient target

`v log2 max(1,N_perp) <= K I(f)`                                           (2)

for a universal finite `K`. The exact statement attempted in this run was whether (2) can hold, perhaps after restricting to `|Ef|>1/2` or even to a fixed stronger bias.

## 2. REFUTED: no universal residual-normalizer coefficient exists

Fix an integer codimension `c>=2`. For each `n>c`, let `B` be a codimension-`c` coordinate subcube of `F_2^n` containing `0`, let

`A=B\{0}`

and define

`f_{n,c}=1-2 1_A`.

Write `d=n-c` and `M=|A|=2^d-1`. Then the minority density, mean, and two nonconstant Walsh magnitudes are

`delta=2^{-c}-2^{-n}`,

`m=Ef=1-2^{1-c}+2^{1-n}`,

`a_H=2^{1-c}-2^{1-n}=2 delta`,

`a_L=2^{1-n}`.

For every fixed `c>=2`, `m>1/2`; for `c=3`, for example, `m -> 3/4`.

### Exact Fourier calculation

Let `K(S)=sum_{x in A} chi_S(x)`, and let `H=B^perp`, so `|H|=2^c`. Since `A` is a subcube with one point removed,

`K(S)=M` for `S in H`, and `K(S)=-1` for `S notin H`.

Thus the nonconstant Fourier spectrum has exactly two magnitude packets:

1. **High packet:** `H\{empty}`, size `L_H=2^c-1`, magnitude `a_H`, sign negative.
2. **Low packet:** the complement of `H`, size `L_L=2^n-2^c`, magnitude `a_L`, sign positive.

For the high signed mask,

`V_H=-sum_{S in H\{empty}} chi_S`

takes the values `-(2^c-1)` on `B` and `+1` off `B`. Hence

`r_H=0`, `N_H=2^c-1`.

For the low signed mask,

`V_L=sum_{S notin H} chi_S = sum_all chi_S - sum_{S in H} chi_S`

takes the values `2^n-2^c=2^c(2^{n-c}-1)` at `0`, `-2^c` on `B\{0}`, and `0` off `B`. Hence

`r_L=c`,

`N_L=(2^n-2^c)/4^c = 2^{n-2c}-2^{-c}`.

Therefore

`N_perp = 2^c-1 + 2^{n-2c}-2^{-c}`.                                (3)

### Exact influence

For each of the `c` fixed coordinates, an edge crosses the minority set exactly when its endpoint in `B` lies in `A`, so its influence is `a_H`. For each of the `d=n-c` free coordinates, the only crossing edge inside `B` is the edge incident with the removed origin, so its influence is `a_L`. Consequently

`I(f_{n,c}) = c a_H + (n-c) a_L`

`             = c 2^{1-c} + (n-2c)2^{1-n}`.                       (4)

Also

`v=1-m^2 -> v_c := 2^{2-c}-2^{2-2c} > 0`.

Combining (3) and (4), for every fixed `c>=2`,

`[v log2 N_perp]/I`

`= [(2-2^{1-c})/c] (n-2c) + O_c(1)` as `n -> infinity`.             (5)

The coefficient is strictly positive. Hence

**REFUTED:** There is no finite universal `K` for (2), even if one requires a fixed strong bias. In fact, for any `m_0<1`, choose fixed `c` large enough that `1-2^{1-c}>m_0`; then this same family has `Ef>=m_0` eventually while the ratio in (2) diverges linearly in `n`.

This refutes only the raw residual-normalizer shortcut. It is not a counterexample to FEI.

## 3. Why FEI survives: the residual KL credit cancels the entire linear divergence

The two nonconstant packet masses are

`p_H=(2^c-1) a_H^2`,

`p_L=(2^n-2^c) 2^{2-2n}`,

and `p_H+p_L=v`. Their residual normalized-energy masses are `N_H,N_L` above. Therefore, with

`alpha=p_H/v`, `beta=N_H/N_perp`,

the residual KL term in (1) is exactly the binary divergence

`D_KL,2(p~||q~)=d_2(alpha||beta)`.

For fixed `c`, `alpha->1` while

`beta=(2^c-1)/N_perp = (2^c-1) 2^{-(n-2c)}(1+o(1))`.

Thus

`D_KL,2(p~||q~) = n-2c-log2(2^c-1)+o(1)`,                         (6)

whereas

`log2(N_perp/v)=n-2c-log2(v_c)+o(1)`.

Their difference stays bounded and in fact tends

`log2[(2^c-1)/v_c] = 2(c-1)`.                                    (7)

So the exact negative KL credit in (1) cancels **all** of the spurious `Theta(n)` normalizer growth. The family gives an explicit all-dimensional reason that a B15 remainder proof must preserve packet-mass/normalized-energy mismatch; multiplying the raw normalizer by the residual variance `v` is still not enough.

For comparison, the arithmetic remainder itself is harmless here. The exact formula is

`D = m^2 log2(1/m) + p_H log2(1/a_H) + p_L (n-c-1)`,              (8)

so for fixed `c`, `D/I` has a finite limit. The full entropy also stays `O(I)` on this family.

### Current-run numerical calibrations from the exact formulas

For `c=3`:

| n | mean m | I | N_perp | v log2(N_perp)/I | D/I | residual KL |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 0.7578125 | 0.765625 | 10.875 | 1.9144 | 1.4763 | 0.4444 |
| 12 | 0.7504883 | 0.752930 | 70.875 | 3.5659 | 1.4793 | 3.3099 |
| 16 | 0.7500305 | 0.750305 | 1030.875 | 5.8360 | 1.4781 | 7.1993 |
| 20 | 0.7500019 | 0.750027 | 16390.875 | 8.1667 | 1.4780 | 11.1930 |

The divergent quantity is precisely the one that discarded KL; `D/I` remains about `1.478`.

For `c=4`, the bias tends `7/8`; the same ratio grows from `1.7626` at `n=8` to `5.6271` at `n=20`, while `D/I` tends about `1.7013`.

As a separate counterexample test before finding this family, exhaustive `n=4` search gave maximum `v log2(N_perp)/I = 1.83135`, while an exact `n=5` example with minority set `{0,1,2,3,18,25,28}` already gave `2.16746`. The punctured-subcube family upgrades that finite warning to the rigorous divergence (5).

## 4. Switch after the dead route: APPROACHES #4 (mass-weighted coefficient depth)

The raw-normalizer route is now dead. The useful quantity is not how many normalized integer packet states exist, but how much **spectral mass** sits at a given Fourier depth.

For the same family, the low packet has exponentially tiny coefficient magnitude `a_L=2^{1-n}` but also exponentially tiny spectral mass

`p_L=(2^n-2^c)2^{2-2n}=2^{2-n}-2^{c+2-2n}`.

Its direct entropy contribution is

`p_L log2(1/a_L^2)=2p_L(n-1)=O(n2^{-n})`,                         (9)

while the high packet carries asymptotically all nonconstant mass at fixed depth `c-1`. Thus the family that makes `N_perp` exponentially large is easy for the actual mass-weighted log-loss in APPROACHES #4. This is a concrete reason to replace raw state counting by a mass-aware multiscale estimate.

A useful exact coarse-graining inequality is available for the next run. For any partition `{B_j}` of nonconstant packet labels, put

`P_j=sum_{a in B_j} p_a`, `M_j=sum_{a in B_j} N_a`.

The log-sum inequality gives

`sum_{a nonconst} p_a log2(N_a/p_a) <= sum_j P_j log2(M_j/P_j)`.   (10)

One giant bin is exactly the refuted raw-normalizer relaxation. Keeping separate mesh/magnitude bands retains part of the KL credit; on the punctured-subcube family, the two natural bins `{H}` and `{L}` make (10) an equality.

**CONDITIONAL next target (not proved):** find a Booleanity-driven, dimension-free way to choose a bounded-cost *adaptive* packet partition for which the right side of (10) is paid by influence. This is narrower and more faithful than (2), because it cannot erase the cancellation exhibited in (6)-(7). A successful version would feed directly back into `H=2 sum p_a r_a+2D`.

## 5. Status ledger

- `H(f)<=C I(f)` for all Boolean `f`: **OPEN**.
- Spectral-lattice identity `H=2 sum p r+2D`: **PROVED previously / used as input**.
- Packet free-energy identity with negative KL: **PROVED previously / sharpened here by the exact residual form (1)**.
- Universal `v log N_perp <= K I`: **REFUTED here** by the punctured codimension-`c` family, with exact asymptotic divergence (5).
- Fixed-bias rescue of that raw-normalizer inequality: **REFUTED here** for every bias threshold `<1`.
- Mass-aware adaptive coarse-bin payment from (10): **OPEN / CONDITIONAL target**.

## 6. Next attack

Stay on APPROACHES #4 and the arithmetic remainder, but do not count `N_perp` in one bin again. Group packets by dyadic mesh depth `floor(log2(1/b_a))` or by coefficient-depth bands, retain the exact binwise log-sum/KL credit, and look for a Booleanity inequality that charges each occupied band to its actual influence contribution. The punctured-subcube family is now a mandatory stress test: any valid candidate must give `O(1)` total charge although `N_perp` is exponential.
