# FEI campaign seed claim ledger

**Full FEI: OPEN.** Updated 11 October 2026. Team IDs below are the F01–F20 identities in `TEAMS.json`, copied from the root campaign roster. This ledger does not assign a replacement roster or claim that workers have run.

## Status and source conventions

- **PROVED_BASELINE:** a theorem/identity established in a cited primary paper or a complete proof in the recovered source. This label does not imply external peer review or proof-assistant certification of the new manuscript.
- **CONDITIONAL:** a proved implication whose hypothesis remains unpaid for the intended general class.
- **OPEN_TARGET:** an unproved mathematical goal; finite tests do not change this status.
- **REFUTED:** the stated assertion fails on the identified witness. The scope of the failure is part of the claim.

Uniform Boolean outputs are ±1, `p(S)=fhat(S)^2`, `H` is in bits, and `I=E|S|`, unless stated otherwise. Write `B=sum_i H(S_i | S_-i)` and `DTC=H-B`. Use `D_char=sum_i min(Inf_i,1-Inf_i)` for character-centered influence; it is **not** DTC. Physical restrictions fix input coordinates. Spectral conditioning and evolving real amplitudes are different operations.

Source aliases below are relative to this campaign directory and work in the repository or downloaded bundle. [SOURCES.json](SOURCES.json) records exact original repository paths, observed immutable blob hashes, commit pins where recovered, and packaged-file hashes. [SOURCES_README.md](SOURCES_README.md) describes the limited curation.

- **P:** [baseline/threshold-paper.tex](baseline/threshold-paper.tex).
- **ER:** [sources/ERASURE_REDUCTION.md](sources/ERASURE_REDUCTION.md).
- **ES:** [sources/ERASURE_SYNERGY_AND_DUALITY_2026-09-18.md](sources/ERASURE_SYNERGY_AND_DUALITY_2026-09-18.md).
- **LA:** [sources/LOG_ALLOCATION_CURATED.md](sources/LOG_ALLOCATION_CURATED.md), mathematical sections 2–6 with original numbering.
- **RIG:** [sources/ERASURE_RIGIDITY.md](sources/ERASURE_RIGIDITY.md).
- **BR:** [sources/BLOCK_RESTRICTION_IDENTITY_2026-09-18.md](sources/BLOCK_RESTRICTION_IDENTITY_2026-09-18.md).
- **RM:** [sources/ROUTE_MAP_CURATED.md](sources/ROUTE_MAP_CURATED.md), selected mathematical sections with original numbering. Its source links identify unbundled proofs and their precise draft/verification status.
- **OP:** [sources/OVERLAPPING_PRODUCT_NOTE.md](sources/OVERLAPPING_PRODUCT_NOTE.md).
- **ONE:** [sources/ONE_BIT_ENDPOINT.md](sources/ONE_BIT_ENDPOINT.md).
- **GAMMA:** [sources/GAMMA_ENDPOINT_LEDGER.md](sources/GAMMA_ENDPOINT_LEDGER.md).
- **ISO:** [sources/ISOSPECTRAL_SPLICING_CURATED.md](sources/ISOSPECTRAL_SPLICING_CURATED.md), complete mathematical sections 2–9.

## Accepted starting statements

