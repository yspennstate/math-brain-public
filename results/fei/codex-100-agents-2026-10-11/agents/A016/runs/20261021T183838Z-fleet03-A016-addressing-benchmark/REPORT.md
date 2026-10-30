# A016 stage 7: one original bank pays nonflat activation histories

Full FEI remains OPEN. The inherited-reference calculation extends from a point event to every activation A=1_{v=0}B(z), where v has k>=5 bits and B is ANY three-bit indicator. This includes unequal Fourier masses and unequal actual child spectra. After q, every adaptive order exposing the activation bits has expected signed rate-4 reserve >121/64. The SAME original half-core bank pays the booked insertion, conversion, all remaining query charges and final positive terminal deficits, leaving >5/128. This is a supplied-reference continuation, not a universal construction.

## exact target, quantifiers, hypotheses and units

All physical bits are independent uniform 0/1 bits, chi_b=(-1)^b, all logarithms are base two. For an arbitrary finite-bit indicator A of probability p<=1/8 put h=chi_u(1-A)+chi_q A and F=1 at gate x=0, hs at x=1. Here s is the two-bit sign point defect [-1,1,1,1]. Write J_A=4 sum_T |T| Ahat(T)^2, the physical total influence of the 0/1 indicator (flip-probability convention). The supplied root reference is Q_h=(P_h+point_q)/2 and Q_F(e,T)=[Q_h(T_core)P_s(T_mask)+point_empty(T)]/4 at BOTH gate frequencies. Every descendant inherits its frequency marginal. Expose q first, then every activation bit in any adaptive order, retaining u, x and the two mask bits. No reset or renewed bank is allowed.

Let P be the common squared spectrum of either h|q child and c=CE(P,(P+point_empty)/2). The general sufficient admission is c<=J_A+2. Under this admission the original bank S=2(1-p+J_A/2)-c/2 pays the complete ledger below and leaves >5/128. An unconditional instance of the admission is A=point_k B for every k>=5 and every three-bit B (including constants). The stage advances the saved signed-bank NEXT; the original addressing baseline is retired.

## sources actually read, revisions and theorem locators

Read the full execution protocol, revision 2026-10-11-execution-v2, machine rules, current BOARD snapshot 2026-10-21 18:37 UTC, B04 STREAM_NOTES v2, own rolling files and archived stage6 report/helper. Read current campaign README/status and relevant entries in CLAIM_REGISTRY, OBSTRUCTION_REGISTRY, PACKET_STATUS, STREAM_NEXT_ACTIONS; inspected the campaign-plan and supplemental CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS, NATIVE_MAPPING and source inventory. Inspected all four context text versions and the current threshold paper Proposition 8.6, equation (75). These source files remain untouched. Existing complete baseline literature reading is carried forward; no fresh external literature claim is made.

New dependency read in full: A020 run 20261021T162111Z-fleet03-A020-selector-boundary-tests REPORT.md, especially sections 1--4 and the signed terminal objection. Its checker was inspected, but the new implementation uses neither that checker nor its imported helpers. A016 stage6 run 20261014T075009Z REPORT sections 1--5 supplies the old exact reference and bank. Later A016 directories contain marker-only artifacts, so they supply no new mathematics. The newer user deadline 23 October 14:49 UTC governs over the older protocol date. Brain wake reported stale owner-model/state notes; they are not mathematical dependencies. Recall supplied no usable new proof, and no recalled claim is accepted on authority.

## complete derivation or exact first unsupported line

1. General activation identity. At q fixed, h_q=chi_u off A and +/-1 on A. Its Fourier coefficients are (1-p) at {u}, +/-p at empty, and two copies of +/-Ahat(T) for each nonempty activation T. Thus the two children have the same squared law P. Their influence is 1-p+J_A/2. At the parent, q moves the u-absent coefficients onto q-present labels; no coefficient interferes. Hence CE(P_h,Q_h)=c, the root is balanced, and

C_root=c/2+3,   I_root=3/2+J_A/4.

The extra ghost point at q is retained. After q it is exactly point_empty. Fresh child activation references differ only on the empty-data gate conditional; the inherited conditional remains uniform. Their conversion E satisfies 0<=E<p^2 for p>0, and E=0 for p=0. Indeed with mu=p/2 its exact value is (1+mu^2)/2 times KL(Ber((1+mu)^2/[2(1+mu^2)]) || Ber(1/2)); chi-square/ln2 and ln2>1/2 give the bound. The denominator is strictly positive. Let J_first be the actual root-to-fresh-child debit. It is L_q+E, not a renewed reserve.

2. Any supplied finite-cost Q transports by Q'=sum_e Q(e,T). The actual Walsh restriction identity gives avg_b P_child(T)=sum_e P_parent(e,T), so

