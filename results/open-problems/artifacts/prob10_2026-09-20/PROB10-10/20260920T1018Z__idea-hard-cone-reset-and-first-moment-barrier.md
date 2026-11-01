Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum was requested, but no authenticated model/effort receipt is exposed, so I do not claim GPT-6 maximum.

# Idea before code — reset the directional target to the genuinely hard cone

The current canonical parent is still ADH Question 4 specialized to iid Exp(1) undirected nearest-neighbor FPP on Z^2. The source metric remains c_* for Delta_12=2 mu(e1)-mu(1,1), and is still 0.

Before tuning another local-SAW transfer, test whether the recently reported reflected cones |y|>=rho x with rho>1 are actually source-relevant. They are not: for any D4-invariant norm N on R^2, convexity plus sign symmetry implies coordinatewise monotonicity in the first quadrant. Hence for rho>=1,

N(1,rho)=rho N(1/rho,1)=rho N(1,1/rho)>=rho N(1,0),

and therefore

N(1,rho)+N(1,-rho)-N(2,0)>=2(rho-1)N(e1)>0  (rho>1).

Thus every reflected strict-triangle cone whose boundary is still >1 is already forced by norm geometry. The all-path inequalities in the earlier reports may remain true, but they must not be counted as progress toward strict convexity. The genuinely nontrivial reflected range is 0<rho<=1, with rho=1 already containing a hard boundary case.

This changes route selection. The newest P04 width-7/length-4 block gives a strong axis upper cap a47=1035580351964689/2000000000000000, but recombining it with the canonical weighted-SAW Chernoff lower-bound compiler can only produce another rho>1 cone. Before doing any more transfer-matrix tuning, test the negation: can any first-moment path-count/Chernoff argument of this type even reach rho=1 at c=a47?

At rho=1 the path family necessarily contains all binomial(2n,n) monotone E/N paths. The optimized Chernoff upper bound for one 2n-edge Gamma(2n,1) path at threshold c n has exponent

J(c)=c-2-2 log(c/2).

The monotone subfamily alone makes the optimized Chernoff union expression grow exponentially whenever J(c)<log 4. Algebraically this is equivalent to

log c > c/2-1.

For c=a47 this inequality appears to hold with a comfortable margin (~0.0829197), so the best first-moment Chernoff union expression over just the monotone paths already has positive exponential exponent ~0.165839. If exact rational log bounds certify this, then no longer-memory self-avoidance automaton or retitling of the same first-moment architecture can cross rho=1 at the consumed P04 cap: the obstacle is the genuine multiplicity of shortest monotone paths, not overcounting loops.

Three routes for this run:

1. D4 norm-geometry negation test of the rho>1 cone metric — expected to supersede that auxiliary metric as source progress.
2. Exact monotone-subfamily obstruction to the canonical first-moment weighted-SAW/Chernoff architecture at rho=1 — prove with rational logarithm bounds, not simulation.
3. Return to the genuinely dependence-sensitive lane: P20's reserved one-edge Busemann residual compiler or an asynchronous frontier/HJB variational comparison. The remaining source-relevant obligation should be stated in a way that cannot be paid by another rho>1 path-count cone.

No claim of full strict convexity is made here.