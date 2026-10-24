# A028 stage 2: arbitrary control indicators

Full FEI remains OPEN. The B06 lead assigned arbitrary control indicators to A028 and proper partial-core exposure to A027. This stage follows that division and extends the existing A028 stopping-payment candidate with an exact bias correction, a uniform controller-certificate bound, and an actual Boolean obstruction to correction coefficient four. No novelty claim or independent acceptance of this extension is asserted.

## exact target, quantifiers, hypotheses and units

For every finite uniform physical control cube y and DISJOINT finite uniform core cube x, let c(y) be any Boolean indicator, a(y)=1-2c(y) its sign encoding, and u(x) any Boolean sign. Define

    p=Pr(a=-1), delta=Pr(u=-1), V_a=4p(1-p), V_u=4delta(1-delta),
    F(x,y)=1+c(y)(u(x)-1).

All entropy is in bits; Fourier coefficients are normalized Walsh coefficients. H_+(f) is the unnormalized NONEMPTY contribution sum_(S nonempty) fhat(S)^2 log2(1/fhat(S)^2), not entropy conditioned on nonemptiness. I(a) denotes sign-function total influence; if influence of the 0/1 indicator is instead defined as sum E[(D_i c)^2], it is I(a)/4. This conversion is essential.

The control-first tree exposes physical y coordinates until c is determined, or simply exposes all y coordinates. Its actual weighted leaves are u with probability p and constant +1 otherwise, with irrelevant leftover controls harmless. Let Pi_H=H(F)-pH(u) be the FULL entropy path cost and Q=Pi_I=delta I(a) the queried influence. Reserved terminal influence is pI(u). We prove

    Pi_H <= delta H_+(a)+C0 delta V_a,
    C0=2+2log2(e)+log2(e)/sqrt(e)<6.

This holds for all p,delta, dimensions and actual spectra, including deterministic signs. If H_+(a)<=T[I(a)-V_a], then Pi_H<=max(T,C0)Q. If only H(a)<=K I(a) is known, Pi_H<=(K+C0)Q. Adding a terminal allowance L I(u) gives complete root constants max(T,C0,L), respectively max(K+C0,L). The terminal may itself use a paid finite stopping tree; its reserved influence is multiplied by p exactly once.

Arbitrary repeated variable occurrences INSIDE the representation of c are permitted: c is treated as one actual Boolean function, not a syntactic sum of gate charges. Sharing physical variables BETWEEN c and u, or between separate control modules, is not covered. That sharing changes the actual terminal partition and invalidates pH(u).

## sources actually read, revisions and theorem locators

Read BOARD.md (observed snapshot 2026-10-12 01:21 UTC), B06 STREAM_NOTES.md v2 (2026-10-11 23:26Z), STATUS.md and LEARNED.md at stage start. The lead explicitly assigns arbitrary indicators to A028; A027 owns partial-core exposure, so the previous NEXT is superseded by this concrete direction. EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2 was reread in full. The prior campaign/report/source scope remains as recorded in stage 1; the large terminal papers are not re-audited here.

Consumed new A024 LEARNED transport conventions (corrected H_+, deterministic child contraction, negative empty-sector subtraction), A057 stage-2 cap/ownership lessons, A023 first-event/disjoint-account lessons, A097 leaf-reference/terminal slack lessons, and B13 stream notes on exact leaf-partition costs. A027 stage-2 REPORT and CLAIMS were consulted solely to avoid duplicating its assigned partial-core theorem; none of its new quantitative bounds is a proof premise. The controller/core formulas below are independently reconstructed from the full Fourier coefficients; they are a specialization/application of the recovered disjoint-composition interfaces, not a claim to discover those general identities.

Recovered threshold paper Theorems A/C/D and Section 7 supply terminal/controller certificate examples conditional on their previously recorded scope and acceptance. A028 stage 1 supplies the retained point-control mismatch result; the stronger exact cost here is proved without assuming that result. out/source_inventory.json pins the actual consulted sources. No Brain writes, external messages, registry edits or Git operations occurred.

## complete derivation or exact first unsupported line

### 1. Exact arbitrary-controller spectrum

Write eta(t)=t log2(1/t), eta(0)=0, and phi(t)=eta((1-2t)^2). For a nonempty core set S and any control set T,

    Fhat(S,T)=uhat(S) chat(T),
    chat(empty)=p, chat(T)=-ahat(T)/2 for T nonempty.

