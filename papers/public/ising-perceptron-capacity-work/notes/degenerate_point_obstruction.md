# The degenerate-maximizer step: a precise account of what is needed

> **Historical note (superseded).** This file records an intermediate
> obstruction analysis and is not a statement of the final proof status. The
> Region-I ray/localization certificate subsequently closed the gap described
> below. See `../STATE.md`, the current manuscript, and the canonical
> `verification/results/huang_region1.json` certificate for the final status.

Both conditions (Huang 1.3, Ding-Sun 1.2) reduce, via the certified bulk
sweeps in this repo, to one remaining statement: the rate function is <= 0 on
an explicit neighborhood of each degenerate critical point (for Huang, the
point a* = (psi_0(1-q_0), q_0) in moment coordinates, image of (1,0)). At a*
the value is 0, the gradient is 0, and the Hessian is negative definite -- all
established pointwise (Huang's own unconditional lemma, reproduced here on a
fast grid). What is missing is an EXPLICIT radius rho with S_* <= 0 on
B(a*, rho), matched to the box the bulk sweep excludes.

This note records why neither of the two tools used elsewhere -- the
convex-duality bulk sweep and interval evaluation of the Hessian over a box --
can close it, so that the reader knows exactly what a solution must supply.

## The geometry: a nearly singular tilted covariance

nabla^2 Phi (the tilted covariance of (X, tanh X)) has eigenvalues about 0.366
and 0.0045 at a*: condition number ~ 82, because X and tanh X are strongly
correlated. Consequently nabla^2 H = -[nabla^2 Phi]^{-1} has eigenvalues about
-2.7 (weak) and -222 (strong). The full Hessian nabla^2 S_* = nabla^2 H +
nabla^2 G has eigenvalues about -0.58 (weak) and -224 (strong): the weak
direction is a near-cancellation, nabla^2 G contributing about +2.9 against
nabla^2 H's -2.7 there.

Everything hard happens in the weak direction, where the margin is only 0.58
and the map a <-> lambda is stretched by [nabla^2 Phi]^{-1} ~ 222.

## Why the bulk (dual-bound) sweep cannot approach a* in the weak direction

The sweep bounds H by its tangent at the cell's dual, H(a) <= Phi(b) - b.a,
which discards H's curvature. Along the weak direction the discarded curvature
is (1/2)|nabla^2 H_weak| d^2 ~ 1.35 d^2, while S_* itself only decays like
(1/2)|nabla^2 S_weak| d^2 ~ 0.29 d^2. Hence the dual-bound value is

  S_*^{ub}(a) - S_*(a) ~ 1.35 d^2,  so  S_*^{ub}(a) ~ (1.35 - 0.29) d^2 = +1.06 d^2 > 0.

The over-estimate has a POSITIVE coefficient independent of cell size: the
sweep is positive in the weak direction at every distance d, no matter how
fine the mesh. This is not a resolution problem; the linear entropy bound is
structurally too weak near a degenerate maximizer where G is not concave.

## Why interval evaluation of the Hessian over a box cannot certify it

To use S_*'s own curvature one needs nabla^2 S_* <= 0 (equivalently <= -c I)
enclosed over a box. Two routes, both blocked by the condition number:

- Moment coordinates. nabla^2 H = -[nabla^2 Phi]^{-1}. Inverting a nearly
  singular matrix amplifies its interval width by the condition number
  SQUARED (~ 5e4). Any box has a lambda-image of width >= (a-width) x 222, so
  nabla^2 Phi carries width >= 1e-3 even for a-boxes of side 1e-3, giving
  nabla^2 H width >= ~40 -- dwarfing the 0.58 margin. Shrinking the box does
  not help: the lambda-image shrinks in proportion, the amplification is
  fixed, and the box count to cover a fixed neighborhood grows like
  (222/0.58)^{...}, i.e. into the hundreds of thousands.

- lambda coordinates. Here nothing is inverted, but the frozen-tilt Hessian
  nabla^2 osS has weak margin only 0.0046, and the chain-rule terms
  (nabla^2_a T composed with the Jacobian) lose their cancellation under
  interval arithmetic, giving box widths of order 1-10 >> 0.0046.

Eigenvector-aligned boxes, higher precision, and 3rd/4th-derivative Taylor
bounds were all checked; each meets the same condition-number-squared wall or
the matching-margin wall. Precision does not help because the loss is
dependency/cancellation, not rounding.

## What a solution must supply

One of:

