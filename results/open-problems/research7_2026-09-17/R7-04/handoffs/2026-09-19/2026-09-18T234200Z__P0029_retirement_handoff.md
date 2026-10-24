Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime model/effort telemetry or binding selector is exposed.

# R7-04 immutable handoff — P0029

Worker: `R7-04`  
Native ID: `6aabe7ea6e1881919a65503f8445a813`  
Canonical target: `P0029`  
Outside source: Krzysztof Burdzy, *My favorite open problems*, Problem 9, https://sites.math.washington.edu/~burdzy/open_mathjax.php  
Source status at handoff: **OPEN / PARTIAL**  
R7-04 operational status after this file: **RESEARCH RETIRED BY SIX-UNCHANGED CLOSABLE RULE**  
Frozen metric: `D_* := limsup_n E[rho_n/n | exactly two peaks]`  
Metric at handoff: `UNKNOWN/UNMEASURED`  
This retirement is worker-local protocol state. It does not assert that the problem is solved, known, globally retired, or available for reassignment without a fresh ownership decision.

## Why the handoff is mandatory

P0029 accumulated six ordinary research runs without movement of the frozen source metric. The mandatory thinking-only STUCK1 diagnosis occurred after ordinary run 3, and its chosen recovery action produced the positive first-merge representation. Ordinary runs then continued through counts 4, 5, and 6. Section I of `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md` requires a CLOSABLE target to retire after six unchanged ordinary runs.

No future R7-04 iteration should continue P0029 unless the owner explicitly changes that protocol. The slot remains enabled and must rotate only through a fresh shard-3 admission.

## Exact source closure criterion

The source conditions a uniformly random labeling of the `n x n` nearest-neighbor square on exactly two peaks and asks whether the graph distance `rho_n` obeys

`rho_n/n -> 0` in distribution.

Because `0 <= rho_n/n <= 2`, this is equivalent to

`E[rho_n/n | exactly two peaks] -> 0`,

hence to `D_*=0`. A rigorous positive subsequential lower bound gives a source-valid NO.

Finite-grid data, path/ladder results, restricted graph classes, or a proof for a surrogate rank-2 pair law do not close the source.

## Cumulative valid mathematics to preserve

### A. Descending-reveal birth formulation

Reveal vertices in decreasing label order. A revealed vertex is a peak exactly when it has no neighbor in the previously revealed set. Thus peaks are births/restarts of the reveal process. This turns the exactly-two-peak event into a two-birth growth problem.

### B. Exact pair counting and finite certificates

The early subset prefix/completion DP gave exact counts through `4 x 4`. A later independent-set inclusion–exclusion formulation reproduced those pair weights and extended the exact law to `5 x 5`.

Recorded normalized means:

- `n=2`: `1`;
- `n=3`: `666/749 ~= 0.88919`;
- `n=4`: `377754599/463868556 ~= 0.814357`;
- `n=5`: `5689414559220285956/7357564043086414875 ~= 0.773274214930740`.

These values are evidence only and must not be extrapolated as a proof.

### C. Promotion theorem

For any finite connected graph, if `F({r,v})` is the rank-2 birth-free completion count and `W(r,v)` is the actual exactly-two-peak ordered pair count,

`F({r,v}) <= W(r,v) <= (N-1)F({r,v})`.

This removes arbitrary second-birth rank at polynomial cost but is too weak by itself for the square asymptotic.

### D. Solved path model

For the path `P_N`, if the two seeds have left length `L`, gap `g`, and right length `R`,

`F_{P_N}({i,j}) = (N-2)! 2^{g-1}/(L! g! R!)`.

Under the rank-2 pair law the gap is a binomial variable conditioned positive, and the actual exactly-two-peak path satisfies `rho_N/N -> 1/2` in probability. This is a solved analogue, not the square result.

### E. Exact actual-pair inclusion–exclusion kernel

For highest peak `r`, with `U_r=V\N[r]`, define recursively for independent sets

`b(empty)=1`,

`b(I)=|N[I]|^{-1} sum_{x in I} b(I\{x})`.

Then

`C(r,v)=sum_{I subset U_r, I independent, v in I} (-1)^{|I|-1} b(I)`

satisfies

`W(r,v)=(N-1)! C(r,v)`.

