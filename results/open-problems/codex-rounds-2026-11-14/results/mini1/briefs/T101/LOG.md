# T101 work log

Task received 2026-11-14, approximately 21:58 Asia/Tbilisi: “push this problem forward by one checkable piece.”

## 21:59 — setup and literature check

All artifacts stay in this folder. No git, external posting, subagents, or shared-brain/mesh/checklist writes: the task-specific folder-only instruction overrides those global write routines. Read the startup memory index and compute state directly. Compute state: warn, owner_away_open, 69% free memory. Commands use `nice -n 15 env OMP_NUM_THREADS=1`; macOS prints `nice: setpriority: Operation not permitted` because this worker already has priority 20 (verified by `os.getpriority(os.PRIO_PROCESS,0)`). Thus calculations inherit a priority lower than nice 15. No priority increase is attempted.

Opened with the web tool:

- Gady Kozma and Vladas Sidoravicius, *Lower bound for the escape probability in the Lorentz Mirror Model on the lattice*, arXiv:1311.7437, https://arxiv.org/abs/1311.7437. Abstract gives the stated 1/(2n+1) lower bound.
- Martin P. W. Zerner, *Infinite light rays and infinite clusters with infinitely many pivots*, arXiv:2610.12460, https://arxiv.org/html/2610.12460v1. Introduction still calls square-lattice finiteness a conjecture. Its p is the probability of EACH orientation, half the density in this task.
- Jian Gu and Qin Hao, *Boundary transmission and excursion geometry in the Lorentz mirror model: a numerical study*, arXiv:2609.14949, https://arxiv.org/html/2609.14949v1. Does not resolve infinite-plane localization.
- Raphaël Lefevere and Hal Tasaki, *Hierarchical Lorentz Mirror Model: Normal Transport and a Universal 2/3 Mean--Variance Law*, arXiv:2602.07988, https://arxiv.org/abs/2602.07988; also opened the PRL acceptance page (27 October 2026), https://journals.aps.org/prl/accepted/10.1103/mrqx-4nlv. Hierarchical transport results do not settle this problem.
- Kieran Ryan, *The spin-1/2 Heisenberg XXZ chain and the Lorentz mirror model with loop weight 2*, arXiv:2608.21306, https://arxiv.org/abs/2608.21306. The loop weight differs from this task's independent environment.

Search strings included `"Lorentz mirror" solved periodic orbits 2026`, `"Lorentz mirror" "November" "2026"`, and `"Lorentz mirror" localization proof 2026 square lattice`. One search snippet mentions a finite-scale criterion; checking its source before ending the bounded literature phase. No solution found so far.

## Literature phase finished; choice made before proof/computation

The remaining lead is Jian Gu and Qin Hao, *Boundary parity in the mirror model on the Manhattan lattice*, arXiv:2609.19498, https://arxiv.org/abs/2609.19498 (opened). It concerns the Manhattan lattice, and its sufficient threshold is not attained at the density tested. No solution or substantial advance for the stated independent square-lattice problem found in this search, which took less than ten minutes. Two SciRate opens failed (cache miss / 403); the arXiv page resolved the lead.

Chosen piece: compute exactly, for every p, the probability that a fixed directed edge belongs to a vertex-simple closed orbit having at most six mirrors. Such polygons should consist precisely of rectangles and orthogonal L-shaped hexagons. Sum over arbitrary side lengths, giving a rigorous explicit contribution to the periodicity probability, then audit the shape counts by an independent self-avoiding-walk enumeration. This is a limited family, not a proposed proof of all-orbit finiteness. It is feasible without simulation or a large finite box; in particular it tests dilute-density scaling after summing arbitrarily large loops.

Predicted formulas to be checked: with q=1-p, rectangle contribution p/[8(2-p)^3], hexagon contribution p q^2/[4(2-p)^5]. Their sum is a lower bound on periodicity and has first-order coefficient 3/128 at p=0. These are provisional until the proof and independent checks are complete.

## Exact audit completed

Wrote `audit.py` (standard library, single thread, CPU limit 180 seconds). Independent methods: enumerate vertex-simple walks starting with the fixed eastward edge, without assuming polygon type; exhaust all local environments in a 3-by-3 box and trace explicit slash/backslash reflection tables; evaluate the infinite sums by exact rational finite sums with rigorous geometric bounds on their tails.

