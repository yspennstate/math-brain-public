Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum was requested, but authenticated runtime metadata does not establish GPT-6/maximum. SOURCE: OPEN -> OPEN. PROB10 METRIC MOVEMENT:** a complete cutoff theorem is proved under **pre-entropic long-range growth only up to `n exp(-rho_n)`**, with relative window `O(L_n^(-1/2)+(rho_n+log log n)/L_n)`; for `rho_n=A log log n` this retains the `Theta(sqrt(log n))` Gaussian profile while requiring no growth condition above `n/(log n)^A`. The historical `W_exp=1/2` floor does **not** numerically improve; the proved hypothesis/class scope does. Three approaches: **truncated Altschuler entropy architecture (SUCCESS); derive it from transitivity+gap (REFUTED by the two-copy expander obstruction); local-fiber/quotient gadgets (PRUNED as active peer-owned duplication).**

# PROB10-08 — pre-entropic long-range growth suffices for cutoff

Repository: `yspennstate/math-open-problems`, branch `master`.

Status: **PARTIAL / SOURCE OPEN / NEW REPOSITORY THEOREM / NOT INDEPENDENTLY AUDITED / WORLDWIDE NOVELTY UNVERIFIED**.

## 1. Required continuity and consumed state

Before research I read the controlling PROB10 contract and current source/exclusion/ownership state:

- `operations/PROB10_2026-09-20.md`;
- current root `POSTED.md`;
- `operations/claims/I0112.md`, blob `707af6a4ca81d0d6bcf52225c6f69c266ae981e9`;
- the R16 successor handoff `artifacts/prob10_2026-09-20/PROB10-08/2026-09-19T23-45-09Z_r16-h0002-handoff.md`, blob `fa18fa8669a638c362ad0f90300b733425e808e5`;
- preceding own report `runs/prob10_2026-09-20/PROB10-08/2026-09-20T00-47-46Z_large-lre-quotient-cutoff_a91e.md`, blob `828ecfe99ee65fc3343a46dae18843ba8bc64dec`;
- newest related P26 report `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_03-57-13__finite-fiber-entropy-transfer.md`;
- repository search of the full earlier I0112 sequence, including product-varentropy, synchronous tensor, moving-window/local-Poincare, Hecke/information-curvature, first stuck recovery, and the tree-subcommutation obstruction.

The R16 handoff preserves its actual intervening successor H0002: newest recovered H0002 report `runs/R16/2026-09-19T22-44-21Z_h0002-balanced-split-isotonic-leakage_8d31.md`, status PARTIAL with `G_layer -> G_split`, remaining all-prefix isotonic/KKT optimization. Nothing from H0002 was overwritten or silently relabeled.

The posted Abelian Cayley/product-condition paper remains excluded. This run is only Salez Problem 2.3 / I0112.

Master immediately before the first write in this run was `2d067d9d3b49cd0f02a4e79725ea03717b228549`.

## 2. Frozen source and current lead

Source target: Justin Salez, arXiv:2508.21055v1, Problem 2.3: every bounded-degree vertex-transitive expander sequence should exhibit total-variation cutoff for rate-one continuous-time SRW

`H_t=exp(t(P-I))`.

Current primary lead: Dylan J. Altschuler, arXiv:2609.14945v1, submitted 14 September 2026. I reread the proof through Lemmas 3.2--3.4 and the covering-tree argument, including the exact uses of long-range expansion. The current arXiv record checked in this run still exposed v1; a bounded correction/erratum search surfaced no v2 or correction. That is current-search evidence, not a guarantee about unpublished correspondence.

The exact architecture is:

1. LRE on vertices -> directed growth on the oriented-edge NBRW state space (Lemma 3.2);
2. directed growth -> near-maximal NBRW endpoint entropy (Lemma 3.3 / Proposition 3.1);
3. spectral expansion dissipates the residual entropy deficit;
4. the regular-tree radial CLT gives the cutoff center and Gaussian profile.

The new idea was written before any code: **stop the LRE argument at the entropy scale instead of macroscopic saturation, keep the resulting entropy deficit explicitly, and let the continuous-time spectral gap pay that deficit.**

## 3. New hypothesis

Fix `d>=3`, put `q=d-1`, and let `G_n` be connected `d`-regular graphs with `n=|V(G_n)| -> infinity` and

