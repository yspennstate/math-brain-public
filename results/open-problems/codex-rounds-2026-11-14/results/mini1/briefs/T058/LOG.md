# T058 work log

Task: “push this problem forward by one checkable piece”, received 14 November 2026; first recorded local clock 20:48:16 +04.

## 1. Orientation and literature search

Only this directory will be modified. No git or subagents. The folder initially contained PROMPT.md, codex.log and run.pid.

Read the compute governor: status `ok`, mode `owner_away_open`. Read the brain navigation index. The session's folder-only rule rules out running brain/mesh/checklist commands that write elsewhere. Those global registrations will therefore not be performed.

Commands used for read-only orientation included `pwd`, `rg --files`, and a short Python pathlib reader, launched with `OMP_NUM_THREADS=1 nice -n 15`. The sandbox reported `nice: setpriority: Operation not permitted`; an attempted `ps` priority inspection was also denied. No substantial computation will be run without resolving this limitation. Symbolic work and tiny file-writing/reading operations suffice for the planned task.

Web search queries:

- `chromatic number random graph concentration Heckel Riordan 2024 2025 2026 typical n`
- `"chromatic number" "concentration" "Steiner" Heckel`

Opened https://arxiv.org/abs/2103.14014 and https://arxiv.org/html/2103.14014 (Annika Heckel, Oliver Riordan), and the author's publication list https://annikaheckel.github.io/ . The abstract confirms the infinitely-many-n lower bound and an older upper bound improved by Alon to approximately sqrt(n)/log(n). The paper contains a “Zigzag Conjecture”; its precise formula and quantifiers need checking before accepting the brief's density-one formulation.

Additional search queries: `"chromatic" "concentration" "2026" "Heckel"`; `"chromatic" "concentration" "2025" "zigzag"`; `"chromatic number" "density one" concentration`; `"zigzag conjecture" chromatic 2025 2026 solved`; `"chromatic number" "non-concentration" "2026"`; and the analogous 2025 query.

Opened Erlang Surya and Lutz Warnke, *On the Concentration of the Chromatic Number of Random Graphs*, https://www.combinatorics.org/ojs/index.php/eljc/article/view/v31i1p44 (2024): the new regimes in its abstract have p tending to 0 or 1. Opened Zhifei Yan, *The chromatic number of very dense random graphs*, https://arxiv.org/abs/2405.13914 (2024): its regime also has p tending to 1. Neither solves the fixed-p=1/2 question. The bounded search has not found a later solution; this is not a claim to exhaustive coverage.

Priority limitation resolved: exact command `OMP_NUM_THREADS=1 nice -n 15 python3 -c 'import os; print("inherited_nice=",os.getpriority(os.PRIO_PROCESS,0))'` printed `inherited_nice= 20` despite the nice diagnostic. A read of the existing verified memory about stacked relative nice explains the diagnostic at the inherited maximum priority reduction. Thus actual priority already satisfies nice >=15. No heavy computation is planned.

## 2. Chosen piece (before proof)

Prove an elementary density theorem for the fractional phase of the independence-number approximation, then use it to state precisely how the published Zigzag Conjecture differs from the brief. In particular, show that an entire positive-lower-density set of integers has predicted width exponent at most 3/8+o(1), which would preclude exponent 1/2 on any density-one set if that conjecture is true. This is a deterministic statement and a conditional consequence, not an unconditional new bound on the chromatic number.

Why this piece: the quantifier caveat is substantive. The paper predicts an exponent max(theta/2,(1-theta)/2), where theta is asymptotic to a fractional phase. Establishing the size of phase bands makes the conflict checkable; “infinitely many” alone would not rule out a density-one formulation. A complete proof needs only inversion, a geometric sum, and careful treatment of integer endpoints. No random-graph simulation is needed.

## 3. Search completed; statement verified

The literature check is closed within the ten-minute budget. No later solution of fixed-p=1/2 concentration was found. Opened https://arxiv.org/abs/2306.07253, Annika Heckel and Konstantinos Panagiotou, *Colouring random graphs: Tame colourings* (submitted 2023, revised September 2024). This develops bounded colourings and supports the Zigzag Conjecture; it is not a solution of the ordinary chromatic-number concentration problem. No SOLVED_ELSEWHERE.md is warranted.

Verified directly in Heckel–Riordan: definitions (2)–(4), equation (9), Conjecture 10, and Theorem 5. Conjecture 10 has width exponent lambda(n)=max(theta(n)/2,(1-theta(n))/2), not constant 1/2 on a density-one set. The proof below will independently derive equation (9), so its uniform error need not be assumed.

Derived candidate exact density formula for any fixed phase band of length d in (0,1), with r=sqrt(2): lower density (r^d-1)/(r-1), upper density r(1-r^(-d))/(r-1). A full cycle is multiplicative in n by r, rather than additive. This already indicates that natural density generally does not exist. The logarithmic density should equal d. All three claims still need a written proof and an independent check.

## 4. Proof written

