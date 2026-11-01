# A041 stage 4: physical signed profiles and an exponential reference obstruction

## exact target, quantifiers, hypotheses and units

Target remains B09's corrected all-product-bias, arity-independent FEI+ for every two-weight threshold F=2*1{w N_A+N_B>=t}-1, arbitrary finite groups, real w>0,t and independent interior biases. Natural corrected entropy is E=sum_nonempty P(S)ln(v_S/P(S)), v_i=4p_i(1-p_i); Hplus=E/ln2; Delta=I-Var. All actual Fourier transforms retain signs before squaring. Deterministic inputs contract before normalization.

New scoped result: every normalized physical B-coefficient profile, as a function of the A-count, has total variation at most two and a signed physical symmetric-tail representation with total absolute weight at most one. The natural absolute-cofactor deficit budget nevertheless has unbounded ratio to the root Delta, exponentially along a specified actual two-weight family with exactly two heavy inputs. This excludes a new reference mechanism, not corrected FEI+. Mixed entropy and full FEI remain OPEN.

## sources actually read, revisions and theorem locators

Read own STATUS.md, updated BOARD.md (local snapshot including all stage-3 stream reports), B09 STREAM_NOTES.md v2 still dated 2026-10-11 23:33 UTC, and execution-v2 protocol in full. Lead's two-weight assignment and review/repair cap remain in force. Read own stage-3 pure-sector proof and current claim hashes. Read A045 run 20261014T004049Z-fleet05-A045-biased-realizability-referee REPORT.md, CLAIMS.json and CHECK_OUTPUT.json: it independently accepts A041-COHERENT-PURE-SECTOR-PAYMENT@1 and gives the mixed degree-reference/admission audit. That acceptance is now consumed at original hash 8f36fbc86ed36574351e69b9dcb2a18eadad8a8b3b74b5936236a033643eab8b, not inferred merely from a board line.

Also read A045's older 20261013T212421Z report, which remains its scalar-payment obstruction rather than its newest result; that obsolete search is not repeated. Read A042 stage-3 REPORT.md: its sharp majority-three bound and common-triple identity are context for why degree credit alone does not extend automatically. Re-read baseline current-threshold-paper.tex at bias:weak (reference weights and coefficient-one credits) and bias:strong (c=460+80ln2 all-bias symmetric baseline). No conjectural weighted extension is used. Source hashes/locators are in out/SOURCE_RECEIPTS.json.

## complete derivation or exact first unsupported line

Complete proof: COFACTOR_REFERENCE.md, equations (1)-(10). For nonempty T subset B, its normalized physical Fourier coefficient profile is

    h_T(z)=E_B[(2*1{wz+N_B>=t}-1)phi_T]/sqrt(v_T).

At a score level its jump is twice that level's signed character moment. Since E|phi_T|=sqrt(v_T), total variation is at most two, independent of both arities, all biases and w. Restricting to attained A-counts gives h_T(N_A)=constant+sum_j alpha_Tj g_j(A), g_j symmetric threshold signs, sum_j|alpha_Tj|<=1. Its nonempty A coefficients give the exact coherent mixed amplitudes. Every g_j is a genuine physical Boolean cofactor, so this route avoids the non-Boolean spectral-marginal error identified by A045.

However B_abs=sum_{T nonempty}v_T sum_j|alpha_Tj|Delta(g_j), the symmetric-tail deficit cost of the absolute-weight mixture, cannot satisfy B_abs<=KDelta(F) with one absolute K. For r>=1 put n=4r+1 light inputs, two heavy inputs of weight n+1, threshold n+1+(n+1)/2, all fair. The branches at heavy counts 0,1,2 are -1, balanced odd-majority g, +1. Each coefficient profile is (0,ghat(T),0), so its two signed tails are OR2 and AND2 with coefficients +/-ghat(T)/2. Their deficits are each1/4, yielding B_abs=||ghat||_1/4.

The exact signed gate formula is F=(s_1+s_2)/2+(1-s_1s_2)g/2. Therefore Delta(F)=I(g)/2<=n/2. For every set of size2r+1, the majority coefficient magnitude is binom(2r,r)/2^(4r), proved by its pivotal central slice and the identity (1-z)^(2r)(1+z)^(2r)=(1-z^2)^(2r). Central-binomial lower bounds give

    B_abs/Delta(F)>=2^(2r)/[2(4r+1)(2r+1)^2] -> infinity.

This is an infinite-family proof; exact finite certificates corroborate it. Failure at fixed heavy arity two means adding a slice-count constant will not repair the reference. The same family's actual mixed entropy is [E(g)+ln4]/4, while Delta_mixed=(I(g)+1)/4. Its full corrected entropy remains paid by the symmetric baseline. The linear absolute-coefficient budget discards cancellation that the exact quadratic profile preserves. No FEI counterfamily is asserted.

Independent A045 review: REVIEW_A045.md reconstructs every clause of A045-MIXED-REFERENCE-ADMISSION-DEGREE-AUDIT@1, hash71bbc3bef10c23401d07806f2a8b948408858c821e700fce94ee9c7a126bd84a, without repair. Verdict HOLDS at exact scope. It verifies the full mixed reference normalizer, harmonic TC factor, actual biased/fair admission counterexamples, coupled phase product-law witness, separable-sign iff characterization, and strict unequal-KL fixture. No A045 code was executed.

Exact first unsupported line: E_mixed/Delta_mixed=E_Rd[ln(v_Uv_T/P)/(d-1)] is still not proved bounded for all actual two-weight thresholds. A root-Delta bound would also suffice. The physical signed profile is now established, but its absolute mixture is excluded. A viable coefficient/matrix reference must retain amplitudes through squaring and charge their quadratic spectral entropy, with the harmonic ordinary spectral-TC rebate intact. Conditional-input TC and spectral erasure remain distinct; the recovered pivotal-credit failure remains precisely coefficient one, not every larger multiplier.

