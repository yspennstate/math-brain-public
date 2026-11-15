# Exact degree-six canonical entry via shared balanced fusion

T067-DEGREE6-UPPER-001 v1. Status: proof (unaudited). No priority claim.

For uniform-prior three-state symmetric ferromagnetic Potts broadcast on
the regular6-ary tree with eta=89/218, the canonical depth26 posterior
signal x=E||p-(1/3,1/3,1/3)||^2 is at most

  942948951491/19791209299968 < 217/4500, gap 1428392677321/2473901162496000.

Use T067-UNIVERSAL-FUSION-001 v1 on N96 with integer mass scale2^32.
There are817 posterior permutation orbits. Start with pure observations.
At every depth apply the physical edge once to the OLD child law and
upgrade it barycentrically to N96, then round down orbit masses and reveal
the root on removed mass. Form fresh independent groups of2 and4 child
experiments and fuse the2-group with the4-group. Each of these three
unit-strength fusions is followed by the same grid and mass upgrade.
The reuse of a group LAW creates independent observations conditional on
the root; it never shares an actual observation. Every intermediate law
remains calibrated and color invariant. The cited algorithm proof derives
the full Blackwell domination, including zero-weight boundary outcomes.

The physical-edge integer denominator is654 and the universal ordered
fusion denominator is995328. The latter table has667489 rows. For S=2^32,
S*654<2^64 and S^2*995328<2^128, so checked ulong one-body accumulation and
the unchanged checked128-bit packed fusion core are exact. Every removed
mass is replaced by root revelation; there is no numerical truncation.
All817 final masses sum to S, and their exact signal is recomputed by
sum_k m_k(3 sum_i k_i^2-96^2)/(S*3*96^2), giving the fraction above.

Artifact: checks/balanced_bp_fast_d6_N96_89-218.json.
Artifact SHA256: 2b0976cced31beda5ca04785b1e15ba8b1e6eca2fb2067e559704b7293303f34.
The native sources and universal table header are pinned in that artifact;
checks/balanced_bp_fast.py verifies every binary table file's hash before
running it. checks/degree6_balanced_entry26.json records the exact comparison.

Rebuild and rerun, from checks/:

  python -X utf8 universal_fusion.py
  python -X utf8 universal_fusion.py build96
  python -X utf8 validate_balanced_controls.py
  python -X utf8 balanced_bp_fast.py --degree 6 --grid 96 --eta 89/218 --steps 1 --validate --radius 217/4500
  python -X utf8 balanced_bp_fast.py --degree 6 --grid 96 --eta 89/218 --steps 90 --seconds 45 --resume --radius 217/4500

If a bounded chunk ends before26, resume the last command. Only completed
depths are checkpoints. All49 N6 ordered unit-table rows matched an
independent all-orientation Fraction implementation; all7 additional native
boundary/nonboundary control trajectories matched every row and final
mass. All N96 generated rows passed normalization and31 selected rows
matched independent Fraction derivations. The complete first N96 degree6
update matched Python, including every mass and all node roundings. A full
26-depth Python trajectory replay is pending and is not claimed here.
These are implementation checks, not replacements for source-level proof
audit. No floating-point probability or signal is used in this result.
