# P0162: exact statement for an independent first attempt

For n >= 1 equip {-1,1}^n with uniform product probability. For a Boolean f:{-1,1}^n -> {-1,1}, define chi_S(x)=product_{i in S} x_i and fhat(S)=E[f chi_S]. Parseval gives sum_S fhat(S)^2=1. Use logarithms to base two, with 0 log2(1/0)=0.

H(f)=sum_{S subset [n]} fhat(S)^2 log2(1/fhat(S)^2).
I(f)=sum_{S subset [n]} |S| fhat(S)^2=sum_i Pr[f(x) != f(x with bit i flipped)].

Target: Does an absolute finite constant C exist such that H(f) <= C I(f) simultaneously for all n and all such Boolean f?

No monotonicity, balance, symmetry, degree, formula-size, or coordinate-independence hypothesis is part of the target. A bound whose C depends on n or a complexity parameter is a special case, not the full target. Constant functions have H=I=0. This packet contains the statement only; no proposed route or proof is supplied to the adversary.

Primary statement checked: Gonzalez, MacManus and Pereyra, arXiv:2606.00246v1, Introduction, definitions and FEI Conjecture, https://arxiv.org/html/2606.00246v1 . Historical originating citation: Friedgut and Kalai (1996), DOI 10.1090/S0002-9939-96-03732-X; original PDF access not yet recovered.

Current openness: UNKNOWN pending completion of owner solved/retired and current primary-source checks. No novelty claim.


P0162 was tier 5/attempted_un on 7 September. Its exact brain attempt card explains why entropy-versus-cardinality alone fails: the uniform singleton law is not a Boolean squared spectrum. H/I targeted searches found no separate target records. The cited F0090 memo claims a percolation-crossing subclass using arm probabilities and dyadic boxes; those geometric hypotheses do not apply to arbitrary Boolean f. It is not used as a proof input here.

The live brain returned six target-related cards, including read-once-formula and linear-threshold results. A read-once representation or a threshold representation is an additional hypothesis; neither theorem supplies a general FEI bound. Their memory verification labels are not independent audits performed in this session. The directly useful card is claim_d15d0160e58b4c9183707be9f49462d2: its large-influence restriction bound exactly matches the elementary bound proved here, and its source memory already refutes arbitrary-coordinate lifts in the small-influence regime. The present result provides a transparent alternative bent/iterated-majority witness and a simultaneous global constant-4 bound. No record-function or majority-point-flip computation from the old work was repeated.

The mathematical gap is a dimension-free aggregate conditional-entropy budget over complete restriction trees. The good-coordinate condition is sufficient but is not asserted to follow from FEI. The arbitrary-coordinate condition is false. Current global openness and novelty are not certified.

# Exact bridge checkpoint (own deductions; independent check pending)

Use the notation and uniform Boolean assumptions of STATEMENT.md. Split f on coordinate i and write a_S=hat(f+)(S), b_S=hat(f-)(S), P_S=a_S^2, Q_S=b_S^2, R_S=(P_S+Q_S)/2. All are indexed by subsets of the remaining coordinates. P,Q,R are probability distributions. For R_S>0 set q_S=(a_S-b_S)^2/(2(a_S^2+b_S^2)); zero-weight terms are zero. Let h be binary entropy in bits and t=I_i(f)=sum_S (a_S-b_S)^2/4=sum_S R_S q_S.

Direct entropy chain rule gives, exactly,

Delta_i(f)=H(f)-(H(f+)+H(f-))/2 = JS(P,Q)+B_i(f),
JS(P,Q)=H(R)-(H(P)+H(Q))/2,
B_i(f)=sum_S R_S h(q_S).

Proof: parent squared coefficients without/with i are (a+b)^2/4 and (a-b)^2/4, with common marginal R. Thus H(f)=H(R)+sum R h(q). Subtract average child entropy. Jensen-Shannon divergence is nonnegative. Consequently B <= Delta. In particular Delta is not identically B.

Own two-variable witness: f(x,z)=x when z=+1 and 1 when z=-1. Both restrictions are characters/constants, with disjoint single-atom Fourier spectra. Four parent squared coefficients equal 1/4: H(f)=2, average child entropy=0, t=1/2, B=1, JS=1. Any quoted identity Delta=B fails on this Boolean witness.