This representation is exact but heavily cancellation-prone.

### F. Exact positive first-merge representation

This was the successful STUCK1 recovery. If `S=A sqcup B` is the unique two-component state immediately before the first merge, then

`W_G(r,v)=sum_S binom(|S|-1,|A|-1) h_A(r) h_B(v) g_G(S)`.

For the unordered peak pair,

`U_G({r,v})=sum_S binom(|S|,|A|) h_A(r) h_B(v) g_G(S)`.

Let

`R(C)=sum_u h_C(u)`, `mu_C(u)=h_C(u)/R(C)`,

and

`Omega_G(S)=binom(|S|,|A|) R(A)R(B)g_G(S)`.

Conditional on `S`, the two roots are independent with laws `mu_A` and `mu_B`. The actual conditioned pair law is therefore a positive mixture.

### G. Reversible component-root conductances

For each connected component `C`,

`h_C(r)=sum_{y~r} F_C({r,y})`.

Hence `mu_C` is the stationary law of the reversible nearest-neighbor walk with conductances

`c_C({x,y})=F_C({x,y})`.

This implies, among other things, `max_r mu_C(r) <= 1/2` for nontrivial `C`.

### H. First-merge flux and geometry

For state `S=A sqcup B`,

`P(S)=binom(|S|,|A|)R(A)R(B)` is the two-birth prefix count,

`Q(S)=P(S)F(S)` is active full-order mass,

`Omega(S)=P(S)g(S)` is exact absorption flux,

and `lambda(S)=g(S)/F(S)` is the merge hazard.

After the second birth, inter-component distance never increases and drops by at most one at each reveal. If the first-merge prestate has `s` vertices and the roots are distance `d`, the promoted two-front trajectory has exactly `d-2` distance-decreasing additions and `s-d` neutral additions. In particular `d<=s`.

### I. Barycenter/dispersion reduction

For root law `mu_C`, define barycenter `b(C)` and variance

`V(C)=E_{mu_C} ||R_C-b(C)||_2^2`.

For `S=A sqcup B`, conditional independence gives

`q_n(S)=||b(A)-b(B)||_2^2+V(A)+V(B)=E[||R_A-R_B||_2^2 | S]`.

The absorption-weighted average of `q_n(S)/n^2` is a positive geometric-energy quantity. A positive fixed fraction of `Omega_n`-mass with `q_n(S)>=c n^2` would already refute the source.

Barycenter separation alone is insufficient: symmetric nested components can share a barycenter while one has variance `Theta(n^2)`.

### J. Final run: scaled positive field is source-equivalent

For component `C`, define

`Z_C(theta)=sum_{r in C} h_C(r) exp(theta dot r)`.

For an unordered first-merge state `{A,B}`, symmetrize the two orientations and define the global positive absorption partition `mathcal Z_n(theta)` exactly as in

`research7_2026-09-17/R7-04/artifacts/2026-09-19/2026-09-18T233800Z__P0029_scaled_tilt_equivalence.md` @ `59da568f7431170cfac9b243a419f143eeae5482`.

If the actual peak pair is given an independent fair orientation, `D_n=R_1-R_2`, and

`Y_n=(D_n)_1/n`,

then

`mathcal Z_n((s/n)e_1)/mathcal Z_n(0)=E exp(sY_n)`.

Let

`psi_n(s)=log mathcal Z_n((s/n)e_1)-log mathcal Z_n(0)`,

`V_n=E Y_n^2`.

D4 symmetry gives

`m_n:=E[rho_n/n]=2E|Y_n|`,

so

`2V_n <= m_n <= 2 sqrt(V_n)`.

Therefore the source YES statement is equivalent to `V_n->0`.

For every fixed `s>0`, exponential tilting of the bounded variable `Y_n in [-1,1]` gives

`a_-(s)V_n <= psi_n(s) <= a_+(s)V_n`,

where

`a_-(s)=(2s-1+e^{-2s})/4`,

`a_+(s)=(e^{2s}-1-2s)/4`.

Hence, for **any one fixed `s>0`**,

`rho_n/n -> 0` in distribution

iff

`psi_n(s)->0`

iff

`mathcal Z_n((s/n)e_1)/mathcal Z_n(0)->1`.