Exact command:

```sh
nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 audit.py --max-length 14 --output audit_data.json
```

Output:

```text
nice: setpriority: Operation not permitted
PASS: rooted self-avoiding polygons through length 14
length=4: four_turns=2, six_turns=0
length=6: four_turns=6, six_turns=0
length=8: four_turns=12, six_turns=16
length=10: four_turns=20, six_turns=80
length=12: four_turns=30, six_turns=240
length=14: four_turns=42, six_turns=560
PASS: all 19683 three-by-three environments; 546 successes
PASS: five exact rational series checks, including p=1; tails < 1e-25
small-p coefficient: 3/128
priority=20; OMP_NUM_THREADS=1; peak_RSS_bytes=17235968
elapsed_seconds=0.06367
data=audit_data.json
```

The inherited nice 20 explains the warning as recorded above. Peak memory about 17.3 MB. All results saved in `audit_data.json`. At p=1/2 the separate infinite-family probabilities are 1/54 and 1/243, totaling 11/486. Proof being written; no general localization conclusion follows from these positive lower bounds.

## Proof and adversarial checks

Wrote `PROOF.md`. The six-corner classification follows from C-R=4: five convex corners and one reflex corner force the L shape. The four independent positive lengths and the choice of missing bounding-box corner are unique. The number of translates containing the fixed horizontal edge equals the number of horizontal unit boundary edges, rather than the total perimeter. No second orientation factor is allowed: the root is directed.

Checked possible omissions and overcounting: boundary corner states are prescribed uniquely; straight vertices must be empty; interior/exterior states are unrestricted; different shapes through the root are disjoint events by deterministic continuation. Positive parameters exclude degenerate hexagons. The p=1 endpoint gives rectangles=1/8, hexagons=0, consistent with requiring empty straight vertices. The result deliberately excludes self-intersecting periodic trajectories and simple polygons with eight or more mirrors. The independent walk enumeration actually finds 40 eight-turn polygons of perimeter 10, so interpreting B(p) as the full periodicity probability would be false for 0<p<1.

Second derivations: rooted perimeter counts are m(m-1) and 16 binom(m,4), independently verified by direct walks, then their generating functions reproduce the side-length sums. The two small-p coefficients 1/64 and 1/128 agree with the combined rational formula's coefficient 6/(8*2^5)=3/128. The finite-environment trace also reproduces the geometric box calculation at p=1/4,1/2,3/4, and its 546 successes split as 486 length-4 rectangles, 54 length-6 rectangles, and 6 length-8 hexagons.

One data-format issue found: converting extremely small positive exact tail bounds to float can display 0.0 (at p=3/4). Added the exact rational bounds to the data so decimal underflow cannot be read as a zero tail, and made the small-p coefficient an exact computed assertion. Re-running the same audit after these changes.

Final rerun, same exact command:

```sh
nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 audit.py --max-length 14 --output audit_data.json
```

```text
nice: setpriority: Operation not permitted
PASS: rooted self-avoiding polygons through length 14
length=4: four_turns=2, six_turns=0
length=6: four_turns=6, six_turns=0
length=8: four_turns=12, six_turns=16
length=10: four_turns=20, six_turns=80
length=12: four_turns=30, six_turns=240
length=14: four_turns=42, six_turns=560
PASS: all 19683 three-by-three environments; 546 successes
PASS: five exact rational series checks, including p=1; tails < 1e-25
small-p coefficient: 3/128
priority=20; OMP_NUM_THREADS=1; peak_RSS_bytes=17481728
elapsed_seconds=0.064552
data=audit_data.json
```

Finalized `REPORT.md` with a PARTIAL verdict. No proof of the full conjecture and no claim of literature novelty. The checkable result is the exact infinite-family probability in `PROOF.md`; all calculation artifacts remain here.

Final artifact check used a short `nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 -c ...` command to assert the five required artifacts exist, the report begins `VERDICT: PARTIAL`, the JSON records 19,683 environments, and every series row includes an exact tail bound. Output: `Artifact audit passed`.
