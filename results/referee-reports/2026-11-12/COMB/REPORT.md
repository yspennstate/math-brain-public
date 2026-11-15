Overall verdict: SOUND WITH GAPS

The proof is incomplete as written. I found a concrete gap in the proposed repair of the coarse walk (line 74), upstream of the exit estimate and the quantitative good-environment lemma. Changing to visits to a **different** coarse-grid point changes the clock. The assertion that a crossing necessarily completes a tooth excursion is false. A quantitative local-time argument can repair this; I give one below. I found no counterexample to Theorem 1.1. Conditional on the stated heat-kernel inputs, the spatial averaging, single-logarithm second-moment calculation, restart conditioning, and conditional Borel–Cantelli argument work.

There is a necessary limitation on the citation audit. The folder contains `PAPER.tex` and the authors' numerical script/output, but no DNNS manuscript or source, nor the other cited works. I used no browsing. Consequently I cannot certify what the original numbered DNNS statements actually say, their parameter restrictions, or the claimed errors in them. Below, “conditional” means conditional on the explicitly stated inputs in this paper, not confirmation against the original source. This distinction matters especially for Lemma 4.1. An unconditional acceptance recommendation would require the missing source audit as well as the repair.

Line numbers refer to the supplied, unmodified `PAPER.tex`. I did not run the authors' program. All computations below use newly written programs in this folder.

## Theorem 1.1 — GAP

**Statement:** lines 46–48. **Proof:** lines 332–344.

The theorem follows from Lemma 5.1 by the restart argument printed here. The outstanding gap is in the inputs to that lemma, principally the coarse-clock repair and its propagation into Lemma 4.1. This is a gap in the proof, not a demonstrated false theorem.

I checked the conditioning in Section 5 in detail:

* The boxes are finite and nested. Their first exit times are finite stopping times for the joint walk. For sufficiently large scales, both initial vertices are inside the smaller box. At its first exit, both walks are inside or one step outside that box. Thus their coordinates satisfy the bounds placing them in `S_N`.
* With `N_m=b^m`, the enlarged box at scale `N_m` is exactly the next box. It contains the restart positions. No earlier exit from this larger box could have occurred before the first exit from the smaller one. The restarted killing time is therefore `sigma_(m+1)-sigma_m`.
* Lemma 5.1 is uniform over **both** restart vertices in `S_N`, rather than merely over a common backbone start. This is the uniformity needed for the strong Markov step. The earlier-time upper kernels used to obtain it have times of order `N^3`; their applicability does not depend on the restart heights once Lemma 2.2 is available.
* A restarted `H'_N>0` produces a collision in `[sigma_m,sigma_(m+1))`, so it implies `Col_m`. The bound is conditional on the whole joint past `F_m`, with the environment fixed. It is at least a fixed positive constant times `1/(m log b)`.
* `Col_m` belongs to `F_(m+1)`, as required. The shifted filtration and events in line 343 have the correct indices. In the quenched argument, `m_0` depends on the fixed environment and fixed initial vertices, not on the walk trajectories. Taking a trivial initial sigma-field for the first shifted event is legitimate: its unconditional probability is obtained by integrating the displayed conditional bound.
* Conditional Borel–Cantelli needs no independence between successive scale events. Its conditional-probability sum diverges. The time intervals are disjoint, so infinitely many successful intervals yield distinct collision times. Also `sigma_m` tends to infinity: a finite walk path cannot leave boxes of arbitrarily large horizontal and vertical extent.

The parity argument is **SOUND**. The colour of `(x,h)` is `x+h mod 2`. Each walk changes colour at each step, so equality of their colours is preserved. Odd initial distance makes a collision impossible. Even distance allows the two lower kernel bounds to hold at the same half of the times for each target. It is preserved at every simultaneous restart. No additional synchronisation assumption is being made.

There are countably many vertex pairs. The environment estimates are already uniform over their scale windows, so the full-measure environment set need not be selected anew for each realised restart position.

## Lemma 2.1 (`off`) — GAP, minor endpoint repair

**Lines 80–100.** The intended proof is valid conditional on the exit and diagonal bounds, after an interval-endpoint correction.

At line 87, reaching a point at distance `floor(d/2)` does not imply exit from the **closed** interval of that half-width. Apply the exit estimate instead at half-width `floor(d/2)-1`, or another fixed smaller fraction of `d`. For large scales this remains comparable to `d` and exceeds the lower cutoff because `delta_1<delta_3/3`. This gives the same bound with changed constants. When the resulting time ratio exceeds one, use the trivial probability bound; in that range `d^3/n` is bounded, so the desired stretched-exponential expression still holds after increasing its prefactor.

The rest is sound:

