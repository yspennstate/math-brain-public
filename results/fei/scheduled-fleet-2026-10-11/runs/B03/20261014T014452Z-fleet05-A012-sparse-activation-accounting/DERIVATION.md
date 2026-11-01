# Two shared bits: exact collision influence ownership

Bits throughout. This continues A012's complete-reference admission packet after consuming the independently authored one-bit extension and A095's linear shared-width tax. No universal FEI result is claimed.

## 1. Setup, folding and a conserved influence partition

Let G(s,X),H(s,Y) be arbitrary Boolean signs, s a shared block of at most two uniform bits, X,Y disjoint private cubes, and z a fresh uniform selector. F=(G+H)/2+z(G-H)/2. Let d=Inf_z(F) and d*=min(d,1-d). If necessary replace H by -H for the proof: this preserves child spectra and swaps parent selector-frequency atoms, so B_z, JS_z, entropy and terminal costs are unchanged. The physical budget in the original output remains d, with d*<=d.

Extend child coefficients a_T,b_T to the union data cube. Let C consist of all shared-only sets; pad with dummy shared coordinates to give N=4 available sets. Write e_T=(a_T-b_T)^2/4, m_T=(a_T^2+b_T^2)/2, delta=sum_(T in C)e_T after folding. Parseval gives sum_all e_T=d*. Outside C only one child can have a nonzero coefficient. Its parent selector-frequency masses are equal and its entire conditional-selector entropy equals its total mass, which is 2 e_T. Therefore the exact ownership identity is

    B_out=2(d*-delta),  B_z=2(d*-delta)+B_C.               (1)

This is the new payment step. Replacing B_out by 2d*, as in A095's valid coarse bound, leaves the collision influence delta available a second time. Formula (1) reserves it for the collision packet instead.

Conditional private independence gives 2d*=E_s(1-u(s)v(s)), where u=E_X G,v=E_Y H lie in [-1,1]. The elementary pointwise inequality |u-v|<=1-uv implies |a_T-b_T|<=2d* for each shared-only Fourier coefficient. Thus

    0<=delta<=min(d*,4 d*^2).                             (2)

At each collision row the entropy packet is m_T h2(e_T/m_T). Add a dummy zero-minority row of mass 1-sum_C m_T. Jensen gives B_C<=h2(delta). No dummy entropy is charged and no reference mass is removed.

## 2. All-parameter two-bit erasure payment

If 0<d*<=1/4, put x=4d* in (0,1]. Since delta<=4d*^2<=1/4 and h2(q)<=q log2(e/q),

    B_z <= 2d* + f(delta),
    f(q)=q log2(e/q)-2q.

Here f'(q)=log2(1/q)-2>=0 for q<=1/4. Equations (1),(2) therefore give

    B_z/d* <=2+x[1/ln2-2 log2(x)]
             <=2+2/(sqrt(e) ln2)<4.                     (3)

The maximum occurs at x=exp(-1/2), by elementary differentiation; continuous zero is included. The strict final bound follows from ln2>2/3 and e>9/4.

If 1/4<=d*<=1/2, the maximum of h2(q)-2q for q in [0,1] is log2(5/4), attained at q=1/5. This follows by solving h2'(q)=2 and evaluating. Consequently

    B_z <=2d*+log2(5/4)
          <=[2+4 log2(5/4)]d*<4d*,                     (4)

since (5/4)^2<2. If d*=0, the two children are identical or opposite everywhere on the union cube, so the selector spectrum is deterministic conditioned on data and B_z=0. Thus B_z<=4d* in all cases. This handles the first nonlinear shared-phase case without a common character translation and without assuming a terminal core reserve.

## 3. Full normalized reference and exact retained terminal debt

Supply normalized finite-cost references R_G,R_H positive on their respective spectra. Calibrate separately every shared-only atom T in C to a_T^2 or b_T^2; on the private complement preserve the incoming conditional reference law and rescale to its true total mass. The removed CE is exactly the categorical KL of all shared singleton atoms and the private complement, hence nonnegative. Arbitrary terminal cost and all conditional private debt remain.

Set Q(u,T)=(a_T+(-1)^u b_T)^2/4 on C. Outside C for a private G set use Q(u,T)=R_G^c(T)/4 in each selector sector, and for private H use R_H^c(T)/4. A reference can have off-target private sets; these are retained with the same formula. Sets meeting both private blocks have zero mass. This Q is one fixed normalized finite-output reference; coherent signs, all zero rows and the entire sector label law are explicit. Direct Fourier expansion gives its true probabilities by replacing private reference masses with actual child probabilities. Therefore

    D(P_F||Q)=[D(P_G||R_G^c)+D(P_H||R_H^c)]/2,
    CE_F=[c_G^c+c_H^c]/2+Delta,
    Delta=B_z+JS_z.

