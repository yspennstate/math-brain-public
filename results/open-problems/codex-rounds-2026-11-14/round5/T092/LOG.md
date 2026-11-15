# T092 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Started 2026-11-15 approximately 08:13 +04 (Asia/Tbilisi); first explicit
clock read: 08:15:03 +0400.

## Scope and initial reading

All writes stay in this folder. The task-specific scope excludes global brain,
checklist and mesh mutations; no subagents, git, external writes or build.
Read the original REPORT.md, LOG.md and SOLVED_ELSEWHERE.md, the round 3
REPORT.md, LOG.md, PROOF.md and CLAIM_AUDIT.md, and the round 4 REPORT.md,
LOG.md and PROOF.md. Directory discovery confirms no prior computation scripts;
the original directory has no PROOF.md.

Shell reads use `env OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c '...'`.
The sandbox reports `nice: setpriority: Operation not permitted` but performs
the tiny reads. No substantive computation will run without the required priority.
Compute state: status ok, mode owner_away_open, 100% CPU; no heavy work planned.

## Bounded literature check

Web searches: `"Banach" "simple Lebesgue" "2026" probability` and
`"A smooth three-torus diffeomorphism with simple Lebesgue spectrum"`.
Opened https://arxiv.org/abs/2210.15480 and the OpenAI preprint's primary README:
https://raw.githubusercontent.com/openai/math/main/preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/README.md
The same September 23, 2026 OpenAI claim is present. No newly verified resolution
was established. End general status searching here, within five minutes.
Further source opens are the mathematical audit only.

## Earlier result, independent check in progress

For each phase density, E[Z]=lambda a and Var(Z)=1-lambda^2|a|^2,
so the block predictor is unbiased and its exact variance is
1/(n lambda^2)-|a|^2/n. For the mixture, directly integrate H_r H_u:
E[H_r H_u]=(1+2 lambda^2 Re(a_r conjugate(a_u)))^n.
The first nonconstant binomial term is 2s|beta-q|^2. The tail is bounded
by 2s^2 v^2/(1-18s), where v=sum t_r|a_r|^2<=1+|beta-q|^2.
This independently reproduces the load-bearing identities in round 4.
The remaining constant and transfer checks will be recorded explicitly.

Completed the earlier-result check: write I=int sqrt(p)<=sqrt(2)<3/2 and
J=int sqrt(p)|beta-q|^2<=delta. The exact square-root identity gives loss
at most sJ+s^2(I+11J)/(1-18s). At s<=delta<=1/100 this is at most
delta^2[1+(50/41)(161/100)]=(243/82)delta^2<3delta^2.
Second arithmetic check: 3-(243/82)=3/82>0; alternatively the bound below
3 reduces to I+47delta<2, and 3/2+47/100=197/100<2.
The predictor increase is <=2/s<=4/delta. For diagonal transfer, the
polynomial lower bound Q(R)<=sqrt(R) and finite Fourier averaging suffice;
the final L1 perturbation costs sqrt(e) for the root integral and W e
for the bounded prediction weight. The tolerance in round 4 makes each
cost at most nu/2. No flaw found; its claim holds under its hypotheses.

## Chosen extension, before the work

Audit the geometric producer behind `exists_refresh_transmit_reflected_state`,
beginning with residue equidistribution and transport of spectral densities,
as round 4 requests. Aim for one self-contained verified lemma, or a concrete
counterexample to a stated intermediate claim. Opened ControlledBlocks.lean;
its controlled realization calls the named geometric producer. A guessed
`03-passages.tex` URL failed (cache miss); obtain the actual file names next.

## Geometric source reached

Opened `build/main.tex`, which names `02-passages.tex` and `03-signals.tex`,
then opened both through the web tool. Sources are OpenAI, *A smooth
three-torus diffeomorphism with simple Lebesgue spectrum*, September 23,
2026; all source URLs use mutable main. The passage calculation transports
coefficient masses to a lattice-sampled density; residue equalization is
the next local lemma. Read startup MEMORY.md directly; a relevant verified
memory explains that stacked relative nice can itself report permission
errors at a very low inherited priority. No compute was launched on that
basis, and no global recall command (which logs outside this folder) ran.

Primary sources opened:
- https://raw.githubusercontent.com/openai/math/main/lean/OAI/Dynamics/ThreeTorus/ControlledBlocks.lean
- https://raw.githubusercontent.com/openai/math/main/preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/build/main.tex
- https://raw.githubusercontent.com/openai/math/main/preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/build/sections/02-passages.tex
- https://raw.githubusercontent.com/openai/math/main/preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/build/sections/03-signals.tex

## Precise extension selected before proving it

Prove a finite, quantitative weighted residue-transport theorem. The input
is any nonnegative coefficient array, not an assumed stationary-phase
expansion. Bound the sum of ALL residue-density errors by four explicit
terms: coefficient-array L1 discrepancy, freezing the slow lattice
argument, broad-jitter quadrature, and removed cutoff mass. This will
separate exactly what residue equalization proves from what still needs
an oscillatory-integral estimate. It extends the round 4 transfer analysis
toward the physical producer rather than changing the block estimate again.

The linear jitter is J(a)=L a+beta on the coefficient support. Its residue
periodization is a shifted quadrature rule of mesh P/(|s|L). A centered
cell proof suggests the constant 1/2, improving the coefficient 1 in the
opened neutral-refresh calculation. Prove this factor by two methods and
test sharpness. Also keep the total freezing error independent of P by
summing the disjoint residue classes before estimating. No condition such
as P dividing N should be needed; verify negative s, h offsets, and N=1.

