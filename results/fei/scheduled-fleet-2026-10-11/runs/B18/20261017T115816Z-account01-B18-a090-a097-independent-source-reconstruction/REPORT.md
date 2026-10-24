# B18 / A090 — independent reconstruction of the corrected A097 GU chain

Run: 20261017T115816Z-account01-B18-a090-a097-independent-source-reconstruction  
Primary packet: B18/A090, independent reconstruction  
Stable gap: G-GU-SIGNED-KL-LOG-NORMALIZATION-LEAF-v2 (unchanged)  
Exact candidate: B20-A097-DUAL-ENVELOPE-ROW-NORMALIZATION-v1, frozen pair (a,b)=(4,3/4)  
Model / effort: GPT-6 / UNKNOWN  
Endpoint: 2026-10-21T19:15:57Z, unchanged

## Result and first unpaid implication

The complete A097 original, its corrected packet delta, the full predecessor singleton-min proof, the high-degree-reserve proof, B07 signed restriction identity, B11 root proof, degree-two theorem/verifier, and U-universal notes/referee were read from their source paths and pinned by blob SHA in source_pins/SOURCE_PINS.json. The prior own global-potential-drift report was recovered locally byte-for-byte; its alternative drift criterion remains OPEN and is not substituted for the leading candidate.

The exact signed restriction identity, sharp root payment, both singleton-row estimates, high-degree reserve, pointwise minimum, tensor-prime localization, degree-two exclusion, and conditional GU-to-FEI reduction reconstruct at their stated scopes. The first substantive unpaid implication is the corrected A097 dual-envelope leaf:

D_ge2 + min{ V1/2 + (2/ln2)(I-Q_ge3), (2/ln2)M1 + sum_j min{V_j/2+L_j/2+r_j/ln2, (9/ln2)(2r_j+s_j)} } <= 4I + 3U/4

for every tensor-prime genuine Boolean function with R=G-4I-3U/4>0 and Fourier degree at least three. The source explicitly marks this leaf OPEN. No joint payment of the signed base sum_i(B_i-Gamma_i), every |A|>=2 KL row, and either complete singleton/high-degree branch is proved. Universal GU and full FEI remain OPEN.

## First source-text defect and repair

In the predecessor ROWWISE_MIN_SINGLETON_CUT.tex, equations (10)–(11) use D<=chi-square and S log(2/S)<=2/e while the file front matter says all logarithms are base two. These are natural-log inequalities. In base two, S log2(2/S)<=2/e is false at S=2/e. The intended proof is correct when the intermediate divergence is explicitly D_nat and the expression is S ln(2/S), followed by one conversion D_2=D_nat/ln 2 in equation (12). The final coefficient 9/ln 2 is unchanged. This run supplies that normalization repair and is a contributor to the repaired helper version, not its independent approver.

## Booleanity, signs, budgets, and terminals

The proof uses genuine Booleanity in f squared equals one, which forces the signed root cancellation sum_A a_A b_A=0 and normalizes both physical children. The derivative g=D_j f is ternary and satisfies |g|=g squared. The upper correlation C_A is retained as a signed sum until the KL or genuine-child inequality is used; no arbitrary spectral law or absolute-value relaxation is inserted. Constants and zero-mass rows are handled separately.

The singleton row estimates are alternatives for the same row and are minimized before summation. The two whole-function envelope branches are also alternatives, not additive credits. The high-degree branch uses M1+W2=I-Q_ge3; the rowwise branch uses its own M1 and r_j,s_j bounds. D_ge2 remains signed and intact. No adaptive stopping-tree theorem is used, so no terminal credit is claimed; the source correctly says a static V1/2 cannot be replaced by adaptive-root payment without a nonreuse embedding and terminal remainder.

## Conditional GU-to-FEI reduction

If a universal pair G<=aI+bU with a>=0 and 0<=b<1 is assumed, weighted averaging over relevant coordinates gives Delta_i U <= (a+bU/I)Inf_i for some i. Restriction induction with C=a/(1-b), r=U/I, and t=Inf_i/I yields r<=C(1-t)+(a+br)t=C+bt(r-C), hence r<=C. Therefore U<=aI/(1-b). The source-reviewed Boolean G-key estimate gives H<=2(I-Var)+2U<=2I+2U, so H<=(2+2a/(1-b))I. For (4,3/4), the conditional consequences are U<=16I and H<=34I; neither is established without GU.

## Validation, reviewers, and next action

The local checker verifies the carried six-bit Boolean potential-route obstruction exactly at the Fourier-mass and potential level, then checks deterministic numerical grids for the root and natural-log ternary scalar estimates. It reports 6,560 root-grid pairs and 22,960 valid ternary-grid triples with no negative floating slack. These are diagnostics only and do not test the all-dimensional A097 leaf. The witness has negative frozen GU residual and is not a GU/FEI counterexample. Actual output is outputs/CHECK.json; command is commands/COMMANDS.txt; source pins and hashes are in source_pins/SOURCE_PINS.json.

Two independent end-to-end reviews are not complete. A094 and A085 are nominees only, not claimed reviewers; if either contributed to the normalization repair, replace that reviewer for the repaired version. Next action: an uninvolved reviewer should independently rederive the normalized ternary singleton lemma, then attack the unchanged joint A097 leaf while preserving the signed aggregate, normalization credits, branch alternatives, and terminal/nonreuse obligations.

Persistence is recorded in persistence/READBACKS.json. The required canonical and mirror paths for the previous own run and this new run were read and returned HTTP 404 before writes. Create-only recovery/write attempts will be recorded separately; no shared index, schedule, held source, protected evaluation, held PR, request payload, live graph/store, or public release is touched.