# exact target, quantifiers, hypotheses and units

A083, B17, run 20261013T234228Z-account05-A083-formal-core. Formalize the coherent branch row that supports the live A092 root-spectral/output-bank conversion, then expose the exact loss from replacing its root label by a terminal residual spectral label. All Fourier functions are Boolean signs under uniform physical inputs; information is in bits; influence is ordinary pivotal/squared-Fourier influence.

Formal statement: for all rational p0,p1,a,b, with a,b>=0 and p0+p1=(a+b)/2, define k(a,b)=a/(a+b) on positive rows, with k=1/2 on the zero row. Then (p0+p1)k(a,b)=a/2 and k(a,b)+k(b,a)=1. Nonnegativity makes zero sum imply a=b=0. The certificate covers normalization and unreachable-row handling, not entropy or a universal reference payment.

Exact Boolean family: for every integer r>=1, let f_r(x)=product_(j=0..r-1)(1-2x_(2j)x_(2j+1)), x_i in {0,1}, with independent uniform bits. Query each block's first bit; query its second bit only when the first is 1; process blocks in fixed order. This is an essential computing tree, never repeating a coordinate. Let Pi be its stopped transcript, S0 its coherently retained root Fourier label, and E its terminal residual label. Every leaf is constant, so E=empty. Put Y=f_r(X), C_root=H(Pi|Y)-H(Pi|S0) and C_reset=H(Pi|Y)-H(Pi|E). The exact claim is

    H(Pi|S0)=r/2, H(Pi|E)=3r/2,
    C_root=r-h2((1-2^-r)/2), C_reset=-h2((1-2^-r)/2),
    C_root-C_reset=r, sum_v w_v J_v=r, H(f_r)=2r, I(f_r)=r.

Thus substituting terminal-label conditioning into the root-conditioned conversion identity is not free. A universal influence payment for this omitted reset difference must have coefficient at least 1, or at least 1/2 for the half bank. This is not an FEI counterexample: H/I=2 for every r.

# sources actually read, revisions and theorem locators

Read BOARD.md at stage start, supervisor snapshot 2026-10-13 23:39 UTC; B17 STREAM_NOTES.md v2 dated 2026-10-11 23:40 UTC; own STATUS.md. The lead's JS formal-core target was completed in stage 2 and its notes have not changed. Per dispatch, consume a new dependency rather than repeat that proof. No disagreement with the lead is asserted.

Read A092 stage-3 REPORT.md and CLAIMS.json, run 20261013T222550Z-account05-A092-counterexample-referee. Relevant exact claim: A092-UNIFORM-SIGNED-TRANSCRIPT-BANK-CONVERSION v1, statement hash c89760d342c1dae8edfae7474c238db3774ba50882b854eab3ab2bc5dbbfbe63. Its source explicitly excludes arbitrary witness conditioning/reference resets; it is not refuted by this stage. Read A037 NO_REUSE_CERTIFICATE.md and CLAIMS.json, run 20261011T220010Z-account05-A037-conditional-credit-ledger, especially A037-PHYSICAL-SPECTRAL-COMMON-LIFT v1 and its zero-fiber/fair-branch review obligations. Read A097 stage-3 REPORT.md/CLAIMS.json and A085 stage-2 REPORT.md for frontier context; A097's arbitrary excess-collision terminal reserve remains unpaid, and A085's helper audit is already complete. No census or old logarithm margin is repeated.

out/SOURCE_RECEIPTS.json pins the core sources and protocol by local byte hashes. EXECUTION_PROTOCOL.json is revision 2026-10-11-execution-v2; the original campaign and manuscript baseline readings remain context. An attempted A092 CONVERSION_PROOF.md path was absent; its actual report contains the conversion proof, and no missing file is claimed as read.

# complete derivation or exact first unsupported line

Local coherent transport: if parent coefficients are u=(Ghat(T)+Hhat(T))/2, v=(Ghat(T)-Hhat(T))/2, then u^2+v^2=(Ghat(T)^2+Hhat(T)^2)/2. Set a=Ghat(T)^2,b=Hhat(T)^2. Conditional on the erased row T, the physical branch kernel is a/(a+b) or b/(a+b). Multiplying by row mass (a+b)/2 gives a/2 or b/2 exactly. This retains the original full label and only uses its current projection to select the branch. For a+b=0 the row mass is zero, so the normalized fallback adds no true mass. Summing over T and applying the child's Parseval identity yields fair physical branches. The local rational statements are checked in Lean; the Fourier identity and tree interpretation are outside its scope.

