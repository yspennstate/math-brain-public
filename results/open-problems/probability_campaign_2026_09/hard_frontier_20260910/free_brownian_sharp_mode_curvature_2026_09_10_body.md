Status: complete author-derived proof with exact-algebra and numerical controls; not independently refereed, not novelty-cleared, not fully formalized in Lean. This is new progress beyond the campaign's existing C=1 threshold candidate [[hasebe_ueda_problem_33_the_constant_is_one_2026_09_08]].

For a compactly supported probability measure mu of support diameter D and the variance-t semicircle law, mu boxplus S(0,t) has a unique mode m_t when t>D^2. Its physical density satisfies
p_t''(m_t) <= -(t-D^2)/(4*pi*(t-D^2/4)^(5/2)).
The bound is sharp for every t>D^2. For D>0, equality forces mu to be a translate of the equal law on {-D/2,D/2}. D=0 is the translated semicircle equality case. At t=D^2>0, zero mode curvature is possible only for the same symmetric endpoint law; its mode is quartically strict.

Proof file: ~\probability-hard-problems-20260910\P0174_CURVATURE.md, SHA256 b23e61582277523e8b6d28d4a5f2a6f706b5b94726b4a3f8d55d6616b8975776. The proof tilts by ((u-x)^2+v^2)^(-2), centers the tilted law, uses a<=D^2/4 and Var_Q((u-X)^2)<=a(D^2-4a), and then optimizes the physical-coordinate curvature over the entire feasible moment region. The Jacobian psi'(u)=2v^2/(a+v^2) at a critical point is essential. The two endpoint cases in the moment optimization are proved, not sampled.

Controls:5 exact symbolic identities,28 atomic-law/time cases at80 decimal digits, and7 independent finite-difference checks solving at nearby physical x coordinates. Equal two-point laws and point masses attain the bound. Evidence: ~/<private-repo>/12_cognitive_architecture/audits/evidence/2026/09/10/probability_publishability/p0174_curvature_controls.json. Controls do not prove the all-measure theorem; read the full written proof. Compact support is essential; this is not a theorem for arbitrary finite-variance inputs.

The governing source is Hasebe-Ueda, ALEA15(2018),353-374, Problem3.3 and Section2.2, DOI10.30757/ALEA.v15-15. A bounded web check found no direct preemption, but absence was not established. A September7 anonymous proof candidate on symmetric-unimodal closure is a different input class and is not a novelty clearance for this result.