`1-lambda_2(P_n)>=gamma>0`.

For fixed `c>0` and a defect sequence `rho_n>=0`, assume

**(PE)** for every nonempty `S subset V(G_n)` and integer `r>=0`,

`|S| q^r <= n exp(-rho_n)`

implies

`|B(S,r)| >= c |S| q^r`.

No lower bound on `|B(S,r)|` is assumed once the tree-volume scale exceeds `n exp(-rho_n)`.

This is strictly weaker as a formal hypothesis than Altschuler's full LRE requirement. I do **not** claim in this report that a new explicit transitive family has been separated from all previously published positive cutoff classes; worldwide/priority separation remains UNVERIFIED.

## 4. Proved theorem

Let

`L_n=log_q n`, `v=(d-2)/d`, `T_n=L_n/v=(d/(d-2))L_n`.

### R16-PROB10-08-C3 — pre-entropic LRE cutoff theorem

Under (PE), there is `C=C(d,c)` such that every NBRW endpoint law at or beyond the entropic radius `j_n=min{j:dq^(j-1)>=n}` satisfies

`H(K_j(x,.)) >= log n - Delta_n`,

uniformly in `x,j`, where

`Delta_n <= rho_n + C log log n + C`.                           (4.1)

Consequently, for every fixed `epsilon in (0,1/2)`, if

`rho_n=o(log n)`,                                               (4.2)

then

`|t_mix^(n)(epsilon)-T_n|`

` <= C_(d,c,gamma,epsilon)[sqrt(L_n)+rho_n+log log n+1]`,       (4.3)

and therefore

`[t_mix(epsilon)-t_mix(1-epsilon)]/t_mix(1/2)`

` = O_(d,c,gamma,epsilon)(L_n^(-1/2)+(rho_n+log log n+1)/L_n)`

` = o(1)`.                                                      (4.4)

Thus Salez-convention continuous-time SRW has cutoff.

If moreover

`rho_n=o(sqrt(log n))`,                                        (4.5)

then for every fixed real `z`,

`sup_x | ||delta_x H_(T_n+z sqrt(L_n))-pi_n||_TV - Phi(-v^(3/2)z) | -> 0`. (4.6)

A clean concrete scope is `rho_n=A log log n` for any fixed `A`: it is enough to have tree-rate set growth only until `|S|q^r` reaches `n/(log n)^A`. No macroscopic-scale LRE assumption remains, yet the optimal `Theta(sqrt(log n))` Gaussian profile is retained.

For the source, restrict C3 to vertex-transitive sequences. The proof itself does not use transitivity.

The complete proof was written before this report at

`artifacts/prob10_2026-09-20/PROB10-08/2026-09-20T01-48-49Z_pre-entropic-lre-proof_4f2a.md`

created at commit

`8a7d97b5b702a237af0ad4d7caca40c41d849661`

and read back at that exact commit; artifact blob `ec658d45ad0f921103d93f8b580c66c0ade75d9c`.

## 5. Proof audit on the page

### 5.1 Truncated vertex-growth -> truncated oriented-edge growth

Let `Omega={(u,w):u~w}`, `N=dn`, and let `Q` be NBRW on oriented edges. Choose a fixed integer `k` with

`q^(-k)<=c(q-1)/2`.

For `F subset Omega`, let `C` be the terminal vertices of `B_Omega(F,2k)` and `U subset C` those not reached at a positive time up to `2k`. Altschuler's path-reversal argument is local and gives

`|U|<=q^(-k)|C|`, `|C|>=|F|/d`.

Also `|C|<=K_k|F|`, where `K_k=1+q+...+q^(2k)`. If `r=2k+ell` and

`|F|q^r <= theta N exp(-rho_n)`, `theta=q^(2k)/(dK_k)`,

then

`|C|q^ell<=n exp(-rho_n)`,

so (PE) applies to `(C,ell)`. Subtracting the exceptional endpoints generated from `U` yields

`|B_Omega(F,r)| >= (c/2)|C|q^ell >= [c/(2dq^(2k))]|F|q^r`.

For `r<2k`, `|B_Omega(F,r)|>=|F|` supplies the fixed constant. Hence directed tree-rate growth holds up to `theta N exp(-rho_n)`.

### 5.2 The forest entropy induction needs growth only below that threshold

