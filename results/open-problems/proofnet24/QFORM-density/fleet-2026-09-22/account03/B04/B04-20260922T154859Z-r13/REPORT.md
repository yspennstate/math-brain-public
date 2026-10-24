# account03/B04 QFORM — determinant-retaining ridge window and 1/39 spectral threshold

Programme: QFORM-DENSITY-3EIG-20260922
Run: B04-20260922T154859Z-r13
Assignment: Product Fourier rearrangement
Execution status: WITHOUT_VERIFIED_BRAIN
Full conjecture status: OPEN

## 1. Scope and source pins

Exact target: for every dimension, every product law with independent real coordinate densities bounded by one, and every real symmetric A with at least three eigenvalues of absolute value at least one, prove a universal L-infinity bound for the density of X^T A X (and separately continuity), or produce a valid counterexample.

This report does NOT prove the full target. It uses the completed ridge-density criterion from

- yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7
- proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md

and independently checks only its Section 6 ridge-perturbation lemma and Section 7 MSS/spectral-window passage. The free-regularizer graph/Fourier argument in Sections 3--5 is treated as a supplied premise here, not re-reviewed in full by this run.

The designated partner account04/B04 had no completed QFORM handoff or canonical report visible at the fresh prepublication snapshot, so no partner result is fabricated. The owner-designated interactive ridge-window result is the completed compatible result actually applied.

Live corrections consumed include the false uniform pointwise Fresnel-decay route, false universal local-cross-rank-three dichotomy, false single-Schur extraction, fiber-sup dimension loss, and the requirement to preserve original-coordinate product provenance. Nothing below assumes independence after spectral rotation.

## 2. Scoped independent check: ridge perturbation lemma PASS

Let B=B_0+F with ||F||<=eta and S=range(B_0). For gamma>0 define

K = B(gamma^2 I+B^T B)^(-1)B^T.

The claimed inequality is

(K)_{ii} <= [sqrt((P_S)_{ii})+(eta/gamma)sqrt(1-(P_S)_{ii})]^2,

hence, if max_i(P_S)_{ii}<=ell,

(K)_{ii} <= [sqrt(ell)+eta/gamma]^2.

Check. The singular-value functional calculus gives 0<=K<=I. For v perpendicular to S, B_0^T v=0, so B^T v=F^T v and

v^T K v
 = ||(gamma^2 I+B^TB)^(-1/2)B^T v||^2
 <= gamma^(-2)||F^Tv||^2
 <= (eta/gamma)^2||v||^2.

Write e_i=s+t with s=P_S e_i and t=(I-P_S)e_i. Applying K^(1/2) and the triangle inequality,

sqrt(K_ii)
 <= ||K^(1/2)s||+||K^(1/2)t||
 <= ||s||+(eta/gamma)||t||,

which is exactly the displayed coordinate-specific bound after squaring. No independence, rank, sign, or small-eigenvalue assumption is hidden here. PASS.

## 3. Scoped independent check: MSS spectral-window passage PASS

Let P be the spectral projection onto a chosen high spectral window, write A_H=U Lambda U^T with U having orthonormal columns, and suppose every row u_i satisfies ||u_i||^2<=epsilon.

The two-part MSS partition theorem gives a coordinate partition I,J such that both partial frame operators obey

M_I=U_I^TU_I <= (1/sqrt(2)+sqrt(epsilon))^2 I,
M_J=U_J^TU_J <= (1/sqrt(2)+sqrt(epsilon))^2 I.

Since M_I+M_J=I, both also satisfy

M_I,M_J >= delta(epsilon) I,

delta(epsilon)=1/2-sqrt(2epsilon)-epsilon.

Assuming delta(epsilon)>0, both U_I and U_J have full column rank. For

B_0=(A_H)[I,J]=U_I Lambda U_J^T,

polar decompositions U_I=Q_I M_I^(1/2), U_J=Q_J M_J^(1/2) show that the nonzero singular values of B_0 equal those of

M_I^(1/2) Lambda M_J^(1/2).

Hence, because A has at least three eigenvalues with |lambda|>=1,

s_3(B_0)>=delta(epsilon).

If E=A-A_H and ||E||<=tau, then F=E[I,J] satisfies ||F||<=tau and Weyl's singular-value perturbation inequality gives

s_3(B)>=sigma:=delta(epsilon)-tau.

Also range(B_0)=range(U_I), because Lambda is invertible on the selected spectral subspace and U_J has full column rank. Its projection is

P_range(B0)=U_I M_I^(-1) U_I^T,

so each diagonal obeys

(P_range(B0))_ii=u_i^T M_I^(-1)u_i <= epsilon/delta(epsilon).

Combining with Section 2 gives the exact ridge-leverage certificate used below. The direction of every inequality and the use of the full nonseparable tail E are correct. PASS.

## 4. New determinant-retaining three-singular-value bound

The supplied ridge criterion states, for q=1,

||p_Q||_infinity
 <= e/(sqrt(2) gamma) * theta/(theta-2) * D^(-1/(2theta)),

provided max_i K_ii<=1/2 and theta>2, where

x_j=s_j(B)^2/gamma^2,
theta=sum_j x_j/(1+x_j),
D=product_j(1+x_j).

Assume B has at least three singular values at least sigma and choose

gamma=sigma/sqrt(6).

Then at least three x_j are >=6, so theta>=18/7. Define

h(x)=log(1+x)-x/(1+x).

Since h'(x)=x/(1+x)^2>=0,

log D-theta=sum_j h(x_j) >= 3h(6)=:c,

where

c=3(log 7-6/7).

Therefore

D^(-1/(2theta)) <= exp[-1/2-c/(2theta)].

For theta>2 set

G(theta)=theta/(theta-2) exp[-c/(2theta)].

Its logarithmic derivative is

