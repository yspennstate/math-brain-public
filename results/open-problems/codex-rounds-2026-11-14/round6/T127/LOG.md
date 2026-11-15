# T127 round 6 log

Task: “take the NEXT checkable step on this problem, building on that work.”
Started 15 November 2026, approximately 11:02 Asia/Tbilisi.

All writes remain in this directory. The specific directory restriction
excludes global mesh, checklist and brain writes, including recall commands
that record events. No git, subagents, publication or external messages.
Read the brain index and compute state: warn, owner_away_open, CPU saturated.
Only small, single-thread standard-library source checks are planned.

## Literature check (11:02–11:05)

Web queries: `frog model 3 4 ary trees recurrence transience 2026 Lean proof`
and `frog model trees Mathews 2309.14443 recurrence 2026`.
Opened the primary paper and statement map:
https://raw.githubusercontent.com/mt0-svg/frog-model-tree/main/paper/main.tex
https://raw.githubusercontent.com/mt0-svg/frog-model-tree/main/STATEMENTS.md
Also opened Christopher Hoffman, Tobias Johnson and Matthew Junge,
https://arxiv.org/abs/1404.6238 . The latter proves d=2 and d>=5;
the former claims the two missing cases. This confirms round 5's retrieval
claim, without certifying the imported proofs. No new arXiv identifier found.
The literature check ends here, within five minutes. No further research
on comparison models is undertaken under the step-1 stopping branch.

Read the predecessor reports, logs, proofs and scripts (reads continued below
where output limits require separate commands). Round 4 has no proof/script.

## Chosen check

Recheck round 5's source-identity and model claims independently. Then inspect
the d=3 assembly/certificate boundary, the specific next step requested in
its report. This is an audit of the claimed outside solution, not a new
solution of the original problem. Do not equate a saved historical PASS or
a source text comparison with a freshly checked Lean proof.

GitHub read-only fetch at the pinned commit obtained
FrogModel/D3/Assembly.lean, blob ec9c5aebbb295621254b33e403c4908ab9e3b793.
Its recurrence theorem explicitly depends on Iface.m1run_certS, which the
comment says is discharged in FrogModel/D3/Chain/Final.lean. Next inspect
that discharge and the checker, and save exact source provenance.

## Source dependency inspection

The target applies `Assembly.recurrent_three_of_m1` to
`Chain.m1run_certS_proof`. Chain/Final.lean discharges this using
`M1K.storedRun_holds`, `CertData.certS1_stored`, and `LaneD.step_sound`,
with separate seed and extension soundness results. CertData/Main.lean
returns 404 at the pinned commit because it is generated from release
data; the generator explicitly names this directory. This is expected,
not evidence of a missing proof in a completed release build.

Fetched the interface conditions, assembly, bridge, M1 run/soundness,
step-soundness theorem, generators and their module-hash manifests. The
step theorem requires every part to pass AND `covers L ps = true`, with
explicit bounds E<=64, GM<=256 and state well-formedness. The final
certificate interface requires a chain from height 100, the terminal
postfixed inequality, hn<=m1-30, E>=62 and both deficit bounds. Merely
checking a list of successful parts would not supply these conditions.

The GitHub connector exposes UTF-8 responses only, so it cannot download
binary release assets. Tried the shell fallback:
`OMP_NUM_THREADS=1 nice -n 15 curl -I -L --max-time 20 https://github.com/mt0-svg/frog-model-tree/releases/download/v2.0.0/frog-model-tree-d3-m1run.txt.xz`
Exit 6: `Could not resolve host: github.com`. The sandbox also denied nice.
No binary asset was obtained; no certificate PASS will be claimed.

Read-only release metadata supplies asset sizes and SHA-256 digests. Save
these separately and compare all three advertised input digests against
round 5's ASSETS.md. These are metadata matches, not downloaded-byte hashes.
The two module manifests allow a further consistency check: the M1 top-mass
input must be identical to input/masses100.txt of the chain certificate.

The concrete independent checks will recompute the d=3 terminal deficit
conversion and the linear-to-planted-count ratio, including thresholds,
with rational arithmetic and polynomial identities. These check the
assembly arithmetic, conditional on its imported inequalities; they do
not certify all the probabilistic lemmas or the data.

## Independent recheck and refinement of the chosen audit

Read the actual planted-count criterion (Planted/Main.lean and Awake.lean),
not the unused full-tree `LemmaRStatement` in LemmaR/Statement.lean.
The unused statement is explicitly not proved there; the target instead
uses the planted criterion and ZeroOne.recurrent_of_frozenCount.

