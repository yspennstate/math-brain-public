VERDICT: PARTIAL local bond-direction defects separate arbitrarily filled strips between two fixed orientations

The round-5 occupation result holds. Its geometric estimate was re-derived, its four-square constant independently checked by a fine rational interval and an integer comparison, and its unchanged audit rerun from a copy in this folder.

The new result answers its proposed geometric test positively for an explicit local detector. Let a diameter-one packing agree outside a bounded vertical strip with triangular crystals of spacing 101/100, orientations 0 and pi/6, arbitrary relative phases, and arbitrary particle displacements below 1/400. Fill the strip arbitrarily, subject only to exclusion. On unit-grid anchors, define good windows using short bonds of length at most 11/10 and angular tolerance arcsin(1/100) around the two respective six-direction families. The detector observes radius 31/10 and also requires central occupancy and existence of short bonds.

**Defective anchors necessarily have an eight-neighbor crossing of every finite-height strip rectangle, and one defective component is unbounded in both vertical directions.** Every crossing spanning h rows has at least h anchors. The proof shares a bond between nearby good windows to exclude opposite labels, then uses planar boundary parity to force a separator. It makes no vacancy assumption.

For the round-5 construction, including every admissible addition of centers inside its strip of half-width 203/400, the separator lies among the seven columns -3 through 3. Every square of side four still contains at least three centers. Thus these direction defects are detected even when the earlier occupation detector detects nothing.

The definition tests two prescribed orientation families. An intermediate, perfectly triangular orientation can be defective under this definition. The result does not count dislocation cores or prove a Gibbs cost, orientational surface tension, symmetry breaking, or freezing. T080 remains open. Novelty of this elementary separator argument is not established.

Reproduce:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 prior_recheck/verify.py > prior_recheck/VERIFY_OUTPUT.txt 2>&1
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify.py > VERIFY_OUTPUT.txt 2>&1
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_artifacts.py > ARTIFACT_AUDIT.txt 2>&1
```

The new audit checked exact constants and all 26,487 assignments on three small label rectangles. All 482 assignments satisfying the hypotheses had an eight-neighbor defect crossing; independent row transfer counts and a separate interface graph agreed. Three supporting floating-point jittered interfaces allowed 11,11,14 added strip centers and each retained a crossing. The final run took 0.378 seconds and peaked at 15.422 MiB RSS; the copied prior audit took 1.132 seconds at 15.359 MiB. Actual nice priority was 20. Complete output, independent derivations, and negative controls are in LOG.md; results are in verification.json.

What failed: a stronger face-connected separator assertion is false. An explicit diagonal example and 188 legal enumerated cases detect this. Omitting central occupancy or short-bond existence also invalidates label exclusivity. No mathematical audit failed. The nice wrapper warning came from inherited lower priority.

The bounded literature check found no later Euclidean solution. Opened primary sources were Lewis Bowen, Marcus Michelen, Will Perkins, *A phase transition for the hard sphere model on the hyperbolic plane*, [arXiv:2607.23873](https://arxiv.org/abs/2607.23873), and Andreas Göbel, Matthew Jenssen, Marcus Michelen, Marcus Pappik, Will Perkins, Leon Schiller, *Uniqueness, analyticity and mixing for Gibbs point processes via spectral gaps*, [arXiv:2606.28009](https://arxiv.org/abs/2606.28009). They concern a hyperbolic transition and improved uniqueness bounds. This search was not exhaustive.

Next worker: test whether this fixed-family defect event admits any useful conditional partition-function suppression estimate, with all particle positions integrated and a common exterior. Include densely occupied intermediate-angle crystalline windows as a negative control; neither low occupation nor independent defect probabilities is available. If this detector is too broad for such a bound, introduce a continuous local orientation and seek a quantitative cost for its cumulative change. The present result supplies only the geometric separator.

Task: “take the NEXT checkable step on this problem, building on that work” — 2026-11-15, first retained clock 10:36:07 Asia/Tbilisi; exact receipt time unavailable.
