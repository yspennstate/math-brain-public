# Three unequal shared rows with arbitrary correlated private events

All entropies and reference costs are in bits. Boolean inputs are uniform, Fourier coefficients use the probability normalization, and costs are ideal negative logarithms. Full FEI is open.

## 1. Actual Boolean family and exact influence owner

Let c be a sign on three shared bits s. Let w0,w1,w2 be distinct shared points, and let E0,E1,E2 be arbitrary events on the SAME independent finite private cube V. No independence between the events is assumed. Write qj=Pr(Ej), and set

G=c(s), H=c(s)(1-2 sum_j 1_(s=wj)1_Ej(V)), F=(G+H)/2+z(G-H)/2.

The shared row indicators are disjoint, so H is Boolean even when the events overlap or coincide. Set a_T=chat(T), b_T=(1/8)sum_j c(wj)chi_T(wj)qj. Then

d=Inf_z(F)=sum_j qj/8 <=3/8, delta=sum_T b_T^2=sum_j qj^2/8,

B_z=2(d-delta)+sum_T Phi((a_T-b_T)^2,b_T^2),

where Phi(A,B)=A log2((A+B)/A)+B log2((A+B)/B), with continuous zero terms. The shared-only parent amplitudes are a-b and b. Every nonempty-private frequency belongs only to H, giving two equal parent atoms and erasure equal to their combined mass. The total private mass of H is 4(d-delta), proving the displayed identity independently of the joint private spectrum.

The physical influence identity is I(F)=(I(G)+I(H))/2+d. The selector is paid ONCE. The original physical shared-coordinate influences are used; an affine relabeling below is only a symmetry of B_z,d, not of total influence.

## 2. General entropy tangent and convex corner certificate

For every rational r in (0,1), Gibbs' inequality for a two-point probability gives

Phi(A,B) <= lambda A+mu B, lambda=-log2(1-r), mu=-log2 r.

This also holds on both axes. Since r(1-r)<=1/4, lambda+mu>=2. For a fixed a and b linear in any real parameter vector, subtraction of 2b^2 gives the upper quadratic

lambda a^2-2lambda a b+(lambda+mu-2)b^2.

Its quadratic coefficient is nonnegative, so it is convex in every coordinate. After summing and subtracting 2d, where d is linear, its maximum on a rectangular box occurs at a corner (apply the one-dimensional chord inequality successively). This argument applies to ANY finite number of row parameters, not just three. If a=0, Phi(b^2,b^2)-2b^2=0 exactly, so that frequency is omitted instead of bounded. Upper-rounded lambda and mu remain valid and keep the quadratic coefficient nonnegative.

In a box qj in [ij/2^D,(ij+1)/2^D], choose r at the center as b^2/((a-b)^2+b^2); if either squared amplitude vanishes, use 1/1024 or 1023/1024. These are fixed rational tangent parameters on the ENTIRE box. At its eight corners evaluate the upper quadratic for B_z-4d. Strict negativity certifies the whole box. No sampling or interpolation assumption is used.

## 3. Complete phase symmetry and continuum

Any ordered triple of distinct points of F2^3 is affinely independent: the two nonzero differences are unequal and hence independent over F2. Extend them to a basis to map the triple to (0,1,2). Invertible affine relabeling permutes/signs Fourier coefficients, preserving B_z and d. Common character multiplication and common sign multiply both branches and permute/sign their Fourier coefficients. The 256 phase tables therefore reduce to the 16 masks

0,1,2,3,4,5,6,7,16,17,18,19,20,21,22,23.

CLASSIFICATION.json records every phase-to-representative map. The validation separately checks the direct Walsh coefficients, all 256 masks and all ordered triples through affine maps.

Two analytic domains are reused with their actual hypotheses. For arbitrary conditional row means on at most three shared bits, delta<=min(d,8d^2). Entropy concavity gives B<=2d+h2(delta)-2delta. If 0<d<=1/32, put x=8d<=1/4 and use h2(delta)<=delta log2(e/delta) to obtain B/d<=2+x[1+1/ln2-2log2 x]<=2+(5+1/ln2)/4<4. Monotonicity on this range follows by differentiation; ln2>2/3 suffices for the final strict bound. If d>=1/6, maximize h2(u)-2u at u=1/5 to get B<=2d+log2(5/4)<2d+1/3<=4d, since (5/4)^3<2. At d=0 all qj=0 and B=0. No denominator is canceled there.

