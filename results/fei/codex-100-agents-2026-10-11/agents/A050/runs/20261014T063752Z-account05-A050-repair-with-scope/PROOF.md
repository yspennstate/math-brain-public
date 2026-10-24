# Conditional likelihood-envelope repair

Finite normalized laws, bits, with all inherited references retained. This is a local repair of the nonmatching conditional-KL payment, not a universal FEI proof.

## 1. The support-complete envelope

Erase queried frequency i from actual Fourier law p to obtain p_e(t,z), and from a complete dominating reference q to obtain q_e(t,z). Apply the SAME actual coherent branch kernel K_b=p_b/(2p_e), and a fixed normalized fallback on source-zero rows, to both. Set P(b,t,z)=p_e K_b, Q(b,t,z)=q_e K_b. Thus P_B is fair. On the FULL reference support put r(t,z)=p_e/q_e, allowing zero. For each occupied row (b,t), put

    m_bt = sum_z Q(z|b,t) r(t,z) = P(b,t)/Q(b,t),
    A_bt = max_{Q(b,t,z)>0} r(t,z)/m_bt,
    V_bt = sum_z Q(z|b,t) r(t,z)^2 / m_bt^2,
    B = sum_(b,t) P(b,t) log2 min(A_bt,V_bt).

Both A,V are finite and >=1. There is NO positive lower-likelihood hypothesis and no equality-of-support hypothesis. Reference-only atoms remain in the means and in V; they have r=0.

The actual child conditional likelihood is ell=r/m_bt. Therefore

    C_child = sum_(b,t) P(b,t) E_(P(Z|b,t)) log2 ell
            <= B.

Indeed log ell<=log A pointwise, and concavity of log gives E_P log ell<=log E_P ell=log V. One may choose the smaller certificate separately in every row. No entropy-drift credit or new source-KL bank is used. B=0 iff every occupied child conditional matches its inherited reference: A=1 or V=1 forces ell=1 Q-almost surely, including reference-only atoms. Conversely matching gives both 1. This includes A047's disjoint-component exceptions and A083's support-complete graph criterion.

The useful additional hypothesis is the AGGREGATE envelope condition B<=K Inf_i(f), for one fixed K across intended queries. It implies C_child<=K Inf_i. It is weaker than demanding pointwise matching, bounded two-sided likelihood ratios, or paying each row with the same fraction of influence. It is the weakest condition expressible by this particular sum of rowwise max/second-moment certificates, not a claim of an absolutely weakest hypothesis among all possible repairs. Unlike assuming the desired KL inequality, B depends only on rational extrema and moments of the erased likelihood and normalized channel, without evaluation of conditional KL. For a stopping tree the reach-weighted bound sums to K times removed physical influence, provided each transaction concerns the chosen inherited reference and is booked once. Fresh resets, quotient debt and terminal entropy still require their own signed accounts; summing this bound does not make their charges free.

## 2. Nonzero mismatch with a uniform influence price

Use A047's actual selector: f_r=+1 on B=0, and h_r on B=1, where h_r is parity on r>=2 bits with its sign at one vertex flipped from -1 to +1. Let mu=2^(1-r), a=mu^2<=1/4. Influence of B is (1-mu)/2. The erased empty-frequency mass is (1+a)/2. Choose q_e(empty)=alpha=1/4 and distribute remaining reference mass proportionally to actual nonempty masses; lift using the source conditional law of queried frequency. This is the declared reference, not a canonical occupancy assertion.

Actual child0 is constant and its envelope is zero. Actual child1 has empty mass a; its inherited empty mass is beta=a/(3+4a). This follows directly by transporting K_1(empty)=a/(1+a), K_1(nonempty)=1. Thus

    V_1 = a^2/beta+(1-a)^2/(1-beta)
        = 1 + 4a(1+2a)^2/[3(1+a)] <= 1+(12/5)a.

The coefficient is increasing for 0<=a<=1/4, with maximum 12/5. Hence

    C_child <= B <= (1/2)log2 V_1
            <= 6a/(5 ln2) < 2a <= 2 Inf_B(f_r).

