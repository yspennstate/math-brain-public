# One original collision account crosses the shared coordinates

Entropy is in bits; all remaining physical inputs are independent uniform bits. This extends the concrete constant-outside two-point family in A077/A078. It does not assert a new FEI constant or supply arbitrary source entropy certificates.

## 1. Family and inherited private payment

On d>=1 shared bits, with e=2^-d, put F=V at shared vertex0, W at vertex e1, and +1 elsewhere. V,W are arbitrary correlated Boolean functions on the SAME independent private cube. Write mu=EV, nu=EW, g(t)=-t^2 log2(t^2), and

    Xi=e sum_(T nonempty) k(Vhat(T),What(T)),
    k(a,b)=[g(a+b)+g(a-b)]/2-g(a)-g(b),
    R=de[2-mu^2-nu^2], Tcore=e[H(V)+H(W)].

The inherited A077 mean-sector theorem, reconstructed below, is

    Delta_private H(F)<=Delta Tcore+release_R+12Inf_private(F)+Delta Xi. (1)

The exact spectrum is Fhat(S,empty)=1{S=empty}+e(mu-1)+e(-1)^(1 in S)(nu-1), and Fhat(S,T)=e[Vhat(T)+(-1)^(1 in S)What(T)] for nonempty T. The binary entropy formula for k gives -4e<=Xi<=0. No Fourier label is omitted other than the explicitly excluded empty private label. Direct physical edges give Inf_i(F)=e[Inf_i(V)+Inf_i(W)].

For completeness the mean proof does not need an FEI hypothesis. Along a mean segment in direction(a,b), the translated-row derivative has squared norm t=e(a^2+b^2). Its normalized law has entropy d-1+h2((a+b)^2/(2(a^2+b^2)))>=d-1. The row mass is 1-e(2-mu^2-nu^2)<=1. Weighted log concavity therefore gives E''>=2t(d-1)-6t/ln2. Adding de(2-mu^2-nu^2) leaves curvature >=-(2+6/ln2)t. The midpoint bound and |g'|<=6 on[-1,1] give the remainder at most e[(1+3/ln2)(a^2+b^2)+6(|a|+|b|)]<=12e(Inf_i(V)+Inf_i(W)); use |a|<=Inf_i(V)<=1 and the analogous b bound. All zero rows glue because g is C1 and varying rows are affine; zero direction is treated separately. This proves (1), independently of any supplied source certificate. The exact reserve release is de(a^2+b^2).

To make the decomposition used in this curvature argument explicit, let Emean be the entropy of the complete empty-private Fourier sector. Direct expansion of the nonempty rows gives

    H(F)=Tcore+Xi+2R+Emean-e[g(mu)+g(nu)].

Consequently the residual after the one reserve release is the midpoint decrement of Emean+R-e[g(mu)+g(nu)]. The curvature bound pays the first two terms; the stated Lipschitz bound pays the last two. Since 1+3/ln2+6<12, this gives exactly (1).

Here and below the two-child channel estimate is Delta_i H<=B_i+2Inf_i/ln2. For a self-contained check, a paired Fourier row has Jensen-Shannon contribution E(a,b)/ln2, where E(a,b) is the natural-log entropy of the two values (a+b)^2,(a-b)^2 with equal weights. By homogeneity set a=1,b=t; E(0)=E'(0)=0 and

    E''(t)=ln((1-t^2)^2/(1+t^2)^2)+4/(1+t^2)<=4.

The logarithmic singularity at t=1 is integrable and E' is continuous there. Integrating gives E(1,t)<=2t^2; a=0 follows directly, and homogeneity covers every real a,b. Summing all rows yields the channel estimate without an external FEI premise.

## 2. Shared activation gates cost less than six actual influence units

First let F=1+1{r shared gates all zero}(M-1), where r>=1 and M is ANY Boolean core on disjoint physical inputs. Set p=2^-r, mu=EM, and w=p(1-mu). A query of one gate has Inf_gate(F)=w, including constant and biased cores. Pairing its full Fourier rows gives exactly

    B_gate(F)=Phi((1-w)^2,w^2)+2w(1-w),
    Phi(P,Q)=(P+Q)h2(Q/(P+Q)).                         (2)

