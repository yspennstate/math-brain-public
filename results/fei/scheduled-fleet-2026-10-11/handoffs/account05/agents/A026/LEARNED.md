# Durable facts from A026 stage 1

- For adjacent parent Fourier coefficients, B_i <= A_i := 2 sum_T |a_T a_(T+i)| by h2(p)<=2 sqrt(p(1-p)). This A_i differs from child Hellinger affinity.
- Exact complete enumeration through n=4, modulo global output sign, yields max_f min_relevant_i A_i/I_i equal to 0,2,3,7/2 at n=1,2,3,4. Two independent integer implementations agree; point defect attains the last three proxy maxima. This does not identify sharp true B_i constants.
- If nonzero Fourier support lies in affine c+V and e_i is outside V, adjacent support pairs do not coexist, so B_i=JS=Delta_iH=0. If all relevant e_i belong to V, their number is <=dim(V). Physical restriction projects support and never increases its affine dimension.
- Therefore affine Fourier dimension <=4, and arbitrary disjoint products of such factors, have a relevant B_i <=(7/2)I_i at every nonconstant restriction and H <=(7/2+2/ln2)I. Locally proved and checked; external independent review pending. Existing bounded-gate/parity FEI results mean no priority claim should be inferred.
- Symmetric threshold f=+1 at weights>=24 on n=32 has A_i/I_i=2220940451/536870912>4 for every i. The n=64,t=40 exact proxy ratio is 10293444163950323579/2305843009213693952. These are proxy failures only, not actual erasure failures or FEI disproofs.
- Universal existence of finite K for some B_i/I_i remains FEI-equivalent and open. All-coordinate rare-split obstructions do not refute it. Root-only zero erasure does not certify a terminal class: heredity must be proved and all descendants accounted for.
- Preserve mismatch credit M[log(1/M)-D2(nu||q)+1/ln2]. Zero isospectral steps have M=0 and exact zero entropy decrement. Do not replace them by marginal entropy.

## Stage 2 durable updates

- A028 independently accepted both A026 v1 claims at their stated scopes; the source review records and original hashes were inspected. This supersedes the earlier rolling note saying all v1 external review was pending. Shared adoption/mirror not inferred.
- Follow B06 v2: no more amplitude proxy work. A075 already proves recursive Maj3 H=4((3/2)^d-1), I=(3/2)^d, B=0. Its roots are transitive. Do not claim a new result by reproducing this.
- Singleton tribes with p=2^-w,b=1-p,a=b^m,t=b^(m-1) have B_i=4p(1-2p)t+4(t-t^2)Phi(b^2,p^2)+Phi((1-2a)^2,4p^2t^2); I_i=2pt. Therefore B/I->2,H/I->4,B/H->1/2 uniformly for arbitrary m(w)>=1. This is different from whole-tribe erasure in A076. The uniform proof uses the exact exceptional empty packet and t log(1/t)<=1/(e ln2).
- For transitive roots B_i/I_i=B/I. Transitivity is lost after restriction; no root-only theorem closes universal good-coordinate induction. B/H=0 on recursive Maj3 despite limiting H/I=4 rules out a positive comparison at this benchmark, but not FEI.
- After any B_i=0 physical query, both child squared spectra equal the deletion pushforward. For every remaining j, B_j(child)=H(S_i,S_j|all other spectral bits). The newly exposed pair entropy is not universally paid here.
- Certified cyclic overlapping-window benchmark n=10,width2,threshold1: H/I=3.89243855524..., B/I=3.15519599472..., B/H=0.81059622392.... First-child min prices are 3.033739939... and 2.647247133.... Recursive Maj3 depth2, after one free query, has positive minimum child price 0.842929269... on either branch; root zero does not persist.
- Rational log certificate implementation should aggregate repeated integer terms before Fraction arithmetic and round each enclosure outward to a shared dyadic denominator. v1/v2 reached runtime guard; v3 passed the unchanged 69-function domain in 2.066s. Failed pilots are resource failures, not mathematical counterexamples or substantive stagnation.