Here ln2>3/5 follows from the positive first two atanh terms, 2/3+2/81>3/5. The final inequality is 2mu^2<=1-mu for 0<mu<=1/2. This proves the additional hypothesis with K=2 for EVERY r>=2, with genuinely nonmatching inherited children and quadratic decay in their mean. Full terminal H is H(h_r)/2 and terminal influence r(1-mu)/2; neither is discarded. At the extreme tilt alpha=1-a^2, beta=1-a, actual C_child=((1-2a)/2)log2((1-a)/a)~r-1 whereas Inf_B tends to1/2. Since B>=C_child, no uniform envelope condition survives. This preserves A047's obstruction and identifies precisely which intended reference family fails.

## 3. Canonical exposed priority gate, with ghost rows

Use actual F(x,a,b,y)=(-1)^a if x=0; otherwise 2y-1 if b=1, otherwise +1. Query b, retain T=(S_x,S_a), spectator Z=S_y, and fair fallback. Direct Walsh reconstruction gives root H=3, I=3/2, Inf_b=1/4. Actual children both have H=2 and influences 1,3/2; their unused mean rate-four surplus is 3.

The complete canonical occupancy reference has Q(empty)=1/16 and Q(nonempty)=(15/16)/c times product Bernoulli parameters (8c/15,8c/15,4c/15,4c/15). Its unique positive normalizer solves 1-c=(1-8c/15)^2(1-4c/15)^2, and 3/4<c<13/16. Normalization and uniqueness: g(c)=ln(1-c)-2ln(1-8c/15)-2ln(1-4c/15), g(0)=0, g'(0)=3/5; g''<0 since sum r_j^2=32/45<1 and r_j/(1-r_j c)<=r_j/(1-c). g tends to minus infinity, so exactly one positive zero. Rational polynomial signs give the stated bracket.

In occupied rows with S_a=1, actual Z=0, inherited Q(Z=1|b,t)=tau=4c/15. Reference-only Z=1 rows are retained. Their likelihood is zero and ell(0)=1/(1-tau), so A=V=1/(1-tau). These rows have total physical weight1/2. Rows with S_a=0 are deterministic and matched under both laws, so their A=V=1. Consequently

    B=C_child=-(1/2)log2(1-4c/15) < (1/2)log2(60/47) <3/16.

Last sign is the integer inequality 60^8<8*47^8. Thus the hypothesis holds with K=3/4: C_child<(3/4)Inf_b. This independently reconstructs A083's existing conditional formula/payment, rather than claiming a new fixture. If the certified mean child surplus is chosen as sole owner, withdraw this exact B once: less than 1/16 of that owner, with both terminal entropies retained. An alternative query-influence price cannot be counted as a second refund. The envelope is EXACT here, so no universal smaller envelope bound can improve this particular source/reference row.

## 4. Same inherited reference through the next y query

Continue ONLY the b=1 child, leaving b=0 as a complete terminal. Let theta=8c/15 and tau=theta/2. At b=1 the source has four atoms {a},{x,a},{y},{x,y}, each of mass1/4. In the inherited reference, all rows with a present have the original occupancy product mass multiplied by 1/2 (including reference-only y atoms); rows with a absent and y present have multiplier1; rows with a and y absent have multiplier0. The empty-atom exception is therefore absent from this child. After erasing y, the inherited reference is exactly product Bernoulli(theta) on S_x and Bernoulli(eta) on S_a, where

    eta = (theta/2)/[theta/2+(1-theta)tau] = 1/(2-theta).

This comes from the SAME root reference; no new normalizer, root bank or reset is introduced. Actual erased law is uniform on the four x,a masks. Both physical y children also have that uniform spectrum, so K_y=1/2 everywhere on the erased reference support. Hence outcome KL is zero, and the inherited terminal reference is that same product. Query influence in this b=1 child is1/2. Take S_a as spectator and S_x as retained quotient. Conditional KL and envelope are independent of x:

    V=(2-theta)^2/[4(1-theta)],
    C_y= D_2(Ber(1/2)||Ber(eta))=(1/2)log2 V,
    B_y=log2 V.