For empty S and nonempty T, Fhat(empty,T)=delta ahat(T). The global empty coefficient is 1-2pdelta. Parseval for the indicator gives sum chat(T)^2=p, and its raw spectral entropy is

    sum_T eta(chat(T)^2)=eta(p^2)+H_+(a)/4+V_a/2.

Summing the entropy of all NONEMPTY core rows and the empty-core/nonempty-control row yields the exact identity

    H_+(F)=delta H_+(a)+pH_+(u)+G(p,delta),
    G=V_u eta(p^2)+V_u V_a/2+delta^2 V_a log2(1/delta^2).

The last term is zero at delta=0 and 1 by continuity. Thus

    Pi_H=delta H_+(a)+G+phi(pdelta)-p phi(delta).

This keeps both exceptional empty coefficients, rather than deleting the negative terminal subtraction. At p=1 it cancels to Pi_H=0; at delta=1 it gives Pi_H=H(a). These endpoint checks are also exact finite certificate checks.

Physical edge counting gives I_x(F)=pI(u), I_y(F)=delta I(a), I(F)=pI(u)+delta I(a). These are dedicated disjoint budgets. The weighted sum of actual queried control influences is Q for every control-only tree determining c; its remaining entropy is exactly pH(u). This uses the already established physical-tree telescope, not a new telescope claim.

### 2. A global bias correction without an endpoint logarithmic loss

Set b=log2(e). The function phi is C^1 on [0,1]. Away from t=1/2,

    phi''(t)=-16log2|1-2t|-24b >= -24b.

The positive logarithmic singularity at 1/2 is locally integrable and phi' is continuous there. Therefore phi(t)+12bt^2 is convex on the whole interval. Apply the convex chord between 0 and delta at pdelta, with phi(0)=0, to get

    phi(pdelta)-p phi(delta)<=12b p(1-p)delta^2=3b delta^2 V_a.

Also -ln p<=(1-p)/p gives eta(p^2)<=b V_a/2, including p=0,1 by continuity. For delta>0, divide the remaining G bound by delta V_a when V_a>0. The result is

    [G+phi(pdelta)-p phi(delta)]/(delta V_a)
    <=2b(1-delta)+2(1-delta)+3bdelta+2delta log2(1/delta)
    =2+2b+delta[b-2+2log2(1/delta)].

The scalar final term has maximum b/sqrt(e), attained at delta=1/(2sqrt(e)): differentiation gives 2log2(1/delta)-b-2=0. The continuous delta=0 limit is zero. This proves the advertised C0. The cases delta V_a=0 are obtained directly from the exact identity, so no illegal division occurs.

The inequality C0<6 is an exact elementary certificate: ln2>=56/81 and e>8/3>(8/5)^2 imply b<=81/56 and 1/sqrt(e)<5/8. Consequently C0<2+(81/56)(21/8)=2597/448<6. These inequalities are rational; no floating sign is used.

Since V_a<=I(a), H_+(a)<=T[I(a)-V_a] gives

    Pi_H<=delta T[I(a)-V_a]+C0delta V_a<=max(T,C0)Q.

Ordinary H(a)<=K I(a), together with H_+(a)<=H(a), gives (K+C0)Q. The actual terminal H(u)<=L I(u) costs pL I(u). Therefore the complete expected path PLUS terminal bound is the stated maximum against Q+pI(u)=I(F), with no reused ancestral influence.

### 3. What this does and does not say about mismatch upper bills

Pi_H is the full ACTUAL entropy decrement, the leaf-partition quantity required by B06 R2. It is not equal to the particular retained magnitude-mismatch upper bill from stage 1. At every physical query the retained KL/log charge J_v satisfies J_v<=Delta_v H. Thus sum w_v J_v<=Pi_H; adding its upper allowance 3b sum w_v mu_v costs at most an additional 3bQ. If a consumer insists on that upper bill, a valid controller-strong rate is max(T,C0)+3b, not silently max(T,C0). The stage-1 point-control bound on that particular upper bill remains unchanged.

### 4. Strong composition and arbitrary finite nesting

Let D=4pdelta(1-p)(1-delta). The physical deficit has the exact nonreuse decomposition

    I(F)-Var(F)=delta[I(a)-V_a]+p[I(u)-V_u]+D.

When D>0, the previously computed correction obeys

    G/D=2+2p log2(1/p)/(1-p)+2delta log2(1/delta)/(1-delta)
        <=alpha, alpha=2+4b<8.

