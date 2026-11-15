# T098 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Started 15 November 2026, approximately 10:50 Asia/Tbilisi.

All writes stay in this folder. The original and rounds 3–5 are read-only.
No git, subagents, external messages, background workers, or shared-memory,
checklist, or mesh mutations: the task-specific folder-only rule overrides
the global requests for those writes. Read the startup memory and compute
state directly. State: ok, owner_away_open. Only small serial calculations
are needed; numerical runs use nice -n 15 and five thread limits set to one.

## Literature check, within the first five minutes

Used the web search tool for `many body localization unconditional proof
Imbrie 2026 limited level attraction` and `Huveneers 2609.39462 many body
localization`. Opened John Z. Imbrie, *On Many-Body Localization for Quantum
Spin Chains*, https://arxiv.org/abs/1403.7837, and Francois Huveneers,
*Many-body localization: an introduction for mathematicians*,
https://arxiv.org/html/2609.39462v1#S4.SS5. The former retains its
level-attraction assumption; the latter discusses the outstanding
high-probability extension. No newer unconditional solution was found.
This bounded search does not exclude unindexed work.

Read the earlier REPORT.md, LOG.md, PROOF.md and Python scripts in chunks.
Read commands: rg --files, wc -l, cat, sed. The old script's spectator-index
correction and the warning about omitting [A,V_D] were checked.

## Independent analytic recheck of round 5: holds

Regrouping each active run as an atom gives at most five atoms per generator
and at most three generators at each atom. If alpha is the weighted local
generator norm, the first commutator against an onsite interaction of size b
is at most 10 alpha b. After n commutators a support has at most 1+4n atoms;
the next commutator costs at most 2 alpha(6+4n), bounded by
10 alpha(n+1) for n>=1. Thus ||ad_A^n B|| <= b n! q^n, q=10 alpha.

Independently subtract the H0 conjugation integral from the V conjugation:
the retained-root coefficient at order n is 1/n!-1/(n+1)!, while the
discarded-root coefficient is 1/n!. Since their roots are disjoint, their
combined onsite bound is epsilon. Summing n>=2 gives epsilon q^2/(1-q).
The quadratic discarded term remains [A,V_D]. The geometric cutoff tail
follows from P(a+b=k)=(k+1)(1-p)^2 p^k and is
p^(ell-1)[ell-(ell-1)p]. No error found in the main round-5 estimate.
A local copy of its computational check will be rerun before extension.

The rerun completed at 10:53. Copied verify_simultaneous.py byte-for-byte
from round 5 to audit_round5.py here; it writes only beside its local copy.
Command:
```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_round5.py > round5_stdout.txt 2> round5_stderr.txt
```
Output: PASS; 2,046 structural masks, 4,572 rational path checks, 60 recurrence
checks, 324 finite cutoff probabilities, 27 geometric tails, 67 matrix cases
through dimension 128 and eight orders, three matrix-integral checks. Largest
direct-conjugation/series difference 3.713e-14. RSS 50,446,336 bytes, .6304 s,
nice 20. The only stderr is the redundant nice-adjustment denial. Read back
both streams. The main round-5 result holds in both audits.

## Choice, recorded before extension

Prove a volume-uniform exponential size tail for the physical nearest-neighbor
components obtained by joining active sites through discarded frozen sites.
Keep only components containing a discarded frozen site as exceptional blocks;
the full discarded cell is contained in such a block plus its outer frozen
controls. This includes oversized cells, with no cap on their actual size.

The useful extra observation is that all-state first-flip resonance at f
does not depend on any *other frozen longitudinal field*: those fields are
scalars that cancel, and outer frozen spins are tested over every assignment.
After conditioning on the indicators, all active fields, and g,J, the bad
events at frozen sites are independent functions of their own h_f. Combine
their conditional bounds with a fractional geometric moment; every active
site can enter at most two adjacent cell counts. This should give a size
exponent that stays positive as the cutoff grows, unlike a direct coloring
argument whose dependence range grows with ell. No claim about new energy
denominators or a second rotation will be made.

## Extension proof written