The max envelope is at least this second-moment envelope, so the minimum used in Section1 really is V. Since V=1+theta^2/[4(1-theta)] increases on (0,1), theta<13/30 implies V<2209/2040. Integer comparison 2209^8<2*2040^8 gives B_y<1/8 and C_y<1/16. Thus the new envelope hypothesis holds at price K=1/4 times this query's influence. With its reach1/2, the conservatively booked total envelope is

    B_b+(1/2)B_y <3/16+1/16=1/4.

The earlier b withdrawal remains booked in full, even though y-erasure releases some previously charged conditional debt. This released amount is NOT recycled as another owner. The new S_a conditional component belongs to the previously unpaid b=1 quotient debt, not to a fresh root reference. Each of the three final actual leaves (b=0, or b=1 followed by either y value) has H=2,I=1, so final mean S4=2. Original mean b-child S4=3 partitions EXACTLY into a distinct y-query edge reserve 4*(1/2)*(1/2)=1 and final S4=2: child/terminal entropy decrements are zero. Pay both booked conditional envelopes solely from the final S4=2 portion, leaving >7/4 of that SAME portion; the query-edge reserve1 is not simultaneously counted as terminal surplus. This is an explicit partial allocation with all complete terminal entropies retained. Remaining S_x quotient KL, the b=0 quotient debt, source erasure/outcome costs and any future reset are still not paid by this allocation. No ownership assertion beyond this declared unused actual rate-four certificate is made.

## 5. Independent reconstruction of A047 boundary audit

Source A047-INHERITED-CONDITIONAL-LIKELIHOOD-BOUNDARY-AUDIT@1, statement hash efa7c3469dd8d1d5b48045fe1f14c233eb5ad071c2997391f64346db2262158e, is accepted unchanged at its stated common-support scope. This review does not attribute the new envelope repair to its author.

Reconstruction: on common erased support r>0 and child likelihood is 2Q_B(b)r. At fixed T, matching conditionals is constancy of r on each branch support. The branch supports are graph cliques; their intersections propagate constants, giving exactly the connected-component condition. An atom with both branch probabilities positive joins the two cliques. For AND2 sign queried at its first bit, erased spectral law is uniform, branch0 constant and branch1 character. Tilting q_e to (1/4,3/4) yields r=(2,2/3), but each branch has one atom, so both inherited children match exactly. The source KL is paid in outcome KL, not deleted.

For general conditional erased rows the joint conditional likelihood P(B,Z|T)/Q(B,Z|T) equals P(Z|T)/Q(Z|T), since the same K is used. Conditional chain rule therefore splits source conditional KL exactly into branch conditional KL plus mean inherited-child conditional KL. No extra bank appears. Section2 independently derives A047's beta and both exact reference families from the actual full-support selector. At alpha=1/4, natural-log expansion yields a ln3 from the empty atom and -2a/3 from the other atom, hence the source coefficient (ln3-2/3)/(2ln2); ln3>2/3 by integrating 1/t. At alpha=1-a^2, beta=1-a, yielding the stated exact divergence. Since a=2^(2-2r), log2((1-a)/a)=2r-2+o(1), so C_child=r-1+o(1). Inf=(1-mu)/2 tends to1/2. The r6 integer certificate and full terminal budgets are reconstructed in the targeted checker. Root likelihood lift preserves queried conditional law, so erasure KL is0; transport retains root KL exactly as outcome plus full child KL. The growing source KL is a reference liability and does not refute FEI. These formulas prove all-dimensional limits rather than extrapolating the finite r=2..8 checks.

## 6. Scope and first unsupported line

Admitted: all matched conditional-kernel applications previously accepted; A047's disjoint balanced branch example; its regular alpha=1/4 full-support parity perturbations in every dimension; and the specified canonical b-query gate including reference-only rows, continued through its actual y query with the SAME inherited reference and the b=0 terminal retained. Excluded: A047's extreme tilt for a uniform K, and any arbitrary reference/reset asserted paid by positive entropy drift alone (A092's four-bit certificate). The proof concerns INHERITED conditional references; a newly projected child reference can incur another signed conditional reset.

FIRST UNSUPPORTED universal line: prove the same aggregate envelope condition, or fund its failure from a genuinely unused signed child/source account, for the prescribed next mixed priority query while preserving the quotient/conversion debt and both complete terminal continuations. Neither this local hypothesis nor the canonical fixture supplies a universal source bank.
