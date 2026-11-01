# exact target, quantifiers, hypotheses and units

Compress the existing A048 actual-descendant schedule-injection obstruction, preserving a uniform Boolean function, an essential query at every reached node, the prescribed coherent root spectral lift, the actual ambient terminal Fourier set, retained terminal entropy and a single removed-influence account. Entropies are bits, influence is pivotal probability. The false extension under test is

    o/2 + [Gamma_W]_+/2 <= R/ln(2),
    o=I(Y;Pi), Gamma_W=H(Pi|Y)-H(Pi|W), R=I(F)-E I(F_leaf),

when W is allowed to be the actual adaptively labelled terminal spectrum without the root-Markov hypothesis. A047's root-compatible theorem and A050's repaired injection allowance are not refuted. Full FEI is OPEN.

We give a fixed 17-variable exact certificate, down from A048's 56-variable finite certificate. Moreover 17 is the minimum over the following explicitly restricted class: F=G(x) times parity on 2^r separate coordinates, G an arbitrary uniform k-bit Boolean core; query r distinct fixed core coordinates in order, each essential at every reached node; then query one parity coordinate indexed injectively by the full r-bit prefix and stop; use W equal to the actual ambient terminal spectral set. Here r>=1, k>=r, n=k+2^r. No minimum over arbitrary Boolean functions or arbitrary stopping trees is claimed.

# sources actually read, revisions and theorem locators

Execution protocol 2026-10-11-execution-v2 was reread in full. BOARD opening is supervisor 2026-10-14 02:53 UTC; B10 notes remain v2, 2026-10-11 23:31Z. Own STATUS, WORKLOG, LEARNED and prior census were recovered. Earlier campaign documents, registries, source trees and context-paper readings remain prior-stage provenance; this is not a new literature audit. Read A048 run 20261013T234007Z REPORT and PROOF, especially 'Family and physical tree', 'Coherent root lift and actual descendant witness' and its repair boundary. Also read A050 run 20261014T004109Z REPORT and A048 run 20261014T022727Z REPORT: the active-label repair survives and the new common-factor signed-reserve objection determines NEXT. Source paths and hashes are saved in out/SOURCE_RECEIPTS.json. The lead's older finite-block assignment was completed last stage; this stage follows protocol dispatch by consuming the saved descendant-reference objection, without reopening that census.

# complete derivation or exact first unsupported line

Encode a cube sign coordinate by (-1)^bit. Put z=(z0,z1,z2), u=(u0,...,u5), each bit uniform, and let A0=1_{u=0}, A1=1_{u=(1,0,...,0)}. Define the Boolean circuit

    N = (A0 AND ((z2=0) OR (z0=z1=1)))
        OR (A1 AND (z1=z2=1)),
    G = 1-2N,
    F = G product_{b=0}^7 (-1)^{y_b}.

The two guard events are disjoint. In least-significant-bit order z0,z1,z2,u0,...,u5, the complete negative core set is {0,1,2,3,7,14,15}; this supplies a second exact description without parameters. Query z0,z1,z2, obtain B=z0+2z1+4z2, then query y_B, obtain C and stop. Pi=(B,C) is uniform on 16 transcripts.

The undirected core crossing-edge counts in coordinate order are (1,3,5,5,7,7,7,7,7). Each crossing edge contributes 2/512=1/256 influence. Hence I(G)=49/256 and I(F)=8+49/256=2097/256. The seven reached core-query node influences are, by depth and prefix, 1/256; (1/128,1/64); (1/64,1/64,1/32,1/64). All are positive, and every y_B query has influence one. Every root coordinate is essential as well. Averaging these node influences and adding the final parity query gives R=1+(1+3+5)/256=265/256. The terminal influence is exactly 229/32, so no remaining parity influence has been discarded.

For completeness the terminal core functions comprise five one-point defects on six guard bits, two constants, and one two-point defect at {0,e0}, the last equivalent to a one-point defect on five bits and independent of u0. Thus, writing h_t=1-2*1_{0^t},

    E H(F_leaf) = (5/8)H(h_6)+(1/8)H(h_5),
    E I(F_leaf) = 7+(5/8)*6*2^-5+(1/8)*5*2^-4 = 229/32.

The root entropy is H(G), independently certified by the integer Walsh transform; its complete exact prime-log vector is in certificate.json. At least seven unqueried parity coordinates remain at every leaf. Therefore Y=F is conditionally fair given Pi, o=0 and H(Pi|Y)=4.

Use A048's coherent lift explicitly: for a parent spectral set S at query i let T=S\{i}, q_T=hat f(T)^2+hat f(T union {i})^2; choose physical outcome b with probability hat f_b(T)^2/(2q_T), and retain T. The sum of the two probabilities is one because hat f_b(T)=hat f(T)+(-1)^b hat f(T union {i}). Summing over the root law gives the physical fair outcome and the squared Fourier law in that child. Iterating gives W=S0\Q(Pi), with actual descendant laws. Zero-mass q_T pairs are not sampled.

The root parity spectrum is the deterministic full eight-label set. Consequently the parity part of W is precisely that set minus y_B, and its missing label recovers B. Its law given B does not depend on C, since changing the queried parity bit changes only a global sign. It follows exactly that I(W;Pi)=3 and H(Pi|W)=1. Therefore Gamma_W=3 and conversion=3/2 bits. Conditional on S0, W is equivalent to B: its core part is the deterministic root projection off z0,z1,z2 and its missing parity label encodes B. Hence

    e=H(W|S0)=I(W;Pi|S0)=H(B|S0)=3-I(S0;Pi).

