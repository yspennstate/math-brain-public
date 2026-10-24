# R29 verification - spherical radial almost-sure lower envelope

Date: 2026-06-28.

## Scope

This round used exactly five tool-managed review agents:

1. `019f0c98-32e0-7752-93dd-c0bb35d7bdcd` verified that the spherical radial
   strengthening is valid as an almost-sure lower envelope, not as an exact
   almost-sure law.
2. `019f0c98-49f5-75e1-99a3-d22ee604b112` found that the general
   row-normalized Gaussian lower envelope was missing from `parts/ensembles.tex`
   and supplied the summable row-norm argument.
3. `019f0c98-6354-7be3-97c5-24690e9987bd` audited notation and ledger text,
   recommending the label `cor:rot-inv-as-lower-envelope`, the
   \(\alpha_-=\liminf m^{-1}\log b_m\) notation, and explicit no-exact-a.s.-law
   wording.
4. `019f0c98-7700-7f82-8d75-69e90c6ec8b3` adversarially audited the radial
   transfer theorem and flagged wording fixes: direction-dependent radii are
   spherical-direction, not necessarily rotationally invariant; logarithms need
   positivity off a null event; and the spherical radius should be explicitly
   deterministic positive.
5. `019f0c98-8c14-79f2-bf2b-bbbe993aee3f` recommended leaving Lean unchanged for
   this round; the radial theorem is analytic/probabilistic and the available
   small log-bound formalization would not verify the real result.

No terminal-launched agents, background daemons, or scheduled tasks were
created.

## Main changes

1. Strengthened `cor:row-normalized-gaussian` with the general almost-sure lower
   envelope
   \[
     \liminf_m m^{-1}\log\min_{|T|=m}\smin((U_m)_T)
     \ge -h(\gamma)/d_\F
   \]
   on any common coupling.  The proof uses
   \(M_m(U)\ge M_m(G)/\max_i\|(G_m)_i\|_2\), the Gaussian square lower envelope,
   and the summable bound
   \[
     \sum_m \PP\{\max_{i\le N_m}\|(G_m)_i\|_2>e^{\delta m}\}<\infty.
   \]
2. Added `cor:rot-inv-as-lower-envelope`.  If
   \(A_m=D_m^{\rm rad}\Theta_m\), \(b_m>0\) is deterministic,
   \(\alpha_-=\liminf m^{-1}\log b_m\), and
   \(\Delta_m^{\rm rad}(b_m)=o(m)\) almost surely, then
   \[
     \liminf_m m^{-1}\log\min_{|T|=m}\smin((A_m)_T)
     \ge \alpha_- - h(\gamma)/d_\F
   \]
   almost surely.
3. Added the iid-radii summability criterion:
   \[
     \sum_m N_m\,\PP\{|\log(R_{1m}/b_m)|>\varepsilon m\}<\infty
   \]
   for every \(\varepsilon>0\) implies the radial-extrema assumption.
4. Moved the spherical critical-frame almost-sure lower envelope into
   `cor:spherical-pr`, keeping it as a liminf statement only.
5. Tightened wording in `parts/rotinv_universality.tex`: direction-dependent
   radii are described as a spherical-direction extension; positivity is noted
   before taking logarithms; and the sphere radius is explicitly deterministic
   positive.
6. Updated the theorem ledger rows `A-as` and `V.B-rad`, and the roadmap entry
   for spherical-direction radial transfer.

## Verification

Standalone build:

```text
pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex
pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex
```

Both passes exited 0.  The final standalone PDF has:

```text
paper19/extremal_hard_edge.pdf
43 pages, 637166 bytes
```

No Lean files were changed in this round.
