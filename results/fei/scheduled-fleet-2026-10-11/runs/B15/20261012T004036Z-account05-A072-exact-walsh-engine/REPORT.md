## exact target, quantifiers, hypotheses and units

Stage 2 follows the explicit A072 direction in B15 STREAM_NOTES v2 (2026-10-11 23:25 UTC): add B_i, JS_i and Delta_iH to the uniform engine and reconstruct masks 4194372 (n=5), 1103806792023 (n=6). Define E(f)=min over relevant physical coordinates of B_i/Inf_i. Spectral law mu(s)=W_s^2/N^2, N=2^n; characters are (-1)^popcount(x&s), tables use little-endian x. A negative mask bit means f(x)=-1. Entropy uses bits. No symmetry reduction or search: exactly two named witnesses, all 11 coordinates and 22 physical children. Pilot: all 16 two-bit truth tables, 32 coordinate cases.

## sources actually read, revisions and theorem locators

BOARD.md was read at stage start, supervisor snapshot 2026-10-12 00:39 UTC. B15 STREAM_NOTES.md v2 was read in full, including its exact witness masks, selection/composition scope, retired targets and one target per agent. Own STATUS.md was read: prior baseline complete, no need to repeat the B09 grid. The earlier protocol was retained, revision 2026-10-11-execution-v2; exact field sets are rechecked against its current local bytes. A072's prior EXACT_WALSH_INTERFACE.py and certificate/report are the reused algebraic interface. B15 lead original CLAIMS.json was read; its REPORT.md is absent. The present reconstruction uses only the original truth masks and definitions, not lead-computed spectra. Source hashes and exact consultation scopes are in out/source_receipts.json. No entropy theorem, external fact or unpublished class result is needed for this finite certificate. A073/A074 already handle selected bias-grid log/reproduction work; that work is not repeated.

## complete derivation or exact first unsupported line

First run the prior uniform certificate on every parent and physical child: integer WHT; WHT(W)=Nf; sum W_s^2=N^2; direct character sums agree; physical undirected edge counts give Inf_i=2e_i/N=sum_(s containing i)mu(s). These checks precede entropy expressions. The exact masks reconstruct the actual Boolean functions, rather than assuming a proposed spectral law is Boolean.

For a packet indexed by s not containing i let a=mu(s), b=mu(s union i), q=a+b. Define phi(a,b)=q log2 q-a log2 a-b log2 b, with zero terms omitted. Then B_i=sum_s phi(a,b)=H(S_i|S_-i). Physical children are independently made from the truth table by setting x_i=0 or 1; their spectra are certified as above. Their signed Walsh coefficients satisfy 2W_child,0=u+v and 2W_child,1=u-v for parent packet values u,v. Consequently (mu_0+mu_1)/2=q exactly, also checked by Fractions. Define JS_i=H(q)-(H(mu_0)+H(mu_1))/2 and Delta_iH=H(mu)-(H(mu_0)+H(mu_1))/2. Since H(mu)=H(q)+B_i, Delta_iH=B_i+JS_i, verified by exact prime-log coefficient equality for all 11 witness coordinates (and all 32 pilot coordinates). The average physical-child influence vector equals the parent's retained-coordinate influence vector exactly. This is the conserved physical ledger, not an entropy-payment bound.

For every positive rational t, factor numerator and denominator and record log2 t=sum_p valuation_p(t) log2 p. Every entropy and erasure expression is therefore a finite rational coefficient map. The zero term t log t is omitted. Exact equality of maps certifies equality of the expressions. Nonzero prime-log forms cannot cancel: clearing denominators gives a product of prime powers; unique factorization detects exact zero. To compare two maps, clear rational denominators D and compare A=product_(e_p>0)p^e_p with B=product_(e_p<0)p^(-e_p). The sign of the original form is the sign of A-B because the logarithm is strictly increasing and D>0. All products are Python arbitrary-precision integers. The checker uses the integer bound sum_p |e_p| bit_length(p) before construction and refuses above the frozen 8000000-bit budget. It stores the exponents, denominator and product bit sizes; recomputation requires no numerical logarithm.

Exact minima and their prime-exponent forms:

n=5, mask=4194372, negative assignments=[2, 6, 22]; minimizing coordinates=[0, 1, 3].

    E(f) = (16/3) log2(2) + (-3/8) log2(3) + (-169/24) log2(13) + (89/24) log2(89)

