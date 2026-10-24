# C0023 statement for independent attack

For each integer d with 3 <= d <= 10, let E_d be the unordered pairs {x,y} of vertices of Z^d with ||x-y||_1=1. Under P_p, the variables omega_e, e in E_d, are independent Bernoulli(p). Let C_omega(0) be the vertices joined to 0 by finite open-edge paths, theta_d(p)=P_p(|C_omega(0)|=infinity), and p_c(d)=inf{p in [0,1]:theta_d(p)>0}. The target is theta_d(p_c(d))=0. By translation invariance and countability this is equivalent to absence of any infinite open cluster almost surely at p_c(d).

This packet scopes the target to nearest-neighbor BOND percolation. Site percolation has a different product space and its own critical parameter; it is not inferred from the bond statement.

Ranking source: RANKING_2026-09-07.csv, row 539, C0023, tier 5, attempted_un. The ranking title omits bond/site. Primary reduction source recovered: Gady Kozma and Shahaf Nitzan, arXiv:2401.12397 (2024). The 2026 literature search also surfaced later proof claims whose primary artifacts are being checked. CURRENT OPENNESS: UNKNOWN; this packet makes no novelty claim.

Independent roles: w430 adversary; w431 referee; w434 independently reviews any new result of w431. This file deliberately supplies only the target, assumptions, and provenance to the adversary.
