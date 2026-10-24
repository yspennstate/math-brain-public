# A066 / B14 — semigroup dissipation

## exact target, quantifiers, hypotheses and units

For every finite-dimensional Boolean sign f on the uniform cube, write p_S=hat(f)(S)^2, I(f)=sum |S|p_S, and H_nat(f)=sum p_S ln(1/p_S). Entropy in bits is H_nat/ln(2). The objective of this packet is an exact noise-semigroup integral identity, its boundary terms and endpoint integrability, and the precise unproved universal influence payment.

**Outcome:** this packet's identity and endpoint deliverables are complete locally. A sufficient integrable pointwise influence-envelope mechanism is analytically ruled out by actual Boolean point defects. The universal integrated influence bound and full FEI remain OPEN. Both authored claims await independent review; no novelty or priority claim is made.

The semigroup is T_t=exp(-tL), L chi_S=|S|chi_S. Its squared spectrum q_t(S)=p_S exp(-2t|S|) is unnormalized. Define F(t)=sum q_t ln(1/q_t), E(t)=sum |S|q_t and G_f(t)=F(t)-2tE(t). This corrected entropy tracks the initial spectral information; it is not the entropy of a renormalized evolving law. Set

J_f(t)=sum |S|p_S exp(-2t|S|)ln(1/p_S).

## sources actually read, revisions and theorem locators

The complete execution protocol, revision `2026-10-11-execution-v2`, governed this run. Campaign README, status, claim/obstruction/packet registries, next-action file, and plan were loaded. The plan's B14/A066 acceptance test specifically requires the semigroup, normalization, boundary terms, both endpoint bounds and an honest unpaid integral. BOARD.md dated 2026-10-11 21:45 UTC lists no completed A066 stage. `claude/B14/STREAM_NOTES.md` was absent at the supplied path; independent permitted B14 work proceeded.

Supplement CAMPAIGN.md, CLAIMS.md, COUNTEREXAMPLES.md, SEED_LEMMAS.md and NATIVE_MAPPING.md were loaded together with all twelve packaged source notes. In particular:

- SEED_LEMMAS.md §3 gives the recovered point-defect spectrum, fixed-Renyi failure and Shannon ratio tending to four. The spectrum is reconstructed here, rather than treated as an accepted new theorem dependency.
- COUNTEREXAMPLES.md X006 and claim C033 give the non-Boolean degree-one relaxation control. Its heat-flow translation is stated explicitly in DERIVATION.md.
- GAMMA_ENDPOINT_LEDGER.md equations (2) and (6) distinguish the reveal policy's weighted lifetime from its dissipation budget. Neither is substituted for the heat integral here; this route uses a different semigroup and functional.
- Earlier B05, B09 and B19 REPORT.md files were loaded; their local-payment and uncertainty claims are not premises of this derivation. The campaign's B09 interval correction and scope qualifications remain in force.

The four supplied paper texts were loaded and scanned, with targeted review of their introductions, conventions and relevant keyword matches: threshold 38pp §1 equation (1), threshold 29pp earlier version §1 equation (1), percolation 30pp §1.1 equations (1)–(2), and percolation 31pp other version §1.1 equations (1)–(2). Their convention is entropy in bits, with natural logarithms distinguished. No threshold, percolation or composition theorem is used as a proof premise. This is targeted source consultation, not an independent audit of those entire papers. Paper text encoding required CP1252 fallback; hashes are computed on original bytes.

`out/SOURCE_READ_RECEIPTS.json` records exact paths, SHA256, bytes, decoding and line counts for 33 loaded files. These read receipts are not theorem-acceptance receipts. No Brain write, shared-index edit, external message, git command or network search was performed.

## complete derivation or exact first unsupported line

The complete finite-sum proof is in `DERIVATION.md`. Differentiation yields G_f'=-2J_f and the exact identity

H_nat(f)=p_empty ln(1/p_empty)+2 integral_0^infinity J_f(t) dt.

The boundary satisfies 0<=p_empty ln(1/p_empty)<=I(f). For each fixed f, J_f(t)<=J_f(0) near zero and J_f(t)<=exp(-2t)J_f(0) at infinity. The tail integral is at most J_f(0)exp(-2T)/2. Boolean coefficient granularity also gives J_f(0)<=2(n-1)ln(2)I(f) for n>=1; this bound retains dimension dependence.

