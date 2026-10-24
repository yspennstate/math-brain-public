Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# P0471 admission-side mathematics — critical transform obstruction and a sharp Tauberian closure gate

Date: 2026-09-19 UTC  
Worker: `R7-05 Sharp Inequality Research`  
Native ID: `6aabe805f32881919992996e1c5cfad6`  
Own root: `research7_2026-09-17/R7-05/`  
Candidate: `P0471` — mean number of sites deep in an extremal DGFF cluster  
Disposition in this run: **HARD / NOT ADMITTED**  
Methods: **B2 / B18 / B24**

## 1. Exact source target and notation

The current single-page version of Marek Biskup's PIMS-CRM lecture notes, *Extrema of the two-dimensional Discrete Gaussian Free Field*, states on p. 222:

> Conjecture 16.6. For `f_h` as above, `lim_{h->infinity} exp(-alpha h) E_nu(f_h)` exists in `(0,infinity)`.

Here `nu` is the extremal cluster law and

`f_h(phi) = sum_{z in Z^2} 1_[0,h](phi_z)`.

There is a source-version numbering shift: the older double-page PDF calls the same displayed assertion Conjecture 16.5 and the following near-extremal profile statement Conjecture 16.6. The mathematical target is the displayed limit (equation (16.8)), not the bare conjecture number.

Set

`F(h) := E_nu[f_h]`,

and

`q(h) := exp(-alpha h) F(h)`.

Then P0471 is exactly the assertion that

`q(h) -> c` for some `c in (0,infinity)`.

Because `f_h` is increasing in `h`, `F` is nonnegative and nondecreasing. The existing campaign attempt observed that, for `beta>alpha`, Tonelli gives the critical cluster transform

`G(beta) := sum_z E_nu[ exp(-beta phi_z) ] = beta integral_0^infinity exp(-beta h) F(h) dh`.

Equivalently, with `s=beta-alpha>0`,

`G(alpha+s) = (alpha+s) integral_0^infinity exp(-s h) q(h) dh`.

The source conjecture would imply `(beta-alpha)G(beta) -> alpha c`. The point of this note is to identify exactly how much stronger information is needed for the converse.

## 2. B2 — a stronger obstruction: even the full singular principal part of the transform is blind to persistent oscillation

The archived attempt already contained an increasing oscillatory model showing that the leading Laplace pole alone does not force `q(h)` to converge. One can sharpen this materially: the *entire singular principal part* at `beta=alpha` can agree with the convergent model while the normalized profile still oscillates forever.

Fix

`0 < epsilon < alpha/sqrt(alpha^2+1)`

and define

`F_epsilon(h) := exp(alpha h) (1 + epsilon sin h)`.

Then

`F_epsilon'(h)
 = exp(alpha h) [ alpha + epsilon(alpha sin h + cos h) ]`.

Since

`min_h [alpha sin h + cos h] = -sqrt(alpha^2+1)`,

the stated bound on `epsilon` gives `F_epsilon'(h)>0` for all `h>=0`. Thus this is not an obstruction created by violating the only elementary shape information available for the true cumulative count: `F_epsilon` is strictly increasing and positive.

Its normalized profile is

`q_epsilon(h)=1+epsilon sin h`,

which has no limit. Yet its transform is exactly

`G_epsilon(alpha+s)
 = (alpha+s) integral_0^infinity exp(-s h)(1+epsilon sin h) dh`

`= (alpha+s) [ 1/s + epsilon/(1+s^2) ]`.

Hence

`G_epsilon(alpha+s)
 = alpha/s + 1 + epsilon(alpha+s)/(1+s^2)`.

The last term is analytic at `s=0`. Consequently every `epsilon` in the admissible interval has the same complete negative-power singular part at the critical point as `epsilon=0`:

`Sing_{s=0} G_epsilon(alpha+s) = alpha/s`.

### Consequence

Any proposed proof of P0471 that uses only the meromorphic principal part, the pole order, the pole residue, or any finite collection of negative-power singular coefficients of `G(beta)` at `beta=alpha` is insufficient. The missing information has to be genuinely local-in-depth rather than merely critical-transform singularity data.

This is stronger than the previous observation `(beta-alpha)G(beta)->alpha c` alone is not Tauberian enough.

## 3. B18 — exact translation to critical truncated cluster mass

Define the expected critical truncated cluster mass

`S(H) := E_nu[ sum_z exp(-alpha phi_z) 1_{0 <= phi_z <= H} ]`.

Writing the counting measure of cluster depths as `d f_h` and using Tonelli/Stieltjes integration,

`S(H) = integral_[0,H] exp(-alpha x) dF(x)`.

Integration by parts gives the exact identity

`S(H)
 = exp(-alpha H)F(H) - F(0) + alpha integral_0^H exp(-alpha h)F(h) dh`.

In terms of `q`,

`boxed{ S(H) = q(H) - F(0) + alpha integral_0^H q(h) dh. }`

This puts the source conjecture into the language of critical mass. If

`q(H) -> c in (0,infinity)`,

then immediately

`boxed{ S(H)/H -> alpha c. }`

Thus P0471 implies an exact linear-growth law for the expected critical truncated mass.

But the converse is false without extra regularity. For the monotone oscillatory model above, `F_epsilon(0)=1` and

`S_epsilon(H)
 = q_epsilon(H)-1 + alpha integral_0^H q_epsilon(h) dh`

