# A selected training law for two positively correlated inputs, all initial residual signs

**Status: internally PROVED, independently reviewed within the stated shallow two-input model. Full catalog T384 remains OPEN. External priority is unverified.** New work in this run is the same-sign entrance, inherited continuation, and one-capture simplification. The two initially mixed sectors use the previously proved run021857 result; they are not new discoveries.

## Model and exact scope

Fix d<infinity, 0<alpha<2, deterministic unit inputs x1,x2 in R^d with rho=x1 dot x2 in (0,1), deterministic labels y in R^2, and gamma>0. There are m hidden neurons, no biases, and iid standard symmetric alpha-stable initial coordinates W_i,U_iell, with characteristic function exp(-|t|^alpha). Put a=m^(1/alpha), L=(log m)^(1/alpha), X=(x1;x2), G=XX^T, v_i=XU_i and

    f=(aL)^(-1) sum_i W_i(v_i)_+,   r=y-f.

At physical grid step h=gamma/L, simultaneous gradient descent on half squared error with rate multiplier L^2 is

    U_i^+=U_i+(gamma/a)W_i X^T D(v_i)r,
    W_i^+=W_i+(gamma/a)r^T(v_i)_+,
    D(v)=diag(1{v1>0},1{v2>0}).

The strict zero derivative is used at a kink; projected gates are not artificially absorbed. For every fixed T<infinity, polygonal outputs converge in law in C([0,T];R^2), jointly with their initial primitive limits, to the selected law below. This is an unconditional theorem over all initial residual signs. It does not claim a pre-step tangent-Gram limit in L1 or J1, a deep-network law, or a simultaneous gamma-to-zero/width limit.

## Joint primitive law and branch definitions

Let c=Gamma(alpha)sin(pi alpha/2)/pi, beta=alpha/2, q_l=X e_l and q_l^sign=(sign q_l)_+. Independently over signed coordinate rays, let Z_l^sign be symmetric with characteristic function exp(-c|t|^alpha), and S_l^sign be positive with Laplace transform exp[-c Gamma(1-beta)lambda^beta]. Independently of all these let N be a Poisson measure on nonzero z and original-coordinate u, with intensity alpha c |z|^(-1-alpha) dz P_U^(tensor d)(du). Define

    F=sum q_l^sign Z_l^sign,
    C=sum S_l^sign q_l^sign(q_l^sign)^T,
    R=y-F.

The prior finite-ray theorem and BOUNDARY_GRID.md prove this joint independent primitive limit. C is positive definite, C12>0 for rho>0, R has a full-dimensional continuous density, and integral z^2 N is finite almost surely. The C12 proof is supplied in agents/i02_matching.md. In particular the two residual axes have probability zero.

**Initially positive residuals.** On R1,R2>0, set

    P_+=integral_{z>0} z^2 1{max((Xu)1,(Xu)2)>0} N(dz,du).

Let Q=C+P_+G and initially r^a(t)=exp(-Qt)R. Follow ONE_CAPTURE.md: if r^a never reaches a residual axis, use r=r^a. Otherwise let b be its first zero coordinate, p the other, and ell_b=(GQ^{-1}R)_b. If ell_b>=0, still use r=r^a on every finite horizon. If ell_b<0, let sigma be the unique positive root of

    [GQ^{-1}(I-exp(-Q sigma))R]_b=0.

Use Q up to sigma, then the constant matrix Q_s=C+P_+(1-rho^2)e_p e_p^T forever. There is at most one permanent endpoint-face capture. The residual-axis crossing precedes capture and is not itself a matrix switch.

Equivalently, after identifying b, put I(t)=integral_0^t r and S(w)=w-min(0,min_{s<=t}w(s)); the global reflected endpoint is

    V_b=S(I_b+rho I_p),
    V_p=rho V_b+(1-rho^2)I_p,
    r=R-CI-P_+V.

This formula retains the nonzero endpoint accumulated before the residual changes sign. Each selected atom has endpoint zV; all other atoms are exactly dead after a finite original-mark boundary history and have zero limiting endpoint.

**Initially negative residuals.** On R1,R2<0, set

    P_-=integral_{z<0} z^2 1{max((Xu)1,(Xu)2)>0} N(dz,du).

Apply the preceding positive-residual construction to R_tilde=-R, C and P_-, obtaining r_tilde, and put r=-r_tilde. Indeed, with I_tilde=integral r_tilde, a selected negative-z endpoint equals |z|V_tilde, so its signed output is -z^2 V_tilde. The macro residual identity becomes -r_tilde=-R_tilde+C I_tilde+P_-V_tilde, exactly the negative of the positive construction. At finite width the symmetry (W,y,r)->(-W,-y,-r), U unchanged, preserves the simultaneous update and the symmetric initialization law. Thus the entrance, matching, no-exit handling and convergence proof transfer without changing normalization or imposing new gate absorption.

