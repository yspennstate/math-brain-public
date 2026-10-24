# exact target, quantifiers, hypotheses and units

Full FEI remains OPEN. Compress A047's existing canonical full-source rate-four failure to a parameter-free exact Boolean circuit, retaining the source and both physical terminal bills. For all positive integers r,m, let h be the product of m disjoint width-r point-defect signs and define F_h(x,a,b,z)=(-1)^a if x=0, h(z) if x=b=1, and +1 otherwise. The inputs are independent uniform bits. Entropy, cross-entropy and KL use base two; I is total uniform influence. The root reference is exactly the canonical empty-mass-and-coordinate-marginal reference defined below. Minimality is only within this homogeneous point-tensor selector family, over all positive r,m, not over all Boolean functions, references, circuits or restriction trees.

The minimum dimension for CE(P,Q)>4I(F_h) is 30, uniquely at (r,m)=(3,9) within the minimal dimension. Its exact margin is between 1/6 and 3/16 bit. Its actual Fourier entropy is below eight bits and below 4I. This is a falsifier of the specified full-reference payment, not a falsifier of FEI.

# sources actually read, revisions and theorem locators

Read the complete execution protocol revision2026-10-11-execution-v2; supervisor BOARD2026-10-22 22:38UTC, B10 lead notes v2 (2026-10-11), own STATUS/WORKLOG/LEARNED and previous source-complete run20261014T055836 REPORT. The lead's original finite bias-grid census was already completed; later empty marker directories do not establish new mathematics. Read current campaign README/status, claims/obstructions/packet/next-action registries, campaign plan, supplemental campaign/claims/counterexamples/seeds/mapping and source texts, and all four supplied paper text versions for relevant context. SOURCE_RECEIPTS records hashes, encodings and relevant locators. Text extraction includes explicit cp1252 fallback for the PDF text files; the initial strict UTF-8 reader stopped before creating receipts and was repaired, not mistaken for source corruption.

New primary inputs: A047 run20261021T221810 REPORT and code/certify.py, especially the complete source payment and canonical obstruction; A050 run20261021T171109 PROOF sections1-4 (fixed-reference owner, unique normalizer, hereditary terminal certificate); A048/A050 current STATUS; A092 LEARNED stage17 acceptance of A047's all-r obstruction. These are read-only inputs, not imported proof helpers. The current stage compresses an existing falsifier and repairs no accepted theorem. A read-only brain recall returned broad route-specific-obstruction cautions, with no theorem used. Wake flagged stale personal-context notes; the owner was informed. Current user campaign endpoint overrides the obsolete protocol endpoint.

# complete derivation or exact first unsupported line

Put delta=2^-r, mu=(1-2delta)^m, t=(1-mu)/2, p0=(1-t)^2/4, and v=1-p0. Direct Fourier expansion and physical edges give the root marginal vector

    (Inf_x,Inf_a,Inf_b,Inf_zj)=(1/2,1/2,t/2,delta/2),
    I0=1+t/2+rm*delta/2.

Every variable is essential for positive r,m. Every root source atom is dominated by the reference. Let r_i=Inf_i/v and let c in (0,1) solve

    product_i(1-c*r_i)=1-c.

All r_i are in (0,1), sum_i r_i>1 because the xa Fourier coefficient has mass1/4 at degree2, and at least two r_i are positive. The function [1-product_i(1-c*r_i)]/c equals sum_i r_i product_{j<i}(1-c*r_j). It is strictly decreasing, starts above1 and ends below1; hence the positive root exists uniquely. This uses positive denominators and factors only. The zero solution of the undivided polynomial is excluded by the strictly positive rational lower bracket. Define

    Q(empty)=p0,
    Q(S)=(v/c) product_i (c*r_i)^1_{i in S}(1-c*r_i)^1_{i not in S}, S nonempty.

The root equation normalizes Q. Its nonempty coordinate marginals are exactly Inf_i, so log Q is affine in membership on the nonempty sector and CE(P,Q)=H(Q). Two equivalent complete formulas, checked by different implementations, are

    CE=phi(p0)+v log2(c/v)-v log2(1-c)
         +sum_i Inf_i log2((1-c*r_i)/(c*r_i)),
    CE=h2(v)+(v/c)[sum_i h2(c*r_i)-h2(c)],

where phi(q)=-q log2(q), phi(0)=0. No normalizer or empty sector is dropped. No reference-only row is erased by this calculation: CE includes the complete normalized Q and A=CE-H0 is the entire source liability.

