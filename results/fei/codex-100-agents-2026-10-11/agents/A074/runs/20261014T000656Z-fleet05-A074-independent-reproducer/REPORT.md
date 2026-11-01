## exact target, quantifiers, hypotheses and units

Independently review A075-SPARSE-MATCHING-HEREDITARY-CLOSURE@1. For k,l≥0, r=2k+l, let A consist of zero, every unit vector and k disjoint matched weight-two points, and f=1-2 1_A on the uniform r-cube. The target is every relevant coordinate of every physical restriction, including cube isometries, output sign and dummy padding:

    B_i=H(S_i|S_-i) ≤ K6 Inf_i,
    K6=16/3-(21/8)log2(3)+(95/24)log2(5)
             -(121/24)log2(11)+(65/24)log2(13).

Also review the source's perfect-matching limits E→2,H/I→4, terminal-inclusive stopping-tree ledger, and graph/path root upper bounds. Entropy is in bits; spectral membership and physical inputs are different random variables. No universal Boolean erasure bound is claimed.

## sources actually read, revisions and theorem locators

Read BOARD supervisor snapshot2026-10-13 23:59 UTC, B15 STREAM_NOTES v2 dated2026-10-11 23:25 UTC, own STATUS and LEARNED. The lead's explicit A074 witness/census direction was completed last stage; protocol dispatch therefore resumes our productive NEXT and consumes A075's new dependency, rather than repeating a retired census. No disagreement with the lead is asserted. Execution protocol revision2026-10-11-execution-v2 reread in full.

A075 run20261013T212622Z-fleet05-A075-search-to-theorem-bridge REPORT read in full: equations2-4 spectrum/packets, actual restriction closure, equations5-8 cutoff/tree payment, equations9-10 limits, equations11-13 graph/path bounds, and first unsupported line. Its CLAIMS@1 read and preserved. A080 run20261013T212642Z-fleet05-A080-universal-counterexample-standard MATCHING_ASYMPTOTICS read in full; its partial-matching asymptotic claim is context and not independently accepted here. After the completed proof check, A072 run20261013T222130Z-fleet05-A072-exact-walsh-engine REPORT was read in full to source the next target: equations1-3 signed reserve/terminal correction,23 sparse-orbit covering and the common-output-orientation guard. This does not issue acceptance of A072's new claim. Prior context-paper/source consultation remains context, not a premise. No other agent code is imported or executed. Current source bytes and scope are pinned in out/source_receipts.json.

## complete derivation or exact first unsupported line

**Independent representation.** Write t_i=(-1)^(1_(i∈S)). For each matched pair its contribution to the negative indicator's character sum is t_i+t_j+t_i t_j:3 once and−1 three times. An isolated coordinate contributes1 or−1 once each. The multiplicities of the sum z are coefficients of the Laurent generating polynomial

    (z^3+3 z^-1)^k (z+z^-1)^l.

Our code constructs these coefficients by repeated integer convolution, independently of A075's binomial (u,v) enumeration. The indicator sum at S is1+z. Nonempty Fourier coefficients are−2(1+z)/N with N=2^r. At the one empty index replace the formal−2a/N by1−2a/N, a=1+3k+l. The squared-Walsh histogram therefore removes exactly one4a² atom and inserts one(N−2a)² atom. Counts and Parseval are verified exactly.

To reconstruct a paired coordinate's conditional law, convolve the other k−1 pairs and all l isolates. If their sum is z, put u=1+z. The target pair contributes joint squared-Walsh packets(4(u+3)²,4(u−1)²) when its partner is absent and(4(u−1)²,4(u−1)²) when present. For an isolated direction, use the other k pairs and l−1 isolates and packet(4(u+1)²,4(u−1)²). The unique empty packet receives the same exceptional replacement. These are joint probabilities after division by N², not an arbitrary realizability relaxation. Erasure is summed directly as−p0 log2(p0/q)−p1 log2(p1/q), q=p0+p1. Our second representation visits the actual negative physical points and directly sums characters, without a Walsh butterfly. Signed spectra, packet multiplicities and physical edges reconcile for every directly checked root.

A paired direction has two internal negative edges and an isolated direction one. Hence crossing counts areδ=a−4 andδ=a−2 respectively, Inf_i=2δ/N and fhat({i})=−2δ/N. The checker separately counts disagreeing physical edges and reconciles spectral influence.

**Restriction closure.** If all fixed inputs are zero, intact pairs remain pairs and broken pairs leave isolates. If exactly one fixed input is one, the only possible negative free assignments are zero and its free partner's unit vector; the latter coordinate is a dummy of a point defect. Two fixed ones leave a point defect only when they form a matched pair, otherwise a constant; three or more fixed ones leave a constant. Degenerate full-negative small cubes are constants too. This exhausts simultaneous histories. Further point-defect restrictions retain point defects/dummies/constants. Our classifier predicts the negative residual set from this argument and compares it with direct conditioning of the original physical point set at every history through six bits.