The checker constructs the entire rational joint root/prefix/terminal law (3,740 nonzero final entries), checks all physical prefix masses and all child Fourier laws, and proves this entropy identity by exact prime-log cancellation. Fixed y0 instead of y_B gives e=0, also checked by exact cancellation. This distinguishes adaptive ambient labels from a root-conditional copy. The repaired A050 theorem carries e/2 and is respected.

The sign certificate needs only three terms of the positive atanh series. For z=1/3,

    L=2(z+z^3/3+z^5/5)=842/1215 < ln(2)
      < L+2z^7/(7(1-z^2))=23581/34020=U <139/200.

The lower bound is strict since the remaining terms are positive; the upper bound follows by replacing all remaining odd denominators by 7 and summing the geometric tail. Since L>265/384,

    3/2 - (265/256)/ln(2)
      > 3/2 - (265/256)/L
      =1353/215552 >1/256 >0.

This is a rigorous sign comparison, not a floating search. F is far from a disproof of FEI: its Fourier support has at most 512 points, so H(F)<=9 while I(F)>8 and H(F)/I(F)<9/8.

Minimum in the stated class: at depth ell<r there are 2^ell reached prefix cells. Essentiality of the queried coordinate in each cell requires at least one crossing edge in that cell. The cells are disjoint for this coordinate, giving Inf_ell(G)>=2^ell*2^(1-k). Influence on an unqueried coordinate averages exactly under restriction of other coordinates. Consequently

    R >= 1+(2^r-1)*2^(1-k).

As above conversion=r/2 for every G in the class. For r<=2, r/2<=1<R/ln(2), so no violation. For r=3 and k<=8, R>=1+7/128=135/128, whereas (3/2)ln(2)<(3/2)(139/200)=417/400<135/128; again no violation. For r>=4, n=k+2^r>=r+2^r>=20. Thus no member has n<17, and our k=9,r=3 member attains n=17. This argument quantifies over all cores in the class rather than enumerating them.

An earlier analytic 16-variable idea with a single point defect fails essentiality: after its first zero query the remaining core becomes constant. It was rejected before execution, and is not exported as an essential-tree certificate. The first unsupported global line would be removing the fixed-prefix/parity assumptions from the minimality theorem. We do not take that step. The universal FEI history-bank payment also remains unproved.

# executed validation with domain, arithmetic, commands and outputs

Frozen specification out/FROZEN_SPEC.json was written before computation. One fixed n=17 family, no symmetry reduction or dimension escalation, memory estimate 120 MB and maximum runtime 60 seconds; neither job was expected to exceed 300 MB, so no memok-gated job was launched. No GPU or background process was started.

Commands from A049: `python -X utf8 runs/20261014T025532Z-fleet05-A049-minimal-falsifier-extraction/code/certificate.py` and the same prefix with `code/reproduce.py`. Main PASS: 6,841 assertions, 1.751 arithmetic seconds. Separate representation PASS: 131,124 assertions, 1.835 arithmetic seconds. Total 137,965 assertions. The second script imports no helper code: it reconstructs the core from seven explicit negative points, uses direct signed-character sums for its Fourier coefficients, scans all 131,072 full truth-table values, and independently computes balanced physical leaf outputs and retained influence from every leaf's crossing edges. It also rechecks the rational sign and analytic minimum bounds. This is internal reproduction, not an independent agent review.

Complete truth table: out/truth_table.txt, line x+1 is F at x, with LSB coordinate order z0,z1,z2,u0,...,u5,y0,...,y7. SHA256: 7e8bc0e09ac6e7b532724ee17d8204b4d622b5c0b86c6d5938465d7a79eddd89. out/core_truth_table.json has the complete 512-entry core table. certificate.json stores exact rational influences, prime-log entropies, rational log bounds and injection information; reproduction.json records the separately reconstructed checks. All files are below 20 MB.

# proof dependencies and changed downstream conclusions

The proof above is self-contained; no external theorem is required. A048-ACTUAL-DESCENDANT-SCHEDULE-INJECTION v1 is the existing obstruction being compressed, not a newly refuted named theorem. A047's root-Markov conversion and A050-ACTIVE-LABEL-SCHEDULE-REPAIR v1 remain unchanged. B10 can reproduce the essential-tree obstruction with one seven-point core rather than four separate rare-defect blocks. The new minimum is conditional on the explicit construction class; no arbitrary-tree minimum is asserted. Review cap respected: this repairs and verifies an existing mechanism rather than opening another broad potential.

# one next mathematical action and independent reviewer

NEXT: minimize A048's newer common-factor signed-reserve obstruction after one actual data reveal, retaining its full terminal law and the negative signed residual in one common-row reference. A048 is primary independent reviewer of this compression; A074 or A092 can reproduce the essential-edge minimum and sign. These are local handoffs, not sent messages. Independent review is pending.

# actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, identical PACKET_DELTA.json, both scripts, frozen specification and exact outputs are saved in this assigned run. STATUS has two lines; WORKLOG and LEARNED are appended. out/PERSISTENCE.json records local sizes and SHA256 values; out/SOURCE_RECEIPTS.json records read-only source provenance. No local save blocker. Supervisor copying, remote mirrors, canonical adoption and downstream use are not verified or claimed.

**Universal bridge:** This stage moves C024 history transfer by compressing the known actual-descendant scope failure from 56 to 17 variables, proving 17 minimal in the essential fixed-prefix/parity class, and exposing the adaptive-label injection without irrelevant queries or a discarded terminal budget. It does not improve a universal FEI constant or pay the remaining C019 conditional history bank. What remains is a single signed common-row account that pays history together with retained terminal entropy; NEXT attacks the newer shared-core signed-reserve objection with the smallest exact data-reveal certificate, so it sharpens that surviving universal interface rather than treating another finite class as a solution.
