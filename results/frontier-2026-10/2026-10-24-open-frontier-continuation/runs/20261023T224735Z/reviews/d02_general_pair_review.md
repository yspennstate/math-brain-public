# Independent audit: general orthonormal-pair initialization and hybrid limit

**Disposition:** The fixed-`d`, two-orthonormal-input extension in `agents/d01_hybrid.md` is mathematically supported by its stated arguments, conditional on the explicit absorbing-at-zero flow selection. I found no counterexample to the initialization law or the global `C([0,T]) x L^1([0,T])` hybrid statement. The rotated 45-degree theorem in `TWO_INPUT_LIMIT.md` is a narrower, separately supported case. The general-pair result should remain labeled an internally reviewed extension until the finite-ray joint initialization and full dynamical proof are incorporated into a stand-alone main statement; external review and novelty are not established.

## Signed-ray initialization

Let `v_ell=(x_{1,ell},x_{2,ell})`, `h_ell^+=(v_ell)_+`, and `h_ell^-=(-v_ell)_+`. The proposed reduction

`F=sum_(ell,sign) h_ell^sign Z_ell^sign`,

`C=sum_(ell,sign) S_ell^sign h_ell^sign(h_ell^sign)^T`

has the correct ray coefficients and constants. Each `Z` has characteristic exponent `c_alpha|t|^alpha`, and each `S` has Laplace exponent `c_alpha Gamma(1-alpha/2)t^(alpha/2)`. A negative large `U_ell` contributes its **positive magnitude** on the ray `(-v_ell)_+`, so there is no missing minus sign. Zero rays are harmless.

The output-reduction error is genuinely negligible at the `b_m=(m log m)^(1/alpha)` scale. If `M_2(U)` is the second-largest absolute original coordinate, the ReLU Lipschitz bound gives `||H(U)-Psi(U)||<=C_d M_2(U)`. Since independent stable coordinates give `P(M_2>t)=O(t^(-2alpha))`, `E M_2^alpha<infinity`. Conditional on all hidden coordinates, the W-weighted error is an exact symmetric alpha-stable vector. For each test direction its conditional exponent is bounded by `const (m log m)^(-1)sum_i M_2(U_i)^alpha`, whose expectation is `O(1/log m)`. Hence the vector error tends to zero in probability. For the Gram matrix, the deterministic error is bounded by `C_d sum_(ell<q)|U_ell U_q|`. Choosing `alpha/2<p<min(alpha,1)` makes the probability of its normalized sum exceed epsilon at most `const m^(1-2p/alpha)->0`. These estimates preserve **joint** convergence when added to the primitive endpoint limit.

I checked the claimed independence of all primitive `Z`, `S`, and the full marked W-endpoint process `N`. Different signed product categories on the same coordinate are rowwise disjoint; different-coordinate product categories sharing W have one-row overlap `O(1/(m log m))` at fixed jump cutoffs, by the conditional-U estimate already proved in `research/T384_orthogonal_initialization.md`. Product versus U-square endpoints, product versus W endpoints, and W versus U-square endpoints have `o(1/m)` overlap by the split-at-large-auxiliary-scale argument. Distinct signed U-square endpoints are disjoint within one coordinate and asymptotically disjoint across coordinates. Because `d` is fixed, finitely many pairwise bounds control the whole mixed transform. Symmetry centers the discarded product small jumps, whose variance is `O(epsilon^(2-alpha))`; positive-square small jumps have mean `O(delta^(1-alpha/2))`. Thus the fixed-cutoff factorization survives cutoff removal. The joint law is stronger than separate marginal stable limits and is the needed basis for sign selection from `F` while using `N`.

## Positive definiteness, density, and the zero-off-diagonal case

The note states only that `C` is positive semidefinite. In fact it is **positive definite almost surely** for every orthonormal pair. The deterministic ray vectors span `R^2`: if `q` is orthogonal to every `h_ell^+` and `h_ell^-`, then it is orthogonal to every `v_ell=h_ell^+-h_ell^-`; hence `q_1 x_1+q_2 x_2=0`, which by orthonormality forces `q=0`. Every positive-stable `S_ell^sign` is strictly positive almost surely. Therefore for every nonzero q,

`q^T C q=sum_(ell,sign) S_ell^sign(q dot h_ell^sign)^2>0` almost surely.

The same span gives `F` a **bounded continuous and everywhere-positive density** on `R^2`. Its characteristic function is

`phi_F(t)=exp[-c_alpha sum_(ell,sign)|t dot h_ell^sign|^alpha]`.

The sum in the exponent is bounded below by `k||t||^alpha` for some deterministic `k>0`, by compactness of the unit circle and spanning; Fourier inversion gives a bounded continuous density. Select two linearly independent nonzero rays. Their independent, symmetric stable coefficients have strictly positive one-dimensional densities, so their vector sum has an everywhere-positive two-dimensional density. Convolution with the independent remaining ray sum preserves positivity. In particular both residual coordinates `y_j-F_j` are nonzero almost surely, and the initial residual cannot lie on a prescribed nontrivial affine line with positive probability.

