# What an outcome invoice requires: likelihood control, not bounded KL

All inputs are actual uniform Boolean cubes, all logarithms in displayed information quantities are base2. Full FEI remains OPEN. References are normalized. No reference-only atom is silently dropped. The theorem below assumes reference support contained in source support; the explicit witnesses have exactly matching support. This restriction is deliberate, and does not assert a price for extra-support references.

## 1. Universal Boolean outcome geometry

Write the queried coordinate as i, and its paired real Fourier coefficients as a_T=hat f(T), b_T=hat f(T+i). Put p_T=a_T^2+b_T^2, s_T=a_T*b_T/p_T on p_T>0, and eta=Inf_i(f). Booleanity implies

    sum p_T=1, sum p_T*s_T=sum a_T*b_T=0,
    |s_T|<=1/2,
    V=sum p_T*s_T^2=sum a_T^2*b_T^2/p_T
      <=eta(1-eta)<=theta=min(eta,1-eta).                 (1)

The zero mean uses the two child Parseval identities: sum(a+b)^2=sum(a-b)^2=1. For the variance bound put u_T=b_T^2/p_T; E_p u=eta and E_p[u(1-u)]<=eta(1-eta) by concavity. Thus (1) uses a genuine Boolean constraint, rather than an arbitrary spectral law with guessed fair physical outcomes.

Let q be ANY probability reference on the source support, qbar its erased law, L_T=qbar_T/p_T, and t=E_qbar s. The coherent reference outcomes are r=(1/2+t,1/2-t). Assume both positive. Then

    O=D(fair||r)=-log2(1-4t^2)/2,
    t^2 <= chi2(qbar||p)*V.                             (2)

Indeed t=E_p[(L-1)s] and Cauchy-Schwarz proves (2). All terms, including zero source pairs, are handled on the complete positive erased support; the support hypothesis gives qbar=0 on the omitted pairs, so no mass is lost.

If qbar>=beta*p for 0<beta<=1 then r_b>=beta/2. Since -ln(1-x)<=x/(1-x),

    O <= 2 chi2(qbar||p)*eta(1-eta)
                  /[beta(2-beta) ln2].                  (3)

If additionally qbar<=Lambda*p, where Lambda>=1, the exact inequality

    chi2(qbar||p) <= (Lambda-1)(1-beta)                  (4)

follows by averaging (L-beta)(Lambda-L)>=0 and using E_p L=1. Combining (3)-(4) gives a dimension-independent O<=K(beta,Lambda) Inf_i. This prices ONLY O, until a separate residual bound is supplied. A049's fixed-mask theorem supplies sigma<=O+[2+alpha/(1-alpha)]Inf_i/ln2 for its full-spike rule; its support/essential-mask hypotheses must also be retained when using that composition. Neither (3) nor A049's residual inequality prices an arbitrary initial source.

## 2. Forward KL provides a weaker, sharp logarithmic barrier

For any lambda>=0 and |s|<=1/2, termwise expansion gives

    exp(lambda*s)<=1+lambda*s
              +4s^2[exp(lambda/2)-1-lambda/2].

The same bound holds for -s. Taking P expectation and using (1), then Jensen under qbar, yields the elementary variational bound (with natural logarithms in this one line)

    (ln2)D(qbar||p)
      >= lambda*|t|-ln(1+4V[exp(lambda/2)-1-lambda/2]).

For clarity, Jensen is applied to log(exp(lambda*sign(t)*s)/L): its qbar expectation is lambda|t|-D_nat, at most log E_p exp(lambda*sign(t)*s). No external information inequality is needed. For 0<theta<=1/2 choose lambda=2ln(1/theta). The logarithm's argument is<=5. Therefore

    D(qbar||p) >= 2|t| log2(1/theta)-log2(5).            (5)

The full forward KL D(q||P) dominates the erased forward KL by log-sum. If it is<=B and qbar>=beta*p, then

    |t| <= [B+log2(5)]/[2log2(1/theta)],
    O <= [B+log2(5)]^2
          /[2beta(2-beta)ln2 * log2(1/theta)^2].         (6)