PROOF.md gives tails for the actual union E of full discarded cells I_f,
with physical nearest-neighbor connectivity, so shared controls and touching
collars are merged. The smaller core union B is analyzed separately.

For the cores, conditional independence gives d_f<=u 4^(s m_f), where
u=max(t^s,4^(-s(ell-1))), t=4 rho delta. Every internal active site enters
at most two m_f counts, and external runs enter once. Thus
P(J subset B)<=M^2 lambda^|J|, with M=(1-p)/(1-p4^s) and
lambda=p16^s+(1-p)u. The full union cannot simply inherit this bound:
two distinct cores can merge through a shared retained control.

To handle that merger exactly, a five-consecutive-frozen-site pattern with
its middle three retained leaves its center outside every discarded cell.
Each middle cell has m=0 and diameter 2, so this separator has probability
at least sigma=(1-p)^5(1-t)^3 for t<1, independently across disjoint
five-site windows conditional on g,J. Consequently
P(J subset E)<=(1-sigma)^floor(|J|/5). A union over at most n length-n
intervals containing x gives P(|E_x|>=n)<=n(1-sigma)^floor(n/5).
No cutoff is imposed on the discarded cells in this argument.

Rarity is separate from the size estimate: a selected occupied component
contains a discarded frozen site. Either one lies within distance r of x,
or there is an active run of length r. Hence P(x in B)<=
(2r+1)(1-p)b+2p^r and P(x in E)<=3 times this quantity, capped at one.
For b->0 this is O_p(b[1+log(1/b)]); the separator size exponent remains
positive as ell grows. The result is still one first-step rare-block lemma.

Next: exact enumeration of a conditionally independent marking majorant,
geometry with merged collars and oversized cells, the fractional moment
constants, and a direct field-based test of conditional independence.
One attempted log-only patch failed to match context and changed nothing;
this replacement patch records the completed proof.

## First cluster audit: PASS (11:00)

Created verify_clusters.py, using exact fractions for all probability
enumerations. It tests an independent-discard majorant conditional on the
indicator pattern; this dominates the actual conditional probabilities by
(10), and is not a simulation of the interacting chain. Command:
```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify_clusters.py > cluster_stdout.txt 2> cluster_stderr.txt
```
Read both streams and cluster_verification.json. Output PASS:
29,523 ternary geometry cases through 9 sites; 2,188 separator checks;
14,846 incidence/interval checks; 13,842 conditional majorant checks;
1,512 exact core interval bounds; 38,352 marking configurations through
7 sites; 1,512 full-cell interval bounds; 2,520 full-cell cluster bounds;
4,032 rarity bounds; 126 no-separator bounds; three actual-field separator
integrations over 1,099 rational boxes; 48 disjoint-window checks; 45 scalar
checks of exponential conversion. The merger fixture has two singleton
cores but one full-cell block of length five, so silently ignoring shared
controls would miss a real case.

Peak RSS 18,022,400 bytes, elapsed 1.4716 s, actual nice 20, all five
thread limits one. stderr contains only the inherited nice-adjustment
denial. No mathematical or numerical check failed. Parameter illustrations
with lambda<1 include p=1/2, 4^s=5/4, ell=16, t=4^-16, giving
M=4/3 and lambda=780119322309/976562500000 (about .7988421860).
At p=.9 the constants can be much weaker: ell=64, 4^s=21/20,
t=4^-64 give lambda about .9968745998. These are exact bound parameters,
not measured physical decay lengths.

Audit continues: check the conditional-independence observation directly
against full interacting small Hamiltonians with nonzero active transverse
fields, and rederive the separator constants by a second calculation.

## Independent conditioning audit and attempts to break the proof

Created audit_conditioning.py without importing an earlier script. It builds
full bit-basis Hamiltonians, restricts every frozen-spin sector, and evaluates
their energies in tensor products of conditional active-block eigenvectors.
It compares transition multisets with separately diagonalized local cells,
then changes every frozen field and checks that only the central 2 h_f
contribution changes. Cases include a two-spin active block, active spectators
sharing outer controls, adjacent frozen sites, and no active sites.
Command:
```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_conditioning.py > conditioning_stdout.txt 2> conditioning_stderr.txt
```
Output PASS: 64 full-Hamiltonian sectors, 232 frozen-scalar checks,
108 transition-multiset comparisons, four masks, largest dimension 128.
Maximum local/full transition error 9.77e-15; maximum cancellation error
8.88e-15. Local offsets were exactly unchanged on resampling frozen fields.
Peak RSS 32,227,328 bytes, .0254 s, nice 20, all thread limits one.
Read both streams; stderr contains only the known nice message. These
floating-point checks audit the algebra; they are not certified intervals.

