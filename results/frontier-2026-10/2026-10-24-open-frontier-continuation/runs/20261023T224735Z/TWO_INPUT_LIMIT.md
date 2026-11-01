# Full two-input rotated training limit

**PROVED (internal), independently reviewed in reviews/d04_compactness.md.** This extends the prior run's positive-probability nonfreezing result to a complete macroscopic training law for the stated two inputs. It does not close the general deep-network catalog question T384.

## Statement and limiting law

Fix 0<alpha<2, any deterministic y in R^2, and x1=(1,1)/sqrt(2), x2=(1,-1)/sqrt(2). Initialize all output weights W_i and original hidden coordinates U_i1,U_i2 independently with characteristic function exp(-|t|^alpha). There are no biases. Use f_m=(m log m)^(-1/alpha) sum_i W_i[(U_i dot x1)_+,(U_i dot x2)_+] and both-layer gradient flow of half squared error with multiplier (log m)^(2/alpha). Select the absorbing ReLU solution: a projected hidden coordinate reaching zero stays zero. This convention is consistent with the orthogonal projected flow equations; no extension to nonorthogonal inputs is implicit.

Let c=Gamma(alpha)sin(pi alpha/2)/pi and b=alpha/2. The joint initialization from the previous run is

F=(Z0+Z1,Z0+Z2)/sqrt(2),

C=(1/2)[[S0+S1,S0],[S0,S0+S2]],

where the Z variables are independent symmetric alpha-stables with characteristic exponent c|t|^alpha, the S variables are independent positive b-stables with Laplace exponent c Gamma(1-b)s^b, and these six variables are independent of N. Here N is the marked Poisson process of output-weight endpoints (z,u1,u2), with intensity alpha c |z|^(-1-alpha) dz P_U(du1)P_U(du2) on both signed half-axes. Put v1=(u1+u2)/sqrt(2), v2=(u1-u2)/sqrt(2), r0=y-F, sigma_j=sign(r0_j), and

P_j=integral z^2 1{v_j>0, sigma_j z>0} N(dz,du).

Almost surely r0 has no zero coordinate, C is positive definite with C12>0, and P1,P2>0. Define Q0=C+diag(P1,P2).

If r0 has opposite signs, set tau=infinity and r(t)=exp(-Q0 t)r0. If its signs agree, write r0=sigma(u,v), with u,v>0, and Q0=[[a,c0],[c0,d]]. There are three alternatives:

- If v/u>d/c0, coordinate 1 switches.
- If v/u<c0/a, coordinate 2 switches.
- Otherwise there is no switch, including equality at either threshold.

The thresholds are strictly ordered since ad>c0^2, so at most one coordinate is selected. In a switching case, tau is the unique positive zero of [Q0^(-1)(I-exp(-Q0 t))r0]_j, and Q1=Q0-P_j e_j e_j^T. Set

r(t)=exp(-Q0 t)r0 for t<=tau,

r(t)=exp(-Q1(t-tau))exp(-Q0 tau)r0 for t>=tau.

The effective kernel is Q(t)=Q0 before tau and Q1 after tau; its value at the single switching time is immaterial below. In the no-switch case Q(t)=Q0 for all t.

**Theorem.** For every finite T, jointly with the initialization variables,

(f_m,H_m) converges in distribution to (y-r,Q)

in C([0,T];R^2) times L1([0,T];R^(2x2)), where H_m is the learning-rate-scaled tangent kernel. The initial kernel may have additional opposing-sign mass; the L1 topology discards neither a positive-length interval nor its training effect, but a vanishing initial layer has vanishing integral. At a later switch the kernel loses P_j>0. A full J1 kernel limit is not asserted. The limit r tends exponentially to zero because both Q0 and Q1 are bounded below by the positive-definite matrix C.

## Finite-width estimates

Write a_m=m^(1/alpha), L_m=(log m)^(1/alpha), beta_m=L_m/a_m, V_ij=U_i dot xj, and r_m=y-f_m. The exact equations are

V_ij'=beta_m W_i r_m,j 1{V_ij>0},

W_i'=beta_m sum_j r_m,j(V_ij)_+,

r_m'=-H_m r_m, H_m=C_m(t)+diag(A_1,m(t),A_2,m(t)),

C_m(t)=a_m^(-2)sum_i V_i(t)_+ V_i(t)_+^T,

A_j,m(t)=a_m^(-2)sum_i W_i(t)^2 1{V_ij(t)>0}.

On {|r_m(0)|<=R,S_m<=K}, with S_m=a_m^(-2)sum_i[W_i(0)^2+|V_i(0)|^2], residual contraction and G_i=W_i^2+|V_i|^2 give |G_i'|<=2 beta_m R G_i and hence G_i(t)<=exp(2 beta_m RT)G_i(0). Integration yields coordinate movement at most O_{R,T}(beta_m)sqrt(G_i(0)). Therefore C_m(t)-C_m(0) and the normalized total absolute W-square drift are uniformly O_{K,R,T}(beta_m), while |H_m(t)|<=2K eventually.

Define B_j,m(t)=a_m^(-2)sum_i W_i(0)^2 1{V_ij(t)>0}. Each B_j,m is nonincreasing and nonnegative by absorption, and sup_t|A_j,m-B_j,m| tends to zero on the localized event. Until the first hit of gate ij,

V_ij(t)=V_ij(0)+L_m[W_i(0)/a_m]J_j,m(t)+e_ij,m(t),

J_j,m(t)=integral_0^t r_m,j(s)ds,

sup_{i,j,t<=T}|e_ij,m(t)|<=O_{K,R,T}(L_m^2/a_m) -> 0.

