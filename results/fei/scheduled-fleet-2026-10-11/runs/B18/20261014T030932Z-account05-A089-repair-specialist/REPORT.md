# A089 stage 4: one-use payment for the complete oriented composition ledger

## exact target, quantifiers, hypotheses and units

Entropy and logarithms are in bits. For every actual nonconstant Boolean core g on any finite uniform physical cube, iterate the matched six-input gate h negative on {0,1,2,4,8,16,32,6,17,40}, always on six disjoint identical copies. At each level let p be the smaller output probability, orient it negative, and use that orientation when p<=7/32, its complement otherwise. Reorient the output to its minority; this preserves its squared spectrum and influence. Write R(g)=H(g)/I(g) and Q for the total outer pivotal probability. Every level is finite-dimensional and Boolean.

The theorem proved here is, for EVERY finite depth d,

    -322/15 <= R(g_d)-R(g_0) <=1088/15<73.

The moderate prefix alone has signed correction in [-50/3,172/3], uniformly even when its duration grows without bound near the irrational bias fixed point. The rare tail has correction in [-24/5,76/5], improving A075's +16 bound. The exact starting entropy remains present. This is a composition ledger, not a physical restriction-tree payment or an absolute FEI bound.

## sources actually read, revisions and theorem locators

Read all EXECUTION_PROTOCOL.json, revision2026-10-11-execution-v2; BOARD.md supervisor snapshot2026-10-14 02:53 UTC; B18 STREAM_NOTES.md v2 unchanged since2026-10-11 23:34; own STATUS.md. The lead's lex/raw-five-bit target is already closed at its assigned scope. A084/A075 have now closed the continuum orientation policy, so repeating our previous NEXT would duplicate finished work. This stage consumes their new terminal-payment gap instead.

Read A084 run20261014T000747Z PROOF.md and CLAIMS.json, continuum policy, bias equations and terminal identity. Read A075 run20261014T005346Z REPORT.md, PROOF.md and CLAIMS.json, especially Sections4-5 (finite but unbounded moderate duration; retained rare entropy), its local independent acceptance of A084@1, and the explicitly unpaid moderate prefix. Read A072 run20261014T020611Z REPORT.md and PROOF.md, summable rare escape and repeated-excursion warning. Read A080 run20261014T005622Z REPORT.md, actual rare high-E obstruction. Read our prior192-bit arithmetic helper; only our own code is copied/imported. Sources and exact consulted files are hashed in out/SOURCES.json. Earlier campaign and manuscript readings remain prior context; no new literature or full continuum audit is claimed.

## complete derivation or exact first unsupported line

### Original failed statement, counterexample and failed payment step

The false unguarded statement remains visible: every recentered reserve is nonnegative, or some common output sign always preserves E(g)>K. The actual six-bit point defect has E>9/4, while both common-sign36-bit compositions under h have every coordinate ratio<9/4. Our previous run's out/FIXTURES.json independently certifies it; that source is pinned again. The new A080 actual1296-bit circuit even has E>669/200 in the rare band and both next common signs fall below that threshold. Its circuit is source context, not independently re-reviewed here. These counterexamples do not refute FEI or A084's correctly restricted continuum theorem.

The payment gap being repaired is the unsupported step: finite termination of the moderate prefix supplies a dimension-independent bound by summing a fixed cost per level. Near the irrational fixed point the number of levels is not uniformly bounded. The replacement uses reciprocal influence, which decreases geometrically during the long segment, and charges each signed correction once. No uniform duration assertion is needed.

### Exact signed terminal identity

At an oriented input negative probability a, set m=1-2a, v=1-m^2 and

    q(a)=2a(1-a)^3(2-a), Q(a)=6q(a).

