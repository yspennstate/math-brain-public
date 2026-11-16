# Relaxation of the one-dimensional Fredrickson-Andersen model from a single infection at high density

Yitzchak Shmalo

The one-spin facilitated Fredrickson-Andersen model (FA-1f) on Z, with equilibrium density q of infected
sites, is considered out of equilibrium. For q > 1/2 the paper proves that, for every initial law nu and
every local function f,

    |nu P_t f - pi(f)| <= ||f|| (C exp(-c t) + 2 nu(R > gamma t)),

where R is the distance from the origin to the nearest infection and C, c, gamma depend only on q and the
support of f. No independence, stationarity or uniform control of the gaps between infections is assumed.
Consequently Conjectures 1 and 2 of Martinelli, Shapira and Toninelli (Long time behaviour of one
facilitated kinetically constrained models: results and open problems, arXiv:2510.20461) hold for every
q > 1/2, including the case of a single initial infection. The proof transfers the relaxation theorem of
Blondel, Cancrini, Martinelli, Roberto and Toninelli (arXiv:1205.4584) from uniform to origin-centred
hypotheses. The paper also shows that the two extreme infections of a finite infected set move away
linearly when q > 1/2, and records, for every q, the near-equilibrium argument of Cancrini, Martinelli,
Schonmann and Toninelli with explicit constants. Both conjectures remain open for q <= 1/2.

## Contents

- `paper/main.tex`, `paper/main.pdf`: the paper.
- `code/checks.py`: a check, in floating-point arithmetic, of the generator inequality of Lemma 3.1 on every configuration of
  windows of up to twelve sites with frozen infected exterior, and an exact continuous-time simulation from a
  single infection. Pure Python 3, no dependencies. Run `python code/checks.py` from the repository root
  (under a minute).
- `data/checks.json`: the output of that script (seed 20261113).
- `SHA256SUMS`: checksums of the files above.

The checks are not part of the proof.

## License

MIT, see `LICENSE`.
