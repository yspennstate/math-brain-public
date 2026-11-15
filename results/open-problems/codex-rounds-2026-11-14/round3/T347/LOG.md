# T347 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Start: 15 November 2026, 03:50 +04.

## Orientation and earlier files

Read the earlier REPORT.md, LOG.md, and SOLVED_ELSEWHERE.md in
`~/codex_op_1114/briefs/T347` without editing them.
Directory listing and `rg --files` confirm that the earlier folder has no
PROOF.md or mathematical scripts. Its contribution was a literature/scope
audit, not a new mathematical result.

Read the startup memory and compute_state.json. The governor reports
`warn`, `owner_away_open`, and CPU saturation. Computations will be small,
single-threaded, below 1 GB and under 20 minutes. No agents or git.
The session instruction that all writes stay here takes precedence over
global mesh/checklist/brain commands that would write elsewhere. Those
registrations and logging recall commands are therefore not run.

Commands: `pwd`; `rg --files` on this and the earlier folder; `cat` on
the earlier files, startup memory and compute state; `ls -la`; `date`.

## Bounded update check (started 03:50 +04)

Web searches: “Hopfield capacity 0.138 2026 rigorous strict merging
inequality”; “Hopfield Bernoulli variational free energy 2026 retrieval
proof”. Opened arXiv:2611.03306 abstract and v1 HTML, and Hexagon
2611.00105v1 landing page. Both still show v1 only. Direct PDF opening
failed; following its landing-page link is the next read.
No newer solution was located in these searches. The existing capacity
claim explicitly uses wells of a fixed-overlap thermodynamic profile.
This is not yet the requested iff statement about individual local minima.

## Recheck and choice (03:54 +04)

The update check is finished, within five minutes. Following the PDF link
worked. Read the capacity paper's definitions, Section 6 merging statements,
and its zero-temperature Theorem 6.9. These do not state an exclusion of
individual local minima when the profile has no well. The earlier report's
scope conclusion holds. Its assertion that a substantial advance alone
required stopping was broader than this session's stop rule, which requires
a solution of the problem. No such solution has been established here.

Independent normalization check: Gaussian integration of
`exp(sqrt(beta/N) z dot X^T sigma)` gives
`exp(beta |X^T sigma|^2/(2N))`. Averaging spins uniformly instead of summing
subtracts exactly log(2) from pressure per spin. The all-load variational
formula in arXiv:2611.03306, Theorem 1.1 and Corollary 1.5, minimizes over
arbitrary overlap laws. It is not a theorem that the minimizer is a point
mass throughout retrieval. The paper's replica-symmetry discussion confirms
this distinction. Thus the main earlier claim survives an independent
derivation and direct theorem check. No earlier computation exists to rerun.

ONE selected extension: make the relation between fixed-overlap profile
wells and single-spin local minima precise. Prove a finite-N barrier lemma,
including the exact zero-diagonal stability convention, and test the
converse within the class of binary-pattern Hopfield energies. The target
is a checkable implication and, if possible, an explicit counterexample to
the converse. This directly resolves one of the next steps named in the
earlier report. It does not audit the numerical capacity certificates or
claim a new iid capacity bound.

Web reads used: https://arxiv.org/abs/2611.03306;
https://arxiv.org/html/2611.03306v1 (Theorem 1.1, Corollary 1.5,
replica-symmetry discussion); https://hexagonmath.org/2611.00105v1;
https://hexagonmath.org/pdf/2611.00105v1 (Section 6, Theorem 6.9).

## First finite landscape search

Added `audit_landscape.py`: a seeded NumPy search at N=12, followed by
independent exhaustive verification using Python integers and a Gram-matrix
energy calculation. Command:

`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 audit_landscape.py --search`

The sandbox rejects setting niceness from inherited 20 to 15; the program
prints priority 20, which is already lower priority than required. The
search found a monotone shell profile with a strict local minimum at
trial 69, M=13, in 0.045 seconds. Verification failed an additional
requirement: the selected minimum was also a maximum of Q on its own
shell. That does not invalidate a counterexample to the converse, but the
stronger desired example is suboptimal even within its shell. The search
filter will explicitly include this extra condition, then verification
will be rerun. No result is claimed from this first certificate.

## Exact finite counterexample verified

With the strengthened filter, the same command succeeded at trial 620:

```text
priority 20
OMP_NUM_THREADS 1
search: N=12 M=11 seed=347 trial=620; 0.4547 seconds
sigma = [1,1,1,-1,1,1,1,1,1,1,1,-1]
errors = 2; overlap = 8/12
Q(sigma) = 240
max Q by errors d=0,...,6 = [192,236,256,284,288,300,304]
Q(sigma)-Q(single-flip neighbor) =
[36,36,4,36,100,4,20,20,100,20,52,4]
minimum energy increase = 4/24 = 1/6
shell-maximum witness at d=2 = [1,1,-1,1,1,1,1,-1,1,1,1,1]
all 4096 states checked twice
```

