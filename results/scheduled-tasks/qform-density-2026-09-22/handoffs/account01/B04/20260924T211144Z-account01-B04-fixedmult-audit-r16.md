# account01/B04 r16 handoff

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Fresh control pins: `AGENTS.md@207b1dfce26c35dd8437cb469a807071aa5a0f08`; `CURRENT_OBJECTIVE.md@194c09609c2ce750efaa9634a0849b5a27ff651c`.

Source pins:
- historical 790-line baseline: `7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`;
- current 955-line nine-direction paper: `eeb752c8943536541b34b42b8bf48e924f4d3d2f`, blob `19fb119877426b640b2c0dae19ec2f78a399fe11`, SHA256 `bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3`.

Audit:
- geometric Brascamp--Lieb heat-flow derivative sign, IBP, Gaussian domination, (t\to\infty), (t\downarrow0), monotone rough approximation: PASS;
- current paper lines 598--600 have a local repairable gap: the negative hyperbolic tail must choose a separate coordinate (i_-) with (|w_{i_-}|\ge\rho_0/\sqrt2), rather than reuse the coordinate selected from (u). Same defect occurs in historical lines about 472--474. Constants unchanged.
- historical line 735 has undefined `\norm{A/B}`; intended Schur-complement norm.
- current `verify_new.py` is not source-hash-bound; reproducibility-only gap.

New structural result `QFORM-S7-MAXSEED-EXCHANGE-DIFFUSENESS-v1`:
in normalized no-pivot (s_7(A)\ge1), any order-two seed with completion error (\varepsilon=\|E\|_F) has a same physical anchor (h) with an overlap packet at least ((1-\varepsilon)|\det B|), and both a row and column replacement with determinant ratio (>(11/2)(1-3/40-\varepsilon)). A globally maximal seed therefore has (\varepsilon>327/440), hence
[
V_3>(106929/193600)M_2.
]
If (V_3\ge V_2/800), the existing (Z_3) receiver gives density (<495). Otherwise the seed law has max atom (<242/106929), hence at least 442 nonsingular ordered seeds. More than (719/800) of seed mass has (\varepsilon\le1/3); each such seed has a same-anchor overlap packet (ge(2/3)|\det B|) and row/column replacement squared factor (>609961/57600). Good seeds contribute overlap mass (>719V_2/900). Multiplicity seven remains OPEN; missing step is a dependence-safe diffuse same-anchor analytic receiver.

The requested private `math-open-problems` write was attempted twice and blocked by the platform safety layer. It was not bypassed. Full audit/improvement/checks were preserved as conversation-local files for the owner.

Status: `WITHOUT_VERIFIED_BRAIN`. No scheduler/task state, email/push, public release, paid call, or cross-account authentication change.
