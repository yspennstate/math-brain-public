# R17 PROB10-02 idea before code — symmetric single-debt peeking

Model request: GPT-6 maximum reasoning. Applied model/effort telemetry is not authenticated here, so actual reasoning metadata remains UNVERIFIED.

Target remains the true iid-binary Chvatal–Sankoff constant. All proposed transitions below expose actual future source bits and retain any exposed-but-unconsumed bit in state; no independent Bernoulli match field is introduced.

## Continuity

The immediately preceding R17 report is `runs/prob10_2026-09-20/PROB10-02/20260920T1200Z_r17_snell_elimination_variational_c8d4.md`. It proved exact one-sided debt Snell elimination and the source transfer `gamma_2 >= 2 rho/(1+rho)`, with best displayed mechanism certificate `rho=6293309/10000000`, still below the source-improvement threshold `99083249/150916751`. The H0021 handoff and all earlier R17 failure counters remain untouched.

## Attack A — symmetric single-debt process

The one-sided process has states `N,A_0,A_1`: it can exploit a peek on the X side but not make the same adaptive choice on the Y side. Enlarge the information state minimally to

`N, A_0,A_1, B_0,B_1`,

where `A_u` means the next X refill bit has already been exposed as `u` and remains unconsumed, while `B_v` is the Y analogue. Never expose a second bit on a side that already carries debt.

At a mismatch in state `N`, retain ordinary skips and one-sided peeks in either orientation. In addition, try a **paired peek**: reveal the next refill bits `(u,v)` from both genuine source tails and then choose which head to skip. If X advances, `u` enters the visible X window while `v` remains as state `B_v`; if Y advances, `v` enters the visible Y window while `u` remains as state `A_u`. Thus the unconsumed exposure is not forgotten.

At a mismatch in `A_u`, one may either use the ordinary actions (advance X and clear debt; or advance Y and retain `A_u`) or expose only the fresh Y refill `v` and choose after seeing it. Advancing X converts the outstanding information from `A_u` to `B_v`; advancing Y keeps `A_u`. The `B_v` rule is symmetric. A match consumes both heads and clears debt after the known refill on the indebted side and a fresh refill on the other.

Critical claims to prove before treating any computation as source-valid:

1. deferred decisions realize every transition on two genuine iid binary strings;
2. after every decision there is at most one exposed-but-unconsumed refill bit, so a block end can be freshened by discarding only `ell+1` symbols beyond each consumed index;
3. every Bellman subsolution with mean reward increment `rho` therefore transfers by the same paired-block argument to `gamma_2 >= 2 rho/(1+rho)`;
4. the new operator pointwise dominates the one-sided operator after the natural embedding, so it cannot worsen the mechanism bound.

The numerical question is whether exact small-width Bellman iteration raises `rho` enough to approach or cross `99083249/150916751 ≈ 0.6565424205`. Any displayed finite value counts only after the transfer proof and a global exact residual scan.

## Attack B — debt-orientation switching as a coupled Snell problem

If Attack A improves but does not cross the source threshold, derive a two-orientation optimal-stopping system for the debt values. Unlike the preceding scalar Snell envelope, the continuation branch can switch from `A_u` to `B_v`. Look for a block contraction after `O(ell)` steps by the first forced head match on either orientation. The goal is a finite truncation theorem for the coupled debt envelope, permitting larger `ell` without optimizing `4*4^ell` debt coordinates independently.

A key falsification test: determine whether a uniform geometric contraction exists for the coupled envelope. Orientation switching may avoid the head value that would have killed the old one-sided perturbation, so the old `2^{-r}` proof cannot simply be copied.

## Attack C — exact symmetry/low-order potential route, not another behavioral quotient

If the raw `5*4^ell` process still scales poorly, do not repeat the exhausted exact-bisimulation route. Instead test an inequality-only potential class invariant under simultaneous bit complement and string swap, initially local in head/run/tail features. The separation oracle must scan all formal states exactly. A low-order ansatz is useful only if its globally checked residual exceeds the inherited threshold; sampled or simulated improvements do not count.

A likely obstruction to test explicitly is whether any head-only or leading-run-only potential can distinguish states already separated by the preserved length-six counterexample `A=010011,B=110100`. If not, record the exact counterexample and move to a richer local interaction rather than silently enlarging a false quotient.

No source endpoint is claimed moved in this idea note.