Rare-switch construction: on m=2k binary bits, g(x)=(-1)^(sum_{j=1}^k x_(2j-1)x_(2j)), with the usual Walsh characters (-1)^(S dot x). Let h=g-2*1_{x=0}; g(0)=1, so h is Boolean. Let F(x,z)=g(x) for z=+1 and h(x) for z=-1. The new coordinate has t=2^-m. Product of k two-bit Walsh transforms gives |ghat(S)|=2^-k for every S. Parent coefficients are ghat(S)-2^-m without z and 2^-m with z. Put N=2^m, epsilon=N^-1/2. The marginal R_S=(sigma_S epsilon-epsilon^2)^2+epsilon^4 >= epsilon^2/2 for k>=1, so q_S=epsilon^4/R_S <=2/N. Hence

B_z(F) >= sum_S R_S q_S log2(1/q_S) >= (m-1)/N,
Delta_z(F)/I_z(F) >= m-1.

This is a proof for all k, conditional only on the explicitly proved flat Walsh transform. It refutes a universal bound for every arbitrary splitting coordinate. It does not refute FEI, nor the existence of a good coordinate. No monotonicity is claimed for this construction. Exact source comparison and independent referee review remain pending.

Single hardest remaining piece: prove a dimension-free conditional entropy charge B_i <= K I_i for a suitable coordinate at every recursive restriction, or an amortized complete-tree analogue. Bounding B_i by h(I_i) retains the logarithmic loss and does not close the conjecture.


# Universal entropy-increment bound and exact remaining budget

Uniform Boolean assumptions and notation are as in BRIDGE_CHECKPOINT.md. Everything here is an independent elementary derivation of known bounds; no novelty claim.

For two nonnegative numbers x,y, put r=x+y. Their one-index Jensen-Shannon contribution in nats is j(x,y)=(x ln(2x/r)+y ln(2y/r))/2, with continuous zero conventions. Then

j(x,y) <= (sqrt(x)-sqrt(y))^2/2.

Proof: when r>0 write u=(x-y)/r and use symmetry to assume u in [0,1]. The inequality is equivalent to (1+u)ln(1+u)+(1-u)ln(1-u) <=2(1-sqrt(1-u^2)). Both sides vanish at zero. The derivatives are 2atanh(u) and 2u/sqrt(1-u^2). The latter is larger because atanh(u)=integral_0^u (1-v^2)^-1 dv <=integral_0^u (1-v^2)^-3/2 dv=u/sqrt(1-u^2). Extend to u=1 by continuity. The case r=0 is immediate.

Apply this with x=a_S^2 and y=b_S^2. Since (|a|-|b|)^2 <=(a-b)^2, summing and converting nats to bits gives

0 <=JS(P,Q) <=(1/(2ln2)) sum_S(a_S-b_S)^2=(2/ln2) I_i(f).

Binary entropy is concave and R is a probability distribution, so B_i=sum R h(q)<=h(sum Rq)=h(I_i). Consequently,

B_i <=Delta_i=B_i+JS <=B_i+(2/ln2)I_i <=h(I_i)+(2/ln2)I_i.

For t>0, h(t)<=t log2(1/t)+t/ln2, since -(1-t)ln(1-t)<=t. Thus Delta_i <=t[log2(1/t)+3/ln2]. This loses log(1/t); it is not a full FEI proof. For a chosen coordinate with t>=tau>0, it gives Delta_i <=[log2(1/tau)+3/ln2]t. This matches the small-influence reduction card retrieved from the brain (its printed constant is 2/ln2+log2(e/tau)).

If B_i<=K I_i at the selected split, then Delta_i <=(K+2/ln2)I_i. Conversely Delta_i<=K I_i implies B_i<=K I_i. Constant changes must be retained; Delta_i is not B_i.

An exact full-tree form identifies the single remaining mathematical budget. Let T be any finite adaptive restriction tree ending in constant functions, with each internal node v at depth d(v) splitting an unfixed coordinate i(v), and let w_v=2^-d(v). Telescoping the identities H(f_v)=average_child H+Delta_v and I(f_v)=average_child I+I_i(f_v) gives

