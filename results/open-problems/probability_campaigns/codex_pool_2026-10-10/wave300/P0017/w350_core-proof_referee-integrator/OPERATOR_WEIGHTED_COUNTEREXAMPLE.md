Draft counterargument to the stronger operator-norm weighted input, w350, 2026-10-10

Independent review requested; this is not an audited theorem or a full KLS proof. It concerns the stronger sufficient input mentioned in w349 WEIGHTED_GAP.md, not the actual covariance estimate (W).

For a prior mu and observation Y_t=tX+sqrt(t)G in dimension one, write A_t(Y_t)=Var(X|Y_t), V_t(f)=Var(f(X)|Y_t), and

B_mu(t,f)=E[A_t V_t(f)]/E[V_t(f)].

Claim: no universal T>0 and finite K bound B_mu(t,f)<=K for every compactly supported full-dimensional isotropic log-concave mu, every smooth fixed f, and almost every t in (0,T). In fact the unbounded shifted-exponential prior has

lim_{c increases to 1/2} B_mu(t,exp(c x))=1/t

for every fixed t>0. The violations transfer to compact isotropic priors. The actual quantity E|Cov_mu_t(f,X)|^2/E Var_mu_t(f) is NOT asserted to have this limit or to violate (W).

1. A finite prior Poincare bound, with its proof visible.

The rate-one exponential law on [0,infinity) has C_P<=4. For a centered function h, put g(y)=h(y)exp(-y/2). In the weighted Sobolev domain, g and g' belong to ordinary H^1 on the half-line, and g^2 tends to zero at infinity. Integration by parts gives

int h'^2 exp(-y)dy = int g'^2 dy + (1/4)int g^2 dy - (1/2)g(0)^2.

Centering says int g(y)exp(-y/2)dy=0. Hence int g'(y)exp(-y/2)dy=-g(0). Cauchy-Schwarz, using int exp(-y)dy=1, gives g(0)^2<=int g'^2 dy. Therefore the energy is at least (1/4)int g^2 dy=(1/4)Var(h). Initially this can be read for smooth functions with the stated integrability and then extended by cutoff/density. Translation gives C_P<=4 for X=Exp(1)-1.

Claim A of ATTEMPT.md consequently gives, for this prior and every L^2 f,

E[V_t(f)] >= Var_mu(f)/(1+4t).

The channel normalization agrees: conditioning on tX+sqrt(t)G is equivalent to conditioning on sqrt(t)X+G.

2. Posterior variance and deterministic test functions.

For the same prior, the posterior at Y_t=y has density proportional to exp((y-1)x-tx^2/2) on x>=-1. It is N((y-1)/t,1/t) truncated at -1. Thus 0<A_t(y)<=1/t, A_t is continuous, and A_t(y) tends to 1/t as y tends to positive infinity. These facts are separately checked in the w349 posterior-counterexample review.

Take the fixed smooth function f_c(x)=exp(c x), 1/4<=c<1/2. It is in L^2(mu), and

E f_c^2 = exp(-2c)/(1-2c),
Var(f_c)/E f_c^2 = c^2/(1-c)^2 >= 1/9.

Consequently E V_t(f_c)>=E f_c^2/[9(1+4t)].

Let D_t(y)=1/t-A_t(y), which is nonnegative and bounded by 1/t. Since V_t(f_c)<=E[f_c^2(X)|Y_t], the tower property gives

0 <= 1/t-B_mu(t,f_c)
   = E[D_t(Y_t)V_t(f_c)]/E V_t(f_c)
  <= 9(1+4t) E[f_c^2(X)D_t(Y_t)]/E f_c^2(X).

The last normalized expectation is an expectation under the weighted joint law with density f_c^2(X)/E f_c^2(X). Under this weighting, X+1 has rate 1-2c and G remains independent standard Gaussian. Thus X tends to positive infinity in probability and Y_t tends to positive infinity in probability as c increases to 1/2, with t fixed. IMPORTANT: A_t(y) still denotes the posterior variance for the ORIGINAL rate-one prior, not a posterior recomputed under the weighted prior. Since D_t(y) tends to zero as y tends to positive infinity and is bounded, its weighted expectation tends to zero. This proves the stated limit.

3. Compact support, whitening, and an interval of violations.

For given T>0 and K>=0, choose deterministic t_* in (0,T) with 1/t_*>K. The preceding limit gives one fixed c<1/2 with B_mu(t_*,f_c)>K by a strict margin.

Let X_L have the original law conditioned on X<=L. Write m_L=E X_L and sigma_L^2=Var(X_L), and Z_L=(X_L-m_L)/sigma_L. Then Law(Z_L) is a compactly supported, full-dimensional isotropic log-concave law in dimension one. Its mean and variance normalization converge to those of X: m_L tends to 0 and sigma_L tends to 1. Use f_L(z)=exp(c(sigma_L z+m_L)), which can be multiplied by a smooth cutoff equal to one on the fixed compact prior support if a globally bounded test is required.

An observation t Z_L+sqrt(t)G is equivalent, after an invertible affine change of its value, to s X_L+sqrt(s)G with s=t/sigma_L^2. The posterior covariance of Z_L is the posterior covariance of X_L divided by sigma_L^2, and the test values are f_c(X_L). Thus the weighted ratio for the isotropic law equals sigma_L^(-2) times the original-variable ratio at s.

Here is a domination check for passage to the limit, rather than an unsupported assertion about conditioning. Couple X_L and X by their truncated-exponential inverse CDFs, so X_L<=X and X_L tends to X almost surely, with one independent G. For s in a compact interval [a,b] subset (0,infinity), posterior moments for X_L are those of a Gaussian truncated to [-1,L]. For increasing functions exp(2c x), they are at most the corresponding [-1,infinity) posterior moments. At observation y<=0, this moment is bounded by its value at y=0, uniformly for s in [a,b], by monotone likelihood ratio. At y>=0, the explicit truncated-normal formula bounds it by C exp(2c y/s), with C depending only on a,b,c: the lower-tail normalization Phi((y-1+s)/sqrt(s)) is bounded away from zero. At the coupled observation y=s X_L+sqrt(s)G this is dominated by

C(1+exp(2c X+2c|G|/sqrt(a))),

which is integrable because 2c<1. Posterior variances are bounded by 1/a. Gaussian integral formulas give pointwise convergence of the posterior moments as L tends to infinity and s tends to t_*. Dominated convergence therefore proves convergence of both E V and E[A V]. The limiting denominator is positive by step 1. The whitening identity above then yields convergence of the isotropic ratios to B_mu(t_*,f_c). For large L the compact isotropic ratio still exceeds K.

Fix this L and the fixed smooth f_L. Posterior moment integrals and their expectations are continuous in t>0; compact prior support makes domination immediate on every compact time interval. E V is positive. Hence the strict violation persists on an open interval around t_* contained in (0,T), not just at one exceptional time. This refutes the stronger input even with its almost-everywhere time quantifier.

The unresolved full-target input in this packet is still universal all-function variance retention, or the actual covariance estimate (W). The stronger operator-norm estimate cannot be substituted for (W). The proof is an author draft dependent on the complete Claim A derivation and the elementary exponential Poincare calculation above; w353 must independently check these and the conditioning/whitening limit before any theorem promotion. No numerical experiment or novelty claim is made.

NEXT: w353 audit the retained original posterior under the f_c^2 weighting and the compact-isotropic transfer; keep (W) distinct from its stronger operator-norm surrogate.
