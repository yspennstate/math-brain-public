# A stable-mask rare query with a nonvanishing reset cost

Uniform Boolean signs and base-two entropy/KL throughout. Full FEI remains OPEN. This strengthens a reference-price obstruction; it is not a Boolean FEI counterfamily. No reset below is asserted necessary for an eventual FEI proof.

## 1. An exact equal-mean reset identity

Let g(a,z) have two restrictions g_0,g_1 on the SAME nonempty set of essential z coordinates, all of which remain essential in both children. Assume E g_0=E g_1=mu, u=mu^2<1. Put t_b=hat(g_b)(FULL_z)^2>0, E=(t_0+t_1)/2, beta=1-alpha, c=alpha(1-u), 0<alpha<1. Use the prescribed matching-empty full-ESSENTIAL-block reference q(0)=p(0), q(S)=beta*p(S)+alpha(1-p(0))1[S=FULL] at the parent and both children. Require the parent's full coefficient nonzero, so all these references have exactly source support. Full characters obey the same formula. Both physical children are retained.

Equal child means imply p_parent({a})=0 and p_parent(0)=u. After erasing a, the empty row reference/source ratio is1. Every nonempty nonfull row has ratio beta, and the FULL_z row has ratio L_E=beta+c/E. The actual coherent outcome kernel on that last row is t_b/(2E). Consequently the ACTUAL reference outcome law is

    r_b = 1/2 + (c/2)(t_b/E-1).

Define L_b=beta+c/t_b. At every child source-positive atom the inherited/fresh reference ratio is1/(2r_b), except at FULL_z where it is L_E/(2r_b L_b). Thus the complete physically averaged fresh-minus-inherited KL is EXACTLY

    sigma_core = D(fair||r) + Gamma,
    Gamma = (1/2)sum_b t_b log2(L_E/L_b).

For F(t)=t log2[t/(beta*t+c)], Gamma=(F(t_0)+F(t_1))/2-F(E), and

    F''(t)=c^2/[ln(2)*t*(beta*t+c)^2]>0.

Hence Gamma>=0, and sigma_core>=D(fair||r), strictly positive when t_0!=t_1. No Fourier sample is used to choose a physical branch; r is the reference's own outcome law and physical weights remain1/2.

For either-sign activation J_epsilon(x,a,z)=epsilon at x0,g(a,z) at x1, use the normalized lift copying actual zero-data controller masses and putting q(S)/4 at each of the two copies of nonempty data. Query a and reset both activation children by the SAME rule. The zero-data masses are unchanged because the two child means agree. The same atom calculation gives

    r_b^act = 1/2 + (c/4)(t_b/E-1),
    sigma_act = D(fair||r^act) + Gamma/2.                 (1)

This is a different normalized outcome law from the core law; the activation bill is NOT obtained by blindly halving sigma_core. A disjoint character multiplying g makes its mean exactly zero; when the whole balanced core uses its full-essential spike, the same identity holds with u=0 and the same t_b.

## 2. Explicit actual Boolean family

For r>=4 let delta=2^-r and let h(z)=(-1)^z_1 when z_0=0, and (-1)^z_2 when z_0=1. Higher z coordinates are initially dummy. Define h_0 by flipping h only at the integer input1, and h_1 by flipping h at the integer inputs1,4,5. Integers use little-endian z bits. Finally g_r(a,z)=h_a(z). These are explicit truth tables/circuits, not abstract spectral weights.

At inputs1,4,5, h values are +1,+1,-1 and h(z)chi_FULL(z)=-1 at all three. Since h is balanced and its full coefficient is0 for r>=4,

    E h_0=E h_1=-2delta,
    hat(h_0)(FULL)=2delta, hat(h_1)(FULL)=6delta,
    t_0=4delta^2, t_1=36delta^2, E=20delta^2,
    Inf_a(g_r)=Pr(h_0!=h_1)=2delta.                    (2)

The parent full coefficient is (2delta-6delta)/2=-2delta, so its full atom is occupied. Every displayed variable is essential in the parent AND both children. Indeed h has four Walsh coefficients of magnitude1/2. The one-edit and three-edit corrections have magnitudes at most2delta and6delta<=3/8, so these original coefficients cannot vanish. At every other frequency the edit corrections are odd multiples of2delta and cannot vanish either. Each child therefore has FULL Fourier support; the parent may have zero atoms, but its old reference has EXACTLY that same parent support. All child inherited/fresh references have full support. There is no added source-zero support and NO changed essential mask after querying a.