The separator probability was rederived by direct rational integration of
three actual uniform-field resonance unions, including shared unequal bonds,
coincident offsets and zero bonds. Cartesian box integration agrees exactly
with the product of the three retention probabilities and bounds it below
by (1-t)^3. This checks the constants 4, 3 and the slope-two interval length
without using products of the upper bounds as numerical data.

The incidence audit attains multiplicity two for an internal active site;
using p4^s instead of p16^s in lambda would discard a real multiplicity.
External active sites enter at most once. Missing physical controls reduce
diameter, and the oversize implication is m>=ell-1, not m>=ell. The exact
finite checks cover both effects. Every oversized cell is marked with
probability one in the majorant, so no size event is dropped from the audit.

The full-cell bound cannot be obtained by merely padding a single core:
padding merges different cores. This is why (4) uses separators directly
for the full union E; (9) is stated separately for B. The separator events
are independent only after conditioning on g,J; no unconditional independence
of adjacent bad cells is asserted. The proof uses nearest-neighbor physical
connectivity, including cells which only touch.

Checked b->0 independently by dominated convergence of its capped series
and the explicit geometric tail. Choosing r=ceil(log(1/b)/log(1/p)) gives
p^r<=b and density O_p(b[1+log(1/b)]). The full-cell rate has the separate
uniform bound kappa<=1-(1-p)^5/8 once t<=1/2. Its polynomial prefactor is
absorbed via max_y y exp(-a y/2)=2/(a e), verified at 45 scalar cases.

Simplified an unused import and the disjoint-window summation in
verify_clusters.py, then reran its identical command. PASS with all counts
unchanged; accepted final RSS 17,170,432 bytes and 1.3569 s. The previous
PASS numbers above describe its first run. There were no failed runs.

No proof inequality failed. The direct dependence-range coloring route was
not used: it would lose the size rate as ell grows. The conditional-field
and separator arguments avoid that loss. Their constants remain weak near
p=1, and no optimization or literature novelty is claimed.

## Final report and artifact audit (11:06 Asia/Tbilisi)

Wrote REPORT.md with the required PARTIAL verdict, the full merged-cell
theorem, sharper core estimate, commands and accepted output, limitations,
opened-paper links, and the next concrete task. Re-read the probability
conditioning, separator geometry, external-run counting, density argument,
and small-perturbation quantifiers. Removed an ambiguous use of the letter J
in a conditional probability by spelling out the conditioned coefficient
array. No assertion changed.

Ran a short read-only artifact audit using
`env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
nice -n 15 python3 - <<'PY'` (Python heredoc). It parsed all three scripts,
compared the copied round-5 script's SHA256 against its original, compared
all accepted stdout objects with their JSON files, checked every stderr,
thread and resource figure, independently recounted the ternary cases and
interval/rarity/tail checks from their elementary sums, and verified required
files and the exact report verdict. Output:

`Artifact audit: PASS. Scripts parse; copied audit is byte-identical; JSON
matches accepted stdout; counts, resources, stderr, and verdict agree.`

The only stderr was the already documented nice-adjustment denial.
The shell clock read `2026-11-15 11:06:19 +04`. All writes stayed here.

Next worker: diagonalize H0+V_D in its occupied components with retained
frozen-spin controls, then prove spatial bounds for the conjugated Q,T and
identify which transition gaps retain an independent field. Same-barrier
quadratic terms can still mix active labels across a retained frozen control;
they cannot be assumed diagonal. The present result controls static first
discarded blocks and does not establish their stability under that operation.

Task: “take the NEXT checkable step on this problem, building on that work.”
15 November 2026, approximately 10:50 Asia/Tbilisi.
