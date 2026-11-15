# A compensated fourth observable with favorable cubic sign

Claim T067-COMPENSATED-CUBIC-001, version 1. Status: proof (unaudited).
This is an auxiliary replacement lemma; no improved degree cutoff or canonical
fourth-moment ceiling is claimed. No novelty or priority assertion.

For p in the three-state simplex put a=3p-1, A=sum_i a_i^2, J=sum_i a_i^3,
and Phi(p)=A^2+(49/4)A. For logit softmax derivatives D_i, define

  ell_i^Phi=[sum_r D_r^3 Phi-D_i Phi-(D_j-D_k)^2 Phi]/4,
  S_Phi(p)=sum_i p_i ell_i^Phi(p), {i,j,k}={1,2,3}.

Then S_Phi(p)<=0 throughout the simplex, strictly when 0<A<6. Thus for any
symmetric calibrated auxiliary Bayesian experiment W and any symmetric
three-state branch input with T=E sum_i(3p_i-1)^3>=0, the retained third-order
term in its Gaussian replacement for Phi has nonpositive expectation.
The fourth-order remainder and any resulting U<=K M^2 estimate are open here.

1. Exact operator identities.

Logit differentiation on a polynomial f(p) is
D_i f=sum_j p_j(delta_ij-p_i) partial_j f. The conditional-root mean,
second and third raw-moment calculation in PIECEWISE-D0 v1 Part A.1 gives
lambda^3 T ell_i^f. In that calculation D_vi=D_i/2 since functions of softmax
are invariant under common logit translation, and vi=(e_i-u)/2. Conditional
auxiliary posteriors have density 3p_i, so permutation symmetry converts the
averaged coefficient to T E_nu S_f. These statements use independence of W
and the replaced branch conditional on the root.

For Q=A^2 the direct polynomial derivation in radial_fourth_cubic_sign.py gives

  S_A=-9e2(e2-9e3),
  S_Q=54(18e2^3-270e2^2 e3-5e2^2+99e2 e3-6e3),

where e2=sum_(i<j)p_i p_j and e3=p1p2p3. Substitution of
e2=(6-A)/18 and e3=(J+3-3A/2)/81 yields

  S_A=-(6-A)(A-J)/18,
  S_Q=4A-4A^2+(2/3)A^3+J(-2+3A-5A^2/9).               (1)

The exact script compensated_cubic_certificate.py checks this substitution
and each factorization below; it does not infer sign from a sampled grid.
By linearity, with beta=49/4,

  S_Phi=C(A)+B(A)J,
  C(A)=(4-beta/3)A+(-4+beta/18)A^2+(2/3)A^3,
  B(A)=beta/3-2+(3-beta/18)A-5A^2/9.                    (2)

2. Feasible moment geometry.

The simplex gives 0<=A<=6. Since sum_i a_i=0, its discriminant identity is
A^3/6-J^2=product_(i<j)(a_i-a_j)^2/3>=0. Therefore J<=A^(3/2)/sqrt(6).
Also e3>=0 and its displayed expression give J>=3A/2-3. These bounds are
pointwise, so no distributional or canonical fixed-point restriction is used.

3. Two cases prove the sign on the whole simplex.

If B(A)>=0, set t=sqrt(A/6) in [0,1], and use J<=6t^3. Substituting the
upper bound into (2), exact expansion and completing the square give

  S_Phi <= -2t^2(1-t)^2
              [48(t-23/384)^2+239/3072+60t^3] <=0.       (3)

For verification before completing the square, the bracket with the opposite
sign is -1/4+(23/4)t-48t^2-60t^3. The positive constant 239/3072 proves strict
negativity whenever 0<t<1.

If B(A)<0, use instead J>=3A/2-3. Multiplication reverses that inequality,
and substitution in (2) factors exactly as

  S_Phi <= -(6-A)^2(24A+25)/144 <=0.                    (4)

This is strict for A<6. At A=0 the posterior is uniform, and at A=6 it is a
pure state; the polynomial coefficient vanishes there. Equations (3),(4)
cover all possible signs of B and all simplex points, proving the claim.

4. Replacement interpretation and scope.

Since lambda^3 T>=0, multiplying the pointwise coefficient bound and taking
the calibrated auxiliary expectation proves the stated favorable cubic sign.
Boundary posteriors are included by polynomial continuity. Logit derivatives
of Phi are polynomials in p, so they are bounded; this also permits the usual
integrable Taylor treatment when W includes Gaussian branches. This proof
does not bound the fourth Taylor remainder or derive a finite-degree theorem.

The unmodified Q has a positive coefficient at (2/5,3/10,3/10), as recorded in
FOURTH-CUBIC-OBSTRUCTION v1. The present added term corrects that sign globally;
it does not validate discarding the cubic for Q itself.

NEXT: Measure the Gaussian Phi gap and explicit derivative/remainder constants
before investing in a full comparison; compare its prospective degree floor
with the proposed d>=156 result. Keep all cutoff claims at their audit status.