The exact induction in Altschuler Lemma 3.3 remains valid if the growth hypothesis is available only when `|S|q^r<=M`, provided one states the conclusion only when

`|S|q^(h+C0)<=M`.

The nontrivial recursive check is that every departure set `S_(t,i)` satisfies

`|S_(t,i)|q^((h-t)+C0)`

` <= |S|q^t q^(h-t+C0)`

` = |S|q^(h+C0)<=M`.

Thus the induction never invokes growth outside the allowed range. Starting from one oriented edge with `M=theta dn exp(-rho_n)`, it gives at time

`h_n=floor(log_q M)-C0`

entropy

`>=log(dn)-rho_n-O_(d,c)(log log n)`.

Double stochasticity of `Q` makes Shannon entropy nondecreasing under subsequent NBRW steps. Choosing the fixed `C0` large enough that `h_n<=j_n-1`, then forgetting the predecessor coordinate (cost at most `log d`) proves (4.1).

### 5.3 Paying the remaining entropy deficit in continuous time

For any law `mu`, with `f_s=d(mu H_s)/d pi`,

`-d/ds D(mu H_s||pi)=E(f_s,log f_s)`

` >=4E(sqrt(f_s),sqrt(f_s))`

` >=4gamma Var_pi(sqrt(f_s))`

` >=4gamma ||mu H_s-pi||_TV^2`.

Since TV is nonincreasing,

`||mu H_s-pi||_TV <= sqrt(D(mu||pi)/(4gamma s))`.                (5.1)

Therefore an endpoint law with deficit at most `Delta_n` is `epsilon`-mixed after `O_(gamma,epsilon)(Delta_n)` extra continuous time. Only the **one-sided** spectral gap is used.

### 5.4 Covering-tree radial CLT

For rate-one continuous-time SRW on the infinite `d`-regular tree, let `R_t` be distance from the root. Projection gives

`delta_x H_t = sum_j Pr(R_t=j)K_j(x,.)`.

The radial drift is `v=(d-2)/d`, returns to the root contribute only a tight correction, and Poissonization gives

`(R_t-vt)/sqrt(t) => N(0,1)`.

Combining this with (5.1) gives the upper side `T_n+O(sqrt(L_n)+Delta_n)`. For the lower side, use a ball of radius `L_n-b_n` with `b_n->infinity`, `b_n=o(sqrt(L_n))`; its stationary mass is `o(1)` by the universal degree bound, while the radial CLT supplies the matching lower probability. This proves (4.3)-(4.4). If `Delta_n=o(sqrt(L_n))`, choose an entropy-dissipation time `s_n` with `Delta_n/s_n->0` and `s_n=o(sqrt(L_n))`; the same upper/lower sandwich gives (4.6).

## 6. Three materially different approaches

### A. Stop Altschuler at the pre-entropic scale — SUCCESS

This is C3. The exact use of LRE was isolated: the proof only needs enough tree-rate growth to create all but `o(log n)` nats of endpoint entropy. The fixed spectral gap can manufacture the remaining entropy in `o(log n)` continuous time.

### B. Derive C3's hypothesis from vertex transitivity + spectral gap — REFUTED

The obstruction is already implicit in Altschuler Section 2.3. Let `H_m` be a `d`-regular vertex-transitive spectral-expander sequence and form `G_m=H_m square K_2`, i.e. two copies joined by the matching between corresponding vertices. Then `G_m` is `(d+1)`-regular, vertex-transitive and a one-sided spectral expander. But for the top branching parameter `q_top=d`,

`|B_G((x,i),r)| <= 2|B_H(x,r)| <= C_d(d-1)^r`.

For any `rho_n=o(log n)`, at `r=floor((1/2)log_d n)`, the PE admissibility condition `d^r<=n exp(-rho_n)` holds eventually, while

`|B_G((x,i),r)|/d^r <= C_d((d-1)/d)^r ->0`.

Hence no fixed `c>0` makes (PE) follow from transitivity plus spectral expansion. This is **not a counterexample to cutoff**; it is a finite structural obstruction to completing Salez 2.3 via any theorem that still insists on maximal tree-rate volume growth, even only to `n exp(-o(log n))` scale.

### C. Local fiber / quotient transfer — PRUNED as duplication

