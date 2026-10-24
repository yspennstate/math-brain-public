# P0429: sharp collision scale for arrival paths

Label: proof for finite-horizon arrival-path total variation, pending w347. This does not determine the optimal batch size for a stationary queue vector at one time.

There are n servers. Jobs arrive as a Poisson process of rate Lambda=lambda*n/k and independently choose a uniform k-subset. Observe k fixed tagged servers on [0,T], with lambda,T>0. Their individual arrival streams have rate lambda. Let H be the hypergeometric number of tagged servers hit by one job and beta=Lambda*P(H>=2).

The total variation distance between the joint arrival-path law and k independent rate-lambda Poisson paths is at least 1-exp(-beta*T). Indeed the observed event that two tagged paths have a simultaneous arrival has probability 1-exp(-beta*T) in the original model by Poisson thinning, and zero under independent Poisson streams. Arrival times are continuous and the interval is observed exactly.

The factorial moments are E[(H)_r]=(k)_r^2/(n)_r. For nonnegative integer H,

    E[(H)_2]/2 - E[(H)_3]/2 <= P(H>=2) <= E[(H)_2]/2.

The upper inequality is the pair union bound. The lower follows pointwise from binom(h,2)-1_{h>=2} <= (h)_3/2 (check h=0,1,2, and for h>=3 use h-2>=1). If k grows and k=o(sqrt(n)), then E[(H)_3]/E[(H)_2]=(k-2)^2/(n-2)->0. Consequently beta ~ lambda*k^3/(2*n). In particular if k/n^(1/3)->c>0, the path-TV liminf is at least 1-exp(-lambda*T*c^3/2)>0. If n^(1/3)<<k<<sqrt(n), this lower bound tends to one.

For completeness, delete original jobs hitting at least two tagged servers and restore each lost marginal arrival rate with independent Poisson streams. The remaining one-tag streams are independent by Poisson marking; the restored marginal rates yield k independent rate-lambda streams. A disagreement probability is at most Lambda*T*(P(H>=2)+E[H*1_{H>=2}]) <= (3/2)*Lambda*T*E[(H)_2] = 3*lambda*T*k*(k-1)^2/(2*(n-1)). Hence k=o(n^(1/3)) suffices at fixed T. The cubic scale is therefore sharp for this exact-path coupling in the stated growing-k regime. Passing from path-TV to the stationary queue vector loses the simultaneous-time witness; no necessary stationary-vector threshold follows from this proof.

If each arrival adds a strictly positive service requirement, upward jumps of continuous workload paths reveal arrival times, so the lower bound also applies to joint workload paths versus independent workload paths. It still does not apply directly to one-time workload marginals.

Prior attempt quoted: "A finite-horizon input coupling suggests a cubic collision scale". That attempt already supplies the cubic sufficient regime and stationary burn-in bound; the new step is the measurable simultaneous-arrival witness proving the finite-horizon path obstruction.