CE_parent=avg CE_child+sum_(e,T) P_parent(e,T) log(Q'(T)/Q(e,T)).

Every summand is nonnegative and support is preserved: a positive child mass has positive erased parent mass. On any finite adaptive tree these full charges telescope with the actual physical reaches. No arbitrary-probability surrogate or free terminal is substituted.

3. Complete endpoint depends only on p. Parseval gives sum Ahat^2=p. After q and all activation frequencies are erased, Q_core(empty)=(1+p)/2 and Q_core({u})=(1-p)/2. Every actual inactive history has core chi_u; the active histories have constants +1 and -1 with equal total weights p/2. Their complete inherited costs are

C_par=5-(1/2)log((9+p)(1-p)),
C_con=5-[5log(9+p)+3log(1+p)]/8,
C_end=(1-p)C_par+p C_con.

The corresponding influences are 3/2, 3/4 and 5/4. For 0<=p<=1/8, C_par>27/8, C_con>23/8, C_con<25/8, and therefore C_end>53/16=424/128. Exact endpoint checks suffice: 9^4<2^13, (73/8)^4<2^13, (9/8)^4<2; monotonicity covers the interval. C_par<5<6 and C_con<25/8<5 show that ONLY the positive constant history may have a deficit. Its full weighted positive deficit D=(p/2)(C_con-3)_+ obeys D<p/16<=1/128. This deficit is explicitly booked, even though the aggregate signed code budget already retains it.

4. One original bank. The fresh q-child activation has cost c/2+3-L_q-E, at most c/2+3-E, and influence 1+(1-p+J_A/2)/2 minus/plus p/4. Its complete rate-4 surplus is therefore 1+S minus/plus p+E+L_q, at least S+1-p. Thus S is an actual unused part of the supplied fresh-child budget; the mask/gate remainder pays the remaining profile and is not borrowed again. Let C_0 be the mean inherited cost after q. All later charges total C_0-C_end, irrespective of the adaptive exposure order. The total debit including the already-booked insertion is

J_first+(C_0-C_end)=C_root-C_end+E.

The exact remaining bank after paying the final positive deficit separately is consequently

S-[J_first+C_0-C_end]-D
 = C_end-c-1-2p+J_A-E-D.

Under c<=J_A+2, use C_end>424/128, 2p<=32/128, E<2/128 and D<1/128 to obtain a strict lower bound 5/128. The p=0 endpoint has E=D=0 and the same strict conclusion. This is an explicit single-owner allocation. It does not say each rare history is separately rate-4 eligible. The admission is a supplied-core code condition, not asserted for arbitrary cores.

5. Unconditional nonflat family. Take A(v,z)=1_{v=0}B(z), k bits v, r bits z, beta=E B, delta=2^-k, p=delta beta. Define L_B=sum_U Bhat(U)^2 log(1/Bhat(U)^2), omitting zeros. Exact tensor coefficients give

H(P)=eta((1-p)^2)-eta(p^2)+4kp+2delta L_B,
J_A=2kp+delta J_B,

where eta(t)=t log(1/t), with eta(0)=0. Every nonzero Bhat is an integer multiple of 2^-r; thus L_B<=2r beta. Also eta((1-p)^2)<3p for p>0 (ln2>2/3), while eta(p^2)>=0. It follows that H(P)-J_A<(2k+4r+3)p. Since c<=H(P)+1, a sufficient condition is (2k+4r+3)2^-k<=1. For r=3,k>=5 the left side decreases and is at most25/32. The p=0 case has H=J_A=0,c=1 and is admitted directly. This proves c<J_A+2 for EVERY three-bit B and all k>=5. The proof uses actual Boolean lattice coefficients, not an arbitrary spectral-law relaxation.

There is also a uniform intermediate signed reserve. H(P)<(4k+4r+3)p, so for r=3,k>=5, c<1+35/32=67/32 and C_root<259/64. Any partial adaptive exposure can be completed to the endpoint, giving expected remaining influence >=I_end=3/2-p/2 and expected CE<=C_root. Since p<=1/32,

E(4I_leaf-CE_leaf)>6-2p-259/64>=121/64.

Both signed terms E(4I-CE)_+ and E(CE-4I)_+ remain present; their difference is this reserve. Local nonconstant or constant eligibility is not required. This estimate applies to partial stopping partitions as well as fixed-depth prefixes, provided only activation coordinates are exposed after q.

6. Independent review consumed. A020's point-event all-prefix formulas Q_t, I_t and R_t are reconstructed from an independently written integer Walsh implementation at k=3,6,8, all t=0,...,k and both q signs, retaining active/inactive physical probabilities and both signed terminal terms. The all-k proof in its sections 1--4 is checked algebraically: the decreasing bound (2k+4)2^-k, the entropy upper bound using ln2>2/3, the k=3 rational417/128 endpoint and the stated terminal estimates all hold. The original bank margin >1/32 is accepted at its exact point-event scope. This review does not accept every statement of its broader source history or silently promote its Lean timeout. Its separate nonconstant penultimate claim is not needed for the extension here; no whole-report acceptance is inferred from the finite checks.

First unsupported universal line: an arbitrary Boolean activation/core must have a constructible supplied reference with c<=J_A+2, or an alternative paid source bank replacing that condition. For arbitrary A the entropy-minus-influence admission may fail; this stage neither assumes it universally nor proves full FEI. The new all-dimensional theorem is confined to padded fixed-width activations and the stated complete supplied reference.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json precedes the pilot/search. Independent helper v1; all256 three-bit B truth tables at k=5, including both constants; no symmetry reduction. Eight designated tables receive complete full-F Walsh/reference and a proper activation-bit query with both actual children. Three point-event families k=3,6,8 receive independent all-prefix reconstruction. Integer Walsh, Fraction masses, direct physical-edge influence, exact normalization/support, and outward rational logarithm intervals are used. Logs use32-term range-reduced atanh with explicit tail2*z^65/[65(1-z^2)] and outward72-bit dyadic rounding. Zero spectral atoms are omitted only from entropy sums, and ghost reference atoms are retained.

Commands: python -X utf8 code/check.py --pilot; python -X utf8 code/check.py. Pilot: one family,19,987 assertions,0.2628694 seconds, PASS. Full:256 activation families plus3 review families,456,239 assertions,27.7509214 seconds, PASS. Exact checkpoint output is out/CHECK.json. The separately frozen ALGEBRA_SPEC.json certifies11 load-bearing rational endpoints, ln2>2/3, the bank/partial-reserve fractions and the polynomial remainders proving both all-k monotonicities; out/ALGEBRA_CERTIFICATE.json records PASS. No failed numerical sign, tolerance or automated dimension increase is accepted. The finite tests check the endpoint and admission; the derivation above supplies the all-k and all-adaptive-order bridge. Memory estimate110MB, no job expected above300MB, no GPU or background process; peak memory is not measured. Compute snapshot was ok with15,918MB available RAM, no hung windows and45.4GB free disk. No running work was stopped.

A Lean check of rational bank algebra returned RUNTIME_UNVERIFIED after35.286 seconds, compiler exit unknown, with no verified target or axiom closure. Its source hash is212adc37a769a657841e45418c57cfa8c76dd3c62ecf8447a92d0c59570689e9; the local receipt directory is recorded in out/LEAN_ATTEMPT.json. No claim follows from this timeout. Until an exact target and acceptable axiom audit are available, the mathematics is analytic proof with exact finite validation, pending independent review, NOT advertised as Lean-checked. The entire Fourier and entropy argument is not formalized by that small algebra check.

## proof dependencies and changed downstream conclusions

The supplied root reference and one-owner half-bank are A016 stage6/A020's explicit interface. The full transport and final reference are reconstructed here. A020 all-prefix/original-bank sections1--4 independently HOLD at their stated point-event scope; the new sufficient admission and padded nonflat extension await review. No universal FEI claim is used as a premise. All prior local-eligibility counterexamples remain valid. B04's initial addressing target is completed and is not rerun. This continuation follows the lead's paid-tree direction; it changes the flat event hypothesis rather than renaming an existing gap.

Downstream consumers A018/A019/A020/A090/A091/A094/B20 may use the exact original-bank identity, with c<=J_A+2 explicitly retained. Complete ghost cost, conversion, both constant signs and weighted positive deficits cannot be removed. Local persistence and review do not imply shared-registry adoption, mirror verification or public release.

## one next mathematical action and independent reviewer

Replace the finite-width padding admission by a complete supplied activation reference on one unbounded-width nonflat core, and bound c-J_A using an already unused signed child surplus rather than an ambient Fourier coefficient lattice. Keep the same Q, J_first and both terminal accounts. A020/A019 should independently reconstruct the generalized endpoint and source-bank inequality; A018/A090/A091/A094 should challenge arbitrary partial-history scope and the admission's FEI hardness.

## actual persistence receipts or precise save blocker

The four protocol files, frozen spec, independent checker, pilot/full output and final local hashes are saved inside this A016 run. STATUS has exactly two lines; WORKLOG is appended; LEARNED records the sufficient condition and its scope. out/PERSISTENCE.json checks protocol fields, JSON parsing, statement hashes, file sizes and identical progress/delta. No git, network publication, messages, other-agent write or research write to the brain occurs. The required wake/checklist helpers are session bookkeeping. Independent review of the extension, supervisor adoption and mirror persistence remain pending.

## Universal bridge

This stage moves C024 history transfer and B04's C019 stopping-tree payment from a flat point event to an arbitrary three-bit activation with unequal spectra under all k>=5 paddings and every adaptive activation-bit history: the SAME root Q and original half-core bank retain >5/128 after all query charges, conversion and the positive terminal deficit, and every partial partition has expected signed reserve>121/64. It independently accepts A020's all-prefix original-bank theorem at its exact scope. The arbitrary-core admission c<=J_A+2 remains unpaid and must not be mistaken for universal FEI. NEXT replaces that admission using actual unused signed child surplus on an unbounded-width core; it targets the precise reference/ownership step needed for full FEI rather than enlarging another finite census.