**All-dimensional cutoff.** For any spectral law let q0=fhat(empty)² and qi=fhat({i})². Every ordinary erasure packet is at most its mass. The exceptional empty-remainder packet is at most qi log2(e(q0+qi)/qi), because x log2(1+y/x)≤y/ln2. Therefore

    B_i ≤ 1−q0−qi+qi log2(e/qi).

For this family qi=4δ²/N² and1−q0≤4a/N. Using1/ln2<3/2 (the positive atanh expansion of ln2 has first term2/3 and positive remainder) gives, for r>3,

    B_i/Inf_i ≤ U(r)=2+8/(r−3)+(3r+2)(2r+3/2)/2^r.

Hereδ≥r−3,a≤1+3r/2 and2a/δ≤2+8/(r−3). We verify U(13)=240651/81920<368/125<K6. The rational term decreases. For P(r)=(3r+2)(2r+3/2),

    2P(r)−P(r+1)=6r²−(7/2)r−23/2>0 for r≥13,

since it is positive at13 and has positive derivative thereon. Thus U decreases for every r≥13. The remaining r≤12 comprise49 parameter pairs including the zero-dimensional constant,76 relevant coordinate orbits. Exact rational intervals certify75 strict inequalities; the single equality orbit(k,l)=(3,0) represents all six coordinates and is checked by exact cancellation into the stated K6 prime-log expression. No overlapping numerical interval is used to assert equality.

Point-defect descendants on s non-dummy variables have d=2^(1−s) and

    B_i/d=2−2d+Phi((1−d)²,d²)/d
         ≤2+d(2s−4+log2 e).

At s=1 erasure is zero, at s=2 the bound is<11/4, and for s≥3 the correction2^(1−s)(2s−5/2) decreases from its value at3. This yields B_i/d<23/8<368/125<K6. Therefore the finite certificate plus analytic tail and closure prove the sharp bound at every descendant. Dummy directions are irrelevant; cube reflections/output sign preserve squared spectra and coordinate permutations merely relabel ratios. Equality is precisely the six-variable three-pair core up to these operations. This also proves sharpness for min_i B_i/Inf_i and aggregate B/I within the class.

**Stopping ledger, with terminals.** For any actual physical split, parent Fourier amplitudes u,v give child amplitudes u+v,u−v; averaging child squared laws gives q=u²+v². Entropy chain rules give Δ_iH=B_i+JS_i. In natural units the JS packet is q d(2uv/q), where d(z)=((1+z)ln(1+z)+(1−z)ln(1−z))/2. The bound d(z)≤1−sqrt(1−z²) follows from atanh(z)≤z/sqrt(1−z²): both vanish at0 and the derivative of the latter is(1−z²)^−3/2≥(1−z²)^−1, the derivative of atanh. Evenness handles negative z. Thus JS_i≤(2/ln2)sum min(u²,v²)≤(2/ln2)Inf_i. The ordinary influence identity is I=Inf_i+average I(children). Applying the hereditary bound and telescoping gives for every stopping tree

    H(f)≤E H(leaf)+(K6+2/ln2)[I(f)−E I(leaf)].

Our split checks reconcile signed child coefficients, mixed squared laws and retained physical influence at every actual node through six bits. The general argument retains both terminal quantities and spends each removed physical coordinate once. It does not assume zero-entropy leaves for an arbitrary stopping tree.

**Limits and adjacent mechanisms.** For perfect matchingsδ=a−4 and r=2k. The same scalar inequality proves x²+y²−Phi(x²,y²)≤(|x|−|y|)²/ln2. Partner-present packets have zero deficit; the other amplitude differences are at most8/N on at most N/4 rows. Consequently

    2a/δ−2(a²+δ²)/(δN)−8/(δ ln2)
       ≤E≤2a/δ+(2δ/N)(2r+3/2),

so E→2. With T=1−q0, every nonempty Fourier numerator is a nonzero integer of magnitude between2 and2a, and the empty entropy is at most T/ln2. Hence T(2r−2−2log2 a)≤H≤T(2r−2+1/ln2). Dividing by I=2rδ/N proves H/I→4. These are analytic limits, not finite trends.

For a graph-edge negative set,δ_i=a−2(1+degree_i) is again both the boundary count and singleton numerator parameter. A minimum-degree vertex hasδ≥a(1−4/n) for n>4; a≤(n²+n+2)/2. The same empty-packet bound gives the source's E≤2+8/(n−4)+(n²+n+2)(2n+3/2)/2^n. Its value at16 is551825/196608<368/125; monotonicity follows from2Q(n)−Q(n+1)=2n³−(5/2)n²−(15/2)n−8, positive and increasing for n≥16. A monotone path of length m has boundary m−1 in active directions and m+1 outside, and singleton parameter2i−m−1 in active direction i (one-based). If m<n choose an outside direction; if m=n choose a middle direction with singleton parameter of magnitude≤1. This yields precisely the source's two path bounds. At10 these are2521/1024 and22571/9216, both<368/125; the quadratic-tail difference4n²−n−8 and decreasing rational factors prove monotonicity thereafter. Smaller fixed dimensions have finite granularity bounds. Thus neither adjacent root mechanism can produce unbounded E. These graph/path root conclusions are not transferred to arbitrary descendants.