The standard scalar proof reconstructed in A012 stage 3 gives JS_z<=2d*/ln2: coefficientwise use ((1+w)ln(1+w)+(1-w)ln(1-w))/2<=1-sqrt(1-w^2), proved by differentiating, then sum the minority squared amplitudes. Combining (3),(4) proves

    CE_F <= [c_G^c+c_H^c]/2 + K d*,
    K=4+2/ln2<7.                                        (5)

The original influence identity is I(F)=[I(G)+I(H)]/2+d, by conditioning on the actual z. It includes each shared physical coordinate once through the averaged branch charge. Supplied child CE bounds with constants K_G,K_H give CE_F<=max(K_G,K_H,K) I(F). There is no integer prefix-rounding claim.

## 4. Structural admission and hidden-core audit

Extend the existing A012 literal/constant certificate grammar to fresh-selector muxes whose child support intersection has at most two physical coordinates. Keep disjoint products, sign flips and fresh point activation. Every node has an explicit normalized spectral reference. At a mux recompute its at-most-four shared moments and calibrate its child references as above. Products tensor references and add cost/influence; signs preserve squared spectra; the proved fresh-activation coefficient 6 is less than K. By induction the entire grammar has complete CE<=K I.

Physical restrictions preserve the syntax and cannot enlarge a support intersection. Fixing a selector selects its actual child; fixing shared/private bits leaves at most two shared bits; point activations either shorten or collapse to constants. Therefore the admission is hereditary. It survives balancing, disjoint tensor powers, and arbitrarily rare fresh activation. For any seed f, f, its balanced fresh tensor and its fresh activation have equivalent membership, since physical restrictions recover f from either construction. No opaque arbitrary Boolean leaf is admitted. This is an enlargement of the saved grammar, rather than treating a numerical CE bound as a supplied proof.

The class is proper. For f on four bits equal to +1 iff at least two binary inputs are one, all eight one-bit cofactors depend on all three remaining coordinates. Thus a fresh mux root would have child support intersection three, outside admission. Every nontrivial coordinate bipartition has an exact nonzero rank-one minor, excluding a disjoint-product root; these seven unordered partitions and their integer witnesses are in out/NONMEMBER_CERTIFICATE.json. A fresh activation root is a chain of constant-child muxes and is excluded by the same cofactor test. Sign flips do not change relevance or rank-one tests. This excludes every possible nonleaf root operation, so the function is a concrete nonmember. Its fresh balanced tensors and rare activations remain nonmembers by the restriction reflection above. This is an admission obstruction, not a FEI counterexample.

## 5. Independent A095 application review and exact remaining line

A095-RANK-KL-EQUIVALENCE@3, new shared-t application Sections 1-4, is independently valid without repair. For N=2^t,t>=2, conditional means give the same cap delta<=min(d*,N d*^2); Jensen bounds B_C; B_out<=2d*. Split at d*=1/N. In the rare regime x=N d*<=1 gives B_C/d*<=x log2(e N/x^2)<=log2(e N), because the derivative in nats is ln N-1-2ln x>0. In the other regime monotonicity of h2 below 1/2 gives B_C/d*<=t+1/ln2. Add 2d* and 2d*/ln2 for the stated t+2+3/ln2 bound. The calibration reference/debt is exactly that of Section 3 for arbitrary C. This accepts only the new upper-bound/calibration/debt application, not the bundled rank equivalence, earlier block claims or asymptotic lower-bound claim. The improved ownership identity (1) is a separate refinement, not a source error or substantive repair needed for that acceptance.

For three shared bits this proof only gives in the rare regime B_z/d*<=2+x[1+1/ln2-2log2 x], x=8d*. Its maximum is 2+2 sqrt(2/e)/ln2, above 4. This does not refute B_z<=4d* for three bits, but is the first exact unsupported line in attempting the same constant by the present scalar relaxation. At growing width selector-only absolute payment is impossible by the actual bent/point-flip family already recorded by A013/A097/A095. A universal nonreused terminal/shared-core reserve and arbitrary terminal reference payment remain open. Next test whether the three-bit extremal minority relaxation is Boolean-realizable with actual joint row masses; do not spend its collision influence again.