The certificate is `counterexample.json`. Every energy was checked by
both pattern dot products and the expanded integer Gram quadratic form;
each flip difference was also checked from the zero-diagonal local field.
The positive-overlap shell maximum is monotone, yet a strict local minimum
exists and is suboptimal on its own shell.

To address the thermodynamic rather than just finite-grid formulation,
the same extension will include a block construction: use nonconstant
Walsh characters to decouple this 12-spin example from many ferromagnetic
blocks. It yields a flat limiting fixed-overlap energy profile and strict
local minima at overlap tending to one with every stored pattern.
The patterns in this construction are deterministic/correlated; it tests
the proposed logical implication and does not refute an iid theorem.
The finite barrier implication and this nonconverse form the one selected
landscape audit.

## Proof and independent block verification

Wrote PROOF.md. Proposition 1 proves that a strict shell energy gap yields
a local minimum inside the Hamming cap, with the correct zero-diagonal
single-spin field. Corollary 2 states precisely the common probabilistic
event required for simultaneous iid-pattern minima, and proves their
distinctness for disjoint small caps. Proposition 3 constructs the
nonconverse at extensive load: for B>=2 and K=2^q,
N=12+B(K-1), M=11K, all shell profiles tend uniformly to 11/2 while every
stored pattern lies within twelve flips of a strict local minimum.
The proof uses explicit Walsh orthogonality and uniform upper/lower
bounds, not numerical extrapolation. Patterns are correlated.

Added `audit_blocks.py`. Command:

`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 audit_blocks.py`

Output:

```text
priority 20
OMP_NUM_THREADS 1
all Gram entries checked: 18 neurons, 44 patterns
all 262144 actual states: Gray-code profile equals block DP
strict local minima verified near all 44 patterns
minimum flip energy increase 4/9
B=79 limiting load 11/79 = 0.13924050632911392
K N M profile_min profile_max proved_uniform_error_bound
2 91 22 0.247675402 8.326892887 5.5
4 249 44 4.495185562 6.653344301 1.194633958
8 565 88 5.187024826 6.025355157 0.541394001
16 1197 176 5.377771915 5.751326241 0.258473041
elapsed_seconds 1.138
```

The small-instance verification constructs the actual binary pattern
matrix, checks every Gram entry, enumerates all actual spin states by
Gray-code pattern-projection updates, and compares their shell profile
with a separate exact block dynamic program. Direct dot products check
every flip at the proposed minima near all 44 patterns. The B=79 data
are exact block calculations displayed as decimals; the proof of the
limit is analytical. Its bounds use Q_core<=1584, so the asymptotic proof
does not depend on the exhaustive maximum Q_core=304.

Also reran the base certificate without searching:

`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 audit_landscape.py`

It passed with exactly the same shell maxima and twelve flip differences
recorded above. Runtime about 0.016 seconds. All verification runs are
single-threaded, tiny compared with 1 GB, and below two seconds.

Independent arithmetic for the strict core minimum: P*s=(8,0,8,0,4,-2,
6,6,0,-4,-2), whose squared norm is 240. Signed off-diagonal fields,
computed by summing over j!=i, are (9,9,1,9,25,1,5,5,25,5,13,1);
they also equal s_i(P^T P s)_i-11. Thus the minimum base flip cost is
1/6. In the block family it is 2K/N, while a block flip costs
22K(B-1)/N; for K=4,B=2 this is min(4/9,44/9)=4/9, agreeing with
direct full-pattern energies. The load 11/79 was checked as an exact
Fraction against 0.13820106, independently of its decimal printing.

## Attempts to break the result and final scope check

Checked the energy sign in both Q and H conventions and the N versus N^2
normalization. A well is a rise of -H/N with increasing overlap. Shell
minimizers on the outer boundary do not suffice; the strict shell gap
forces the cap minimizer one full spin step inside. Ties give non-strict
minima in Proposition 1; strictness in Proposition 3 is separately checked.

The block construction would have neutral spins at B=1, so the statement
requires B>=2. Bounds are uniform in every shell, including d=0 and N,
and in every reference pattern. At the endpoint shells the construction
can put up to twelve errors in the core. Minima for different correlated
patterns need not be distinct; no such claim is made. The iid distinctness
corollary has its own disjoint-cap hypothesis b<1/4.

Opened the capacity preprint's Theorem 1.2(e) again and checked the exact
simultaneous ground-state barrier statement (1.14). Proposition 1 applies
to such a statement. Its upper-regime Theorem 1.2(d) asserts a strictly
decreasing profile, whereas the asymptotic construction here has a flat
profile. The construction therefore disproves a general no-well inference,
not a potential theorem using strict decrease and iid estimates. This
limitation is explicit in PROOF.md and REPORT.md.

The positive-temperature free-energy formula does not turn into a
ground-state barrier without a zero-temperature argument; none is silently
assumed here. The actual iid 0.138 question and replica symmetry remain
unresolved in this work. No outside-folder files were edited, no git was
used, and nothing was published. Wrote REPORT.md with the required verdict
and next-step instructions.


