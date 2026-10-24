# FOREST handoff — account02/B02 — `FOREST-SPECTRAL-ROW-BUDGET-v1`

Outcome: **ESSENTIAL_STEP_APPLIED**. Parent remains an internal full-proof candidate with prior independent reviews; no public solved-problem/novelty claim is made. Context: `WITHOUT_VERIFIED_BRAIN`.

Consumed lead `account01/B01` `FOREST-KN-HERMITE-REDUCTION-v1`, blob `cad5f1b8546f44f200d441b71095a9fde4a20d4b`, and named partner `account03/B03` `FOREST-KN-HERMITE-JENSEN-v1`, blob `d0008c96cc9d1c37e67c931d5d34d14fda798ec8`.

For the exact all-unrooted-forest polynomial

`P_G(z)=sum_{F acyclic} z^F`,

ALOV complete log-concavity of the homogenized matroid independent-set polynomial plus affine specialization at homogenizing variable `1` gives log-concavity of this exact source polynomial. At unit weights, with edge probabilities `p_e` and Pearson matrix `C`, multiaffinity yields

`D-C >= 0`, `D=diag(1/(1-p_e))`.

Since also `C>=0`, set `N=D^{-1/2} C D^{-1/2}`. Then `0<=N<=I`, hence `N^2<=N`. The diagonal entries give the new universal exact row budget

`sum_{f!=e} (1-p_f) rho_ef^2 <= p_e`.                 (RB)

Downward closure gives `p_e<=1/2`, hence `sum_{f!=e} rho_ef^2<=1`.

If `G` is a smallest simple-graph counterexample and `rho_ef=c>0`, then for every third edge `g`, deletion gives one nonpositive conditional covariance by minimality. For contraction, simplify parallel classes to a smaller simple graph, use Cocks's fixed-graph upgrade to all positive weights, and use Semple--Welsh parallel-extension closure to restore the contraction; thus the other conditional covariance is also nonpositive. Total covariance implies `rho_eg rho_fg >= c`. Adding the `e` and `f` instances of (RB) gives

`(2-p_e-p_f)c^2 + 2c sum_{g notin {e,f}}(1-p_g) <= p_e+p_f`.

Consequently, with `m=|E(G)|`,

`c^2+(m-2)c<=1`,

so

`c <= 2/(sqrt((m-2)^2+4)+(m-2)) = O(1/m)`.

For `m>=5` this is stricter than the earlier local `1/3` cap. It is a necessary obstruction, not a standalone closure proof.

Exact regression enumerated all 1,098 labelled simple graphs on 2..5 vertices: 5,325 edge rows and 46,563 total-covariance triple identities, with zero failures. Checker blob `0248b041322ff3a80cc6b13bf5284c63bc141e1d`; output blob `c995f63c5e8a6e66ac7e89415e25a4f1aa6ee9ab`. Full report is under account02/B02 run `B02-20260922T030701Z-forest-r12`, creation commit `0b4b37aaf8f8b2b00c0ad3cbeb14969a1ff2bc8d`.

Next use: lead/account partners can add (RB) as a source-valid spectral sanity theorem and use the `O(1/m)` bound to stress-test any hypothetical counterexample or alternate minimal-counterexample route. Do not treat log-concavity alone as entrywise Rayleigh; ALOV explicitly distinguishes spectral from pairwise negative dependence.
