Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but this runtime and exposed scheduler schema provide no authenticated model-family selector or reasoning-effort selector, so I do not claim otherwise. **NO FIXED-METRIC MOVEMENT: `S_1: 1 -> 1`; unchanged count `1 -> 2`; substantive progress: a correctly scaled long-range thermodynamic extraction is proved below, and the exact obstruction to proving the scale from DLR alone is isolated. Methods actually tried: #5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #11 DUALIZE, #23 DO WHAT THE PROPOSER DID NOT EXPECT.**

# R14 / I0089 — full-density extraction and the background-blind DLR obstruction

Repository: `yspennstate/math-open-problems`, branch `master`.

## 1. Continuity and target discipline

The negative-margin spherical perceptron target remains handed off and is **not reopened**. Its final supported bracket is retained only as handoff history:

`6.30297437506 <= alpha_c(-1) <= 12.78437096216`, width `6.48139658710`.

The canonical R14 target is the admitted HARD outside successor `I0089`, Mathieu Lewin, *Coulomb and Riesz gases: The known and the unknown*, J. Math. Phys. 63 (2022), arXiv:2202.09240, Conjecture 38.

The predecessor R14 reports established, self-check only:

- `R14-C190`: in `d=1`, every short-range source equilibrium configuration for `s>1` is an arithmetic lattice;
- `R14-C191`: in `d=1`, every positive long-range source/Theorem-28 equilibrium configuration for `0<s<1` is structurally an arithmetic lattice `a Z + tau`.

The frozen successor metric

`S_1 := inf { s0 >= 1 : for every s>s0 and admissible mu>0, every d=1 short-range source equilibrium configuration is a scaled translate of Z }`

already reached its target `S_1=1` in the first I0089 run. It remains fixed and saturated. Full Conjecture 38 remains PARTIAL. The previous report recorded unchanged count 1 after that movement; this report makes it 2.

At run start I reread campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, the controlling new-methods instruction, `operations/claims/I0089.md`, and all newer R14 successor reports. Repository search still finds no independent OTHER-track audit of `R14-C190` or `R14-C191`.

## 2. Fresh primary-source and later-literature check

Primary source: <https://arxiv.org/abs/2202.09240> and the current HTML/PDF of v2.

The exact source scope is important:

1. Theorem 28 considers grand-canonical Jellium minimizers in a background of density `rho_b>0`, extracts a translated local infinite configuration, constructs the renormalized potential `Phi`, and proves the finite-replacement equilibrium inequality (82).
2. For `d=1`, `0<s<1`, the simplified move-function representation (83) applies and the source proof gives the force-balance relation appearing at equation (170)/(the limit recorded immediately after (83)).
3. Immediately before Conjecture 38, Lewin says the desired statement concerns **all possible infinite Riesz equilibrium configurations**, not only lattice-energy minimizers, and says nothing like this was known to the author even in `d=1`.
4. Conjecture 38 prescribes, in the long-range regime, the scale `r=rho_b^{-1/d}`.
5. In the proof of Theorem 28, Step 1 does not prove pointwise equidistribution at every center. It proves that **most** bulk centers have small averaged discrepancy on all sufficiently large dyadic scales; the author explicitly says uniform equidistribution/no-large-hole control is missing.

A fresh bounded search through 2026-09-17 did not locate a later theorem matching the all-equilibrium-configuration statement. The closest recent one-dimensional results I recovered are De Luca--Goldman--Ponsiglione, *Dynamics of screened particles towards equi-spaced ground states*, Adv. Calc. Var. 19 (2026), 399–422, and De Luca--Pini--Ponsiglione--Santilli, arXiv:2607.29663, *Periodic ground states for a one-parameter family of nonlocal energies on the real line*. Both are about screened **periodic/global-minimizer** problems. They do not classify every Lewin/Theorem-28 finite-replacement equilibrium configuration. This is bounded negative evidence, not a novelty certificate.

## 3. New theorem: a full-density Theorem-28 extraction has the conjectured scale

### R14-C192 — correctly scaled crystalline extraction in `d=1`, `0<s<1`

**PROVED on the page below; self-check only; external audit count `0/2`.**