`= epsilon sin H + alpha H + alpha epsilon(1-cos H)`.

Therefore

`S_epsilon(H)/H -> alpha`

although `q_epsilon(H)=1+epsilon sin H` has no limit.

### Consequence

Even a theorem proving the exact first-order linear asymptotic of expected critical truncated cluster mass would not, by itself, settle P0471. One still needs a Tauberian regularity input that prevents order-one oscillation of `q` across large depth scales.

## 4. B24 — a sufficient Tauberian closure criterion isolating the missing regularity

The obstruction above suggests looking for the weakest source-plausible regularity statement that would turn a critical-mass asymptotic into the desired pointwise cluster asymptotic.

### Proposition (relative terminal-window Tauberian criterion)

Let `alpha>0`. Let `F:[0,infinity)->[0,infinity)` be nondecreasing and define

`q(H)=exp(-alpha H)F(H)`

and

`S(H)=q(H)-F(0)+alpha integral_0^H q(h) dh`.

Assume:

1. `S(H)/H -> L` for some `L in (0,infinity)`;
2. for some fixed `delta in (0,1)`,

   `omega_delta(H) := sup_{u in [(1-delta)H,H]} |q(u)-q(H)| -> 0`.

Then

`boxed{ q(H) -> L/alpha. }`

In particular, if these two conditions can be proved for the DGFF cluster law, then P0471 follows with `c=L/alpha`.

### Proof

Because `q>=0`, the exact identity gives

`alpha integral_0^H q(h) dh
 = S(H)-q(H)+F(0)
 <= S(H)+F(0)`.

The first assumption therefore implies

`(1/H) integral_0^H q(h) dh = O(1)`.

Let

`M_delta(H) := (1/(delta H)) integral_{(1-delta)H}^H q(u) du`.

Then `M_delta(H)=O(1)`. By the terminal-window oscillation assumption,

`|M_delta(H)-q(H)| <= omega_delta(H)`,

so `q(H)=O(1)`. In particular `q(H)/H -> 0`. Dividing the exact identity by `H` now yields

`alpha A(H) -> L`,

where

`A(H):=(1/H) integral_0^H q(h) dh`.

Hence `A(H)->L/alpha`. The terminal-window average can be expressed exactly as

`M_delta(H)
 = [ A(H) - (1-delta) A((1-delta)H) ]/delta`.

Both Cesaro means tend to `L/alpha`, so

`M_delta(H) -> L/alpha`.

Finally

`|q(H)-L/alpha|
 <= |q(H)-M_delta(H)| + |M_delta(H)-L/alpha|
 <= omega_delta(H) + o(1) -> 0`.

This proves the proposition.

## 5. What this changes about the mathematical bottleneck

The source-level problem can now be separated into two conceptually different obligations:

1. **averaged critical growth:** establish `S(H)/H -> L in (0,infinity)`;
2. **relative-scale rigidity:** show that the normalized cumulative cluster profile cannot undergo persistent order-one oscillations on a fixed relative terminal window, for example

   `sup_{u in [(1-delta)H,H]} | exp(-alpha u)E_nu f_u - exp(-alpha H)E_nu f_H | -> 0`.

The first is an Abelian/critical-mass statement. The second is the genuinely Tauberian, local-in-depth ingredient. A critical Laplace pole, even with its entire principal part known, does not supply (2).

This gives a concrete test for future DGFF input: ballot estimates, pinned-field growth theorems, or renewal/random-walk representations are useful for P0471 only if they can furnish a ratio/Harnack/oscillation estimate strong enough to imply (2), or an alternative Tauberian condition of comparable force.

## 6. Current-source/literature boundary relevant to admission

The original source statement remains the displayed p.222 limit above. The published Biskup-Louidor extremal-process paper identifies the cluster law and gives the pinned-field/random-walk construction underlying `nu`. The Biskup-Gufler-Louidor near-maxima work proves the adjacent near-extremal profile theorem, but that is not the same as the cluster-mean limit (16.8).

A dated author-history check also found Oren Louidor's 16 April 2023 CV listing, under **Papers in Preparation**, Stephan Gufler, Oren Louidor and Dominic Yeo, *On the growth of the pinned discrete Gaussian free field*. A bounded 2026-09-19 search did not surface a published/arXiv version under that exact title. This is not proof that the source conjecture has been solved, but it is directly source-adjacent author work and raises the prior-art/admission risk.

Accordingly P0471 remains an honest **HARD / NOT ADMITTED** candidate for this CLOSABLE worker. No canonical claim is created and no source research stagnation count starts.

## 7. Durable conclusion for R7-05

- Candidate screened: `P0471`.
- New mathematics: stronger transform obstruction; exact critical-mass identity; proved sufficient relative-window Tauberian criterion.
- Mathematical status of P0471: **OPEN-LOOKING / PARTIAL ANALYSIS ONLY**; no source-level proof or refutation.
- Admission status: **HARD / NOT ADMITTED**.
- R7-05 state after this artifact: **PENDING_ADMISSION**.
- Successor metric: **UNKNOWN/UNMEASURED -> UNKNOWN/UNMEASURED**.
- Target unchanged/stagnation count: **not started; no admitted successor**.
- No `operations/claims/P0471.md` is created.
- No shared `RESULTS.md`, `QUEUE.md`, or `POSTED.md` edit is authorized or performed by this worker.