## executed validation with domain, arithmetic, commands and outputs

Frozen before computation: out/FROZEN_SPEC.json. Commands from A041:

    python -X utf8 runs/20261014T012508Z-fleet05-A041-weighted-threshold-fei/code/check_stage.py --pilot
    python -X utf8 runs/20261014T012508Z-fleet05-A041-weighted-threshold-fei/code/check_stage.py

Pilot v1 passed2,744 assertions in0.229s; main v1 passed4,547 in0.861s. An amendment adds two exact product-law/determinant assertions on the already frozen coupled-phase fixture, with no domain or arithmetic change. The amendment-save command returned a live shell session; the checker was inadvertently started before that save completed. File times exposed this (draft output01:35:10Z, amendment01:35:14Z). Awaited completion, preserved the draft, then reran after the amendment existed. out/AMENDMENT_TIMING.json records the event; no mathematical assertion failed. Only that final v1.1 output counts:4,549 assertions in1.156s.

Final domain:12 exact count-compressed majority-profile family members r=1..12 (up to49 light inputs), independent full actual truth-table transforms at r=1,2 (7 and11 total bits),190 frozen two-weight thresholds on group sizes(2,2),(3,3), weights1/2,2,4, all half-integer threshold cells and two B-bias profiles, giving1,026 nonempty coefficient-process variation checks; all20 specified one-/two-bit Boolean catalog tables; four A045 explicit admission/KL fixtures. The 49-input calculation uses proved permutation symmetry and exact binomial counts, not a49-bit truth table. No dimension is raised automatically.

Arithmetic is Fraction throughout spectra, Parseval, variation, binomial formulas, degree normalizers and likelihoods. Entropy/KL signs use24-term rational atanh enclosures with omitted tail at most2z^49/[49(1-z^2)], power-of-two range reduction and outward export to2^-80. Exact multiplicative log-factor identities certify the coherent family formulas; interval overlap alone is not used to claim equality. The independent five-bit source certificate reproduces M=60993/262144, Delta_mixed=122391/262144 and a strictly negative rational interval for degree KL minus ordinary TC. All computations are under the frozen60-second cap, estimated90MB; peak memory unmeasured. No>300MB/heavy job, GPU, background worker or external write was started.

## proof dependencies and changed downstream conclusions

A045's original independent acceptance of A041 pure-sector@1 is locally consumed without modifying the original statement, run or shared registry. A045's own reference/admission audit is independently accepted at original hash. This reduces the B09 review queue while the scoped physical-profile obstruction continues the existing target, rather than launching a new broad candidate.

The new representation/obstruction depends only on actual Boolean Fourier integration, physical character absolute moments, the explicit threshold family and elementary binomial identities. The symmetric baseline is used to diagnose that the actual family remains paid, not to prove divergence of B_abs. A042's majority theorem is contextual, not a premise of the new result. No source dependency is contradicted or invalidated; the refuted B_abs payment is an unregistered newly tested mechanism. Neither A041's pure-sector theorem nor A045's valid degree reference is refuted.

B09/A045/A024 can now discard absolute tail mixing even when every component is an admissible symmetric gate and total variation is bounded. The precise information to keep is the signed quadratic coefficient profile; mass, slice count and Boolean admission alone do not pay its complete-set logarithm. No universal constant or C018/C019 payment improves this stage.

## one next mathematical action and independent reviewer

NEXT: construct a normalized quadratic coefficient-process or matrix reference for the physical signed profiles, using their bounded variation but retaining cancellation through squaring. Test it first on the exact rank-one profile control (4)-(9), and retain A045's degree-normalized harmonic TC and the already owned root sectors. A090/A091 or A085 should independently check the pivotal-slice central coefficient and exponential B_abs lower bound; A045/A024 should consume the failed-reference certificate before normalizing a tail prior. This is the first substantive failure of this absolute-cofactor mechanism, distinct from earlier mass-only and scalar-tax failures.

## actual persistence receipts or precise save blocker

All four protocol files, proof, independent review, code, frozen specifications, exact outputs and timing correction are saved only in this A041 run. STATUS.md is two lines, WORKLOG.md appended and LEARNED.md updated. Saver validates exact protocol field sets, original claim hashes, progress-copy bytes, report headings/final bridge and files below20MB, then records and verifies local receipts. Prior runs, other agents, source trees, board, brain and shared indices remain unchanged. New obstruction review, supervisor adoption/copy and remote mirror verification are pending. No local save blocker exists.

The first save attempt assumed A045 used A041's compound statement/hypotheses hash and stopped at that assertion. Reading A045's finalizer showed its new claim hashes the statement alone; both conventions are now verified explicitly, preserving the original hash and hypotheses. out/HASH_CONVENTIONS.json records this serialization-convention correction; no mathematical source gap or repair was found.

**Universal bridge:** This stage moves B09's G-BIASED-LTF mixed-sector target toward C020 whole-set reference cost by proving an arity-free, total-variation-two physical signed-cofactor interface and excluding its natural absolute-mixture budget with an exponential actual Boolean family at fixed heavy arity two. It consumes the independent pure-sector acceptance and independently accepts A045's full degree/admission audit, retaining the harmonic spectral-TC correction. It gains no mixed-payment constant: the exact degree-normalized logarithmic expectation remains open, as does full FEI. NEXT replaces the now-false linear absolute-cofactor budget by a quadratic signed reference, directly addressing that unpaid universal mechanism instead of another isolated gate bound or endpoint grid.