* Every path to the other backbone point crosses the midpoint. Splitting into early forward crossing and late crossing reversed in time is valid. Reversibility costs at most a factor three.
* The Chapman–Kolmogorov/Cauchy–Schwarz calculation uses the reversible measure `deg`, and the diagonal times are `2 floor(r/2)` and `2 ceil(r/2)`. They are even, eliminating the parity problem.
* Using a strictly smaller diagonal cutoff, as line 95 expressly does, puts `n/2-1` in range.
* `n^(-2/3) exp(-c(d^3/n)^beta)` is bounded by a constant times `d^(-2)` because `u^(2/3) exp(-cu^beta)` is bounded for `u>=1`.

There is no logarithm in this lemma. I cannot confirm the paper's description of DNNS equation (4.100) without that source.

## Lemma 2.2 (`gen`) — SOUND conditional on the stated backbone bounds

**Lines 104–124.** The repair of the hitting-time convolution works.

Folding a simple walk on `[0,2H]` about `H` gives precisely the tooth walk reflected at its actual top and stopped at its root. To bound the hitting-time density, dominate by the sum of unrestricted first-passage densities to the two endpoints. For an endpoint at distance `a`, the first-passage identity gives `(a/s) P(S_s=a)`. The local Gaussian bound, followed by absorbing `a/sqrt(s)` into a weaker Gaussian, gives `C s^(-1) exp(-h^2/(Cs))`, uniformly in `H>=h`. The cumulative bound follows from the maximal inequality. The two endpoints both have distance at least `h`.

The three contributions are respectively

```
C n^(-2/3) exp(-h^2/(Cn)),
C n^(-1) exp(-h^2/(Cn)) sum_(j<=n/2) j^(-2/3),
C n^(-1) exp(-h^2/(Cn)) sum_(j<2sqrt(n)) (1+j)^(-1/2).
```

The last two are `O(n^(-2/3))` and `O(n^(-3/4))`, with the same type of Gaussian factor. The strict hierarchy `delta_3<delta_4/2` makes the middle-range diagonal inputs available. There is no hidden logarithm. The case `h=0` follows from the backbone Cauchy–Schwarz bound, with suitably lowered input cutoffs.

The example at line 102 does demonstrate why a purported `n^(-7/6)` bound for the entire convolution would fail at height one. Whether that is what DNNS printed remains unverified.

## Lemma 2.3 (`low`) — SOUND conditional on the stated hitting and exit inputs

**Lines 134–159**, including the lower-diagonal input at lines 128–132.

The order of constants removes the circularity described in the paper: choose the intermediate hitting box `d`, then `c_l`, then `c_u`, and only then the killing enlargement `b`. The commute-time estimate applies to a finite network with the exterior boundary glued to one vertex. The time to hit the target or that boundary is bounded by the unrestricted target-hitting time in that finite network. Its edge count is `O(N^2)` and the resistance between the backbone roots is at most `3N`. The preliminary descent/exit of the starting tooth costs `O(N^3)` as claimed.

The volume bound can be checked independently. For fixed `d`, truncate heights at `L=O(N^(3/2))`. The tail assumption gives

```
E min(H,L) = O(L^(2/3)),
E min(H,L)^2 = O(L^(5/3)).
```

Summing over `O(N)` independent teeth gives mean `O(N^2)`, variance `O(N^(7/2))`, and summand bound `O(N^(3/2))`. Bernstein's inequality bounds an excess of order `N^2` by `exp(-c sqrt(N))`. This is summable even over all integer `N`. The additional glued-boundary edges are `O(N)`. Thus the claimed volume estimate has the right strength at the critical exponent; it introduces no logarithmic correction.

The diagonal lower bound is also consistent with a direct survival/volume argument, conditional on the exit estimate. At time `j`, use a box about the target with horizontal radius `K j^(1/3)` and height `K sqrt(j)`, for a fixed sufficiently large `K`. Horizontal exit is unlikely by (E1). Vertical height is dominated by a reflected nearest-neighbour walk with holding at zero: couple using the same up/down coins, suppress up moves at actual tooth tops, and at a root use up probability at most `1/3`, versus `1/2` for the dominating walk. Its maximal height has a Gaussian bound. The box therefore has survival probability bounded below. Its degree volume is `O(j^(2/3))` on the corresponding volume event, by the same Bernstein calculation. Reversibility and Cauchy–Schwarz yield

```
q_(2j)^D(w,w) / deg(w)
    >= P_w(tau_D>j)^2 / sum_(u in D) deg(u).
```