The all-awake proof first establishes a hitting bound d^(-(|v|+1)), then
weakens it to d^(-|v|). Retaining the first bound gives
E U_m <= (m+1)/d and E U_m^2 <= (m+1)/d + ((m+1)/d)^2.
This gives a concrete independent check of the same bridge:
if E Z_m >= c m along unbounded m, Z_m<=X and Z_m<=U_m, then
P(X=infinity) >= d^2 c^2. At d=3 and the assembly's c=1/20 this is 9/400.
This is conditional on the imported linear estimate; it cannot verify the
finite data. It sharpens the numerical positive-probability bound in the
paper's second-moment bridge, without changing the claimed classification.
PROOF.md will give two derivations and state all conditions explicitly.

Saved 18 pinned source records in source_archive.json and two further
criterion records in criterion_sources.json, with exact contents and Git
blob identities. Saved selected release metadata in release_metadata.json.
No source code fetched from the repository has been executed.

## Finite audit run

Command:
`OMP_NUM_THREADS=1 nice -n 15 python3 audit_bridge.py > audit_bridge_output.txt 2>&1`
Exit 0, about 0.11 seconds. Peak RSS 22446080 bytes. The sandbox denied
nice; no heavy work ran. Output retained verbatim in audit_bridge_output.txt.

The independent script imports none of the preceding audit code and writes
nothing to earlier directories. All 14 preceding blob hashes match without
repair. It independently recovers 13 shared definitions in the transience
challenge, 12 in the recurrence challenge and the recurrence predicate.
An explicit uniform-step pushforward enumeration agrees with the model
derivation. Thus the preceding main source/model claim holds.

All 20 newly saved source blobs match their pinned Git identities; 16 are
Lean files and have no executable sorry/axiom/native_decide tokens under
the scanner. This is a limited scan, not verification of their imports.
The chain manifest has 1539 entries and the M1 manifest 26. Their shared
mass input digest agrees exactly:
20899e67ffede92c5a40da027d7cac84730974e39fdca2fc53af912fe9b6e227.
All three release-input digest metadata entries match ASSETS.md. No binary
asset bytes were downloaded or hashed here.

Exact arithmetic output:
`mu=1778342/3, delta=7045771/88917100, (1-delta)*mu=b1=27290443/50`.
The reverse calculation `1-b1/mu=delta` also holds.
The first planted index allowed by the linear bound is 1778251;
`E Z_m >= (m+6)/20`, so c=1/20 is legitimate conditional on that bound.
The independently proved moment estimate has leading coefficient 1/9
after division by m^2 at d=3, giving conditional probability 9/400.
The comparison factor against the paper's c^2/24 is exactly 216.

Wrote PROOF.md with the model recheck, an independent second-moment
proposition, a second threshold derivation, exact interface arithmetic and
the limits of the conditional application. No original q=1 classification
or certificate replay is claimed.

## Attempts to break the result and final audit

Checked the planted root separately: it has d+1 neighbors including the
absorbing leaf, whereas the original root has d. The harmonic identity at
that planted root is (1+d*d^-2)/(d+1)=1/d, so the extra factor 1/d applies
at depth zero too. The upper count includes that root frog exactly once.
The hitting indicators are independent before activation; activated-frog
indicators need not be independent, and the proof never assumes they are.

Checked the passage from moments to an infinite count twice: a fixed-K
Cauchy–Schwarz tail argument and a variable-threshold argument followed
by theta decreasing to zero. Both use probability continuity from above.
They require only an unbounded sequence of good heights, not convergence
or monotonicity of the Z_m. Countably many almost-sure comparisons may
be intersected first. The hypotheses also force c<=1/d by the first-moment
bound, so the probability lower bound cannot exceed one. At c=1/20,d=3
this presents no boundary issue.

Checked the index at n=m1-30: the imported inequality is strict there,
so n=1778249 is excluded and m=1778251 is the first usable planted index.
The assembly uses the more conservative m>=m1, which is consistent.
Checked terminal deficit conversion in both directions. No numerical or
logical counterexample to the stated conditional proposition was found.
The missing data cannot be replaced by its digests or saved PASS records.

Final command (same as above), after requiring exactly three release-input
metadata entries, exited 0 in about 0.14 seconds, peak RSS 25264128 bytes.
All mathematical output agrees with the first run. This repetition checks
the one changed assertion; no broader test or build was run.

Wrote SOLVED_ELSEWHERE.md and REPORT.md with a PARTIAL verdict. Final
inspection confirmed all requested artifacts, the pinned source archives,
the reproducible script and output, and explicit conditional qualifications.
Only this folder was changed. No complete outside-solution certification
or original-model recurrence/transience claim is made.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, approximately 11:02 Asia/Tbilisi.
