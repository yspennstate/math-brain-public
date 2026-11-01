# Adversarial audit of w351's conditional-variance route

2026-10-10. ATTEMPT.md was saved before reading w351's APPROACH_PRECOMMITTED.md or CLAIMS.jsonl. The inspected w351 records were L0-L3. The actual L1 statement and proof explicitly assume maximal correlation rho<1 for all centered block-measurable L2 functions and almost-everywhere bounds on conditional Poincare constants. They do not infer those hypotheses from isotropy. The conditional-variance proof is valid as written: if P,Q are the two centered conditional projections, a=Pf, b=Qf and S=||a||^2+||b||^2, then S=<f,a+b> and ||a+b||^2 <= (1+rho)S yield S <= (1+rho)||f||^2. The sum of the two conditional variances is 2||f||^2-S. The affine normalization L0 is also correct under its stated finite-energy/positive-definite covariance hypotheses. This audit does not certify a complete KLS proof; none is asserted in those records.

The important missing premise for using L1 in a balanced recursive split is a dimension-uniform maximal-correlation gap. Here is a separate obstruction, using Euclidean balls rather than w351's simplex computations.

Let n=2d, d>=1, and let (U,V) be uniform on the Euclidean ball in R^{2d} of radius sqrt(n+2), with U,V each in R^d. This law is centered isotropic and log-concave. Put A=|U|^2 and B=|V|^2. Rotational symmetry and radial integration give

E X_i^2=1,
E X_i^4=3(n+2)/(n+4),
E X_i^2 X_j^2=(n+2)/(n+4) for i!=j.

For completeness, E|X|^4=n(n+2)^2/(n+4), since the radial density is n r^{n-1}/R^n on [0,R]. Rotating (X_i,X_j) by 45 degrees gives E X_i^4=3 E X_i^2 X_j^2. Expanding |X|^4 then gives the displayed moments. Consequently

E A=E B=d, Var A=Var B=d,
Cov(A,B)=-d^2/(d+2),
Corr(A,B)=-d/(d+2)=-n/(n+4).

Thus the maximal correlation rho between the block sigma-fields is at least n/(n+4). Any bound obtained by inserting rho in w351-L1 has factor 1/(1-rho) at least (n+4)/4. Isotropy gives Cov(U_i,V_j)=0; it does not control this nonlinear correlation.

The linear factor is necessary for the conditional-variance comparison itself on this example, not merely for that estimate of rho. Given U=u, V is uniform on the d-ball of squared radius n+2-|u|^2. Therefore, with t=d/(d+2),

E[B-d | U]=-t(A-d),
E[A-d | V]=-t(B-d).

Take f=A-B. Its mean is zero. Then Pf=(1+t)(A-d), Qf=-(1+t)(B-d), and Pf+Qf=(1+t)f. Orthogonality of conditional projections gives

E Var(f|U)+E Var(f|V)
 = 2 Var(f)-<f,(P+Q)f>
 = (1-t) Var(f).

In particular, for this polynomial f the ratio

Var(f) / [E Var(f|U)+E Var(f|V)] = 1/(1-t)=(n+4)/4

is exact. All moments and gradient energies are finite. More explicitly,

Var(f)=2n(n+2)/(n+4),
E|grad f|^2=4n,
Var(f)/E|grad f|^2=(n+2)/(2(n+4)).

The global Poincare ratio stays bounded while the proposed balanced-block comparison factor grows linearly. This rules out removing w351's maximal-correlation premise by appealing only to isotropic log-concavity for all balanced splits. It does not rule out a favorable unbalanced split, a different proof route, or KLS.

Verdicts: KEEP L0 and the projection calculation in L1 with their hypotheses. GAP for extending L1 to general KLS: neither conditional constants nor a uniform dependence gap is supplied. The ball example concretely blocks a uniform balanced-block variance comparison. L2-L3 simplex claims were used only as boundary metadata and are not certified here; no review of another review was performed.

New ball calculation: author derivation, pending independent w353 check. It is retained as draft concept material, not an independently checked theorem. w356 must independently referee any new theorem w353 contributes.
