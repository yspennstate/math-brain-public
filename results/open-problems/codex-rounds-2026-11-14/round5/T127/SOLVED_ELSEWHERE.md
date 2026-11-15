# Outside solution and verification status

mt0-svg, *The frog model is recurrent on the 3-ary tree and transient on
the 4-ary tree*, v2.0.0, 4 October 2026. The opened CITATION.cff gives
DOI [10.5281/zenodo.23121586](https://doi.org/10.5281/zenodo.23121586).
The Zenodo record itself could not be opened. No arXiv id was identified;
no claim is made that none exists. The paper's author field is an account
email; the citation file explicitly credits mt0-svg. No personal name is known.

The [paper](https://github.com/mt0-svg/frog-model-tree/blob/d6b298c0100af57a8f46f8314eca8bf8f7eb4693/paper/main.tex)
claims almost-sure recurrence for d=3 and transience for d=4 with one active
root frog, one sleeper at each other vertex, and independent simple random
walks. Its d=4 mean bound is 5.756 visits after time zero.

New beyond round 4: the [formal model](https://github.com/mt0-svg/frog-model-tree/blob/d6b298c0100af57a8f46f8314eca8bf8f7eb4693/FrogModel/Defs.lean),
[recurrence predicate](https://github.com/mt0-svg/frog-model-tree/blob/d6b298c0100af57a8f46f8314eca8bf8f7eb4693/FrogModel/D3/Defs.lean),
[d=4 target](https://github.com/mt0-svg/frog-model-tree/blob/d6b298c0100af57a8f46f8314eca8bf8f7eb4693/FrogModel/Solution.lean)
and [d=3 target](https://github.com/mt0-svg/frog-model-tree/blob/d6b298c0100af57a8f46f8314eca8bf8f7eb4693/FrogModel/SolutionRecurrent.lean)
were retrieved through the GitHub connector and saved locally. Their model
definitions have been checked for applicability, including the additional
root-sleeper convention; see PROOF.md. The corresponding frozen challenge
definitions agree in the text checks in audit_sources.py.

The fixed commit is d6b298c0100af57a8f46f8314eca8bf8f7eb4693. Fourteen
retrieved files have checked Git blob identities in outside_manifest.json.
ASSETS.md identifies the three required compressed certificate inputs and
their SHA-256 hashes, but those inputs have not been downloaded or checked.
Historical comparator and nanoda outputs are also archived; these are
source reports rather than independently reproduced checks.

Status: applicable outside solution claimed, with formal definitions now
inspected. Complete proof and certificates have not been independently
verified here. The task's literature branch ends further original-model
research in this session; the report uses PARTIAL to preserve that limit.
