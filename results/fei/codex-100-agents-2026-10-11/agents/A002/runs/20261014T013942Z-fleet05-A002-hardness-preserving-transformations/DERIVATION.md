# Signed corrected selection: tensor growth and same-C completeness

Uniform finite physical cubes; actual Boolean signs; normalized Walsh coefficients; H and JS in bits. Write d_i=Inf_i, B_i=H(S_i|S_-i), L_i=H(f)-average H(f_i,+/-)=B_i+JS_i, I=sum d_i. Fix C>=0, delta=H-CI, and sigma_i=average[CI(child)-H(child)]. Only relevant coordinates occur in minima. Define

    q_C,i=(B_i+max(-sigma_i,0))/d_i,   Q_C=min_i q_C,i.

Constants have no relevant coordinate and are assigned Q_C=0. C is fixed before functions/dimensions. No finite universal FEI constant is assumed.

## 1. Source-owned signed interface

A005 stage 3 owns the point-edit eligibility/transport theorem. A061 stage 4 already identifies the following maximum form; it is consumed rather than claimed as new:

    delta+sigma_i=B_i+JS_i-Cd_i,
    q_C,i=max(B_i/d_i, C+(delta-JS_i)/d_i).                (1)

The scalar JS bound JS_i<=a d_i, a=2/ln2, then implies, for delta>0,

    Q_C(f)>=C-a+delta/d_max,    d_max=max_i d_i.           (2)

This corrects any price-two witness by its actual negative descendant slack. It is not a payment: (1) contains the root deficit explicitly.

## 2. New exact tensor growth, including the finite transition

Fix a nonconstant seed f on n relevant bits. For t disjoint copies, influence d_i, erasure B_i and JS_i at a coordinate in a given copy do not change. Root deficit is t delta, and actual child slack is

    sigma_(copy,i)(f^tensor t)=sigma_i(f)-(t-1)delta.

The slack transport is already proved by A005 stage 2. Substitution into (1) yields the NEW complete corrected-price transport:

    Q_C(f^tensor t)
       =min_i max(B_i/d_i, C+(t delta-JS_i)/d_i).          (3)

If delta>0, then once (t-1)delta>max_i sigma_i all averaged children violate C, and exactly

    Q_C(f^tensor t)=C+min_i (t delta-JS_i)/d_i,
    Q_C(f^tensor t)/t -> delta/d_max>0.                  (4)

The finite minimum is over n seed directions, so the limit follows without an exchange over growing dimension. Thus tensoring preserves the ordinary H/I and minimum B_i/d_i but amplifies the corrected price. It does not preserve child certification. Negative descendant slack is extensive and cannot be treated as a local influence account.

## 3. Same-C universal dichotomy

For fixed C>=0 let M_C(N)=sup Q_C(f) over nonconstant signs on at most N relevant bits (constants can be added harmlessly). Every finite N has a finite supremum, because there are finitely many labelled truth tables after removing dummies.

If FEI(C) holds universally, all actual children also satisfy H<=CI. Hence sigma_i>=0 for every f, and weighted averaging gives

    Q_C(f)=min_i B_i/d_i<=B(f)/I(f)<=H(f)/I(f)<=C.         (5)

If FEI(C) fails, fix any seed with delta>0. For t=floor(N/n), (4) shows

    liminf_(N->infinity) M_C(N)/N >= delta/(n d_max)>0.   (6)

Thus the following are EQUIVALENT at the EXACT SAME C:

    universal FEI(C);
    sup_f Q_C(f)<infinity;
    M_C(N)=o(N).

The converse bounded-price implication needs no additive JS constant: tensoring amplifies a positive deficit until every fixed finite corrected-price budget fails. Equation (6) is a scoped quantifier consequence of the existing signed bank, not a finite universal upper bound. In particular searching for an independent dimension-free payment of Q_C is already a same-C full-FEI task, stronger in constants than ordinary C018's K-to-K+2/ln2 comparison.

## 4. Same-C completeness even on rare, weak, full-support representatives

The positive-deficit branch of the dichotomy survives standard hardening. Fix the same arbitrary violating seed and set k_t=ceil(sqrt(t)), p_t=2^-k_t. Balance t copies with one fresh physical sign z, producing g_t=z f^tensor t. Activate g_t at one point of k_t fresh controls, with value +1 otherwise, giving A_t. This uses the previously proved activation ledger, not a new activation claim:

    H(A_t)=p_t tH(f)+2k_t p_t(2-p_t)+phi((1-p_t)^2),
    I(A_t)=p_t(tI(f)+1+k_t),
    d_max(A_t)=p_t,
    E A_t=1-p_t.

