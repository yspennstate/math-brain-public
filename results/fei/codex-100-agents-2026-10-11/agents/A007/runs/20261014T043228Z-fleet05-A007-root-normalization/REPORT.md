# A007 stage 5: the retained ownership-entropy tail is closed

## exact target, quantifiers, hypotheses and units

C020 whole-set witness cost / B02 PI-J. For all integers s,N>=1, use the EXACT old full-cell surrogate posterior W from A015's OCCUPATION_ENVELOPE.md, including labels, actual forest factorial moments and old congestion. Sizes are ordered by increasing used gate ID; no extra k! is inserted. Gamma=6/5; entropy and costs are bits. The theorem is

    Pr_W(H(owned sizes/s)>=h)<=min(1,C_s*2^(-sh/5))
                           <=min(1,6^(s-1)*2^(-sh/5)), h>=0,
    E_W H<=5log2(6)<13,
    C_s=sum_k binom(s-1,k-1)(s)_(k-1)/k!.

For every nonconstant B using its fixed full-cell AND cover, lambda=1/N and common physical orders, fresh common-core activation has controller correction Psi_dist<=(1-b)log2(6)I_core(F), b=E B. Inherited complete cost pR_g remains. General full-cell covers need not be prime; parity's positive cells are its exact prime table. A separate all-support variational budget retains selected-intersection cost K_tau, globally scaled labels, root-rarity credit and actual-event factorial credit. No universal FEI or general PI-J constant is claimed.

## sources actually read, revisions and theorem locators

Read BOARD.md (2026-10-14 04:29 UTC), B02 STREAM_NOTES.md v2 (2026-10-11 23:35 UTC), own STATUS/LEARNED, and full protocol revision 2026-10-11-execution-v2. Long board output was followed by middle/end chunks. Read A015 stage-4 OCCUPATION_ENVELOPE.md, CLAIMS.json and REVIEW_A007.md in runs/20261014T031846Z-fleet05-A015-minterm-barrier-analysis. Read A008 stage-4 OCCUPATION_MASS.md as current complete-probability context; its graph theorem is not a premise. Reread forests.tex original queue, source-SCC partition interface, eq:forestcost, eq:forestconditioning and thm:posteriorforest. Prior stage's distributed proof and independently implemented helper are retained/pinned, not claimed newly reread in full. out/SOURCES.json pins source bytes; board hashes describe final saved bytes. Earlier campaign/paper baseline reads remain inherited.

The lead's original review-A009/tribes task is completed. A015 independently accepted the entire distributed lift v1 without repair and isolated a new exact posterior-size law and tail question. This stage consumes that acceptance, reconstructs the whole new diagnostic, and closes the tail question rather than opening another broad candidate or repeating a variational identity/read-once calibration. It does not claim all B02 review-cap obligations have disappeared.

## complete derivation or exact first unsupported line

POSTERIOR_TAIL.md proves the all-s,N tail. Write A(v)=prod(v_i/s)^v_i=2^(-sH). A multinomial probability implies [s!/prod v_i!]A(v)<=1. The original finite-N labels satisfy binom(N,k)N^-k<=1/k!, while the k=1 weight is exactly one, giving posterior normalizer >=1. Each record is therefore bounded by (s)_(k-1)/k!*2^(-sH/5). Sum positive ordered compositions BEFORE paying the entropy loss to get C_s.

With n=s-1, C_s<=sum_j binom(n,j)binom(n+j,j)=sum_j binom(n,j)^2 2^j. Vandermonde proves the identity directly. Nonnegative cross terms bound it by (1+sqrt(2))^(2n)<6^n for n>0. Integrating the resulting exponential tail proves E H<=5log2(6). The strict rational constant sign is 6^5=7776<8192=2^13. Neither an asymptotic estimate nor floating-point entropy is needed.