Set eta=4alpha(1-4delta^2)/5. Equations(1)-(2) give

    r^core=((1-eta)/2,(1+eta)/2),
    r^act=((1-eta/2)/2,(1+eta/2)/2),
    sigma_core>=-(1/2)log2(1-eta^2),
    sigma_act>=-(1/2)log2(1-eta^2/4).                   (3)

The balanced variant chi_y*g_r has the SAME essential sets in both children and matching source/reference supports, with u=0 and eta=4alpha/5 EXACTLY. Its query influence remains2delta. Both activation signs are covered; activation query influence is delta.

For the fixed profile alpha1/6 and EVERY r>=4, eta>=21/160. Since -ln(1-z)>=z and ln2<1,

    sigma_core >441/51200 >1/128,
    sigma_act >441/204800 >1/512.                       (4)

Thus sigma_core/Inf_a(g_r)>2^(r-8) and sigma_act/Inf_a(J)>2^(r-9), diverging. The same conclusion holds for EACH fixed0<alpha<1 with the positive lower bound in(3). No finite K_alpha can make sigma<=K_alpha*Inf_a universally valid for this prescribed full-spike refresh, even with fixed essential masks, matching support, matching empty masses and arbitrarily small physical query influence.

The scalar Gamma in this family tends0: its two log ratios tend1/5 and9/5 while their source weights are O(delta^2). Therefore the exact limiting costs are -log2(1-16alpha^2/25)/2 for the core and -log2(1-4alpha^2/25)/2 for its activation. The all-dimensional obstruction already follows from(3)-(4); these limits are explanatory and not finite-search extrapolation.

## 3. This actual family is not an FEI counterexample

The base mux h has four Fourier weights1/4, H(h)=2 and three coordinate influences1/2. In the parent cube g_r differs from h at exactly4inputs out of2^(r+1), probability2delta. Fourier mass outside the four original h frequencies is at most ||g_r-h||_2^2=8delta. Splitting spectrum into those four atoms and the rest gives

    H(g_r)<=1+2+8(r+1)delta<=11/2, r>=4.

Each of the three original mux influences changes by at most twice the disagreement probability4delta, so I(g_r)>=3/2-12delta>=3/4. Hence H(g_r)<=8I(g_r) for EVERY r>=4. Multiplying by an independent character preserves entropy and adds1 to influence, so the same bound holds. Activation entropy is at most2+H(core)/2, while I(J_epsilon)=(1-epsilon*Ecore)/2+I(core)/2. Here |Ecore|<=1/8, so H(J)<=8I(J) as well. This elementary guard distinguishes a failed reference-price rule from the still-open conjecture; no novel FEI class result is claimed.

## 4. Relation to incoming work and the original account

A046 already found a rare-query, whole-core price obstruction at alpha1/7. Its example loses an essential y block in one child and recomputes the spike mask. This stage does not claim that first obstruction as new: equations(1)-(4) strengthen it to unchanged essential masks, full child source support and every fixed tilt0<alpha<1, and isolate the surviving ACTUAL outcome divergence as the obstruction.

A048 independently accepted A047's earlier3bit obstruction and paid its positive bill from an explicitly supplied original source for products of small factors with a bounded number of resets. That payment remains valid. The present local bill is not assigned that old bank for free; its all-dimensional supplier and cumulative budget are not supplied. Neither A036 point-factor invariants nor A039's high-influence parity-point price is refuted. No existing source debit, old quarter or complementary terminal is dropped to claim a global account failure.

FIRST UNSUPPORTED UNIVERSAL LINE: a hereditary reference construction/payment rule whose normalized physical outcome distortion is funded by the SAME actual unused original source surplus, retaining all previous debits and BOTH full terminal laws. A bound solely by the newly queried influence is false for the prescribed full-spike rule even in the stable-mask/full-support regime. One must change the reference mechanism or pay an appropriate whole-source/cumulative charge; an influence-priced arbitrary-core initial supplier remains unavailable. Full FEI remains OPEN.