**Initially mixed residuals.** On R1<0<R2, use the already proved finite original-mark classifier of run021857 ALL_MIXED_ENTRANCE.md. Let P2 be the total z^2 of positive-z survivors and P1 that of negative-z survivors. Each is selected by the actual frozen grid v^+=v+gamma z G D(v)R from v0=Xu; they may depend on R and gamma. Set

    I=integral r,
    u=S(I1+rho I2),        v=rho u+(1-rho^2)I2,
    u_-=S(-I2-rho I1),    v_-=rho u_--(1-rho^2)I1,
    r=R-CI-P2(u,v)+P1(v_-,u_-).

The prior ALL_MIXED_LIMIT.md proves unique full-horizon selection of this equation from actual GD. For R2<0<R1, apply the coordinate permutation J=[[0,1],[1,0]] to X,y,F,R,C and projected endpoints, use that theorem, then undo J. This is an exact relabeling: JGJ^T=G and X^T r is unchanged after jointly permuting X and r. It proves the opposite orientation with its original marks intact.

## Why the four branches give full convergence

agents/i01_entrance.md proves the same-sign frozen classifier with finite strict certificates. agents/i02_matching.md transfers it via fixed finite cutoffs and random-certificate-index localization; it identifies every macro subsequence with Q until its own first residual-axis hit. The action of every unselected macro subsequence has off-diagonal at least C12>0, forcing a strict crossing and subsequent mixed-sign invariance before assuming any selected continuation. Each selected atom arrives with q(tau)=zGI(tau)>0 and tangential margin q_p-rho q_b=z(1-rho^2)I_p(tau)>0. The negative-part chain rule and increasing tangential margin rule out support loss. Monotone relay uniqueness then identifies its inherited reflected path. The previous uniform small-square-mass estimate permits summation and cutoff removal; reflection is 2-Lipschitz, so Picard/Gronwall gives pathwise uniqueness. The zero coefficient at the residual-axis time is harmless: the monotone lemma holds for a<=0, and the running-minimum construction divides by a only where it is strictly negative. ONE_CAPTURE.md gives the additional explicit two-matrix form.

The positive quadrant, negative quadrant, and the two mixed quadrants partition the limiting initial residual space up to a null set. Their finite-width indicators converge jointly with the initial primitives. Conditional convergence on each of the four continuity events, multiplied by the converging event probabilities and added, proves unconditional joint convergence. No assertion about continuity of a global hitting-time map is needed, and no exceptional no-finite-exit branch is silently discarded.

The loss bound inherited from the macro theorem remains

    ||r(t)|| <= exp[-lambda_min(C)t] ||R||.

The same-sign conditional laws are independent of the fixed gamma. This assertion is not extended to the full all-sign law: general mixed selectors may depend on gamma, and a selector difference alone does not establish a marginal path-law difference. Existing negative-correlation results are separate.

## Selected mass and original-coordinate geometry

P_+ and P_- are iid positive beta-stable variables, independent of F,C, with transform exp[-pi_X c Gamma(1-beta)lambda^beta], where pi_X=Pr(max((XU)1,(XU)2)>0). For original-coordinate iid stable initialization this probability generally depends on X beyond G. agents/i01_entrance.md derives a conditional Gaussian-mixture formula and a rigorous alpha=1 same-Gram counterexample; its decimals are supplementary quadrature, not the proof. Thus a Gram-only formula for the *selected mass distribution* is false in general. This does not by itself prove distinct unconditional output laws for arbitrary rotated input pairs.

## Proof dependencies and remaining problem

All dependencies are in the same private continuation root:

- runs/20261023T232238Z/BOUNDARY_GRID.md and MACRO_COMPACTNESS.md: exact model, joint primitives, finite grid, full-horizon compactness, endpoint inclusion and uniform small-mass control.
- runs/20261024T012528Z/agents/g02_audit.md: monotone relay for a<=0, reflection, stability and countable-phase uniqueness.
- runs/20261024T021857Z/ALL_MIXED_ENTRANCE.md and ALL_MIXED_LIMIT.md: the previously selected initially mixed law.
- This run's agents/i01_entrance.md, agents/i02_matching.md, ONE_CAPTURE.md and independent reviews: new same-sign proof and its assembly.

No native claim IDs or external novelty are asserted. Full T384 still asks about broader input geometries, deep training and feature learning. Remaining negative-correlation initial regimes, more than two nonorthogonal inputs, deep layers, test predictions, rates and varying critical step scales remain open here.
