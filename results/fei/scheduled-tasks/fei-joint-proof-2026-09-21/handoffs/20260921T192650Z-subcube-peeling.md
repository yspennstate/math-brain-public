# Joint FEI handoff: paid subcube peeling, a near-support block theorem, and its sharp qualitative obstruction

21 September 2026. This is new mathematics for ALL four accounts under FEI-JOINT-FOUR-ACCOUNTS-2026-09-21-192650Z, following the common ORDER.md. Full FEI remains OPEN / NOT PROVED. All new results are self-checked, pending independent review, with no publication-priority claim. The initial report, stronger addendum, and later obstruction are separate preserved stages; read the latter two before continuing from the initial constants or hypotheses.

## 1. Complete scientific package and read order

Private repository: yspennstate/math-open-problems, master. Complete package at commit

    b14ac1bc289df3f1e72ef8e0c2ce14d5bde313a9

Directory

    proofnet24/P03-fei/fleet-2026-09-21/account02/interactive/20260921T192650Z-joint-fei-subcube-peeling/

Read in order:

* REPORT.md, blob 1f1297678b1cafd06bf28f2e39e72eb0f011c03f: exact signed-row peeling, initial Shannon/Holevo argument, balanced-substitution invariance and the greedy maximum-influence obstruction.
* ADDENDUM.md, blob baa3155a268d936d6b191667ee71a6df84969292: arbitrary derivative signs with the genuine payload retained; a classical punctured-cube log-Sobolev proof improving the coefficient; and the approximate-support physical block theorem.
* FIXED_RELATIVE_OBSTRUCTION.md, blob 63fde9689760e5e94c2341fe2d0ed27bc3705d55: the attempted fixed-relative-error strengthening is false, even with a unique maximum-influence pivot and the folded-budget refund.

The executed new code and actual outputs are check_peeling.py/verification.json, check_support_extension.py/support_extension_checks.json, and check_fixed_relative_obstruction.py/fixed_relative_obstruction_checks.json. The unsuccessful depth-moment exploration is preserved separately. EXTENSION_MANIFEST.json records all twelve pre-manifest file identities; all remote blob hashes and byte lengths matched local artifacts at 2d49864bb569e5adefdefc555aeaead0223ad632. Both manifests, all new code and output files were delivered normally. The older denied centered-critical-budget checker was NOT retried or bypassed; these are different new scripts.

All source results below are on the uniform Boolean cube. H is Fourier entropy in bits, I is ordinary total influence, and J=sum_i min(I_i,1-I_i) is folded influence. Multiplication by a character can make I=J without changing H. No arbitrary linear transformation is treated as influence-preserving.

## 2. A one-row decomposition retaining arbitrary derivative signs

Suppose one pivot x has sensitivity support exactly a coordinate subcube:

    |D_x f(z,w)|=1{z=a},    r=|z|>=1,    q=2^-r, q0=1-q.

Then necessarily

    f(x,a,w)=(-1)^x g(w),
    f(x,z,w)=h_z(w) for z!=a,

where g and every h_z are genuine Boolean physical descendants, possibly sharing all residual variables. Define the transverse-control surplus

    B=sum_(k in z)[I_k(f)-q]>=0.

There is an exact influence identity

    I(f)=q(r+1)+B+q I(g)+q0 E_z I(h_z).

At B=0, connectivity of the punctured control cube forces all h_z equal one h, and

    H(f)=q H(g)+q0 H(h)+K_r,
    K_r=phi(q0^2)+2qr(2-q)<4q(r+1),
    phi(t)=t log_2(1/t).

The coefficient four is sharp as r tends to infinity, already with constant g,h. If x is a maximum-influence pivot, every control influence is both at least q and at most q, so B=0 automatically. Hence a centered restriction-critical core with H/J>4 cannot have even ONE maximum-influence derivative whose support is an exact coordinate subcube. Constant derivative sign is NOT required in this stronger version.

Do not drop q H(g). A concrete r=1 example with a six-bit bent payload has H(f)=5 and would violate the incorrect no-payload right side four. The retained payload contributes three bits. This is a counterexample to that incorrect extension, not FEI.

## 3. Positive surplus: a residual-dimension-free Shannon step

ADDENDUM proves, for every epsilon>=0,

    B<=epsilon q
    => H(f)<=q H(g)+q0 E_z H(h_z)+4(1+epsilon)q(r+1).    (A)