> **Theorem.** Fix `d=1`, `0<s<1`, background density `rho_b>0`, chemical potential `mu in R`, and the grand-canonical minimizers `X_ell` from Lewin's Theorem 28. There exists a choice of bulk recentering points `tau_ell`, a subsequence, and a Theorem-28 local limit `X` such that
>
> `X = rho_b^{-1} Z + tau`
>
> for some `tau in R`.
>
> More generally, any Theorem-28 extraction whose recentering sequence satisfies the countable full-density version of Step 1 used below has the prescribed scale.

This is **not** the full long-range clause of Conjecture 38: it proves that one can extract a correctly scaled crystalline equilibrium from the finite grand-canonical minimizers. It does not yet prove that *every* abstract/source equilibrium configuration, or every possible thermodynamic recentering, has the same scale.

### Proof

Scale first to `rho_b=1`; the final statement follows by the source scaling.

Lewin's Step 1 defines, for bulk centers `tau`, the averaged discrepancy bad set

`A_{ell,eps,k}`

and proves in `d=1`

`|A_{ell,eps,k}| <= C |Omega_-| / (eps^2 2^{k(1-s)})`.

After summing over all dyadic scales `2^k >= M`, the source obtains

`| union_{2^k>=M} A_{ell,eps,k} | <= C |Omega_-| / (eps^2 M^{1-s})`,             (3.1)

with the upper scale restricted in the finite container by `2^{k+1} <= delta ell`.

Choose a deterministic sequence `eps_m downarrow 0`, for instance

`eps_m = 2^{-m}`,

and choose dyadic `M_m` sufficiently large that

`C/(eps_m^2 M_m^{1-s}) <= 2^{-m-2}`.                                            (3.2)

For each large `ell`, let `m(ell)` be the largest integer tending to infinity sufficiently slowly that

`2 M_{m(ell)} <= delta ell`.

For every `m <= m(ell)`, delete from `Omega_-` the centers that fail the Step-1 discrepancy condition at some allowed dyadic scale `2^k >= M_m`. By (3.1)-(3.2), the total deleted relative measure is at most

`sum_{m>=1} 2^{-m-2} = 1/4`.

Hence the intersection of all the good-center sets for `m <= m(ell)` is nonempty. Choose `tau_ell` in that intersection and translate coordinates so that `tau_ell` is the origin.

The `m=1` condition supplies the fixed coarse density bound needed by Lewin's Step 1 to obtain an infinite local cluster; separation then gives the usual diagonal extraction. Pass to a subsequence so that the translated finite configurations converge locally to `X` and the Theorem-28 potential/equilibrium conclusions hold.

Fix now one `m` and one dyadic `2^k >= M_m`. For all sufficiently large members of the subsequence, `m <= m(ell)` and the upper finite-container restriction also holds. Therefore

`| 2^{-k} int_{2^k}^{2^{k+1}} q_{r,0}(X_ell) dr | <= eps_m`,                    (3.3)

where in the bulk

`q_{r,0}(X_ell) = (#(X_ell cap [-r,r]) - 2r)/(2r)`.

Local convergence plus the uniform separation allows passage to the limit in (3.3): for almost every `r` there is no point on the boundary `{+-r}`, the counts stabilize, and on a fixed compact `r`-interval they are uniformly bounded. Hence

`| 2^{-k} int_{2^k}^{2^{k+1}} ( #(X cap [-r,r])/(2r) - 1 ) dr | <= eps_m`       (3.4)

for every `2^k >= M_m`.

Now invoke `R14-C191`: every such one-dimensional positive long-range equilibrium limit is an arithmetic lattice,

`X = a Z + tau`, `a>0`.

For a lattice,

`#(X cap [-r,r]) = 2r/a + O(1)`,

uniformly in `r>=1`. Therefore the quantity inside the absolute value in (3.4) converges, as `k->infinity`, to

`a^{-1}-1`.

Thus, for every `m`,

`|a^{-1}-1| <= eps_m`.

Since `eps_m -> 0`, we obtain `a=1`. Undoing the initial scaling gives

`a=rho_b^{-1}`.

This proves R14-C192. ∎

## 4. Why this still does not give the all-equilibrium scale: exact DLR background cancellation

The attempted #5/#11 route uncovered a clean obstruction that is useful in its own right.

### R14-X44 — the local finite-replacement functional is explicitly background-blind after `Phi` is fixed

**PROVED algebraically; this is an obstruction, not a refutation of Conjecture 38.**

