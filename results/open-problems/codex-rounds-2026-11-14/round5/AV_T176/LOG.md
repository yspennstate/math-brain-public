# T176 continuation log

Task: “Verify: has open problem T176 been settled by the OpenAI math release?” Session began 15 November 2026, approximately 07:33 Asia/Tbilisi (exact receipt time unavailable).

## Step 1 — orientation and earlier work

Listed this folder and all three earlier folders, and read their REPORT.md, LOG.md and the available PROOF.md files using `OMP_NUM_THREADS=1 nice -n 15 /bin/cat ...`. The first session has no PROOF.md; the listings show no computation scripts in these earlier folders. Some combined tool output was truncated, so the mathematical notes will be reread separately before use. Round 4 proposes inspecting the actual Lean definitions and dependency chain, especially reciprocal degrees and EightBlocks.

All writes are confined to this folder. The task explicitly excludes global brain, mesh and checklist writes, so those state-changing commands are not run. No git, subagents, external posting or accounts. The attempted startup-memory path `~/brain-views/MEMORY.md` was absent; a read-only file search was attempted. Read compute_state.json: status warn, mode owner_away_open, CPU saturated. No heavy computation or Lean build is planned.

Every shell command has used `OMP_NUM_THREADS=1 nice -n 15`. The sandbox nevertheless reports `nice: setpriority: Operation not permitted`; the wrapped read-only command still executes. No substantial computation will run under that unresolved restriction. An initial guessed `/usr/bin/cat` was absent; `/bin/cat` works.

## Step 2 — bounded literature check started

Used the web search tool with queries `"Thorp shuffle" "2026" "OpenAI"`, `"Optimal-order mixing" Thorp`, and `"Thorp" "Jiang" mixing 2026`. Opened the repository history, arXiv:2610.18884, current Lean Main.lean and lean/docs/238.md. Jiang's page lists Yunjiang Jiang, v1 submitted 3 October 2026, and the same dyadic d^(5/3) result; repository history lists no Thorp correction.

The bounded search concluded with `"Thorp shuffle" "all even" 2026` and `"Thorp" "OpenAI" correction error refutation November 2026`, and opening the repository issues page and the community revised entry. No later all-even solution was found, so no SOLVED_ELSEWHERE.md is warranted. The community entry (updated November 4, preceding round 1) labels its collected notes unreviewed and AI-generated; it links undated 24d/45d improvements and an October 10 reciprocal-constant calculation. These are not new independent validation. Its human notes section is empty. No Thorp-specific refutation was found in this bounded search. Search snippets are not cited as opened papers.

## Step 3 — independent recheck and chosen extension

Reread round 3 and round 4 PROOF.md separately without output truncation. Re-derived round 4's crucial degree argument: reserve u top-row labels, choose the u lower labels among the remaining s-u labels, and fill both parts in row order. Every lower column is at most u, so this gives binom(s-u,u) distinct standard tableaux. For u≤s/4 the degree is at least 3^u; for u>s/4 and longest row/column ≥s/8 the trimmed lower ideal with floor(s/16) cells gives degree ≥2^floor(s/16). The remaining hooks are shorter than s/4, giving degree ≥(4/e)^s. The partition envelope exp(3sqrt(s)) then gives the stated limit by taking s→∞ before the truncation parameter K→∞. Independently rechecked the final exponent: an eighth power costs D^(-5/2) in operator norm, hence D^(-3) after squaring and multiplying by D twice. The trim costs 8r and sign coefficient is bounded by r/(1-r). The earlier conditional result survives this recheck.

Chosen ONE extension: audit the source-level Lean dependency and model chain for the short paper's 1600d endpoint. In particular, distinguish the first-power reciprocal sum in FirstMain from the inverse-square sum actually used in EightBlocks, and verify that Model defines independent physical shuffles and full-permutation TV. This is the next step named by round 4. It is a source audit, not a local Lean compilation or a declaration of correctness of the whole preprint.

## Step 4 — source acquisition

Read startup instructions at the actual path `~/.claude/brain_startup.md`. Used the read-only GitHub fetch tool to list `lean/OAI/Probability/ThorpShuffle` and open Main, Model, FiniteLaw, EightBlocks, ReciprocalDegrees, FirstMain, DegreeBounds, PartitionBounds and ExceptionalShapes. Saved their exact source bodies under sources/lean/. The listing contains 56 entries including one FixedLists directory. Main imports EightBlocks; the endpoint's `inverseDegree` is 1/(degree²), whereas FirstMain advertises a separate first-power reciprocal theorem. Further dependencies are being traced rather than assuming these are the same lemma.

## Step 5 — exact preprints and recursive Lean import record

Reopened the three candidates themselves through read-only raw GitHub fetch: short paper build/main.tex and both long papers' build/sections/00-introduction.tex, plus their build/main.tex headers. All identify OpenAI and September 26, 2026. Saved exact returned text under sources/. Extracted the five relevant theorem/corollary environments directly, for exact quotation in VERIFY.md.

Recursively fetched OAI imports from Main and FirstMain. There are 51 modules in Main's transitive closure, plus four modules reached only from FirstMain (FirstMain, FirstFourier, FirstMoment, ExceptionalShapes), 55 in total. The only outside import is Mathlib; no cycle was found. A lexical scan of these source bodies found no `sorry`, `admit`, `axiom` or `unsafe` token. This is not kernel checking. All bodies are saved under sources/lean/. A failed LOG.md context patch made no changes and was corrected here.