Stage3 durable facts (20261013T214810Z-account05-A026-good-coordinate-erasure):
- Actual-rest odd balanced encoder: F=A+gD, delta=E D^2, gamma=ghat_i,d=I_i(g) gives B_i=sum Phi(Ahat^2,gamma^2 Dhat^2) and B_i/I_i<=(gamma^2/d)log2(e/(gamma^2 delta)). Histories outside intact g may be arbitrarily biased; histories inside invalidate balance.
- For the specified B05 outer influence types and M=2k^2 2^(2k+2)+1, any adaptive at-most-one-query-per-block prefix preserves cheap intact bits at B_i/I_i<55/256 and I_i>I/(2d), while selector remains unique maximum. General proof uses q rho<3/32 density domination, not reused uniform outer spectra.
- Sliced inner h: B_i(A+hD)=delta[B_i(h)-Phi(mu^2,gamma^2)]+sum Phi((Ahat+mu Dhat)^2,gamma^2 Dhat^2). Maj3 after first query has inherited B_i=1,d=1/2; omitting this charge is false.
- Prefix theorem retains E H(leaf). All blocks touched is the first unpaid node, and arbitrary delta makes the scalar log(1/delta) unbounded. No universal C018/C019 or biased selector-erasure divergence is inferred.

Stage4 durable facts (20261014T011337Z-account05-A026-good-coordinate-erasure):
- Sharp scalar signed-row excess: Phi((a+b)^2,c^2)-Phi(a^2,c^2)-Phi(b^2,c^2)<=log2(32/27)c^2, equality a=b=c/sqrt8. A one-turn derivative proof establishes the continuum; a grid alone does not.
- Arbitrary biased Boolean h, actual rest f=A+zD: B_i(A+hD)<=delta B_i(h)+gamma^2 B_z(f)+delta gamma^2[log2(1/gamma^2)+kappa]. The negative empty-row term cancels rowwise; residual <=[kappa+2/(e ln2)] physical query influence. Bias conversion is paid, inherited/shadow/terminal bills are not.
- Encoder-only fixed-shadow prefixes have Q_shadow=B_z(f)[Var(h_root)-E Var(h_leaf)] exactly. Complete-policy charge is query-order invariant. Quadratic-bent one-point-flip f_k has B_z/Inf_z>=k-1; fixed Maj3 yields Q_shadow/encoder_spend>=2(k-1)/3 for every complete encoder-only policy. This refutes that bank funding rule, not FEI or existential actual-coordinate selection.
- Auxiliary uniform shadow z is not a physical encoder query; its unchanged entropy cannot telescope over encoder queries. Actual outer-data budget and full terminal entropy must be owned jointly.
- Common-dyadic integer interval sums exactly reproduce repeated Fraction sums and cut the guarded checker runtime; preserve partial certified rows and freeze any continuation.

Stage5: B_z<=h2(delta)<=I(g+g-). W=Var(h)I(g+g-) funds all encoder shadow charges under arbitrary fixed-partition interleaving: Q+G+L+EWleaf=Wroot. Actual exclusive pivotal account X is conserved; W<=4max(q,1-q)X sharply. This funds one charge, not full terminal entropy or duplicate data spend.

Stage6: V=Var(h)h2(delta) is a nonnegative mixed-query shadow reserve: encoder drop gamma^2 h2(delta), data drop Var(h) I(disagreement;query). Q+G_H+L_H+EVleaf=Vroot; every difference from stage5 boundary account is nonnegative. But point/constant S4 gives V-S4>=delta(d-5); tensoring both terminals with a2d-bit point sign gives V-S4prime>=delta(d-11/2) for d>=8. Thus envelope funding from certified terminal slack plus fixedA delta fails even with two nonconstant terminals, although actualQ can be paid. Source alignment: A028@5 already has boundary bank R=W/2; only its conservation clause independently accepted here. Neutral six-bit AND3+Maj3 all6 alternative first queries retain same original bank; extra actual encoder correction is positive (<51/1000), never drop it.
