# C0017: two Cardy martingales and the missing square-lattice estimate

Worker w408, 2026-10-10. Status: proved conditional identification lemma; model-specific input UNPROVED; independent mathematical review pending. No solution or novelty claim.

## Target and scope

The working interface target is in STATEMENT_FOR_ADVERSARY.md. Square-lattice bond percolation at p=1/2, with Dobrushin exploration boundary conditions, should converge to chordal SLE_6. A theorem identifying a hypothetical subsequential driver does not by itself establish convergence of discrete curves, or a full CLE/percolation configuration limit.

## Lemma L1: identify the driver without assuming a semimartingale

Use chordal half-plane capacity normalization dg_t(z)=2/(g_t(z)-W_t) dt. Let W be a continuous adapted real process with W_0=0 on a filtration satisfying the usual conditions. Let 0<a<b<c be three fixed real boundary marks. Up to a stopping time tau, set

X_t=g_t(a)-W_t, Y_1,t=g_t(b)-W_t, Y_2,t=g_t(c)-W_t.

Assume all real Loewner solutions exist and, for some deterministic eta,L>0,

eta <= X, Y_1-X >= eta, Y_2-Y_1 >= eta, Y_2 <= L

on the stopped interval. Localizing strictly before exit from these inequalities suffices. Define the normalized Cardy function

C(u) = [integral_0^u v^(-2/3)(1-v)^(-2/3) dv] / B(1/3,1/3), 0<u<1.

Assume BOTH processes M_i(t)=C(X_t/Y_i,t), i=1,2, stopped at tau, are local martingales in the SAME filtration. They are bounded, so after localization they are true martingales. Then W is a continuous semimartingale up to tau, its finite variation part vanishes, and its continuous local martingale part has bracket 6(t wedge tau). With such pairs on a countable family covering every finite time, W/sqrt(6) is Brownian motion in that filtration.

### Proof: first recover the semimartingale property

Write A_t=g_t(a), B_t=g_t(b). These are continuous adapted finite variation processes on each localization, since dA=2/X dt and dB=2/Y_1 dt. The derivative C' is positive. Its inverse is C^2 on compact subsets of (0,1). Therefore U_t=C^(-1)(M_1(t)) is a continuous semimartingale by Ito's formula. Algebraically

W_t = (A_t-U_t B_t)/(1-U_t).

The denominator stays positive on the localization. The smooth semimartingale calculus applied to this formula makes W a continuous semimartingale. This argument uses no Brownian or diffusion assumption about W.

Let W=V+N with V continuous finite variation, V_0=0, and N a continuous local martingale, N_0=0. Put Q=<N>. Q may initially have a singular part with respect to dt; no absolute continuity assumption is made.

### Proof: compute the exact signed-measure identities

For f(x,y)=C(x/y), u=x/y, D=partial_x+partial_y and Aop=(2/x)partial_x+(2/y)partial_y,

C''(u)/C'(u) = 2(2u-1)/(3u(1-u)),

Df = C'(u)(1-u)/y > 0,

D^2 f = -(2/3) C'(u)(1-u^2)/(u y^2),

Aop f = 2 C'(u)(1-u^2)/(u y^2) = -3 D^2 f.

Ito's formula, with dX=2/X dt-dV-dN and dY_i=2/Y_i dt-dV-dN, gives the finite variation part

0 = -(Df_i) dV + (1/2)(D^2 f_i)(dQ-6dt).

The zero is justified by uniqueness of the continuous local martingale/finite variation decomposition, since each f_i is a local martingale. Divide by Df_i and use

(D^2 f_i)/(2Df_i) = -(1/3)(1/X+1/Y_i).

Thus the following equalities hold as signed measures, not just as formal density equations:

dV = -(1/3)(1/X+1/Y_1)(dQ-6dt),
dV = -(1/3)(1/X+1/Y_2)(dQ-6dt).

Their difference is

