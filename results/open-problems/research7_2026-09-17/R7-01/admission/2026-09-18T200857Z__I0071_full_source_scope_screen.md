Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# R7-01 — I0071 full-source scope reconciliation

Date: 2026-09-18 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Slot: `R7-01 Counterexamples and Constants`  
Native ID: `6aabe777361481919c9e614646464772`  
State entering screen: `PENDING_ADMISSION`

## 1. Why I0071 is in this worker's shard

The owner's R7 partition acts on the exact case-sensitive canonical candidate **ID**, not on a title or source alias. For

`I0071`

one has

`73 + 48 + 48 + 55 + 49 = 273 = 39 * 7`,

so `sum(ord(c) for c in "I0071") % 7 = 0`. Thus I0071 is a legitimate R7-01 *screening candidate*. The partition is not ownership and does not make the source admissible.

The current intake row identifies I0071 as Agresti--Veraar, Problem 7, reaction--diffusion with triangular structure. The current master has no `operations/claims/I0071.md` file. The latest R7-01 checkpoint remained `PENDING_ADMISSION`, and the exact Git history query since that checkpoint found no `QUEUE.md` or `operations/claims/` mutation that releases or newly assigns shard-0 inventory.

## 2. Exact outside source and locator

Outside authors: **Antonio Agresti and Mark Veraar**.

Published source: **Nonlinear SPDEs and Maximal Regularity: An Extended Survey**, *Nonlinear Differential Equations and Applications NoDEA* **32**, article 123 (2025), published online 1 September 2025, DOI `10.1007/s00030-025-01090-2`.

Preprint: arXiv `2501.18561`, first submitted 30 January 2025.

Primary URLs:

- `https://doi.org/10.1007/s00030-025-01090-2`
- `https://arxiv.org/abs/2501.18561`

Exact locator: **Problem 7, “Reaction-diffusion with triangular structure”**, in the final open-problems section; published full-text page 131/150 in the repository copy / the campaign's canonical locator `Problem7,PDF93;system8.14`. The PDE referred to by the question is equation **(8.14)**.

The source's system (8.14), in its periodic presentation, is

\[
\begin{cases}
\mathrm d u_i-\nu_i\Delta u_i\,\mathrm dt
= f_i(\cdot,u)\,\mathrm dt
+\displaystyle\sum_{n\ge1}\big[(b_{n,i}\cdot\nabla)u_i+g_{n,i}(\cdot,u)\big]\,\mathrm dW^n,
\\
u_i(0)=u_{0,i},
\end{cases}
\]

for the components `i=1,...,ell`. The source notes that coupling is through `f` and `g`, while the diffusion/transport operators are componentwise.

## 3. Full source statement and quantifiers

Problem 7 asks whether **global well-posedness** holds when `O` is `T^d` or `R^d`, `ell >= 2`, the transport coefficients satisfy `(b_{n,i})_{n>=1} in C^gamma(O;ell^2)` for some `gamma>0` (with possibly additional boundary conditions outside the torus), and for a fixed `h>1`, each component satisfies all of:

1. nonnegative initial data `u_0 in [0,infty)^ell`;
2. `g_i:R^ell -> ell^2` is globally Lipschitz and vanishes on the boundary face `u_i=0` of the positive cone;
3. `f_i(u)>=0` on that same face;
4. polynomial local Lipschitz growth
   `|f_i(u)-f_i(u')| \lesssim (1+|u|^{h-1}+|u'|^{h-1})|u-u'|`;
5. a mass-control inequality of the form
   `sum_j f_j(u) <= K_0 + K_1 sum_j u_j` on the positive cone;
6. a triangular condition: there are `r in R^ell` and an invertible lower-triangular `ell x ell` matrix `R` with nonnegative entries for which
   `R f(y) <= [1+sum_i y_i] r` componentwise for every nonnegative `y`.

### Material source-scope correction

The source **does not stop after condition (6)**. Immediately after those six conditions it asks two further questions:

- whether global well-posedness still holds when the `g_i` have **superlinear growth**;
- whether one can allow the **optimal growth of `g`**, namely the source's Assumption 8.4(3).

