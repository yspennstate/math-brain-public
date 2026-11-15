# T098 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Session began 15 November 2026, approximately 08:15 Asia/Tbilisi.

## Scope and orientation

All writes stay in this folder. No git, subagents, publication, or background
workers. The specific folder-only instruction overrides the global requests
to mutate the shared brain, checklist, and mesh. Read the startup memory index,
BRAIN_INDEX, and compute_state.json. The latter reported status warn,
mode owner_away_open, CPU saturation. Only small serial checks are planned.
Commands use OMP_NUM_THREADS=1 and the other numerical thread limits,
nice -n 15, and PYTHONDONTWRITEBYTECODE=1. As in earlier rounds, nice reports
a redundant-adjustment denial; actual priority will be checked through libc.

Read earlier REPORT.md, LOG.md, PROOF.md and scripts from the original,
round-3 and round-4 folders in chunks. Those folders remain read-only.

## Literature check (08:15–08:17, within five minutes)

Used the web search tool for:

- many body localization unconditional proof one dimensional Imbrie limited level attraction 2026
- "Huveneers" "2609.39462" localization
- "many-body localization" "proof" "October" "2026"
- "many-body localization" "unconditional" "2026" proof

Opened John Z. Imbrie, On Many-Body Localization for Quantum Spin Chains,
https://arxiv.org/abs/1403.7837, and Francois Huveneers, Many-body localization:
an introduction for mathematicians,
https://arxiv.org/html/2609.39462v1#S4.SS5. Imbrie's abstract retains the
level-attraction assumption. The survey's outlook continues to discuss
the missing high-probability extension. No later unconditional solution
was found in this bounded search. This does not exclude unindexed work.

## Earlier-result audit, in progress

The main round-4 input is a local anti-Hermitian generator A_f with
[H0,A_f]=V_f on its all-state good event, norm at most
sqrt(8/3)|epsilon_f|/delta, and support I_f consisting of the two adjacent
active blocks, f, and at most two outer frozen controls. Its proof uses the
continuous multiplier f(x)=x for |x|<=1 and 1/x otherwise. Both squared
Sobolev norms are 8/3, so Fourier Cauchy–Schwarz gives sqrt(8/3).
The sign is consistent with e^A(H0+V)e^-A: [A,H0]=-V.

The exact one-barrier identity is
R=integral_0^1 t e^(tA)[A,V]e^(-tA)dt. Subtracting [A,V]/2 and
integrating once more gives ||T||<=4||A||^2||V||/3. This independently
recovers its main analytic constants. A new computational audit will
compare spectral division with an independent Sylvester solve and direct
unitary conjugation before an extension is attempted.

## Earlier-result audit completed: holds (08:19)

Created audit_previous.py. It constructs the inverse primarily by a product-
basis Sylvester linear solve, then checks it against a separate spectral
construction and direct unitary conjugation. Twelve cases, sector dimensions
1,2,4,8, cover interlaced spectra, within-sector degeneracies, and separated
spectra. All inverse, dimension-free norm, exact remainder, and dressed-spin
commutator bounds passed. Maximum inverse residual 5.04e-17; maximum spectral
comparison error 9.88e-17. Peak RSS 32,718,848 bytes, .031 seconds, nice 20.

Command:
```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_previous.py > previous_stdout.txt 2> previous_stderr.txt
```

Read both streams and previous_audit.json. stderr contains only the redundant
nice adjustment denial. Independent analytic re-derivation also recovers
the multiplier bound and cubic constants, as described above. No error in
the round-4 main claim was found.

## Choice, before doing the extension

Prove the round-4 report's proposed volume-uniform simultaneous remainder
bound, after omitting generators at bad cells and cells with physical
diameter above ell. Use an exponentially diameter-weighted per-site
interaction norm. Group each whole active block as one tensor factor, while
keeping frozen spins as singleton factors. Each A_f then meets at most five
factors and each factor meets at most three generators. This should remove
both chain length and active-block dimension from the nested-commutator
counting constants. Bad-site perturbations must remain in the identity,
including their order-two commutators with nearby retained generators.

Reason: this fills the exact gap named by round 4 without assuming control
of the new energy denominators. The target is one simultaneous first
rotation, not a second rotation or full localization. The proof will also
state the cutoff rejection probability and a consistent small-epsilon choice.

## Extension proof written (before numerical verification)

PROOF.md now gives the explicit interaction construction. On the atom lattice
each generator has at most five atoms, and each atom belongs to at most three
generator supports. In the physical-diameter-weighted per-site norm,
alpha<=3 exp(mu ell) sqrt(8/3) epsilon/delta. Set q=10 alpha.

For an onsite perturbation B of size b, the first commutator has norm at most
q b. Each subsequent commutator enlarges atom support by at most four.
The two possible locations of the norm's anchor give
||ad_A^n B||_mu<=b n! q^n. This is uniform in volume and block dimension.
The exact cancellation identity gives the nth term
ad_A^n[(n/(n+1)) V_retained+V_discarded]/n!. Its root amplitude is at most
epsilon, since retained and discarded roots are disjoint. Thus the remainder
after the quadratic term is <=epsilon q^2/(1-q) when q<1.

The cutoff failure is bounded by the earlier F_p(4 rho delta) plus the
geometric convolution tail p^(ell-1)[ell-(ell-1)p]. Taking mu=1/ell avoids
an ell factor in q. A logarithmically growing ell and delta=epsilon^beta,
0<beta<1, give a vanishing fixed-site discard probability and a uniform
O(epsilon^(3-2 beta)) remainder. This is still only one rotation.

