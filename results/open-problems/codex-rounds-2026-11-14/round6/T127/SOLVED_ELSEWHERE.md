# Reported outside solution

mt0-svg, *The frog model is recurrent on the 3-ary tree and transient on
the 4-ary tree*, version v2.0.0, 4 October 2026.

- [Paper source](https://raw.githubusercontent.com/mt0-svg/frog-model-tree/main/paper/main.tex)
- [Statement map](https://raw.githubusercontent.com/mt0-svg/frog-model-tree/main/STATEMENTS.md)
- [Release](https://github.com/mt0-svg/frog-model-tree/releases/tag/v2.0.0)
- DOI given by the source: [10.5281/zenodo.23121586](https://doi.org/10.5281/zenodo.23121586).

ArXiv id: none identified. Attribution follows CITATION.cff; no personal
name is inferred. Both the paper and statement map were actually opened
in this session. The pinned formal-source commit used for the audit is
`d6b298c0100af57a8f46f8314eca8bf8f7eb4693`.

The claimed theorems are almost-sure recurrence for d=3 and almost-sure
transience for d=4, with mean root visits after time zero at most 5.756
in the latter case. The definitions match T127, subject to the harmless
root-frog convention proved in PROOF.md.

Verification here: the earlier model audit holds; the d=3 target's
certificate boundary and final arithmetic were inspected. An independent
second-moment proof gives a sharper bound on the planted infinite-frog
event, conditional on the outside linear mean estimate. Neither the
release certificates nor the entire imported proof were replayed.
This records a claimed solution, not independent certification of it.

The source release metadata and input manifests agree on their shared
digests. The actual binary input bytes could not be retrieved. A source
or metadata match must not be represented as a certificate PASS.
