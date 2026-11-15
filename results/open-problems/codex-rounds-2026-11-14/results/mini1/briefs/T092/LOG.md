# T092 work log

Started 2026-11-14 21:58 +04 (Asia/Tbilisi).
Task: “push this problem forward by one checkable piece.”

## Scope and startup

All writes stay in this folder. No git, external publication, subagents,
or global checklist/mesh/brain updates: those would write outside the scope
explicitly authorized for this session. Read the startup and identity/method
memories directly. Read the compute state: status warn, mode owner_away_open,
CPU 97%; no heavy computation planned. Programs will use nice -n 15 and
OMP_NUM_THREADS=1.

Commands: `pwd`, `date '+%Y-%m-%d %H:%M:%S %Z'`, `ls -la`, and read-only
`cat`/`rg` for startup notes and compute state. An initial file-name search
was too broad and its output was truncated; it was narrowed immediately.

## Literature search, initial step

Web searches: `Banach problem simple Lebesgue spectrum probability preserving
2025 2026`; `"simple Lebesgue spectrum" "2024" "2025"`; `"2210.15480"`.

Search returned a claimed exact solution, “A smooth three-torus diffeomorphism
with simple Lebesgue spectrum”, attributed to OpenAI, dated 23 September 2026,
with a GitHub URL. Opening that URL initially returned cache miss. This is a
lead, not yet a verified solution. Opening arXiv:2210.15480 confirmed author
el Houcein el Abdalaoui, latest version 9 June 2023. Opening arXiv:2405.03641
confirmed author Valery V. Ryzhikov and that its abstract still treats the
finite-probability problem as open. Opened V. V. Ryzhikov's 2026 paper page
“Spectra and joint dynamics of Poisson suspensions over rank-one
automorphisms”, https://www.mathnet.ru/eng/sm10228; its results concern tensor
powers and Poisson suspensions, not a claimed finite simple-Lebesgue example.

Next: inspect the claimed 2026 solution directly within the ten-minute
literature budget. Do not infer a theorem from a search snippet.

## 21:59 +04 — primary-source statement located

Opened the manuscript's GitHub `build/sections/01-introduction.tex`, its
`README.md`, its `paper.pdf` wrapper, and `lean/docs/144.md` using the web
tool. README confirms author **OpenAI**, date **September 23, 2026**, and
repository preprint identifier
`OAI:A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026`.
The introductory theorem claims a smooth volume-preserving diffeomorphism
of the standard-volume three-torus and a real mean-zero vector with a
complete bilateral orthonormal orbit. The scope note claims a matching Lean
formalization. No arXiv id is supplied in the primary README.

The GitHub PDF wrapper is not the PDF contents. Next open the raw PDF and
check the exact theorem directly. No independent proof validation has yet
been done; source assertions of formalization are not a replay.

## Primary text and validation check

The raw introductory TeX opened successfully; it states exactly the required
finite-probability conclusion. The raw PDF returned unsupported
application/octet-stream, so the TeX is the directly inspected manuscript.
Opened raw `05-completion.tex` and read the final diagonal argument: it
retains each finite Laurent-polynomial approximation under summable changes
and repeats a dense family of targets. This checks the intended scope but
does not validate the earlier finite construction.

Exact-title searches with `arxiv` found no arXiv identifier. Searches with
`error OR gap OR review OR counterexample` found no independent mathematical
review establishing validity or an error in the inspected results.

Opened `lean/ComparatorChallenges/ThreeTorus.lean`: the challenge theorem
ends in `sorry`. This is NOT by itself evidence of a gap in the claimed
proof: it is a comparator challenge, and the repository instructs readers
to compare it to separate proofs. Opened the repository README: it describes
the collection as model-produced research data at differing verification
stages. Next read the comparator instructions and manifest before drawing
a conclusion about formal proof availability.

## Choice — stop at the external-result branch

The one concrete piece is to establish whether the newly located theorem
has the exact scope of T092 and identify its actual proof artifact. This
avoids spending this session on a special case of a problem for which a
direct solution has just been announced. The output will distinguish a
located claim from an independently checked proof. No new existence theorem
will be claimed.

## Proof-artifact check and independent scope audit

Web-opened `lean/ComparatorChallenges/ThreeTorus.json`. It identifies
`OAI.Dynamics.ThreeTorus.Main` as the solution module and
`OAI.ThreeTorus.simple_lebesgue_spectrum` as the theorem; permitted axioms are
propext, Quot.sound, Classical.choice. Web-opened the actual file
`lean/OAI/Dynamics/ThreeTorus/Main.lean`: its top-level theorem has a proof
body invoking `exists_physical_basis` and `mainConclusion_of_basis`, rather
than `sorry`. This checks source availability only, not the dependency
closure or compilation. `formalization.yaml` had no `ThreeTorus` text match;
the comparator configuration provides the direct artifact path.

Independent mathematical scope check: if an invertible probability map
has a vector f whose integer translates form an orthonormal basis of the
whole mean-zero space, send U^n f to z^n. On finite linear combinations this
preserves norm by orthonormality. Completeness on both sides extends it to
a surjective isometry, and sending n to n+1 intertwines U with multiplication
by z. Thus the stated conclusion would answer exactly T092. Conversely, a
unitary equivalence to multiplication by z pulls back the constant circle
function 1 to such a vector. This check does not use the manuscript's
construction or its Lean proof.

Failure modes checked: finite versus infinite measure; discrete map versus
flow; entire mean-zero space versus one component; orthonormal versus merely
cyclic orbit; and challenge statement versus separate solution proof. None
changes the claimed scope. No proof replay, dependency audit, or independent
review was obtained. No numerical computation was run, hence there are no
load-bearing numerical outputs to reproduce.

Decision: save SOLVED_ELSEWHERE.md as a claim notice, with REPORT.md carrying
VERDICT: PARTIAL. The filename follows the requested external-result branch;
it must not be interpreted as certification that the problem is settled.
Search work ended within ten minutes of 21:58 +04. No git or external write
was used. No new mathematical construction was attempted.

## 22:01 +04 — saved-file checks

Commands and outputs:

```
env OMP_NUM_THREADS=1 nice -n 15 /usr/bin/wc -l LOG.md REPORT.md SOLVED_ELSEWHERE.md
nice: setpriority: Operation not permitted
118 LOG.md
45 REPORT.md
29 SOLVED_ELSEWHERE.md
192 total

env OMP_NUM_THREADS=1 nice -n 15 /usr/bin/head -n 1 REPORT.md
nice: setpriority: Operation not permitted
VERDICT: PARTIAL located an exact claimed external solution; validity not independently verified

date '+%Y-%m-%d %H:%M:%S %Z'
2026-11-14 22:01:21 +04
```

The sandbox refused the requested niceness adjustment for these millisecond
file checks, despite returning their output. No computation or build was
launched after this failure. The line counts above precede this appended
entry. Files and verdict prefix were checked; search finished about three
minutes after startup.
