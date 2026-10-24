# FOREST / account02 B01 — source-safe 2-cut straddling budget and exact theta-grid compression

**Run:** `B01-20260922T055947Z-forest-r16`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`  
**Parent target:** OPEN; no full-proof claim.

## 1. Fresh controls and exact source scope

Fresh owner controls were resolved from `yspennstate/math-research-brain` main and reread before this report at commit `ebb0abd3bed054a5000f49a0d532a5f779b0d82c`. Owner control revision is `2026-09-22.2`, directive `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. The later collective order supersedes the stale installation language retained in historical `AGENTS.md`: account02/B01 remains FOREST research, and new installation/benchmark work is stopped. No account02/B01 pause or stop was present.

The target remains the exact unit law on **all** unrooted acyclic edge subsets of every finite simple graph, including disconnected forests and all sizes. For distinct edges `e,f`, prove `Z_e Z_f-Z Z_ef >= 0`. No rooted, fixed-size, spanning-tree or arbitrary-weight law is substituted.

The same-hour create-only canonical login already existed and was preserved rather than overwritten, as PROTOCOL requires. This invocation has its own immutable start and finish records.

## 2. Exact peer state consumed, including the latest correction

Latest complete lead version consumed: account01/B01 `20260922T050946Z-b01-forest-auto11`, shared handoff blob `4cee205cb7d254caf785692838111988a0b8a155`. Its source-safe survivor is the triangle-free deletion/contraction Simpson identity; its proposed rank-degree complete-log-concavity strengthening is **not** used below.

Latest decisive correction consumed: account01/B02 `20260922T054825Z-b02-forest-auto11`, shared handoff blob `fb4265dc413059fc93e8dada0ef0ba90a008d947`. It exhibits a `K_3` Hessian counterexample to the claimed rank-degree homogenization and correctly notes that the ALOV independent-set homogenization uses ground-set degree, not matroid rank. Therefore the rank-CLC justification in my immediately preceding run is retracted fail-closed.

Named OTHER-account result consumed and directly applied: partner account03/B02 handoff `20260922T051758Z`, blob `c165e7c6b6ca991a97c5ed3d646611f91cf96adc`. I use its exact two-terminal path-bundle transfer: `Q(k,a)`, the union of `k` internally disjoint length-`a` unit paths between two terminals, has disconnected/connected lift counts

`D_Q=(2^a-1)^k`, `C_Q=k(2^a-1)^(k-1)`,

hence exact boundary activity `C_Q/D_Q=k/(2^a-1)`. I do **not** import the partner's Cocks-dependent weighted closure.

Own predecessor: account02/B01 r15 report blob `f7100e76da7d479c61557d1d28c953ce2c9cbc1b`. Its exact 2-cut factorization and edgewise straddling lemma survive. Its rank-width inequality happened to have a valid conclusion, but its stated proof through rank-degree CLC was invalid. Section 5 below gives a new source-safe proof using only minimality, pairwise covariance signs, Cauchy--Schwarz, and elementary matroid extension counting.

## 3. Conditional end-to-end separator route

Assume the simple source conjecture fails. Since a simple graph is a loopless multigraph, choose an edge-minimal **loopless-multigraph** counterexample `G` and a violating pair `e,f`. Minimality then pays every strictly smaller loopless unit instance. Parallel marked edges themselves cannot violate, because they cannot occur together in a forest.

Consider a proper 2-separation with terminals `u,v`, with both marks in one side `B` and a non-singleton outside side `O`. Put

- `D` = number of forests of `O` in which `u,v` are disconnected,
- `C` = number in which `u,v` are connected,
- `lambda=C/D`, `q=C/(C+D)=lambda/(1+lambda)`.

If `R(s)` denotes the marked Rayleigh gap in `B` after adding a virtual `uv` edge of activity `s`, exact two-terminal gluing gives

`Delta_G(e,f)=D^2 R(lambda)`, with `R(s)=d0+b s+d1 s^2`.

Because `O` is non-singleton, the unit augmented marked side and the deletion/contraction endpoint graphs are strictly smaller loopless unit graphs, so minimality gives

`R(0)>=0`, `R(1)>=0`, and the leading coefficient `d1>=0`.

Thus, if the parent violates, the negative set of `R` on the projective half-line is one open interval `J=(alpha,beta)` containing `lambda` and not containing `1`. Write its probability-coordinate endpoints

`ell=alpha/(1+alpha)`, `u=beta/(1+beta)`,

with `beta=infinity` mapped to `u=1`, and put `delta=u-ell>0`.

Cross-side marked pairs remain governed by the exact proper-2-sum factorization already derived by the partner; this run attacks the unresolved same-side case without a weighted-Cocks step.

## 4. Surviving straddling lemma, sharpened pointwise

Let `h` be any physical edge of `O`, `X_h` its indicator under the unit uniform-forest law of `O`, and `Y=1[u connected to v]`. Write

