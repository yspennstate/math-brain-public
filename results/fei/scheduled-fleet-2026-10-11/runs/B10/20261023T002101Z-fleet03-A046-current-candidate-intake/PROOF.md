# A paid correlated reset after an actual mixed query

Entropy, cross-entropy and KL are in bits. All inputs are independent fair physical bits. The all-dimensional claim below concerns a specified Boolean family and a specified INITIAL reference; it does not supply that initial price for an arbitrary Boolean function.

## 1. Exact target and original owner

For m>=1,r>=2 let h be the product of m disjoint width-r point-defect signs, each equal to -1 exactly when all its input bits are 1. Put delta=2^-r, t=Pr(h=-1), and define

    F_h(x,a,b,z)=(-1)^a on x=0;
                 h(z) on x=b=1;
                 +1 otherwise.

Let p_r be the factor Fourier law, u_r=p_r(empty)=(1-2delta)^2 and v_r=4delta(1-delta). The ORIGINAL factor reference is

    q_r(empty)=u_r,
    q_r(s)=(7/8)p_r(s)+(v_r/8)1_{s=full}, s nonempty.

The full core reference is q=product q_r. It is normalized, dominates p_h and matches its empty mass. The ORIGINAL full reference Q of F_h copies the six actual zero-data/a-containing atoms, and puts q(s)/16 on each of the four control copies 0,x,b,xb for nonempty data s. Its mass is exactly one. In particular

    A0=D(P_F||Q)=D(p_h||q)/4.

No earlier canonical-product bill is silently converted to this Q. The old debit below is an eligible booking against this specified original account.

Query b first, retain b0, and on b1 use ANY finite adaptive physical DATA-only stopping tree. At any selected frontier leaves, query x OR a once. Both children of each selected query are kept and further physical queries then stop. Leave all unselected leaves inherited. Thus the choice of x/a and selected leaves may depend on physical history, but never on the Fourier set being encoded.

## 2. The original source has unused structural allowance

Write CE(P,Q)=H(P)+D(P||Q). A direct disjoint-sector calculation gives

    H(F_h)=2+H(g)/2, g(b,z)=1 on b0,h(z) on b1.

Erasing b from g gives (delta_empty+p_h)/2. Retaining a fair mixture label bounds its entropy by 1+H(h)/2; its erased-bit conditional entropy is at most one. Consequently

    H(F_h)<=3+H(h)/4,
    CE(P_F,Q)<=3+CE(p_h,q)/4,
    I(F_h)=1+t/2+I(h)/4.

For a width-r point, nonempty entropy is exactly 8(r-1)delta(1-delta). The empty atom contributes at most v_r/ln2, and D(p_r||q_r)<=v_r log2(8/7)<v_r/4. The last sign is exactly 8^4<2*7^4. Also ln2>2/3, so CE(p_r,q_r)<(8r-1)delta(1-delta)<4I(point_r)-delta. Tensor additivity therefore yields

    M0:=4I(F_h)-CE(P_F,Q)>1+2t+m delta/4.       (1)

This last m delta/4 is an UNUSED part of the same original source margin, not an additional influence allocation. Ordinary point-defect entropy satisfies H<=4I including width-one characters and constant restrictions, so the terminal class certificates used next are actual finite Fourier statements.

## 3. Actual terminal surplus after x/a exposure

Every conditional data core g is still a tensor of point-defect signs, characters and constants; its physical restriction is a cylinder with uniform unqueried inputs. For the selector of a fresh character and g, exact formulas give H=2+H(g)/2 and I=1+I(g)/2, so 4I-H>=2.

For an x query the two children are the character and g, with mean surplus at least 2. For an a query Inf_a=1/2 and its entropy drop is nonnegative: it equals erasure entropy plus Jensen-Shannon divergence of the two child spectra. Thus the actual mean surplus of the a pair is at least 0. This is an aggregate paired statement; neither a-child is individually assumed to be a certified FEI leaf.

The retained b0 child has reach 1/2 and surplus 2, contributing one bit. All other selected pairs and unselected active leaves have nonnegative mean surplus. Therefore the COMPLETE final entropy surplus

    S=E_terminal[4I-H]>=1.                         (2)

No reset changes this S, because resets change reference laws, not the Boolean functions.

## 4. Prescribed FULL fresh references

For each remaining point factor of width k>=2, put d=2^-k, v_k=4d(1-d), and prescribe the STRONGER fresh reference

    r_k(empty)=p_k(empty),
    r_k(s)=(6/7)p_k(s)+(v_k/7)1_{s=full}, s nonempty.

For a character or a constant use its exact spectral law. Tensor these factor laws to r_g. They match p_g(empty), are normalized and dominate the actual source. The initial 1/8 tilt is not renewed: this new 1/7 tilt is an explicitly charged target. Its factor KL satisfies

    D(p_k||r_k)<=v_k log2(7/6),
    log2(7/6)<1/4, since 7^4<2*6^4.                (3)

After x, RESET ONLY the x1 core-bearing child to r_g embedded with zero dummy-frequency masses. The x0 character child remains on its inherited full law. After a=c is exposed, each child is a selector J(c,g) on x and the remaining data, with c in {+1,-1}. Its nonempty-data probabilities are p_g(s)/4 on two control copies 0,x, and its zero-data probabilities are (c+Eg)^2/4,(c-Eg)^2/4. Copy these two actual zero-data masses and replace nonempty p_g(s)/4 by r_g(s)/4. This is a FULL normalized reference, with

    D(P_J||R_J)=D(p_g||r_g)/2.                    (4)