One-block witness: f=[1,1,1,-1] indexed by x0+2x1 has Walsh amplitudes (1/2,1/2,1/2,-1/2) and four root masses 1/4. Its transcript alphabet is 0 (x0=0), 10 (x0=1,x1=0), 11 (x0=1,x1=1). Under the actual coherent coupling, the only nonzero joint masses are

| S0 | Pi | probability |
|---|---|---:|
| 0 | 0 | 1/4 |
| 1 | 0 | 1/4 |
| 2 | 10 | 1/8 |
| 2 | 11 | 1/8 |
| 3 | 10 | 1/8 |
| 3 | 11 | 1/8 |

The transcript law is (1/2,1/4,1/4), with H(Pi)=3/2. Root entropy is 2 and joint entropy is 5/2, so H(Pi|S0)=1/2 and I(Pi;S0)=1. Terminal E is empty, giving H(Pi|E)=3/2. Output entropy is h2(1/4)=2-(3/4)log2(3), and the transcript determines output. Consequently C_root=-1+(3/4)log2(3)>0, while C_reset=-2+(3/4)log2(3)<0. The strict signs are integer comparisons 27>16 and 27<256. The reset changes both magnitude and sign. Dimension two is minimal: on zero or one bit every Boolean sign is constant or a literal, with deterministic root spectrum, hence no lost root/transcript mutual information.

All-r bridge: Fourier coefficients of disjoint products factor and root spectra tensor. At each block, preceding evaluated signs multiply the remaining function by a sign; this changes no squared branch coefficient. Unqueried other blocks contribute the same tensor factor to numerator and row denominator, and it cancels from the coherent branch kernel. Therefore the joint root-label/transcript law is the tensor product of the displayed six-entry block law, for every r, not just the tested range. Entropy additivity gives H(Pi)=3r/2, H(S0)=2r, H(S0,Pi)=5r/2. Each factor has mean 1/2, so E Y=2^-r and P(Y=-1)=(1-2^-r)/2. The transcript determines Y. This proves all displayed bank formulas.

Each first-bit query has J=1 and each reached second-bit query has J=0; the weighted total is r. Every physical coordinate in an AND block is pivotal with probability 1/2, so each block has total influence 1 and the product has influence r. All terminal Fourier entropies are zero because the tree computes the function. Thus the example respects the same consumed influence R=r and the existing A092 upper bound; it refutes only a proposed free substitution of E for S0. It says nothing about a complete witness that additionally retains history or extra side information: its conditional-bank/reset correction must be recomputed explicitly.

First unsupported universal line: a prescribed normalized witness/reference channel funds its particular conditional bank, reset correction, erasure residual and terminal core entropy from a remaining exclusive influence reserve. The kernel check and this obstruction neither supply that reference nor justify spending the same r units again elsewhere.

# executed validation with domain, arithmetic, commands and outputs

Frozen specs precede every job: out/FROZEN_SPEC.json for the Lean core, out/RESET_PILOT_SPEC.json for r=1 and out/RESET_MAIN_SPEC.json for r=1,...,5 (dimensions 2,4,6,8,10). No symmetry reduction or automatic dimension escalation. The analytic factorization supplies the all-r conclusion; finite tests only certify the frozen cases.

Lean 4.33.1, import Init.Data.Rat.Lemmas only: final PASS, exit 0, 3.837 seconds, 532,078,592 bytes peak process commit. row_transport, transport_with_fallback, transport_nonnegative and kernel_normalized print only propext, Classical.choice and Quot.sound; no sorryAx or target axiom. Hard process cap 1400 MiB, timeout 60 seconds. Every Lean attempt followed memok exit 0. First attempt timed out without a diagnostic. The next draft failed because Rat.mul_left_comm is not a core theorem and zero multiplication needed explicit simplification; a proved local commutation lemma and Rat.zero_mul repaired it. Final compiler output is saved separately from failed attempts.

