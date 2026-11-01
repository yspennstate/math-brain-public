# T384: a nonorthogonal finite-grid boundary theorem for actual simultaneous GD

Status: PROVED (internal), independently audited in reviews/e04_boundary_review.md. This is a boundary-scale theorem, not a macroscopic training limit or a continuous-time boundary-selection theorem. It extends the scalar finite-grid result in run 20261023T224735Z to coupled, reactivating gates. No external priority claim is made.

## Model and statement

Fix 0<alpha<2, integers k<=d, linearly independent inputs x_1,...,x_k in R^d, fixed labels y in R^k, and gamma>0. Write X for the k-by-d matrix with rows x_j, and G=XX^T. Unit norms are not required. All initial W_i and original-coordinate U_iell are independent standard symmetric alpha-stable variables (characteristic function exp(-|t|^alpha)). There are no biases. Set

a=m^(1/alpha), L=(log m)^(1/alpha), b=aL,
v_i=XU_i, h_i=(v_i)_+, D(v)=diag(1{v_j>0}),
f_n=b^(-1) sum_i W_i,n h_i,n, r_n=y-f_n.

Both-layer simultaneous GD for half squared error, with rate multiplier L^2 and physical step h=gamma/L, is exactly

U_i,n+1=U_i,n+(gamma/a) W_i,n X^T D(v_i,n) r_n,
W_i,n+1=W_i,n+(gamma/a) r_n^T h_i,n.                 (1)

Do not absorb a projected gate after a crossing: (1) updates U through every other active input, so a negative projection can become positive again. Its rate-scaled tangent Gram is

H_m,n=C_m,n+a^(-2)sum_i W_i,n^2 D(v_i,n)G D(v_i,n),
C_m,n=a^(-2)sum_i h_i,n h_i,n^T.                   (2)

Define the initial primitives as follows. Put c=Gamma(alpha)sin(pi alpha/2)/pi and p=alpha/2. Let q_ell=X e_ell and q_ell^±=(±q_ell)_+. Independently over signed rays, let Z_ell^± have characteristic function exp(-c|t|^alpha), and S_ell^± have Laplace transform exp(-c Gamma(1-p)s^p). Independently of all these, let N on (R\{0}) x R^d be a Poisson measure of intensity

alpha c |z|^(-1-alpha) dz P_U^(tensor d)(du).

Set

F=sum_(ell,±) q_ell^± Z_ell^±,
C=sum_(ell,±) S_ell^± q_ell^±(q_ell^±)^T,
r=y-F.                                             (3)

For each atom (z,u) of N, define a discrete endpoint orbit, using the same r for all steps,

v_0(z,u)=Xu,
v_(n+1)(z,u)=v_n(z,u)+gamma z G D(v_n(z,u))r.         (4)

For n>=0 let

K_n=C+int z^2 D(v_n)G D(v_n) N(dz,du),
P_n=n gamma C r+int z[(v_n)_+-(Xu)_+] N(dz,du).      (5)

The integrals in (5) are ordinary absolutely convergent Poisson sums, not compensated sums. For every fixed integer N_0, jointly with the initial primitives,

(f_0,C_m,0,N_m,(H_m,n, L[f_n-f_0])_(0<=n<=N_0))
 => (F,C,N,(K_n,P_n)_(0<=n<=N_0)).                  (6)

The point-process coordinate has the usual vague topology away from z=0, with finite original-mark cutoffs as used below.

Consequently, for fixed S<infinity, the held paths indexed by n=floor(s/gamma), 0<=s<=S, converge jointly in the product J1 topology. This assertion is only for a fixed finite boundary horizon s=L t. It does not allow N_0 to grow with m, nor interchange m->infinity and gamma->0 or S->infinity.

## Initial law: orthogonality is unnecessary here

