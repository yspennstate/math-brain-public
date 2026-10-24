# Audit 1: source scope, hypotheses, and attribution

**Outcome: scope check passed after bibliographic corrections. Publication novelty remains unverified.**

This is the first of five separate review passes by the same assistant. It is not an independent referee report. The reviewed claim is Theorem 2.1 and Corollary 2.2, not the neighboring positive-boundary-mean problem.

## Source question and version control

The zero-radius question is Problem 19.41 on page 228 of the published survey, and Problem 18.40 on page 122 of the December 2011 preprint. The neighboring positive-mean question is 19.40 in the journal and 18.39 in the preprint. The prior draft mixed the journal bibliographic entry with preprint locators. The final manuscript now gives separate references for the journal article and preprint and explicitly identifies both question numbers. The root identity is cited to the preprint's Lemma 14.7 rather than attaching that locator ambiguously to the journal entry.

The original arXiv PDF was read and its question page visually inspected. The journal numbering was cross-checked against a reproduction of the published text. Direct publisher PDF retrieval did not succeed during this pass. This access limitation does not concern the directly inspected preprint question, but it is recorded rather than described as a successful publisher-PDF check.

Primary source: S. Janson, *Simply generated trees, conditioned Galton--Watson trees, random allocations and condensation*, Probability Surveys 9 (2012), 103--252, doi:10.1214/11-PS188; arXiv:1112.0510v1. The related paper by Janson, Jonsson and Stefansson, arXiv:1104.2810, was checked for its actual theorem scope: its ratio-growth local-limit theorem and explicit factorial-family results do not have the general hypotheses of the current theorem. Its branching-weight indexing differs from allocation outdegree indexing; no factorial constant is transferred without that shift.

## Logical comparison with the problem

The weights are one fixed sequence of finite nonnegative numbers, with positive constant term and zero radius. The mass path is prescribed, with eventual admissibility and positive finite limiting density. There is no regularity requirement on its increments. These assumptions are retained, not strengthened to full support or ratio growth.

The claimed subsequence conclusion $Y_{(1)}/m\to1$ implies $Y_{(1)}/n\to\lambda>0$ on that subsequence. This contradicts full-sequence convergence to zero and therefore answers the entire zero-radius question, provided the argument is correct. A subsequence conclusion is sufficient for the source question; it is not a scope defect. By contrast, the argument neither proves condensation at every size nor proves literal concentration on one occupied box.

The identification of the source's nontrivial $\nu=0$ regime with zero radius was checked directly: if the radius were positive and any positive index had positive weight, the logarithmic-derivative mean at a positive argument would already be positive. A sequence supported only at zero cannot support the stated positive-density path.

## Attribution and remaining limitations

The cyclic lemma and size-biased root identity are identified as known. The source's sparse-factorial example is used only to explain why a full-sequence near-total result would be false. The manuscript does not claim to settle the positive-mean question, establish a rate uniform in the weights, or prove a universal result on an arbitrarily lacunary sampled set.

Bounded current-literature searches were conducted, but the returned material did not establish publication priority. The paper must not be announced as a independently verified new resolution on that basis. The author's affiliation, email, general funding wording, and competing-interest declaration were recovered from his existing repository manuscripts; the applicability of individual grants to a submission remains an author responsibility. No personal mathematical contributor or discussion was invented.