For the fixed minimizer r=3,m=9 the data circuit has nine AND3 gates, XORs their outputs to hbit, takes selected=b AND hbit, and outputs sign1-2*MUX(x,a,selected). CIRCUIT.json specifies every input and gate, including bit and sign conventions; it is a complete exact circuit certificate without constructing a 2^30-entry table. In LSB order x,a,b,z0,...,z26 the uniform Boolean spectrum is unambiguous. The exact root values are

    mu=(3/4)^9, t=242461/524288,
    p0=79426457929/1099511627776,
    I0=3060509/1048576.

The unique canonical c lies in the exact rational bracket saved in WITNESS.json (decimal display0.9724566279444984 to0.9724566279444993). The two exact entropy calculations certify

    1/6 < CE-4I0 < 3/16,
    11.856238956345 < CE < 11.856238956346,
    H0 < 8 < 4I0.

For the physical tree query b, retain b=0, and query one data bit in b=1. Both active data children have nonconstant cores because m,r>=2. Every leaf retains the independent a-character selector. If p_r is the Fourier entropy of a width-r point defect, its exact formula is

    p_r=phi((1-2delta)^2)+(2^r-1)phi(4delta^2).

Tensor additivity and the separated a-character support give

    Hf=2+((m-1)/4)*p_r+p_(r-1)/8,
    If=1+(rm-1)*delta/2,
    R=I0-If=t/2+delta/2.

For r=3,m=9, If=21/8, R=307997/1048576, p_2=2 and Hf=9/4+2p_3. Define the unused final budget S=4If-Hf, full source A=CE-H0, signed query deficit e=H0-Hf-4R and complete conservative liability L=A+max(e,0). The replay certifies e>0, so the EXACT algebra gives

    L-S=CE-4I0>1/6.

Numerically for orientation only: S is3.81616562662, A is3.88480287084, e is0.112686398406, and the shortfall is0.181323642625. All final terminals and the original source remain in this comparison. No new reference at a descendant is assumed. With SAME-channel inherited Bayes transport, the KL chain partitions A into nonnegative erasure, outcome and terminal debts; it does not manufacture another A-sized budget. Thus even the complete source plus signed-query transaction exceeds the original certified terminal budget. The sharper liability max(A+e,0) also fails because A+e>0 and e>0.

Each leaf core is a product of point defects, whose entropy is at most four times its influence. For r>=2 the nonempty entropy is8(r-1)delta(1-delta) and the empty contribution is at most4delta(1-delta)/ln2; ln2>1/2 implies H<=8r delta=4I. Width0 or1 has entropy zero. This supplies a certificate for each actual leaf without assuming FEI for arbitrary cores. The root itself is checked directly by its exact entropy formula, so the failure is purely a cost of the prescribed reference.

Minimality: the frozen discovery domain contains645 positive pairs rm<=128. Binary64 merely locates a candidate of data dimension27. The proof then independently certifies ALL95 positive pairs rm<=27 by rational intervals, including r=1 and m=1 boundary cases; only (3,9) is positive. Each of the other94 upper endpoints is strictly less than-1/20. All rm>=28 have at least31 physical variables automatically. This proves the global minimum30 for the declared homogeneous family, not just a capped-family minimum. It does not claim the minimum among heterogeneous block widths or arbitrary cores.

FIRST UNSUPPORTED UNIVERSAL LINE: a correlation-preserving prescribed reference, or an actual selected signed inherited transaction, is payable from a genuinely unused dimension-independent owner for every Boolean core and mixed query history, retaining old bookings and both terminals. The unchanged full coordinate-product source cannot satisfy that line, as A047 already proves in unbounded dimensions. This stage supplies a smaller finite exact witness; no universal FEI constant improves.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC was written before computation by python -X utf8 code/minimize.py --freeze. Domain645 pairs, memory estimate70MB, maximum runtime55seconds, no dimension escalation or symmetry quotient beyond homogeneous block relabeling. Pilot six predetermined pairs: PASS174 assertions,0.6684seconds. Main command python -X utf8 code/minimize.py: discovery645 pairs, exact certification95 pairs, PASS2516 assertions,11.0993seconds. A stopped or failed search would leave the target open; no mathematical checker failed. Discovery is explicitly noncertifying. There are no sampled or binary64 sign conclusions in the proof.