n=6, mask=1103806792023, negative assignments=[0, 1, 2, 4, 6, 8, 16, 17, 32, 40]; minimizing coordinates=[0, 1, 2, 3, 4, 5].

    E(f) = (16/3) log2(2) + (-21/8) log2(3) + (95/24) log2(5) + (-121/24) log2(11) + (65/24) log2(13)


The saved minimum_comparisons compare every relevant coordinate's ratio to the selected minimum; every sign is nonnegative and exactly zero identifies the listed minimizing coordinates. The strict-cutoff products certify E(f5)>539/200 and E(f6)>368/125. Separate integer products show both E values exceed Kstar=4+(5/2)log2 5-(9/2)log2 3, and E(f6)>E(f5). Thus these are genuine counterexamples to using Kstar as a universal physical-coordinate selection constant; they do not contradict the proved four-bit leaf theorem. The JSON records include each coordinate's exact influence, B_i, JS_i, Delta_iH, ratio, physical children, and child entropies.

The first unsupported line is any extrapolation that this finite rise continues without bound in a Boolean family, or that it refutes all finite selection constants. Neither is claimed. No independent 30-digit interval reconstruction is claimed; that remains A073's directed task.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was saved before computation. Commands from A072:

    python -X utf8 runs/20261012T004036Z-account05-A072-exact-walsh-engine/code/verify.py --pilot
    python -X utf8 runs/20261012T004036Z-account05-A072-exact-walsh-engine/code/verify.py
    python -X utf8 runs/20261012T004036Z-account05-A072-exact-walsh-engine/code/finalize.py

Pilot: 16 functions, 32 coordinate checks, zero failures; 0.008000200032256544 seconds. Witness verification: 2 functions, 11 coordinates, 22 children, 2 exact minima and 11 exact entropy-decrement identities; zero failures; 2.9248420000076294 seconds. One serial job, runtime cap 55 seconds, estimated memory below 100 MB (not measured), explicit integer-product bit budget, no GPU or dimension escalation. Exact witness outputs were saved immediately as each witness completed; out/comparison.json and ENGINE_CERTIFICATE.json follow. Mathematical arithmetic is integer/Fraction only; runtime uses perf_counter. No floating entropy comparison is used.

## proof dependencies and changed downstream conclusions

No unreviewed entropy/helper theorem is a premise. The baseline FWHT/sign/edge algorithm is reused from the prior source-complete A072 interface, whose hash is pinned; its elementary Walsh orthogonality proof remains in that prior report. The truth masks are sourced to Claude B15, but all spectra, physical children, edge counts, entropy expressions and exact comparisons are independently reconstructed here. One bundled finite claim A072-UNIFORM-ERASURE-WITNESSES@1 is created, review pending. This corroborates the lead's B15-LKSTAR-FAILS-N5-N6 algebraic claim; it is not acceptance of a full census or a universal theorem. Full FEI remains OPEN. No shared registry is modified; there is no new refutation propagation beyond the already reported finite failure of Kstar universality.

## one next mathematical action and independent reviewer

Next: consume A075's parameterized sparse Hamming-ball-plus-matching formula, then certify a frozen bounded list of parameters and physical restrictions with this interface. That tests whether the rise survives heredity and identifies the exact unpaid erasure term; it avoids another exhaustive census. Reviewers A085/A092 should reconstruct the exponent products and min-coordinate comparisons. A073 can use the exact maps for its 30-digit intervals; A074 can compare its third-path conditional-entropy reconstruction without importing our spectrum as independent input.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, identical PACKET_DELTA.json with packet_ids=[A072], EXACT_WALSH_INTERFACE.py, ENGINE_CERTIFICATE.json, FROZEN_SPEC.json, code and out records are locally saved in the requested stage directory. The finalizer validates protocol field sets, delta equality and file sizes below 20 MB, and writes out/manifest.json with SHA256 receipts. Rolling STATUS.md is current; WORKLOG.md and LEARNED.md receive dated stage facts without discarding previous entries. Supervisor copying, independent review, adoption and mirror verification remain pending and are not inferred from local saving. All writes remain inside A072.

**Universal bridge:** This stage moves C018's erasure-selection diagnostics by independently certifying E(f5)>539/200, E(f6)>368/125 and E(f6)>E(f5), while making B_i, JS_i and the actual physical decrement auditable together. It changes no universal constant and supplies no unbounded-ratio family: the first unpaid obligation is a dimension-independent erasure/influence payment or a proved Boolean family violating every finite bound. A075's parameterized sparse matching family, checked through actual restrictions and retained child costs, is the shortest next route because it tests that dimension bridge directly rather than repeating a completed baseline or closing another isolated finite class.
