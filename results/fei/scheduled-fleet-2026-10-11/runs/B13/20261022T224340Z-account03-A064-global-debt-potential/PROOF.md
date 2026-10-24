# Deferred conversion through a physical bent carrier

All entropies and KL use bits. The reference at each node is declared explicitly. No universal FEI certificate is assumed.

## 1. General carrier symmetry, including reference-only rows

Let y be m physical bits, z any additional physical bits, and g(y,z) any Boolean sign. Let u,v be fresh bits, let L(y) be a linear parity, and put

    F(u,v,y,z)=(-1)^((u+v+L(y))*v) g(y,z).

The affine constant in u is immaterial and is allowed. Start with ANY spectral reference R for g, containing its squared spectral support. Lift it by the independent uniform spectrum of the two-bit bent sign (-1)^(uv), then apply the SAME physical shear w_u=u+v+L(y), w_j=t_j to its frequency coordinates. Call the result Q. R need not be a product and may have source-zero/reference-positive atoms. Actual and reference Fourier coordinates are merely permuted by the shear, so no general influence invariance is presumed.

For the physical query v, the actual children are g and a sign times chi_u chi_L g. In the remaining frequency labels their source supports have u-indicator respectively zero and one, with the y frequencies translated by L in the latter. Pair every atom (u-indicator0,S_y,S_z) with (u-indicator1,S_y+L,S_z). The erased reference has equal mass R(S_y,S_z)/2 on this pair. Their erased source masses are likewise p_g(S_y,S_z)/2. If that source mass is positive the coherent v kernel is respectively deterministic zero and one. If it vanishes, BOTH atoms use the prescribed fair extension. Thus every pair predicts a fair outcome, with its full reference-only mass retained. The predicted reach is exactly1/2 in each branch and O_v=0.

This proves fair prediction for inherited lifted references, not only for product references. In particular an unmasked selector query whose two children have a common carrier preserves this lifted form: all amplitudes share the same bent coefficient, so its squared child kernel depends only on core frequency; erasure, normalization and fair extension preserve the independent uniform carrier factor before the shear.

If Q is the ACTUAL product reference, take L to mask every y coordinate. Their parent spectral marginals, as well as those of u,v, are1/2. Spectator z marginals are unchanged from g. Let M_y(g)=sum_j h2(Inf_yj(g)). The exact signed product-reset debit of this carrier query is

    D_v=M_y(g)-m <=0.

Indeed parent entropy is H(g)+2, both child entropies are H(g), the parent marginal entropy is m+2+M_z, and both children's marginal entropy is M_y+M_z (their u indicator is deterministic). Hence the mean child TC minus parent TC is M_y-m, and O_v=0. No claim that an arbitrary Boolean function has such a fresh carrier is made. Optional subsequent query u has O=0 and no positive product-reset debit, since the actual u-frequency is deterministic in each converted child.

