# A056: balanced disjoint substitution and its physical restrictions

## exact target, quantifiers, hypotheses and units

For every finite k and pairwise disjoint physical coordinate blocks B_i, let g_i:{-1,1}^{B_i}->{-1,1}, let h:{-1,1}^k->{-1,1}, and put F=h(g_1,...,g_k). Physical coordinates are independent uniform signs. Entropy H is Shannon entropy in bits of the **entire** squared Fourier spectrum, including the empty coefficient; I is expected Fourier-set size, equivalently total flip influence. No restriction on the mean of h is needed. First assume every g_i is balanced: E g_i=0. Then

    E F = E h,
    Var F = Var h,
    H(F) = H(h) + sum_i Inf_i(h) H(g_i),
    I(F) = sum_i Inf_i(h) I(g_i),
    Inf_x(F) = Inf_i(h) Inf_x(g_i),  x in B_i.

This packet proves these identities, extends them to arbitrary child means, and identifies precisely what must be updated after a physical restriction. These are composition baseline identities, not a proof of unrestricted FEI. The complete analytic proof is local; independent acceptance is pending.

## sources actually read, revisions and theorem locators

Execution protocol revision 2026-10-11-execution-v2 governs this run. Campaign README, CURRENT_STATUS, claim/obstruction/packet registries, STREAM_NEXT_ACTIONS, the LaTeX plan and earlier B05/B09/B19 reports were inspected for scope and review guards. The advisory campaign CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS, NATIVE_MAPPING and source archive supply route context. Exact filenames and byte hashes are recorded in out/source_manifest.json; mathematical source excerpts are in out/source_excerpts.txt.

The threshold 38-page local text, Section 7, Proposition 7.1, equations (67)-(70), contains exact product-measure strong-entropy, influence and deficit identities. Section 7.3, Corollary 7.8, specializes to balanced children. Section 6.1 defines the strong entropy and product Fourier basis; these must not be confused with ordinary full Shannon entropy. Its earlier 29-page version and both percolation text versions were inspected for normalization/context. The percolation 30-page text Section 1.1 uses normalized product characters; its geometric hypotheses supply no premise to this proof. The source text files require legacy decoding rather than UTF-8; this affects reading, not the Fourier formulas. No novelty is claimed for known composition identities.

BOARD.md snapshot 2026-10-11 21:45 UTC reports no completed A056 stage. claude/B12/STREAM_NOTES.md was absent at initial inspection; no contrary lead direction was available. No shared files were edited. No registered theorem or unreviewed B09 assertion is used as a proof dependency.

## complete derivation or exact first unsupported line

### Balanced coefficient identity

Write g_i=sum_{U subset B_i} c_i(U) chi_U and h=sum_{T subset [k]} a(T) chi_T. Balance means c_i(empty)=0. For a physical Fourier set S, put S_i=S intersect B_i and T(S)={i:S_i is nonempty}. Expanding h after substitution, a term indexed by T can contribute to S only if T=T(S): unused blocks contribute the constant 1, and every used block has a nonempty set. Disjoint blocks make the union unique. Hence, including S=empty,

    Fhat(S) = a(T(S)) product_{i in T(S)} c_i(S_i).                  (1)

Parseval gives sum_{U nonempty} c_i(U)^2=1. Thus the spectral law is exactly the following experiment: sample T with probability a(T)^2; independently for each i in T sample a nonempty U_i with probability c_i(U_i)^2; output S=union U_i. Conversely S recovers T and every U_i. The experiment is bijective on positive-probability outcomes, so its entropy is H(h)+sum_i P(i in T)H(g_i). Since P(i in T)=Inf_i(h), this proves the entropy formula, with no latent-label correction or omitted empty atom. Its expected size is sum_i Inf_i(h)I(g_i). The probability a given x in B_i is included is Inf_i(h)Inf_x(g_i). Finally (1) at empty proves E F=E h and therefore the variance formula. Zero coefficients are simply omitted; 0 log(1/0)=0.

### Arbitrary means: reexpanded outer gate

Let m_i=E g_i and v_i=1-m_i^2. First absorb all deterministic children (v_i=0) into h by fixing those output coordinates to m_i. This is exact because a Boolean uniform-cube function of mean +/-1 is constant at every input. Reindex the remaining children; now v_i>0. Their independent output law is mu, with P(Y_i=+1)=(1+m_i)/2. In its orthonormal basis psi_i(y)=(y_i-m_i)/sqrt(v_i), write

    h(y)=sum_T a_mu(T) product_{i in T} psi_i(y).

Define P_mu(T)=a_mu(T)^2, w_i=sum_{T containing i} P_mu(T), H_mu(h)=H(P_mu), and I_mu(h)=sum_T |T|P_mu(T). These biased spectral influences w_i are not the ordinary unweighted pivotal probabilities. Indeed w_i=v_i E_mu[(D_i h)^2], where D_i h=(h(y_i=+1)-h(y_i=-1))/2 on the other outputs.

