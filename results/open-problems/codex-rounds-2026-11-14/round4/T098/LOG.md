# T098 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Started 15 November 2026, approximately 04:50 Asia/Tbilisi.

All new files stay here. The two earlier folders are read-only. No git,
subagents, external messages, or shared-brain/mesh/checklist mutations. The
specific folder-only instruction overrides the global shared-state duties.
Read the startup memory index and compute governor state directly. Governor:
warn, owner_away_open, CPU saturation. Only small serial checks are planned.
All Python runs use one numerical thread, nice -n 15, and short time limits.

## Literature check, completed within five minutes

Used the web search tool for “many body localization unconditional proof
random spin chain 2026 limited level attraction Imbrie”, “Huveneers
2609.39462 many-body localization introduction mathematicians”, and November
2026/unconditional-proof variants. Opened John Z. Imbrie, *On Many-Body
Localization for Quantum Spin Chains*, https://arxiv.org/abs/1403.7837,
and Francois Huveneers, *Many-body localization: an introduction for
mathematicians*, https://arxiv.org/html/2609.39462v1. Imbrie's abstract retains
the level-attraction assumption. The survey's mathematical discussion does
not give the unconditional high-probability full-spectrum result. No newer
solution was found in the bounded search; this cannot exclude unindexed work.

Read both earlier REPORT.md, LOG.md, PROOF.md, and all three Python scripts.
Read-only shell commands used cat, sed, rg, wc, date, pwd, and ls. The prior
matrix-script warning and indexing corrections are understood; new checks
will use explicit einsum products and independent bit-based assembly.

## Independent analytic recheck of the earlier result: holds

In a frozen-spin sector H0 is a sum of disjoint active-block matrices and
frozen scalars. Controlled diagonalizers commute on shared diagonal controls.
Only the two adjacent blocks change when f flips. In each outer assignment,
their combined dimension is d=2^m, so there are d^2 forward differences;
the reverse differences are their negatives. There are at most four outer
assignments. Each denominator is 2 h_f+c with c independent of h_f. The
resonance interval in h_f has length delta, giving the factor 4 rho delta 4^m.

The independent left and right geometric runs have convolution
(k+1)(1-p)^2 p^k. Splitting at K=floor(log_4(1/t)) gives the earlier finite
sum and tail p^(K+1)[(K+2)-(K+1)p]. Finite ends truncate both runs. The
earlier capped estimate and its three asymptotic regimes therefore hold.
The exact-barrier support argument also holds: crossing radius r requires
r consecutive active indicators on that side; inclusion-exclusion gives
2p^r-p^(2r), with the stated boundary restrictions.

## Choice, recorded before extension

Construct the first Schrieffer–Wolff rotation at a good frozen barrier, with
an operator-norm bound independent of the adjacent blocks' Hilbert-space
dimension. Combine it with the earlier probability and support bounds.
Give an exact local remainder bound and identify the order-two terms when
several barriers are perturbed. This directly addresses the next step named
in the round-3 report. It is one rotation, not an iteration or an MBL proof.

The entrywise denominator bound alone would lose a factor depending on
dimension when converted to operator norm. Instead use a Fourier multiplier
that equals 1/x outside the excluded gap and has integrable Fourier transform.
The proof must justify this multiplier and its constant without assuming
ordered or noninterlacing spectra. Small matrices and exact rational sums
will independently audit the earlier result and the new identities.

## Proof and verification script written

Wrote PROOF.md and verify_rotation.py. The inverse-commutator multiplier is
f(x)=x for |x|<=1 and 1/x outside. Both its squared L2 norm and that of its
weak derivative equal 8/3. Plancherel and weighted Cauchy--Schwarz give an
L1 Fourier norm at most sqrt(8/3); rescaling gives C_*/delta. This provides
a dimension-independent local generator even for interlaced sector spectra.

Re-derived the exact remainder by integration of unitary conjugation:
R=integral_0^1 t exp(tA)[A,V]exp(-tA) dt. Thus ||R||<=||A||||V||,
and after subtracting [A,V]/2 the remainder is at most
(4/3)||A||^2||V||. Since [A,V] preserves Z_f, the dressed frozen spin
has commutator bounded by (8/3)||A||^2||V|| for a single perturbed barrier.

The simultaneous finite-volume coefficient includes [A,V_bad] as well as
[A,V_good]/2. Pair terms vanish beyond consecutive frozen sites. A same-site
two-flip term can mix active labels without any unused h_f in its endpoint
gap. Two-distinct-site bare endpoint gaps remain affine in h_f,h_g, but
diagonal corrections already make renormalized energies nonlinear.