When eta=0 or1, all s vanish and O=0, so endpoints require no limiting convention. Bounded forward KL plus a fixed lower likelihood floor forces O->0 as eta->0, but (6) is logarithmic, not an influence price. Section3 proves that its inverse-square-logarithmic order cannot be improved in general.

## 3. Actual Boolean sharpness with BOTH KL directions bounded

Use r>=3, d=2^-r and a=e0+e1 in the private cube, and define the SAME actual Boolean family from A040 stage9:

    v_r(j,z,w)=(-1)^z(1-2*1{w=0 or(j=1 and w=a)}),
    G_epsilon(x,j,z,w)=epsilon at x0, v_r at x1.

Its source has zero core mean, parent full mass d^2, erased full-row mass10d^2, child full masses4d^2,16d^2, and Inf_j(G)=d/2. In every core use q_alpha=(1-alpha)P+alpha*delta_full; in G copy the exact controller-only half and put q_alpha(T)/4 on each of its two active data copies. Both old/fresh references have exactly source support. Query j, normalize the inherited reference by its OWN outcome probability, and actually refresh both children to the SAME alpha remaining-full law. Section4 of stage9 gave a complete paid one-query ORIGINAL priority-source transaction; this stage never renews that account or assumes a reset is mandatory.

For any alpha the exact reference outcomes and complete signed reset are

    r=(1/2-3alpha/20,1/2+3alpha/20),
    kappa_alpha=-log2(1-9alpha^2/100)/2,
    sigma=kappa_alpha+
      [F_alpha(4d^2)+F_alpha(16d^2)-2F_alpha(10d^2)]/4
      >kappa_alpha,

where F_alpha(m)=(1-m)log2(1/(1-alpha))+m log2[m/(alpha+(1-alpha)m)]. The second derivative is alpha^2/[m(alpha+(1-alpha)m)^2 ln2]>0. These formulas are reconstructed by both scripts from complete physical laws, not taken on trust from stage9.

Now choose alpha_r=1/r. This is a profile chosen ONCE for each r and is unchanged across the rare query. The actual pointwise likelihood floor is>=1-1/r>=2/3. Its reverse and forward full divergences satisfy

    D(P_G||Q_G)=F_(1/r)(d^2)/2 ->0,
    D(Q_G||P_G)
      =[(alpha+beta*d^2)log2((alpha+beta*d^2)/d^2)
          +beta(1-d^2)log2(beta)]/2
      =1-h2(1/r)/2+o(1) ->1.                           (7)

They are uniformly bounded, for example reverse<=log2(3/2)/2 and forward<=2 for all r>=3. For the latter write its forward KL as half the Bernoulli divergence D(Ber(alpha+beta*d^2)||Ber(d^2)); dropping negative entropy gives an upper bound r(alpha+beta*d^2)+[-log2(1-d^2)]/2. The first term is1+r beta*d^2, and the second is<=d^2/[(1-d^2)ln2]/2<1/2 using ln2>1/2. Hence this sum is<2. The expansion in (7) follows by replacing alpha+beta*d^2 by alpha; the error is O(r*d^2+r^2*d^4), including its logarithm, and tends to0.

Nevertheless

    O=kappa_(1/r) ~ 9/[200ln2*r^2],
    sigma=O+c*d^2+O(r*d^4) ~ 9/[200ln2*r^2],
    sigma/Inf_j(G) ~ [9/(100ln2)]*2^r/r^2 ->infinity,   (8)

with c=18-5log2(10)>0. Thus bounded forward KL, bounded reverse KL, fixed likelihood floor, same support and same-alpha child refresh do NOT give a dimension-independent local influence price. They also show (6)'s order log(1/eta)^-2 is sharp even for actual Boolean functions and supported references.