(1/Y_1-1/Y_2)(dQ-6dt)=0.

The positive coefficient is bounded below by eta/L^2 on each localization. Hence dQ=6dt and dV=0 there. Exhaust the localization to obtain the stopped conclusion.

For the global conclusion, require the martingale assumption for every triple (n,2n,3n), n a positive integer, on its nondegenerate localizations. Use the predetermined exit stops tau_n and their increasing tail-infimum sigma_n in GLOBAL_EXHAUSTION.md. That file proves tau_n -> infinity from positive-denominator ODE and separation estimates, so sigma_n increases to infinity almost surely. Local L1 and optional stopping give W stopped at sigma_n a martingale of bracket 6(t wedge sigma_n). Thus W is globally a continuous local martingale with bracket 6t, and Levy's characterization identifies W/sqrt(6) as Brownian motion. This explicit covering hypothesis/construction must not be dropped. w410 kept local L1 and requested this global FIX; w413 review of the new construction is pending.

## Lemma L2: stability when actual drift measures are controlled

Under the same localization, suppose f_i(X,Y_i) is instead a continuous semimartingale with predictable finite variation residual R_i. Write D_i=Df_i, s_i=1/X+1/Y_i and lambda=inf(s_1-s_2)>0. The preceding calculation yields

dQ-6dt = 3[(dR_2/D_2)-(dR_1/D_1)]/(s_1-s_2),

dV = [s_2(dR_1/D_1)-s_1(dR_2/D_2)]/(s_1-s_2).

If D_i>=d_min>0 and s_i<=s_max, then

||Q-6dt||_TV <= 3(||R_1||_TV+||R_2||_TV)/(lambda d_min),

||dV||_TV <= s_max(||R_1||_TV+||R_2||_TV)/(lambda d_min).

Here the first norm denotes the total variation of the signed measure dQ-6dt. This is a conditional deterministic consequence of the identities, and does not supply a lattice estimate for R_i.

## The single hardest missing input: stopped Cardy martingale approximation

For every fixed mark triple and every nondegenerate localization, construct the correctly oriented bounded Doob crossing/exit martingales P_delta,i for the square-lattice exploration, and prove

E[sup_{t<=T wedge tau_delta} |P_delta,i(t)-C(X_delta,t/Y_delta,i,t)|] -> 0,

along with joint convergence of the stopped driving and marked-point processes and compatibility of the limiting filtration. A complementary crossing event uses 1-C instead and gives exactly the same identification. The exact discrete event/boundary convention must be fixed in the model-specific construction; an arbitrary quad event is not automatically the needed martingale in a slit domain.

This input is UNPROVED here. It contains the square-lattice conformal observable estimate. It is not derived from rotational invariance, RSW, self-duality, or the independence of the unexplored bonds. Those facts support other steps but do not give this Cardy limit.

An explicit candidate removes the unspecified-event placeholder. Choose a conformal chart taking the exploration endpoints to 0,infinity, and choose three marks x<y_1<y_2 on the positive boundary arc. On the discrete marked boundary, fix the convention that an endpoint is assigned to the interval on its right. Let E_delta,i be the event that the exploration's first contact with the boundary subarc from x_delta to the target endpoint b_delta lies on the subarc from y_delta,i to b_delta. For the exploration edge filtration F_delta,j define P_delta,i(j)=E[1_{E_delta,i}|F_delta,j]. These are exact bounded Doob martingales without an independence assumption. The Cardy hitting-tail candidate is C(X_delta,j/Y_delta,i,j). Its correct lattice limit and the boundary-event dictionary are precisely what the proposed estimate must prove; neither is treated as an already checked theorem.

The discrete formulation is E[max_j |P_delta,i(j)-C(X_delta,j/Y_delta,i,j)|] -> 0 over steps before the nondegenerate marked-point exit and before a fixed capacity T. To invoke L3, use a valid stopping-time embedding of these discrete martingales in capacity time, with vanishing capacity overshoot and joint continuous limits; arbitrary linear interpolation is not an exact martingale. This is an explicit prerequisite of the conditional route, not an omitted proof step.