This matters operationally. A proof only for globally Lipschitz `g_i` would answer the first displayed question but would **not by itself close the full Problem-7 source block** if the repository treats the whole numbered problem as the source target. Any future admission would have to freeze its closure criterion explicitly rather than silently dropping these final source sentences.

The current intake transcription is therefore unsafe as a self-contained closure specification: it records the beginning of Problem 7 and the six structural assumptions, but the final published-source questions must also be carried if the target is the full numbered source problem.

## 4. Current-source and follow-up check, dated 2026-09-18

The final 2025 NoDEA article itself still prints Problem 7 as open. This is stronger status evidence than relying on the earlier arXiv intake alone because it is the authors' revised published version.

The closest earlier author paper recovered is Agresti--Veraar, **Reaction-Diffusion Equations with Transport Noise and Critical Superlinear Diffusion: Global Well-Posedness of Weakly Dissipative Systems**, *SIAM Journal on Mathematical Analysis* 56 (2024), DOI `10.1137/23M1562482`. It proves global well-posedness for important subclasses, including weakly dissipative systems such as Lotka--Volterra and the Brusselator in specified dimensions. Its open-problems discussion explicitly says that deterministic triangular systems use a duality argument that the authors do not know how to extend to SPDEs with transport noise. The later 2025 survey was written after that work and still asks the general triangular problem.

A bounded 2026-09-18 search for the exact Problem-7 phrase, triangular stochastic reaction--diffusion systems, transport noise, and later Agresti/Veraar work did not recover a later theorem matching all of the published Problem-7 quantifiers. That is **negative evidence only** and is not a novelty or permanent-openness certificate.

A useful neighboring report, `proofnet24/NM13-04/runs/2026-09-18/2026-09-18T18-30-19Z__successor-admission-screen-i0060-i0130-canonical.md`, independently recovered the same Agresti--Veraar source family and the canonical preprint identity for Problem 7. That worker uses a different SHA-256/mod-13 partition, so its shard conclusion is not an ownership claim over R7-01's ID-mod-7 partition. Its source recovery is nevertheless useful corroboration and has been reused rather than ignored.

## 5. Admission classification

**Classification: HARD / BROAD; reject as an R7-01 CLOSABLE admission.**

The reason is source architecture, not pessimism about technique. A source-valid positive answer ranges simultaneously over dimensions/domains, arbitrary component count `ell>=2`, every fixed polynomial-growth exponent `h>1`, non-small transport noise in the stated regularity class, the mass and triangular structural inequalities, and then asks for a still stronger superlinear/optimal-noise extension. The deterministic proof uses a global duality mechanism, while the stochastic source itself identifies extending that mechanism through transport noise as highly nontrivial.

There is no source-fixed finite certificate, one-witness counterexample endpoint, sharp scalar constant, or short finite classification whose completion would settle the full numbered problem. Proving a special dimension, a special triangular matrix, small transport noise, bounded `h`, one reaction network, or globally Lipschitz `g` without the source's extension questions would be useful partial mathematics but would not be full-source closure.

Accordingly R7-01 does **not** relabel I0071 as CLOSABLE merely because it is unclaimed and happens to lie in shard 0.

## 6. Admission verdict and metric

- candidate ID: `I0071`;
- shard: `0` (eligible to screen);
- canonical claim: absent on the fresh master checked for this run;
- source classification: `HARD / BROAD`;
- R7-01 preferred class: `CLOSABLE OUTSIDE`;
- admission: **REJECTED / NOT CLAIMED**;
- source-matching successor metric: `UNKNOWN/UNMEASURED -> UNKNOWN/UNMEASURED`;
- successor stagnation count: `NOT_STARTED`;
- Section-B methods charged: **none**, because admission did not occur.

No theorem, simulation, proxy metric, or checker is credited. No canonical claim is created. No shared `RESULTS.md`, `QUEUE.md`, or `POSTED.md` file is edited.

## 7. Durable consequence

Absent a genuine source-status or ownership change, R7-01 should not spend another admission run re-reading I0071. If a future worker chooses to pursue it under a HARD allocation, the admission record must preserve the final two Problem-7 questions or explicitly state that it is admitting only a proper subproblem and must not call that partial target full-source closure.