The boundary cases have G=D=0 where required and follow by continuity. Thus strengthened controller/core certificates T_a,T_u compose with constant max(T_a,T_u,alpha). This is the standard disjoint FEI+ composition mechanism specialized to a negative-event conjunction, now stated with an explicit scalar gate correction and the physical stopping budgets. The scalar alpha is sharp for G/D: take actual Boolean a and u equal -1 except at one point on separate r-bit cubes, so p=delta=1-2^-r and the ratio tends to 2+4b. This is sharpness of a correction functional, not an optimal FEI constant or a disproof family.

For a strengthened constant at least b, H_+(f)<=T[I(f)-Var(f)] also implies H(f)<=TI(f), since eta((Ef)^2)<=b Var(f). Therefore finite disjoint conjunction/De Morgan expression trees inherit the indicated complete terminal-inclusive constant, with no dependence on depth. There is no claim for shared physical support.

More directly, if EACH control module has an ordinary certificate K0 and an innermost core has terminal allowance L, sequential fresh activation trees have complete constant max(K0+C0,L), independent of the number of modules. At each new activation the queried module uses Q and passes p times the existing core tree's full budget forward. Intermediate cores need not remain regular. For regular or character-regular controller and terminal modules use K0=L=C_reg, giving C_reg+C0<14.74. This is a concrete conditional application of recovered controller certificates, not a new claim that arbitrary control indicators are regular.

### 5. Point-control strengthening and a certified obstruction

For the point sign a=1-2A_r, p=2^-r, I(a)=2rp, Var(a)=4p(1-p), H_+(a)=8p(1-p)(r-1). For r=1 both H_+ and I-Var vanish. For r>=2 the bound H_+(a)<=6[I(a)-Var(a)] reduces to

    2r-8+4p(r+2)>=0.

At r=2 it is equality, at r=3 it is positive, and for r>=4 it is immediate. Consequently the arbitrary-controller theorem proves Pi_H<=6Q for EVERY unbalanced point-activated core. This improves the ACTUAL leaf-partition rate while retaining the different stage-1 mismatch-bill result.

A tax-free controller charge and correction coefficient four both fail on an ACTUAL three-bit function: take a dictator controller (p=1/2, H_+(a)=H(a)=0, V_a=I(a)=1) and core u=D_2 (delta=1/4). The root is D_3 and terminals are D_2 or +1. Direct integer spectra give

    Pi_H=3-(9/8)log2(3), Q=1/4,
    Pi_H/Q=12-(9/2)log2(3)>4.

The strict sign is the integer certificate 3^9=19683<65536=2^16. It follows that the best universal additive coefficient in Pi_H<=delta H_+(a)+Cdelta V_a is at least this exact ratio, whereas the proof gives C<=C0<6. No optimal coefficient claim is made. The finite witness does not refute FEI.

### 6. Honest universal frontier

Setting u identically -1 gives F=a, Pi_H=H(a), Q=I(a). Hence a fixed finite K paying control-first Pi_H for EVERY controller implies full FEI with the SAME K. Conversely full FEI C and the proved bias bound give a universal control-first rate C+C0. Thus this arbitrary-controller endpoint is FEI-equivalent in finiteness and cannot be declared solved by merely transferring its unpaid H_+(a).

The first unsupported line toward full FEI is a universal controller certificate, or a new structurally justified decomposition/ownership law for overlapping controllers that pays their full controller entropy and terminal cores. Allowing c and u to share inputs invalidates the exact leaf cost pH(u); no overlap extension is asserted. Further fresh nesting on one unchanged core merely combines control indicators and is not a new universal mechanism.

## executed validation with domain, arithmetic, commands and outputs

The initial out/FROZEN_SPEC.json was saved before execution. Pilot domain: every sign controller and core on dimensions 0,1,2, 484 ordered pairs, with constants and both mean orientations. Full domain fixed from the start: all 22 controllers of dimensions 0,1,2 and all 278 cores of dimensions 0,1,2,3, 6116 actual Boolean functions, maximum five physical variables; no symmetry quotient or automatic dimension escalation.

The first helper pilot passed 4380 assertions in 59.509 seconds; its receipt is out/PILOT_V1_RECEIPT.json. Before executing the refinement, out/VALIDATION_REFINEMENT.json froze outward floor/ceiling rounding of prime-log intervals to denominator 2^48 and caching of repeated bias expressions. This avoids large unrelated interval denominators while preserving certified enclosure. The amended full-job ceiling was 600 seconds, below the 30-minute campaign ceiling; estimated memory 128 MB, so the >300 MB memok condition did not apply. The improved pilot passed the identical 4380 assertions in 0.179 seconds.