These smaller boxes fit inside `B_b` for `j<=C_u N^3` when `b` is chosen afterwards. This explains both the restricted time range and why the lower constant can be independent of `C_u`. The necessary volume events can be made uniform over the polynomially many centres and times in the stated window; their failure probabilities are stretched exponential above the polynomial lower cutoff.

The rest of the printed proof is correct. A hitting probability at least `3/4`, minus a Markov-inequality loss at most `1/4`, gives at least `1/2`. The even diagonal of a killed reversible chain decreases with even time, including when eigenvalues are negative. This permits small residual times `n-s`, even zero, without applying the large-time lower bound there. Parity ensures that residual times are even. The multiplication of killed kernels at line 157 counts exactly the before-exit collisions; free kernels would not.

Actual applicability of the quoted DNNS Lemma 4.5 to the enlarged start set still requires checking against its source. I found no internal contradiction in its use here.

## Lemma 3.1 (`large`) — SOUND conditional on the upper kernel chain

**Lines 168–181.** Near the starting site there are `O(n^(1/3))` backbone targets, each with kernel at most `C n^(-2/3)`. Farther away, summing `d^(-2)` gives `O(n^(-1/3))`. Thus the total backbone probability is `O(n^(-1/3))`. Multiplication by the supremum kernel gives

```
sum_y q_n((z,0),(y,0))^2 <= C n^(-1).
```

Summing from `N^delta` to `C_0 N^3` gives `(3-delta) C log N+O(1)`. This is one logarithm.

The displayed choices `delta_3=delta/3`, `delta_4=3delta/4` satisfy the inequalities used here. However, “may be taken as small as we please” is not by itself assurance that these particular numerical values satisfy every DNNS parameter restriction. The proof needs only an admissible sufficiently small hierarchy `delta_1<delta_3/3`, `2delta_3<delta_4<delta`; use that hierarchy if the original restrictions are stronger.

## Lemma 3.2 (`cap`) — SOUND

**Lines 183–203.** This is a valid deterministic bound for every comb in this paper, including non-lazy walks and teeth of height zero.

Each colour-class distance-two graph is connected, infinite, and has bounded degree. Every nonempty finite subset has a boundary edge. Its edge weights in `P^2` are uniformly positive, and degree measure is comparable to counting measure. The asserted one-dimensional Nash inequality can be obtained without relying on the exact CSC citation: telescope `f^2` along an infinite path from a vertex where `|f|` is maximal, apply Cauchy–Schwarz, and combine the resulting bound on `||f||_infinity` with `||f||_2^2<=||f||_1 ||f||_infinity`.

`P^2` is positive and self-adjoint on a colour class. The energy recurrence gives `u_j=O(j^(-1/2))`; duality gives the normalized kernel bound, and degrees cost at most a constant. Odd times follow by one transition. Passing from the displayed even powers of `Q` to intervening powers uses its contraction property, a routine semigroup step. Summing `sum_y q_k^2<=sup_y q_k` gives `O(sqrt(b))`. No logarithm is lost.

I have verified the argument, not the exact statement or attribution in CSC.

## Lemma 3.3 (`range`) — SOUND

**Lines 205–219.** The horizontal jump skeleton is a simple symmetric walk, with at most `k` jumps by physical time `k`. Although the number of jumps depends on the path and environment, the pathwise inclusion in the maximum event for its first `k` skeleton steps suffices. No independence between this clock and skeleton is needed.

The exponential maximal bound follows from `cosh(lambda)<=exp(lambda^2/2)` and optimisation. Killing subtracts a nonnegative transition mass whose total is at most the exit probability. The squared-kernel difference is at most twice that mass. This gives the constant `4b` in the statement. Killing leaves the original exit probabilities in place; it does not renormalize transitions at the boundary. Consequently only tooth heights within the interval are needed, including its endpoints.

## Lemma 4.1 (`A0`) — GAP

**Lines 228–247**, with an upstream **ERROR in the proof assertion at line 74**.

The quantitative failure bound is indispensable. An almost-sure eventual quenched bound alone cannot be integrated to give Lemma 4.2. The proof correctly recognises this and attempts to extract the necessary rates from DNNS. The following parts of that extraction are internally sound, assuming its stated source inputs:

* The fixed small dyadic `t_0` addresses the mean-versus-threshold issue. For larger `t`, the probability bound can be made trivial by its prefactor.
* The unconditioned occupation event described in line 240 is monotone as `t` increases: eligible roots are removed while the threshold increases. This permits dyadic interpolation. The non-monotone intersection with `A(n,t)` is not interpolated.
* Intersecting the events for polynomially many centres/radii and logarithmically many times preserves a stretched-exponential failure bound. The count is `O(m^2 log m)` and the extra `n` in the per-event bound gives `O(m^3 log m)` overall.
* The interval locality is adequate: centres at most `2m`, radii at most `4m`, and the stated extra extension at most `m` fit in `[-8m,8m]` for sufficiently large scales. Finitely many small scales can be absorbed in constants.
* The diagonal-input radii and the even times needed later in Lemma 4.2 lie in the asserted ranges. In particular the off-diagonal calculation only asks for diagonal times at least `ell^3/2-O(1)`, above `ell^3/4`.

