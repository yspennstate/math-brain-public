# A second prescribed reference uses the same original owner

Uniform-cube normalized Walsh spectra, Boolean sign outputs, and base-two entropy are used throughout. This proof concerns a specific paid reference and a specified next reset. It is not a universal FEI payment.

## 1. Source, history and references

For every integer L>=1 let X2,X3 have L private bits each, with distinct physical bits x,a,b,c. Set E1={x,a,c}, E2=X2 union{a,b}, E3=X3 union{b,c}, and f_L=2 product_j(1-1_(E_j=0))-1. The ORIGINAL owner is

    W=17 I_private(f_L), private={x} union X2 union X3.

Debit the original oriented erasure M(f_L)=sum_i sum_T p(T+i)log2[(p(T)+p(T+i))/p(T+i)]. Query x and let p_s be the two actual child squared spectra, at physical reach1/2. A031 prescribes Q_s=fair_b(marg_b p_s), meaning both b-frequency labels receive half their actual row mass. Its source statement is

    M(f_L)+B_x(f_L)+E_s CE(p_s,Q_s) < W-1/16.       (A)

The next physical query is b in BOTH parents p_s. Write p_(s,t) for the four actual children, each of original reach1/4. Prescribe, without optimization,

    Q'_(s,t)=fair_a(marg_a p_(s,t)).

