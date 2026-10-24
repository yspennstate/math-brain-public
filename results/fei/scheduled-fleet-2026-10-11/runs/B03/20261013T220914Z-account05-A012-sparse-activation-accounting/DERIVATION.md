# Opposite shared-selector reference: disjoint private cores

Bits throughout. Let g(a), h(b) be arbitrary Boolean functions on disjoint uniform private cubes and let z be fresh. Write mu=Eg, nu=Eh and F=(g+h)/2+z(g-h)/2. Supplied normalized references Rg,Rh are positive on their respective spectra. Empty-calibrate them to mu^2 and nu^2, preserving their conditional nonempty laws. KL disintegration shows this cannot increase either terminal CE. These known scalar biases are instance data, not sampled-frequency choices.

Set Q(0,empty)=((mu+nu)/2)^2 and Q(1,empty)=((mu-nu)/2)^2. For nonempty data T wholly in a, set Q(u,T)=Rg(T)/4 for u=0,1; for T wholly in b use Rh(T)/4. Mixed private sets have zero mass. Thus Q is a normalized, finite, explicit full-output reference. Its sector selector and private-subset labels are all included. The same formula with true core probabilities gives P_F. Coherent empty-row interference is retained rather than replacing that row by an unsigned mixture.

Consequently D(P_F||Q)=(D(Pg||Rg)+D(Ph||Rh))/2 exactly, and

    CE_F = (CE_g+CE_h)/2 + Delta(mu,nu),
    Delta = 2-mu^2-nu^2 + L((mu+nu)^2/4)+L((mu-nu)^2/4)
            -[L(mu^2)+L(nu^2)]/2,
    I(F)=[I(g)+I(h)]/2+d, d=(1-mu*nu)/2.

All zero terms have continuous value zero. No terminal entropy or reference deficit is deleted. The physical independence of a,b is essential to the last expression for d.

## All-bias payment

Let v_g=1-mu^2,v_h=1-nu^2,m=(mu^2+nu^2)/2,A=(mu+nu)^2/4,B=(mu-nu)^2/4. Decompose Delta=v_g+v_h+E(A,B)+J(mu,nu), where E(A,B)=m h2(B/m), and J is the empty-frequency contribution to the Jensen-Shannon divergence between the two child spectra. The nonempty JS and conditional-selector contributions are each (v_g+v_h)/2. This decomposition follows directly by expanding L; it also covers m=0.

The elementary binary entropy inequality h2(t)<=2 sqrt(t(1-t)) gives E(A,B)<=2 sqrt(AB)=|mu^2-nu^2|/2. A proof without importing a numerical bound: G(t)=2 sqrt(t(1-t))-h2(t) is symmetric and zero at 0 and 1/2. On (0,1/2), G'' has the sign of sqrt(t(1-t))/ln2-1/2, which changes once from negative to positive. G' tends to +infinity at 0 and is 0 at 1/2, with negative values immediately to the left of 1/2. Therefore G' crosses once from positive to negative, proving G>=0.

For J use d0(x)=[(1+x)ln(1+x)+(1-x)ln(1-x)]/2 <=1-sqrt(1-x^2). The difference of the right derivative and left derivative is x/sqrt(1-x^2)-atanh(x); its derivative is nonnegative on [0,1). Evenness and continuity give both signs and endpoints. Substitution x=(mu^2-nu^2)/(mu^2+nu^2) yields J<=(|mu|-|nu|)^2/(2 ln2). This independently reconstructs the scalar JS inequality used in A095.

If mu*nu>=0, let s=|mu|,t=|nu|. Then
  v_g+v_h<=2(1-st)=4d;
  |s^2-t^2|/2<=1-st=2d;
  (s-t)^2<=1-st=2d.
The last inequality follows because s^2+t^2-st<=1 on the unit square: for fixed t its convex dependence on s has maximum at 0 or 1, and both endpoint expressions are <=1. The middle inequality follows for s>=t from s^2-t^2+2st<=2 (maximize the convex quadratic in s at endpoints, then 1+2t-t^2<=2).
Thus Delta<=(6+1/ln2)d <(15/2)d. If mu*nu<0, conditional-selector entropy and JS are each <=1, so Delta<=2<=4d. d=0 means equal constant leaves and Delta=0 directly.

With C_mux=6+1/ln2<15/2, supplied CE_g<=K I(g),CE_h<=K I(h) give CE_F<=max(K,C_mux)I(F). This closes the one opposite shared-literal/private-disjoint admission with one payment of z. It is a reference-transfer refinement of familiar read-once composition, not a claim of a new FEI class or optimal constant.

