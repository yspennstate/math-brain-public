Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.

Date: 2026-09-20 UTC. Retained screen only: Talagrand F0111, k=2, PENDING / SELF_CHECK_ONLY / NOT CLAIMED. Native Burdzy--Scheutzow I0076 remains OPEN / PARTIAL / RETIRED-HANDOFF and is not reopened.

Methods for this run: #4 PROVE SOMETHING WEAKER COMPLETELY, #19 MAKE IT AN ALGORITHM, #30 DO ONE SCALE / ONE DIRECTION AT A TIME. Historical R15 work has already used every Section-B number, so the literal globally-never-used condition is exhausted; this triple is different from the preceding #8/#11/#24 and is applied to a new scalar object.

# Idea before checker: classify the entire scalar n=30 two-level feasibility envelope

The previous run proved that the heterogeneous one-heavy limiting system cannot occur as z=1+epsilon -> 1+ in dimension n=30, but the separation epsilon>0 was non-effective. Instead of another local expansion, use the exact scalar block inequalities already proved for every full-support two-level Hessian-null exact quadratic contact.

Write d=delta in (0,1), z=1+s with s>0, and let N=|K|. From the projective fourth-order/block-capacity argument and full-support positivity,

    N >= L_K(d,s) := y(d,s) A_K(d,s),
    N <  U_K(d,s) := -29 y(d,s)/k(d,s),

where

    k = 2 z(1-z^2)/[(1-d^2)(d+3z)],
    y = (d+z)(1-z)(1-d-2z)/[2(1-d)(d+3z)],
    A_K = 1 + 3 t_K^2/R,
    t_K = (1+z)^2 - (d+z)(1-z^2)/(d+3z),
    R = -2(d+z)(1-z^2)(d^2 z+3 d z^2+d+3 z^3)/(d+3z)^2.

Also Q_K=-k A_K and n=30 forces Q_K<29.

The route is:

1. Prove Q_K is strictly increasing in s. Since Q_K(d,0)=48/[(1-d)(1+d)^3], Q_K<29 localizes 2/5<d<3/5. Then prove exactly that Q_K(d,3/200)>29 throughout d in [2/5,3/5]. This gives the first explicit global separation

       0 < s < 3/200.

2. Prove L_K and U_K are strictly increasing in both d and s. Their boundary values are

       L_K(d,0)=6/(1-d),
       U_K(d,0)=29(1+d)^3/8.

   Together with 2/5<d<3/5 and s<3/200, this should force N in {11,12,13,14}, and sharper d-strips

       N=11: 11/25 < d < 5/11,
       N=12: 12/25 < d < 1/2,
       N=13: 13/25 < d < 7/13,
       N=14: 14/25 < d < 4/7.

3. For fixed N and s, monotonicity in d gives unique threshold points d_U(s), d_L(s) solving U_K=N and L_K=N. Scalar feasibility is exactly d_U(s)<d_L(s). A boundary collision satisfies U_K=L_K=N, equivalently U_K=N and Q_K=29.

4. Eliminate d from those two exact equations. The resultant appears to be a degree-nine polynomial p_N(s). Prove p_N is strictly decreasing on [0,3/200], has one sign change, and isolate its unique root s_N by exact rational signs. Then scalar feasibility is exactly

       0 < s < s_N,

   for the corresponding N. Preliminary exact algebra indicates the isolating intervals

       s_11 in (0.009291, 0.009292),
       s_12 in (0.014403, 0.014404),
       s_13 in (0.012636, 0.012637),
       s_14 in (0.004339, 0.004340).

If proved, this converts the remaining two-dimensional scalar n=30 search into four compact algebraic strips, with the global bound s<0.014404. It does not solve the full F0111 problem: even a scalar-feasible point still has to satisfy exact coefficient/contact/PSD/global-majorant constraints, and non-two-level/null-with-zero/second-contact mechanisms remain.

No numerical path sample is evidence here. The next action is an exact symbolic/rational checker only after the analytic route above has been fixed.