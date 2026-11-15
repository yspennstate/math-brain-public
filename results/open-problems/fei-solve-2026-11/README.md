# Fourier entropy-influence: working records of a solve campaign, 9-11 November 2026

The Fourier entropy-influence conjecture of Friedgut and Kalai (1996) asks for a universal constant C with
H(f) <= C I(f) for every Boolean function f on {-1,1}^n, where H is the entropy of the spectral distribution
fhat(S)^2 and I is the total influence. This folder is the complete working record of one attempt on it: the shared
notes, the briefs given to each Codex worker, every worker's status files, proofs, reports and scripts, the referee
passes on their claims, and the numerical checks. Nothing here proves the conjecture. What it does contain is a set of
exact reformulations, several proved partial bounds, a list of routes shown to fail, and the code that checks each
claim on every function of four variables and large samples beyond.

## Where to start

- `FLOW.md` is the summary. Every line there is marked PROVED (a short proof is written out and the statement passed
  the census check) or OPEN. Section 1 has the exact identities H = 2 A1 + 2 Gamma and H = A + B and the two-sided
  bounds that split the conjecture into a containment half and a cancellation half. Section 2 is the chain flow and
  a generalized Talagrand bound. Section 3 says where the proof of A1 <= C I stops at level r >= 2, and section 5(f)
  and 6 list shortcuts that are false, with the counterexample for each.
- `codex/NOTES.md` is the note every worker was given; `codex/briefs/` holds the individual briefs.
- `codex/workers/FEIB*/`, `workers_r8/`, `workers_r9/` are the workers' own files: STATUS, PROOFS, RESULTS, REPORT,
  and the scripts and outputs behind them. A worker's claim is not a result until a referee file agrees with it.
- `referee_p*.md` and `referee_r9/` are the referee passes. Each claim was re-derived by hand and, where possible,
  checked by an independent script.
- `code/` holds the checks (`check_p.py`, `check_feib09.py`, `check_sec5.py`, census tables over all 65,536
  functions of four variables) and the search outputs (`hill_out/`, `mc_out/`).
- `interval_cert/` certifies three rows of the monotone tower table by 60-digit outward-rounded interval arithmetic.
- `results/census5/` holds the census over functions of five variables, split into parts, with the frontier of each
  part (the functions with the largest ratios) as CSV.

## What is proved here, and what was known

Known before this work: the conjecture itself (Friedgut and Kalai); the KKL theorem (Kahn, Kalai and Linial, 1988)
and Talagrand's inequality (1994), which are the level-1 shadow of the statement; hypercontractivity (Bonami 1970,
Beckner 1975), used throughout; the bound for read-once formulas and symmetric functions and the lower bound 6.278 of
O'Donnell, Wright and Zhou (2011), later raised by Hod (6.4548) and by Numaro (6.5218, 2026, the record cited here);
the level-weight approach of Keller, Mossel and Schlank (2012); and the concentration of the spectrum on
2^{O(I log I)} characters of Kelman, Kindler, Lifshitz, Minzer and Safra (2020), the strongest general statement.

New in these records: the up-ratio form H = A + B with A a containment term and B a dispersion term, and Theorem 1
(A <= B + 2I - 2 Var), which reduces the conjecture to B <= C' I; the further split into P <= C I and Gamma <= C I;
the chain-flow telescoping of A1 and the bound m(R) <= up(R) min(1, r!/L(R)^r), whose r = 1 case is Talagrand's
inequality; the level-1 theorem E_S log(1/min_{i in S} Inf_i) <= C I and the fixed-level bounds A_1 <= 3.520226 I,
A_2 <= 6.1033 I, A_3 <= 7.872677 I; the coupling identity A = D(nu || mu x mu) and the noise form Phi(u), which gives
an equivalent statement for every fixed u < 1. The failures are as useful as the proofs: plain restriction
induction, max-influence restriction, monotone shifting, per-coordinate payment, the exponential-moment shortcut and
Conjecture W are each refuted with an explicit family (tribes, majority, AND, or an address construction).

## How the work was organized

One Claude agent kept the shared notes and refereed every claim. Thirty Codex workers took one brief each (a lemma to prove, a family to compute, a counterexample to look for) and wrote their attempts and
scripts into their own folder. Claims came back as reports; the referee re-derived them, ran an independent check, and
only then moved them into FLOW.md. The census scripts run every statement on all functions of four variables (and all
2^31 functions of five for Theorem 1) before a proof is attempted, which removed most false lemmas within minutes.

## Credit

The conjecture and every result cited above as known belong to the mathematicians named with it. The new statements
were produced by AI agents (Claude and Codex) and have been checked by those agents and by the census scripts, not by
a human referee. Agent and session labels have been removed from file names; worker folder names (FEIB01 and so on)
are the brief numbers. A few files that quoted private messages, raw arXiv responses and copies of third-party papers
are left out.

## Reusing it

The census pattern carries over to any inequality about Boolean functions: write the claim as a script first, run it
on every function of four variables and a sample of six, and only then spend effort on a proof. `code/check_sec5.py`
is a compact example that checks a dozen identities and bounds at once.
