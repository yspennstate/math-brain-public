# T097 work log

Task received: 14 November 2026; first local clock reading 21:16:48 +04
(Asia/Tbilisi). Task: “push this problem forward by one checkable piece.”

## 21:16–21:20 — orientation and initial literature check

Read the local startup memory, brain index, relevant search-index entries,
and compute-state file. Work is confined to this folder. The later task's
folder-only rule overrides the general requests to update the external brain,
mesh, and checklist; none of those external stores was modified.

Read-only shell calls were prefixed with `OMP_NUM_THREADS=1 nice -n 15`.
The sandbox reports `nice: setpriority: Operation not permitted`. No numerical
workload will be launched unless this restriction can be met. A proof-only
piece avoids needing such a workload. The compute governor reported `warn`,
`owner_away_open`, and CPU saturation.

Web searches used the requested web search tool, including:

- `Gaussian free field lattice critical exponents 2025 2026 percolation three dimensional`
- `"2610.03703"`
- `"2406.02397"`
- `"lattice" "Gaussian free field" "critical exponents" "2026"`
- `Muirhead strongly correlated Gaussian fields II sharpness percolation density beta bound capacity`

Opened arXiv pages 2610.03703, 2609.08702, 2406.02397, and 2002.07735.
The first three concern metric-graph/cable connectivity. Search also found
Stephen Muirhead's 2206.10724, which needs checking for existing quantitative
lattice bounds before choosing a result. No resolution of the lattice exponent
problem has been found so far. Exact references and scope will be recorded
after reading the relevant statements.

## Choice of the checkable piece (recorded before proof work)

Prove an explicit finite-set Gaussian change-of-level comparison in terms of
the lattice capacity, and derive its precise consequence for the still-open
critical one-arm and percolation-density exponents on Z^3. The planned
conditional constraint is `beta >= 2 rho`, where `theta(h_* - t) = t^{beta+o(1)}`
and `P(0 connects to boundary B_R at h_*) = R^{-rho+o(1)}`. Neither exponent's
existence will be assumed as a theorem. Also determine what this comparison
actually gives for a clearly defined relative one-arm crossover scale.

Reason: this produces a finite-scale, checkable reduction on the lattice
without transferring cable connectivity identities across the positive
critical-level gap. It can be proved directly by finite-dimensional Gaussian
calculus and a lattice Dirichlet-energy test function. It may be a standard
consequence of existing change-of-measure methods; no novelty is claimed.

The audit will check the sign of the level shift, the covariance/energy
normalization, a second derivation of the comparison, all power and logarithm
exponents, and the distinction between a relative crossover scale and an
ordinary correlation length.

## Literature check completed (within the ten-minute allowance)

Opened the full HTML of Stephen Muirhead, *Percolation of strongly correlated
Gaussian fields II. Sharpness of the phase transition*, arXiv:2206.10724v2,
especially Theorems 1.2 and 1.10. For Z^3 these give, for every q > 4,
`theta(h_* - t) >= c_q t^q` at small t. This is existing quantitative
near-critical information missing from the short problem summary; it does
not prove the existence of beta. It supplies an external input for an
unconditional corollary of the planned comparison: for every epsilon > 0,
`p_R(h_*) >= R^(-2-epsilon)` for all sufficiently large R.

Also opened the full HTML of Vivek Dewan and Stephen Muirhead,
arXiv:2102.12123v2. Its stated Gaussian one-arm bounds concern finite-range
or sufficiently rapidly decaying fields; no direct application of those
theorems to the massless Z^3 GFF is being made.

The last search found arXiv:2611.05357, opened on arXiv itself: Pierre-François
Rodriguez, Jialu Shi, Wen Zhang, *On the one-arm probability for the metric
graph Gaussian free field in high dimensions* (3 November 2026). It treats
cable-system sign clusters, including d >= 6, not critical lattice excursions.
No source found settles the lattice question. No SOLVED_ELSEWHERE.md is
appropriate for a lattice resolution; the cable update is recorded here and
in LITERATURE.md. Literature searching stops here.

## Proof construction

For simple-random-walk Green normalization, the exact energy of a sup-norm
tent equal to one on B_R and zero outside B_(2R) is
`(28 R - 1/R)/3`. Therefore `cap(B_R) <= (28/3) R`.
The Gaussian comparison will have the explicit displacement
`t sqrt(cap(B_R)) <= t sqrt(28 R/3)`. This is sharper than using the number
of sites, which would give the wrong R^(3/2) displacement.

Two proof routes are available: a Gaussian score/rearrangement argument,
and a likelihood-ratio half-space argument. Both will be written out.

## Completed proof

Created PROOF.md with the finite-dimensional comparison, a full capacity
normalization argument, and the exact tent-energy calculation. It proves:

- `beta >= 2 rho` conditional on the two logarithmic exponents existing;
- unconditionally, using Muirhead's existing theorem,
  `limsup -log(p_R(h_*))/log R <= 2`;
- for the explicitly defined first radius at which the subcritical arm is
  half the critical arm, `L_rel(t) >= c t^-2/log(1/t)` at small t.

The ordinary correlation length, exact exponent values, exponent existence,
and agreement with cable exponents remain unresolved.

## Adversarial checks completed

Created AUDIT.md. Independently re-derived the Gaussian inequality by a
likelihood ratio; checked the exponent calculations again by a third method,
using Hölder and Gaussian likelihood moments. Recomputed the tent energy by
expanding sums of squares and checked R=1,2 exactly. Tested the logarithmic
loss by substituting both candidate scales into the bound. The stronger
claim `L_rel >= c t^-2` does not follow. Checked small radii, critical
percolation, non-monotonicity of the probability ratio, field normalization,
and the distinction between lattice and cable connectivity.

Exact mathematical commands: none (proof-only result). No numerical script
was run, and no numerical data file is claimed. File creation used the
apply_patch tool in this folder. Web queries and their relevant findings are
listed above; source URLs are in LITERATURE.md.

## Final deliverable

Created REPORT.md with verdict PARTIAL. The finite-scale comparison and its
consequences are complete; the original exact-exponent problem is open.
No git operations, external writes, subagents, or numerical workloads were
used. No novelty or equivalence with a standard correlation length is claimed.

Final read-only verification command:

```sh
OMP_NUM_THREADS=1 nice -n 15 /bin/zsh -c 'for f in LOG.md PROOF.md AUDIT.md LITERATURE.md REPORT.md; do if [[ -s "$f" ]]; then print -r -- "$f: present"; else print -r -- "$f: MISSING"; fi; done; head -1 REPORT.md; date "+%Y-%m-%d %H:%M:%S %Z"'
```

Output:

```text
nice: setpriority: Operation not permitted
LOG.md: present
PROOF.md: present
AUDIT.md: present
LITERATURE.md: present
REPORT.md: present
VERDICT: PARTIAL a capacity-based lattice reduction and a relative one-arm crossover lower bound
2026-11-14 21:23:29 +04
```