The nonempty-core rows and all nonempty remaining-gate rows together contribute 2w(1-w). This count retains the old empty frequency. If w=0 there is no bill. For 0<w<=1, P+Q<=1 and P ln(1+Q/P)<=Q give

    Phi(P,Q)<=2w^2 log2(1/w)+w^2/ln2.

The P=0 endpoint is included by continuity. Because 1/ln2<2, (2) implies

    B_gate/w <=2+2w log2(1/w)<=2+2/(euler ln2).

The elementary two-child channel bound JS<=2Inf/ln2 then gives

    Delta_gate H(F) <= [2+2/ln2+2/(euler ln2)] Inf_gate(F)
                    <=(1339/224)Inf_gate(F)<6Inf_gate(F). (3)

Here ln2>=56/81 follows from the first two positive terms of 2atanh(1/3), and euler>=8/3 follows from the first four terms of its series. Thus (3) has a rational margin5/224. At w=1, (2) vanishes as does the entropy decrement, so the endpoint is harmless. No restriction on M's dimension, entropy, mean or spectrum is imposed.

For the two-point family, every shared coordinate OTHER THAN e1 is such a gate, with M the one-bit mux of V,W. Its influence is e(2-mu-nu). On gate0 the family survives with d'=d-1,e'=2e; on gate1 it is the constant +1 and the two-event geometry dies. Its original reserve releases exactly e[2-mu^2-nu^2]. Tcore is harmonic: the surviving child's coefficient doubles and its probability halves.

## 3. The shared profile-separating coordinate is also paid

Query the coordinate distinguishing0 and e1. Let delta=Pr(V!=W), q=2-mu-nu, c=mu-nu, and j=2e delta=Inf_sep(F). The two physical children are ONE-point activations of V and W, respectively, on d-1 shared gates, each of probability2e. Their full input entropies have average Tcore, and their original point reserves have mean (d-1)e[2-mu^2-nu^2]. Thus

    release_R=e[Var(V)+Var(W)].                        (4)

For every NONEMPTY private label, summing the erasure fiber over all remaining shared frequencies and using Phi(P,Q)<=P+Q gives an erasure contribution at most e[Var(V)+Var(W)]. This is precisely (4), not a new donor. The complete EMPTY-private sector contributes

    B_empty=Phi((1-eq)^2,e^2c^2)
               +(1/(2e)-1)Phi(e^2q^2,e^2c^2).         (5)

Use Phi(a^2,b^2)<=2|ab|, which follows from h2(t)<=2sqrt(t(1-t)). A self-contained verification of this binary bound is given below. If d>=2, e<=1/4, 0<=q<=4, and 1-eq>=0, so (5) is at most

    2e|c|[1+(1/2-2e)q]<=6e|c|<=12e delta=6j.

For d=1 the second term vanishes and |1-eq|<=1, giving the stronger B_empty<=2j. The coupling bound |mu-nu|<=E|V-W|=2delta is essential here. If delta=0, mu=nu and B_empty=0, so no zero denominator is used. Together with JS<=2j/ln2<3j this proves

    Delta_sep H(F)<=release_R+9Inf_sep(F).             (6)

No common private-controller factorization is assumed in (5)-(6); V,W may be arbitrarily correlated. The signed Xi disappears at this query, but it is not discarded as a free credit: the original collision account is explicitly frozen and retained in BOTH children in section4.

Here is the binary bound used in (5). By symmetry take 0<=t<=1/2 and write z=1-2t. The desired inequality is h2((1-z)/2)<=sqrt(1-z^2). Define f(z)=sqrt(1-z^2)-h2((1-z)/2), f(0)=f(1)=0. On(0,1), f'(z)=atanh(z)/ln2-z/sqrt(1-z^2), and f''(z)=[sqrt(1-z^2)-ln2]/[ln2(1-z^2)^(3/2)]. Thus f' first increases and then decreases, starts at0 and tends to-negative-infinity, with exactly one interior zero. Hence f first increases then decreases to0 and is nonnegative. This uses 0<ln2<1 and covers the endpoints by continuity. No unproved numerical entropy inequality is imported.

## 4. One source account across ALL adaptive mixed histories