This is the sharpest cumulative reduction. A successor can refute the source by proving a positive limsup of the scaled free-energy gain for one fixed field.

## Exact blocker at retirement

The unresolved formula is now positive and source-equivalent:

`limsup_n [ log mathcal Z_n((s/n)e_1)-log mathcal Z_n(0) ] ?`  for fixed `s>0`.

No argument currently proves it positive or zero.

The missing ingredient is an asymptotic comparison/coarse-graining principle for the **absorption-weighted two-root partition**. Pointwise root-pair bounds are unnecessary, but the existing positive mixture still involves global component shapes and the birth-free suffix count `g_n(S)`.

## Routes tried and why they stopped

1. Direct finite-grid enumeration: exact through `5 x 5`, no asymptotic control.
2. Rank-2 pair law plus promotion: polynomial `n^2` distortion is too large without exponential separation estimates.
3. Local seed-shift ratios: moving a seed can alter the full suffix history, so no uniform local distortion bound emerged.
4. Signed independent-set kernel: exact, but absolute values destroy the cancellation that produces the positive pair law.
5. Pointwise spatial control: stronger than needed and unsupported.
6. First-merge geometry alone: `d<=|S|` does not say the absorption measure gives enough weight to large root distance.
7. Barycenter alone: symmetric nested components can have zero barycenter separation and macroscopic dispersion.
8. Zero-field dispersion directly: reduced to a positive quantity but no lower bound.
9. Unscaled exponential field: can be dominated by exponentially rare `O(n)` displacements and is not source-equivalent.
10. Scaled field: exact and source-equivalent, but the required positive asymptotic free-energy gain remains unproved.

## Best successor attack

Do **not** spend the first successor run extending the exact checker to `6 x 6`. Instead preserve the `1/n` field and attack the positive ratio directly. The most promising concrete target is:

> Find a family `F_n` of first-merge states carrying a fixed positive fraction of the zero-field absorption mass, and show that on `F_n` the symmetrized component-root partition gains a fixed factor `>1` at field `(s/n)e_1` for some fixed `s>0`.

That would immediately yield `limsup psi_n(s)>0`, hence `D_*>0`.

A weaker sufficient variant is to show a positive absorption-weighted mass of states on which either component-root law has coordinate variance `Omega(n^2)` or the two component barycenters are separated by `Omega(n)`.

## Prior reports and key commits

- admission/claim: `research7_2026-09-17/R7-04/admissions/2026-09-18T174300Z__P0029_admission.md` @ `b9c3499c0283b8f7715239a98222621e32302139`;
- ordinary run 1 report: `.../2026-09-18T174556Z__report.md` @ `470216c37630828040ac70cdf553aed3d2a3eb55`;
- ordinary run 2 report: `.../2026-09-18T184200Z__report.md` @ `72bb76694b0d9754495c71218ba670634d19dd56`;
- ordinary run 3 report: `.../2026-09-18T200800Z__report.md` @ `5054d0923d7d622bdee71efbe59da7961774cd62`;
- mandatory STUCK1 report: `.../2026-09-18T203112Z__report.md` @ `480205a43c1fe6f0233044a49058f965e32286f9`;
- ordinary run 4 report: `.../2026-09-18T214800Z__report.md` @ `e06a415500361add082c0d803e0dbe951723bad3`;
- ordinary run 5 report: `.../2026-09-18T223800Z__report.md` @ `977ead471881528673145d42bae8c23630ad53a3`;
- ordinary run 6 mathematical artifact: `research7_2026-09-17/R7-04/artifacts/2026-09-19/2026-09-18T233800Z__P0029_scaled_tilt_equivalence.md` @ `59da568f7431170cfac9b243a419f143eeae5482`.

The exact finite checkers and earlier artifacts are discoverable through the path-scoped R7-04 history and should be read before any future computational extension.

## Handoff verdict

Mathematical verdict: **OPEN / PARTIAL**.  
Frozen metric: **UNKNOWN/UNMEASURED -> UNKNOWN/UNMEASURED**.  
R7-04 ordinary unchanged count: **6**.  
R7-04 stuck recoveries used: **1**.  
R7-04 action: **HANDOFF / RESEARCH RETIRED from this worker**.  
Global source resolution: **none claimed**.
