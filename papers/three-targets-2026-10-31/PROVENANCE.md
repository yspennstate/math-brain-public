# Contribution history and public-edition changes

This release consolidates the three completed manuscripts supplied on 31 October 2026. It does not count their earlier project versions as additional solved problems or reassign discovery credit.

## Contribution history

- **T067:** the principal construction is the three-state posterior cone and exact global pair certificates, yielding the arbitrary finite-mean observed Galton-Watson extension. The published Formentin-Kulske conjecture, Mossel-Sly-Sohn results, earlier OpenAI regular/Poisson results, and the earlier four-state cone are cited in the paper. The four-state verification material is retained with its original attribution and license. The consolidated version makes the iid child-order convention in the pruning proof explicit.
- **T228:** the manuscript builds on earlier author-directed Math Brain work. The forward tilted-walk, overshoot and stationary last-exit positivity mechanism was supplied by a project Claude agent; the subsequent continuation verified the nonzero-teacher law and developed the consolidated moment statements. The paper contains that complete argument and preserves this attribution. The probability tools themselves have prior literature.
- **T357:** the manuscript combines the finite-time proof package of 24 October 2026 with its later strongly overparameterized continuation. Theorem D and Appendix F contain that extension. The reused-data GD trajectory and stopping-time conclusions are stated separately from the prior random-feature calibration and AMP inputs.

The papers retain their supplied authorship, affiliation, funding, competing-interest and AI-assistance declarations. This release does not independently reverify the underlying nonmathematical declarations.

## Changes in this public edition

1. Added citations inside each paper to the public Math Brain repository and the paper's own public archive and PDF.
2. Added the missing critical-moment reference: D. Buraczewski, E. Damek and J. Zienkiewicz, *On the Kesten-Goldie constant*, Journal of Difference Equations and Applications 22(11), 1646-1662 (2016), DOI [10.1080/10236198.2016.1234613](https://doi.org/10.1080/10236198.2016.1234613). This is distinct from the four-author 2016 perpetuity paper already cited in T228. The direct proof for this SGD model does not imply exclusive priority for the formula.
3. Corrected one malformed sentence in T357 Appendix F and changed its introduction to finished-result wording.
4. Made source-availability statements and supplement paths refer to the self-contained public package. Internal working-file identifiers were replaced by contribution descriptions while preserving attribution.
5. Replayed T067's complete three-state coefficient check and recorded the ten T228 rational checks. A targeted independent final-source review found no material proof blocker within the reviewed scope.

The new bibliography and availability text do not alter the mathematical hypotheses or conclusions. File hashes in `MANIFEST.json` identify this exact public edition. The released verification log abbreviates an ephemeral working-directory prefix; its mathematical output is unchanged. Build logs and temporary typesetting files are not part of the release.
