# C064 — Stochastic-covering entropy acceleration (historical checkpoint)

Completion note: the full proof is now in agents/C064.md. The updated exact
verifier passes, including the fair-middle identity and the shorter sharp
count Fisher decomposition. The interrupted derivation below is retained as
history; its former in-progress status no longer applies.

Status: proved derivation checkpoint, 2026-09-15. Full report and exact verifier
are being written; the proof below does not rely on a numerical sign guess.

Inputs read: TARGET.md, PRIOR_FRONTIER.md, C033, C035, C044, C056,
ROOT_PROJECTION_ENTROPY_GLUE.md, ROOT_PROJECTION_ENTROPY_LEAD.md, and
ROOT_RANK_TWO_SPECTRAL.md. Prior rank-one-bottom diamonds, full-angle phase
diamonds, and tree-overlap projection-entropy submodularity are not counted as
new.

The present bounded direction is quantitative Fisher cancellation. For a fixed
projection flag with four projection entropies H0,H1,H2,H3 and
beta=H1+H2-H0-H3, the exact spectral-square entropy is

    F(lambda,mu) + affine - beta lambda mu
      + G(lambda(1-mu),mu(1-lambda)),

where F is the two-Bernoulli count entropy and G is the homogeneous
Jensen-Shannon perspective. G has nonpositive same-sign affine curvature.
Thus a sharp quantitative same-sign lower curvature bound on F could absorb
a bounded *negative* beta. The unknown step is a useful cover-based entropy
defect bound, without incorrectly inferring entropy submodularity from an
unlabeled diamond coupling.

The gap closes as follows.

1. Fairly order the two additions of an unlabeled rank-r diamond as i,j. Put
   M=S+i, N=S+j; both have the aggregate middle law m=(mu1+mu2)/2. Strong
   subadditivity gives

       2 H(m)-H(S)-H(T)
       >= log 2 + H(S|T)-2 H(S|M)
       >= log 2-2 log(r+1).

   Subtracting twice the Jensen-Shannon divergence of mu1,mu2 proves

       beta >= -2 log(r+1)-log 2.

   In particular every rank-one-bottom diamond has beta >= -3 log 2.

2. For the two-Bernoulli count law f=(a,b,c), let rho=sqrt(ac)/b<=1/2 and
   z=1/rho>=2. The count Fisher matrix has entries

       I11=(v+d^2)/(v b), I22=(w+d^2)/(w b), I12=1/b,

   where v=p(1-p), w=q(1-q), d=p-q. For same-sign slopes alpha,zeta,

       I/(2 alpha zeta)
       >= [1+sqrt(1+b(z^2-4))]/b
       >= z+2.

   The last step follows from b<=z/(z+2) and monotonic decrease in b of the
   displayed function. Since F''=-I+4 alpha zeta log z,

       F'' <= -2(4-2 log 2) alpha zeta.

   The constant is sharp at p=q=1/2, alpha=zeta.

3. The nonpositive same-sign Jensen-Shannon-perspective curvature gives

       H'' <= -2(4-5 log 2) alpha zeta <= 0

   for any rank-one background flag. Opposite-sign slopes are handled by the
   already proved arbitrary rank-one-bottom diamond construction. Therefore
   H(P_{ww*+p uu*+q vv*}) is jointly concave on [0,1]^2 for arbitrary
   orthonormal complex w,u,v in every ambient dimension. Complementation also
   covers arbitrary top-codimension-one flags.

This does not claim beta>=0. Only agents/C064.md and computations/C064/ are
owned. No subagents or external writes are used.
