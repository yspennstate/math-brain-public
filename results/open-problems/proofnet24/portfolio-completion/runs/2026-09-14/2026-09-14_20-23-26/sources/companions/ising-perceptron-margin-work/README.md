# Ising perceptron at nonzero margin

Working repository for the margin extension of the zero-margin capacity
result in [ising-perceptron-capacity](https://github.com/yspennstate/ising-perceptron-capacity):
the storage threshold alpha_*(kappa) of the binary-weight perceptron with
constraints <w, x_a>/sqrt(N) >= kappa.

Contents:

- `km.py` - the replica-symmetric Krauth-Mezard system at general kappa
  (Ding-Sun conventions): high-precision continuation of the fixed point
  (q, psi), the zero-free-energy candidate alpha_cand(kappa), and the
  numerical content of Huang's per-point conditions (contraction,
  amp-works, local-concavity) with stationarity residuals.
- `scan_kappa.py` - continuation driver over a kappa grid; appends rows
  to `results/kappa_*.csv` as they complete.
- `huang2var.py`, `scan2var.py` - Huang's two-variable global function
  S_*(lambda_1, lambda_2) at general kappa (float64): the (1,0) anchor,
  Hessian, moment-body clearance, global grid, and far rays.
- `certify_km_slab.py`, `gen_slabs.py`, `run_batch.sh` - ball-arithmetic
  certificates of Condition km-well-defd on kappa slabs (python-flint;
  uses core.py from ising-perceptron-capacity).
- `plot_kappa.py` - figures from the continuation CSVs.
- `collect_slabs.py` - batch result collection into
  `results/certified_intervals.csv`, with contiguity checking.
- `note/margin_note.tex` - a short write-up: the stationarity and
  dR/dq identities with proofs, the curve, the condition map, and the
  certificate design.
- `NOTES.md` - derivations, anchors, design notes, and the honest
  status of every claim.

At kappa = 0 the code reproduces the certified rectangle
(alpha in [0.833078599, 0.833078600], q in [0.56394907949, 0.56394908030],
psi in [2.5763513100, 2.5763513224]) from a fresh mpmath transcription.

Current state: the capacity candidate curve and the numerical content
of Huang's conditions are computed on kappa in [-2.0, 1.5] (all hold
everywhere measured, with the fixed-tilt Hessian at the distinguished
point losing definiteness between kappa 1.15 and 1.20);
ball-arithmetic certificates cover kappa in [-0.65, 0.19] in 1680
contiguous slabs across two uniqueness lanes (the per-slab
contraction up to 0.10, Nakajima's certified premise beyond;
results/certified_intervals.csv and certified_intervals_nak.csv,
worker evidence under results/box/), discharging his fixed-point
condition verbatim together with the AMP and local-concavity
conditions, with alpha_*(kappa) pinned per slab, tightened to ~2e-6
intervals at five margins by certified bisection, and the fixed-tilt
Hessian at the distinguished point certified at six margins
(kappa = 0, both signs of 0.05, 0.0995, -0.45, and 0.13 past the
product bound's reach).  The global two-variable condition is
certified at kappa = 0.05 through the located-box port of the
zero-margin architecture (huang_cert_*.py; Region II, Region I from
the symbolic maximizer, the manifest-driven stage 2, and the star
interior; AUDIT.md maps every algorithm to its code).  A paper
covering all of this is in paper/; the curated public artifact it
cites is assembled by build_release.py into
github.com/yspennstate/ising-perceptron-margin.  NOTES.md carries the
derivations and the precise status of each claim; note/margin_note.pdf
is the earlier short write-up.