Every law is complete and normalized. The new target is

    M(f_L)+B_x(f_L)+E_s B_b(p_s)
         +E_(s,t) CE(p_(s,t),Q'_(s,t)) < W-1/32.    (B)

Both x branches and both b branches remain, including the constant (x,b)=(1,1) child. No private child reserve is renewed.

## 2. Exact signed conversion and the released fair flag

For any actual Boolean p with current Q=fair_b(marg_b p), let pbar=marg_b p. Physical children have amplitudes u+v and u-v, so their squared laws average to pbar, with the signs added BEFORE squaring. The carried incoming reference after b is exactly pbar, rather than a freshly normalized child law.

The already supplied full cross entropy is

    CE(p,Q)=H(p)+1-B_b(p).

The exact conditional KL released by querying b is

    K_old=sum_T pbar(T) D(p(b|T)||fair)=1-B_b(p).

The reference conservation equation is

    CE(p,Q)=B_b(p)+E_t CE(p_t,pbar)+K_old.

Let J_b=H(pbar)-E_t H(p_t)>=0 be the physical phase channel. For the prescribed fresh a-reference,

    Delta_new=E_t[CE(p_t,Q'_t)-CE(p_t,pbar)]
             =1-E_t B_a(p_t)-J_b.                  (1)

The change in the COMPLETE bill, including the newly booked b erasure, is therefore

    N=B_b(p)+E_t CE(p_t,Q'_t)-CE(p,Q)
      =B_b(p)-J_b-E_t B_a(p_t)
      =Delta_new-K_old <= B_b(p).                  (2)

These are generic reference identities for normalized physical-child laws, not new Booleanity inequalities. They do not say a fresh reset is free: Delta_new can be positive while K_old pays most of it. In particular, one cannot count K_old again after booking the new terminal cross entropies. For the family here, both b queries have positive influence at every finite L. Indeed, the physical event a=1,c=0,X3=0 has probability2^(-L)/4>0, makes E1 and E2 inactive, and makes the output toggle with b, for BOTH values of x and every assignment of X2. All denominators are used only at positive mass; a zero actual mass can retain positive reference mass.

## 3. Independent review of the old owner

A031-TRIANGLE-SAME-ORIGINAL-BANK-WEAK-RESET v1 states (A). Its finite part is re-evaluated independently for L1..15 by a new compressed-coordinate implementation, and checked against direct Boolean character sums for L1,2,3. No source helper is imported. The all-width analytic chain is reconstructed as follows.

Put q=2^-L and let h be the three-bit point defect on {x,a,c}, padded by dummy coordinates. The two extra clauses trigger with total probability at most q/2, giving |hat f-hat h|<=q and squared spectral mass outside the eight core labels <=2q. On the eight core labels squared masses move by <=3q, with interpolated masses >=1/64 for L>=16. Entropy derivatives are <8, so the core entropy error is <=192q and the tail entropy is <=(6L+6)q. Thus H(f)<=H(h)+(6L+198)q.

For F(u,v)=v log2(1+u/v), on these positive core rows |partial_u F|<3/2 and |partial_v F|<8. Four rows for each of x,a,c cost <=342q in total; off-core rows cost <=6q. The other2L+1 coordinates have influence <=q and M_i<=h2(Inf_i)<=q(L+3/2). Hence

    H(f)+M(f)<=H(h)+M(h)+(2L²+10L+548)q.

The source energy is at least1/4-q/4. The physical x-channel retains the empty-label discriminator: its two output probabilities differ by >23/32 for L>=16. The midpoint Jensen gap for h2 is > (23/32)²/2>1/4, since h2''<=-4. Therefore the old bill is at most

    H(h)+M(h)+3/4+(2L²+10L+548)2^-L.

The polynomial times2^-L decreases for L>=16 because 2P(L)-P(L+1)=2L²+6L+536>0. At L16, P=1220. The rational-log endpoint check verifies

    17(1/4-1/262144)-[H(h)+M(h)+3/4+1220/65536] >1/16,

where H(h)=-(9/16)log2(9/16)+(7/16)*4 and M(h)=(3/16)log2(10)+9/16. The source proof's original finite and tail bounds require no repair. The unchanged all-L statement (A) is independently accepted at its stated triangle/reference scope; it supplies no universal admission theorem. Its no-reset continuation is the standard conditional-KL identity, not an additional unpaid lemma.

## 4. All-width second-reset payment

The physical influence telescope gives E_s Inf_b(p_s)=Inf_b(f_L)=3q/4-q²/8<q. By concavity and monotonicity of binary entropy,

    E_s B_b(p_s)<=h2(Inf_b(f_L))<q(L+3/2), L>=16.

The binary entropy upper bound follows from -(1-q)ln(1-q)<=q and ln2>2/3. The latter follows from the positive atanh series at1/3. The function 2^-L(L+3/2) decreases; at L16 it is35/131072. Combining (A) and (2), the NEW spare is strictly greater than

    1/16-35/131072 =8157/131072 >1/32, L>=16.        (3)

For L1..15 (B) is a finite exact rational-log certificate, not numerical evidence. These certificates and (3) establish (B) for every integer L>=1. Boundary costs retain their actual signs.

The fresh reset is genuinely positive in the tail. At (x,b)=(1,1), every clause is inactive and the actual child is constant, so B_a=0, while its prescribed Q' has full cross entropy ONE bit. Every other child has B_a<=1. Thus E B_a<=3/4. The one-bit phase bound gives E_s J_b(p_s)<3 Inf_b(f_L), using2/ln2<3. Equation(1) gives

    E_s Delta_new >=1/4-3 Inf_b(f_L)>1/8, L>=16.     (4)

The positive fresh price is therefore paid by the released fair conditional KL plus the same unused source reserve, with all four full terminals retained. It is not explained away by a negative reset or a dropped constant branch.

## 5. Boolean admission, tensor guard, and limitations

The conversion identities (1)-(2) are generic. The paid initial bank (A), and hence (B), uses the actual signed clause structure. For a precise non-Boolean control take N=2^18 private characters on X2 union X3 (L=2^17), each amplitude1/sqrt(N), and dummy x,a,b,c. This real function has norm one, and BOTH physical queries preserve norm one, because the queried variables are dummies. Its old M and both erasures are zero; I_private=1. Its final fair-a reference has CE=log2(N)+1=19, exceeding the SAME rate17 bank. Nonempty signed convolution at two distinct private labels is2/N, so it violates Booleanity. No truth table at that dimension is allocated.

An untouched Boolean spectator g with supplied reference Q_g retains its entire M(g)+CE(g,Q_g) with coefficient one on BOTH sides of the tensorized account. The triangle reserve does not pay it. The constant final branch retains CE=1, and zero-actual/reference-only rows remain normalized. All sums are finite; no limits, exchanges of infinite sums, or phase-free substitutions are used.

For this spectator extension the supplied references are explicitly Q_s tensor Q_g and Q'_(s,t) tensor Q_g; Q_g need not be the spectator's actual spectrum. The prescribed fair lifts in section1 act only on the triangle factor. This separates the extension from the special choice Q_g=p_g and retains every spectator cross-entropy term.

The first unsupported universal step is an arbitrary signed-core initial admission or a prescribed next reset when the incoming queried-bit reference kernel is nonfair. The exact one-bit release used here is special to the supplied fair kernel; it cannot be renewed by relabeling the next node. NEXT should identify the actual conditional reference capacity at such a nonfair mixed query and price its positive fresh-reference surcharge from the SAME remaining original reserve, preserving old debits and all complementary terminal functions.

## 6. Executed certificate and precision repair

The full fixed domain is L1..15,16,32,64. The first helper used128-bit outward rounding on each atom before multiplying by its nonempty-hit multiplicity. Those intervals remained valid, but at L64 the roughly2^128 multiplicity amplified a per-atom rounding quantum to order one; assertions could not certify the sign. This is not a mathematical counterexample. The failed diagnostic, original helper, original frozen specification and completed checkpoints are retained. V2 evaluates exact multiplicity-weighted log coefficients BEFORE rounding. The domain and runtime cap remain unchanged. Both versions of the frozen reproduction specification are retained; the independent helper rounds separate24-term rational log sums outward to120bits before printing. This changes no sign formula.

V2 main validation passes2806 checks in6.386061s on18widths; independent direct-character reconstruction passes1445 checks in3.248170s. The finite signs establish a positive new reset for L2..15 and a negative boundary at L1; the analytic tail proves positivity for every L>=16. The memory gate refused Lean (3.0GB free,4.0GB required), so only the proposed algebra statement is saved and no formal acceptance is claimed.