**First unsupported line for full FEI:** there exists a finite universal K such that integral_0^infinity J_f(t)dt<=K I(f) for all finite-dimensional Boolean f. If proved, it would give the bit-entropy constant (1+2K)/ln(2). Conversely FEI implies that integral bound with K=C ln(2)/2. The integral identity is therefore an explicit equivalent open target, not a universal payment.

For the actual Boolean family f_n=1-2 1_{x=(1,...,1)}, n>=2,

J_{f_n}(t)/I(f_n)=(2n-2)ln(2) exp(-2t)[(1+exp(-2t))/2]^(n-1).

Choosing n=ceil(1/t) proves that any dimension-independent measurable pointwise envelope k(t) must satisfy k(t)>=ln(2)exp(-3/2)/t almost everywhere on (0,1/4]. Such an envelope cannot be integrable. However the exact area is

(integral J_{f_n})/I(f_n)=2(1-1/n)(1-2^(-n))ln(2)<=2ln(2).

This rules out the pointwise-envelope mechanism while leaving the integrated target intact. It already fails on a simple threshold family. Full signed Booleanity is not used by the identity; a future universal payment must use additional Boolean structure. The normalized, non-Boolean singleton law has I=1 and integral J=(ln n)/2, so normalization alone is insufficient.

## executed validation with domain, arithmetic, commands and outputs

The specification was saved before execution as `FROZEN_SPEC.json`. Command, from the A066 workspace:

```text
python -X utf8 runs\20261011T214539Z-account05-A066-semigroup-dissipation\code\check.py
```

Output `out/CHECK.json`: PASS; **6,999 exact assertions**; all **278** Boolean truth tables in dimensions 0 through 3, plus seven point-defect truth tables in dimensions 2 through 8. Integer Walsh transforms and Fraction arithmetic check Parseval, Fourier influence against direct physical pivotal probabilities, coefficient granularity, unnormalized heat-polynomial mass/degree bounds at four rational damping values, and the point-defect closed formulas. A separate binomial degree-sum calculation checks the relevant multiplicity identity. The measured Python computation took 0.0993 seconds; shell startup/wait time is separate. Memory remained a small bounded truth-table workload, with no job estimated above 300 MB.

Logarithms are formal atoms in the exact checks. No floating logarithm or numerical quadrature supplies a certificate. The all-n and continuum-time obstruction is proved analytically in DERIVATION.md; the finite checks do not establish the universal integral inequality. No formal verification or independent review is claimed.

The source-reader command was also executed with `python -X utf8` on `code/read_sources.py`; its successful output records 33 full file loads and targeted excerpts. An initial UTF-8 decode attempt failed on the paper texts and was repaired using recorded CP1252 fallback.

## proof dependencies and changed downstream conclusions

Claim `A066-HEAT-ENTROPY-IDENTITY` v1 is an elementary finite-sum derivation with no imported mathematical claim dependencies. Claim `A066-NO-INTEGRABLE-HEAT-ENVELOPE` v1 uses its definition of J and a separately reconstructed actual Boolean family. Both are author-proved, pending independent review.

No existing registered theorem is declared false. The newly specified helper `J_f(t)<=I(f)k(t)` with one nonnegative integrable universal k is refuted. Consumers A067/A070 should avoid trying to prove such a pointwise estimate for this J, including by a fixed-Renyi strengthening. A088/A094 can audit the Boolean/non-Boolean distinction and the countable almost-everywhere quantifier. B20 can adopt the precise no-go while keeping the universal integrated gap open. No downstream adoption is yet observed.

## one next mathematical action and independent reviewer

Seek an influence charging argument across dyadic time intervals with nonnegative charges that are summable for each fixed Boolean function. A separate O(I) bound for every interval is insufficient: the number of intervals may grow. Test the charging rule on the point-defect spike before broader application. Proposed independent reviewer: A070, with A088/A094 for the all-dimensional implication and scope.

## actual persistence receipts or precise save blocker

All authored artifacts are confined to this A066 run and the three rolling files. `CLAIMS.json`, `PROGRESS.json`, `PACKET_DELTA.json`, `DERIVATION.md`, frozen specification, code and exact output accompany this report. `out/PERSISTENCE.json` records byte sizes and SHA256 of the final local files, and `out/SCHEMA_CHECK.json` records exact protocol-key validation. No local save blocker remains after verification. Supervisor copying, GitHub/Brain mirroring, independent acceptance and downstream use have not been performed or verified in this stage.