1. A closed-form (paper) proof that the relevant quadratic form is <= 0 on an
   explicit neighborhood, using the fixed-point identities that simplify the
   Hessian at a* (Huang's C_1,C_2,C_3 form) to control it off a*. The obstacle
   is that those identities hold only at a*; extending them to a neighborhood
   with sign control is the mathematical content.

2. A validated-numerics method for degenerate optima that avoids forming
   [nabla^2 Phi]^{-1} explicitly -- e.g. a Krawczyk/interval-Newton
   verification of the stationarity+definiteness system in the joint
   (a, lambda, s) variables with a preconditioner built from the approximate
   inverse at a*, so the amplification is applied to a residual rather than to
   the width.

3. A decorrelating reformulation of the constraint that makes the tilted
   covariance well-conditioned (a genuine change of the FUNCTION, since a
   linear change of coordinates leaves the condition number of the definiteness
   problem invariant).

Route 2 is the most likely to succeed with the present machinery: the pointwise
data (value, gradient, Hessian, and the residual of the stationarity system)
are all computed rigorously here; only the preconditioned inclusion test is
missing.

## Update: the bordered Hessian, and exactly why boxes still fail

`huang_bordered.py` implements the joint (bordered) Hessian B of
L(a,l,s) = Phi(l) - l.a + s^2 psi/2 + alpha T(a,s) in the 5 variables
(a1,a2,l1,l2,s). At a* it has inertia (3,2,0) and condition number ~92 -- the
-I coupling between the a- and l-blocks ABSORBS the near-singularity of
nabla^2 Phi. By Haynsworth additivity, B's inertia (3,2,0) together with the
(l,s)-block being positive definite proves nabla^2_a S_* is negative definite,
WITHOUT ever forming [nabla^2 Phi]^{-1}. This is a clean pointwise certificate
(cleaner than the direct reduced Hessian) and is included in `verify_all.py`.

It still does not certify over a box, and the reason is now precise and final.
B's a-block is alpha nabla^2_a T, whose entries vary by about 1.9e4 per unit a2
(the 1/D^3 * Ht^2 sensitivity). Over an a-box of radius r this block GENUINELY
moves by ~1.9e4 r -- this is real variation of a smooth function, not a wrapping
artifact, so mean-value/Taylor to any order gives the same leading width.
Pointwise this motion is exactly cancelled in the reduced Hessian by the
matching motion of the l-block through l = l(a); but that cancellation is
POINTWISE (each a pairs with its own l(a)), and any interval enclosure evaluates
the a-block over all a in the box against the l-block over all l in the image,
losing the pairing. Empirically the LDL^T pivots stay sign-indefinite down to
r = 5e-5 (a-block width ~1), and the box count to reach r = 2.6e-6 (a-block
width < 0.05) is ~10^7 -- infeasible, and no refinement removes the pairing loss.

Conclusion: the neighborhood step is not a resolution/precision problem; it
requires making the a<->l compensation explicit, i.e. an analytic (symbolic)
argument or a validated method that carries l as the function l(a) rather than
as an independent interval. The pointwise negative-definiteness -- the actual
mathematical content of "a* is a strict local maximum" -- is fully certified
here, three independent ways (Huang's frozen brackets, the envelope Hessian,
and the bordered inertia).

## A rigorous small neighborhood, and the precise remaining gap

The bordered Hessian B at a* has smallest-magnitude eigenvalue -0.0536, whose
eigenvector is 90% in the (l,s)-block and only 10% in the a-block. An eigenvalue
perturbation argument (first order uses the projected v^T dB v ~ 29 |a-a*|;
second order uses ||dB||^2 / gap with gap 0.44 to the next eigenvalue) keeps B's
inertia at (3,2,0), hence keeps nabla^2_a S_* negative definite, on an explicit
a-ball of radius ~1e-3. This is a genuine rigorous neighborhood (not just the
point), and can be certified with the machinery here.

It still does not meet Region II. On the weak eigendirection the dual-bound
sweep over-estimates S_* by the discarded H-concavity ~1.35 d^2 while S_* only
decays ~0.29 d^2, so the sweep value is ~ +1.06 d^2 > 0 at every distance until
d is large enough (~0.05) that the higher-order decay of S_* dominates. Thus:
  Region I (bordered perturbation) certifies weak-direction |a-a*| < ~1e-3;
  Region II (dual sweep) certifies weak-direction |a-a*| > ~0.05;
leaving an annulus ~[1e-3, 5e-2] that needs the true Hessian certified over
boxes -- which wraps by the same condition-number mechanism, since the annulus
is still inside the near-singular zone.

## The single lemma that closes the problem

Everything reduces to: prove the 2x2 matrix inequality

    alpha nabla^2_a T(a, s*(a))  <=  [nabla^2 Phi(lambda(a))]^{-1}   (Loewner)

on the explicit annulus, with the fixed-point identities that make it an
EQUALITY-with-margin at a* (Huang's C_1,C_2,C_3 form) extended by explicit
Lipschitz control of both sides in a. Equivalently
1 - tr(P) + det(P) >= 0 and tr(P) <= 2 for P = nabla^2 Phi . nabla^2 G, whose
det(P) = det(nabla^2 Phi) det(nabla^2 G) is a product of two scalars with
manageable variation, and whose trace carries the a<->lambda coupling. This is
a self-contained analytic lemma about explicit Gaussian integrals; it is the
one piece not reducible to the finite machine checks completed in this repo,
and it is left open here rather than asserted.

## A structural seed for the lemma (log-concavity)

log Psi is log-concave (the Gaussian upper tail is log-concave). In the
constraint term T(a,s) = E_z log Psi(V), the argument
    V = -(a2/q) Ht / D - (a1/psi) N / D + s N,  D = sqrt(1 - a2^2/q),
is AFFINE in the rescaled variables (atilde1, atilde2) = (a1/D, a2/D) and in s.
Hence T is CONCAVE in (atilde1, atilde2, s) jointly (an expectation of a concave
function of an affine image). This is almost certainly the source of the
concavity of S_* = H + G at the maximizer. It converts the opaque matrix
inequality into a statement about the nonlinear change of variables a -> a/D:
any failure of concavity in the original a can only come from the curvature of
that substitution, which is explicit and small on the whole annulus (D ~ 0.66,
bounded away from 0). Making this precise -- bounding the Hessian of the
substitution against the concavity margin of T (and combining with H concave)
-- is the concrete route to the closing lemma, and is the recommended next step.

## The log-concavity reduction (closest analytic route; still open by 0.235)

A genuine advance, worth recording precisely. The Gaussian upper tail Psi is
log-concave, and in the constraint term T(a,s) = E_z log Psi(V) the argument V
is AFFINE in the rescaled variables u = (a1/D, a2/D), D = sqrt(1-a2^2/q). Hence
T is concave in (u,s); adding the s-convex term s^2 psi/2 (Sss>0) and
minimizing over s, the saddle fact "min over a convex variable of a function
concave in u is concave in u" gives G-tilde(u) := G(a(u)) CONCAVE in u.
Verified: nabla^2_u G-tilde eigenvalues -4.38, -0.10 (stable). With H concave
(free) this yields the exact split in moment coordinates

    nabla^2_a S_* = [ nabla^2_a H + Ju^T nabla^2_u G-tilde Ju ]  +  C ,

bracket PROVABLY <= 0 (two concave Hessians), C the explicit coordinate
curvature C = sum_k (grad_u G-tilde)_k nabla^2_a u_k with nabla^2_a u closed
form from D(a2). The whole neighborhood reduces to one explicit 2x2 inequality

    C  <=  [nabla^2 Phi]^{-1}    (equivalently nabla^2_a H + C <= 0).

At a*: bracket eig (-226.58, -5.319), margin m=5.319; C pos.def. eig
(1.96, 5.554); [nabla^2 Phi]^{-1} eig (2.729, 221.729). C <= Phi^{-1} is TRUE
with slack 0.58 (= -lambda_max(nabla^2 S_*)), but eigenvalue additivity gives
only -5.319 + 5.554 = +0.235: the misalignment of C's and the bracket's top
eigenvectors. Linear reparametrization u->Mu does NOT help (Ju^T HGt Ju is
M-invariant). Closing needs a sharper-than-additivity bound using the explicit
eigenvectors of C and Phi at a*, with Lipschitz control over the annulus, or a
nonlinear change of variable lowering lambda_max(C) below m. This is the
precise self-contained statement the theorem now rests on: proven-reduced,
honestly not closed.

### Correction to the reduced inequality

The reduced condition is nabla^2_a S_* = bracket + C <= 0, i.e.

    C  <=  -bracket  =  [nabla^2 Phi]^{-1}  +  |Ju^T nabla^2_u G-tilde Ju|

(the second term is positive semidefinite since G-tilde is concave). This is
STRICTLY WEAKER than the "C <= [nabla^2 Phi]^{-1}" written above, which is in
fact false here (lambda_max(nabla^2 Phi . C) = 1.74 > 1). With the extra
positive term |Ju^T nabla^2 G-tilde Ju| the true inequality C <= -bracket holds
with slack 0.58. So the honest reduced statement is: C <= -bracket, an explicit
2x2 Loewner inequality that is true by 0.58 but whose eigenvalue-additivity
relaxation is short by 0.235. This is the corrected, precise open lemma.

## BUG FOUND, and the obstruction dissolves (corrected picture)

A serious correction. The a-coordinate Hessian routine `true_hessian_a` was
WRONG: it reported nabla^2_a G = [-1.08, 2.68, 1.09] at a*, from which the whole
"weak margin 0.58 / gap 0.235" narrative followed. The correct value, verified
THREE ways -- direct central finite differences of G(a); the log-concavity
composition G_{11} = nabla^2_u G-tilde_{11} / D^2 = -1.617/0.4361 = -3.708; and
the new u-coordinate assembly `huang_ucoord.hessG_a` -- is

    nabla^2_a G(a*) = [ -3.708,  3.490 ;  3.490,  0.832 ].

Hence nabla^2_a S_* (a*) = [ -78.35, 106.34 ; 106.34, -148.99 ] with eigenvalues
(-225.7, -1.618): still negative definite (a* is a strict local max, as it must
be), but the WEAK margin is 1.618, not 0.58, and the concavity certificate
lambda_max(nabla^2 Phi . nabla^2_a G) = 0.734 <= 1 has slack 0.266.

More important, the log-concavity route is not just a reduction -- it removes the
1/D wrapping. In u = a/D coordinates the constraint argument V is affine with
z-only coefficients, so nabla^2_u G-tilde carries NO 1/D and is well conditioned
over u-boxes; the only 1/D content is in the explicit closed forms Ju and the
coordinate curvature C, computed directly. The +-150 sensitivity that defeated
every earlier attempt was an ARTIFACT of differentiating T in a-coordinates.

A coverage map over the neighborhood of a* (25x17 grid, in K) shows EVERY point
is covered by either {nabla^2_a S_* <= 0 here} (Region I, concavity, now cheap
to certify via the u-assembly) or {S_* < -1e-4} (Region II, the bulk sweep),
with a nonempty overlap band and ZERO uncovered points. The directions in which
concavity fails (decreasing a1, increasing a2) leave the moment body K almost
immediately, so concavity is never needed there. The obstruction was an artifact
of the bug plus computing in the wrong coordinates; with nabla^2_a G correct and
in u-coordinates, Region I is a finite, well-conditioned box check that meets the
existing Region II sweep. The closure is now a matter of implementing the u-based
concavity certificate over the excluded box and matching it to the sweep.

## Accurate status (correcting "dissolves" above)

Progress is real but I have NOT completed a rigorous end-to-end Region I
certificate. Honest state:

WHAT IS SOLID
- Bug in `true_hessian_a` found and confirmed three ways; correct
  nabla^2_a S_*(a*) has eigenvalues (-225.7, -1.618) (weak margin 1.618).
- u-coordinate identity: in u = a/D the constraint integrand is affine with
  z-only coefficients, so nabla^2_u T-tilde has NO 1/D and is well conditioned.
- lambda-coordinates remove the a->lambda stretch: a thin lambda-box gives a
  thin a-box (mean-value moment map `moment_map_mv`), so nabla^2 Phi and a(lam)
  are tight together.
- Frozen (osS) certificate needs no s-box: alpha nabla^2_u T at fixed s0. At a*
  the frozen indicator lambda_max(Phi.alpha nabla^2_a T)=0.837<1 (= Huang's
  point result), slack 0.163.
- Nonrigorous coverage map over K near a*: {concave} union {S_*<-1e-4} has ZERO
  gaps, with an overlap band -- strong evidence Region I meets Region II.

WHAT REMAINS (the honest gap)
- Converting nabla^2_u back to nabla^2_a reintroduces the coordinate curvature
  C = sum (grad_u G) nabla^2_a u, which carries 1/D^3, 1/D^5. Over an a2-box of
  half-width ~6e-3 this term wraps ~+-0.3-10, exceeding the frozen margin 0.163.
  Fixes (each implementable, none done/verified): mean-value C in a2 (needs the
  3rd/4th a-derivatives of u, closed form); or small lambda-box tiling
  (rl ~ 6e-3, a few hundred boxes) so the wrap falls under the margin.
- The frozen margin is small and its concave region is elongated; the exact
  match to the existing Region II sweep (does eval_cell < 0 hold just outside
  the frozen-concave set in every in-K direction?) is checked nonrigorously
  (0 gaps) but not rigorously assembled.

So: the obstruction is no longer the condition-number wall it appeared to be
(that was partly the bug, partly a-coordinates). It is now a finite, well
conditioned computation with two mechanical pieces left. I am not claiming the
theorem is closed; I am recording exactly what is proven and what is pending.