The remaining domain is certified by the entropy tangents. Each of the 16 jobs starts with the 64 side-1/4 cubes. A box is either certified by strict negativity at every corner, pruned entirely inside an analytic domain, or split into its eight dyadic children. All jobs terminate with no unresolved boxes. The separate verifier reconstructs direct Walsh coefficients, uses exact Fraction logarithm series instead of author fixed-point arithmetic, recomputes every tangent-corner sign, and verifies exact volume one plus the dyadic antichain condition (no ancestor/descendant overlap). The saved result counts and the minimum independently recomputed rational gap are in EXACT_RESULTS.json. Thus every real probability triple is covered, and in particular every event triple on every finite private cube satisfies

B_z<4d for d>0, B_z=0 for d=0.

The already reconstructed scalar channel inequality JS_z<=2d/ln2 gives Delta=H(F)-(H(G)+H(H))/2 <=K d, K=4+2/ln2<7. This last scalar inequality is a dependency; the new result is the B_z payment.

## 4. Complete reference and retained joint private bill

Supply fixed normalized finite-cost child references positive on true support. Calibrate each shared-only atom to its actual child probability, preserving and rescaling the full private conditional reference law, including any off-target reference mass. Calibration decreases CE by categorical KL. G is pure shared, so its calibrated reference equals its true spectrum. On parent shared-only atoms set Q=P_F. On each private H frequency set Q(u,T,U)=R_Hcal(T,U)/4 for BOTH selector sectors. Then Q is one fixed normalized reference, and direct expansion gives

D(P_F||Q)=D(P_H||R_Hcal)/2,
CE_F=(CE_Gcal+CE_Hcal)/2+Delta.

The true joint private entropy is INSIDE these complete costs. It is not replaced by a product of three event references: arbitrary correlations can cause private Fourier interference. If both actual child certificates satisfy CE_child<=K I_child, the parent satisfies CE_F<=K I(F). An independent common terminal factor tensors the reference and adds its entire CE and KL; it supplies no unused reserve.

## 5. Structural admission, closure and hidden-core test

Extend A012's v4 literal/constant grammar by this three-row rule, requiring BOTH ACTUAL CHILDREN to have already constructed structural certificates and checking the displayed Boolean representation. Earlier signs, disjoint products, overlap<=2 muxes, common-event three-bit rules and fresh point activations remain available. Each node constructs its normalized complete reference, so the same K=4+2/ln2 works inductively. This is a well-founded syntax with no arbitrary opaque leaves.

Physical restrictions preserve it: a private query restricts the three events on their common private cube and retains the rule; a shared query leaves at most two shared coordinates, handled by the earlier overlap<=2 rule; a selector query chooses its already certified child. Structural induction supplies the actual restricted child certificates. Disjoint product, fresh balancing and fresh point activation remain closed. Conversely, restrictions of the fresh balanced tensor or rare activation recover the original seed (up to an allowed sign), so membership is reflected back to the seed. An uncertified arbitrary hard core cannot gain admission by rarity.

The new rule still has one pure shared child supported on at most three coordinates. The five-bit sign that is +1 exactly at Hamming weight at least two therefore remains outside: every one-bit cofactor depends on all four remaining bits; no activation root has such cofactors, and every nontrivial disjoint bipartition has a nonzero two-by-two product minor. The earlier exact 10-cofactor/15-minor certificate is retained and replayed. This is a grammar nonmember, not a FEI counterexample. The v4 admission of all at-most-four-bit signs remains valid.

## 6. Exact remaining line

The full three-bit profile q(s) may have four to eight separately varying rows, or both actual branches may have private fluctuations. Neither reduction to three rows nor a complete collision payment for these cases follows from the certificates above. The entropy tangent/corner lemma removes the previous first-order box overestimate and applies in arbitrary parameter dimension, making complete signed-row certification the next direct mechanism. Growing shared overlap still needs a dimension-independent structural payment from unused shared/terminal capacity. No universal reference admission or full FEI proof follows here. Independent-agent review is pending.
