# Exact zero-cost refresh criterion and adaptive transported-witness repair

All cubes are uniform; signs are Boolean; logarithms are base two. This is a repair of a reference class, not a proof of FEI. No conversion to a fixed fresh profile is required by the repaired class.

## 0. Sharp repair retaining the fixed-profile interface

Consume A047's equal-mean identity in its 20261023T120344Z run, PROOF sections1-2. Let g(a,z) have children of the same signed mean mu, the same nonempty essential residual mask, and positive full-mask weights t0,t1; assume the parent full mask is occupied. Let 0<alpha<1, beta=1-alpha, u=mu^2, c=alpha(1-u), E=(t0+t1)/2. Use matching-empty full-spike references at parent and BOTH children. Direct erase/kernel normalization gives r_t=1/2+(c/2)(t_t/E-1) and

sigma=D(fair||r)+[F(t0)+F(t1)]/2-F(E),
F(t)=t log2(t/(beta*t+c)).

We independently reconstruct the atom ratios: at empty the old/fresh child ratio is1/(2r_t), at ordinary nonempty frequencies it is the same, and at the full mask it is [beta+c/E]/[2r_t(beta+c/t_t)]. Averaging the exact source-weighted log ratio gives the displayed formula. Since F''(t)=c^2/[ln(2)*t*(beta*t+c)^2]>0, BOTH terms are nonnegative and strict Jensen gives

sigma<=0 IF AND ONLY IF t0=t1.

Under this condition r is fair and inherited Q equals the fresh Q AT EVERY atom. Thus there is neither positive nor negative conversion. This is an exact necessary-and-sufficient (hence weakest within the stated equal-mean stable-mask class) repair of the claim that fixed-alpha full-spike refresh is nonpositive. For either-sign activation the same criterion holds: sigma_act=D(fair||r_act)+Gamma/2, r_act=1/2+(c/4)(t_t/E-1), with Gamma the same strict Jensen gap. This is NOT a criterion outside the displayed hypotheses; unequal means introduce additional terms.

Nontrivial surviving application: let h be the point sign on r>=2 bits, and define g(a,z)=h(z with its first input flipped iff a=1). Its two children are nonidentical input translates. They have the same signed mean and identical Fourier squares; their full coefficients are opposite and nonzero, so the parent full coefficient is occupied. Every residual variable remains essential. The selector influence is 2^(1-r)>0 and may be arbitrarily small. Every alpha in(0,1), both activation signs, and disjoint products with spectator factors satisfy the zero-conversion criterion. More generally any input-translation pair with occupied opposite full coefficients qualifies. A047's unequal-top-energy witnesses and A048's repeatedly changing mod3 profiles do NOT satisfy this sharp fixed-profile repair in general. No assertion about all of A097's isospectral histories is made without checking its signed-mean and occupancy hypotheses.

On a finite history where every required fresh refresh satisfies the criterion, cumulative conversion is exactly zero; all original signed ledger terms and BOTH terminals remain, as in section3 below. Where this hypothesis fails, the following adaptive interface remains hereditary but no longer promises the requested fixed profile.

## 1. The hereditary class

At a physical node v let P_v be the complete squared Fourier law of the restricted Boolean function. Admit any reference of the form

Q_v = b_v P_v + sum_{j=1}^k c_{v,j} delta_{W_{v,j}},

where b_v>0, c_{v,j}>=0, b_v+sum c_{v,j}=1, and every positive witness atom is in the support of P_v. Witnesses are subsets of the remaining ORIGINAL coordinates; they need not remain the full essential set. Duplicates are allowed and merge if desired. This last freedom, and allowing weights to change, are the additional hypothesis on the intended reference/application interface.

For a query i, put R=P_v after erasing i. Write P_{v,t} for its two child spectra on the residual cube. Their average is R, by the Fourier restriction identity. At each R(U)>0 the coherent kernel is K_t(U)=P_{v,t}(U)/(2R(U)). Transport both Q and P by erase, then this SAME kernel. On R(U)=0 the choice of kernel is immaterial: support matching gives erased Q(U)=0. Let r_t be the resulting reference outcome probability. The source outcome probability is exactly 1/2, including constant and irrelevant queries. Set U_j=W_{v,j}\{i} and

r_t=b_v/2+sum_j c_{v,j}K_t(U_j),
b_{v,t}=b_v/(2r_t),
c_{v,t,j}=c_{v,j}K_t(U_j)/r_t.

Then r_t>=b_v/2>0 and DIRECT atomwise division gives

Q_{v,t}=b_{v,t}P_{v,t}+sum_j c_{v,t,j}delta_{U_j}.

The coefficients are nonnegative and sum to one. Any positive new witness coefficient has P_{v,t}(U_j)>0. Hence the class is hereditary for EVERY Boolean function, EVERY coordinate policy, and BOTH children, with at most k witnesses for an arbitrary finite tree. There is no reset conversion: the child reference is exactly the inherited normalized law. No entropy premise or query-influence lower bound enters this statement.