The problem is Case 2. First visits to a different point of a grid of spacing `D` indeed give a simple symmetric coarse chain. But, already for the ordinary backbone trace,

```
E_0[next visit after time 0 to D Z] = D,
E_0[first visit to {-D,D}] = D^2.
```

The old recording has holding probability `1-1/D`; removing those recordings changes the clock by factor `D`. Therefore estimates involving recorded counts or accumulated local time do not follow just because the new spatial chain is simple.

Moreover, crossing a deep root does not force a tooth excursion. If all relevant teeth have positive height, the path `(0,0),(1,0),(2,0),(3,0)` has probability `1/27` and contains no tooth excursion, regardless of how high the tooth at 1 or 2 is. For spacing `3L`, the analogous straight crossing has probability `3^(-3L)>0`. This remains a counterexample to the deterministic implication when the selected root is arbitrarily deep and the finite environment satisfies the proposed deep-root condition.

**A quantitative repair.** The following supplies the missing factor rather than ignoring it. Work with the horizontal trace and grid spacing `3L`. Suppose each middle third of a grid gap contains a selected eligible deep root. Conditional on a recorded step from 0 ending at `3L`, it crosses a selected root `a in [L,2L]`. The number `K` of visits to `a` before the step ends is geometric with parameter

```
p_a = (1/2)(1/(3L-a)+1/(3L+a)) <= 3/(5L).
```

To see this, split excursions from `a` according to return, terminal escape to the left, and terminal escape to the right. Conditioning on the terminal direction changes the terminal normalisation but leaves the geometric return factor unchanged. Thus `P(K>=cL)` is bounded below uniformly in `L` and in the selected root. The same holds for a left-going step. By the strong Markov property, these visit counts are independent conditional on the coarse directions, with parameters satisfying this uniform bound. A Chernoff bound gives

```
P(total selected-root visits over M complete coarse steps < c L M
  | coarse directions) <= exp(-c' M).
```

This restores exactly the missing factor `L`. If the required quantity counts tooth excursions rather than trace visits, add an explicit thinning argument: at each root visit the chance of at least one vertical excursion before the next horizontal jump is `1/3`, independently of the horizontal direction. A second Chernoff bound gives the corresponding lower bound for excursion counts; it is not a deterministic implication.

For completeness, this repair has the required strength in the small-`t` regime described in the paper. Write `a_0=1/2-alpha>0`, take `t=n^(-epsilon)`, and let the required count be `A=n^(3/2-epsilon*a_0)`. With `L=O(sqrt(n))` as asserted in line 242, take `M` a sufficiently large constant times `A/L`. Premature spatial exit before these coarse steps has probability at most `C exp(-c n^2/(L^2 M))`; insufficient selected-root local time has probability at most `C exp(-c M)`. These are bounded by

```
C exp(-c n^kappa),  kappa=min(epsilon*a_0,1-epsilon*a_0)>0,
```

after choosing the small parameters so `epsilon*a_0<1`. Endpoint margins in the coarse interval change constants only. This is a stretched-exponential rate, which is all the later union bound requires. The actual definition of `O_n(x)` must be checked to ensure it supplies the selected middle-third roots and their eligibility.

The small-`t` cutoff also needs an unambiguous occupation definition. A root visit is forced by a crossing; a strictly positive vertical excursion is not. If the DNNS occupation includes the root/trace visits, the integer-count cutoff at line 72 can be used, and its displayed exponent arithmetic is correct. If it excludes them, that emptiness assertion is false. For the **exit estimate actually needed here**, one can instead extend a stretched-exponential exit bound at `t=n^(-epsilon)` by monotonicity down to the deterministic minimum exit time: exit from the closed radius-`n` interval takes at least `n+1` steps. Below `(n+1)/n^3` the exit event is empty; above it choose, for example, `2 beta<=kappa`. This avoids claiming that a vertical excursion is forced.

The paper must write this clock/local-time argument and propagate its possibly changed positive exponents through the event rates and cutoffs. “(4.57)–(4.63) go through” does not do that. Until then, the rate extraction and hence this lemma are not proved by the supplied text.

## Lemma 4.2 (`A`) — GAP inherited from Lemma 4.1; subsequent calculation SOUND

**Lines 249–266.** Conditional on the claimed good event, the calculation is correct.