| ID | Status | Exact statement and scope | Teams | Source |
|---|---|---|---|---|
| C000 | OPEN_TARGET | There exists one finite absolute C with H(f)≤CI(f) for every finite-dimensional Boolean f. No current campaign artifact proves or disproves this. | F20; all | P, introduction; RM |
| C001 | PROVED_BASELINE | A unate function with one total desirability order satisfies H≤C_reg D_char, C_reg=log₂(4+e)+2log₂(eπ)<8.937. Includes every deterministic LTF. “Regular” here means that coordinate order, not small weights. | F04,F13,F19 | P, `thm:A`, `eq:constants` |
| C002 | PROVED_BASELINE | An arbitrary combination of m regular functions satisfies H≤(11.238+(17/5)log₂m)I and H≤(11.460+(22/5)log₂m)D_char. The parameter m remains in the bound. | F04,F14 | P, `thm:B` |
| C003 | PROVED_BASELINE | Union/intersection of gates, each combining ≤M regular functions, with each input relevant to ≤k outer gates: H≤(41+7log₂k+(29/5)log₂M)I. This does not cover arbitrary outer coherent combinations with that constant. | F01–F04,F14 | P, `thm:readk-intro` |
| C004 | PROVED_BASELINE | Every symmetric threshold has corrected product-measure H_mu^+≤[80+460/ln2](I_mu−Var_mu), uniformly in arity and biases; the stated read-once closure includes parity gates. Arbitrary weighted thresholds under arbitrary bias are not established. | F13,F14 | P, `thm:formulas-intro`, `bias:strong` |
| C005 | PROVED_BASELINE | For actual restrictions f_±, Δ_iH=H(S_i|S_-i)+JS(fhat_+²,fhat_-²); JS≤(2/ln2)min(Inf_i,1−Inf_i); I(f)=Inf_i+(I(f_+)+I(f_-))/2. | F05,F07,F19 | ER §§1–4 |
| C006 | PROVED_BASELINE | For a physical block A and uniform assignment X, H(f)−E H(f_X)=H(S_A|S_Ac)+I(X;Y), where Y is sampled from the restriction's spectrum. The channel term is ≤(2/ln2)I_A. | F06,F19 | BR |
| C007 | PROVED_BASELINE | Full signed Booleanity is equivalent to sum_S a_S²=1 and sum_S a_S a_(S△U)=0 for every nonempty U. Arbitrary nonnegative spectral laws or truncated identities do not suffice. | F09,F16,F19 | ER §6; RM §3 |
| C008 | PROVED_BASELINE | The final queue law is a subprobability reference. Every valid complete forest/assignment witness gives a Gibbs entropy bound, retaining normalization, roots, attachments, subset/rank costs, and used-gate counts jointly. | F01–F03,F18 | P, “A bound retaining the joint witness cost” |
| C009 | PROVED_BASELINE | Ordinary addressing with a address bits and 2^a distinct data bits has H=2a, I=1+a/2, hence H=4(I−1). The complete queue proof also yields H<10I for this family. | F01–F03,F11,F17 | P, addressing benchmark and `cor:affine-selectors` |
| C010 | PROVED_BASELINE | For a physical selector partition with balanced data leaves whose nonempty Fourier supports are pairwise disjoint: H(F)=H(p)+sum_j p_j[H(q_j)+H(g_j)], I(F)=sum_j p_j d_j+sum_j p_jI(g_j), q_j=ahat_j²/p_j. Data variable sets may overlap; leaf Fourier supports may not. | F11,F14,F19 | P, `prop:selector-identities` |
| C011 | PROVED_BASELINE | Affine selector cells of codimension c_j and dual-coordinate support size r_j have H(F)=2sum p_jc_j+sum p_jH(g_j), I(F)=½sum p_jr_j+sum p_jI(g_j), under C010's leaf hypotheses. | F11,F12 | P, `cor:affine-selectors` |
| C012 | PROVED_BASELINE | For balanced g, M_g=((1+g)/2)y₁+((1−g)/2)y₂ has H=2+H(g)/2 and I=1+I(g)/2. Tensoring/balancing proves the optimal constant on these unrestricted two-cell selectors equals C_FEI. | F11,F15,F20 | P, “Unrestricted selectors and the optimal FEI constant” |
| C013 | PROVED_BASELINE | Balanced-core activation F=1+A_r(g−1), p=2^−r, has H=pH(g)+2rp(2−p)+(1−p)²log₂(1/(1−p)²), I=p(I(g)+r). For every ε,δ>0, the supremum H/I over such activations with 0<I≤ε and P(F=−1)≤δ equals C_FEI. | F03,F15,F17,F20 | P, `prop:activation`, `cor:activation-equivalence` |
| C014 | PROVED_BASELINE | Arbitrary signed constant leaves on singleton address cells represent every Boolean g exactly. Even requiring balanced leaves does not remove full scope if overlapping supports are allowed: leaves g_u(y)=g(u)y give F(z,y)=g(z)y, H(F)=H(g), I(F)=I(g)+1. Tensor amplification removes the additive one. | F11,F14,F15,F20 | Direct identity from C010's selector setup without its disjoint-support hypothesis; see X005 |
| C015 | PROVED_BASELINE | The parity lift f(x,z)=g(x₁z,…,x_nz) has H(f)=H(g), B(f)=0, and I(f)=I(g)+P(|S_g| odd)≤2I(g). Its physical z=+1 restriction is g. | F05–F07,F15,F17 | ES §3 |
| C016 | PROVED_BASELINE | Exact product Boolean spectra satisfy H≤2I. One spectral address with product conditional spectrum is also proved with constant two; two addresses already admit H/I=40/17>2. | F09,F12,F17 | RIG §1; RM §§9.1,9.4; ONE §§1–3 |
| C017 | PROVED_BASELINE | Read-k decision trees satisfy H≤O(sqrt(k))I; k counts all query nodes for each variable. Whole-set coding is prior art. | F01,F10,F19 | Shalev, https://arxiv.org/html/1806.03646v2, Theorem 9; Wan–Wright–Wu, https://arxiv.org/abs/1312.3003 |

## Live obligations and conditional bridges

