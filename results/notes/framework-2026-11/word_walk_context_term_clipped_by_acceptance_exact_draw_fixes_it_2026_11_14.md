---
name: word_walk_context_term_clipped_by_acceptance_exact_draw_fixes_it_2026_11_14
description: "Why a page-context term barely moved a short Metropolis walk's offers: the acceptance min(1, ratio) clips at 1, so a much better-fitting neighbour is taken no more often than an acceptable one, and in 1-5 steps a median of about 0.17 of the log-context weight reached the offers. Drawing exactly from weight x personalised PageRank around the seed lets the context act in full. Two side results: per-row tempering of a plot planner is undone by row normalisation, and two judges agreeing at Spearman 0.2 need about ten judges for reliability 0.7."
metadata:
  type: project
  created: 2026-11-14
  status: verified
---

Three checks on the mathematics of the writing brain, each computed exactly rather than sampled.

1. The context term in a short walk. The word walk offered words by taking 1 to `steps` Metropolis-Hastings steps
(Metropolis et al. 1953; Hastings 1970) from a seed, with target pi(x) times a page-context factor ctx(x)^beta.
Computing the exact law of the first offer with the context off and on, from the same start sense, the mass on words
that fit the page moved by only +0.00 to +0.10 at 3 and 5 steps; the share of log ctx^beta that reached the offers
ranged from 0.01 to 0.77, median about 0.17.

The cause is the acceptance probability min(1, pi(y) deg(x) / (pi(x) deg(y))). Once a neighbour is acceptable at all,
it is accepted with probability 1 however much better it fits, so in a few steps the context term can reject a move
but cannot promote one. This does not mean the offers fit worse: absolute fit mass tied 4-4 with the sampler, because
the walk stays near the seed's sense.

The fix draws offers exactly from pi(x) x PPR_seed(x) over the sense states within `steps` links, where PPR_seed is
personalised PageRank with restart 0.35 (about two links; Page et al. 1999, Haveliwala 2002). With it, both the
context weight and the restart act as intended: on a harbour sentence the share of the context term reaching the
offers went from 0.12 ("walk") and 0.58 ("quiet") to 1.00, and the mass on page-fitting words for "walk" from 0.72 to
0.85. Running the walk long enough to mix (a step count from the spectral gap) is the wrong target here: the
stationary law forgets the seed, and offers should stay near it.

2. Tempering a plot planner. A planner that tempers each row of a transition matrix by beta and renormalises undoes
beta wherever a beat's choices are even. On a toy with a one-way and a four-way branch the obvious plot kept 50.0%
at beta 1, 0.5 and 0.1. Tempering whole plots instead (P^beta over complete paths, a Gibbs measure on plots that
arrive, no per-row renormalising) gives 50.0, 33.3 and 22.3%; on the example plan at beta 0.6 the top plot fell from
30.9% to 22.7% and the entropy rose from 2.84 to 3.11 bits.

3. Judges in A/B tests. Two judges agreeing at Spearman about 0.2 means one judge's reliability is about 0.2. By the
Spearman-Brown formula (Spearman 1910; Brown 1910) the mean of k judges has reliability 0.33 at k = 2, 0.56 at 5 and
0.71 at 10. So a writing A/B test needs five or more judges from two model families, same-writer pairs, and a
Bradley-Terry model (Bradley and Terry 1952) with a discrimination parameter per judge.

Not measured here: whether either fix makes better prose. That is the blind test's job, and the later blind tests
of palettes found no effect.

Related: [[word_walk_dictionary_walk_weighted_to_the_shelf_2026_11_14]],
[[story_palette_blind_test_no_effect_lean_is_length_2026_11_15]].