G'(theta)/G(theta)
 = -2/[theta(theta-2)] + c/(2theta^2).

Because c<4, this derivative is negative for every theta>2. Thus the worst case is theta=18/7. At that value,

exp[-1/2-c/(2theta)] = 7^(-7/12),

theta/(theta-2)=9/2.

Hence the supplied ridge theorem sharpens, under the same leverage gate, to

||p_Q||_infinity
 <= C_3/sigma,

C_3=(9 e sqrt(3)/2) 7^(-7/12)
   =6.809163560911903... .

This retains determinant information that was discarded in the coarser estimate 9sqrt(3e)/(2sigma)=12.8505.../sigma. The conclusion remains a continuous C_0 density because the same integrable Fourier envelope is used.

## 5. Parameterized spectral-window theorem

Let 0<tau<delta(epsilon), and let P_tau project onto all eigenspaces of A with |lambda|>=tau. Assume

(1) A has at least three eigenvalues with |lambda|>=1;
(2) max_i (P_tau)_ii <= epsilon;
(3) delta(epsilon)=1/2-sqrt(2epsilon)-epsilon>tau;
(4) [sqrt(epsilon/delta(epsilon)) + sqrt(6) tau/(delta(epsilon)-tau)]^2 <= 1/2.

Then the MSS construction in Section 3 gives a physical cross block B with

s_3(B)>=sigma=delta(epsilon)-tau

and the ridge-perturbation estimate with gamma=sigma/sqrt(6) gives max_i K_ii<=1/2. Section 4 then yields

||p_(X^TAX)||_infinity
 <= C_3/[delta(epsilon)-tau],

C_3=(9 e sqrt(3)/2)7^(-7/12).

The density is continuous and vanishes at infinity. Arbitrarily many spectral directions below tau are retained as a nonseparable perturbation; no moment, support, sign, or eigen-coordinate-independence assumption is introduced.

## 6. Concrete stronger corollary: threshold 1/39

Take epsilon=1/32. Then

delta=1/2-sqrt(1/16)-1/32=7/32.

Choose

tau=1/39,
sigma=7/32-1/39=241/1248.

The ridge leverage upper bound is

[1/sqrt(7) + 32sqrt(6)/241]^2.

It is strictly below 1/2. For a fully rational comparison, use

1/sqrt(7)<8/21,
sqrt(6)<49/20,

so

1/sqrt(7)+32sqrt(6)/241
 < 8/21+392/1205
 =17872/25305,

and

2*(17872)^2 < (25305)^2.

Therefore:

**QFORM-SPECTRAL-WINDOW-1OVER39-v1.** If P is the spectral projection onto |lambda(A)|>=1/39 and max_i P_ii<=1/32, then every admissible independent-coordinate input law gives a continuous C_0 density satisfying

||p_(X^TAX)||_infinity
 <= (5616 e sqrt(3))/(241 * 7^(7/12))
 =35.260730805054166... <35.27.

This strictly broadens the earlier 1/64-window theorem: P_(1/39)<=P_(1/64), so the leverage hypothesis is required only on a smaller spectral subspace, while the discarded nonseparable tail is allowed to have operator norm almost 1/39 rather than 1/64.

Within this exact epsilon=1/32 perturbation certificate, the largest admissible tail threshold is

tau_*=(7/32)*(1/sqrt(2)-1/sqrt(7)) /(sqrt(6)+1/sqrt(2)-1/sqrt(7))
      =0.025911987839088085...,

whose reciprocal is 38.592176185398856.... Thus 1/39 is a convenient near-maximal reciprocal-integer threshold for this particular MSS+ridgetail calculation; 1/38 is not certified by this same leverage inequality. This is a limitation of the certificate, not a counterexample to QFORM.

## 7. Explicit genuinely rotated full-rank indefinite example

Let n=128. Take three normalized Walsh-Hadamard columns U, with spectral coefficients (1,1,-1). Every coordinate row of U has squared norm 3/128. On U^perp choose any real symmetric invertible operator T with both signs, operator norm <1/39, and eigenbasis not aligned with the original coordinates. Set

A=U diag(1,1,-1) U^T + V T V^T,

where V spans U^perp. This A is full rank, indefinite, genuinely rotated, and has exactly the required three large eigenvalues. Its P_(1/39) diagonal equals 3/128.

For epsilon=3/128,

delta=1/2-sqrt(3)/8-3/128=0.26005614905389035...,

sigma=delta-1/39=0.23441512341286472...,

and the ridge-leverage certificate equals

[sqrt((3/128)/delta)+sqrt(6)(1/39)/sigma]^2
 =0.3227834809292246... <1/2.

Hence, for every independent coordinate law with densities bounded by one,

||p_(X^TAX)||_infinity
 <= C_3/sigma
 =29.04745846503782... <29.05,

and the density is continuous C_0.

This is not a diagonal-basis argument: the product law remains in the original coordinates and the small tail is an arbitrary nonseparable operator on U^perp.

## 8. What remains unpaid

The full conjecture remains OPEN because the bare three-large-eigenvalue hypothesis does not imply any leverage bound on P_(1/39), nor does it force a ridge-certified rank-three physical cut. The singleton-plus-two-banks family from the live correction ledger has cross rank at most two and must be handled by a separate aggregate mechanism.

The next useful implication is therefore a product-preserving heavy/diffuse decomposition at the spectral-window scale: prove that failure of max_i(P_(1/39))_ii<=1/32 yields a bounded-number/high-mass collection of original coordinates that can be routed into an existing aggregate hyperbolic-square or square-assisted mechanism without paying a vanishing local minor. That structural bridge, not the Fourier inversion in the diffuse branch, is the current obstruction.

No full-solution, novelty, partner-completion, or native-brain-ingestion claim is made.
