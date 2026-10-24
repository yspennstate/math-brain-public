# Account03/B10 FEI run — quarter-biased physical-reveal entropy theorem

**Delta:** Proved a new **all-dimensional, singleton-physical-reveal** restricted case of frozen \`B10-A046-HALF-BIAS-TAX@1\`: if the revealed bit has independent physical bias \`p=1/4\` or \`p=3/4\`, then \`J_i <= M_i + delta(p)/2 - epsilon_star\` where \`epsilon_star=0.03589471281848533...\` bits is explicit and strictly positive. Every other product bias and every Boolean f/dimension are allowed. **Limitation:** this is only a two-point revealed-bias subclass; global coefficient-one-half and full FEI are still OPEN. Independent review is pending.

- Logical account/slot: account03/B10; current mathematical B stream B10, selected packet A046, intended account03 cohort FALSIFY_AND_STRESS. Native physical account binding and prompt adoption **UNKNOWN**; no assertion that account01/B10's native task was used or changed.
- Directive read: owner Oct12 FEI-only rev 2026-10-12.1 overrides Oct7 Brain probability-card task **for covered scheduled research**. Preserved old contract and source controls; no editing of schedules/Brain live store.
- Original request read: \`REQ-20261012T031958Z-FULL-FEI-OWNER--owner-relay-fei-control--send-r1.json\`, revision 1, blob \`3290aff155f63dbc1a5c58ae58c3dc3d6254b508\`. Older Claude requests \`REQ-2026101012394322\`, \`REQ-2026101011362242\`, and Oct10 export/card request are acknowledged as historical/currently out of FEI research scope. \`unread[]\` plus \`not_listed_files\` (529 named archived messages at observed index) were inspected; exhaustive retrieval of every historical original is **NOT_CLAIMED**.
- Existing B10 knowledge prior: account01/A046 frozen v1 half-tax candidate, coefficient-one comparison from B09, account01/A047 two-bit endpoint theorem and diagnostic **read**; do not relabel or duplicate either.
- Source and protocol pins: see \`SOURCES.json\`. Proof has zero reliance on protected eval banks, private user data or denied Oct7 coordination content.

## Exact result, comparison, and proof

See **full original** \`QUARTER_BIAS_LEMMA.md\`. For \`q_T=(1-p)a_T^2+p b_T^2>0\`, physical-posterior amplitudes \`v_T=(sqrt(1-p)a_T,sqrt(p)b_T)/sqrt(q_T)\` are two-dimensional; their Fourier-coefficient counterpart is \`U_p v_T\`. Exactly
\`J=h_2(p)-sum_T q_T H(v_T^2)\` and \`M=sum_T q_T H((U_p v_T)^2)\`.
The proof establishes an absolute scalar sum-entropy lower bound \`L=37/32-45/(128 ln2)\` at qubit-basis overlap \`sqrt(3)/2\`, by a cubic upper polynomial for entropy deficiency and a monotonicity argument on the exact angle parameter. The threshold for the proposed half-tax is \`T=2-(7/8)log2(3)\`, and a rational log bracket establishes \`L-T>0\`. Zero-mass fibers are omitted from normalization and weighted by zero; \`0log0=0\`; natural logs in scalar bounds, binary entropy in bits.

This is a genuine restricted-theorem increment over the earlier **two-bit** boundary work: it permits arbitrary n and arbitrary Boolean gates at these two fixed singleton biases. It supplies no uniform theorem for p approaching zero. No FEI counterexample or full proof is claimed.

## Verification actually performed

The accompanying **original** Node.js standard-library checker \`CHECK.js\` was executed with \`node CHECK.js\` in a local Node v22.16.0 runtime; complete literal stdout in \`CHECK.out\`. No random seed. 20,001 scalar angles; all 256 three-bit Boolean truth tables, all three singleton reveals, p=1/4 or 3/4 for that reveal, five choices for each other bias: **38,400 complete parameter instances**. All diagnostics PASS, no violation of explicit analytic epsilon bound. Minimum observed helper slack 0.11518806279639898 bits, scalar min 0.7091578075536797 bits, max Parseval numeric error 6.66e-16. These floating checks are **NOT** exact interval certificates and are not a substitute for the analytic proof. The strict rational comparison is shown in the proof, not established by floats.

## State distinction

Mathematics: restricted theorem author-proved, independent review UNVERIFIED; A046 frozen universal conjecture OPEN; full FEI OPEN.
- CONFIG/ADOPTION of own native task: UNKNOWN, no modifications made.
- NATURAL_RUN_WORK: substantive independent mathematical derivation and checker executed.
- SAVED_REMOTE/IMMUTABLE_READBACK: to be established **only** by an actual GitHub connector receipt and full content readback after this report is written; its mere presence is not evidence of independent review.
- INBOX_POST: separate subsequent create-only message action (not presumed in this report).
- RECEIPT/CLAUDE_READ/PEER_REVIEW/NATIVE_INGESTED/USED/OUTCOME: UNKNOWN/NOT_CLAIMED.
- Next handoff: request independent A087/A092 reconstruction of scalar log-polynomial and exact q_T posterior law, then attempt a rigorously quantified open interval of p values around 1/4 and 3/4; preserve actual head pin and stop if later source corrections invalidate prerequisites.

No new workers, task edits, billing, credits, protected-bank reads/writes, public release, merge, deployment, permission bypass, live-store changes, or held source transport.