At an original continuation state o let e_o=2^-d_o, Xi_o=e_o chi_o, and supply ONE unused original donor B after all old debits. Put beta=B/e_o. Before the separating shared coordinate is revealed, define at every still-live two-point state

    chi_v=Xi_v/e_v,
    K_v=e_v[beta-chi_o+chi_v].                         (7)

If the event has died at an activation gate, set e_v=R_v=Tcore_v=K_v=0 and retain its actual constant F terminal. Under a PRIVATE query e_v is unchanged, and

    Delta Xi+average K_child=K_parent.                (8)

Under a shared ACTIVATION gate, the surviving e and Xi double while the other child has zero event. Thus average K_child=K_parent and average Tcore_child=Tcore_parent. The bank has not been reissued. At the profile-SEPARATING query, assign K_child=K_parent to BOTH actual children and henceforth freeze that value on all descendants, including later constant terminals. This assignment preserves its conditional average exactly. It is a transported ancestor earmark, not a claim that each child independently supplies the original donor.

After separation the children have one point activation each. A076 v7, independently accepted by A077 at its stated scope, supplies private price11 with the corresponding inherited point reserve. Its complete proof is not reproved here. Every later shared activation gate obeys (3); K stays fixed. When no shared gates remain, F is simply its actual private core and inherited entropy is retained without a reserve.

Since -4<=chi_v<=0, the sufficient admission B>=4e_o implies K_v>=e_v(beta-chi_o-4)>=0 in the two-point phase; freezing preserves positivity thereafter. More precisely, K_v>=e_v(beta-4) if chi_o<=0. The process e_v, doubled on surviving gates and zero on dead gates, is a martingale up to separation; after separation freeze its value as a bookkeeping mass. Every finite adaptive frontier therefore has

    E K_frontier>=B-4e_o.                              (9)

All reach probabilities here are the ORIGINAL physical probabilities. Summing the stopped inequalities from (1),(3),(6),(8) and the one-point theorem gives, for EVERY finite adaptive mixed tree with no repeated physical query per path,

 H(F_o)-E H(F_leaf)+E[R_leaf+K_leaf]
   <=Tcore_o-E Tcore_leaf+R_o+B
        +12 P_private+6 P_gate+9 P_separator.          (10)

At a separator, Tcore changes representation to one-point core weight2e in each child; its average remains unchanged. Every complete physical terminal entropy and both original input allocations remain in (10). No positive-part clipping of signed private collisions is allowed. The maximum CONTINUATION transaction price is still12, not a new global FEI constant. Original donor admission and arbitrary inherited input entropy remain separate obligations.

## 5. Actual bent donor after the already booked first collision

Use the A078 source V=y*b_k(z), with k>=4 even, b_k quadratic bent, and W=y[1-2*1{z=0,x1=...=xm=0}], m>=2. Outside the two edited shared vertices use +1. At the ORIGINAL source e_o, the actual C5 V surplus is S=e_o(3k/2+5). Retain an old debit D0>=0 and the FIRST booked collision4e_o. Take B=S-D0-4e_o. If D0<=S-8e_o, equations(7)-(10) give the SAME all-private/mixed admission as A078 and leave

    E K_leaf>=S-D0-8e_o>=3e_o-D0.                    (11)

No descendant bent certificate is recomputed, even if the private history queries z or y. The original entropy allocation e_o H(V) and S are disjoint parts of the original5e_o I(V); their later allocations and all old debits remain present. Actual physical query allowances in(10) are continuation prices, not permission to add that original source twice to an FEI deficit. The separate root input budgets still need a noncircular complete admission.

## 6. Exact remaining universal line

This closes the next shared-query handoff for the constant-outside two-point source, and actually allows every finite mixed private/shared history at the same continuation price12 with the old donor and full terminals retained. It does NOT cover arbitrary nonconstant h outside the two edited vertices: its shared-node fibers contain the carrier's genuine Fourier amplitudes and cannot use(2)/(5) as written. It also does not supply the original donor or arbitrary input/terminal FEI certificates at an unrestricted root, nor prescribed terminal-reference conversion. The next useful target is one nonconstant threshold carrier with the inherited collision account, measuring the extra carrier-row bill against actual unused original signed surplus. Full FEI remains OPEN; new analytic clauses await independent review.
