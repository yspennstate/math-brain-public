## Current owner assignment: full FEI in this environment, 11-21 October 2026

This environment's twenty enabled account01/B01-B20 jobs focus on full FEI through **21 October 2026 at 19:15:57 UTC (22:15:57 Asia/Jerusalem)**. The native full-FEI assignments were installed concurrently and are preserved. Their primary plan and B-stream ownership are in `yspennstate/math-open-problems`, `reports/fei-2026-10-11/`. The additional report, seed lemmas, sources and counterexamples are in `research_pushes/2026-10-11-full-fei-100-agents/` in both private repositories. Its `NATIVE_MAPPING.md` maps proposed F-role groups to live B streams; Fnn is not a replacement native identity.

For these twenty jobs during this fixed window, the owner's full-FEI priority supersedes older Brain-maintenance, movie, Primary Directive, OPEN_PROBLEMS_200 and mixed-portfolio assignments. Stalled work changes mathematical route within FEI. B20 must not restore this account's obsolete prompts through the older shared OWNER_CONTROL JSON or a historical renderer. Preserve shared controls for other accounts and leave the five disabled jobs untouched. Do not restart or extend the deadline, create more schedules, or claim 100 simultaneous workers.

Existing source holds, access restrictions, usage limits and honest-proof requirements retain their scope. Continue the installed immutable B-stream result paths and Brain handoffs, preserve peer-owned work, and verify saves. The reports and campaign remain private. Only the separately owner-approved completed threshold-paper package is authorized for the public paper repository; the strategy report, task metadata and private Brain history are excluded. Any permitted publication follow-up must use the latest verified paper package and preserve Claude's repository work.

<!-- FULL_FEI_ACCOUNT01_20261011_OVERRIDE_END -->

# Current scheduled-fleet direction: all 80 workers on FEI

Effective owner order: **FEI-ALL-TEAM-20260922T095941Z**; control revision **2026-09-22.3**; initial state revision **FEI-20260922T1000Z-v1**.

All eighty existing workers now target full FEI. The older restricted allocation and expired sprint below are historical; valid mathematical results and scoped refutations remain evidence.

The sole target for account01-account04/B01-B20 is full uniform-cube Fourier Entropy-Influence: one finite dimension-independent C such that H(f) <= C I(f) for every finite Boolean function, with entropy in bits, or a rigorous Boolean counterfamily with unbounded H/I. Full FEI remains **OPEN**.