RESET BOTH a-children to these specified laws. There is no optimization per spectral atom and no omitted reference normalizer. Source-zero rows in the incoming law are retained until the explicit reset; their removal or redistribution at that reset is included in its signed KL change. For characters, constant factors and zero empty mass, the definitions above use no division and require no limiting convention beyond 0 log 0=0.

## 5. The adaptive variance bound pays every selected reset

Let H_j be the jth original point sign and let L denote the finite data-only frontier. The observations can be adaptive and can stop at unequal depths. Its leaf events are disjoint cylinders partitioning the fair data cube, so

    E Var(H_j|L)=1-E(E[H_j|L]^2)<=1-(E H_j)^2=v_r.

The exact lost variance is E[(E[H_j|L]-E H_j)^2]>=0. This finite sum identity avoids any optional-stopping or limit assumption. It remains valid when data observations are chosen from several factors adaptively; no independence between L and H_j is assumed.

At an x exposure only one child is reset, at half the active leaf's reach, with KL D(p_g||r_g). At an a exposure both children are reset, but each has KL half that value by (4). In both cases the total freshly introduced KL is half the active leaf reach times D(p_g||r_g). The b1 reach is another half. For ANY selected subset and arbitrary x/a choices, the COMPLETE fresh KL cost T therefore satisfies

    T <= (1/4) log2(7/6) E_L sum_j Var(H_j|L)
      <= (1/4) log2(7/6) m v_r
       = m delta(1-delta) log2(7/6)
       < m delta/4.                              (5)

The unselected leaf contribution is simply zero and all terms are nonnegative. The input to the variance bound is the ORIGINAL factor variance, used once for the whole chosen frontier; no separate copy is charged per depth or per query.

## 6. Signed inherited-reference ledger, including the old booking

Transport the ORIGINAL Q through every actual physical query using the actual coherent child kernel. With p,q the source/reference erased laws, use k_b(s)=P_b(s)/(2p(s)) on p(s)>0 and the fair fallback 1/2 on source-zero rows. Normalize with the actual reference probabilities z_b=sum q(s)k_b(s). All z_b are positive: a child source has positive total mass and incoming reference dominates it on that support. The factorized likelihood identity at each atom proves

    A0 = sum_reached(erasure KL+outcome KL)+Kold,

where Kold is the complete terminal inherited KL, including every complementary child and source-zero reference row. Let sigma be the reach-weighted sum of D(P_leaf||R_leaf)-D(P_leaf||Q_leaf) on RESET leaves only. Then

    sigma = T-Kold_selected <= T,
    A0+sigma = sum_reached(erasure KL+outcome KL)+Knew.   (6)

This is the actual reset cost, not T plus another copy of sigma. No root reference is renewed. All terminal KL remains in Knew.

Let e=H0-EHleaf-4(I0-EIleaf). Exact physical influence/entropy bookkeeping yields S-(A0+e)=M0. Hence with the COMPLETE reset bill N=A0+e+sigma,

    S-[N]_+ = min(S,M0-sigma).                      (7)

By (1),(5), M0-sigma>1+2t, while (2) gives S>=1. For any supplied earlier booking 0<=omega<=1/4 against this same signed account,

    S-[A0+e+sigma]_+-omega >= 3/4.                 (8)

The positive reset is actually exercised in the zero-data-prefix x cases: coherent transport of the empty-mass-matching original lift gives exactly the original q_g at the pure-core child, and r_g has the stronger nonempty tilt. Both likelihood ratios are retained in the certificate. Other histories can have negative reset cost. The proof uses the actual signed sum throughout; it does not replace [A0+e+sigma]_+ by A0+[e]_++[sigma]_+.

## 7. Checks, limits and first unsupported line

The independently written checker reconstructs full Boolean truth tables, Walsh probabilities, physical restrictions, original and new reference probabilities and normalizers. A direct character-sum check corroborates the small root spectra. It verifies the atomwise rational likelihood factorization before using interval logs; interval overlap alone is not the proof of (6) or (7). The logs use 32 positive atanh terms after range reduction to [1,2], with tail at most 2z^65/[65(1-z^2)], z<=1/3, and outward2^-110 rounding. Every finite claimed strict margin is checked with rational endpoints. The finite tests corroborate (8), whose unbounded quantifiers come from the derivation above.

The initial diagnostic used the same 1/8 target tilt and found only nonpositive reset increments. It is preserved as a narrower diagnostic, not used as evidence of positive reset cost. The final 1/7 target and its exact 7^4<2*6^4 sign were frozen before the amended pilot and main computation. This changes the prescribed reference while keeping the same original Q, rate, Boolean family and owner.

The result ends at this mixed-query/reset frontier. A further divergent history after a may not retain S>=1, and repeated resets need a new accumulated variance/accounting bound. More fundamentally, an arbitrary Boolean core still lacks a useful supplied correlated reference with a paid initial source price; choosing its own spectrum as an unpriced certificate would hide FEI in that input. These are the first unsupported universal steps. Full FEI remains OPEN. Rung: analytic proof with exact finite certificates; independent external review pending. No Lean certificate is asserted unless a separate receipt verifies the actual formal target, compiler, imports and allowed transitive axioms; a scalar check would not certify this entropy theorem.