Commands from A028: `python -X utf8 runs\20261012T011208Z-account05-A028-stopping-tree-payment\code\check.py pilot` and the same command with `full`. out/pilot_validation.json and out/full_validation.json record executed counts and elapsed compute time. Integer Walsh spectra and direct edge counts independently verify influences; exact Fraction vectors multiplying logs of primes verify the full entropy and gate-correction identities, including the actual sequential control tree. Rational atanh-series intervals with an explicit positive tail certify Pi_H<=delta H_+(a)+6delta V_a and G<=8D. The analytic proof supplies the sharper constants C0 and alpha and the all-dimensional scope. The coefficient-four sign is a separate exact integer certificate.

The full run passed 55068 assertions over all 6116 frozen cases in 104.698 seconds of observed elapsed Python execution, within its pre-amended 600-second ceiling. The smallest recorded strictly positive rational margin lower bound was 2829104944022891/36028797018963968. This is a finite certificate margin, not an optimal asymptotic constant.

Intervals use ln q=2 sum_(j=0..23) z^(2j+1)/(2j+1)+R, z=(q-1)/(q+1)<=1/3 after binary range reduction, with 0<=R<=2z^49/[49(1-z^2)]. Division by the positive ln2 enclosure is sign-correct; outward dyadic rounding retains enclosure. No floating result is used as an inequality certificate. Code enforces the frozen runtime cap. There are no GPU jobs, proof-assistant claims, unbounded family searches or new n=6 census.

## proof dependencies and changed downstream conclusions

The new transport uses only direct Fourier/edge algebra, the already established actual-leaf telescope, the explicit scalar convexity calculation, and elementary rational inequalities. General disjoint-composition identities are recovered prior art; the packet delta is the exact control-first bias payment, its all-endpoint C0<6 bound, the correct separation of exact path and retained KL upper bills, and the exact coefficient-four obstruction.

This is a source-complete extension/version 2 of A028's existing stopping-payment candidate, preserving the version-1 point-control theorem as an unchanged pinned component. It does not open another broad universal route while B06 has pending candidates. The old local source and claim remain immutable. A027's partial-core theorem is not duplicated or used as an unreviewed premise. A028's four stage-1 reviews remain at their original scopes; no second audit is invented here.

A023/A024/A029/A057/A064/A065/A097 can consume the controller-bias correction with explicit controller and terminal certificates. A097 reference-history costs must still retain their own posterior/reset terms; an actual Pi_H bound does not automatically bound an independently selected witness cross-entropy. Likewise a shared-control module cannot reserve the same physical bit twice merely because each individual controller has a certificate.

## one next mathematical action and independent reviewer

Derive one signed ownership correction for two activation events sharing exactly one physical control bit and acting on disjoint arbitrary core blocks. Keep the actual conditional controller functions after exposing that shared bit, full weighted core terminal entropies, and the single physical influence account of the shared bit. Consume A057/A023 ownership interfaces instead of assuming an arbitrary controller FEI bound. A087 is the independent reviewer of the extended A028 theorem and A094 should challenge its terminal/certificate interfaces. No message delivery or review acceptance is claimed.

## actual persistence receipts or precise save blocker

The designated immutable stage run contains REPORT, CLAIMS, PROGRESS, identical PACKET_DELTA, proof checkpoint, frozen/refined compute specs, checker, exact validation outputs and source pins. STATUS has two lines; WORKLOG and LEARNED are updated only in A028. out/persistence_receipt.json records observed SHA256 hashes and byte counts plus protocol field checks. Supervisor copying, mirror verification, independent review of version 2 and downstream adoption remain unobserved. No other worker folder or read-only source tree was modified.

## Universal bridge

This stage moves C019 at the lead's arbitrary-control target by replacing point-control rarity bookkeeping with an exact controller/core entropy identity and a uniform bias surcharge C0=2+2log2(e)+log2(e)/sqrt(e)<6, paying the entire control-first Pi_H plus certified terminals from separate physical budgets. It also sharpens actual point-control path payment to 6Q and certifies that coefficient four fails. The remaining arbitrary-controller certificate is explicitly FEI-equivalent; this stage does not reduce that universal gap to a solved class. NEXT attacks a single shared-control ownership correction with all arbitrary core terminal entropy retained, the shortest route beyond fresh disjoint modules because repeating controller-class examples or silently assuming controller FEI would leave the same unpaid universal entropy in place.