The last estimate is unscaled: integrate the W-coordinate movement against beta_m r, use max_i sqrt(G_i(0))<=a_m sqrt(K), and beta_m^2 a_m=L_m^2/a_m. This vanishing unscaled error is important when proving survival of a gate with a fixed positive initial mark.

## Compactness and sign geometry

Initialization and S_m are tight. On the localized events r_m has uniformly bounded derivative and B_j,m belongs to a bounded set of monotone functions, compact in L1. Thus the joint tuple of initialization, S_m, marked endpoints, r_m and B_m is tight in the product of the initialization spaces, continuous-path space and L1. Extract a subsequence and use a joint representation on which r_m converges uniformly, B_m converges in L1, and finite truncated marked configurations converge. Uniform drift bounds imply that the limit solves

r(t)=r0-integral_0^t [C+diag(B(s))]r(s)ds.

This passage uses only boundedness, L1 convergence of B and uniform convergence of r. The coefficients B_j are bounded, nonnegative and nonincreasing; C12>0. The fundamental matrix of this bounded linear equation is invertible at finite times, so r never becomes the zero vector if r0 is nonzero.

For any such measurable coefficients, the strictly mixed-sign residual quadrants are invariant: replacing (r1,r2) by (r1,-r2), or its negative, produces a cooperative linear system with positive off-diagonal entries. From initially equal signs, until the first zero both components have their initial sign. If one reaches zero, the other is nonzero with its initial sign, and the derivative at the zero is -C12 times that other component. The crossing is strict. Thereafter the mixed-sign quadrant is invariant. This reasoning is valid across coefficient jumps because the diagonal coefficient multiplies a coordinate tending to zero; integrating over a small interval gives the same strictly directed crossing.

Consequently at most one residual component changes sign. Its signed cumulative integral first increases and then strictly decreases. Any later return of that integral to zero is unique and transverse. The other signed cumulative integral stays strictly positive. Mixed-sign initial data have no cumulative return. In particular no cumulative zero interval, grazing return, or repeated return is possible for any subsequential limiting coefficient path.

## Identifying the surviving Poisson populations

Fix a finite output-endpoint cutoff |z|>epsilon and truncate large |z| and marks, leaving finitely many matched atoms with positive marks separated from zero. Choose all cutoff boundaries to have zero limiting intensity; each projected stable mark has a density. Including S_m and the uniformly vanishing drift/error variables in the joint coupled tuple makes the localized pathwise bounds available along every extracted subsequence. Endpoint coordinates satisfy W_i(0)/a_m -> z and V_ij(0) -> v_j. Initial residual signs agree with sigma for all large m.

An initially active atom with sigma_j z<0 dies on a time tending to zero. Indeed r_m,j has its initial sign and magnitude bounded away from zero on a short interval, uniformly by residual convergence, and L_m grows without bound. Survival through a fixed short time would contradict the integrated gate formula.

For a supporting atom sigma_j z>0, fix t strictly before the limiting cumulative return. Near zero, uniform residual convergence gives sigma_j r_m,j>0, so that the gate cannot die there (W_i retains its sign). On the remaining interval to t, sigma_j J_j has a positive minimum; uniform J_m convergence makes the integrated gate formula positive at any alleged first hit. The fixed positive initial mark also controls the unscaled o(1) error. Thus the atom survives through t.

If t is after the limiting cumulative return, there is some s<t with sigma_j J_j(s)<0. Survival through s contradicts the integrated formula, since L_m |z| times that negative margin dominates the finite mark and o(1) error. Once dead the gate stays dead. The sign geometry ensures that the exceptional times consist only of zero and at most one later return.

It follows for each finite truncation that the initial-square-weighted alive process converges at almost every time and hence in L1. The removed small-weight contribution is uniformly bounded by

Z_m,epsilon=a_m^(-2)sum_i W_i(0)^2 1{|W_i(0)|<=epsilon a_m},

with limsup E Z_m,epsilon<=constant epsilon^(2-alpha). Its limiting Poisson counterpart has the same vanishing bound. Large endpoints and excluded marks are controlled by probabilities of omitted atoms, not expectations of their untruncated squares. Let m increase, then remove the large-endpoint/mark truncations and then epsilon decrease. These unconditional bounds remain valid when intersecting with any residual/energy localization. They identify, almost everywhere,

B_j(t)=P_j before its first cumulative return, and B_j(t)=0 afterward.

Thus every subsequential limit solves the same irreversible population rule; there is no unsupported conditional-independence assertion involving the evolved residuals.

## Uniqueness and conclusion

Before any return the equation is r'=-Q0 r, so its cumulative vector is Q0^(-1)(I-exp(-Q0 t))r0. For mixed initial signs there is no return. For same signs, the elementary two-eigenvalue calculation in agents/d03_geometry.md gives exactly the threshold classification in the statement. Each finite return has the strict opposite sign of its instantaneous residual component. At that time the selected diagonal population is removed. The residual is then mixed-sign, so the new constant matrix Q1 preserves those signs and there can be no further cumulative return. This constructs the unique global solution of the rule.

Every subsequential limit is therefore this measurable function of the same initialization tuple; tightness and uniqueness identify the entire sequence. This proves the claimed joint C times L1 convergence. No convergence of all microscopic gate times is needed, and no claim about finite-width infinite-time limits is obtained by exchanging m->infinity with t->infinity.

Dependencies: the complete joint initialization proof is in ../20261023T222120Z/agents/c01.md and its independent review in ../20261023T222120Z/reviews/c03_root_review.md. The present compactness identification is also developed independently in agents/d01_hybrid.md; deterministic classification is in agents/d03_geometry.md. Catalog scope and literature limits are recorded in LITERATURE.md and CLAIMS.json.