## Requested two-event application

Take A={z=+1} A_a and B={z=-1} A_b, where A_a,A_b are arbitrary private conjunctions on disjoint cubes, and let q(a'),t(b') be supplied Boolean terminals on corresponding disjoint private data. The product [1+1_A(q-1)][1+1_B(t-1)] equals z?G:H, G=1+A_a(q-1),H=1+A_b(t-1), because A and B cannot occur together. These are two incompatible control events sharing the physical z. Using A095's biased activation reference bound (independently reconstructed below), with p_a=2^-r_a,p_b=2^-r_b,

  CE_F <= [p_a CE_q_cal+p_b CE_t_cal]/2
          +3[r_a p_a(1-Eq)+r_b p_b(1-Et)] + C_mux Inf_z(F).

Every physical influence occurs once: all private coordinates carry a factor 1/2 and z carries d. Consequently terminal bounds with constant K yield CE_F<=max(K,6,C_mux) I(F). Allow r_a or r_b=0. The whole bound is conditional on supplied terminal references; arbitrary difficult cores retain their weighted costs.

## Independent A095 biased-activation subclaim review

For any biased g and empty-calibrated normalized R, p=2^-r, Qvac=[1-p(1-mu)]^2, Qctl=p^2(1-mu)^2 per nonempty control subset, Qdata(U,T)=p^2 R(T). Summing proves normalization and the direct Fourier expansion proves debt exactly p D(Pg||R). For one control let t=(1-|mu|)/2. The conditional-selector cost is at most 2t(1-t)+[2t^2 ln(1/t)+t^2]/ln2, using ln(1+x)<=x on the empty row; the above independent JS proof adds <=2t/ln2. Maximizing the resulting t expression gives Delta_activation/t <=2+(2+exp(-1/2))/ln2<6, since ln2>2/3 and exp(-1/2)<2/3. The actual influence (1-mu)/2>=t. Iterating gives CE_F<=p CE_g_cal+6rp(1-mu), with exact terminal debt retained. This accepts only the biased transfer subclaim of A095-RANK-KL-EQUIVALENCE@2, not its rank equivalence or other block bounds.

## Structural admission and hidden-core exclusion

Use a finite structural certificate whose leaves are literals or constants and whose internal operations are disjoint products, fresh point activations, sign flips, and the above fresh-selector mux with disjoint private child supports. No arbitrary Boolean leaf is admitted. Keep the actual bias and the explicit calibrated reference at every node. Constants and characters have zero spectral CE. Disjoint products tensor the references, add CE and influence, and preserve calibration. Sign flips preserve squared spectra and influence. The proved activation and mux transfers imply by induction that every admitted function has a complete explicit calibrated reference with CE<=(15/2)I (indeed max(6,C_mux) suffices).

This admission is hereditary under physical restrictions: a restricted product stays disjoint, a restricted point gate collapses to a constant or a shorter fresh gate, and a restricted mux either selects a child or retains disjoint restricted private cubes. Leaf literals become literals or constants. It is closed under substituting certified functions for private terminal slots. The operations actually used here (disjoint product, balancing, fresh activation and private-slot composition) are closed. Substituting a general certified function for a physical selector is outside this grammar and requires a separately proved gate-composition lemma.

For every f, define g_t=z0 product_(j=1)^t f(x_j) and F_t=1+A_r(g_t-1). Membership of f, g_t and F_t is equivalent in this certificate class, by closure forward and physical restrictions backward. Fix all controls active, z0 and other blocks to values with product +1 or compensate by sign flip. This recovers f. Thus arbitrarily rare activations cannot admit a nonmember seed. Membership in the class is a finite structural certificate, not the numerical condition CE<=KI assigned to an unproved opaque core. This adds fresh mux composition to the fresh-activation/disjoint-product operations, while retaining the earlier hereditary audit. It does not assert inclusion of every general read-once AND/OR formula in this particular grammar.

## Exact first unsupported line

When the two private cores share an additional physical coordinate, their nonempty frequencies can collide. The formulas Q=Rg/4 or Rh/4 then conflict and cannot be combined unsigned. No bound on the full conditional row entropy plus JS minus posterior KL, with one-use source-owned reserve, is proved here. Admission is preserved by physical restrictions, sign flips, disjoint substitution into terminals and fresh point activation; repeated data coordinates across the two branches violate admission. Arbitrary seeds can still enter as terminals, but cannot acquire an unproved terminal reference bound from rarity. A universal influence-paid terminal reference remains FEI-strength.