`p_h=P(X_h=1)`, `q_i=P(Y=1 | X_h=i)` for `i=0,1`.

The r15 argument is source-safe and survives the CLC correction. Adding a unit virtual `uv` edge to `O` gives a strictly smaller loopless unit graph; minimality applied to `(h,uv)` yields `q_0<=q_1`. Deleting or contracting `h` in the whole counterexample gives smaller loopless unit children, so their boundary odds cannot lie in the open negative interval. Since the parent probability `q` is the mixture of `q_0,q_1`, every outside edge satisfies

`q_0 <= ell < q < u <= q_1`.                                      (4.1)

This gives more than the previous width lower bound. Put

`x=q-q_0`, `y=q_1-q`.

The mixture identity gives `p_h=x/(x+y)`, while binary covariance gives

`Cov(X_h,Y)=p_h(1-p_h)(q_1-q_0)=xy/(x+y)`.

Since `x>=q-ell`, `y>=u-q`, and `xy/(x+y)` is increasing in both positive arguments,

`Cov(X_h,Y) >= kappa := ((q-ell)(u-q))/(u-ell)`.                 (4.2)

The same mixture inequalities also force the **individual inclusion interval**

`(q-ell)/(1-ell) <= p_h <= q/u`,                                (4.3)

and ordinary forest deletion injectivity gives `p_h<=1/2`. Therefore a same-side violation necessarily has

`(q-ell)/(1-ell) <= 1/2`.                                       (4.4)

All of (4.1)--(4.4) retain the actual boundary-connectivity distribution of `O`; no external field has been introduced.

## 5. Repair of the prior rank-width bound without complete log concavity

Let `m=|E(O)|`, let `K=sum_h X_h`, let `mu=E K`, and let `r` be the graphic-matroid rank of `O`. Define

`S=sum_h p_h(1-p_h)`.

Because `O` is a strictly smaller loopless unit graph, minimality gives pairwise negative correlation for every distinct pair of its physical edges. Hence

`Var(K) = S + 2 sum_{h<j} Cov(X_h,X_j) <= S`.                   (5.1)

From (4.1), each edge has influence at least `delta`, so

`Cov(K,Y)=sum_h Cov(X_h,Y) >= delta S`.                          (5.2)

Cauchy--Schwarz, (5.1), and `Var(Y)=q(1-q)` therefore give

`delta^2 S <= q(1-q)`.                                          (5.3)

No log-concavity is used.

Next, `p_h<=1/2` implies `p_h(1-p_h)>=p_h/2`, so `S>=mu/2`. The elementary matroid extension inequality

`(k+1)i_{k+1} >= (r-k)i_k`

holds because every independent `k`-set extends to a basis and therefore has at least `r-k` addable elements, while every independent `(k+1)`-set has exactly `k+1` predecessors. Thus `i_k/binom(r,k)` is nondecreasing, so the independent-set size law is an increasing tilt of `Bin(r,1/2)` and

`mu>=r/2`.

Consequently `S>=r/4`, and (5.3) yields the repaired source-safe rank-width obstruction

`boxed: r delta^2 <= 4 q(1-q).`                                 (5.4)

This recovers the useful numeric conclusion of r15 while **discarding** its invalid rank-CLC proof.

The pointwise floor (4.2) also gives a new edge-count obstruction. Since `Cov(K,Y)>=m kappa`, while `Var(K)<=S<=m/4`, Cauchy--Schwarz gives

`boxed: 4 m kappa^2 <= q(1-q).`                                (5.5)

Finally, summing the lower and upper inclusion bounds in (4.3), using `mu<=r` and `mu>=r/2`, gives

`boxed: m (q-ell)/(1-ell) <= r`,                               (5.6)

`boxed: r/2 <= m q/u`.                                          (5.7)

These are all necessary conditions for an offending same-side 2-cut and use only the actual outside unit law.

## 6. New exact theorem — cheaper theta gadgets cannot hit the forbidden interval

The named partner's `Q(k,a)` identity becomes a direct separator-compression tool here.

For any integers `a,k>=1`, glue the marked side `B` to the two-terminal unit gadget `Q(k,a)`. Its exact response is

`s_{a,k}=k/(2^a-1)`,

and the resulting marked gap is

`Delta_{B union Q(k,a)}(e,f)=D_Q^2 R(s_{a,k})`.                 (6.1)

If `ak<m`, the replacement graph has strictly fewer edges than `G`. It is a loopless **unit** multigraph (for `a=1`, parallel terminal edges are allowed in the minimality class), so edge-minimality applies directly. Therefore

`boxed: R(k/(2^a-1)) >= 0 whenever ak<m.`                       (6.2)

Equivalently, if `Theta_{<m}={k/(2^a-1): a,k>=1, ak<m}`, then

`boxed: J intersect Theta_{<m} = emptyset.`                     (6.3)

