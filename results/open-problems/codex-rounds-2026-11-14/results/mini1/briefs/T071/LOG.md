# T071 work log

Task received: 14 November 2026, approximately 20:50 Asia/Tbilisi
(16:50 UTC): “push this problem forward by one checkable piece.”

## 1. Orientation and constraints

Read the supplied task and the compute governor state. State was `ok`,
`owner_away_open`. All writes will stay in this folder. The later, explicit
folder-only instruction rules out writing the shared mesh, checklist or brain.
No subagents, git, external messages, installations or background jobs.

Commands used for orientation included `pwd`, `rg --files`, and reads of
`~/.claude/compute/compute_state.json` and the brain navigation directory.
Subsequent shell reads were invoked with `env OMP_NUM_THREADS=1 nice -n 15`.
The sandbox printed `nice: setpriority: Operation not permitted`; `ps` was also
denied. Therefore no numerical workload will be launched. The piece chosen
below is a proof, with an independent analytic audit.

## 2. Literature check, begun 16:50 UTC

Web search queries:

- `"N-BBM" genealogy Bolthausen Sznitman 2025 2026`
- `"branching Brownian motion" selection genealogy coalescent 2025 2026`

Opened arXiv abstract pages, rather than relying on search snippets:

- Pascal Maillard, *Speed and fluctuations of N-particle branching Brownian
  motion with spatial selection*, arXiv:1304.0562, v4 (19 June 2018), journal
  reference 2016. Abstract concerns front positions and a Lévy limit.
- Alexandre Legrand and Pascal Maillard, *Time-inhomogeneous N-particle
  Branching Brownian Motion and the continuous random energy model*,
  arXiv:2402.04917, v4 (9 April 2026). Abstract concerns displacement.
- Julien Berestycki and Oliver Tough, *Selection principle for the N-BBM*,
  arXiv:2407.05792, v1 (8 July 2024). Abstract proves convergence of the
  stationary empirical measure to a minimal travelling wave, not genealogy.
- Jacob Mercer, *Branching Brownian motion with rank-based selection and
  reaction-diffusion equations*, arXiv:2605.04860, v1 (6 May 2026). Abstract
  concerns hydrodynamics, velocities and a weak selection principle.

No solution located so far. This is a bounded search, not a proof of absence.

## 3. Chosen piece (written before the proof)

Prove a topology obstruction for the actual N-BBM sample genealogy, together
with an explicit necessary three-lineage diagnostic under the weaker intended
finite-dimensional convergence. Every finite-N ancestral jump is binary;
the Bolthausen–Sznitman coalescent has genuine triple jumps. On a finite
partition space, J1 cannot collapse two binary jumps to one triple jump.

The useful quantitative output will be an exact lower bound for the
probability that the two successive mergers of a sample of three occur within
a short interval on the conjectured rescaled clock. This identifies a
specific burst estimate a proof of N-BBM convergence would have to establish.
It neither proves nor disproves the intended finite-dimensional conjecture.
The obstruction is elementary; no claim of literature novelty is made.

### Refinement before writing the proof, 16:54 UTC

The three-lineage calculation gives a stronger, useful reduction: for an
exchangeably labelled binary genealogy, convergence of the entire three-label
process in finite-dimensional distributions is equivalent to joint convergence
of just two times, the first merger time S_N and the duration H_N with two
ancestors. The proposed target is independent S ~ Exp(2) and
H ~ (1/4) delta_0 + (3/4) Exp(1). Equivalently its joint Laplace transform is
(r+4)/(2(s+2)(r+1)). Prove this equivalence as the main piece; the topology
obstruction and burst probability are consequences of the same calculation.

Additional literature check: opened arXiv:2301.07762v2 by Emmanuel Schertzer
and Alejandro H. Wences (13 March 2025). Its genealogy theorem concerns a
noisy branching random walk, not N-BBM. Opened arXiv:1001.2337v3 by Julien
Berestycki, Nathanaël Berestycki and Jason Schweinsberg, the absorption model.
Maillard's full HTML, section 1.4, explicitly explains that the spatial
coupling deforms genealogical trees. Mercer full HTML has no match for
`genealog`. The publisher page for the noisy BRW paper returned HTTP 403;
the arXiv abstract was accessible. No later N-BBM genealogy result found.

## 4. Proof saved

Created PROOF.md using the file patch tool. It proves the exact three-label
equivalence, a finite-grid burst lower bound, and the J1 obstruction with
bounded Lipschitz test-function separation (1-exp(-2T))/4. All mathematics
is analytic; there is no numerical output or simulated evidence.

The search was confined to the opening minutes of the session. The full HTML
of the absorption and noisy-BRW papers was also opened. The latter's model
description explicitly has discrete generations and multiple selection steps.
It is not the continuous-time, binary, leftmost-deletion N-BBM in the task.

## 5. Independent audit

Read PROOF.md back with
`env OMP_NUM_THREADS=1 nice -n 15 cat PROOF.md`.
Output was the saved proof; the sandbox again denied the requested priority
change. No numerical workload was run.

Created AUDIT.md. Re-derived all central constants using the three-state
generator and discounted backward equations. Checked the transform through
the independent absorption density, checked total probability, and obtained
the same exact values 1/4, 3/4 and 3/16. Constructed a counterexample showing
that correct separate merger-time marginals do not imply the required joint
limit. Checked finite history, sample labels, spatial collisions, suppressed
branches, limiting atoms, J1 endpoints and the undetermined time constant.

The last literature lookup was at 16:57 UTC, within the ten-minute limit.
The absorption paper's Theorem 3 explicitly states finite-dimensional
convergence; therefore the J1 obstruction does not contradict that theorem.
No N-BBM estimate is claimed, and no assertion of novelty is made.

## 6. Search record and report

Follow-up web search queries were:

- `"N-BBM" "genealogy" "2026"`
- `"N-BBM" "Bolthausen" "2025"`
- `"Genealogical transition in the noisy N-Branching Random Walk"`

Web open calls used the arXiv abstract URLs for 1304.0562, 2402.04917,
2407.05792, 2605.04860, 2301.07762 and 1001.2337, then full HTML URLs for
1304.0562v4, 2605.04860v1, 2301.07762v2 and 1001.2337v3. Find calls checked
`genealogical tree`, `genealog`, `Bolthausen`, `N-BBM`, and
`finite-dimensional distributions`. Relevant outputs are summarized above;
the precise supporting sections and clickable sources are in REPORT.md.

Created REPORT.md with verdict PARTIAL. Deliverables: PROOF.md, AUDIT.md,
REPORT.md, and this log. No SOLVED_ELSEWHERE.md: no qualifying solution or
substantial later N-BBM genealogy advance was located. No git was used and
no files outside this folder were edited.

Final readback at 17:00 UTC:

    env OMP_NUM_THREADS=1 nice -n 15 wc -l LOG.md PROOF.md AUDIT.md REPORT.md

Output before this final log append: 129, 262, 153 and 90 lines respectively.

    env OMP_NUM_THREADS=1 nice -n 15 head -n 8 REPORT.md

Confirmed first line exactly:
`VERDICT: PARTIAL exact three-lineage reduction and J1 obstruction`.
Both commands printed the same sandbox priority warning. The final artifacts
were checked against their stated scope: the auxiliary theorem is proved,
while the N-BBM-specific limit is explicitly left open.