Let `D` be bounded, let `X_D=X cap D`, and define

`I_D(y) := int_D |y-z|^{-s} dz`.

For a trial configuration `Y={y_1,...,y_n}`, Lewin's exterior potential is

`Phi_{D^c}(y) = Phi(y) - sum_{x in X_D}|y-x|^{-s} + rho_b I_D(y)`,

with the usual regularized interpretation when evaluating the current configuration at one of its own points. The Jellium energy has the form

`E_s(Y,D,rho_b) = sum_{a<b}|y_a-y_b|^{-s} - rho_b sum_a I_D(y_a) + C_{rho_b,D}`,

where the background-background term `C_{rho_b,D}` is independent of `Y`.

Therefore

`sum_a Phi_{D^c}(y_a) + E_s(Y,D,rho_b)`

is exactly

`sum_a Phi(y_a)
 - sum_a sum_{x in X_D}|y_a-x|^{-s}
 + sum_{a<b}|y_a-y_b|^{-s}
 + C_{rho_b,D}`.                                                            (4.1)

The explicit `rho_b` terms cancel particle by particle. In comparisons between `Y` and the current configuration, `C_{rho_b,D}` cancels as well.

There is a second invariance already anticipated in the source: replacing

`Phi -> Phi + C`, `mu -> mu + C`

leaves the local objective `L_D(Y)-mu |Y|` unchanged.

The exact coefficient bookkeeping was independently executed and archived in

`artifacts/R14/2026-09-17T04-49-34Z_i0089_background_cancellation_check.py`

and output

`artifacts/R14/2026-09-17T04-49-34Z_i0089_background_cancellation_check.out`,

which ends `BACKGROUND_CANCELLATION_PASS`.

**Consequence.** A proof of the prescribed long-range scale cannot come from equation (82) **alone** after an admissible renormalized potential `Phi` has been handed to us. The density parameter is carried by the *thermodynamic origin / zero-frequency discrepancy information* used to construct `Phi`, not by the explicit local DLR algebra. This exactly explains why C191's local force/rigidity proof recovered the lattice shape but not `a=rho_b^{-1}`.

This does **not** prove that a wrong-density lattice actually occurs as a Theorem-28 thermodynamic limit for background `rho_b`; establishing such an occurrence would be a counterexample, and I have not done that. R14-C192 instead proves that a countably full-density choice of source centers produces the correct scale.

## 5. The three new-method moves and what happened

### #5 — ADD A PARAMETER AND DIFFERENTIATE IN IT

I treated `rho_b` as an explicit parameter in the DLR functional rather than assuming the missing scale should fall out of C191. The result is stronger than a failed derivative computation: the `rho_b` dependence cancels **exactly** from every trial-configuration term once `Phi` is fixed. Thus varying `rho_b` inside the local equation cannot identify the lattice spacing. The parameter is encoded upstream, in the admissible thermodynamic construction of `Phi`.

### #11 — DUALIZE

The correct dual quantity is the charge/discrepancy zero mode

`#(X cap [-r,r]) - 2 rho_b r`.

Lewin's Step 1 controls this zero mode on most centers in an averaged dyadic sense. C191 controls the nonzero/local geometry by forcing every positive long-range equilibrium limit to be a lattice. Combining them makes the scale calculation one-dimensional: a lattice has a unique asymptotic density, so countably vanishing averaged discrepancy forces `1/a=rho_b`.

### #23 — DO WHAT THE PROPOSER DID NOT EXPECT

I assumed the opposite scale, `a != rho_b^{-1}`, and asked where the contradiction actually appears. It does **not** appear in the local DLR algebra because of R14-X44. It appears precisely when the thermodynamic extraction is required to be good for arbitrarily small discrepancy tolerances. This isolates the remaining all-equilibrium problem: rule out exceptional recenterings/phases that can evade the source's "most centers" discrepancy control at infinitely many large scales.

## 6. Exact remaining obligation for the long-range `d=1` source slice

The structural theorem is now complete for every positive `s<1`, and a correctly scaled source extraction exists. What is still missing for the literal all-equilibrium long-range clause is a **uniform density theorem**:

> For every source-admissible long-range equilibrium configuration at background `rho_b`, prove
>
> `lim_{R->infinity} #(X cap [-R,R])/(2R) = rho_b`,
>
> or prove an equivalent condition strong enough to exclude a wrong-density thermodynamic recentering.

