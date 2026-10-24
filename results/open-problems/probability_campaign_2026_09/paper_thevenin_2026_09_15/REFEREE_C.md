# Referee C (Claude Opus 5, 2026-09-15): novelty, prior art, framing and exposition

Brief: is the result new, is the paper fair to Thevenin, and does it read as a professional mathematics paper.
(This file quotes the banned tell-words as a checklist, so it carries the token voice-ok.)

## Prior art

Searches on arXiv, Google Scholar and the open web, on the conjecture itself, on degree counts in conditioned
Galton-Watson trees, on condensation, and on the citing literature of Thevenin's paper, 2018 to 2026.

| Work | What it does | Why it is not this |
|---|---|---|
| Thevenin, EJP 25 (2020), arXiv:1812.07365, Section 6.2 | Theorem 6.7 (subcritical power law) and the closing conjecture | The target of this paper |
| Janson, Probab. Surv. 9 (2012), Problem 20.2 | Asks the three questions | Open questions, no answers |
| Kolchin, Random Mappings, Theorem 2.3.1 | Degree-count CLT for critical laws of finite variance, variance pi_d(1 - pi_d - (d-1)^2 pi_d/sigma^2) | The case the conjecture extends from |
| Armendariz-Loulakis, SPA 121 (2011), arXiv:0912.1516 | For subexponential laws, removing the largest coordinate leaves an asymptotically i.i.d. sample | The step Thevenin's proof uses; the examples here break it |
| Rakotoniaina-Ralaivaosaona, arXiv:2603.08076 (March 2026) | Asymptotic normality for general subtree counts in CRITICAL trees under E xi^{2 Delta(t)+1} < infinity; two counterexamples (Examples 11 and 12) when it fails | Different statistic (subtree counts, not degree counts); the failure is that Var is no longer of order n, so the scaling is wrong; no condensation, no subcritical case; Thevenin is not in its bibliography |
| Janson, ECP 26 (2021), arXiv:2011.04224 | Fringe and general subtree counts, critical, finite variance, no further moment condition | Positive result, different statistic |
| Dan, arXiv:2607.14792 (July 2026) | Trees conditioned on n vertices AND k_n = o(n) leaves; outdegrees, Poisson limits at critical scales | A different conditioning; not the conjecture |
| Poudevigne-Thevenin, arXiv:2503.11501 (2025) | Critical tiltings and local limits of multitype trees | Different objects |
| Kortchemski, AIHP 51 (2015); Jonsson-Stefansson (2011); Abraham-Delmas (2014) | Condensation and local limits for non-generic trees | Structure of the tree, not fluctuations of degree counts |

I found no published or preprint refutation or modification of Thevenin's conjecture, and no earlier example of a
non-Gaussian limit for degree counts of a conditioned Galton-Watson tree at the conjectured centering and scale.
The two theorems appear to be new. Priority is not certified: a negative search result is not proof of novelty.

The nearest thing in the literature is Rakotoniaina-Ralaivaosaona, and the distinction is worth keeping sharp,
because it is the stronger form of refutation that makes this paper interesting. Their failure is a failure of
normalisation: the variance of the count stops being linear in n, so nothing converges at scale sqrt n. Here the
centering n mu_A and the scale sqrt n of the conjecture are exactly right, the normalised counts are tight, the
limit along n_r exists, and it simply is not Gaussian. The paper now says this, and cites both papers.

## Framing

The conjecture is stated loosely ("We believe that these conclusions should hold ..."), and the paper should not
and does not present this as the fall of a famous conjecture. Checks:

- The abstract and the introduction both say the conclusions fail "in general" and never claim Theorem 6.7 is
  affected. Correct: the lacunary laws are asymptotic to no positive power law.
- The paper now records the conjecture's own first sentence, that the conclusions are known for critical laws in
  the domain of attraction of a stable law and for subcritical power laws, and states that the critical law of
  Theorem 1.2 is in no such domain. Without that sentence a reader could think the paper contradicts something
  already proved. This was the most important framing fix.
- Section 6 offers the regularity hypothesis that the argument suggests, as a question and not as a theorem, and
  it is the right shape: local constancy of the tail on windows of width sqrt k is what makes the
  Armendariz-Loulakis description available at resolution sqrt n. It holds for regularly varying tails and fails
  for these laws. Well posed.
- The claim about Janson's Problem 20.2 was overstated and is now exact (see Referee B, items B1 and B2). The
  paper now also notes that Theorem 1.1 bears on the third question of that problem, which it does.
- The observation that 3/16 = pi_1(1 - pi_1) is exactly the conjectured variance, so that only the means are
  wrong, is worth the sentence it now gets; likewise that Kolchin's correction term vanishes as sigma^2 grows,
  which is why the conjecture predicts pi_d(1 - pi_d) for infinite variance.

Nothing else in the paper asserts more than it proves. The numerical statements in Section 5 are labelled as
computations and each is reproducible from the script.

## Exposition and voice

- Process narrative: none. Grep for the banned forms ("first version", "earlier record", "was corrected", "we
  found no", "afterwards", "before inclusion", "session", "the companion script", "we do not know") returns only
  the AI declaration, which is where the process is permitted to be named.
- No machine tells of the kind the house rules ban (the words headline, delve, remarkably, strikingly, notably),
  no emoji, no bold-fests.
- The one overclaim of the finite-size kind, "with probability tending to one" for the 0.02 sqrt n window, is now
  "tending to a limit above 1 - 2 x 10^{-6}", which is what the mixture actually gives.
- Notation is consistent: q = pi_1 is fixed once; N = n - 1 is introduced where it is used; eps is the sign of
  the large atom throughout Section 3 and the accuracy parameter eps_r throughout Section 4, which are different
  sections and different alphabets in print, but a reader could stumble. Acceptable; a footnote is not worth it.
- xi was introduced with law mu in the introduction and then used for pi in both theorems. Fixed: both theorems
  now say "let xi have law pi".
- The Lean paragraph now describes exactly what the file proves. It claimed "integrality of the atoms" in
  general; the file certifies stages 1 and 2 (`stage_one`, `stage_two`) and not the induction, so the paragraph
  now says "the atoms of the first two stages". The other items listed are formalised in the generality claimed,
  and the build log shows every theorem depending only on propext, Classical.choice and Quot.sound.
- The figure caption matches results.md after the rebin: two spikes of mass 0.49996 and 0.50004, standard
  deviation 0.0042 = sqrt(1.7284e-5). Correct.
- The declarations read as disclosures. The AI declaration was factually wrong, claiming three adversarial
  reviews by one model; it now names the systems that did the work and says every claim was re-derived in
  adversarial review, which is what happened.
- Title: a noun phrase, no colon explainer. Abstract: one paragraph, no list. Both fine.

## Verdict

The two counterexamples are new as far as this search reaches, and the refutation is of the sharp kind (right
centering, right scale, non-Gaussian limit) rather than a failure of normalisation. The framing was too strong in
three places and is now accurate. The exposition is clean. Recommend publication as a short note, in a venue of
the size of Electronic Communications in Probability.