For `k in [ell^3,8ell^3)`, the local diagonal bound and the repaired off-diagonal argument give supremum backbone kernel `C k^(-2/3)` and total local backbone mass `C k^(-1/3)`. Their product is `C/k`. The complementary horizontal mass is at most `2 exp(-(log(ell+2))^2/16)`. Squared masses are bounded by masses there. Summing over the block yields a deterministic constant: although it can be very large, `ell^3 exp(-(log(ell+2))^2/16)` is bounded on `ell>=1`.

On bad environments the cap gives `S_ell<=C ell^(3/2)`. For its first and second annealed moments, the bad-event contributions are at most `C ell^(3/2) P(G_ell^c)` and `C ell^3 P(G_ell^c)`. Choosing a polynomial failure exponent greater than three suffices. No independence between `S_ell` and the good event is assumed or needed.

This proves a constant bound **per multiplicative time block**, not for the whole interval `[1,ell^3]`. That distinction is necessary when describing the result in the abstract and strategy.

## Lemma 4.3 (`small`) — SOUND conditional on Lemma 4.2

**Lines 270–294.** The averaging is over the correct environment variables, and the block independence and union over scales are valid.

* The time blocks `[2^(3j),2^(3j+3))` cover the requested half-open time interval. There are `O(log N)` blocks.
* `m_j=13 sqrt(log N) ell_j^(3/2)` is deliberately a diffusive spatial truncation radius, larger than the typical horizontal travel scale. The deterministic skeleton bound applies without a typical-environment assumption. Its exponent is `(169/16) log N>10 log N`, so the cumulative killing error is at most one for large `N`.
* Each killed variable depends on precisely a finite interval of independent tooth heights. Variables whose intervals are disjoint are independent. Overlapping variables need only Cauchy–Schwarz covariance bounds. No independence between different time scales is claimed.
* The target restriction `|y|<=N` and the killing only decrease the variable below `S_ell_j(z)`. Stationarity of that full variable supplies the uniform first and second moment bounds even though the restricted variable itself depends on `N` and `z`.
* The covariance count gives `Var Sigma_j<=C N(m_j+1)`. Minkowski followed by a geometric sum gives `sqrt(Var Sigma)<=C N^(1/2+delta/4)(log N)^(1/4)`. In particular, this sum does **not** introduce another `log N`.
* Chebyshev at deviation `N log N` gives `C N^(-1+delta/2)(log N)^(-3/2)`. For `delta=1/2` this is `C N^(-3/4)(log N)^(-3/2)`. It is summable on dyadic `N`. First Borel–Cantelli requires no independence between scales. Monotonicity of the full target, starting-site and time ranges then extends the estimate to all `N`.

The exceptional profiles have measure zero. The starting-site sum is already included before the probability bound, so no missing union bound over `z` remains. The only logarithm in the resulting mean bound is the number of time blocks.

## Lemma 5.1 (`moments`) — SOUND conditional on its stated kernel and averaging inputs

**Lines 302–330.** This is the claimed spatial averaging step, and it works.

For the earlier time `n` in the scale window, both starts may be anywhere in `S_N`. Lemma 2.2 yields, uniformly in each collision site `x`,

```
q_n(v,(x,0)) q_n(w,(x,0)) <= C n^(-4/3) <= C N^(-4).
```

This is a bound on transition probabilities, not normalized densities with an unaccounted reversible weight. The collision site is therefore summed with **counting measure**. Factors from converting `p` to `q` are bounded by degree three and have already been absorbed into constants. No degree-biased or collision-biased average has been substituted.

For `n<n'`, the Markov property gives the product of the earlier kernels times `sum_y q_(n'-n)((x,0),(y,0))^2`. Dropping killing is an upper bound. Summing the earlier time gives `O(N^3) N^(-4)=O(N^(-1))`, so the cross term is bounded by

```
(C/N) sum_(|x|<=N) G_[1,c_u N^3](x).
```

There is no supremum over `x` here. The first moment has powers `N^3 * N * N^(-4)=1`. The short-time and long-time sums are each `O(N log N)`; multiplying their **sum** by `1/N` gives `O(log N)`, not `O((log N)^2)`. The diagonal contribution to the second moment is `E H'_N=O(1)`.

The lower first moment follows from Lemma 2.3 using killed kernels and the common allowed parity. All upper estimates are uniform over the starts, which is precisely what Section 5 requires. The quantitative good-event gap remains an upstream obstacle to an unconditional conclusion.

## Checks, programs, and outputs

### Citation and range audit

The following table records what the supplied paper claims; the original DNNS text was unavailable, so none of the original statement numbers or original gamma restrictions is independently certified here.