Independent exact checker: truth tables and integer Walsh spectra generate actual coherent root/transcript laws through every prescribed physical node. Marginals are independently verified by direct physical assignments. A separately tensor-constructed six-entry block law agrees entry by entry with the recursive coherent construction. Fraction arithmetic verifies every mass; prime-log coefficient maps verify entropy identities exactly, with no floating-point logarithm or tolerance. Physical edges and squared-Walsh expected cardinality independently agree on influence. Every completed r case is saved immediately.

Pilot PASS: 57 exact checks, 0.0107 seconds. Main PASS: 5,149 exact checks, five family members, 1.2153 seconds, estimated memory 80 MB. The first pilot caught an incorrect expected influence 3r/2 in the draft checker; physical edges and spectral influence both gave the correct r. That assertion was repaired before the successful pilot/main runs; mathematical bank values were unaffected. The source and history preserve this correction. No large enumeration, GPU, package install, library rebuild, external message, git or shared-folder write occurred.

Commands from A083:

```text
python -X utf8 runs/20261013T234228Z-account05-A083-formal-core/code/prepare.py
python -X utf8 ~/brain_workers/FEI100_20261011/tools/memok.py
python -X utf8 runs/20261013T234228Z-account05-A083-formal-core/code/check_lean.py
python -X utf8 runs/20261013T234228Z-account05-A083-formal-core/code/check_reset.py pilot
python -X utf8 runs/20261013T234228Z-account05-A083-formal-core/code/check_reset.py main
python -X utf8 runs/20261013T234228Z-account05-A083-formal-core/code/finalize.py
```

# proof dependencies and changed downstream conclusions

The formal arithmetic has no campaign claim premises; source coupling definitions are reconstructed rather than assumed as accepted universal theorems. The all-r family proof uses elementary Fourier tensor factorization and entropy additivity. A092's conversion formula remains intact under its stated retained-root coupling. The zero-row normalized branch core now has a precise checked artifact. No shared claim index or source statement was edited.

Consumers A037/A039/A050/A064/A091/A092/A097 must preserve the identity of the conditioning variable. Dropping the retained root label loses exactly r bits in this actual family, requiring at least r/2 additional half-bank accounting. A085/A090/A094 can use the exact one-block joint table and formal scope to audit substitutions. This is a narrow certificate/risk result, not a new broad FEI candidate. Statement hashes use compact sorted UTF-8 JSON with keys exact_statement and hypotheses.

# one next mathematical action and independent reviewer

A090 primary/A094 alternate should independently reconstruct the root-versus-terminal bank distinction and inspect the exact Lean theorem assumptions. A092/A039 should specify one actual reference witness W and its required side information A on the priority shared-control tree, then compute H(Pi|S0)-H(Pi|W,A), adding this reset price to the same exclusive influence account before paying terminal CE. The next question is the paid reference-side channel, not another tensor-family or scalar baseline.

# actual persistence receipts or precise save blocker

All four protocol files, REPORT.md, CLAIMS.json, PROGRESS.json and identical PACKET_DELTA.json, are saved in the assigned A083 run with FORMAL_SCOPE.md, code and out. finalize.py checks protocol field sets, successful exact/formal outputs, no sorryAx, byte-identical compatibility and artifact size limits. out/ARTIFACT_RECEIPTS.json provides local sizes and SHA256 values. STATUS.md has two lines, WORKLOG.md appends this stage and LEARNED.md retains its exact reset lesson. Independent review, supervisor copying, Brain/GitHub mirroring and downstream use remain unverified; local persistence is not any of those receipts.

Universal bridge: This stage moves C024 history transfer and C019 accounting by kernel-checking the zero-safe coherent row normalization and certifying an actual Boolean all-r obstruction to free root-to-terminal label reset: the signed bank shifts by exactly r bits with consumed influence r, so its omitted half-bank price is at least r/2. It reduces no universal FEI constant; prescribed witness conditioning, reference resets, residual erasure and complete terminal core cost remain unpaid. NEXT names and prices one real witness-side channel on the existing shared-control tree, which attacks that remaining universal bridge instead of adding another isolated class bound.