Created PROOF.md with the complete inverse-function argument, a dominated geometric-sum bound for old cycles, integer-rounding errors, logarithmic density, and a direct derivation of theta={f(n)}+O(log log n/log n) using elementary factorial bounds. The resulting density formulas give a set of positive lower density with conjectured width exponent at most 3/8. Also formulated fixed-confidence widths W_q so that “shortest high-probability interval” has a precise meaning.

Audit to perform next: check the asymptotic constants by a second derivation from just the counts at the two band endpoints; compare direct integer enumeration with inverse-interval counting; evaluate finite cycles against the limit; check endpoint and uniform-error issues and the conditional/proved distinction.

First check command: `OMP_NUM_THREADS=1 nice -n 15 python3 verify_phase.py`. It stopped before computation because macOS rejected setting RLIMIT_AS to 768 MiB (`ValueError: current limit exceeds maximum limit`). The script's memory-limit setup needs a platform-compatible correction. No mathematical assertion failed.

A second invocation of the same command also stopped at platform resource-limit setup, after trying a soft RSS limit bounded by the inherited hard limit. Removed the incompatible resource-limit changes. The check uses only standard-library scalar arithmetic, 200,000 enumeration steps and a few thousand stored floats, with fixed loop bounds; it records actual peak RSS and duration instead. This is far below the requested memory/time budget.

## 5. Verification output

Exact command: `OMP_NUM_THREADS=1 nice -n 15 python3 verify_phase.py`

Exit code: 0. Stderr: `nice: setpriority: Operation not permitted` (inherited nice is verified as 20). Full stdout:

```json
{
  "nice": 20,
  "constants": {
    "lower": 0.45678638313705516,
    "upper": 0.5432136168629449,
    "log_density": 0.5
  },
  "integer_counts": [
    {
      "N": 1000,
      "direct_count": 454,
      "inverse_count": 454
    },
    {
      "N": 10000,
      "direct_count": 4976,
      "inverse_count": 4976
    },
    {
      "N": 100000,
      "direct_count": 49829,
      "inverse_count": 49829
    },
    {
      "N": 200000,
      "direct_count": 106225,
      "inverse_count": 106225
    }
  ],
  "finite_cycle_diagnostic": [
    {
      "cycle": 40,
      "entry": 0.45400514448656504,
      "entry_error": -0.0027812386504901254,
      "exit": 0.5459609866730059,
      "exit_error": 0.0027473698100609623
    },
    {
      "cycle": 160,
      "entry": 0.4560492884973589,
      "entry_error": -0.0007370946396962896,
      "exit": 0.5439484911386314,
      "exit_error": 0.0007348742756865256
    },
    {
      "cycle": 640,
      "entry": 0.45659615289557787,
      "entry_error": -0.00019023024147729606,
      "exit": 0.5434037007327444,
      "exit_error": 0.00019008386979946224
    },
    {
      "cycle": 2560,
      "entry": 0.45673822345672804,
      "entry_error": -4.8159680327120036e-05,
      "exit": 0.5432617671873853,
      "exit_error": 4.8150324440388026e-05
    }
  ],
  "bracket_identity_max_error": 8.215650382226158e-15,
  "theta_checks": [
    {
      "log2_n": 10,
      "phase": 0.2415338920032024,
      "theta": 0.46012237035216536
    },
    {
      "log2_n": 20,
      "phase": 0.2415338920032042,
      "theta": 0.4645807883029279
    },
    {
      "log2_n": 40,
      "phase": 0.2415338920032042,
      "theta": 0.4099246874423199
    },
    {
      "log2_n": 80,
      "phase": 0.24153389200318998,
      "theta": 0.3546164042926988
    },
    {
      "log2_n": 160,
      "phase": 0.24153389200318998,
      "theta": 0.3124192057871862
    }
  ],
  "elapsed_seconds": 0.169,
  "peak_rss_bytes": 14483456,
  "status": "all checks passed"
}
```

The successful run used about 14.5 MB peak RSS and 0.169 seconds. All four integer counts agreed across direct enumeration and inverse-interval counting. The independently derived density constants agree within 1e-14. The cycle diagnostic approaches both limits, and the bracket identity error is below 1e-12.

Created AUDIT.md with an independent contracting recurrence for both density constants, a second log-coordinate derivation of logarithmic density, the separate inequality calculation yielding d=4 beta-1, and checks of endpoint errors, density-one intersections, and probabilistic quantifiers.

## 6. Final report

Created REPORT.md with verdict PARTIAL. The completed piece is the unconditional deterministic phase-density theorem and its conditional consequence for the published Zigzag Conjecture. The main random-graph problem remains open in this work. No claim of a new unconditional concentration bound or of literature novelty is made. All created artifacts are in this folder.

Final artifact audit: `OMP_NUM_THREADS=1 nice -n 15 python3` with pathlib/json checks confirmed required files, PARTIAL verdict and stored all-checks-passed status; no SOLVED_ELSEWHERE.md. Output: `Artifact audit passed: required files present, verdict and stored check status valid.`
