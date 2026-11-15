VERDICT: PARTIAL independently checked the planted-count bridge and strengthened its conditional probability bound to 9/400

The round 5 source/model audit holds. A new independent script checks its
14 saved blob identities, the 13 and 12 shared model definitions in the
two challenges, the recurrence predicate and the uniform walk law. The
additional-root-frog argument also survives a fresh pathwise derivation.

The new mathematical piece is a quantitative second-moment criterion for
the planted model. If Z_m<=X, Z_m<=U_m and E Z_m>=c m along unbounded
heights, PROOF.md proves P(X=infinity)>=d^2 c^2. It retains the degree
factor in the all-awake mean and takes the asymptotic second-moment bound.
Two derivations give the same constant. With the outside d=3 linear
estimate this yields 9/400, compared with the paper's 1/9600 at c=1/20.
This application remains conditional on that estimate. No novelty claim
is made for the general second-moment inequality.

The outside classification remains a claim of recurrence for d=3 and
transience for d=4; SOLVED_ELSEWHERE.md gives the reference. The literature
check ended within five minutes. No new diluted-model computation or
independent q=1 classification was attempted under the stopping branch.

The source audit now follows the d=3 target into the certificate assembly,
including coverage and state-shape requirements, the postfixed terminal
inequality and the planted criterion actually used. Its exact terminal
conversion holds:
`(1-7045771/88917100)*(1778342/3)=27290443/50`.
The planted mean ratio uses the correct index: for m>=1778251 the imported
estimates would give E Z_m>=(m+6)/20. The proof of positive probability
does not assume independence or monotonicity of Z_m.

Reproduce the finite checks:
```
OMP_NUM_THREADS=1 nice -n 15 python3 audit_bridge.py > audit_bridge_output.txt 2>&1
```
Exit 0, about 0.11 seconds on the first run, peak RSS 22446080 bytes.
The sandbox denied the requested nice adjustment. All calculations were
tiny and single-threaded; no heavy build was launched. Final-run resource
output is saved in audit_bridge_output.txt.

Twenty pinned source records are saved in source_archive.json and
criterion_sources.json. Their blob hashes match. Sixteen Lean source files
were scanned for executable sorry/axiom/native_decide tokens; their full
imports were not checked. The 1539-entry chain and 26-entry run manifests
agree on the shared top-mass input. Three release-input digest metadata
entries agree with ASSETS.md. None of these checks is a Lean proof check
or a hash of freshly downloaded binary assets.

What failed: generated CertData/Main.lean is absent from the source tree,
as expected from the generator; it must be reconstructed from release
inputs. The connector does not support binary downloads, and the shell
fallback failed to resolve github.com. An initial log-append patch used
the wrong context line; it made no change and was corrected. No certificate
run, Lean build or comparator replay was performed.

Uncertainty: correctness of the imported linear estimate, its data and
checkers, the implication from the planted event to original-model
recurrence, and the complete d=4 proof remain unaudited here. The proved
second-moment statement does not remove those dependencies.

Next worker: obtain the two d=3 binary inputs using the exact digests in
release_metadata.json, verify the shared mass input, and check a bounded
portion of the seed/chain certificate with its coverage conditions. The
source records now locate the certificate boundary; another retrieval-only
paper/model session is unnecessary. Do not rerun the full historical
comparator under the present resource limits.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, approximately 11:02 Asia/Tbilisi.