H(f)=sum_{v internal} w_v Delta_v,
I(f)=sum_{v internal} w_v I_i(f_v),
sum_v w_v B_v <=H(f)<=sum_v w_v B_v+(2/ln2)I(f).

Thus a dimension-free bound sum_v w_v B_v <=K I(f) would prove FEI with constant K+2/ln2. FEI with constant C would imply this budget for every complete tree with constant C. Unlike a per-node good-coordinate assertion, this aggregate condition is equivalent to FEI up to an additive change in constant. Uniform product measure gives the weights; there is no multiplication of conditional probability bounds.

The hardest gap is this dimension-free aggregate conditional-entropy estimate for Boolean spectra. No such estimate is supplied. The rare-switch lemmas explain why replacing it by a bound at an arbitrary coordinate fails, even after reducing to small influences.


# Bad coordinate persists in the all-small-influence regime

Own deduction, no novelty claim. Independent review pending. This extends the rare-switch checkpoint; it concerns one bad coordinate, not every coordinate.

Fix any tau>0. Choose an odd r=2l+1>=3 such that alpha=binom(2l,l)/2^(2l)<=min(tau,1/2). This is possible: alpha=product_{j=1}^l(1-1/(2j)) <= exp(-sum_{j=1}^l 1/(2j)) <=1/sqrt(l+1). Let G be majority on r uniform sign bits. It is balanced; every physical influence is alpha. If a chosen input v is fixed to +1 or -1, then E[G+]=alpha and E[G-]=-alpha. Indeed G is monotone, E[G]=0, and E[(G+-G-)/2]=Inf_v(G)=alpha.

Let F_m(x,z) be the rare-switch Boolean function of BRIDGE_CHECKPOINT.md, for m=2k, k>=1. Replace all m+1 inputs by independent, disjoint copies of G, forming f_m=F_m(G_1,...,G_m,G_0). Disjointness is essential. Each physical influence is Inf_j(F_m)*alpha <=alpha<=tau. To verify the product, condition on all other blocks: changing a bit in block j changes the output exactly when that bit changes G_j and the outer function is pivotal for j. The outer pivotality event depends only on the other blocks, so the two events are independent. The selected physical bit v in block G_0 has influence t=alpha/N, N=2^m.

Write epsilon=N^-1/2. The outer decomposition is F_m=A(x)+z B(x), with Ahat(S)=sigma_S epsilon-epsilon^2 and Bhat(S)=epsilon^2. The sigma_S are signs from the bent function. For a Fourier index U in the m other gadget blocks, let S be its set of nonempty blocks. Since G is balanced and the blocks are disjoint,

Ahat'(U)=c_U Ahat(S), Bhat'(U)=c_U Bhat(S),
c_U=product_{j in S} Ghat(U_j), and sum_{U: active blocks S} c_U^2=1.

The last equality is Parseval on each balanced gadget and finite factorization on independent product blocks, not a multiplication of dependent conditional estimates.

Consider only the Fourier indices whose remaining selector-block coordinates are empty after splitting on v. The two restriction coefficients are c_U(Ahat(S)+alpha Bhat(S)) and c_U(Ahat(S)-alpha Bhat(S)). Their marginal is R_U=c_U^2(Ahat(S)^2+alpha^2 Bhat(S)^2); their coordinate probability is q_U=alpha^2 Bhat(S)^2/(Ahat(S)^2+alpha^2 Bhat(S)^2) whenever c_U!=0. As epsilon<=1/2,

Ahat(S)^2 >=epsilon^2/4, so q_U<=4alpha^2/N<=1/N.

This sector alone contributes at least

sum_U R_U h(q_U) >=sum_U alpha^2 c_U^2 Bhat(S)^2 log2(N)
=alpha^2 m/N.

The exact entropy identity gives Delta_v(f_m)>=B_v(f_m), and therefore

Delta_v(f_m)/Inf_v(f_m) >=alpha m.

Since alpha is fixed after tau is chosen and m tends to infinity through the even integers, no dimension-free arbitrary-coordinate restriction bound holds even on the class in which all individual influences are <=tau. The construction is Boolean throughout. No monotonicity, universal badness over all coordinates, or counterexample to FEI is asserted.