On the physical block,

    (g_i-m_i)/sqrt(v_i)=sum_{U nonempty} c_i(U)/sqrt(v_i) chi_U.

This again has zero empty coefficient and squared mass one. The same unique union argument gives

    Fhat(S)=a_mu(T(S)) product_{i in T(S)} c_i(S_i)/sqrt(v_i).       (2)

The child's nonempty spectral law is q_i(U)=c_i(U)^2/v_i. Its entropy K_i satisfies

    H(g_i)=h2(v_i)+v_i K_i,                                        (3)

because the empty atom has mass m_i^2=1-v_i. The exact full identities are consequently

    E F = E_mu h = a_mu(empty),       Var F=Var_mu h,
    H(F)=H_mu(h)+sum_i (w_i/v_i)[H(g_i)-h2(v_i)],                   (4)
    I(F)=sum_i (w_i/v_i) I(g_i),
    Inf_x(F)=(w_i/v_i)Inf_x(g_i), x in B_i.                        (5)

Equations (2)-(5) are valid at every finite dimension, for arbitrary nonconstant child means. All entropy terms are finite; no limiting assertion is needed. If every child was deterministic, F is constant and all entropies and influences are zero. Outer irrelevant coordinates have w_i=0 and require no child contribution. Balanced children give v_i=1, h2(v_i)=0 and the uniform outer law, recovering the first formulas.

For comparison with Proposition 7.1, the strong-entropy convention must be distinguished from conditional nonempty entropy. The convention that actually composes is Eplus(g)=sum_{U nonempty} c(U)^2 log2(1/c(U)^2) on uniform physical inputs, and Eplus_mu(h)=sum_{T nonempty} P_mu(T)log2(product v_i/P_mu(T)) on outputs. Then exactly

    Eplus(F)=Eplus_mu(h)+sum_i (w_i/v_i) Eplus(g_i).                (6)

It follows immediately from (2), with no Var(F) numerator. The conditional nonempty entropy in (3), namely H(g)-h2(Var(g)), is a different quantity. This run's main identities (1)-(5) deliberately use full H or conditional K, so do not depend on a strong-entropy naming convention. Define deficit delta=I-Var. Since sum_i w_i=I_mu(h), and Var(F)=Var_mu(h),

    delta(F)=delta_mu(h)+sum_i (w_i/v_i)delta(g_i).                 (7)

### Physical restrictions: what survives, and what changes

Fix actual physical coordinates W to a deterministic assignment rho. In each block replace g_i by g_i^rho=g_i restricted to W intersect B_i. Remaining inputs retain the independent uniform law and disjoint supports. Therefore (2)-(5) hold with the **new** means m_i^rho, variances v_i^rho, absorbed deterministic children, and the Fourier expansion of the reduced outer gate under the **new** output product law. They do not generally hold with old a_mu or old w_i. The balanced formulas are available at a reached branch when every remaining nonconstant child is balanced after absorption of constants. If only one child is restricted, all untouched initially balanced children remain balanced, but the changed child must be checked. Balance of that child is sufficient; it is not claimed logically necessary for accidental numerical equality in a special gate.

For a single initially balanced child j, write the uniform outer polynomial as h=A(y_-j)+y_j B(y_-j). Let a_T=Ahat(T), b_T=Bhat(T), and let the changed child's mean be m, variance v=1-m^2>0. Other children stay balanced. Recenter:

    h=A+mB+sqrt(v) psi_j B.

The new outer coefficients are a_T+m b_T on T not containing j, and sqrt(v)b_T on T union {j}. Thus squared weights include the coherent term 2m a_T b_T; they cannot be replaced by separate a_T^2 and m^2 b_T^2. Direct physical coefficients are (a_T+m b_T) product_{i in T} c_i(S_i) when S_j is empty, and b_T c_j^rho(S_j) product_{i in T} c_i(S_i) otherwise. The j-block physical multiplier is still sum_T b_T^2=Inf_j(h), because w_j^rho=v sum_T b_T^2. Other block multipliers generally change.

If v=0, fix outer y_j=m, giving the actual reduced polynomial A+mB. Do not divide by v. If m=0, the original outer coefficients remain valid. If the restriction is chosen adaptively using already observed physical values, each fixed leaf of the physical decision tree is a cylinder and its unrevealed coordinates are independent uniform. The formulas apply branchwise. An expectation over leaves must retain the branch-specific outer laws and weights; it cannot silently substitute the initial gate's spectrum. Conditioning only on a child output instead of fixing physical coordinates is not such a cylinder and need not leave a product physical law.

### Exact witness against retaining the old balanced formulas