Read the fresh [owner order](https://github.com/yspennstate/math-research-brain/blob/main/scheduled_tasks/work/shared/fei-all-team-2026-09-22/ORDER.md), [current research state](https://github.com/yspennstate/math-research-brain/blob/main/scheduled_tasks/work/shared/fei-all-team-2026-09-22/CURRENT_RESEARCH.md), [claim register](https://github.com/yspennstate/math-research-brain/blob/main/scheduled_tasks/work/shared/fei-all-team-2026-09-22/CLAIMS.json), [pathways](https://github.com/yspennstate/math-research-brain/blob/main/scheduled_tasks/work/shared/fei-all-team-2026-09-22/PATHWAYS.md), [80 assignments](https://github.com/yspennstate/math-research-brain/blob/main/scheduled_tasks/work/shared/fei-all-team-2026-09-22/ASSIGNMENTS.md), and [memory protocol](https://github.com/yspennstate/math-research-brain/blob/main/scheduled_tasks/work/shared/fei-all-team-2026-09-22/MEMORY_PROTOCOL.md). Resolve current main and its MANIFEST.json, required DELTAS.json events and live CORRECTION_INBOX.json before relying on a remembered premise. Initial publication is pinned [here](https://github.com/yspennstate/math-research-brain/blob/0ac3a26c826ff29ae5fc36bc768319a1ff1d045c/scheduled_tasks/work/shared/fei-all-team-2026-09-22/MANIFEST.json); later source-backed corrections can supersede it.

Allocation: Path A 32 workers (B01-B06,B13-B14 per account); Path B 28 (B07-B10,B15-B17); Path C 20 (B11-B12,B18-B20). Each slot has a distinct task, exact inputs, deliverable, acceptance condition, cross-account partner and next recipient. B20 has compact secondary keeper duties and a real FEI proof assignment.

New complete mathematics belongs in this repository under proofnet24/P03-fei/fleet-2026-09-22/<account>/<slot>/<actual-unique-run>/. Source-bound handoffs, immutable correction events and worker-owned memory snapshots belong in the canonical brain bundle. Do not treat publication as verified all-worker adoption or native memory ingestion; actual scheduler rollout is recorded in [ROLLOUT.json](https://github.com/yspennstate/math-research-brain/blob/main/scheduled_tasks/work/shared/fei-all-team-2026-09-22/ROLLOUT.json).

## 24 September 2026: monotone functions (bounded-width DNFs proved; the full monotone case open)

**Full FEI remains OPEN, also for monotone functions.** FEI for all monotone functions would give total influence
Omega(log^2 n) for monotone graph properties, where the best bound known is log^2 n/(log log n)^2 (Kelman, Kindler,
Lifshitz, Minzer and Safra); continuation [2026-09-24-monotone](continuations/2026-09-24-monotone/REPORT.md) records
this, exact data for all monotone functions of six variables and three proof routes that fail. Continuation
[2026-09-24-downset](continuations/2026-09-24-downset/REPORT.md), paper
[fei_monotone_width.pdf](continuations/2026-09-24-downset/paper/fei_monotone_width.pdf), proves for monotone f, with
m = min(Pr[f=0], Pr[f=1]) and Psi(r) = log2(e(r + 2 sqrt r + 2)): the restriction step at any coordinate satisfies
Delta_v <= Inf_v (4.64 + Psi(4m/Inf_v - 2)); hence H(f) <= 9.41 I(f) for every monotone 2-DNF and 2-CNF (indicators of
independent sets and vertex covers of any graph), H(f) <= (w + 8.1) I(f) for every monotone DNF or CNF of width w with
no bound on the number of terms or on how often a variable occurs, and more generally for restriction-closed monotone
classes whose members have a minterm or maxterm of size at most w; the influence-entropy bound
H <= sum_v h(Inf_v) = O(I + sum_v Inf_v log(1/Inf_v)) (subadditivity of entropy, Keller, Mossel and Schlank 2012;
reproved by Han 2025) holds with influences measured relative to m; and FEI for monotone functions reduces to monotone
functions all of whose influences are small compared with m.
The proof uses the uniform measure on the zeros of f, where a coordinate is a fair coin unless it is blocked.
The same classes satisfy O'Donnell and Tan's strengthened inequality H+ <= C (I - Var), with C = 17.43 for 2-DNFs and
at most 2w + 14.8 for width w, so FEI also holds for read-once formulas over AND, OR, XOR and threshold gates of any
fan-in (and bounded-width DNF gates with balanced inputs) whose inputs are monotone DNFs or CNFs of bounded width.
With the influential-variable theorem of O'Donnell, Saks, Schramm and Servedio the same step bound gives
H(f) <= (log2 log2 s + 7.85) I(f) for every monotone function computed by a decision tree with s leaves (Wan, Wright and
Wu had 12 d for expected depth d and I >= 1), H(f) <= (log2 m + 8.85) I(f) for every monotone DNF with m terms, and
H(f) <= (2 log2 s(f) + 7.85) I(f) with s(f) the sensitivity. On every restriction-closed class the conjecture is equivalent to a local
statement, R(f) = E_S sum_{v in S} log2+(P(S - v)/P(S)) <= K I(f): removing one element of the spectral sample raises
its weight by at most a bounded factor on logarithmic average (paper Proposition 6.3).
Checked exhaustively on all 7,828,354 monotone functions of six variables and on graph and formula families up to 20
variables; the scalar core of the erasure bound and the arithmetic of the minterm lemma are checked in Lean 4 with
Mathlib (continuation lean/). Under product measures with every bias in [eps, 1 - eps] the same classes satisfy the
biased strengthened inequality with constant 14.24 + 2w log2(1/eps) (paper Theorem 1.10), so bounded-width DNF gates may
take inputs of such biases; the Jensen-Shannon part of the biased step is bounded by the two-point logarithmic Sobolev
constant, which the sigma^2 factors pay for (paper Lemma 6.2). Open: biases tending to 0 or 1. There the one-coordinate
induction still works numerically with the AND constant 2 + 4 log2 e (largest step ratio 7.7702 over graph gates, 6.87
over random 2- and 3-DNF gates), so what is missing is an erasure bound that sees lopsided weight pairs. Also open, with
data: whether every coordinate of largest influence satisfies Delta_v <= K Inf_v (K = 6.01 on all monotone functions of
six variables and the standard families), which would give FEI for all monotone functions.

## 23 September 2026: read-k DNF formulas, threshold functions and their unions (proved classes)

**Full FEI remains OPEN.** Continuation [2026-09-23-readk-dnf](continuations/2026-09-23-readk-dnf/REPORT.md), paper
[fei_readk_regular.pdf](continuations/2026-09-23-readk-dnf/paper/fei_readk_regular.pdf) (code and logs beside it). Proved,
with explicit constants: H(f) <= min(2.89 + 9.9k, 30 + 5.6 log2 k) I(f) for read-k DNF and CNF formulas (the log k matches the min-entropy bound of Arunachalam et al.); H(f) <= 15.1 I(f) for regular
(2-monotone) functions, which contain all linear threshold functions (FEI for threshold functions was open);
H(f) <= min(3.9 + 21.2k, 54 + 12.8 log2 k) I(f) for unions and intersections of regular functions in which every variable is relevant to at
most k of them (contains both previous classes), and H(f) <= (54 + 12.8 log2 k + 6.8 log2 M) I(f) when each of the
unioned functions is itself a Boolean function of at most M regular functions (unions of M-facet polytopes; read-k
unions of arbitrary functions of at most M variables); H(f) <= (16.5 + 8.4 ln m) I(f) for Boolean functions of m regular
functions; all four classes satisfy O'Donnell-Tan's strengthened inequality, so FEI holds for read-once formulas over
them with bounded-arity gates or gates from these classes with balanced inputs (iterated majorities of any odd fan-in:
constant 66). AND, OR and XOR of any fan-in satisfy the biased strengthened inequality with the sharp constant
2 + 4 log2(e) under every product measure. Symmetric threshold gates T_{t,r} of any fan-in satisfy the biased
strengthened inequality with constant 66.4 when their inputs have a common bias (report section 25), so FEI also holds
for iterated threshold functions with arbitrary thresholds and fan-ins; under arbitrary product measures they satisfy
the biased inequality with I in place of I - Var (26.3 I nats, report section 26), which composes with one constant per
level and gives H(f) <= (38d + log2 e) I(f) for read-once formulas of depth d over AND, OR, XOR and threshold gates of
any fan-in; and they satisfy the strengthened biased inequality itself with constant 760 (report section 27), so FEI
holds with constant 760 for every read-once formula over threshold gates of any fan-in and any depth (the case where
one input is pivotal with probability above 9/10 is perturbative: the other inputs are then nearly deterministic);
the proof of the equal-bias case splits the normalisation by the chain
rule into marginal divergences (paid by the sigma factors) and the total correlation of the conditional law, which a
tilt bounds. Mechanisms: witness activation with a path lemma (terms), a desirability
order with Sperner/Littlewood-Offord (threshold functions), and their combination (unions).

Open questions left there with their reductions: (1) a constant independent of k for read-k DNFs, which is the
conjecture for all DNF formulas (report section 19 has the O(log k) proof: a rooted-animal reference measure that
activates one term per connected piece of the cover); (2) the biased strengthened
inequality for threshold functions, read-k DNFs and symmetric gates: the largest ratio found, in exact arithmetic, is
2 + 4 log2(e) = 7.7708 in all three classes, attained only by AND2/OR2 at extreme bias (report sections 12 and 17); a
proof for weighted threshold functions would give FEI for read-once formulas over weighted threshold gates (for
symmetric threshold gates it is proved, report section 27); for general symmetric gates it reduces to a
biased uncertainty inequality stated in report section 18. Report sections 21-24: the biased left side equals sum_A P(A) log(4^|A| / (E d_A g)^2)
(expected mixed derivatives), a first-element (martingale) rewriting, and a hybrid reference that is bounded (<= 6.1 J)
on every adversarial and one-parameter test so far, with the remaining lemma stated.

---

## Preserved earlier content

# FEI research: current recovery and continuation

## Owner continuation, 21 September 2026: the read-once constant is certified; seven tasks per account, creative attempts only

**Full FEI remains OPEN / NOT PROVED.** The owner's order of 21 September 2026 (12:37 his clock): in every account
seven scheduled tasks work on FEI, no audits, only creative out-of-the-box approaches to the full conjecture. Read
[the order and what a run delivers](continuations/2026-09-21-readonce-certificate/TASKS_2026-09-21.md), then
[the report](continuations/2026-09-21-readonce-certificate/REPORT.md), then
[fourteen routes](continuations/2026-09-21-readonce-certificate/APPROACHES.md); the
[handoff](handoffs/2026-09-21__readonce-certificate-and-approaches.md) lists the files.

What is new and proved: for every read-once formula over AND, OR, NOT, H(f) <= 6.4573 I(f) (a reduction of the whole
class to one inequality in two real variables, plus an interval-arithmetic certificate; the bound published before
was 10). Numerically the sharp read-once constant is Hod's beta(1/2) = 6.4547837, with Hod's construction extremal,
also over gates of fan-in three. What is measured about the general case: the restriction identity
Delta_i H = JS(p_0, p_1) + sum_S m(S) h(q_{i,S}); the potential-free restriction step needs exactly 4.8677 on all
functions of at most five variables, 6.0037 on width-2 tribes, and is bounded on every family tried; the four
simplest potentials do not help; the Jensen-Shannon term is what a general potential must absorb. Code, the two
certificate candidates and the verification logs are in the continuation's `code/` and `data/`.


## Owner continuation: unequal Fourier magnitudes and lattice-valued projections

**Full FEI remains OPEN / NOT PROVED.** Read the [new handoff](handoffs/2026-09-20__spectral-lattices.md), [complete proof](continuations/2026-09-20-spectral-lattices/REPORT.md), [exact checker](continuations/2026-09-20-spectral-lattices/verify_spectral_packets.py), [actual output](continuations/2026-09-20-spectral-lattices/verification.json), and [verified manifest](continuations/2026-09-20-spectral-lattices/MANIFEST.json). The exploratory folder preserves unsuccessful approaches as well as the explicit counterexample.

For each distinct nonzero Fourier magnitude a, let f_a be the inverse Fourier transform of the coefficients of magnitude a. If every PHYSICAL function f_a takes values in `2^-s Z`, for one integer `s>=0`, then

    H(f) <= (4+2s) Ifrak(f) <= (4+2s) J(f) <= (4+2s) I(f).

The theorem allows arbitrarily many unequal Fourier magnitudes and several coefficient valuations. Integer-valued components give constant four, half-integer-valued components give six. This is not merely a condition on Fourier coefficient denominators. The proof extends the preceding centroid theorem to integer flat packets, proves a Boolean projection lattice bound, and pays the large-bias case separately by isoperimetry. The earlier stronger finite-k plateaued bound is retained, not re-announced as new. Class constant four is optimal in the limit; publication priority is unverified.

Independent logical factors with exponents at most s keep the same coefficient after jointly SURJECTIVE affine mixing. Another corollary gives constant four for signed flat-spectrum indicators of possibly NONAFFINE physical cells with distinct actual tags. A separate selector theorem permits arbitrary Boolean branches sharing the same residual variables, provided the selectors have disjoint Fourier supports as well as a signed physical partition; its coefficient is `max{4,C}`. These hypotheses are not a universal representation theorem.

An explicit five-variable Boolean function `f_*=1-2*1{y1=x1*x2,y2=x1*x3}` has Fourier magnitudes 1/2 and 1/4 but magnitude components `1/2` and `f_*-1/2`, which are not integer-valued. Thus automatic integrality is false even for power-of-two amplitudes. Its tensor powers require arbitrarily fine merged grids, while H/I stays 28/15. Neither fact refutes FEI; both rule out dropping the new hypothesis without further work.

For every Boolean function the report gives an exact nonnegative arithmetic remainder D and the universal inequality `H<=4 Ifrak+2D`. It does NOT bound D by a universal multiple of influence. That remaining step is comparable in scope to FEI and is not counted as solved by naming D. Keep the original erasure/selector target and all earlier retired-route warnings.

The final checker passed all 65,812 Boolean functions through dimension four, 147,348 nonempty magnitude components, all 6,651 ternary functions through dimension three, explicit examples through dimension fifteen, 16 affine/character images, 24 shared-branch pairs, and 257 scalar checks. These overlapping finite families do not establish exhaustive FEI coverage at their largest dimension. A separate replay of the exact committed checker produced byte-identical output. All delivered scientific file blobs were read back and matched local bytes. No independent review or proof assistant was used.

Proof commit `bce8ebea37f535bc7a9bdc8845f7fc16b1075dab`; checker `28264ba544ef4b96de2e0f1f4c2b9d893866b88e`; output `5f5b7abd061b635575eb00ad9a7718d2eee5ebb3`; handoff `d4fe7ef0614ae8132ea1c649636eee399dcb294d`. All preceding sections are retained below. No schedules, ownership, permissions, visibility or native atlas metrics were changed; delivery does not demonstrate subsequent worker uptake.

## Owner continuation: centroid theorem, uniform-spectrum bound, and complete Booleanity recovery

**Full FEI remains OPEN / NOT PROVED.** The [new handoff](handoffs/2026-09-20__centroid-and-carries.md) links the [complete proof](continuations/2026-09-20-centroid-and-carries/REPORT.md), [integer checker](continuations/2026-09-20-centroid-and-carries/verify_centroid.py), [actual output](continuations/2026-09-20-centroid-and-carries/verification.json), [manifest](continuations/2026-09-20-centroid-and-carries/MANIFEST.json), and [preserved exploratory records](continuations/2026-09-20-centroid-and-carries/exploratory/).

The centroid candidate (C) explicitly left UNPROVED in the earlier affine-symmetric worklog is now proved analytically, with a stronger weighted pairing theorem. For a nonzero binary polynomial P, its support A of size M, and the sorted distances a_1<=...<=a_M from any center,

    a_j+a_(M+1-j) >= n-deg(P),
    E_{x uniform A}|x+b| >= (n-deg(P))/2.

For nonnegative coordinate costs c, the pairing threshold is sum(c_i)-D_c(P), where D_c(P) is weighted monomial degree. Orthogonality of evaluation spaces and a triangular evaluation-rank bound give the proof; finite searches are not used as a theorem. This entry supersedes only the earlier centroid candidate's unresolved status. The original worklog and its other limitations are retained below.

For Boolean functions whose nonzero Fourier coefficients all have the same magnitude 2^-k (plateaued spectra, with no affine-support assumption), the centroid theorem and the inherited bottom-Walsh-digit observation give

    H(f)=2k,       Ifrak(f)>=(k+1)/2,
    H(f)<=4k/(k+1) Ifrak(f)<4 Ifrak(f)<=4 I(f).

The class constant four is optimal in the limit by the standard addressing example. It is NOT a universal FEI constant. The first-layer scalar influence corollary was already available from isoperimetry and is not re-announced as new. Independent publication priority has not been established.

The same report proves a carry obstruction: for odd n and the genuine Boolean symmetric function f=1-2*1_{|x|=1}, binary digit ell of W(S)/2 has algebraic degree exactly 2^(ell-1), whenever 1<=ell<=n-2 and 2^(ell-1)<=n. Thus a linearly growing bound for higher amplitude-digit degrees is false. This does not refute FEI or every possible multiscale method. Unequal Fourier masses and multiple valuation layers remain outside the positive theorem.

All scientific files in the previously conversation-only exact-Booleanity package are now on master, including its [full report](continuations/2026-09-20-booleanity-order/REPORT.md), [checker](continuations/2026-09-20-booleanity-order/verify_booleanity_order.py), [actual output](continuations/2026-09-20-booleanity-order/verification.json), exploratory code/output, original manifest and handoff. The [delivery recovery](continuations/2026-09-20-booleanity-order/DELIVERY.md) supersedes their historical pending-delivery language and records actual commits and verified hashes. Its counterexamples remain real-valued relaxation counterexamples, not Boolean FEI counterexamples.

Both the recovered checker and the new checker were replayed with byte-identical output. The new checks include 3,152,586 unweighted center profiles, 2,880 weighted profiles, 2,136 plateaued Boolean functions through dimension four, and 23 exact digit identities through dimension seventeen. Families overlap; the counts do not represent exhaustive FEI coverage in the largest dimension. No independent audit or proof-assistant formalization is claimed. New proof commit `9c931d664c65a363fa3fad1c1ddca8d72c4d1411`; checker `0b4a7066a6f2a2818db37343059065cf69039951`; output `07c48ed7db932a53ce8af781c658e93ef0ca2387`; handoff `27a49b3487d4c41b8b4ba4afce94a132bbdd28f4`.

The universal mass-weighted erasure/entropy obligation is unchanged. All preceding sections are preserved below. No schedules, ownership, permissions, visibility, or native atlas metrics were changed; repository delivery does not establish later-worker uptake.

## Owner continuation: affine-symmetric stopping and precise endpoint quantifiers

**Full FEI remains OPEN / NOT PROVED.** Read the [handoff](continuations/2026-09-20-affine-symmetric-stopping/HANDOFF.md), [main proof](continuations/2026-09-20-affine-symmetric-stopping/REPORT.md), [endpoint proof](continuations/2026-09-20-affine-symmetric-stopping/ENDPOINT_QUANTIFIERS.md), and [manifest](continuations/2026-09-20-affine-symmetric-stopping/MANIFEST.json).

The new stopping theorem is

    H((-1)^ell product_t h_t((Lx+b)_{U_t})) <= 32.08 Ifrak <= 32.08 J <= 32.08 I

for arbitrary fully symmetric Boolean factors on disjoint LOGICAL blocks, any jointly SURJECTIVE affine input map L, and an affine output phase ell. Logical forms may overlap extensively on physical coordinates. The constant does not depend on factor degree, number of factors, or the particular surjective map. This uses the published symmetric coefficient 12.04, a new directional-orbit/parity-section payment, and the previously proved exact affine-minimum tensorization/lifting identities. It is not an improvement of the 12.04 coefficient on its original class. Arbitrary dependent logical forms and arbitrary additional quadratic output phases remain outside the theorem. The proof explicitly shows that allowing all dependent forms would already encode every Boolean function.

The companion theorem disproves a stronger endpoint proposal: no universal C pays EVERY prescribed relevant coordinate for `A_i=Phi_n(f)-E Phi_(n-1)(f_child)`, `Phi_d=d(sum |fhat|^(2-1/d)-1)`, even when every input variable is relevant. The construction combines the known bent-background bad split with genuinely relevant rare-factor padding. This does NOT refute a universal EXISTENTIAL coordinate selector, the character-child theorem, or FEI. A finite analytic example has ratio greater than 4.37; its huge truth table was not enumerated.

The [main checker](continuations/2026-09-20-affine-symmetric-stopping/verify_affine_symmetry.py) and [output](continuations/2026-09-20-affine-symmetric-stopping/verification.json) cover all 65,812 Boolean functions through dimension four for 262,948 split checks; all 16,380 symmetric truth tables through dimension twelve; and 108 surjective affine product lifts. The [endpoint checker](continuations/2026-09-20-affine-symmetric-stopping/verify_endpoint_quantifiers.py) and [output](continuations/2026-09-20-affine-symmetric-stopping/endpoint_verification.json) check 5,460 base fibres, 21 all-relevant products through dimension seventeen, and the finite analytic certificate. Both checkers passed separate replays with byte-identical output. Remote blobs were checked against local bytes. These are finite self-checks, not independent review, proof-assistant formalization, or publication-priority clearance.

The [worklog](continuations/2026-09-20-affine-symmetric-stopping/WORKLOG.md) preserves the other full-scope attempts, including a proved dyadic support observation and an explicitly UNPROVED centroid candidate. Its exact finite code search is not used as a theorem and its immediate influence consequence was already available from edge isoperimetry. Do not promote these tests to FEI closure. The remaining universal erasure/selector gap is unchanged. Final main proof commit `45414cf13c0d1a28f3bd1eb641590e2c49f50cba`; endpoint proof `0e0ceff8e9f0a6aecb17dacc38e04b5bfd882816`; handoff `43a0cdcbfc165989301cb5ba65aaba30e2b8e0a2`. No schedules, ownership, permissions, visibility, or native atlas metrics were changed. Repository availability is not evidence of subsequent worker uptake.

## Previously indexed continuations — retained without removing their hypotheses

**Full Friedgut–Kalai Fourier entropy–influence conjecture: OPEN / NOT PROVED by these continuations.** Owner-requested update: 20 September 2026. The latest continuation extends polynomially coupled symmetric cores and combines them with the concurrently developed affine-fibre gluing theorem. It also records a counterexample to an attempted general-operator relaxation, not to FEI.

## Additional owner continuation: directional recovery and a sharper restriction bound

The previously conversation-only directional-compression package is now on `master`: [complete original proof](continuations/2026-09-20-directional-compression/REPORT.md), [original checker](continuations/2026-09-20-directional-compression/verify_directional_compression.py), [actual output](continuations/2026-09-20-directional-compression/verification.json), and [delivery recovery with commits and verified hashes](continuations/2026-09-20-directional-compression/DELIVERY.md). Its report and original handoff are byte-preserved; their earlier pending-delivery statements are historical and superseded by the delivery record.

Continue from the [new handoff](handoffs/2026-09-20__concave-restriction.md), [concave restriction proof](continuations/2026-09-20-concave-restriction/REPORT.md), [new exact checker](continuations/2026-09-20-concave-restriction/verify_concave_cap.py), and [actual output](continuations/2026-09-20-concave-restriction/verification.json).

For a physical Fourier fibre `(u,v)`, set `w=u^2+v^2`, `t=min(u^2,v^2)/w`, `M=sum w t`, `V=sum w(t-M)^2`, and

    Psi(t)=h2(t)+1-h2(1/2+sqrt(t(1-t))).

The exact restriction identity and the new concavity proof give

    Delta_i H = sum w Psi(t) <= Psi(M)-(2/ln 2)V <= Psi(M) <= Psi(j_i).

Dyadic Walsh integrality forces equality in `Delta_i H<=Psi(M)` to occur only at `M=0` or `M=1/2`. The recovered directional-compression theorem now transfers leaf constant `C0` with `max{C0,2^d Psi(2^-d)}`. For quadratic directional derivatives its sufficient payment floor improves from **6.130502579614... to 5.826796887175...**. This is not a universal FEI constant, and a nonzero low-degree direction need not exist.

For products sharing one physical control but having disjoint residual blocks, absolute child-spectrum affinities multiply. Hence the valid replacement bound is

    Delta_control H(product) <= Psi((1-prod_l(1-2M_l))/2) <= sum_l Psi(M_l).

Do not substitute actual factor decrements for these upper envelopes: the recovered eleven-variable example disproves raw shared-control decrement subadditivity. Nor can the new envelope alone supply a universal paid coordinate: every coordinate of a one-point defect has `Psi(M_i)/j_i` growing linearly with dimension. The exact fibre profile or a separately proved summable error budget remains necessary.

The new checker passed all 262,948 coordinate splits of all 65,812 Boolean functions through dimension four, 65,536 shared-control parent pairs, 80 sampled multi-factor products, and 1,089 rational-grid checks. These are finite self-checks, not unrestricted FEI or independent formal verification. Both original and new checkers were replayed with byte-identical output. New proof commit `1770be2243c753e1a2aeecbfe3b41b2ed07eb4d4`; checker `62cac0e2bfa6e8f0cd4c924b0f84a136dcfac61b`; output `fbad9be02ea31ce9b412e4caf17f1238c03dfb84`; handoff `fbbfd2dfd9392fe6e31672cce705c7b8bb7b76d1`. This index addition preserves the concurrent polynomial-core continuation below. No worker uptake, schedule change, or priority clearance is claimed.

The complete immediately preceding index, including the affine-fibre theorem, quadratic-symmetry theorem, Han-overlap obstruction, recovery warnings, and earlier links, is preserved **byte-for-byte** at [README_before_polynomial_cores_be66b911.md](README_before_polynomial_cores_be66b911.md), original blob `be66b9115a00b721b72b262dd595fbebd49f5ff3`. Its relative links still work. No prior reports, worker instructions, schedules, ownership, permissions, visibility, or native finite-dimensional metrics were changed.

## Latest continuation: polynomial cores and polynomial tag phases

Start with the [handoff](continuations/2026-09-20-polynomial-cores-and-tags/HANDOFF.md). The [main proof](continuations/2026-09-20-polynomial-cores-and-tags/REPORT.md) establishes

    H((-1)^P product_t h_t) <= max{12.04+log2(max_t d_t), 2^r h2(2^-r)+2/ln 2} J

when the h_t are part-symmetric on disjoint physical groups, with at most d_t parts in group t, and P has degree at most r over F_2. There is no number-of-cores penalty, even with arbitrary cross-core polynomial interactions. For r<=7 the coefficient remains `12.04+log2(max_t d_t)`. Symmetry cores themselves may have unbounded algebraic degree. The single-core degree-r theorem and degree-seven constant were already proved in the [scheduled single-core report](scheduled-continuation/runs/2026-09-20/2026-09-20T03-23-21Z__report.md); they are explicitly credited, not re-announced as new.

The [polynomial tag extension](continuations/2026-09-20-polynomial-cores-and-tags/TAG_PHASE_EXTENSION.md) consumes the [concurrent affine-fibre gluing proof](continuations/2026-09-20-affine-fibres/REPORT.md). For actual existing tag coordinates x, affine fibres of pi(y), and physical sections satisfying H<=C0 J, it proves

    H((-1)^{Q(x)+x dot pi(y)} g(y)) <= max{4,C0,2^(r-1) h2(2^(1-r))} J

for an arbitrary degree-r tag polynomial Q, r>=2. Arbitrary cubic tag phases retain the sharp class constant four for quadratic sections. Arbitrary degree-at-most-eleven tag phases retain 12.04 when the sections use the newly certified polynomially coupled symmetric cores. Valid affine-fibre gluing can be iterated without a depth penalty. This is not an unrestricted representation theorem, and arbitrary mixed tag/data phases or fixing newly appended tags are not covered.

The proofs include a joint physical block-deletion identity, a degree-sensitive cross-core payment, a local-defect weighted bound, and an exact phase-comparison identity in which the restriction mutual information cancels. The main product class also carries the stated hereditary allocation certificate; the affine-fibre closure must not be mislabeled as closure under arbitrary restrictions.

## A full-scope route tested and ruled out

The [operator obstruction](continuations/2026-09-20-polynomial-cores-and-tags/UNITARY_ERASURE_OBSTRUCTION.md) disproves a dimension-free inequality bounding averaged column erasure entropy by normalized trace-norm coordinate commutators for arbitrary real orthogonal involutions. The explicit ratio exceeds `log2(M)/10` along the constructed family. Such a general inequality would have implied FEI, but it is false. The matrices are **not** Boolean convolution matrices, so FEI itself is not refuted. A successful operator proof must retain more structure.

## Exact executable evidence

The [core checker](continuations/2026-09-20-polynomial-cores-and-tags/verify_polynomial_symmetry.py) and [output](continuations/2026-09-20-polynomial-cores-and-tags/verification.json) cover 46,634 overlapping core/phase parameter cases, 365,403 physical restriction assignments for polynomial structure, and 2,308 universal block-deletion cases. The [tag checker](continuations/2026-09-20-polynomial-cores-and-tags/verify_tag_phase.py) and [output](continuations/2026-09-20-polynomial-cores-and-tags/tag_phase_verification.json) cover 81,852 exhaustive phase-comparison cases through dimension three, 280 affine-fibre/tag cases, and 1,040 derivative-gap checks. The [operator checker](continuations/2026-09-20-polynomial-cores-and-tags/verify_unitary_erasure.py) and [output](continuations/2026-09-20-polynomial-cores-and-tags/unitary_verification.json) verify the full 64-by-64 example exactly and Walsh patterns through M=256.

All three checkers passed and full reruns produced byte-identical output. [MANIFEST.json](continuations/2026-09-20-polynomial-cores-and-tags/MANIFEST.json) records byte counts and SHA256 values. Integer/rational arithmetic, exact prime-log cancellation, and rational outward logarithm enclosures are used. Finite families overlap; they are not exhaustive unrestricted Boolean coverage. Independent expert review, formal verification, and publication-priority clearance are not claimed.

## Surviving universal target and recovery warnings

A finite universal bound `sum_i H(S_i | S_{-i}) <= K I(f)` for every Boolean f would imply unrestricted FEI with coefficient `K+2/ln 2`; see the [erasure reduction](solo-2026-09-17/ERASURE_REDUCTION.md). This remains unpaid. A correctly quantified whole-function dimension-adaptive endpoint selector is another live conditional route; the concurrent affine-fibre report's coefficientwise obstruction does not refute that selector.

Do not reintroduce the false absolute-overlap selector, all-constant pointwise resolvent inequalities, fixed-coefficient affine-drift payments, zero-debt boundary decompositions, fixed-Renyi-exponent influence payments, or the false pointwise converse `H<=sum_i B_i+(2/ln 2)I`. Do not replace joint conditional entropies by universally payable sums of marginal entropies. The main report gives an exact rare-point calculation showing the latter loss diverges while H/I tends to four. Do not treat contraction of an unknown seed's positive entropy excess as proof that its excess is nonpositive.

The new stopping classes are available for further full-scope work; repository delivery does not establish that any subsequent worker has already read them. The previous [affine-fibre handoff](continuations/2026-09-20-affine-fibres/HANDOFF.md), [quadratic-symmetry proof](continuations/2026-09-20-quadratic-symmetry/REPORT.md), and all older records remain available without alteration.