The finite-ray initialization proof of run 20261023T224735Z, agents/d01_k_input_extension.md, applies to every fixed X of full row rank. Its analytic estimates use bounded fixed linear forms, while its nondegeneracy argument uses rank; neither uses G=I. Specifically, with H(u)=(Xu)_+ and Psi(u)=sum_(ell,±)(±u_ell)_+ q_ell^±,

||H(u)-Psi(u)||<=A_X M_2(u),
||H(u)H(u)^T-sum_(ell,±)(±u_ell)_+^2 q_ell^±(q_ell^±)^T||
 <=B_X sum_(ell<j)|u_ell u_j|.

Here M_2 is the second largest absolute coordinate, defined as zero for d=1. Its alpha moment is finite. Conditional stable summation makes the normalized W-weighted first remainder vanish in probability: its conditional scale to the alpha power is at most A_X^alpha/(m log m) times sum_i M_2(U_i)^alpha, with mean O(1/log m). For the Gram remainder, choose alpha/2<q<min(alpha,1); subadditivity and finite stable q moments bound its tail by const m^(1-2q/alpha)->0.

The scalar signed-coordinate product, hidden-square, and marked W-endpoint rare-jump limits are exactly the categories already proved jointly in research/T384_marked_PPP.md and research/T384_orthogonal_initialization.md. Changing X only changes the deterministic ray coefficients. Their independence and small-jump estimates therefore give

(f_0,C_m,0,N_m)=> (F,C,N), N_m=sum_i delta_(W_i,0/a,U_i,0). (7)

This use of the earlier scalar/category proof is a dependency, not a fresh proof of a new stable limit. Since q_ell^+-q_ell^-=q_ell and X has rank k, the rays span R^k. Thus C is positive definite a.s., and F has a bounded continuous density. In particular F is independent of the entire marked N, a fact used below. Positive definiteness is useful context, but no inverse C is needed in (6).

## Deterministic finite-step estimates

Use the original parameter row norm R_i,n=(W_i,n^2+||U_i,n||^2)^(1/2), and S_m,n=a^(-2)sum_i R_i,n^2. The update (1), for a fixed gate pattern at that step, is a symmetric star-matrix update whose increment norm is bounded by

epsilon_n=(gamma/a)||X|| ||r_n||.

Hence R_i,n+1<=(1+epsilon_n)R_i,n and S_m,n+1<=(1+epsilon_n)^2 S_m,n. Both S_m,0 and r_0 are tight. The following bound, which does not assume loss descent, is enough:

L||f_(n+1)-f_n|| <= A_X gamma ||r_n|| S_m,n
                         +B_X gamma^2 a^(-1)||r_n||^2 S_m,n. (8)

Indeed split the exact output increment into W_n(h_(n+1)-h_n) and (W_(n+1)-W_n)h_(n+1), and use ReLU Lipschitzness, ||h_n||<=||X||||U_n||, and 2|W|||U||<=W^2+||U||^2. On any initial event ||r_0||<=R,S_m,0<=B, induction over the fixed N_0 steps gives for all sufficiently large m

max_n ||r_n||<=R+1,
max_n S_m,n<=2B,
max_n ||r_n-r_0||=O_(R,B,N_0,X,gamma)(1/L).           (9)

The row displacement is at most O(1/a)R_i,0 uniformly over these finitely many steps. Consequently

max_n ||C_m,n-C_m,0||=O(1/a)S_m,0,
max_n a^(-2)sum_i |W_i,n^2-W_i,0^2|=O(1/a)S_m,0,   (10)

on the same localized event. In particular both differences vanish in probability. For matched endpoint rows with initial |W_i,0|/a bounded and original U_i,0 bounded, W_i,n/a-W_i,0/a=o(1). Their projected update is exactly

v_i,n+1=v_i,n+gamma (W_i,n/a)G D(v_i,n) r_n.         (11)

No monotone-gate claim has been used in these bounds.

## Discontinuities and retained endpoint orbits

For fixed z,r and a fixed history (D_0,...,D_(n-1)), (4) gives