Next verification will test interaction coefficients before summing them,
compare the whole series with direct unitary conjugation, and enumerate
all small masks to challenge the five-atom/three-incidence assertions.

## First simultaneous-rotation verification: PASS (08:25)

Created verify_simultaneous.py and ran:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify_simultaneous.py > simultaneous_stdout.txt 2> simultaneous_stderr.txt
```

Read stdout, stderr, and simultaneous_verification.json. All tests passed:
2,046 indicator masks for incidence and atom counts; one 1,001-site structural
example (five atoms); 4,572 exact rational positive path-majorant comparisons;
60 exact recurrence-product comparisons; 324 exact finite-volume cutoff
probabilities; 27 exact geometric-tail comparisons; 67 physical matrix cases
through dimension 128, each checked through eight commutator orders (536);
23 cases with no discarded perturbation; 27 mixed cases; 351 spatial-tail
checks; 20 exact integral/Taylor coefficient comparisons.

The largest local inverse residual was 4.32e-15, global homological residual
4.18e-17, uncancelled Taylor-coefficient error 5.06e-19, and unitary residual
7.21e-15. The largest discrepancy between direct conjugation and the
eight-order interaction series was 3.72e-14, within the explicit omitted-tail
bound plus floating-point tolerance. These matrices are not interval-certified.

A deliberately resonant three-site chain retains the two end generators
but discards the middle one. Its [A,V_discarded] norm is
1.8798750857549214e-5, so deleting that quadratic contribution would fail.
An oversized-block example retains only site 5 (one-based), as intended.
Atom-anchor and physical-site-anchor interaction norms matched exactly.
Maximum q=.2500000000000001. Runtime .577 seconds, peak RSS 41,762,816 bytes,
actual nice 20. stderr contains only the redundant nice adjustment denial;
all five thread limits are one and no numerical warning occurred.

## Attempt to break the proof, ongoing

Checked empty active blocks, no frozen sites, physical boundaries, duplicate
generator supports, repeated generators, shared frozen controls, active
spectators beyond controls, and cells omitted for size rather than resonance.
The cutoff-tail exponent is ell-1, not ell: two outer controls add two to
physical diameter, so diameter>ell implies A+B>=ell-1. Its tail was checked
by exact finite mask enumeration and independent collapsed geometric sums.

The first commutator must use its special onsite-root bound, rather than
applying the general two-anchor inequality from order zero; otherwise the
claimed n! constant would not follow as written. The proof explicitly does
this. The global Hamiltonian norm never enters because [A,H0]=-V_retained
is used before estimating. No independence between retained events is used.
The mixed-root coefficient is controlled by epsilon (not 2 epsilon) because
retained and discarded root sets are disjoint.

## Second derivation and final verification

Derived the remainder a second way, by unitary differentiation and Taylor's
integral remainder, rather than collecting exponential-series coefficients:

T=integral_0^1 exp(u ad_A) ad_A^2 [((1-u^2)/2)V_retained
                                     +(1-u)V_discarded] du.

The root amplitude is <=(1-u)epsilon. The factorial estimate gives an
evolution bound 2(1-u)epsilon q^2/(1-uq)^3. Differentiating
(1-u)^2/(1-uq)^2 evaluates its integral exactly as
epsilon q^2/(1-q). This independently recovers the mixed-root coefficient
and denominator. Added the full derivation to PROOF.md, three direct matrix
quadrature checks (all-retained, resonant, oversized), and five scalar
quadrature checks, including q=0 and q=.9, to the script.

Reran the identical simultaneous command. PASS. All earlier counts and
residuals persisted. New matrix-integral error <=1.04e-14; scalar integral
error <=5.33e-15. Final runtime .598 seconds, peak RSS 42,663,936 bytes,
nice 20, all thread variables one. Read both streams and final JSON.
No numerical run failed. No warnings other than the redundant nice message.

Scope audit: the support-count bound is in atoms, while the exponential
weight uses physical diameter; the two are never interchanged. A long
active atom may have large Hilbert-space dimension but still counts once.
Assigned supports are unions of entire atoms, so the anchor maximum in
the interaction norm really is a maximum over physical sites as well.
The smallness condition is q<1; finite-volume exponential convergence alone
would not give this local bound. No conclusion about subsequent denominators
or exact conserved l-bits is inferred. There is no unresolved doubt in the
elementary inequalities; the numerical checks are floating-point, not intervals.

## Final report and artifact audit

Wrote REPORT.md with the required PARTIAL verdict, the exact norm and
smallness condition, proof constants, reproduction commands, accepted output,
limitations, and a concrete next step concerning connected discarded cells.
Read back the proof's integral and remainder sections. Corrected a sentence
capitalization after removing a nonsequential equation label; no assertion
or computation changed.

Ran a short read-only Python heredoc under the same numerical thread limits
and nice -n 15. It parsed both scripts, compared both stdout objects against
their JSON (the extension stdout is the documented summary), independently
recounted 2,046 masks, 4,572 path checks, 536 matrix-order checks and 324 cutoff
checks, and verified the report's verdict, resource figures, required files,
and both stderr streams. Output:

`Artifact audit: PASS. Scripts parse; both saved outputs match JSON; counts,
verdict, constants, resources, and stderr agree.`

The final mathematical result is one exact simultaneous first rotation with
a volume-uniform local remainder. No proof of the full T098 conjecture, an
LLA estimate, or a second rotation is claimed. All writes stayed here.

Task: “take the NEXT checkable step on this problem, building on that work.”
15 November 2026, approximately 08:15 Asia/Tbilisi.