| Input | Claimed original source and scope | Use in this proof; audit finding |
|---|---|---|
| (E1), exit | DNNS Lemma 4.7 via Proposition 4.6; claimed `0<gamma<1` | Needed at `gamma=1/3`, polynomially large radii, small time ratios, and polynomially many centres. The Case-2 repair has the clock/local-time gap above. |
| (E2), diagonal upper | DNNS Lemma 4.10; claimed `0<gamma<1` | Used above polynomial cutoffs, at even times after Cauchy–Schwarz. The deterministic resistance `(ell+1)/2` is correct for a closed radius-`ell` backbone interval with all teeth. The two exits are paths of length `ell+1` in parallel. |
| (E3), off-diagonal | DNNS Proposition 4.11 | The paper supplies its own argument instead of relying on the quoted proof. It works after the closed-interval correction, conditional on (E1)–(E2). |
| (E4), general start | DNNS Lemma 4.12 | The paper supplies a valid convolution repair. Needs a strict hierarchy of cutoffs. |
| (E5), first moment | DNNS Lemma 4.13 via Lemmas 4.5, 4.8, 4.9 | Rebuilt here using killed kernels, an enlarged start set, bounded time window, and reordered constants. Internally valid given the hitting/exit inputs; the actual source's start range needs confirmation. |
| Lower diagonal | DNNS Lemma 4.8 | Restricting its alleged all-time statement to times at most `C_u N^3` is necessary: a finite killed chain cannot have a polynomial lower bound for all times. The replacement is consistent with the survival/volume derivation above. |
| Quantitative environment rates | DNNS (4.37), (4.41)–(4.44), (4.47)–(4.48) | These are stronger inputs than almost-sure eventual bounds. Their precise conditional means, probabilities, locality, and admissible parameters must be supplied or checked in the original text. Lemma 4.1 currently asserts them by reference. |

The assertion at line 69 that `gamma>1/3` is used **only once** in DNNS cannot be verified from this folder. It should not be treated as an independently established fact of this referee report. What can be checked is that this paper's subsequent algebra has no remaining positive-power requirement `3gamma-1>0`, once its critical kernel and quantitative environment inputs are granted.

For the other references, the parity argument, conditional Borel–Cantelli application, and Nash argument were checked mathematically above. I cannot certify the precise theorem numbering in Durrett or the stated scopes of BPS, KP, CWZ, CC, HP, AM, DNS, and CD against their absent texts. Their introductory claims are not used as substitutes for the critical estimates in the proof. I found no internal misuse of those introductory claims. In particular, the HP result does not automatically apply merely by rooting this infinite-mean-tooth comb at a backbone vertex; the required reversible rooted-graph law would have to be established.

### Exponent and logarithm ledger

At `gamma=1/3`, exact rational arithmetic gives

```
4/(gamma+1) = 3,
(3-gamma)/4 = 2/3,
(gamma+1)/4 = 1/3.
```

Thus the quoted scaling is internally consistent: time `N^3`, backbone heat kernel `n^(-2/3)`, horizontal travel scale `n^(1/3)`, total backbone probability `n^(-1/3)`, and backbone collision density at time `n` of order at most `n^(-1)` in the stated regimes. These are backbone/root statements, not an on-diagonal bound uniform over every high vertex of every tooth.

| Operation | Size | Logarithms |
|---|---|---|
| First scale moment | `N^3 * N * N^(-4)` | none |
| Earlier-time sum in second moment | `N^3 * N^(-4)=N^(-1)` | none |
| One annealed time block | `sum_(ell^3<=k<8ell^3) C/k` | bounded, `log 8` |
| All small-time blocks, all starts | `O(N log N)` | one, from the number of blocks |
| Variance summation over block sizes | geometric sum | no extra logarithm; truncation contributes `(log N)^(1/2)` to variance |
| Large-time Green sum per start | `sum_(N^delta<=k<C N^3) C/k` | one |
| Second moment | `O(1)+N^(-1)[O(N log N)+O(N log N)]` | one total |
| Paley–Zygmund on `N=b^m` | at least `c/log N=c/(m log b)` | harmonic in the scale index |

The two Green-function logarithms are added, not multiplied. No `log log` loss arises in the concentration or restart argument. The proof gives a lower bound on scale-success probabilities; it gives neither an asymptotic collision count nor a matching lower bound on the second-moment ratio. In particular, it does **not** prove that total collisions grow like `log log t`. Summing the conditional lower bounds over the first `M` exit scales gives a lower bound of order `log M` on the expected number of successful intervals; relating the random exit-scale index to deterministic time needs further estimates.

### Exact rational checks: `referee_exact.py`