Scope fixed: certify the residue-density step with an explicit coefficient
discrepancy. Do not claim a full stationary-phase audit, a transmission
construction, or an existence theorem for simple Lebesgue spectrum.

## Quantitative proof saved

Wrote PROOF.md. For target weight W and cutoff f=W psi^2, the sum of
the P folded residue errors is bounded by

    E_N + (B-A) J_1/N + J_2/N^2 + P H/(2L) + C_cut.

Here E_N is the summed L1 discrepancy of the actual coefficient intensities
from N^-1 f(j/N,a); H=int |s|^-1 int |partial_a f|; C_cut is the removed
weight mass. For the compact kernel K(s,y)=f(s,(y/s-beta)/L)/(|s|L),
J_1=int |y| sup_s|partial_s K| and
J_2=int (2 y^2+|y|) sup_s|partial_s K|. The freeze error sums all indices
first, so it has no factor P. This is a finite-N inequality, with no
divisibility assumption on N and P. Signed angular indices are allowed.

The quadrature bound is Delta/2 times the L1 derivative norm, proved
by centered cells and independently by a bounded sawtooth primitive.
Narrow smooth unimodal bumps prove optimality of this local coefficient.
This improves the neutral-refresh calculation's derivative bound by a
factor of two; no historical novelty is claimed for that inequality.

Also proved an explicit upper bound on E_N in terms of the complex-array
L2 discrepancy eta_N and the rounding shift d_N. Parseval supplies the
exact coefficient mass; a second quadrature application bounds the leading
array mass by M+U/(2N). Rounding removal is bounded by
|d_N|(B-A+2|d_N|+1/N) Omega. Thus eta_N->0 is sufficient to make E_N->0.
It remains a separate oscillatory-integral assertion, not a consequence
of this transport estimate. This prevents the conditional theorem from
being mistaken for a certificate of the full geometric producer.

## Attempts to break the bound

1. Re-derived the Jacobian by mass integration: int K(j/N,Nt-j) dt
   equals N^-1 int f(j/N,a) da, including negative j. This checks both
   factors of N and the absolute value around s.
2. Re-derived the residue normalization by integrating a length-P
   periodization over one period. Its integral is int f(t,a) da, so
   its mean is that mass divided by P. There is no hidden normalized
   Haar factor and no requirement that P divide N.
3. Verified the slow-argument estimate termwise after y=Nt-j. The
   possible j lie in [NA-|y|,NB+|y|], with at most N(B-A)+2|y|+1
   integers. Multiplication by |y|/N and the Jacobian 1/N reproduces
   both terms D_N. An independent rough check uses |y|<=Y, at most
   2Y+1 contributing indices at a fixed t, and a t interval of length
   at most B-A+2Y/N; this also gives order 1/N, without a factor P.
4. Checked the j=0 edge: the sampled model has zero mass there. Freezing
   can introduce a j=0 summand at small N, but it is already included
   in the all-index difference estimate. No asymptotic argument is
   used to discard it in the finite-N theorem.
5. Proved the quadrature coefficient by two independent arguments and
   tested its optimality on smooth narrow bumps. A piecewise linear
   tent with mesh 1 and half-width 1/4 has area 1/4, derivative variation
   2, and quadrature error 3/4: the proposed half-variation bound is 1,
   while a quarter-variation bound of 1/2 would fail. The smooth-bump
   argument in PROOF.md supplies the exact limiting sharpness claim.
6. Checked zero weights, psi=0, large missing mass, negative shifts,
   N=1, and finite sums of packets. Removed mass is charged once,
   rather than P times. Rounding is removed before the fast variable
   is sampled, so no O(1) fast-phase translation is hidden.
7. Checked the coefficient bound twice: the factor (sqrt(M)+sqrt(B_N))
   is the norm inequality for squared moduli; the lattice mass B_N
   also follows directly by applying the centered quadrature bound
   to M(s) at offset -d_N. The shift-counting bound remains valid
   with either sign of d_N. At fixed L all kernel moments are finite;
   no uniform bound over later choices of L is asserted.

No counterexample to the stated result was found. In particular, a small
coefficient discrepancy remains a hypothesis or a separately proved
input. The theorem alone does not imply it.

## Commands and artifact checks

Read-only shell commands used `cat`, `rg --files`, `sed`, `date`, and an
unsuccessful `ps` priority read, always within a small read-only shell.
Subsequent prefix: `env OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c '...'`.
The sandbox printed `nice: setpriority: Operation not permitted`; `ps`
was denied too. No numerical program, Lean build, network shell command,
or git command ran. File writes used apply_patch. No scripts were needed:
all quantitative checks are exact inequalities in PROOF.md and this log.

Clock checks: 2026-11-15 08:16:20 +0400 and 08:20:10 +0400. Read back the
proof's first 240 lines with sed; remaining proof and report will receive
the final saved-file check. Original reports and sources were never edited.

Final saved-file check at 2026-11-15 08:21:31 +0400: read the rest of
PROOF.md and all of REPORT.md. Counts before this final entry: LOG.md
186 lines, PROOF.md 368 lines, REPORT.md 67 lines. The report's first
line has the required `VERDICT: PROVED` prefix. Corrected an absolute-value
delimiter in the coefficient comparison for readability; its inequality
and constants are unchanged. The result and its conditional scope agree
between the proof, report, and log. All deliverables are in this folder.
