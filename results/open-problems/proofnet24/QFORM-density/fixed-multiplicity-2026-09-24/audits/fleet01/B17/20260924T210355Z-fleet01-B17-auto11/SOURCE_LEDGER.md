# B17 source ledger

Pinned baseline: 7c0d6e60946b19423e6400a12d34b473cf0591e2, manuscript blob 183ccd294763214e6a707e8d4749ff9a8cf7006d, SHA256 9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69.

Current standalone source: eeb752c8943536541b34b42b8bf48e924f4d3d2f, paper blob 19fb119877426b640b2c0dae19ec2f78a399fe11, SHA256 bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3.

Current 955-line paper verdict by exact ranges:
1-86 PASS; 87-160 PASS; 161-215 PASS; 216-297 PASS; 298-396 PASS; 397-527 PASS; 528-562 PASS; 563-597 PASS; 598-600 GAP_REPAIRABLE_LOCAL; 601-662 PASS after that repair; 663-766 PASS; 767-860 PASS; 861-935 PASS; 936-955 PASS for mathematical accounting, with bibliography-priority completeness UNCHECKED because it is not a proof premise.

The local defect is at lines 598-600 of the hyperbolic-pair proof. The positive tail chooses an original coordinate i_plus with |u_i_plus| >= rho0/sqrt(2). The negative tail must separately choose i_minus with |w_i_minus| >= rho0/sqrt(2); it cannot reuse the coordinate selected from u without justification. Since |u|=|w|=rho0, the same cutoff and numerical constants follow exactly. Thus the repair changes no theorem statement or constant.

Historical 790-line baseline verdict:
1-46 PASS; 47-90 PASS; 91-160 PASS; 161-217 PASS; 218-301 PASS; 302-400 PASS; 401-482 PASS; 483-525 PASS; 526-580 PASS; 581-645 PASS; 646-714 PASS; 715-749 PASS; 750-790 PASS for mathematical accounting, with bibliography-priority completeness UNCHECKED.

No fatal mathematical defect was found in the pinned 17-value theorem.
