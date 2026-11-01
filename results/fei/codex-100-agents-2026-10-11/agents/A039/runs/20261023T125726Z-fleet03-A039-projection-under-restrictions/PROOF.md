# Rare unphased restrictions of a partially modulated point defect

All entropy, divergence and prices are bits. Full FEI is OPEN. External review is pending. This is a narrow refinement of A039's factor-only supplier; it does not revive the universal local-price rule refuted by A036/A040 or whole-core replenishment refuted by A037.

## 1. Definitions and exact normalized transaction

Let d=2^(-w), d_w(z)=1-2*1{z=0}, v=chi_J*d_w, and query j outside J. Initially assume 1<=|J|<=w-2. For any non-character factor f, use its ACTUAL spectrum p and the prescribed reference

q(0)=p(0); q(T)=beta*p(T)+alpha*(1-p(0))*1{T=FULL}, T nonempty,

with alpha=1/6, beta=5/6. Character and constant factors use q=p. These references have exactly the source support here. Let u be any disjoint Boolean spectator with a normalized, same-support reference q_u satisfying q_u(empty)=p_u(empty). Form G_epsilon(x,z,t)=epsilon at x=0 and s*v(z)*u(t) at x=1, where epsilon,s are either sign. Its full reference copies the two actual zero-data controller masses and assigns q_v(T)q_u(U)/4 on each controller copy for combined nonempty data.

Write l=q_v/p_v, a=q_u/p_u, assigning one to zero/zero ratios. The full reference is R=P*l*a, including zero-data rows. Both B=P*l and C=P*a are normalized: the v marginal of P is (delta_empty+p_v)/2. Erase the queried frequency, denoting erased laws by bars. The actual physical kernel is k_y(W)=P_y(W)/(2*Pbar(W)); use a fair kernel on source-zero rows. Let r_y=sum_W Rbar(W)k_y(W) be the reference's OWN outcome law.

The spectator cancels in the complete conversion. For U nonempty, the kernel does not depend on U; matching the spectator empty mass and summing q_u or p_u therefore gives r_y=sum_W Bbar(W)k_y(W). Also C has fair outputs. Since l>=beta, R>=beta*C and r_y>=beta/2. The inherited normalized child law is P_y*a*(Bbar/Pbar)/(2r_y). The destination law is P_y*a*l_y. Summing their log ratio against P_y/2 gives the exact identity

sigma=(1/4)sum_y D(p_vy||q_vy) - D(Pbar||Bbar) + D(fair||r).       (1)

No outcome normalizer, source-zero row, sign, terminal or spectator KL is discarded. In particular

O=D(fair||r)<=-(1/2)log2(beta*(2-beta))=(1/2)log2(36/35).          (2)

This is an all-dimensional algebraic reconstruction of the earlier A039 compensated identity, not a numerical overlap test.

## 2. Three-part coarsening and strict nonpositive rare-query theorem

The Fourier amplitude of v is 1-2d at J and has magnitude 2d everywhere else. Because j is unphased and at least two bits are unphased, none of empty, {j}, FULL or FULL\{j} equals J. Each of those four squared masses is 4d^2. The active child is chi_J*d_(w-1); the inactive child is the character chi_J. In the target-erased marginal of P, coarsen into empty, remaining-full, and all other frequencies. The respective Pbar masses are

A=1/2+4d^2, 4d^2, 1/2-8d^2,

and Bbar masses are

A-2alpha*d^2, alpha/2+(4-6alpha)*d^2, beta*(1/2-8d^2).

Data processing bounds the erased KL in (1) from below by the KL of these three masses. The active child's empty and full masses are 16d^2, and the other nonempty masses sum to 1-32d^2. The inactive child fresh KL is zero. Substitution and exact cancellation give

sigma <= -L/4 + A log2(1-2alpha*d^2/A)
          +4d^2 log2((2alpha+(16-24alpha)d^2)/(alpha+(16-32alpha)d^2)) + O,       (3)

where L=log2(6/5). At alpha=1/6 the ratio in (3) is at most 2, since numerator minus twice denominator is (-16+40alpha)d^2<0.

The exact integer inequalities 6^4>2*5^4 and 36^24<2*35^24 prove L>1/4 and O<1/48. For w>=4, discard the negative A-log term and use 4d^2<=1/64:

sigma < -1/16+1/64+1/48 = -5/192 < 0.                (4)

For w=3 the hypotheses force |J|=1. Here d=1/8, A=9/16, and the ratio is exactly 25/16. The integer inequality 25^3<4*16^3 gives log2(25/16)<2/3. Hence

sigma < -1/16+(1/16)*(2/3)+1/48 = 0.                (5)

Thus EVERY such unphased query has strictly negative full signed refresh cost, despite Inf_j(v)=2d tending to zero. This is uniform over spectator, both outer signs and core sign. For w=2, |J|=1, both physical children are constant or character, so fresh KL is zero and (1) gives sigma<=0 directly by common-kernel data processing. The case |J|=w-1 with w>=3 is outside this theorem; finite diagnostics cannot extend it.

