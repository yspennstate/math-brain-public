# R27 verification - spherical radial transfer

Date: 2026-06-28.

## Scope

This round used exactly five tool-managed review agents:

1. `019f0c90-a00d-7ac3-828e-f86039f6f41c` audited the existing rotationally
   invariant second-moment theorem and found it unsafe as written: the complex
   marginal density scaling was wrong, the planar-density proof treated a
   finite spherical projection as an exact Gaussian mixture, and the
   exponentially small two-slab estimate was not proved.
2. `019f0c90-b48a-7ed3-9136-a30dde428100` proposed the safer transfer theorem
   for spherical directions with subexponential radial weights.
3. `019f0c90-c9ce-7432-8491-1c8fa6f33234` audited labels and integration,
   confirming that `parts/rotinv_universality.tex` is already included after
   `parts/ensembles.tex`.
4. `019f0c90-db91-7010-8262-4f465c911541` audited row/column normalization and
   phase-retrieval transfer proofs, finding no fatal issue and suggesting
   explicit null-event clauses.
5. `019f0c90-ed67-74d2-9b5f-4cbdac5a39c7` recommended no Lean formalization for
   the probabilistic radial theorem; the deterministic diagonal singular-value
   sandwich is the only lightweight future Lean target.

No terminal-launched agents, background daemons, or scheduled tasks were
created.

## Main changes

1. Replaced the included rotationally invariant second-moment theorem with the
   proved transfer theorem `thm:rot-inv-univ`.  If
   \(A_m=D_m^{\rm rad}\Theta_m\), the rows of \(\Theta_m\) are iid uniform on
   the unit sphere, \(m^{-1}\log b_m\to\alpha\), and
   \[
     \max_i\left|\log(r_{im}/b_m)\right|=o_\PP(m),
   \]
   then
   \[
     m^{-1}\log\min_{|T|=m}\smin((A_m)_T)
     \to \alpha-h(\gamma)/d_\F
   \]
   in probability.
2. Added the iid rotationally invariant controlled-radii corollary
   `cor:rot-controlled-radii`, with the checkable sufficient condition
   \(N_m\PP\{|\log(R_{1m}/b_m)|>\varepsilon m\}\to0\).
3. Kept the spherical critical-frame corollary `cor:spherical-pr`, now proved
   from radial transfer rather than the unsupported two-slab argument.
4. Removed the leftover quaternionic upper-side theorem that depended on the
   same unsafe second-moment outline.  Quaternionic Gaussian remains a
   conjectural division-algebra item in the ledger.
5. Revised `prob:radial-mixture`: ordinary non-degenerate radial mixtures with
   subexponential sampled extrema do not shift the exponential base; the open
   problem is the genuinely exponential radial-extreme regime.
6. Added null-event clauses to the row-normalized and column-normalized
   Gaussian transfer proofs, and added a phase-retrieval cross-reference to
   spherical rows of radius \(e^{o(m)}\).
7. Marked `notes/rotinv_universality.tex` as a superseded historical draft so
   future searches do not treat its duplicate old labels as current.

## Verification

Standalone build:

```text
pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex
pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex
```

Both passes exited 0.  The final standalone PDF has:

```text
paper19/extremal_hard_edge.pdf
42 pages, 630691 bytes
```

The cleanup scan found no remaining manuscript/ledger references to the old
unsafe labels or claims:

```text
thm:quaternion-univ, lem:rot-marginal, lem:planar, eq:rot-marg,
radially-concentrated, two-slab constant, kappa_m, kappa_inf
```

No Lean files were changed in this round.