No unsupported line remains in A075's scoped claim. The first unsupported universal line is a uniformly paid signed collision/admission reserve for a non-sparse arbitrary inner Boolean core, at its actual bias and every newly relevant coordinate, with complete terminal entropy. The sparse-family theorem supplies none of that operation.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json saved before the job. Pilot:49 compressed parameter cases,319 histories through four bits,12 labelled graphs through three bits and10 paths;4709 exact assertions,zero failures,1.7625767 seconds. Full:49 compressed cases/76 relevant orbits/one exact equality orbit;3964 histories through six bits and7438 actual split checks;1100 labelled graphs through five bits and28 paths through six bits;131327 exact assertions,zero failures,0.8842519 seconds. Runtime variation reflects the shared machine and cache/data workload; no resource throughput is inferred. Estimated memory100 MB, not measured; no job expected>300 MB, no GPU or automatic dimension increase. Caps55/180 seconds. Commands:

    python -X utf8 runs/20261014T000656Z-fleet05-A074-independent-reproducer/code/review.py --pilot
    python -X utf8 runs/20261014T000656Z-fleet05-A074-independent-reproducer/code/review.py

Mathematical arithmetic uses integers/Fractions. Logarithms use40 terms of ln x=sum(1−1/x)^j/j on1≤x≤2, with remainder≤t^41/[41(1−t)], positive-ln2 interval division and dyadic range reduction. Signed weights reverse endpoints. This differs from A075's80-term atanh implementation. No floating entropy sign or extra precision refinement is used. All compressed cases and completed root/history domains are saved immediately in out/. Point-set classification and graph/path formulas were independently reconciled, rather than importing another script's spectra.

## proof dependencies and changed downstream conclusions

The proof uses only elementary character orthogonality, conditional entropy, edge counts, the explicitly reconstructed scalar inequality and the stated log remainder. A075's computed certificates are not premises: the finite remainder is independently recomputed. Its unchanged statement/version/hash receive an ACCEPT_AT_STATED_SCOPE review in local CLAIMS.json. The source's administrative hypothesis text 'Independent review is pending' is retained verbatim for provenance; our added review record records the new local acceptance. No substantive mathematical repair was supplied, so this is an independent review rather than a contributor acceptance. A080's broader uniform partial-matching limit claim is not separately accepted. Shared index adoption remains pending. Full FEI remains OPEN; no new broad candidate is opened.

## one next mathematical action and independent reviewer

Independently reconstruct A072's23 sparse cube-isometry orbits and strict E<14/5 signs, then audit its common-output-orientation repair for six-bit cores with E≥14/5. Source equation1 is B_(j,i)=q B_i(g)+R_p(beta_i²), and equation3 retains H(F)=6q H(g)+C_p, I(F)=6q I(g). Check one orientation works for every coordinate, retaining the signed empty row and full terminal correction C_p; the finite guard may not be reapplied to the resulting36-bit core without a new proof. This changes to the live mechanism after closing the sparse-family review and avoids another dimension census. A085/A092 should challenge the generating-polynomial cutoff and closure certificate here; A075/A072/A080 and B15/B20 can consume the scoped acceptance.

## actual persistence receipts or precise save blocker

REPORT, CLAIMS, PROGRESS and byte-identical PACKET_DELTA with packet_ids=[A074], FROZEN_SPEC, INDEPENDENT_REPRODUCTION.py, REPRODUCTION_REPORT.json, code and exact outputs saved in the assigned A074 stage directory. STATUS is two lines; WORKLOG and LEARNED are appended. Finalizer checks protocol field sets, preserved statement/version/hash, all local artifact sizes<20 MB, summary counts and standalone-script equivalence; out/manifest.json supplies hashes. Source receipts distinguish consultation from proof premises. No git, external message, brain write or other agent/shared-tree mutation occurred. Supervisor copying, remote mirror verification and independent review of this implementation are pending.

**Universal bridge:** This stage moves C018's erasure-selection diagnostics and C019's scoped stopping payment by independently accepting A075's complete sparse-matching hereditary theorem at sharp K6=2.9444953038718586..., including all actual descendants and terminal entropy. Its finite certificate is reconstructed with131327 exact assertions,3964 histories and the proved r≥13 cutoff; the perfect-matching and adjacent graph/path dimension-growth mechanisms are analytically retired. It improves no universal FEI constant: an arbitrary-inner-core signed admission/payment reserve with one physical budget remains unpaid. NEXT audits A071/A072's actual signed f6 admission signatures and high-E guard, because that is the live gain-changing transfer beyond the closed sparse geometry, rather than another isolated finite class or repeated census.