| ID | Status | Statement / missing payment | Teams | Dependencies / source |
|---|---|---|---|---|
| C018 | CONDITIONAL | Uniform B≤KI for all Boolean f implies full FEI with C≤K+2/ln2; conversely B≤H makes FEI imply B≤CI. The equivalence is proved; a universal finite K is not. | F07,F20 | C005; ER §4 |
| C019 | CONDITIONAL | A genuine stopping restriction tree with a linearly paid cumulative mismatch/log charge and FEI-certified leaves gives FEI. The same ancestral influence cannot be spent again in descendants. | F05,F06,F20 | C005,C006; LA §5; ISO §3; RM §§2–3 |
| C020 | OPEN_TARGET | Bound the full expected joint witness cost by an absolute multiple of I on a new class or universally, including the rank, sparse-root, attachment and normalization terms. Addressing alone is already solved. | F01–F04,F18,F20 | C008,C009; P, “Scope of the refinement” |
| C021 | OPEN_TARGET | Improve read-k covariance/entropy dependence beyond O(sqrt(k)), e.g. Cov[T]≤A log₂(k+1)I, with the precise tree hypothesis retained. The logarithmic target is already proposed in the literature. | F10,F18 | C017; Shalev §6.2 |
| C022 | OPEN_TARGET | Find a finite explicit constant for genuine Boolean spectra whose conditional retained laws are product after at most two spectral address coordinates. C=2 is refuted; individual projection rows are not Boolean. | F12,F09,F16 | C016; X008; RM §9.4 |
| C023 | OPEN_TARGET | Under the exact decaying-threshold reveal policy, prove or refute ∫₀∞e^t E TC(P_t)dt≤A_ε[DTC(P₀)+J₀], retaining the negative forced-information refund. This is in natural-log units and does not itself pay entropy transfer. For each fixed finite dimension the integrals are already finite; the open issue is a uniform bound in the stated budget. | F08,F18,F19 | RM §§11.19–11.20; GAMMA equations (1)–(2) |
| C024 | OPEN_TARGET | Pay actual-source entropy/history transfer while retaining history probabilities and full Boolean ancestry. The true integrated cost satisfies H_nat−3I≤C_path≤H_nat+I, so a universal linear payment is FEI-equivalent. | F08,F09,F20 | RM §§11.13–11.16 |
| C025 | OPEN_TARGET | Establish the corrected biased FEI+ inequality uniformly for arbitrary weighted thresholds, not only symmetric thresholds or balanced internal inputs. | F13 | C004; P, “Further consequences and questions” |
| C026 | CONDITIONAL | Strong selector closure gives H(F)≤max(C_s,C_g,4)(I(F)−1) when each cell satisfies H⁺(h_j)≤C_s(I−Var) and balanced leaves satisfy H(g_j)≤C_g(I−1), with pairwise disjoint nonempty Fourier supports. | F11,F14 | C010; P, `cor:selector-strong` |

## Rejected assertions

| ID | Status | Rejected assertion | Teams | Witness |
|---|---|---|---|---|
| C027 | REFUTED | Small or zero local erasure makes the whole function an easy FEI terminal. | F05–F07 | X001–X002; C015 |
| C028 | REFUTED | B_i≤j_i times a multiplier bounded near zero child influences. | F03,F05,F15 | X003 |
| C029 | REFUTED | Selector entropy/influence identities C010 remain valid with arbitrary overlapping leaf Fourier supports. | F11,F14 | X004 |
| C030 | REFUTED | H(fg)≤H(f)+H(g) for all shared-variable Boolean factors, or a fixed correction proportional to common pivotal overlap repairs it universally. | F14,F17 | X007 |
| C031 | REFUTED | All two-address conditional-product spectra satisfy H≤2I. | F12,F16 | X008 |
| C032 | REFUTED | Approximate independence alone pays local rare erasure or gives dimension-free source entropy restoration. | F07–F09,F12 | X009–X010, with each stated scope |
| C033 | REFUTED | Arbitrary real normalized coherent mixtures may replace genuine Boolean sources in universal FEI estimates. | F09,F11,F14 | X006 |
| C034 | REFUTED | Entropy of a normalized coherent sum is always at most label entropy plus average component entropy, even for orthogonal unit real component vectors. | F11,F14,F19 | X013; does not refute a separately proved Boolean special case |

F16–F19 support the mathematical owners above through exact search, asymptotic witnesses, optimization, and independent reconstruction. A new universal result changes C000 only after its complete proof or an explicit unbounded-ratio Boolean family passes the installed B18 and B19 independent review streams and B20 synthesis, with input from the proposed F19 and F20 roles. Append new IDs; do not erase failed claims or silently strengthen their hypotheses.

## Concurrent 38-page extension

| ID | Status | Statement and scope | Teams | Source |
|---|---|---|---|---|
| C035 | PROVED_BASELINE | A fresh physical selector block of a bits gives H(F)≤2a+average H(g_b). Neighboring orthogonal branches yield I_sel=a/2 and FEI closure with max(4,C); a general I_sel≥ca gives ordinary closure max(2/c,C). Recursive fresh-selector orthogonal-neighbor multiplexers with regular leaves retain C_reg, even with shared data. | F11,F14; live B04,B12 | baseline/current-threshold-paper.tex, sec:shared-multiplexers; supporting/shared_data_delta_independent_audit.md |

F11/F14 must move beyond both the orthogonal-neighbor and uniformly positive-selector-energy cases already covered by C035. Low-energy collision credits and reuse of selector coordinates remain live questions. The F labels are topical groups; installed B ownership is preserved by NATIVE_MAPPING.md.
