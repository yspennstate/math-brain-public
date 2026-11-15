# Fourier entropy-influence: the checks behind ten papers, November 2026

Ten short papers on the Fourier entropy-influence conjecture of Friedgut and Kalai (1996) came out of the campaigns in
`../fei-solve-2026-11` and `../fei-lower-bound-search-2026-11`. Each paper is public in its own repository, with its
manuscript, PDF and code. This folder holds the working material behind them: the scripts that check each lemma,
their outputs, the derivation notes, the census cross-checks and the second-reader audits run before posting.

## The papers

| | Paper | Repository |
|---|---|---|
| p1 | The one-coordinate step in the Fourier entropy-influence conjecture | github.com/yspennstate/fourier-entropy-influence-one-coordinate |
| p2 | Good coordinates in the Fourier entropy-influence conjecture | github.com/yspennstate/fei-good-coordinates |
| p3 | A variance form of Han's bound on the Fourier entropy | github.com/yspennstate/fei-variance-han-bound |
| p4 | Four equivalent forms of the Fourier entropy-influence conjecture | github.com/yspennstate/fei-equivalent-forms |
| p5 | A filtration bound for the erasure entropies of Boolean functions | github.com/yspennstate/fei-filtration-witness |
| p6 | Erasure entropies of sparse linear DNFs | github.com/yspennstate/fei-sparse-linear-dnf |
| p7 | The Fourier entropy of linear monotone DNFs on few variables | github.com/yspennstate/fei-linear-dnf-census |
| p8 | Hidden coordinates and selection rules in the Fourier entropy-influence conjecture | github.com/yspennstate/fei-hidden-coordinates |
| p9 | A forced coordinate with nearly maximal erasure entropy | github.com/yspennstate/fei-forced-coordinate |
| p10 | The erasure entropy of a forced coordinate under every bias | github.com/yspennstate/fei-forced-coordinate-bias |

The manuscripts themselves are not copied here; the repositories above are the versions of record.

## Layout

- `p1/` ... `p10/`: for each paper, `code/` with every check script next to its saved output (`*_out.txt`,
  `*.json`), and where they exist the outline (`OUTLINE.md`), the hand derivations (`DERIVATIONS.md`) and the census
  cross-check (`p7/CENSUS_CHECK.md`, an independent C enumeration of linear monotone DNFs up to eight variables that
  agrees with the campaign's own census class by class). `p5/code/lean/` has a Lean file for the two-sequence lemma.
- `checks/`: the lattice and slab checks shared by several papers (exact rational arithmetic where the claim is an
  identity, mpmath where it is a bound).
- `towers/`: the read-once and mixed tower climbs used for the monotone tower table.
- `audit/`: second reads done before posting. A second reader rebuilt the key numbers of p7 and p8 by Monte Carlo
  and orbit counts with code written separately from the paper's, and checked every reference in p8 against its
  source (`p8_refcheck.py`).

## What was known and what is new

The conjecture is Friedgut and Kalai's. The tools the papers build on are the KKL theorem (Kahn, Kalai and Linial,
1988), Talagrand's inequality (1994), hypercontractivity (Bonami 1970, Beckner 1975), Han's inequality, the bound for
read-once formulas of O'Donnell, Wright and Zhou (2011), the level-weight approach of Keller, Mossel and Schlank
(2012), and the lower bounds on the constant of O'Donnell-Wright-Zhou, Hod and Numaro. Each paper's introduction says
which of its statements are new and how they relate to these; the short version is that the papers prove partial
cases (one coordinate, sparse and linear DNFs, a forced coordinate) and equivalent reformulations, and none of them
proves the conjecture.

## Credit

The mathematics the papers stand on belongs to the authors named above. The new statements, the check scripts and
the audits were produced by AI agents (Claude and Codex) working under human direction; each paper's AI declaration
says which system did what.

## Reusing it

Every claim in the papers has a script here that tests it on all functions of a few variables before the proof was
written. To check a new inequality about Boolean functions, copy one of the `check_*.py` files, replace the claimed
quantity, and run it on the census.