The off-diagonal is

`C_12=sum_(ell,sign)S_ell^sign(h_ell^sign)_1(h_ell^sign)_2>=0`.

A term is positive exactly when `x_{1,ell}x_{2,ell}>0`. Thus `C_12>0` almost surely if any such coordinate exists. If none exists, every coordinate product is nonpositive; orthogonality gives `sum_ell x_{1,ell}x_{2,ell}=0`, so in fact **every** product is zero. Hence `C_12=0` exactly when the two inputs have disjoint supports in the original iid-stable coordinate basis. In that case the limiting residual equation is diagonal, each residual keeps its sign, and neither cumulative residual returns to zero. The hybrid rule correctly reduces to the constant post-boundary kernel `Q_0`; it should not be described as having a possible later switch.

For every j, the selected mass `P_j` is also strictly positive almost surely: on the chosen z half-axis, `P(u dot x_j>0)=1/2`, and the PPP has infinitely many small nonzero z atoms with finite, positive summed `z^2` mass. Thus an actual later switch loses a positive diagonal population.

## Global hybrid dynamics

The finite-width projected equations are correct for orthonormal inputs: the first-layer kernel block is diagonal, while the second-layer Gram matrix need not be. The energy bound makes `C_m(t)-C_m(0)` and total W-square drift uniformly negligible on finite physical-time intervals. Each initial-square gate clock `B_j,m` is bounded and nonincreasing because absorption prevents reactivation. Helly compactness in `L^1`, together with residual equicontinuity, permits subsequential limits and passage to the integral residual equation with `C+diag(A_1,A_2)`.

The order of the proof is essential and is correct in `d01_hybrid.md`: establish the two-dimensional sign-cone geometry for **arbitrary** bounded nonnegative subsequential `A_j` before identifying the gate law. If `b=C_12>0`, the mixed-sign cones are invariant under the cooperative transformed system. A same-sign trajectory can have only one residual-coordinate zero: at that zero the other coordinate is nonzero by invertibility of the fundamental matrix, and the crossed coordinate enters a mixed-sign cone transversely. Thus only that coordinate's signed cumulative residual can decrease and it can return to zero at most once, again transversely. For `b=0`, both residual signs persist. This rules out a gate that dies and would need to reactivate after a second cumulative reversal.

The atomwise identification is valid on strict-sign intervals. The pre-hit formula

`V_ij(t)=V_ij(0)+gamma_m W_i(0)J_j,m(t)+e_ij,m(t)`, `sup_i,j,t|e_ij,m(t)|=O(L_m^2/a_m)=o(1)`,

must only be used while an atom is active or at its first hit. The note does so. Fixed W-endpoint atoms keep their W sign under the `O(L_m)` total W drift. Opposing atoms die during a vanishing initial interval; supporting atoms survive while their signed cumulative clock remains positive and die after it becomes negative. The near-zero survival argument separately uses uniform convergence of the residual to keep the initial sign on a short interval, since uniform convergence of J alone would not control its sign arbitrarily close to zero. Finite-atom mark cutoffs, unconditional endpoint/mark escape bounds, and the `O(epsilon^(2-alpha))` small-W square-mass bound then identify `A_j=P_j` before its return and `A_j=0` after it in `L^1`. A possible gate ambiguity at the one return time has zero L1 cost.

Before the first return the equation therefore has the unique solution `r^0(t)=exp(-Q_0t)r_0`. If a return occurs, one P population is deleted and the mixed-sign cone prevents a second return; the post-return equation has the unique constant matrix `Q_1`. This identifies every subsequential limit and gives the claimed global output `C([0,T])` and kernel `L^1([0,T])` convergence. The positive definiteness of C also yields uniform exponential decay of the **limiting** residual after either phase; it does not justify interchanging the width and infinite-time limits.

The explicit classification also survives arbitrary orientation. For same-sign `r_0=sigma(u,v)` with `u,v>0` and `Q_0=[[a,b],[b,d]]`, `b>0`, a first-coordinate return occurs precisely when `v/u>d/b`, and a second-coordinate return precisely when `v/u<b/a`. These alternatives are disjoint because `ad>b^2`. At either equality, the corresponding signed cumulative residual approaches zero only as `t->infinity`; it does not switch at finite time. The full density of F makes an equality threshold a null event conditional on `(C,N)` for deterministic y, but the pathwise rule is well-defined even on that exceptional set.

I would make two proof-presentation repairs before promoting the general-pair note: (1) state the fixed-ray joint initialization lemma explicitly with the above PD/density consequences; (2) in the compactness step include the initialized energy and finite truncated endpoint configurations in the tight/coupled tuple, or phrase the atomwise claims as unconditional probability inequalities before passing to a coupling. This avoids tacit reliance on a Skorokhod coupling preserving microscopic trajectories. These are exposition repairs, not a counterexample to the theorem. The justified kernel topology is `L^1`; coalescing endpoint deaths at the later switch do not support an unqualified `J_1` claim.
