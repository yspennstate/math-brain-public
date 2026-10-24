# FOREST handoff — account01/B01 — 20260922T050946Z

Outcome: `ESSENTIAL_STEP_APPLIED`  
Candidate: `FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1`  
Canonical report: `yspennstate/math-open-problems`, `proofnet24/P14-probability-correlation/collective-2026-09-22/account01/B01/20260922T050946Z-b01-forest-auto11/report.md`, creation commit `79044b575c4b689248892f37b9930e983dddabca`.

## Source correction retained

The prior fixed-graph Cocks globalization remains rejected fail-closed. P14's unit coverage through nine vertices remains valid, but its 3-connected reduction used that weighted step and is not treated as unconditional. R02's `r_block<=6` theorem remains source-secure; the subsequent `r_block<=7` contraction-minor handoff also used fixed-graph Cocks and is conditional pending an independent contraction argument.

## Named peer consumed

Applied account02/B02 `20260922T041021Z-account02-B02-forest-r13`, report blob `d0ed896c51a038ac352aa45c3e9c40513e237dfb`. Its augmented log-concavity/Hessian mechanism is source-valid; its Cocks-dependent minimal-counterexample consequences were not imported.

## New mathematical payload

Let `R=r(M(G))`, `K=|F|`, `mu=E K`, `c_e=Cov(X_e,K)`, and `rho_eh` be the edge correlations under the exact unit uniform-forest law. Using the canonical rank-degree homogenized independent-set polynomial gives the stronger edge budget

`c_e^2/((R-mu)p_e(1-p_e)) + sum_{h!=e}(1-p_h)rho_eh^2 <= p_e`.

This strictly strengthens the peer's denominator `m-mu` to `R-mu`. The corresponding 3-by-3 slack-edge-edge PSD block uses `q=R-mu-Var(K)`.

Now choose an edge-minimal simple counterexample with violating pair `(e,f)`, `a=rho_ef>0`. If a third edge `g` lies in no triangle, both `G\g` and `G/g` are smaller simple graphs, so minimality applies to both conditional strata. Exact total covariance yields

`rho_eg rho_fg >= a`.

If `S` is the set of triangle-free third edges and

`T_i=c_i^2/((R-mu)p_i(1-p_i))`,

then adding the two rank-homogeneous edge budgets and using `p_h<=1/2` gives

`T_e + T_f + a^2 + |S| a <= 1`.

Moreover, restricted to physical edges that lie in no triangle, the graph of positive covariance pairs is a matching: transitivity follows from the same Simpson inequality and a positive 3-clique would force `x<=yz`, `y<=xz`, `z<=xy`, impossible for correlations in `(0,1)`.

## First missing comparison

For a triangle edge `g=uv`, conditioning on `g=1` and contracting creates parallel pairs only from common neighbors of `u,v`. After simplification this is exactly a smaller simple graph with weight 2 on a subset of one star centered at the contracted vertex and weight 1 elsewhere. The first source-generated debt is therefore a `{1,2}` **STAR-2** contraction comparison, not arbitrary positive weights. No STAR-2 proof is claimed.

Parent FOREST remains open. Continue `WITHOUT_VERIFIED_BRAIN`. Preserve the failed fixed-graph weighted route and attack STAR-2 or another direct triangle-conditioner mechanism next; do not relabel weighted `K_n` as a local bridge because the lead proved it parent-equivalent.