This is an exact, source-native prohibition. It is stronger than testing only `R(0),R(1)` and does not ask for arbitrary positive weights. Examples forced outside `J` include every integer `1,...,m-1`, every `k/3` with `2k<m`, every `k/7` with `3k<m`, and so on.

There is also a sharp response-size bound for an arbitrary `m`-edge outside. Map each connected forest to a disconnected forest plus one distinguished edge obtained by deleting an edge of its unique `u-v` path. This injection gives

`C <= m D`, hence `0<=lambda<=m`.                               (6.4)

The strict cost condition in (6.2) cannot be weakened on minimality alone: `Q(k,a)` itself has `m=ak` and exact response `k/(2^a-1)`. In particular, `m` parallel terminal edges have response `m`. This boundary example is preserved as a guard against falsely claiming a cheaper exact compression always exists.

## 7. First essential missing implication

The same-side 2-cut is now reduced to a concrete source-valid incompatibility problem rather than arbitrary weighted closure.

A violation would require a genuine `m`-edge outside response `lambda` and a marked-side integer-count quadratic `R` such that simultaneously:

1. `R(lambda)<0`, while `R(0),R(1)` and the leading coefficient are nonnegative;
2. every outside edge straddles the same probability interval `(ell,u)` as in (4.1);
3. the source-safe budgets (5.4)--(5.7) hold;
4. the entire cheaper theta response grid `Theta_{<m}` avoids the forbidden interval, as in (6.3).

The first unpaid implication is therefore the following **THETA-HIT / source-realizability step**:

> Show that no genuine unit forest two-terminal side `O` occurring in an edge-minimal counterexample can satisfy all four conditions above; equivalently, derive from its straddling data a cheaper theta response inside `J`, or construct an actual graph-side/outside pair showing this mechanism fails.

I do not assume this implication. It is strictly narrower than the discarded fixed-graph weighted-Rayleigh claim: only the finite source-generated grid (6.3) is paid, and the actual outside distribution remains present through (4.1)--(5.7).

If this step is paid, same-side proper 2-cuts are eliminated; cross-side pairs are already controlled by the exact two-side factorization. The surviving lead triangle-free Simpson mechanism can then be combined with the resulting structural reduction. The separate minimality-conditioned triangle-contraction/STAR-2 debt remains open, so even a complete 2-cut elimination would not by itself be a full proof.

## 8. Exact computation used as regression only

`theta_straddling_checker.py` independently enumerates the unit forests of `Q(k,a)` for all tested `1<=a,k<=4` with at most 12 edges and verifies the exact formulas for `D_Q,C_Q`. It checked 15 theta gadgets, including `Q(2,3)` with `(D,C)=(27,27)` and `Q(4,3)` with `(D,C)=(3375,675)`.

The same script performs 7,539 exact-rational mixture checks on denominator-8 and denominator-12 grids for (4.2)--(4.3). All passed; the minimum slack is exactly zero, as expected at boundary-equality configurations. Output terminates `STATUS=PASS`.

This computation is **AUXILIARY_ONLY evidence inside an ESSENTIAL_STEP_APPLIED run**. The proofs of (4.2)--(6.4) are algebraic/counting arguments above; the finite checks are not universal closure or novelty evidence.

## 9. Failure preservation, privacy, and status

Preserved/rejected shortcuts:

- The rank-degree CLC argument from the lead and my r15 is explicitly retracted after account01/B02's `K_3` counterexample. The repaired proof of (5.4) does not use CLC.
- Fixed-graph `unit-good => arbitrary-weight Rayleigh` remains fail-closed.
- Global STAR-2 is not used; the latest peer work identifies it as parent-equivalent. Only minimality-generated unit children and exact source gadgets are used.
- Finite theta/mixture regressions are not promoted to theorem status.
- No rooted/fixed-size/spanning-tree law substitutes for the source law.

Scoped privacy/secret review: this report and its checker/output contain only mathematical derivations, logical account/slot labels, public/source-bound commit/blob identifiers, and permitted control metadata. They contain no credentials, scheduler identifiers, machine paths, benchmark gold, private transcripts, email/Drive material, or unrelated personal data.

Current-account managed inventory was inspected once through the authorized scheduler connection: 20/20 managed tasks were enabled and hourly-valid, with no missing slot observed and no B01 scheduler mutation. Task delivery flags were observed quiet; account-level notification preference remains unverified.

**Status:** `ESSENTIAL_STEP_APPLIED`; parent FOREST remains OPEN.  
**Model self-report:** `GPT-5.6 Sol`.  
**Reasoning effort requested:** `maximum actually supported`.  
**Reasoning effort configured:** `UNKNOWN / not exposed`.  
**Known actual reasoning effort:** `UNKNOWN / not exposed`.  
**Provider reasoning-token usage:** `null / not exposed`.  
**Provider thinking-time usage:** `null / not exposed`.  
**Observed elapsed execution at report snapshot:** `1125.755 seconds` from the first instrumented UTC observation, including tool/network/output overhead and explicitly not pure thinking. The finish record carries the later final observed window.