The script uses independent bit-based full Hamiltonians, local spectral
inverses compared with direct Sylvester linear solves, exact rational capped
sums and finite-mask probabilities, unitary conjugations, and a spectral
two-step path sum. It checks interlaced spectra, within-sector degeneracy,
large rotations, spectators, pair parity, and an explicit same-site
off-diagonal order-two example. No old script is executed in its old folder.

## First independent verification: PASS

Command:
```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify_rotation.py > rotation_stdout.txt 2> rotation_stderr.txt
```

Read back stdout and stderr. PASS: 84 exact capped-sum checks, 63 exact
finite-volume checks, 129 physical barrier cases, 313 local control sectors
including the added examples, 72 consecutive and 39 nonconsecutive pair
checks, 15 generic interlacing/degeneracy cases, a seven-site spectator
test, and three large/small one-spin rotations. The largest inverse-equation
residual was 8.49e-13; the spectral two-path formula residual was 1.31e-18.
All nonconsecutive pair terms vanished exactly in this arithmetic.

The same-barrier order-two active off-diagonal norm was
6.490601756172087e-5 in the explicit three-site fixture. The centered Taylor
errors at t=.04,.02 were 8.04e-10 and 1.93e-10, decreasing by about four.
The bad-site coefficient error was 5.51e-11. Peak RSS 37,732,352 bytes;
elapsed .4265 seconds; actual nice value 20. All five numerical thread
variables were one. stderr contained only the inherited-priority adjustment
denial `nice: setpriority: Operation not permitted`; the script independently
confirmed nice 20 with libc before numerical work. No floating-point warnings.

Corrected a stray plus sign joining two prose lines in PROOF.md and changed
“gap” to “signed sector-energy difference” in its one-spin example, since
h may be negative. No mathematical assertion was changed.

## Attempt to break the result and second derivation of constants

Rechecked the Fourier normalization, the weak derivative at +/-1, the
rescaling by delta, direct-sum versus summed norms, empty blocks, missing
controls, spectator bonds, and reversed signs of h. No dimension factor or
spectral-order assumption is hidden in the integral estimate.

For H0=Z, V=2aX, direct multiplication by the real rotation matrix gives
R_Z=cos(2a)-1+2a sin(2a) and R_X=2a cos(2a)-sin(2a). The latter is
-(8/3)a^3+O(a^5). Since ||A||=a and ||V||=2a, this independently recovers
the factors 4/3 in the cubic remainder and 8/3 in the dressed-spin commutator;
the ratios approach those constants. Added this derivation to PROOF.md and
two trigonometric checks to the script. These constants are sharp when
expressed using the actual generator norm; no optimality is asserted for
the multiplier bound C_*.

The scope audit found a limitation worth preserving: the cubic dressed-spin
commutator applies to one perturbed barrier. Other perturbed sites add pair
terms at order two, so the single-barrier estimate cannot be applied to the
whole perturbed chain unchanged. Equation (14) includes bad-site terms and
explicitly makes only a finite-volume Taylor assertion for the global sum.

## Final numerical run and report

Reran the same command after adding the independent trigonometric checks.
PASS. Counts and earlier residuals unchanged. The two scalar ratios were:

```text
a=.01:  ||T||/(a^2 epsilon)=1.3333175000691253
        ||comm||/(a^2 epsilon)=2.6665600015227104
a=.005: ||T||/(a^2 epsilon)=1.3333293750106594
        ||comm||/(a^2 epsilon)=2.6666400001068564
```

The direct trigonometric remainder and independently exponentiated matrix
agreed within 4.89e-16. Final peak RSS 39,141,376 bytes; elapsed .4209
seconds; nice 20. Read back both streams and JSON. stderr remains only the
redundant nice adjustment denial. No failed numerical runs occurred.

Wrote REPORT.md with verdict PARTIAL, exact assumptions and constants, the
command and output, limitations, opened-paper links, and a concrete next
step: truncate cell diameters and control the simultaneous higher-order
remainder in a per-site interaction norm. Re-read the proof's remainder
and order-two sections. Clarified that its radius statement concerns local
generators, remainders and dressed spins, rather than the global H0.

No proof of a second rotation, an LLA bound, or the original full-spectrum
stability statement is claimed. No uncertainty in the elementary analytic
inequalities was identified; numerical audits are not interval-certified,
and the bounded literature search can miss unindexed work.

Final artifact audit ran as a read-only Python heredoc under the same thread
environment and nice -n 15. It parsed the verification script, compared JSON
with stdout exactly, checked the report's exact verdict line, checked every
required file and its size, checked all reported counts and resource limits,
and verified stderr contains only the known priority message. Output:
`Artifact audit: PASS. Required files present; Python parses; JSON equals
stdout; counts, resources, verdict, and stderr agree.`
