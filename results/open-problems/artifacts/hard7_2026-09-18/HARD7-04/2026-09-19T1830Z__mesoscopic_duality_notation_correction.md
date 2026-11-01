# HARD7-04 immutable-report notation correction

This is a notation-only correction to the immutable report

`runs/hard7_2026-09-18/HARD7-04/2026-09-19T1830Z__bhs_mst_cm_mesoscopic_finite_n_duality.md`

at commit `c09a79c9216330a3774ea3d433045bc29c73439f`.

In equation (8.5) and the matching phrase before (8.11), the plain-text concatenation

`q_n:=1-p_n+p_nu_n`

must be read as

`q_n := 1 - p_n + p_n * u_n`,

where `u_n` is the extinction probability introduced immediately above. It does **not** mean `p_n * nu_n`.

Separately, the plain-text concatenation `p_nnu_n` in (8.18) means `p_n * nu_n`, where `nu_n=h_n'(1)` is the branching factor.

With these multiplication signs restored, the definitions are the standard ones:

`phi_n(s)=h_n(1-p_n+p_n s)`,

`u_n=phi_n(u_n)`,

`q_n=1-p_n+p_n u_n`,

so `q_n=1-p_n+p_n h_n(q_n)` and every subsequent secant identity in the report is unchanged.

No mathematical statement, bound, asymptotic, status label, or frozen metric is changed by this correction. The original run report remains immutable.