At epsilon=1/16 the coefficient is 17/4, improving the first report's 9/2, and the derivative signs may vary arbitrarily through the genuine payload. There is no factor depending on the number of residual variables.

The new mechanism is classical. For real u on the r-cube with one vertex removed,

    Ent_punctured(u^2)
       <=(1+2/r)/(2^r-1) *sum_internal_edges (u(z)-u(z'))^2,

using natural entropy. Extend the missing value by the mean of its neighbors; the extra energy is at most 2/r times the internal edge energy, and apply elementary cube entropy tensorization. Applying this inequality to each SIGNED Fourier coefficient of h_z gives

    H(mean_z |hhat_z|^2)-mean_z H(h_z)
       <=(2/ln2)(1+2/r) B/q0.

The actual nonzero control-frequency mass is q+q0 v, where v=1-||mean_z h_z||_2^2<=2B/q0. Concavity of its scalar entropy profile and the exact zero-surplus formula give (A). The original Holevo argument remains valid but is not needed for this improved proof.

This is a completed transfer from ONE structured derivative to true descendants. A restriction-closed class admitting this structure at every step satisfies the corresponding FEI bound. No theorem states that all Boolean functions admit it.

## 4. An approximate-support block theorem that actually joins stability to restriction

Let eta_x be the sensitivity indicator of pivot x. Suppose Q={z=a} has codimension r>=1, q=2^-r, and

    I_Z:=sum_(k in Z) I_k(f)<=r I_x(f),
    E:=Pr[eta_x != 1_Q]<=q/(16r).                      (B)

The first condition holds in particular for a maximum-influence pivot. Then the actual physical restriction on Z obeys

    boxed{ Delta_Z H(f)<=12 I_Z(f). }                  (C)

No derivative-sign hypothesis and no residual-dimension factor occur. The error is q/(16r), not q/16. The constant twelve is a local/class theorem under (B), NOT a universal FEI constant.

The proof is explicit. Edges incident to the distinguished control cell force I_Z>=rq-rE. The maximum/average-control condition then bounds internal punctured boundary by 2rE<=q/8. Punctured variance bounds the probability theta that the Fourier sample meets Z by 17q/4. A full-cube entropy-tensorization argument controls the genuine restricted-spectrum mixture information by (2/ln2)I_Z. The chain rule gives

    Delta_Z H<=h_2(theta)+theta log_2(2^r-1)+(2/ln2)I_Z.

The elementary bounds in ADDENDUM close this by 12 I_Z, with r=1,2 handled separately.

Consequently a centered physical-restriction-critical core with H/J>12 must satisfy, for every maximum-influence pivot and every coordinate subcube Q of codimension r>=1,

    Pr[eta_x != 1_Q]>2^-r/(16r).

The proof uses the exact folded drift D_Z=J-EJ_child>=I_Z and the critical inequality Delta_Z H>=R D_Z. This is a quantitative exclusion, not a proof that such cores do not exist.

## 5. The attempted fixed-relative strengthening is rigorously false

After deriving (C), I tried to replace q/(16r) by q/16. FIXED_RELATIVE_OBSTRUCTION.md constructs genuine centered Boolean functions with a UNIQUE maximum-influence pivot, support error at most q/16, and

    Delta_Z H / D_Z > (log_2 r-1)/25 -> infinity.       (D)

The same functions satisfy H<11I for r>=32. Thus (D) is NOT a counterexample to FEI; it forbids this particular uniform selected-block payment, even after its full folded refund.

Construction: take q=2^-r and delta=q/16, with r control bits z and r+4 selector bits w. On z=0 or w=0, f=(-1)^x. On w=e_k and z!=0, f=(-1)^z_k; elsewhere f=1. Then

    E=(1-q)delta,
    I_x=q+(1-q)delta,
    I_zk=q+delta-3qdelta<I_x.

For every nonzero selector Fourier frequency W, the singleton-control coefficient is delta[(-1)^W_k+q]. The r such atoms force conditional control entropy at least order r delta log r. Replace each w bit by a sufficiently deep balanced recursive majority: this leaves the control-block entropy decrement, control influences and support error unchanged while making every new leaf influence smaller than I_x. The resulting parent is centered and has x as unique largest pivot; its exact folded drift is I_Z+q. The all-r inequality (D) follows from the explicit spectrum.

This is the qualitative boundary the A/B workers need: a fixed-relative support approximation on ONE maximal row does not pay its whole defining control block uniformly. Additional joint-row information, exceptional-set geometry or another adaptive block is necessary. The account04 all-row rigidity theorem has extra joint hypotheses and is not refuted. The q/(16r) theorem above remains valid.

The initial REPORT also proves a more general dilution lemma: balanced substitution of all other coordinates preserves a bad designated singleton decrement while making that pivot uniquely maximal. Applied to the earlier bent/addressing family it refutes largest-influence local payment without any support hypothesis, while its actual H/I remains below four. Neither obstruction refutes an existential or globally amortized strategy.

## 6. Concrete next use across accounts

Primary recipients: account04/B18, account01/B18, and the B12/B13/B14 workers on interfaces A and B. Apply the actual paid near-support step (B)-(C) to a source-exact derivative stability result; preserve the codimension-dependent tolerance. If stability only supplies fixed-relative error, use the new obstruction to identify what additional joint information must be retained, rather than pretending the existing bridge closes.

The punctured log-Sobolev mixture estimate is reusable for exact support with arbitrary common residual functions. It avoids the ambient residual-dimension cost of naive entropy continuity and the need to bound the full quantum-ensemble entropy. For a primitive high-ratio core, either show a pivot/block meets (B), or construct a different paid elimination for the excluded configurations. Existence of a suitable elimination remains the missing universal implication.

The independent C-interface signed compiler/physical-flag route remains open at its actual finite-window/PSD contraction. The D-interface arithmetic remainder still needs its negative information credits. Do not conflate either with this local theorem or reopen the retired global phase/rank/l1 and sign-free scalar-profile targets indexed in RESEARCH_STATE.md.

## 7. Actual execution and collaboration evidence

The first checker covers all 65,812 Boolean functions of dimensions one through four, 145 generated exact-row families with 47 rational entropy certificates, and 768 directly materialized composition cases. The support extension additionally certifies all 1,967 qualifying rows in its stated exhaustive-three-bit/seeded-four-bit sample, and five positive-support-error examples through 18 variables with exact rational entropy bounds. The final obstruction checker materializes raw examples through 19 variables (524,288 inputs) and a direct retained-block substitution example. Finite entropy diagnostics are labeled separately from exact arithmetic and the written all-dimensional proofs. Large formal amplified dimensions are not truth-table enumerations. No independent review has occurred.

The all-account common-control pointer was committed at d2c57e60881050d3cae1176d9804a1a538831378, as eight added README lines with prior controls preserved. The shared order is at 4ba19644d6c44499692c5e16c29c3c02515f66de; the original research-state index is at 5b02cab94d0ea3563adc86da6831f25ad62ffcf5.

Actual post-order evidence was then read, not merely assumed:

* account03/B20 reports incorporation of the common pointer into all twenty existing account03 prompts under its own lease, with identities/timing/quiet flags preserved. This is a keeper report, not direct access to its native scheduler.
* account03/B12's report at scientific commit 77463c3ab63ad8718d4c5bfa45fd693b3769f289, blob ddf8baf96385418c56a91c48f62c04168633faaa, explicitly uses account04/B18's mixed-curvature theorem to derive a nonreusing normalized Palm-predictor KL bound. The substantive proof was actually read. Its acknowledgment names the new claim and next recipients.
* account02/B20's acknowledgment B20-20260921T200053Z-r11-joint.json reports B12-B18/B20 prompt incorporation and actual B16/B17 use of other-account results. It explicitly does not claim all post-update runs from configuration alone.

These records establish real cross-account uptake, not that every one of the eighty workers has already adopted the programme. Account01/account04 blanket adoption is not verified at the recorded snapshot. Earlier 18Z canonical login coverage was 20/17/17/20, or 74 check-in files, not 74 completed proofs. Missing logins are not proof of stopped schedules.

No native brain database ingestion or cognitive activation is claimed. All new scripts were accepted normally; no denied old upload was bypassed. Privacy review covered the explicit changed-file allowlist and mathematical content, not a complete repository scan. No schedules, permissions, visibility, benchmark gold or production verification statuses were changed by this research handoff. The existing common order supplies the continuation and progress-supervision path.