NEXT: Referee must check the disjoint-block factorization and the empty-selector Fourier sector; then use this lemma only to block an arbitrary-coordinate lift of the brain's small-influence reduction.


# Explicit all-small-influence family: bad local split, global FEI constant 4

Own derivation, independent review pending, no novelty claim. This is a proved special family, not a solution of P0162.

Let M_3 be majority of three uniform sign bits. Its only nonzero Fourier coefficients are the three singletons (1/2 each) and the triple (-1/2). Hence it is balanced, H(M_3)=2, I(M_3)=3/2, and each individual influence is 1/2. Define G_d recursively as M_3 applied to three disjoint copies of G_(d-1), with G_0 a dictator. Every G_d is balanced and monotone, every leaf influence is alpha=2^-d, and

I(G_d)=beta=(3/2)^d,
H(G_d)=4(beta-1).

Here are the composition identities used to prove those formulas. If an outer Boolean F has k inputs and the k substituted gadgets are disjoint balanced Boolean copies of G, then

I(F(G,...,G))=I(F) I(G),
H(F(G,...,G))=H(F)+I(F)H(G).

Proof: balance forces every nonzero gadget coefficient to be on a nonempty subset. A physical Fourier subset therefore identifies its outer active-block set S uniquely. Its coefficient is Fhat(S) times the product of the gadget coefficients in the active blocks. Conditional on S under squared coefficients, the block spectral subsets are independent with the gadget's squared-coefficient law; Parseval normalizes each block. The entropy chain rule gives H(F)+E|S|H(G), and expected physical subset size gives E|S|I(G). This finite product factorization is valid specifically because the blocks are disjoint and balanced. Applying it to M_3 gives I(G_d)=(3/2)I(G_(d-1)) and H(G_d)=2+(3/2)H(G_(d-1)), proving the formulas. Leaf influences multiply by 1/2 at each level; this also follows directly by conditioning on the other disjoint branches.

Take the rare-switch outer function F_m of BRIDGE_CHECKPOINT.md, with m>=2 even, N=2^m. Its entropy is at most m+1, because it has at most 2^(m+1) Fourier outcomes. Its exact influence is

I(F_m)=m/2+(m+1)/N.

Proof: each original coordinate of the quadratic bent g is pivotal with probability 1/2. At zero and each unit vector g=+1. Flipping g only at zero to obtain h adds one previously nonpivotal edge for each coordinate, hence Inf_j(h)=1/2+2/N. Averaging the two restrictions gives Inf_j(F_m)=1/2+1/N; the selector has influence 1/N. Thus I(F_m)>=m/2 and H(F_m)<=m+1<=3m/2<=3I(F_m).

Define f_(m,d)=F_m(G_d,...,G_d) on (m+1)3^d physical bits. The composition identities give

H(f_(m,d)) <=I(F_m)[3+4(beta-1)]
=(4-beta^-1)I(f_(m,d)) <=4I(f_(m,d)).

All physical influences are at most alpha=2^-d. For any chosen selector-block leaf v, E[G_d+]=alpha and E[G_d-]=-alpha by balance and monotonicity, so the empty-selector-sector argument in SMALL_INFLUENCE_OBSTRUCTION.md applies unchanged:

Inf_v(f_(m,d))=alpha/N,
Delta_v(f_(m,d))/Inf_v(f_(m,d))>=alpha*m.

Consequently, for every tau>0 and M>0, choose d>=1 with 2^-d<=tau and even m>=max(2,M*2^d). This gives a Boolean f with all influences <=tau, with some coordinate restriction ratio >=M, and with H(f)<=4I(f). These three conclusions hold simultaneously.

This quantifier-preserving witness blocks a false arbitrary-coordinate lift of the brain's small-influence reduction. It leaves the existential good-coordinate route and the aggregate conditional-entropy budget open.

NEXT: Independent referee checks balanced block composition, the exact outer influence count, and the empty-selector sector. The unresolved target step remains the aggregate conditional-entropy estimate for arbitrary Boolean functions.


Verification command: python -X utf8 ~/brain_workers/w513/verify_bridge.py . Receipt: verification.json. These are arithmetic checks, not a formal proof or an independent audit.