Read Model, Main, EightBlocks, ReciprocalDegrees, DegreeBounds, BlockLaws, ConvolutionBounds, FourierBounds, BlockFibers, MarginalBounds, PrefixTests and TaggedCompletion in detail. EightBlocks uses inverse-square degrees and ultimately a fixed-input marginal bound, stronger than the paper's averaged-input Proposition 4.2. FirstMain's first-power result is not in Main's import closure. The fixed-list branch obtains balanced halves after one initial shuffle, rather than supposing the deterministic initial free set is uniform; the particular fresh-coin estimate is being spot checked.

The community page's links to acprk R5 and R25 failed in web open (robots/cache errors); no numerical improvement from those unopened remarks is adopted. Opened its linked cert-machine statement-audit JSON, which explicitly calls itself a reading rather than a certificate. These are follow-up records, not refereeing or proof validation.

## Step 6 — source-audit findings and fresh-coin spot check

Read FreshCoins, EnergyDecay's half-factorization, MarginalEnergy's one-step preparation and fixed-list energy bound, and MaskedResampling's physical-step identity. A deterministic free set need not have balanced halves initially. One fresh shuffle sends each singly free pair to a fair half, while a doubly free pair contributes one point to each half deterministically. For m free positions, the generating-function factor is 1 for an empty pair, 881/1000 for a singly free pair (≤9/10), and 16/25 for a doubly free pair (≤(9/10)²). Multiplication and Markov give each bad-half probability ≤(9/10)^m, hence both ≤2(9/10)^m. This confirms the actual lemma used in the fixed-list branch without appealing to a random initial list. Full detailed derivation is being saved in PROOF.md.

The inverse-square Fourier route has S²≤D C₂² and ‖ν̂v‖²≤8B S D^(-1)‖v‖². An eighth power and two dimension factors give (8B C₂)^8 D^(-2), matching exceptionalReciprocalSum. For B=4 and eventual C₂≤3 this is 96^8; the sign contribution is bounded by 2(2r)^16 and convolution replacement costs 8r. Re-derived the fixed-list squared marginal prefactor as (7·2^d/2)²·(8·2^d)=98·2^(3d); multiplying its remainder by 32 gives 3136. Thus the constants in marginalRate and fullRate have consistent source-level meanings.

Opened the two Comparator challenge files and lean/README.md. The challenge files end in intentional `sorry`; they are outside the 55 solution-source scan. A guessed root formalization.yaml returned 404; no review-status inference is made from that failed fetch. Saved the Lean scope note and source manifest. No Lean build, Comparator run or new mathematical mixing result is claimed.

## Step 7 — mathematical note and verification record saved

Wrote PROOF.md with the independent earlier-result recheck, exact physical-model interpretation, source dependency split, inverse-square Fourier completion and a detailed check of the one-step half-balancing lemma. A first JavaScript write attempt had a syntax error from embedded Markdown backticks and executed no mutation; the corrected write succeeded. Re-derived the balancing lemma independently by X=a+Bin(b,1/2) and the bound exp(-m²/(8b))≤exp(-m/8)<(9/10)^m. Checked empty, singleton-only, double-only and full free sets, the strict threshold, the preparation time and parity-correlated trimming.

Reopened source files are byte-identical to round 4 snapshots: `OMP_NUM_THREADS=1 nice -n 15 /usr/bin/cmp sources/optimal.tex ~/codex_op_1114r4/briefs/AV_T176/optimal-source.tex`, `OMP_NUM_THREADS=1 nice -n 15 /usr/bin/cmp sources/compatibility.tex ~/codex_op_1114r4/briefs/AV_T176/compatibility-source.tex`, and `OMP_NUM_THREADS=1 nice -n 15 /usr/bin/cmp sources/routing.tex ~/codex_op_1114r4/briefs/AV_T176/routing-source.tex` all exited 0. Wrote VERIFY.md with all five exact theorem environments, the model/range/quantity/strength comparison, opened and failed follow-up records, Lean-scope distinctions, a three-sentence replacement status and the new spot check. REPORT.md was saved provisionally earlier and then finalized.

## Step 8 — reproducible audit

Wrote audit_sources.py using only the Python standard library. Ran `OMP_NUM_THREADS=1 nice -n 15 python3 -B audit_sources.py` in this folder, exit 0. It checks saved imports recursively, detects missing modules and cycles, scans solution bodies for literal hole tokens, checks every theorem quotation against the primary source, checks author/date headers and Markdown control characters, and rechecks the rational constants using Fraction. Output:

```json
{
  "solution_modules": 55,
  "main_closure": 51,
  "outside_imports": ["Mathlib"],
  "literal_hole_tokens": 0,
  "exact_theorem_quotes": 5,
  "single_pair_factor": "881/1000",
  "double_pair_factor": "16/25",
  "marginal_squared_prefactor": 98,
  "marginal_rate_constant": 3136,
  "full_rate_base": 96,
  "physical_steps_per_dimension": 1600,
  "status": "passed; source audit only, no Lean build"
}
```

The sandbox still prints `nice: setpriority: Operation not permitted`. This was a tiny source/rational audit, not a simulation, large computation or proof compilation. Re-read final REPORT.md, PROOF.md and the comparison/follow-up/status sections of VERIFY.md. REPORT.md's continuation verdict is PARTIAL and identifies the new check, failed opens, limits and next dependency to inspect. The mathematical result remains conditional source verification, not a new solution or a judgment of the complete preprint. All authored deliverables, 55 Lean solution snapshots, the manifest, five TeX snapshots and the scope note are inside this folder; no other folder was edited.