The source itself says that pointwise equidistribution/no-large-holes is not known in this regime; its Step 1 proves the required discrepancy only for most centers. R14-X44 shows why the missing statement cannot be recovered by replaying local replacement inequalities.

A natural next attack, if this target survives the next stagnation trigger, is therefore quantitative finite-volume rigidity: exploit one-dimensional convexity of the Jellium energy to show that a macroscopic interval of anomalous lattice spacing has an energy excess that cannot be hidden in an `o(ell)` boundary layer. That would upgrade the source's averaged good-center result to all thermodynamic recenterings and close the `0<s<1`, `d=1` clause.

## 7. Status and audit discipline

- Frozen metric: `S_1 = 1 -> 1` (**no movement**).
- Unchanged streak after the first I0089 movement: `1 -> 2`.
- `R14-C190` short-range structural rigidity: PROVED on page / self-check, external audits `0/2`.
- `R14-C191` positive long-range structural rigidity: PROVED on page / self-check, external audits `0/2`.
- `R14-C192` full-density correctly scaled thermodynamic extraction: PROVED on page / self-check, external audits `0/2`.
- `R14-X44` DLR background-cancellation obstruction: exact algebra PASS / self-check.
- Full Conjecture 38: **PARTIAL / OPEN**.
- No paper folder is created because closure standard is not met.

The fixed metric is saturated but unchanged, so the next no-movement invocation will hit the owner's three-run stuck trigger even if additional non-metric structure is found. I do not reset that count.

## 8. Structured ledger_delta (own immutable report only)

```yaml
ledger_delta:
  track: R14
  canonical_target: I0089
  source: "Mathieu Lewin 2022, Conjecture 38 (Crystallization — configurations)"
  predecessor_target: "negative-margin spherical perceptron, handed off; not reopened"
  fixed_metric:
    name: S_1
    before: 1
    after: 1
    movement: false
    unchanged_count_before: 1
    unchanged_count_after: 2
  status: PARTIAL
  new_results:
    - id: R14-C192
      label: PROVED_SELF_CHECK
      statement: "There exists a countably full-density Theorem-28 extraction in d=1, 0<s<1 whose limit is rho_b^{-1} Z + tau."
      external_audits: 0
    - id: R14-X44
      label: CERTIFIED_OBSTRUCTION_SELF_CHECK
      statement: "After Phi is fixed, the explicit rho_b terms cancel from the local finite-replacement DLR comparison; density information must enter through the thermodynamic/discrepancy origin of Phi."
  retained_results:
    - "R14-C190: d=1, s>1 structural lattice rigidity"
    - "R14-C191: d=1, 0<s<1 structural lattice rigidity"
  remaining_obligation: "Upgrade source Step-1 most-center discrepancy to every source-admissible thermodynamic recentering/equilibrium configuration, or otherwise prove density(X)=rho_b for all long-range d=1 equilibria."
  methods: [5, 11, 23]
  next_methods_candidate: [1, 13, 24]
  prior_art: "bounded fresh search 2026-09-17; recent periodic/screened 1D ground-state papers found, no all-equilibrium Conjecture-38 resolution found; novelty unverified"
```

## 9. Runtime / scheduler-control truth

The repository's current deployment ledger and the exposed task schema still agree: GPT-6/maximum is only requested in prompt text. The scheduler surface available here exposes task prompt/title/schedule/timing/enabled controls, but no model-family selector, no reasoning-effort selector, and no authenticated runtime telemetry. Changing the actual model/reasoning choice would require the platform to expose those fields (or move the task into an authorized scheduler surface that does).

The old P26 `You cannot modify this task` event was context-specific, not a permanent mathematical or account-wide fact: the current root ledger records that P26's full prompt update later succeeded in the P/C authorized context, while a separate context denied edits to all R-series IDs. The legitimate workaround for a denied task remains the owning/authorized workspace context or platform support, never duplication or a permission bypass.

## 10. Persistence

Exact checker creation commit: `087a095ae7c809b937707440ad683ded457a8e9f`.

Executed output archive creation commit: `5f4f046981cda03fa6ad099bf1a2b4b58d9823a5`.

This report is immutable under `runs/R14/`; read back the actual report commit before treating this run as delivered.