The newest P26 report proves an exact finite-fiber entropy/TV transfer for lexicographic blow-ups, while NM13 owns the related line-graph mechanism. Re-entering that route would duplicate active neighboring work. It was therefore not repackaged as R16 progress.

The earlier I0112 product-varentropy, synchronous-tensor, moving-Poincare, Hecke/curvature and tree-subcommutation failures were likewise not repeated.

## 7. Source before/after, metric accounting, and remaining gap

**Source before:** OPEN. Altschuler proves cutoff for fixed-degree full long-range expanders. The earlier R16 runs additionally had a vanishing-LRE quantitative extension and a large-LRE-cover quotient transfer, both PARTIAL.

**Source after:** still **OPEN**. C3 proves cutoff from the weaker pre-entropic growth condition (PE), with exact defect-dependent window. This is a real theorem, but it does not derive (PE) from the source assumptions.

**Historical `W_exp`:** remains `1/2` (provisional restricted-family floor) rather than being falsely reported as numerically improved. The new progress quantity requested by PROB10 is the **complete proved hypothesis/class and the quantitative relative window**, namely (PE) plus (4.4).

**Strict literature class separation:** UNVERIFIED. I do not claim that C3 supplies an explicit transitive sequence outside every previously published positive cutoff class. The theorem is therefore safest to record as a proved mechanism/class-hypothesis enlargement, not a worldwide novelty certificate.

**Remaining full-scope gap:** the two-copy obstruction proves that a full proof cannot simply deduce even truncated maximal-tree-growth from transitivity and a fixed spectral gap. The next genuinely different target is a weighted or average collision/Green-function estimate whose benchmark adapts to local product structure instead of using the ambient degree's tree rate. Such an estimate must survive `H square K_2` and the earlier product/tensor obstructions.

## 8. Current-source checks and tests actually run

Current-source checks during this iteration:

- Salez, arXiv:2508.21055v1, exact Problem 2.3 and continuous-time convention;
- Altschuler, arXiv:2609.14945v1, full cutoff proof through Lemmas 3.2--3.4 and the covering-tree argument; current arXiv history still showed v1 in the bounded check;
- Altschuler Section 2.3 two-copy spectral-expander/non-LRE construction;
- surrounding Pedrotti--Salez local-product and Sarnak--Xue/spectral-density literature to avoid relabeling known criteria;
- current repository neighboring P26/NM13 transfer work.

No finite computation was used or needed. No finite checker was manufactured. The retained claims are analytic and the full proof is written in the artifact. This report is a self-check, not an independent audit.

## 9. Structured ledger delta

```json
{
  "task": "PROB10-08",
  "source": "Salez arXiv:2508.21055v1 Problem 2.3",
  "source_status_before": "OPEN",
  "source_status_after": "OPEN",
  "claim_id": "R16-PROB10-08-C3",
  "claim_status": "PARTIAL / proved restricted theorem / not independently audited",
  "historical_W_exp_before": "1/2 provisional restricted-family floor",
  "historical_W_exp_after": "1/2 provisional restricted-family floor",
  "mechanism_before": "full/vanishing long-range expansion and quotient transfer",
  "mechanism_after": "pre-entropic long-range growth only up to n exp(-rho_n)",
  "hypotheses": "fixed d-regular, one-sided spectral gap gamma>0, PE: |B(S,r)|>=c|S|(d-1)^r whenever |S|(d-1)^r<=n exp(-rho_n)",
  "endpoint_entropy_deficit": "rho_n + O_{d,c}(log log n)",
  "relative_window": "O_{d,c,gamma,epsilon}(L_n^{-1/2} + (rho_n+log log n+1)/L_n)",
  "cutoff_condition": "rho_n=o(log n)",
  "gaussian_profile_condition": "rho_n=o(sqrt(log n))",
  "clean_subclass": "rho_n=A log log n: growth only through n/(log n)^A gives Theta(sqrt(log n)) Gaussian profile",
  "critical_obstruction": "vertex-transitive spectral expanders H square K2 fail PE for every rho_n=o(log n)",
  "independent_audits": 0,
  "worldwide_novelty": "UNVERIFIED",
  "finite_tests": "none applicable; analytic proof only",
  "scheduler_changes": "none",
  "email_drive_public_changes": "none"
}
```

No scheduler state, cadence, enablement, email, Drive object, public posting, workflow, permissions, shared root ledger, or peer file was modified.