For logs, range-reduce a positive rational x=2^k y with1<=y<=2. With z=(y-1)/(y+1), the28-term atanh sum is a lower bound on ln y, and its omitted tail is at most2*z^57/[57*(1-z^2)]. The positive ln2 interval is divided with the proper endpoint directions. Every resulting log endpoint rounds outward to a72-bit dyadic lattice. Root signs and50 bisections use exact Fraction arithmetic. All entropy intervals propagate coefficient signs explicitly, including the negative normalizer coefficient. WITNESS and CERTIFICATE contain exact rational root brackets, margins and every pair's conclusion. Stop precision is the proved1/6 margin, not further digits.

Different-representation replay command python -X utf8 code/replay.py: PASS99 assertions,0.8089seconds. It uses the conditional-product entropy formula instead of the occupied-log formula and separately coded40-term rational logarithms, rechecks both root-polynomial signs, all complete-terminal identities and the1/6 margin. Direct signed-character sums and independent physical edge counts on five full truth tables (dimensions4,5,6,7,9) check normalization, empty mass, every influence and the root entropy formula; small-table SHA256 values are saved. This is internal reproduction, not an independent agent acceptance. Main plus replay:2615 exact assertions. Both small/boundary cases and the source/terminal hypotheses are exercised.

Lean: a core Nat endpoint comparison is prepared as code/Margin.lean with its source hash, but NOT compiled. Fresh memok exited1 at physical free2.0GB versus4.0GB floor (commit free26.4GB); no compiler was started. Rung is exact rational certificate plus analytic derivation, NOT Lean-checked. The prepared theorem would certify only its integer endpoint inequality, not the Fourier translation or interval construction. All jobs actually executed are below70MB, under60seconds, without GPU, detached work or automatic n increases. No running work was stopped. Current compute snapshot showed high CPU with a BelowNormal ffmpeg holder; no resource intervention was attempted. Historical intervention entries are read-only context.

# proof dependencies and changed downstream conclusions

The derivation is self-contained, so proof_dependencies is empty. A047's existing canonical-reference obstruction and A050's scoped low-gap theorem are source leads, not assumptions required by these exact formulas. A050 remains valid at its stated hypothesis; the new minimizer fails its source-payment conclusion and therefore lies outside that sufficient domain. The source-complete payment cannot be repaired by replacing a marginal upper estimate with exact CE at this witness. A092's accepted all-r obstruction remains unchanged. Earlier A049 six-bit contracted-label and four-bit conditional-reset targets are different statements and are not re-labelled as this minimum.

No claim against all references, all selected resets, correlation-preserving references, arbitrary FEI constants or FEI itself follows. The narrow finite extraction avoids opening another broad unreviewed candidate. Independent review, canonical adoption, mirrors and downstream use remain pending.

# one next mathematical action and independent reviewer

NEXT: A047/A050/A092 independently reconstruct this30-bit source-complete certificate; then test one correlation-preserving normalized core reference through the same b/data query, pricing its actual selected signed reset from the SAME original unused owner with old bookings and both full terminals. Another larger canonical-product census cannot close the universal gap. The smaller exact circuit makes alternative references directly comparable on the existing failing transaction. Handoffs are the local source-bound files only; no messages are sent.

# actual persistence receipts or precise save blocker

REPORT, CLAIMS, PROGRESS and identical PACKET_DELTA, code, frozen spec, exact circuit, all95 exact-case records, replay and source receipts are saved under this assigned A049 run. PERSISTENCE checks the exact protocol fields, statement hashes, matching progress copies, current two-line STATUS and file-size limit. WORKLOG and LEARNED append the result. No local save blocker. No git, mail, other-agent edits, protected-tree edits, research-brain writes, deletion or external upload. The required wake is infrastructure; no research result is written outside A049. Supervisor copying and independent acceptance are not claimed.

Universal bridge: This stage moves C024 history transfer and C019 stopping-tree payment by compressing the already established canonical full-source obstruction to a parameter-free30-bit circuit, proving dimension30 minimal over the entire homogeneous point-tensor selector family, and retaining the full original source, signed query deficit and both final terminal bills in an exact shortfall>1/6. The universal FEI constant improves by zero. What remains is a correlation-preserving reference or selected inherited transaction funded from one unused owner through mixed history. NEXT changes the demonstrably failing reference mechanism on the same compact certificate, rather than treating another class bound or a more expensive reference census as a full-FEI bridge.