Here phi(x)=-x log2 x>=0 for x in [0,1]. In particular

    delta_C(A_t)/p_t >= t delta-C(1+k_t).                 (7)

Dimension is tn+1+k_t, every old relevant bit is still relevant, and (2),(7) give a corrected price at least linear in t. Yet I(A_t)->0, every influence tends to zero, and mean tends to +1. H/I tends to the original seed ratio. This does not admit into child-certified roots; its debt is precisely what Q_C records.

For full Fourier support, add two dummy bits to A_t and flip one physical vertex. Call the actual result E_t on N_t=tn+k_t+3 bits. The coefficient change alpha_t=2^(1-N_t) is strictly smaller than the minimum old nonzero Walsh coefficient, at least 2^(1-(N_t-2)); all old zeros become nonzero and no coefficient can cancel. This is the old full-support hardening argument.

Every influence changes by at most alpha_t, so d_max(E_t)<=p_t+alpha_t and |I(E_t)-I(A_t)|<=N_t alpha_t. Spectral total variation is at most 2*2^(-N_t/2); maximal-coupling entropy continuity yields |H(E_t)-H(A_t)|<=h2(v_t)+N_t v_t for large t, v_t=2*2^(-N_t/2). Since N_t is linear in t whereas k_t=O(sqrt(t)), this error and N_t alpha_t are o(p_t). Thus

    delta_C(E_t)/p_t >= t delta-C(1+k_t)-o(1),
    liminf Q_C(E_t)/N_t >= delta/n>0.                   (8)

The mean perturbation is at most alpha_t, and I(E_t)->0. H(E_t)/I(E_t)->H(f)/I(f). Hence for ANY fixed thresholds tau,eta in (0,1), the class of full-spectrum-support Boolean signs with I<=tau, max_i d_i<=tau and E f>=1-eta contains these representatives eventually. A dimension-free or o(N) upper bound on Q_C even on this restricted class forces universal FEI(C); universal FEI(C) implies the bound <=C there. The finite tradeoff is proved analytically, without running a growing-dimensional truth-table search. This strengthens the hardening admission ledger for the debt-corrected endpoint rather than treating rare/weak/full support as structural payment.

## 5. Independent reconstruction of A005's exact stated claim

For a FIXED seed padded to N bits and flipped at zero, let alpha=2^(1-N), eta=f(0), and a_S its normalized seed coefficients. The edited coefficients are a_S-eta alpha on seed-only frequencies and -eta alpha otherwise. They never cancel once at least two dummies are present. A fresh j has d_j=alpha and

    B_j=2 alpha^2(2^(N-1)-2^n)
          +sum_(S subset[n]) Phi((a_S-eta alpha)^2,alpha^2).

Using Phi(x,y)<=y log2(e(1+x/y)) bounds the finitely many exceptional packets by O_f(N alpha^2), so B_j/d_j->2. Old B_i and their positive influence denominators converge by entropy/marginal continuity. A fresh physical child is clean padded seed on one branch and the point-edited seed in dimension N-1 on the other. Thus sigma_j=-(delta(f)+delta(F_(N-1)))/2->-delta(f). Old sigmas converge to seed sigmas; strict positivity gives the stated eligible-minimum conclusion. Continuity of max at zero gives old corrected-price convergence without a seed-slack positivity hypothesis, while every fresh corrected price is asymptotic to delta(f)/alpha. This independently proves A005's full stated transport/eligibility scope without asserting acceptance of the broader A061 lambda/drift theorem.

The finite witness is independently reconstructed from all physical values and child spectra: three-bit point defect padded to N=12 then flipped at zero, C=8/3. Exact rational logarithm intervals certify positive root delta, old individual slacks zero/positive and old B_i/d_i>5/2; fresh individual slacks both negative and B_j/d_j<5/2. This root is NOT minimal. Review verdict HOLDS at A005's exact stated scope, no repair contributed. The finite verification is recorded separately from the tensor/activation transport checks.

## 6. First unsupported line and mechanism boundary

No gap remains in (1)-(8) or A005's stated corollary. The first unsupported universal line is to upper-bound Q_C by any sublinear dimension envelope from an independently owned structural resource, for some absolute C, or directly exclude delta>0 on same-C certified minimal witnesses. The new equivalence says such a bound proves FEI at that same C, and all rare/weak/full-support representatives still contain arbitrary violating seed debt. It supplies neither that resource nor a finite constant. A query's already-negative sigma cannot fund its own reserve. NEXT must retain actual terminal child deficits and seek a signed-collision reserve on a genuinely critical witness; further price-clamp or padding scans are retired.