Let h(y,z)=AND_2(y,z) in sign notation: +1 only when both inputs are +1. Its uniform spectrum has four coefficients of magnitude 1/2, so E h=-1/2, H(h)=2, and Inf_y(h)=Inf_z(h)=1/2. Let the first initially balanced child be majority on three signs (x,a,b), and the second be a fresh dictator z. Physically fixing x=+1 changes the first child to OR_2(a,b), with mean 1/2, variance 3/4, H=2 and I=1. The restricted F=AND_2(OR_2(a,b),z) has constant coefficient -1/4, z coefficient 3/4, and the other six coefficients of magnitude 1/4. Its spectrum is seven atoms 1/16 and one atom 9/16. Hence

    E F=-1/4,     I(F)=5/4,
    H(F)=4-(9/16)log2(9)=4-(9/8)log2(3).

Retaining old balanced formulas predicts E F=-1/2, I(F)=1, H(F)=3. All three predictions are false. For the entropy comparison, 3 > H(F) follows exactly from 3^9>2^8, with no floating point. The new output-biased gate weights are 1/16, 3/16, 9/16, 3/16 on empty, {y}, {z}, {y,z}. Thus w_y=3/8 and w_z=3/4, and (5) gives (3/8)/(3/4)+(3/4)=5/4. This is an actual Boolean physical restriction of an initially balanced substitution, not an arbitrary spectral law.

### Scope of consequences

Ordinary bounds H(h)<=C I(h) and H(g_i)<=C I(g_i) alone do not give the same C under the balanced identity: the outer H(h) remains an additional term. A sufficient balanced compositional invariant is H(q)<=C[I(q)-Var(q)] for the gate and all children. Since Var(g_i)=1, the formulas give H(F)<=C[I(F)-Var(F)]. This is a conditional consequence of explicitly stated gate/child bounds; those bounds are not proved for arbitrary Boolean functions here. After a physical restriction, either verify balance again or use product-biased identities and gate hypotheses at the new means. An arbitrary weighted threshold theorem established only for uniform inputs cannot be applied at newly biased child outputs. No overlap theorem, selector credit, or full FEI conclusion follows from these identities alone.

There is no unsupported line in the proofs of (1)-(5), (6)-(7), or the witness. General dimension-independent FEI remains open. The unpaid next research term is a quantitative entropy/influence payment for changed biased gate laws or overlapping-block coherent coefficients; it is not supplied by disjoint identities.

## executed validation with domain, arithmetic, commands and outputs

Frozen specification: out/FROZEN_SPEC.json, written before testing. Helper code/check.py uses an integer direct Walsh sum and Fraction arithmetic, verifies every physical coefficient, Parseval, mean, full entropy and influence. Entropy identities are checked exactly as rational linear combinations of logarithms of primes; equality of such vectors is a sufficient exact equality certificate, and no numerical logarithms are used. This is finite corroboration of the analytic proof, not an all-dimensional inference.

Pilot: 16 outer gates with two balanced two-bit children, all passed; measured computation time 0.011620600009337068 seconds. Main command: python -X utf8 code/check.py from this run directory. Its output is out/checks.json. Planned exhaustive domain: all 16 outer gates and all 16^2 two-bit-child pairs (4096 cases, including 576 balanced cases), all 16 gates and all six balanced two-bit children under all nine partial restrictions paired with a dictator (864 cases), and the explicit majority/AND witness. No symmetry reduction, random sampling, dimension escalation or heavy job. See checks.json for the actually completed count and runtime.

## proof dependencies and changed downstream conclusions

Proof dependencies are elementary Fourier expansion, Parseval, and finite Shannon chain rule; no registered unaccepted claim is imported. A057 must recenter the gate or retain the signed cross term after restriction. A059 must check balance at each internal node and branch. A060 can use the exact means/weights and witness to audit sharpness. A091 should independently reconstruct the coefficient identity and restriction witness with a different representation. B09/A045 should distinguish newly biased weighted-gate assumptions from uniform gate results. B20 may adopt this as baseline completion after review; it supplies no new full-FEI endpoint.

## one next mathematical action and independent reviewer

Next action: A057 derive an exact signed branchwise restriction remainder starting from coefficients a_T+m b_T and test its entropy payment on the majority/AND witness before averaging across branches. Independent reviewer: A091 (B19), with A087 available for the physical restriction hypothesis audit. These are named handoff consumers, not a claim that communication or acceptance has occurred.

## actual persistence receipts or precise save blocker

All artifacts reside only inside agents/A056/runs/20261011T214407Z-account05-A056-balanced-composition, with rolling STATUS.md, WORKLOG.md and LEARNED.md in agents/A056. out/receipts.json records sizes and hashes after completion. Shared indices and other agents' folders were untouched. Supervisor copying, remote mirror verification, independent review, and downstream adoption remain pending; local hashes certify only local persistence.