For the matching-empty full-spike source q=(1-alpha)P+alpha P(empty)delta_empty+alpha(1-P(empty))delta_FULL, take k=2 and b=1-alpha, provided FULL is occupied (otherwise choose any occupied nonempty witness). Subsequent weights and empty mass may change, and the witness follows the original mask rather than a freshly computed essential mask. These freedoms are necessary features of this repair; the fixed-alpha matching-empty class of the A047/A048 obstructions is not claimed hereditary.

## 2. Actual normalizer and cumulative account

Along a path, b_child=b_parent/(2r_t). Thus the actual normalizer is retained:

log(1/b_v)=log(1/b_root)+sum_path log(2r_t).

It is not a fresh bank at v. Since Q_v>=b_v P_v, A_v=D(P_v||Q_v)<=log(1/b_v). More sharply, data processing with the erasure channel, followed by the exact joint KL chain rule, gives at each node

A_v = D_erase(v)+D(fair||r_v)+(A_{v,0}+A_{v,1})/2.

D_erase=D(P_v||Q_v)-D(erase P_v||erase Q_v)>=0. Therefore for ANY finite adaptive stopping tree,

sum_reached w_v[D_erase(v)+D(fair||r_v)]+sum_frontier w_v A_v=A_root<=log(1/b_root).

This pays ALL cumulative actual outcome normalizers and erasures from the same original KL account, rather than merely bounding the conversion at one node. Every term has its original reach weight; no complementary terminal is discarded. The scalar coefficient certificate also yields sum_frontier w_v log(1/b_v)=log(1/b_root)-sum_reached w_v D(fair||r_v), so this average envelope never renews or increases. Optional stopping is asserted only for finite trees, avoiding an unproved limit interchange.

## 3. Weakest ledger hypothesis and surviving applications

Let the original source have H0, I0, A0 and M0=4I0-H0-A0. At a complete frontier let S=E(4I-H), and let e=H0-EH-4(I0-EI) be the SIGNED edge account. With this hereditary reference there are no conversion charges, and exactly

S-[A0+e]_+=min(S,M0).

For an already booked old debit omega>=0, the remaining amount is min(S,M0)-omega. Consequently retaining reserve rho>=0 is equivalent to the two inequalities S>=rho+omega and M0>=rho+omega. This is the weakest necessary-and-sufficient additional numerical hypothesis for THIS ledger conclusion; it is not advertised as a weakest assumption implying FEI. If earlier actual conversions have already accumulated Sigma_old, retain them and replace M0 by M0-Sigma_old. The new continuation adds zero conversion.

Surviving intended applications: (i) every supplied support-matched A050 point-tensor source, including arbitrary widths and loads, admits this reference repair; (ii) A047 stable-mask rare-query families and A048 same-support mod3 families admit the reference transport whenever their displayed initial full-spike source is supplied; their cumulative fixed-profile reset obstructions no longer apply to THIS altered interface; (iii) arbitrary finite disjoint products of supplied references remain products when one factor is queried, retaining a factorwise bounded witness representation; (iv) a SUPPORT-MATCHED correlation-preserving A050 lift is a finite mixture of its actual spectral law and finitely many occupied witnesses and therefore transports similarly, though the number of atoms may grow with the original core dimension. To see (iv), take b smaller than min_{P(S)>0}Q(S)/P(S) and smaller than1, then decompose the nonnegative remainder Q-bP into its occupied atoms. This is an existence representation, not a new source-price bound. References with positive source-zero ghost atoms are excluded from this occupied-witness theorem. The constant-size two-witness representation applies directly to the supplied core full-spike reference, not automatically to the entire lifted controller law.

For (ii), the theorem pays reference transport and cumulative normalized-outcome KL; it does NOT automatically prove S>=rho+omega at every stopping frontier, nor provide a cheap arbitrary-core initial source. For any application insisting on a freshly matched empty atom, a fixed alpha, or the current full ESSENTIAL mask, admission fails and a positive conversion must still be paid. A073's point-profile theorem can be used when those stronger requirements are actually needed; it is not assumed for this universal transport lemma.

FIRST UNSUPPORTED UNIVERSAL LINE: construct, for every Boolean core, an influence-priced ORIGINAL complete supplier and a useful query/stopping policy whose actual terminal surplus S meets the required reserve, while using only the transported-witness interface (or paying every additional required conversion from its actual remaining original account). Choosing Q=P would make transport trivial but its source price is H itself; this theorem does not solve that circularity.

## 4. Validation

Exact replay PASS:1536 function/order trees plus3 rare witnesses,248925 rational assertions;20 translated-point profiles (core and both activation signs),310 assertions; independent FWHT audit 433 assertions across 216 eligible profiles. Total 249668 nonpilot assertions. Pilot output-only failure and successful rerun are preserved in out/PILOT_FAILURE.json and out/PILOT.json. Primary compute9.399s; criterion0.298s; no job exceeded100MB estimated memory or55s compute cap. Memory peak was not measured. No heavy memory gate was triggered. The proof above uses the exact Fourier restriction identity, normalized Bayes transport, the KL chain rule and Gibbs inequality. Finite replay is a check of these identities and their claimed applicability; the all-dimensional statement follows from the derivation, not extrapolation.
