# Second-chain challenge

## Candidate frozen

Target packet `A023`; source claim version
`B05_A023_NEGATIVE_DEFECT_*_v1`; source commit
`9a6f9a8eeb3795ebdbeebf4efa767ed607af2897`.

The challenge separated four links:

1. exact point-defect spectrum and physical influence;
2. half-activation normalization and selector influence;
3. arbitrary nonstationary rank/depth induction;
4. restriction-tree telescope and terminal-factor cancellation.

## Hard regimes selected independently

- rank `r=2`, where the bias is smallest and the defect ratio has an endpoint;
- rank `r=4`, where the exact defect ratio is maximal numerically;
- ranks tending to infinity, where the bias tends to `-1` and defect influence
  vanishes;
- alternating ranks `(large,2,large,2,...)`, which drive the scalar argument
  toward its lower endpoint `s=1/8`;
- arbitrary three-bit Boolean seeds, including constant, dictator, parity,
  and asymmetric seeds;
- adaptive/pruned trees in which the queried coordinate depends on the branch;
- both no terminal factor and a nontrivial disjoint two-bit factor.

## Findings

- The squared spectrum of `N_r` and formulas for `U(N_r),I(N_r)` are exact.
- The selector term is `(1+s)/2`, not `(1-s)/2`, because the activation input
  mean is `-s`; this favorable sign is used correctly.
- The invariant `m in [1/4,1/2]` is valid for arbitrary rank changes, giving
  `s in [1/8,1/2]` at every post-first level.
- The source's `16/9` induction closes with slack.  A complete analytic
  strengthening to `5/3` is recorded separately.
- The tree argument is reveal-order independent because it is an algebraic
  root-minus-leaf telescope.  It does not imply nodewise positivity or
  first-revelation credit ownership.

## Verdict

The original formal claims are accepted without repair.  The stronger `5/3`
claim is contributor-produced and therefore pending a fresh uninvolved review.
