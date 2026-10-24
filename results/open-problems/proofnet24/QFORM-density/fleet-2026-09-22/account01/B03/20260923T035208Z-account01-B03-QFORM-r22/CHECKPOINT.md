SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B03, 2026-09-23T03:52:08Z.
attacking: close the h=1 decoupled one-volume endpoint by a random-slope sublevel estimate that keeps the hub diagonal arbitrary, then splice it into account02/B03's indefinite-pair logarithmic transducer.

# Early substantive checkpoint

Let X be independent of a pair (L,R), with density f_X<=1 and with L having a density g_L<=M. For any real a and
T=aX^2+2LX+R,
for every z and epsilon,r>0,

P(|T-z|<=epsilon)
 <= P(|aX+L|<=r)
   + P(|T-z|<=epsilon, |aX+L|>r)
 <= 2Mr + 2epsilon/r.

The first term conditions on X. For the second, condition on (L,R)=(l,s): q(x)=a x^2+2lx+s-z has derivative q'(x)=2(ax+l); on the region |ax+l|>r the sublevel set has at most two monotonic components, each of Lebesgue length at most epsilon/r. Since f_X<=1, its conditional probability is <=2epsilon/r.

Optimizing r=sqrt(epsilon/M) gives

P(|T-z|<=epsilon) <= min(1,4 sqrt(M epsilon)).

Hence for every 0<gamma<1/2,

sup_z E|T-z|^{-gamma}
 <= [1+gamma/(1/2-gamma)] (4 sqrt(M))^{2gamma}.

At gamma=1/4 this is <=4 M^{1/4}.

Application planned for the final report: in a residual cross block M_cross, choose a heavy row m. Rogozin/Ball gives the linear form L=m^T Y+const density cap <=sqrt(2)/||m||_2. This supplies the missing h=1/heavy-row endpoint while allowing an arbitrary hub diagonal a and arbitrary remaining quadratic curvature R(Y,conditioned variables). Combine it with account03/B03's diffuse k=1 endpoint when no row is heavy, and then apply account02/B03's completed indefinite-pair logarithmic transducer to recover linear small-ball scaling for the ambient form.

Full target remains open; this checkpoint is a supporting derivation, not a claim of completion.