REVIEW_A015.md independently reconstructs its entire fixed-assignment envelope, sharp coefficient 1/5 and explicit error, actual parity prime realization, same-posterior Jensen step, signed controller ledger and exact owned-size law. No repair is supplied. Its proposed tail was explicitly unsupported in the source; our proof closes it downstream. The source diagnostic is Markdown, not a fabricated registered upstream claim. Separately, A015's independent acceptance record of A007-DISTRIBUTED-CORE-COMPONENT-LIFT v1 is copied at unchanged statement/hash.

In the full-support regime beta=1,c=1,L_0=1. Retain the exact signed identity

    Psi_dist=p Var(g)log[D'/(pD)]-p sum_T P_g(T)E_U log J_dist,U(T).

The reviewed envelope and tail give an upper bound p Var(g)log[D'/(pD)]+(pr/2)Var(g)log2(6). Only after writing this is D'<=pD used. Thus Psi_dist<=(1-b)log2(6)I_core(F), and

    R_F<=pR_g+(7/2)pI(g)
             +[6/5+log2(e)/4+(1-b)log2(6)]I_core(F).

The complete inherited reference cost pR_g, its physical rank/location information, h2(Var F) and K_ref I(F) are retained. They are not replaced by H(g), assumed zero, or charged twice. Surrogate posterior mass is not actual queue probability.

GENERAL_BUDGET.md advances the arbitrary-support continuation. With a_l=s_l/s and s_l<=kappa_l<=s, define K_tau(u)=sum_l a_l[s log(s/kappa_l)-(s+u)log((s+u)/(kappa_l+u))]>=0. A variational law on actual core maps and Jensen give log Z_tau(u)>=-uH(a)/5-(6/5)K_tau(u), with a proved tangent upper bound on K_tau. Unequal root rarities give the valid retained credit sum_root log(1/pi)-max_root log(1/pi), because the exact rooted component counts sum to (u)_(c-1). Jensen on the SAME old posterior gives one signed expected budget containing beta labels, K_tau, ownership entropy, rare-root credit, factorial event credit and log[D'/(pD)]. No term is silently dropped.

The first unsupported general PI-J line is a dimension-independent influence payment of this complete signed budget under one globally fixed feasible reference. The full-support tail is settled, but its inherited R_g and the arbitrary-support K_tau/label/ownership expectation are not. Uniform ownership-entropy tails on arbitrary supports are not inferred from the full-cell law.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json and GENERAL_SPEC.json were saved before their respective jobs. Main pilot s<=5, selected N values, s,N<=2 trace law and parity m<=3: 307 direct plus 20 helper assertions PASS in 0.074552 helper seconds. Full: s=1,...,12, unique N in {1,2,4,16,2^(s-1)}, all positive ordered compositions; 9,050 records and 56 s,N cases. Exactly 41 coefficient identities n=0,...,40 and 494 labelled assignments at s,N=1,...,4 reconstruct 1,206 root minors and 7,660 actual chronological events. Five actual parity truth tables validate their full spectral sets, prime-cell counts and influences. The final main check passed 20,214 direct plus 8,866 helper assertions in 0.833238 helper seconds.

Arithmetic is integers/Fraction, exact fifth-power comparisons for gamma=6/5, sparse determinant polynomials and direct chronological events. The posterior law is checked by equality of rational coefficients per ordered size vector with congestion powers kept formal. For N>2^s, the selected-coordinate incidence graph is realized by full cells on a sufficiently large m-coordinate cube with N<2^m; no claim that N distinct cells exist on only s coordinates is made. Original irrational subset/size choices are not replaced by rational surrogate factors. No floating entropy, arbitrary precision guess, or sampled posterior is used.

The general sign/root-credit job ran its fixed bounded domain once as feasibility plus complete exact certificate: s=1,...,5, u=1,2,3, all positive size compositions and every kappa_l from s_l through s; root counts 1,...,4, widths 1,...,6 and every weak core-component size vector. It checked 18,321 rational intersection products and 48,510 unequal-root records, passing 163,944 assertions in 6.953341 seconds. These intersection configurations can be realized with distinct private unselected literals preventing clause containment; the numerical sign proof also holds without a realization assumption. The variational/tangent bounds remain analytic, not extrapolated from these sign checks.

Successful FULL-stage assertions total 193,024; pilot assertions are separate. Commands from this run directory:

    python -X utf8 code/check.py --pilot
    python -X utf8 code/check.py
    python -X utf8 code/general.py
    python -X utf8 code/finalize.py

Own previous independent checker helper is read/compiled with no author code import or prior artifact write. Frozen RAM estimates are 120 MB and 80 MB; no job expected above 300 MB, so memok was not triggered. Jobs ran one at a time below their frozen 60-second limits; no automatic dimension escalation, GPU, window, background process, git, messaging or brain mutation. Memory estimates are not measured peaks. No mathematical check failed; a narrow prose edit initially missed its exact line and was reapplied before finalization.

## proof dependencies and changed downstream conclusions

A015's no-repair independent acceptance of distributed lift v1 is consumed at its original exact statement/hash. A007 is not its independent reviewer; the review record is A015's. A015's separate complete envelope/size-law artifact receives an independent reconstruction by A007, with no source repair; the new tail closure is an additional theorem rather than a change to that diagnostic. The original forests.tex source is hash-pinned. No graph occupation theorem, arbitrary-support concentration assertion, external theorem or unreviewed universal cost-payment result is a premise.

New A007-RETAINED-OWNERSHIP-TAIL-AND-ROOT-BUDGET v1 is author-proved/exactly-checked and pending review. The proposed full-support posterior tail is closed with a dimension-independent constant and pays its controller correction. The general budget explicitly shows why this does not extend for free to different selected intersections. Consumers should replace the former Var(g)log n ownership bill in that scoped activation correction with the proved bound, while retaining pR_g. They must not continue full-support tail searches or claim a universal base reference from the result.

## one next mathematical action and independent reviewer

Pay the arbitrary-support signed budget jointly under eta_T: control K_tau and ownership entropy together with beta labels minus root-rarity and factorial-event credits. Retain the same reference and base posterior, especially on the connected overlapping degree-scale cases now being investigated by A010/A009. A015/A008/A086 should first reconstruct the exact factorial/label coefficient C_s, its dimension-independent growth bound, same-posterior tail integration and full inherited-cost ledger. A094 should challenge the all-support Jensen/root-credit reduction and whether any next payment spends the same influence twice. No external message was sent.

## actual persistence receipts or precise save blocker

The four protocol files, tail proof, general signed budget, independent review note, two frozen specs, scripts and exact outputs are saved only under this A007 stage directory. STATUS has exactly STATE/NEXT lines; WORKLOG and LEARNED are appended. out/RECEIPTS.json records on-disk hashes/sizes and exact protocol schema checks, matching PROGRESS/PACKET_DELTA, unchanged accepted statement/hash and the 20 MB cap. Local persistence is complete. Supervisor registry adoption and GitHub/brain mirroring are unverified; no local save blocker exists.

## Universal bridge

C020 whole-set witness cost / PI-J advances by closing the exact retained full-support ownership-entropy tail with E H<=5log2(6)<13 and paying its entire controller correction by (1-b)log2(6)I_core(F), with the negative normalizer and inherited pR_g kept. The distributed lift's independent A015 acceptance is consumed, and the arbitrary-support continuation now has an explicit K_tau budget retaining unequal-root and actual-event credits; 193,024 full exact assertions support the proofs. The universal bridge still lacks influence payment of inherited base cost and the general K_tau/label/ownership expectation. NEXT pays that same signed arbitrary-support budget under the actual posterior, rather than proving another isolated class or repeating the now-closed full-support concentration question, because those are precisely the remaining terms needed for a universal prime-table reference.