## Lemma L3: bounded martingale transfer (conditional compactness step)

Let (W_delta,P_delta,1,P_delta,2) converge jointly in the uniform path topology on a fixed stopped interval to continuous (W,P_1,P_2). Suppose P_delta,i are bounded by 1 in absolute value and are martingales in filtrations to which W_delta is adapted. Then P_i is a martingale in the natural filtration generated by (W,P_1,P_2). Indeed, for s<t and bounded continuous cylinder functions Phi of all these paths at times <=s,

E[(P_delta,i(t)-P_delta,i(s)) Phi_delta]=0.

Joint convergence and boundedness pass this equality to the limit. A monotone-class argument extends it from cylinder functions to all bounded functions of the past. If, in addition, the displayed Cardy approximation holds and the cross-ratio processes converge on this interval, P_i=C(X/Y_i). Since this is a measurable adapted functional of W, the martingale property then holds in W's natural filtration. The theorem L1 applies after the usual augmentation. Stopping-time convergence, existence of the Loewner limit and curve-to-driver compatibility are prerequisites here, not conclusions of this elementary transfer argument.

## Attempt at the missing input and where it stops

Start with P_delta,i=E[1_{E_delta,i}|F_delta,t]. Exact domain Markov gives a genuine bounded martingale. Compare it with the conformally computed Cardy function of the current marked slit domain. Set e_delta,i=P_delta,i-C(X_delta/Y_delta,i). No exact discrete identity proving e_delta,i -> 0 has been obtained.

One tempting route treats rotations as giving cancellation of the predictable Cardy defect at successive exploration steps. The established macroscopic rotation result does not itself identify conditional slit-domain crossing probabilities. Even an unconditional reflection-symmetric driver can have nonzero predictable drift: W_t=Zt with a fair sign Z has symmetric marginals and mean zero, but for s>0 its past determines Z and E[W_t-W_s|F_s]=Z(t-s). No independence or martingale factorization can replace this conditioning.

A second tempting route sums uniformly small observable errors over all exploration steps. That step is invalid without a summability estimate or a bounded-martingale limit argument. At times k/n^2, the deterministic error e_n(k)=(-1)^k/n has sup norm 1/n but total variation 2n over k=0,...,n^2. Thus small uniform error does not provide the residual-measure estimate of L2. L3 is the valid route from a true bounded martingale and a uniform approximation; L2 requires actual drift control.

These are counterexamples to proposed implications, not counterexamples to critical percolation's conformal invariance. The attempt proves the identification reduction and exposes the required model-specific estimate. It does not solve C0017.

## Sources and prior work

Primary status check: Wang Zhou, arXiv:2409.03235v6 (2024-12-17), claims the target. No full proof audit was performed. Ioan Manolescu, arXiv:2502.08394v1, Conjecture 5.1 and Theorem 5.2 discussion, treats the conformal scaling limit separately from rotational invariance. Antti Kemppainen and Stanislav Smirnov, arXiv:1212.6215, supply a framework connecting conditional annulus crossing estimates, curve tightness and Loewner descriptions; application to this exact approximation remains a cited prerequisite.

The completed targeted digest and source limits are in PRIOR_ATTEMPTS.md and SOURCE_STATUS.json. Definition 3 of Duminil-Copin's arXiv:1208.3787, PDF page 7, fixes the standard q=1 positive spin as 1/3. Zhou's Theorem 2, PDF page 6, has the technical boundary Condition C; its proof has not been audited here. Own arguments L1-L3 are elementary derivations in this packet, not claims that these ideas are new in the SLE literature. COUNTEREXAMPLES.md adds L4, an explicit wrong-kappa diffusion passing one Cardy test, and the two elementary failed-implication examples.