## 3. Complete single-phase histories, original owner and old debit

For a single phase bit |J|=1, any unphased query either enters the inactive character or preserves the single-phase form. All such queries are free by (4)-(5), including the w=2 endpoint. A query of the phase bit has at most one nontrivial point-factor child. Therefore its fresh term in (1) is <=L/4; (2) gives sigma<11/160+1/48=43/480<1/8. At w>=3 the phase-bit influence is 1-2d>=3/4, so sigma<=Inf_j/6. At w<=2 both child spectra are atoms, hence sigma<=0. Once the phase bit is queried, remaining factors are ordinary signed point defects, whose same-profile costs are nonpositive by A036-NONPOSITIVE-COHERENT-SAME-PROFILE@1. Thus any adaptive physical history costs at most 1/6 per original single-phase factor, since it can query that factor's phase bit at most once on any path. Arbitrary adaptive stopping and sign-dependent choices are allowed; both outcomes remain in the ledger.

Here is a precise SAME-original-owner consequence, not a free replacement source. Take m disjoint factors v_i=chi_{onebit}*d_(w_i), w_i>=2, h=product v_i. Let F(x,a,b,z)=chi_a at x=0, h at x=b=1 and +1 otherwise. Use the ORIGINAL alpha0=1/8 product-factor sector lift Q0: copy all six actual zero-data/controller masses; place product q_i^0(T_i)/16 at each of four nonempty-data control copies. No earlier canonical-source conversion is included. Query b and retain b=0; make any finite adaptive data prefix in b=1 while x,a remain unqueried. At selected prefix leaves query a and retain BOTH signs; actually reset BOTH references to beta=5/6 factor-only lifts. Continue any finite adaptive data history, actually refreshing the selected factor after both physical outcomes, leaving other factors unchanged. Unselected leaves and all complementary terminals are retained.

The prior A039 factor likelihood/variance proof gives first reset sigma1<=L*sum_i V_i/4. The above all-history result gives sigma_later<=m/12, using b=1 reach 1/2. Prefixes only lower these bounds; phase bits consumed in a prefix cannot be charged again. The original cost A0<=L0*sum_i V_i/4, L0=log2(8/7)<1/5. Let t=Pr(h=-1), H0=H(F), I0=I(F). Sector entropy and influence give

H0<=3+(1/4)sum_i H_i; I0=1+t/2+(1/4)sum_i I_i.

For w>=3, H_i<=8w*d (the point-defect entropy bound, unchanged by Fourier translation), I_i=1+(2w-4)d. Therefore

4I_i-H_i-(L0+L)V_i-1/3 > 4-16d-19/40-1/3 >=143/120.

For w=2, H_i=2,I_i=1,V_i=3/4, and the same expression is >629/480>143/120. Consequently the SAME inclusive source margin M0=4I0-H0-A0 obeys

M0-sigma1-sigma_later > 1+2t+143m/480 > 1.          (6)

Every descendant factor is a character, constant, signed point defect or single-phase point defect and obeys H<=4I. In coherent a children the surplus satisfies 4I(G_epsilon(g))-H(G_epsilon(g))>=-2epsilon*E g+(4I(g)-H(g))/2. For different adaptive data trees the mean g is preserved by the physical martingale; the two original a signs cancel their bias in expectation. With the retained b=0 terminal, the COMPLETE final surplus S=E(4I-H)>=1. Unselected prefix leaves satisfy the same original sector bound. Define e_hist=H0-Hf-4(I0-If). Keeping all terminal references and erasure/outcome KL, exact signed ownership is

S-[A0+e_hist+sigma1+sigma_later]_+-omega
 =min(S,M0-sigma1-sigma_later)-omega >=3/4,          (7)

for the SAME eligible prior debit 0<=omega<=1/4. No source is renewed. This extension is conditional on the identified A036 point-factor theorem and the prior factor-prefix lift/variance lemma; it does not admit arbitrary incoming references.

## 4. Honest frontier

The all-dimensional sign theorem (4)-(5) is self-contained modulo the explicitly reconstructed normalized identity. The hereditary owner consequence (6)-(7) additionally uses A036's point-factor theorem and A039's earlier prefix lift/variance proof; external review is pending. The first unsupported universal line is an influence-priced arbitrary-Boolean initial supplier with cumulative normalized transport that avoids nonsummable refreshes. A036/A040's rare-query two-defect geometry is not covered by the four equal small masses used in section 2; A037 prohibits rescuing unlimited whole-core refreshes using a bounded ancestor surplus. No universal FEI constant improves. The shortest next mechanism is a block-aware supplier on A037's actual tensor, with any conversion paid from its diminished owner, rather than extending the disproved whole-core rule.