v_n=Xu+gamma z G sum_(j<n)D_j r.                   (12)

Thus any event (v_n)_ell=0 lies in a finite union of affine hyperplanes in u. Each row of X is nonzero, and the original iid stable vector U has an absolutely continuous law, so each such event has probability zero. This statement holds for every fixed r and z; independence of F and N allows integration over random r=y-F. There are finitely many histories at each n and countably many n, and the marked PPP has only countably many atoms. Hence almost surely no limiting atom lies on any threshold at any fixed integer step.

Restrict to epsilon<|z|<M and ||u||<B, choosing cutoff boundaries of zero intensity. There are finitely many atoms. Joint convergence (7), (9)--(11), and induction using the nonzero threshold margins imply convergence of all retained endpoint orbits through N_0. This includes activation and reactivation. A fixed positive threshold margin is only asserted for this finite retained set and finite number of steps.

## Removing cutoffs and identifying the output increment

At any step, a retained atom's first-layer kernel contribution is bounded by ||G||z^2. Its output displacement obeys

||v_n-v_0||<=n gamma |z| ||G|| ||r||,
||z[(v_n)_+-(v_0)_+]||<=n gamma z^2 ||G|| ||r||.     (13)

The small-|z| square intensity is finite and tends to zero as epsilon^(2-alpha). Large |z| has finite Poisson intensity and its tail probability tends to zero as M->infinity; do not use its generally infinite square expectation. At fixed epsilon, large original marks have vanishing occurrence probability by the product marking law. These observations prove existence of (5) and permit cutoff removal for the limiting sums.

For finite m, the omitted initially small-|W_i,0|/a kernel mass is controlled uniformly in n by

||G|| [a^(-2)sum_(|W_i,0|<=epsilon a) W_i,0^2
          +a^(-2)sum_i |W_i,n^2-W_i,0^2|].          (14)

The first term has limsup expectation O(epsilon^(2-alpha)); the second vanishes by (10). The same bound controls a step's first output term, up to gamma||r_n||||G||. Large endpoint weights and large marks are removed by finite-atom probability bounds, just as above.

More explicitly the exact vector identity is

L(f_(n+1)-f_n)
 =sum_i z_i,n [(v_i,n+1)_+-(v_i,n)_+]
  +(gamma/a^2)sum_i (r_n^T h_i,n)h_i,n+1,           (15)

where z_i,n=W_i,n/a. Its second term equals gamma C_m,n r_n+E_m,n, with

||E_m,n|| <=(gamma^2/a^3)||G||||X||||r_n||^2
                                sum_i |W_i,n| ||U_i,n||
 <= const_(X,gamma) a^(-1)||r_n||^2 S_m,n.          (16)

Thus that term tends to gamma Cr jointly with everything else. The first term converges by retained-atom continuity and (14) to int z[(v_(n+1))_+-(v_n)_+]N. Summation over the finite steps telescopes this endpoint term and gives P_n in (5). Equation (10) and the same endpoint argument applied to (2) give K_n. This proves (6). Each held path uses exactly the same deterministic grid, so the finite-vector convergence implies J1 convergence (indeed uniform convergence under a coupling of grid heights).

## What this pays and what it does not

This proves the coupled, nonorthogonal critical-step *boundary grid* directly from simultaneous GD. It defines that regime without choosing a discontinuous continuous-time ODE. It preserves overshoots and reactivations. Unlike the scalar formula, P_n need not equal a sum of pre-step tangent Gram actions gamma K_j r: the ReLU secant across a step is different from the tangent at its beginning.

Unpaid: n of order L_m at fixed physical time, averaging of rapidly switching gates, continuous-time solution selection at attracting faces, global nonorthogonal random training dynamics, deep networks, and external novelty. Finite-step estimates alone do not pay any of these. The scalar once-per-neuron crossing bound fails under repeated reactivation; see agents/e03_discrete.md for a local mechanism and an exact persistent correction.