Output: `exact_checks.json`. No external numerical package is used. On an independently constructed small killed comb, the program propagates the joint pair chain with accumulated collision rewards and separately expands the moment over pairs of collision times. Results:

```
E H       = 2629303/3779136 = 0.6957418309370184
E H^2     = 4731197/3779136 = 1.251925572405968
uniform-earlier-kernel upper bound for E H^2 = 2.1894038743247135
pair-chain moment == pair-of-times expansion: true (exact fractions)
```

The exact coarse-clock checks give old/new mean recording times `3/9`, `9/81`, and `30/900` for spacings `3`, `9`, and `30`. The no-tooth-excursion crossing witness has probability `1/27`. For the proposed repair with `L=10`, selected root `a=15`, the geometric parameter is `2/45` and mean local time is `45/2`. These are checks of the algebra and the concrete failing assertion, not large-scale proofs.

### Independent long simulations: `referee_sim.c`

This implements the discrete-time **non-lazy** simple random walk, with independent walk streams and shared profile within each pair. Teeth have `H=floor(U^(-1/gamma))`, so for integer `h>=1`, `P(H>=h)=h^(-gamma)`. Profiles are generated on demand by a seeded coordinate hash; corresponding profiles across the three exponents use matched underlying uniforms. There are six profiles for each exponent, one walk pair per profile, all started at the origin.

No spatial boundary was reached: the storage guard is at horizontal distance 131072, versus observed distances below 1600. Heights exceeding `100000001` are stored at that value, which cannot affect any path up to time `10^8` from the origin. Actual tooth tops are reflected by a compulsory downward step. All collisions below exclude time zero. Full outputs also record backbone collisions, collision episodes, and maximum positions.

Commands, after compiling with `cc -O3 -std=c11 -Wall -Wextra referee_sim.c -lm -o referee_sim`:

```
./referee_sim long 0.25 simulation_subcritical.csv
./referee_sim long 0.3333333333333333 simulation_critical.csv
./referee_sim long 0.5 simulation_supercritical.csv
./referee_sim moments 0.3333333333333333 moments_critical.csv
```

Mean counts over six profiles:

| gamma | time | all collisions | backbone collisions |
|---|---:|---:|---:|
| 0.25 | `10^5` | 53.833 | 6.833 |
| 0.25 | `10^6` | 81.333 | 12.667 |
| 0.25 | `10^7` | 81.333 | 12.667 |
| 0.25 | `10^8` | 81.333 | 12.667 |
| 1/3 | `10^5` | 45.000 | 10.833 |
| 1/3 | `10^6` | 48.333 | 11.167 |
| 1/3 | `10^7` | 112.000 | 13.500 |
| 1/3 | `10^8` | 112.000 | 13.500 |
| 0.5 | `10^5` | 77.333 | 20.500 |
| 0.5 | `10^6` | 230.000 | 22.500 |
| 0.5 | `10^7` | 293.167 | 31.667 |
| 0.5 | `10^8` | 333.667 | 40.667 |

At `10^8`, critical all-collision counts by profile are `[60,121,64,36,330,61]`, and backbone counts are `[10,46,11,5,9,0]`. The supercritical all-collision counts are `[43,236,154,952,101,516]`. The plateaus and very uneven bursts prevent a meaningful fit to either `log t` or `log log t` with this sample. Even a supercritical profile may have no late collision during the observation window. These runs neither refute nor establish any almost-sure infinite-collision claim.

### Scale moments and a second numerical method

The paper leaves `c_l,c_u,b` non-numerical. Consequently it is impossible to simulate its particular unspecified constants. I used the explicitly defined version of its statistic with `c_l=1`, `c_u=2`, `b=4`, starts both at the origin, the inclusive time window `[N^3,2N^3]`, and killing on leaving `B_4`. These are numerical diagnostic choices, not a claim that they are the constants supplied by Lemma 2.3. Other starts, and the minimum over restart positions, are not tested by these simulations.

Monte Carlo uses six fixed profiles and 1200 independent pairs per profile for each of `N=4,8,16,32`, and 400 pairs per profile for `N=64`. The table pools first and second moments equally across profiles. Let `R` denote the ratio of these pooled moments, `E H^2/(E H)^2`; this is distinct from the average of six quenched ratios. Both are saved in `CHECK_OUTPUTS.txt`.

| N | estimated E H | estimated E H^2 | R | R/log N | estimated P(H>0) |
|---:|---:|---:|---:|---:|---:|
| 4 | 0.323333 | 1.265278 | 12.1028 | 8.7303 | 0.131806 |
| 8 | 0.315972 | 1.967361 | 19.7054 | 9.4763 | 0.090833 |
| 16 | 0.244306 | 1.779583 | 29.8162 | 10.7539 | 0.057361 |
| 32 | 0.245000 | 2.384722 | 39.7288 | 11.4633 | 0.050417 |
| 64 | 0.262917 | 3.022083 | 43.7190 | 10.5122 | 0.043750 |

