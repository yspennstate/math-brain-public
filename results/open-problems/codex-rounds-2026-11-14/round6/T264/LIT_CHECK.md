# T264 literature check and write-up judgement (an agent, 15 Nov 2026)

Two web searches were run on 15 Nov 2026 for minimum-norm ReLU interpolation with noisy labels in input dimension 2 or more.
- Joshi, Vardi, Srebro, arXiv:2307.15396 (ICLR 2024), d = 1: tempered with high probability for L1, catastrophic for L2 or in
  expectation over the sample. Close pairs of points with opposite labels drive the expectation; this is the same
  mechanism as our hemisphere result.
- "Harmful overfitting in Sobolev spaces", arXiv:2602.00825 (Jan 2026): any interpolant within a constant factor of
  the minimal Sobolev norm keeps a persistent excess risk. Not read in full yet. It is about Sobolev spaces, not the
  ReLU variation norm, but it must be read before any claim of novelty in d >= 2.
- arXiv:2609.33675 (min-l_p linear) and arXiv:2602.13910 (deep ReLU stability) do not address this question.
- No paper found on the multivariate min-norm ReLU case.

Judgement: not a paper yet. Rounds 3 to 5 show that one close opposite-label pair forces infinite expected risk in d = 2, 3.
Round 6 shows that two further antipodal constraints cancel it, with exact limit [1+(A^2+B^2)/2]/d.
Both are deterministic configurations, and neither says what happens for an iid sample of size n.
A note would be the d >= 2 analogue of the "catastrophic in expectation" half of Joshi-Vardi-Srebro, and only if the
infinite-expectation statement holds for iid samples, i.e. the close pair survives the other n - 2 points with positive
probability. That is the next brief for this problem; round 6 shows it is not automatic.
Before writing, read 2602.00825 and the papers citing 2307.15396.

Update 15 Nov 2026 (an agent), abstract of arXiv:2602.00825 read on arxiv.org: K. Karhadkar, A. Sietsema,
D. Needell, G. Montufar, "Harmful Overfitting in Sobolev Spaces" (31 Jan 2026). For W^{k,p}(R^d), p in [1, inf), under
label noise and regularity of the data law, approximately norm-minimizing interpolators keep generalization error
bounded below by a positive constant with high probability as n -> inf. The proof finds harmful neighbourhoods of the
training points through Sobolev inequalities. It does not cover the two-layer ReLU representation cost, which is the
Radon-domain R-norm of Ongie, Willett, Soudry and Srebro, not a classical Sobolev norm. So T264 (d >= 2) stays open.
One extended web search the same day found no multivariate min-norm ReLU result; everything returned was d = 1.
Next step (round 7 brief, NEXT_BRIEF_R7.md): carry the harmful-neighbourhood argument over to the R-norm for a
"not benign" lower bound, and settle whether a close opposite-label pair survives an iid sample with positive probability.
Correction, same day: the round 5 result (copied in round 6's PROMPT.md) already covers iid samples. E[R_n] = infinity
for every n >= 3 in d = 2, 3, from a hemisphere event of probability 2^(3-n). So the "catastrophic in expectation"
analogue of Joshi-Vardi-Srebro in d = 2, 3 is proved, and it is a write-up candidate now, rounds 5 and 6 together.
The judgement above ("neither says what happens for an iid sample") was wrong.
