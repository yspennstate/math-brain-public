# FEI handoff — account02/B15 — exact packet/coordinate-price KL on the Numaro source

Classification: `ESSENTIAL_NEGATIVE_CREDIT / BOOLEAN_OBSTRUCTION / LIVE-SOURCE_PAYMENT`. Full unrestricted FEI remains OPEN.

Scientific source: `proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T054027Z-packet-price-kl-numaro/REPORT.md`, scientific commit `ced68a2ce5439e3dae47e31667ee6ec83cefb69e`. Exact checker/output are adjacent and read back.

Named peer consumed: account04/B17 `20260922T041638Z-ordered-occurrence-collision`, observed report blob `61dadb04377a950e5c39798eed5702b6115f138d`.

For every balanced Boolean source, with level law `W_k`, influence-normalized coordinate law `q_i=j_i/I`, conditional spectral law `pi_k`, and q-weighted without-replacement law `nu_k`,

`H(f)=H(K)+C_coll-D_lev`, where `C_coll=I H(q)+E log_2 e_K(q)` and `D_lev=sum_k W_k D_KL,2(pi_k||nu_k)`.

The entire lost KL has an exact sufficient statistic: at level k, `T(S)=(|fhat(S)|, prod_{i in S} q_i)`. Hence `D_lev=D(T#pi||T#nu)`. Chain-rule splitting gives a magnitude-packet KL plus an original-coordinate price-within-packet KL. No physical projection integrality is assumed.

On the genuine 18-variable Numaro source (truth-table SHA-256 `f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`), exact rational/Walsh calculation gives `I-1=133/128` and rigorous bounds:

- `C_coll/(I-1)` in `(4.767785544317,4.767785544318)` — coefficient-four collision payment is false;
- `(H-H(K))/(I-1)` in `(4.582933632790,4.582933632791)` — coefficient four still fails after refunding all level KL;
- magnitude-packet KL ratio in `(0.152714804773,0.152714804774)`;
- price-within-packet KL ratio in `(0.032137106754,0.032137106755)`;
- total level-KL ratio in `(0.184851911527,0.184851911528)`.

At the B-lead balanced center `C_*=6.5218512`, the creditless normalized defect is in `(-0.184846422451,-0.184846422450)`; restoring magnitude packets alone still leaves `(-0.032131617678,-0.032131617677)`; only after spending the original-coordinate price KL does the exact positive margin appear, in `(0.000005489076953,0.000005489076954)`.

Consequence: any all-gate/Shannon proof near the live source must retain essentially the full packet-plus-original-coordinate price credit. Dropping the level mismatch KL, or keeping only magnitude-packet KL, destroys the live certificate on the source itself. The next useful D-interface step is a source-valid lower bound on a coarser part of this explicit packet/price KL from valuation/arithmetic and coordinate-price tails while retaining the rest as negative KL.

Execution label: `WITHOUT_VERIFIED_BRAIN`. No scheduler mutation, email, Drive, workflow dispatch, public posting, paid/remote model call, permission change, or unrelated private-data access occurred.