`referee_numerics.py` independently constructs the killed transition matrix on these same finite rectangles and evolves probabilities. At a cut tooth it retains the original upward transition as killing; at a horizontal boundary it likewise retains the outgoing killing probability. It does **not** reflect artificial boundaries or renormalize surviving edges. It computes the first moment directly and the second from killed continuation kernels, without Monte Carlo. These are deterministic floating-point calculations, not interval-certified numerical proofs. Output: `numerical_checks.json`.

Pooled deterministic moments over the same six profiles:

| N | E H | E H^2 | R | R/log N |
|---:|---:|---:|---:|---:|
| 4 | 0.339165 | 1.300957 | 11.3094 | 8.1580 |
| 8 | 0.333535 | 2.085765 | 18.7492 | 9.0164 |
| 16 | 0.277480 | 2.281283 | 29.6290 | 10.6864 |

This broadly agrees with the Monte Carlo and is compatible with an approximately constant first moment and logarithmically growing moment ratio over the tested scales. It cannot distinguish asymptotic `log N` from `log^2 N` or exclude a later crossover. The individual quenched ratios vary substantially; for example at `N=16` they range from about 18.47 to 45.10. Sample second moments are sensitive to rare bursts: for profile 1 at `N=8`, the Monte Carlo second moment is about 3.9 of its plug-in standard errors below the deterministic value. I retained this discrepancy; a plug-in error estimate for such a skew statistic is not a reliable coverage guarantee.

`referee_summary.py` generates `CHECK_OUTPUTS.txt` from the raw outputs. The exact-fraction program, the C simulation, the deterministic matrix program, and the summary program are all saved here. The longest recorded numerical run took 24.6 seconds; the C output records about two seconds for each long-walk batch and five seconds for the moments batch. Computations ran sequentially, with one numerical worker and numerical-library thread counts set to one. The largest matrix calculation had 15068 vertices and 33 probability columns, far below 1 GB. No computation approached five minutes.

The authors' existing check uses a lazy walk, reflected height caps, a finite reflected horizontal interval, and a truncated Green function. It can illustrate behaviour, but does not test the non-lazy parity argument, the killed scale moments, uniform restart probabilities, environment failure rates, or the claimed DNNS repairs. Its output is not evidence that those proof steps hold.

## Corrections required

1. **Line 74, coarse recording and “completes an excursion.”** Delete the deterministic implication. Supply a quantitative local-time reward estimate for the changed recording times, such as the geometric/Chernoff argument above. State whether the counted quantity is backbone-trace visits, root-inclusive occupation, or vertical excursions. Propagate its constants and exponent through Case 2, the exit estimate, and Lemma 4.1.
2. **Line 72, small-`t` cutoff.** The integer cutoff requires a forced positive counted occupation. Prove this for the precise DNNS definition. If only vertical excursions count, it is false; for the needed exit estimate use its deterministic minimum-time cutoff instead, with a correspondingly small positive stretched-exponential exponent.
3. **Lines 61–69 and 226–246, DNNS scope and rates.** Make the critical inputs auditable: provide the exact original hypotheses and parameter restrictions, the quantitative environment statements being extracted, and proofs of every changed statement. Distinguish verbatim original results from repaired consequences. The blanket assertion that only (4.120) uses `gamma>1/3` requires source verification; it is not established by the supplied text.
4. **Lines 87–90, midpoint hitting versus exit.** Use a strictly smaller closed interval than the midpoint distance; account for time ratios above one by a trivial bound. The result and exponents are unchanged.
5. **Line 176, cutoff choices.** Use an admissible sufficiently small hierarchy of cutoff exponents, or verify that the displayed explicit values satisfy all original restrictions. Merely permitting arbitrarily small parameters does not license every value below one.
6. **Lines 128–132 and 142, lower inputs.** Retain the finite upper time range for the killed diagonal bound and the order `d,c_l,c_u,b`. Supply or precisely reference the uniform hitting and volume statements on the enlarged start window. The volume estimate has the elementary Bernstein proof given above; no extra logarithm is needed.
7. **Abstract line 33 and strategy line 53, annealed “small-time” bound.** Specify that the scale-uniform constant is for one block `J_ell`. The full small-time sum is bounded by `C log N` after spatial averaging. This distinction prevents a materially misleading account of where the logarithm enters.

Task: “You are refereeing a mathematical paper that has been posted.” — 12 November 2026, 19:14 Asia/Tbilisi (first recorded task time).
