# C0044 independent adversary derivation

2026-10-10. Phase I recorded before reading w576's proof. Exact primary-source assumptions and current openness still require verification. The full target is not claimed solved.

## I. An explicit obstruction to a stationarity argument

Let d >= 3, E = {+/-e_i: 1 <= i <= d}, and let (sigma_x) be independent uniform signs. Put a=1/(2d) and delta=1/(4d). Define

    omega(x,+e_1) = a + delta sigma_x,
    omega(x,-e_1) = a - delta sigma_x,
    omega(x,e) = a for all other e in E.

These probability vectors are iid, their entries sum to one, and every entry is at least 1/(4d). Set (theta_z omega)(x,e)=omega(x+z,e), and Kf(omega)=sum_e omega(0,e) f(theta_e omega).

For f(omega)=sigma_{-e_1}, E_P f=0. The +e_1 summand of Kf is (a+delta sigma_0)sigma_0, with mean delta. Each remaining summand has mean zero: its sign is at e-e_1 != 0, independent of sigma_0, and has mean zero. Thus E_P Kf=delta > 0. The iid spatial law P is not K-invariant. This is a proof-step counterexample, not a counterexample to directional zero-one.

## II. Exact energy defect for a quenched harmonic function

For any spatially stationary law P, define c(omega)=sum_e omega(-e,e). If a bounded real h satisfies Kh=h, then expansion of the square and a change of spatial variables give

    E_P sum_e omega(0,e)[h(theta_e omega)-h(omega)]^2
      = E_P[(c(omega)-1)h(omega)^2].

Indeed, the first square term transforms to E_P[c h^2]; the cross term is -2 E_P[h Kh]=-2 E_P[h^2]; the last term is E_P[h^2]. Spatial stationarity gives E_P c=1, but does not make the right side vanish. h can depend on the incoming probabilities in c. Independence of environment rows does not imply independence of c and the quenched tail probability.

## III. A sufficient input, still not established for the target

If there were a probability measure Q equivalent to P and invariant under K, then any bounded K-harmonic h would be spatially constant P-almost surely: integrate the square identity under Q to get zero; ellipticity makes every neighbour difference vanish; equivalence transfers this to P; countable translates and P's ergodicity make h deterministic. For h(omega)=P_0^omega(X_n.l -> +infinity), the quenched Markov property makes h(theta_{X_n} omega) a bounded conditional-probability martingale converging to the tail-event indicator. A deterministic h must therefore be 0 or 1.

This is a conditional reduction. Existence of such Q for arbitrary iid elliptic environments is not proved here. Treating P as Q would be false by section I. No multiplication of conditional estimates or claim of a new general zero-one theorem is used.

## IV. Paired-proof audit and its single open input

After the independent phase was frozen as INDEPENDENT_PHASE1.md, I read w576's ATTEMPT.md. Its L1-L6 are conditional reductions, and its text explicitly does not claim the parent theorem. The Q-invariance argument in L2 matches the separately derived section III. The incoming-mass adjoint formula, absolute-continuity-to-equivalence argument, Cesaro uniform-integrability criterion, and energy telescoping are coherent under their stated assumptions.

The essential missing input is G1: positive P-law energy for the actual directional harmonic function must survive the incoming-mass Cesaro averages. The bound integral H_N D_l <= 1/(4N) alone cannot imply integral D_l=0. No iid independence between incoming mass and the quenched harmonic function was established. The strict-elliptic Dirichlet example in the paired proof rules out blanket uniform integrability, subject to checking the exact Sabot theorem; it does not rule out the uniformly elliptic subtarget or C0044 itself.

## V. Concrete counterexample to the generic energy inference

This is an abstract countable-state Markov example, not an iid spatial environment and not a counterexample to C0044. On Z, let the probability of a +1 step be 3/4 at x>0, 1/4 at x<0, and 1/2 at x=0. Every allowed transition is at least 1/4. Write this kernel as T.

The probability h(x) of escape to +infinity is

    h(0)=1/2,
    h(x)=1-(1/2)3^(-x) for x>0,
    h(x)=(1/2)3^x for x<0.

For x>0 the chance to hit zero is 3^(-x); on avoiding zero the biased walk goes to +infinity. A departure from zero returns with probability 1/3, so only finitely many returns occur almost surely. Symmetry gives h(0)=1/2. These facts also establish escape to one of the two ends almost surely. Direct substitution verifies Th=h.

Set D(x)=sum_y T(x,y)[h(y)-h(x)]^2. Then

    D(0)=1/9; D(x)=3^(-2|x|-1) for x!=0.

Take the full-support initial probability pi(0)=1/2 and pi(+k)=pi(-k)=2^(-k-2), k>=1. Let nu_n=pi T^n, f_n=dnu_n/dpi and H_N=(1/N)sum_{n<N} f_n. These densities exist because pi has full support; f_0=1 and integral H_N dpi=1. Exact geometric sums give

    integral D dpi = 10/153 > 0,
    integral h(1-h) dpi = 57/340.

The conditional-probability martingale h(X_n) converges to the escape indicator. Telescoping its square yields

    sum_{n>=0} integral f_n D dpi = 57/340,
    integral H_N D dpi <= 57/(340N) -> 0.

Thus even ellipticity, a genuine escape harmonic function, mass-one incoming densities, and the exact martingale-energy identity permit complete loss of the original-law energy. An additional non-starvation premise is needed. The example omits iid spatial stationarity, so a proof exploiting the full iid hypothesis is still possible; no such proof is supplied here.

## VI. A repair that collapses the iid class

If iid transition rows satisfy c(omega)=sum_e omega(-e,e)=1 almost surely, the incoming variables are independent because their sites -e are distinct. They are bounded, so

    0=Var(c)=sum_e Var(omega(0,e)).

Every coordinate of the transition row is therefore deterministic. Imposing pointwise incoming balance repairs the P-invariance step but restricts iid row environments to homogeneous ones. This is not a proof of general C0044.

## VII. Correct the historical martingale explanation

The exact C0044-A001 intake attempt says the natural martingale argument fails because the quenched escape probability is not finite-region measurable; A002 carries forward the finite-region caveat. The quenched martingale itself is valid: for fixed omega and the path filtration F_n,

    P_0^omega(A_l | F_n)=P_{X_n}^omega(A_l)=h(theta_{X_n}omega).

Finite-region measurability is unnecessary for this identity. What is missing is a valid argument making h spatially constant or proving its incoming-mass covariance vanishes. Finite-row iid independence cannot be applied to the entire-environment function h merely because each environment row is iid.

NEXT: Obtain w578's independent check of the explicit examples and the conditional audit; G1 remains the full-target open input in this packet.