There is also a quantitative bound for an ARBITRARY inherited reference Q containing source support, without the exact lifted-reference assumption. Let U be its erased law at v, let tau exchange the two frequency atoms in each pair above, and set eta=TV(U,tau#U). The physical kernel satisfies k0(tau T)=1-k0(T), including fair source-zero pairs. If kappa=2k0-1, the predicted bias is

    r0-r1=sum_one_representative_per_pair (U(T)-U(tau T))*kappa(T).

As |kappa|<=1, its magnitude is at most eta. Source support gives both r outcomes positive; if eta<1 this yields

    O_v <= -(1/2)log2(1-eta^2).

For 0<=eta<=1/2 the right side is <=eta^2/(2 ln2*(1-eta^2))<=2eta^2/(3 ln2)<=eta^2. The first scalar bound follows by integrating 1/(1-t) on[0,eta^2], and ln2>2/3 follows from the positive atanh series at1/3. Equality at eta=0 is allowed. Thus exact symmetry is not essential for a quantitative selected-query outcome payment; its actual imbalance must be measured. This prices O only: a fresh terminal product reset still needs its separate signed booking, as in Sections2--4. The restriction eta<=1/2 cannot simply be omitted from the quadratic corollary; a full-support two-bit bent core and eta=3/4 give O=-log2(7/16)/2>9/16.

More explicitly, let K=KL(p_F||Q) and C=TC(g). Both carrier children have actual product TC=C, irrespective of Q, so the COMPLETE signed selected-query debit is D_v=O_v+C-K. Its nonnegative booking is [D_v]_+, bounded by [C-K-log2(1-eta^2)/2]_+ (or [C-K+eta^2]_+ at eta<=1/2). Parent potential K+[D_v]_+ and terminal potential C retain every current/terminal KL and have drift at least O_v. In the exact lifted case K=KL(p_g||R), eta=0 and this reduces to [TC(g)-KL(p_g||R)]_+. Thus the outcome estimate is not substituted for a free product projection. Availability of the required positive booking from an actual original owner remains a separate condition.

## 2. Apply this symmetry to the A061 bilinear-field stress family

Fix l>=2, m=3l and a field K of size q=2^l, with a nontrivial additive character psi. The actual core is h(a,b,x)=psi(a)(1-2*1[x=ab]). It is balanced. Its squared Fourier spectrum has one atom c^2=(1-2/q)^2 at (alpha=1,beta=gamma=0), and (q-1)q^2 atoms of mass4/q^4 at gamma!=0. To derive this, average x first: gamma0 gives the character atom; at nonzero gamma the b character sum forces the unique a=beta/gamma. The coefficients there have magnitude2/q^2. This proves the support formula for every finite field, rather than extrapolating a finite table check. Write H_h for its exact entropy and M_h=sum of its m binary marginal entropies.

Use the same physical shear and carrier as Section1 with L the parity of all m core bits. A fresh physical selector s chooses G=carrier and H=carrier*h. The root actual product reference Q is uniform on all m+3 spectral indicators. Both selector-child spectra have disjoint core supports and share the carrier. Parent TC is

    K_root=m-1-H_h/2.

At the first query s, retain the actual inherited Bayes references Q_G,Q_H: DO NOT convert to products. They are lifted references as in Section1. The erased product reference predicts

    r_G=2^(-l-1),  r_H=1-r_G,
    O_s=-(1/2)log2(4*r_G*r_H),
    K_G=m+log2(r_G)=2l-1,
    K_H=m-H_h+log2(r_H).

These KL are on the actual source support. Reference-only rows are retained in the normalized reference: their core masses before selector prediction are epsilon=q^-1-2q^-3 and each contributes its fair half. Omitting them would replace r_G by q^-3, a different false account. Conditional selector erasure KL is ZERO because its source conditional spectral bit is fair and Q is uniform. Therefore K_root=O_s+(K_G+K_H)/2 exactly.

Now query physical v in BOTH actual selector children, carrying Q_G,Q_H. Section1 proves both predicted outcomes fair, including every reference-only pair, so there is no second outcome KL. Only at these four leaves convert explicitly to their actual products. The G leaves are a constant and a character, with H=TC=0. The H leaves are h and a character translate of h (with a deterministic u-frequency), so H=H_h and TC=K_h=M_h-H_h. All four actual functions remain on their full ambient cube; no entropy or normalization is removed by a supposed easy terminal.

The one required conservative future booking at each selector child is

    b_G=[0-K_G]_+=0,
    b_H=[K_h-K_H]_+=[M_h-m-log2(r_H)]_+.

Set W=(b_G+b_H)/2. This is the total new expected booking from the SAME original ancestor owner, not a second bank. Negative net block cost alone does not prove W=0: b_H must be kept at the intermediate stopping cut. The potentials

    P_root=K_root+W,
    P_G=K_G+b_G, P_H=K_H+b_H,
    P_final=actual product TC

are all nonnegative. The first drift equals O_s exactly. Each second drift is b_branch-(TC_final-K_branch)>=0=O_v. Thus EVERY stopping cut of this declared two-query policy, including cuts stopping only one selector branch, retains the ACTUAL current reference KL plus its pending terminal-conversion booking. At a root stop the reference is Q; at a selector-child stop it is Q_G or Q_H; at a leaf stop it is the explicit product. If a cut stops in the middle, its pending booking is still present in P. In particular

    E P_tau+E sum_before_tau O <= K_root+W,
    E CE(actual_terminal,current_reference)+E sum O
        <=K_root+W+E H(actual_terminal).

All filtrations are the fair physical history and all depths are at most two (optionally three for u). There is no limit, independence of increments, or infinite-stopping premise.

## 3. Exact all-l price of the pending intermediate booking

For each nonzero physical x-direction, Inf_x(h)=2/q: exactly one of two distinct exceptional points changes sign. For a b-direction, a=0 gives no change, and otherwise the same two-point count gives p=2/q-2/q^2. For an a-direction the same number occurs if psi(direction)=1 and its complement if psi(direction)=-1. Every nonzero direction has nonzero multiplication; the count applies in any chosen physical basis. Binary entropy is invariant under complement, so

    M_h=2l*h2(p)+l*h2(2/q).

For l>=3 both p and2/q are <=1/4. Binary entropy is increasing on[0,1/2] (its derivative is log2((1-t)/t), with endpoints by continuity). The exact scalar h2(1/4)<13/16 yields M_h<13m/16. Since r_H>=7/8>1/2, -log2(r_H)<1, whereas m-M_h>3m/16>=27/16>1. Thus b_H=0 and W=0 for EVERY l>=3. Neither a new ancestor withdrawal nor any intermediate zero-KL assumption is used.

At l=2, h has one atom1/4 and48 atoms1/64, hence H_h=5. Here M_h=4h2(3/8)+2 and r_H=7/8. The remaining positive branch booking is

    delta=11-(3/2)log2(3)-(5/2)log2(5)-log2(7).

Its exact bounds 0<delta<1/64 are certified by the integer comparisons

    2^22 > 3^3*5^5*7^2,
    2^703 < 3^96*5^160*7^64.

Thus W=delta/2 is positive but <1/128. This width-two exception is essential: deferred final net debt is negative, yet making every intermediate stop legal still costs a small positive booking.

## 4. One original owner, earlier bookings and complete boundaries

The A061 original expected owner is defined ONCE before query s:

    Sbar=mean_s(4I(F_s)-H(F_s))=2m+2-H_h/2.

Its child certificates are actual: I=m/2+1 and H=2 or2+H_h; H_h<=m, so both4I-H are positive. This is a family-specific eligibility fact, never a universal hypothesis silently applied to all Boolean functions. If an earlier conservative booking omega has already consumed this same owner, it stays consumed. Assume 0<=omega<=Sbar/4 (or more generally omega+W<Sbar); do not renew the bank after either query.

The caller must supply this as the SAME original carried owner and supply the already booked root product reference. Defining the current Sbar does not authorize a new descendant bank or prove that a previous arbitrary history has left it available. The old omega is a retained explicit input, not a newly proved past-history eligibility statement.

For l>=3 W=0. For l=2 Sbar=23/2, so W/Sbar<1/1472. In all cases W<Sbar/1472 and

    Sbar-omega-W > (1103/1472) Sbar   when omega<=Sbar/4.

This bounds EXPECTED spending over actual stopping cuts. It is not a separately available copy of this capacity in each branch. Terminal cross-entropies at the complete two-query cut have mean M_h/2, with mean entropy H_h/2 and mean TC=(M_h-H_h)/2. Neither term is zeroed.

For comparison, the original immediate selector product reset had debit1+O_s>(l+1)/2. Deferring it through v reduces the new positive booking to ZERO for l>=3 and to less than1/128 at l=2, including the intermediate stopping boundary. The source's immediate-reset upper price also reconstructs directly: D_old=1+O_s<1+l/2, while Sbar>=9l/2+2 and (9l/2+2)/4>1+l/2 for every l>=2. Thus its original conditional D_old<Sbar/4 assertion holds unchanged; our smaller price comes from deferring the reset, not revising that source number. The net final block debit is

    O_s+mean TC_final-K_root =1+O_s-m+M_h/2 <1-l<0,

using M_h<=m and O_s<l/2. This negative endpoint statement is valid, but is not substituted for the stronger stopping-cut accounting above.

## 5. Universal gap and evidence rung

The general fresh-carrier symmetry and the all-l deferred-conversion payment are written proofs, with exact actual spectra, reference kernels and boundary certificates to be executed separately. No Lean certification or independent acceptance is implied until recorded. A087's independent acceptance of A064 v2 is consumed without repeating that finite certificate.

Executed validation now records: pilot l=2 plus two general carriers,6325 exact assertions in0.2873476s; full l=2,3 and all16 two-bit carrier cores,56758 assertions in1.4198857s;48 deliberately imbalanced inherited references,4742 assertions in0.1341142s. Main plus imbalance count is61500, excluding pilot overlap. Atomic KLs are normalized and prime-log identities are checked exactly, rather than by interval overlap; strict inequalities use outward96-bit rational bounds or the three integer powers displayed above. Every physical edge influence is independently compared with its spectral marginal. Full parent dimensions are9 and12, fixed in advance. Source-zero/reference-positive rows are included through both physical queries. These finite checks support the all-dimensional written arguments; they do not establish those arguments by extrapolation. The new conditional selected-query imbalance bound retains an explicit full signed terminal-reset cost above.

First unsupported universal line: a general Boolean restriction history admits an eligible selected query/block or a fresh-carrier factorization, and genuinely unused ancestral reference/influence capacity pays any remaining non-carrier conversions and the full terminal core cost. Arbitrary g is retained at carrier terminals, so Section1 does not establish FEI for arbitrary g. The new result neutralizes the explicit all-dimensional local-price obstruction by a physical selected block, rather than presuming a universal local bound or increasing a fixed price.