Let pi_T be the normalized biased Fourier masses of the actual gate, and let rho be the core's normalized nonempty Fourier law. A physical spectral set uniquely specifies its occupied blocks and the nonempty inner sets. Entropy chain rule and independent physical pivotal edges therefore give

    H(g')=Q(a)H(g)+C(a), I(g')=Q(a)I(g),
    C(a)=H_a(h)-Q(a)h2(v),
    R(g')-R(g)=C(a)/(Q(a)I(g)).                 (1)

Output complements affect none of these quantities. Every core's complete H(g), including its constant spectral mass, is retained. There is no discarded core remainder, hypothetical spectral law, or incoherent square of a signed sum. The code reconstructs biased outer masses from the actual integer Walsh table and verifies (1) against all14 nonconstant two-bit cores composed on12 physical bits.

### Scalar entropy envelopes

The outer spectral-set membership marginals are vq(a). Subadditivity and

    h2(vq)<=q h2(v)+v h2(q)

imply C(a)<=6v h2(q). The scalar inequality follows because the right side minus the left vanishes at q=0,1 and has second derivative -v(1-v)/[ln2(1-q)(1-vq)]<=0. Endpoint values follow by continuity. Also H_a(h)>=0 yields C(a)/Q(a)>=-h2(v)>=-1. Thus

    -1<=C/Q<=v h2(q)/q.                       (2)

We use h2(q)<=q log2(e/q). These are actual spectral entropy bounds, not an asserted entropy ratio bound for arbitrary cores.

For a minority probability p in [delta,1/2], delta=1/16, edge isoperimetry gives I(g)>=2p log2(1/p)>=1/2. The second inequality follows by concavity of2p log2(1/p) and its endpoint values1/2 and1. For completeness the first follows by entropy tensorization of1_A, A the minority set: Ent(1_A)=p log2(1/p), while averaged two-point fiber entropy is1/2 precisely on crossing fibers. Their sum is I(g)/2. Tensorization follows inductively from the entropy chain rule and log-sum convexity. Thus no FEI premise enters the influence normalization.

### Uniform payment for the long moderate segment

Put c=7/32. Ordinary moderate steps use a=p in [delta,c]. The pivotal polynomial has

    q'(p)=2(1-p)^2(2-10p+5p^2)>0

throughout this interval, since the last factor decreases there and equals53/1024 at c. Consequently

    Q(p)>=Q(delta)=313875/262144>rho=19/16.

Furthermore

    v/q=2/[(1-p)^2(2-p)]<=65536/35625<2.

Since h2(q)<=1, (2) gives -1<=C/Q<=2. Define the decreasing potential

    Delta_s=1/I(g_s)-1/I(g_(s+1))=(1-1/Q_s)/I(g_s)>0.

Because1-1/Q_s>=3/19, the exact increment (1) obeys

    -(19/3) Delta_s <= C_s/(Q_s I_s) <=(38/3) Delta_s.  (3)

Summing telescopes; it does not repeatedly spend the starting influence. Any consecutive ordinary segment, of any finite length, has total bill in

    [-(19/3)/I_start,(38/3)/I_start] subset [-38/3,76/3].

This also bounds every partial segment or a hypothetical infinite residence at the fixed point. Physical influence grows by at least rho each step. Finite termination alone was insufficient; reciprocal influence supplies the missing uniform payment.

### At most two complemented steps

Exact gate enumeration gives the minority updates

    tau(p)=12p^2-28p^3+27p^4-12p^5+2p^6 for p<=c,
    b(p)=p^4(3-2p^2) for p>c.

They are the actual minority branches: tau(c)<3/8 and b(1/2)=5/32<c. A possible INITIAL complemented step therefore enters the ordinary interval. After the ordinary segment either the core is rare, or its first crossing above c is at most tau(c)<3/8. One FINAL complemented step then has

    b(p)<=b(3/8)=7047/131072<delta.

Thus the entire moderate prefix has at most ONE ordinary segment and TWO complemented steps. Counting two long ordinary segments would unnecessarily weaken the payment.

At a complemented step a=1-p, c<p<=1/2. Its multiplier is

    Q(1-p)=12p^3(1-p^2)>=1003275/8388608>1/9.

The polynomial increases on this interval. Hence q>1/54 and, from (2),

    C/Q<=v log2(e/q)<=log2(e/q)<8,

using e<3 and54e<162<256. With I>=1/2, each complemented step has bill in[-2,16]. Combining with (3) proves the moderate prefix bound

    -50/3 <= total moderate correction <=172/3.       (4)

Every actual dyadic starting bias enters the rare band in finite time. On(0,c], tau is strictly convex, so tau(p)/p increases and has one positive fixed point p* between delta and c. The divided fixed-point polynomial is2p^5-12p^4+27p^3-28p^2+12p-1. The rational root theorem allows only +/-1,+/-1/2, all OUTSIDE that interval, so p* is irrational. Dyadic iterates cannot equal it. Below p* they eventually cross delta downward; above it they eventually cross c upward. This reproduces the termination argument, while (3) supplies the previously missing uniform price. In fact the ledger bounds hold for partial prefixes without using termination.

### Independent rare-tail payment, with a sharper upper constant

For0<p<=delta the minority policy uses a=p. The output minority tau(p) satisfies0<tau(p)<=12p^2<=3p/4: the positive event requires an unmatched pair among the12 unmatched input pairs. Also3p<=q(p)<=4p. Let the tail start at g_*, and set r_s=I(g_s)/p_s. Poincare I>=Var(g)=4p(1-p) gives r_0>=15/4, while (1) and tau<=12p^2 give

    r_(s+1)>=3r_s/2.                              (5)

Here is a direct proof of the improved upper envelope C(p)<342p^2. Let w=Var_p(h)=4tau(p)(1-tau(p))<=48p^2. There are at most63 nonempty outer spectral atoms, so

    H_p(h)<=h2(w)+w log2(63)
            <=48p^2 log2(63e/(48p^2)).

The last inequality uses h2(w)<=w log2(e/w) and monotonicity in w<=1. Meanwhile

    Qv=48p^2(1-p)^4(2-p)>=96p^2-432p^3,
    h2(v)>=v log2(1/v), log2(1/v)>=log2(1/(4p)).

Subtracting these positive lower bounds gives

    C(p)<=p^2[48 log2(63e/48)+192
                   +432p(log2(1/p)-2)]<342p^2.

Indeed63e/48<4, and p(log2(1/p)-2) is increasing up to delta and is at most1/8 there. Its derivative is log2(1/p)-2-log2(e)>0, since log2(e)<3/2. The elementary constants e<3 and ln2>2/3 follow from their positive series. This estimate uses no numerical bias sampling and no source theorem dependency.

For the lower envelope, in the biased expansion pi_T=v^|T| c_T^2, the raw coefficient c_T is the biased average of a mixed Boolean derivative. Such a derivative lies in[-1,1], so |c_T|<=1 and pi_T<=v^|T|. Therefore

    H_p(h)>=sum_T pi_T |T| log2(1/v)=Qv log2(1/v),
    C(p)>=-Q[-(1-v)log2(1-v)]>=-Qv log2(e).

This retains the distinction between the one-atom entropy -(1-v)log(1-v) and binary entropy h2(v); replacing h2(v) itself by v log2(e) would be false. Using v<=4p and log2(e)<3/2, (1) gives the signed tail envelopes

    -6/r_s <= C_s/(Q_s I_s) <=19/r_s.

Equations(5) and r_0>=15/4 sum a single geometric ledger:

    -24/5 <= total rare correction <=76/5.          (6)

The bound covers EVERY finite tail depth and counts each C_s exactly once. This independently proves and sharpens the entropy part of A075's tail bound; it does not re-review its erasure-loss constant.

### Complete result and honest universal boundary

Summing (4) and (6) gives, at every finite depth of the fixed policy,

    R(g_0)-322/15 <=R(g_d)<=R(g_0)+1088/15.

If the starting core is already rare, (6) alone applies. If the selected depth is inside the moderate prefix, (4) applies and implies the displayed wider bound. The exact bill is sum C_s/(Q_s I_s), and equivalently H(g_d)/(product Q_s)-H(g_0)=I(g_0) times that bill. Thus a single starting influence normalization suffices; no terminal entropy is erased. Every finite core is explicit by recursion, with no infinite Boolean function required.

The first unsupported universal line is an ABSOLUTE bound on the starting rare-core E or H/I, or a different operation whose surplus is paid from an independently certified terminal-core reserve. This fixed policy cannot turn a single finite seed into an unbounded H/I disproof: its entire orbit stays within the additive constants above. The theorem does not price arbitrary alternating uses of A072's one-flip escape, arbitrary shared-data insertions, or physical restriction trees. The warning about uncontrolled repeated excursions survives outside this named policy. Full FEI remains OPEN.

## executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json precedes the moderate pilot and physical job. The successful pilot checks99 exact symbolic/biased assertions in0.1174581 seconds, including all six pivotal polynomials, threshold/fixed-point facts, reciprocal-influence constants,32 exact bisections, and seven rigorous signed entropy profiles. The physical job checks57568 assertions in1.4673537 seconds on all14 nonconstant two-bit cores, all57344 parent Fourier coefficients, all168 physical coordinate influences, Parseval, and the exact hierarchical entropy formula. Coefficient/edge identities are exact rational equalities; entropy identities are analytically proved and separately enclosed by overlapping outward intervals, not asserted from floating equality.

out/RARE_SPEC.json precedes the additional rare check. It checks390 exact assertions in0.0607992 seconds on five frozen biases2^-r,r=4,...,8: all raw coefficient bounds, six marginals, both signed C envelopes and combined rational constants. Total successful recorded assertions:58057, comprising58043 exact mathematical predicates and14 runtime-cap predicates. The exact proofs, not the finite fixtures, supply all-bias/all-depth quantifiers.

Commands from A089:

    python -X utf8 runs/20261014T030932Z-account05-A089-repair-specialist/code/check.py --pilot
    python -X utf8 runs/20261014T030932Z-account05-A089-repair-specialist/code/check.py
    python -X utf8 runs/20261014T030932Z-account05-A089-repair-specialist/code/rare.py
    python -X utf8 runs/20261014T030932Z-account05-A089-repair-specialist/code/persist.py

One initial pilot failed at an unnecessarily strong diagnostic asserting that all rational-root candidates were nonroots: p=1 is a root, outside the relevant interval. out/FIRST_CHECK_FAILURE.md preserves it. The corrected check asserts the actually needed domain exclusion; the successful rerun does not change the theorem, cases or arithmetic. No failed assertion is counted as accepted.

Arithmetic is integer Walsh, Fraction polynomials, and own192-bit outward logarithms with80 positive atanh terms and the proved tail18/[8*161*3^161]. Jobs are serial, capped55 seconds, estimated<=100MB, with no job expected above300MB and no memok override. No GPU, full large-circuit table, automatic dimension escalation or background process was used. Memory estimates are not measured peaks.

## proof dependencies and changed downstream conclusions

The new signed entropy theorem has no unreviewed proof dependency: actual biased expansion, physical influence, scalar entropy envelopes, bias dynamics and both terminal payments are independently reconstructed above. A084's E-monotonicity and A075's kappa<0.914 remain external reviewed/pending claims at their recorded scopes; they are not premises of this H/I payment theorem. Applying our completed entropy ledger alongside their selectable-erasure localization retains their original review status.

A075/A072/A084/A089 can remove the unpaid moderate-prefix entropy clause for THIS fixed policy. A075's rare upper entropy price16 can be replaced by76/5, with the same lower24/5, using this independent proof. No universal FEI constant follows because R(g_0) is still present. A080's actual rare high-E counterexample and both-sign failures survive. New narrow repair claim is author-proved pending independent review; no shared registry is changed.

## one next mathematical action and independent reviewer

NEXT: use A075's localized rare-core reduction and the now-complete retained entropy ledger to identify a noncircular terminal-core constraint beyond |beta_i|<=min(Inf_i,2p) that bounds E, or permits an owned negative-reserve payment. Test that constraint on A080's existing high-E rare circuit, retaining the full conditional law and seed entropy. A075/A072 should independently reconstruct the reciprocal-influence potential and one-segment/two-complement count; A074/A092 should check the raw-derivative lower entropy bound and improved rare envelope. Arbitrary repeated-excursion pricing is a separate mechanism, not a reason to leave this fixed-policy bill open.

## actual persistence receipts or precise save blocker

The four protocol files, proof, code, frozen specs, exact outputs and failure record are saved only in the requested A089 run. out/RECEIPTS.json binds source/artifact hashes and sizes, schemas, delta equality and runtimes. Rolling STATUS.md has two lines; WORKLOG.md and LEARNED.md are current. Independent review, shared adoption, supervisor copy, remote mirror verification and downstream use remain pending. No other agent folder, shared tree, brain or repository was written.

## Universal bridge

This stage moves B18/B15's signed-admission/retained-terminal bridge adjacent to C018 by closing the moderate-prefix entropy payment uniformly in arbitrary core dimension and duration, then proving a complete one-use signed composition bill in[-322/15,1088/15] at every finite depth of the existing localization policy. It improves the rare-tail upper price16 to76/5 and moves no absolute FEI constant or C019 physical stopping-tree payment. What remains is the localized actual rare-core erasure bound or an independently certified terminal surplus; the starting H/I cannot be discarded. NEXT attacks that precise universal bottleneck on the existing high-E rare fixture, which is shorter than another sign grid, depth search, or repeated payment of a now-closed prefix.