The five previously specified positive credits remain quantitatively insufficient. With g=1-(3/2)log2(3/2)>0 their asymptotics are

    E~9r*d^2, J~(1+c)d/2, P~rd/2,
    Gamma~g*rd, TC~(3/2)r^2*d.                         (9)

Only E depends on alpha: E=[F_alpha(d^2)-F_alpha(10d^2)]/2. With alpha=1/r its additional error is O(d^2 log r), so the same leading9r*d^2 holds. All five are strictly positive for every r>=3 by decreasing F, distinct child laws, nonconstant posterior probabilities, strict Bernoulli concavity and nonproduct support respectively. Set K=9/(200ln2). Their ratios to sigma are asymptotic to (9/K)r^3*d^2, [(1+c)/(2K)]r^2*d, [1/(2K)]r^3*d, (g/K)r^3*d, [3/(2K)]r^4*d; all tend to0. Their ratios to H(G)->2 also vanish. The forward KL in (7) is bounded and nonvanishing; it is NOT falsely included among the five vanishing credits.

The actual erased likelihood distortion is exactly

    chi2(Q_erased||P_erased)=alpha^2/2*(1/(10d^2)-1),
    Lambda_erased=1-alpha+alpha/(10d^2).                (10)

Thus the hypothesis of (3) with uniformly bounded chi2, or (4) with bounded Lambda, is exactly what this family violates. The large likelihood on a rare source row creates the outcome bias; bounded KL alone permits it. H(G)/I(G)->2, so no FEI counterexample is asserted.

There is a stronger vanishing-KL corollary. Choose alpha_r=1/r^2, still unchanged across each physical rare query. The SAME exact formulas give

    D(P_G||Q_G)~1/(2ln2*r^2), D(Q_G||P_G)~1/r,
    sigma~9/(200ln2*r^4),
    sigma/Inf_j(G)~[9/(100ln2)]*2^r/r^4 ->infinity.

Both KL directions now tend to zero, and the fixed likelihood floor is>=8/9. To verify the uniform expansion, write F_alpha(m)=log2(1/beta)+m log2(beta*m/alpha)-m log2(1+beta*m/alpha); the last term is bounded by m^2/(alpha ln2). In its Jensen combination the linear m log(beta/alpha) terms cancel, leaving c*d^2+O(r^2*d^4). The forward error in replacing alpha+beta*m by alpha is O(r*m+r^4*m^2), negligible compared with1/r; h2(alpha)/(alpha*r)->0. Thus the corollary is an analytic consequence of the all-alpha identities, not a fit to finite examples. The five credits in(9) keep their same leading terms (E has only O(d^2 log r) error), so each divided by sigma still tends to zero, now with the r powers in those ratios increased by2. All seven named KL-type quantities are positive and vanish relative to retained H(G)->2; only the original FIVE, not the two reference divergences, are asserted to vanish relative to the reset bill.

## 4. Consequence of the new cumulative obstruction

REVIEW_A037.md reconstructs A037-REPEATED-WHOLE-CORE-SPIKE-EXHAUSTION@1 unchanged. Its claim is stronger than a new local witness: on one admitted ORIGINAL priority source, k complete generations each have total reach1/2 and bill>1/1200, while inclusive original margin is<49/16. At k=4096 the final signed account is<-421/1200 even BEFORE oldquarter, although initial admission/first reset are paid and all terminal surplus is positive. A048 independently supplies a shared mod3-tail obstruction; its proof was read as corroborating mechanism retirement, not independently accepted here.

Accordingly we retire unlimited fixed whole-core replenishment. Neither our last stage's paid first transaction nor the bounded-KL normalization in this stage repairs that exhausted owner. A coherent inherited reference avoids optional conversion costs; any useful replacement supplier must pay its actual conversion from current unused source, rather than a newly named KL budget. The first unsupported universal line is an influence-priced initial arbitrary-Boolean source whose selected policy preserves enough likelihood control, or pays its loss once, through a complete physical history. We do not assume that such a policy exists. No universal FEI constant improves in this stage.
