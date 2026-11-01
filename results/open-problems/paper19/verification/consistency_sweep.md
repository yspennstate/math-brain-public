# Document-level consistency/completeness sweep (read-only critic, 2026-06-27)

Manuscript was being edited live during the sweep; re-run a final label/ref audit after the
build freezes. Good news first: all `\ref/\eqref/\cite` resolve, no duplicate labels, no
Toeplitz/structured-symbol scope drift, and cross-section constants reconcile (e_k=d_F k^2,
h(gamma) expansions, all h/d_F bases).

## HIGH
1. **Missing Balan--Wang / phase-retrieval citations.** `parts/phaseretrieval.tex` invokes the
   Balan--Wang result and the complement-property / full-spark reduction
   `omega(A)=min_T smin(A_T)` with NO `\cite`. `BalanWang2015`,
   `BandeiraCahillMixonNelson2014`, `ConcaEdidinHeringVinzant2015` are in refs.bib but unused.
   FIX: cite them at the reduction and at first use of "Balan--Wang"/"full spark"/"complement
   property". (Owner's file — flagged for the user.)
2. **`lem:two-proj` is a proof sketch deferred to `notes/IIB_lemma_2D.md`.** For a standalone
   paper the load-bearing pair-correlation lemma should have its full proof in-text (appendix)
   or be softened. STATE marks it PROVED; the in-paper text is a sketch ending "routine ...
   [Petrov1975]". FIX: add an appendix with the full argument, or state explicitly that the
   complete proof is a companion note. (Lead's lemma.)

## MED
3. **Excess index clash `k` vs `r`.** geometric.tex rectangular subsection uses `k` for fixed
   excess (M_m^{(k)}), but `r` is used in cor:rect:finite-entropy, ensembles.tex, and STATE; and
   `k` is also the singular-value index in the next subsection (M_m[k], e_k). FIX: use `r` for
   excess everywhere, reserve `k` for the SV index.
4. **`\rho` overloaded** = density-growth rate (`limsup m^{-1}log K_m`) AND normal-overlap
   `<u,v>`, both in universality.tex. FIX (lead): rename the overlap to `\varrho` in lem:two-proj,
   rem:pc-reduction, and prob:pc. [BEING FIXED NOW by lead.]
5. **`L_m` overloaded** = entropy budget `log binom(N_m,m)` and binomial trial count in
   cor:poisson-thinning(2) `Bin(L_m,p_m)`. FIX: rename the trial count.
6. **Abstract omits the cleanest PROVEN new result.** prop:sign-critical / cor:rademacher-pr-fail
   (every sign frame at N>=2m-1 fails full spark, deterministic) is unconditional but not in the
   abstract/intro. FIX: add one clause.

## LOW
7. One-matrix s_min prefactor stated as `m^{d_F+1}` (prop:bd-tail) vs `m^{1+d_F/2}`
   (ldp:one-matrix, rect:tall-tail at p=1). Both valid; harmonize or note.
8. Smoothing parameter `alpha` (STATE) vs `eta` (manuscript cor:smoothed-lower). Harmonize.
9. Run one final `\ref`/label/line audit after edits settle.

## Lead disposition
- Item 4 (the `\rho` clash) was introduced by the lead's lem:two-proj edit; fixing now (-> `\varrho`).
- Items 1,3,5,6,7,8 are in the user's sections; recorded here for the user / a later coordinated pass.
- Item 2: the full 489-line proof is in notes/IIB_lemma_2D.md and was adversarially verified
  SOUND (one fixable t->0 quantifier, already corrected). Promote to an appendix in a later pass.
