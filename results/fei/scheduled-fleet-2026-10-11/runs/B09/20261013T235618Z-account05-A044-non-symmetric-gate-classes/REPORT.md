# A044: sharp unequal-mean mux, arity-uniform closure, and the two-mean residual

## exact target, quantifiers, hypotheses and units

Full FEI remains OPEN. The B09 lead asks A044 to drop the common-data-mean hypothesis in two-mean address gates. This stage finishes the unfinished predecessor's exact one-address-bit optimization and checks the transfer to arbitrary two-mean address tables. For every fixed interior address bias q, the three-input Boolean mux F(z,y0,y1)=(1-z)y0+z y1 has

    sup_{-1<m0,m1<1} H_mu^+(F)/Delta_mu(F)
      = K(q) = 2+2[1+g(max(q,1-q))]/ln2,
    g(t)=t ln(1/t)/(1-t).

The exact supremum over all three interior input biases is K*=2+4/ln2. It is finite and sharp. On independent-cell address tables of arbitrary arity whose data means take two values, the profile-scale entropy is paid from the actual centered-data deficit. The exact remaining charge is t^2 H_q^+(b), where b is the Boolean table assigning the two means and t=(m1-m0)/2. The same root deficit is spent only once.

An all-product-bias family with no equal-data-mean condition is also explicit: gates selecting between two distinct data wires according to the parity of a arbitrary-fan-in selector block. These gates and genuine disjoint read-once formulas built from them satisfy H^+<=K*Delta, uniformly in all physical and induced biases, depth and fan-in. Literals, AND/OR and parity may be included at the same maximum constant. This is a sharp quantitative application of known composition; neither the class's existence nor publication novelty is claimed new. All entropy is corrected entropy in bits; Delta=I-Var is spectral deficit, and I is spectral expected degree, not unweighted pivotal count.

Artifact complete locally. The fixed-q mux target is resolved on the page; unrestricted arbitrary-arity two-mean address tables retain universal biased FEI+ difficulty. Independent review/adoption remain pending. This is completion/repair of the already active A044 candidate plus a scoped independent review of A042's majority main theorem, respecting the B09 cap on new broad candidates.

## sources actually read, revisions and theorem locators

Read BOARD.md snapshot 2026-10-13 23:49 UTC, B09 STREAM_NOTES.md v2 still dated 2026-10-11 23:33 UTC, own STATUS and LEARNED, and EXECUTION_PROTOCOL.json v2 in full. The board shows A041/A045 already reviewed A042's binary theorem; it was source-read rather than redundantly recertified. Read A042 stage-2 REPORT/CLAIMS (20261012T002547Z) and stage-3 REPORT/CLAIMS (20261013T221414Z), especially majority theorem (T), sections 1--3. Read A041 stage-2 REPORT (20261011T232825Z) for its one-exceptional class and unpaid mixed-reference term; this theorem is not assumed here.

Recovered own stage-2 frozen spec, code, proof checkpoint and output (20261012T040658Z). The output is PASS: 245 cases, 7,690 exact assertions, 10.3426 computation seconds. The predecessor contains a supervisor .final marker but lacks the four protocol files; it is left unchanged. This new run supplies the source-complete recovered proof/handoff and byte-for-byte source copies, with out/RECOVERY_RECEIPTS.json. No earlier output was silently relabeled an independent review.

Threshold 38pp: normalization section 6.1; Proposition 7.1/Corollary 7.2; Lemma 7.5 (parity/AND/OR constants); Lemma 8.4 scalar correction. Re-read the parity scalar proof and independently reconstruct it below. Primary literature checked: O'Donnell--Tan, https://www.cs.cmu.edu/~odonnell/papers/fei-composition.pdf, Theorem 1 and Proposition 2. The source establishes maximum-constant disjoint composition and a bias-uniform bounded-arity bound. Its searchable text has no 'multiplexer' match; this and the bounded web search are not novelty certificates. The sharp mux formula is proved directly here. Source bytes/hashes and read locators are in out/SOURCE_RECEIPTS.json.

## complete derivation or exact first unsupported line

### 1. Unequal-data-mean mux: exact spectrum and fixed-q supremum

Let z be Bernoulli q and let independent data signs have means m0,m1 and variances vj=1-mj^2. Put d=|m1-m0| and W=v0+v1. The actual normalized biased spectrum has exactly these possible masses:

    P(empty)=((1-q)m0+q m1)^2,
    P(z)=q(1-q)d^2,
    P(y0)=(1-q)^2 v0,       P(z,y0)=q(1-q)v0,
    P(y1)=q^2 v1,           P(z,y1)=q(1-q)v1.

Sets containing both data coordinates have zero mass. Thus Delta=q(1-q)W. Under interior data biases W>0. The address singleton contributes q(1-q)d^2 log2(4/d^2), interpreted as zero at d=0. With ell(r)=2(1-r)-2r log2 r, the remaining complete corrected entropy is (1-q)v0 ell(1-q)+q v1 ell(q). Dividing the sum by Delta gives the exact ratio

    R=2+[d^2 ln(4/d^2)+2v0 g(1-q)+2v1 g(q)]/[W ln2].       (1)

No ordinary Shannon entropy or missing empty-atom term is used in (1).

The integral representation g(t)=integral_0^1 t/[s+(1-s)t]ds shows g is strictly increasing on (0,1). Its limits are g(0)=0 and g(1)=1. For d in [0,2], write u=(m0+m1)/2; |u|<=1-d/2. Hence

    W=2-2u^2-d^2/2 >= d(2-d).                             (2)

The inequality ln x<=x-1, applied to x=2/d, gives

    d^2 ln(4/d^2)=2d^2 ln(2/d)<=2d(2-d)<=2W,              (3)

with d=0 treated continuously. Combining (1)--(3) and the weighted-average bound proves R<K(q) at every interior data pair. Strictness follows from (3) for d>0 and from its unused positive allowance when d=0.

To prove the exact lower bound, fix q<=1/2 and take m0=-1+e, m1=1-e^2, with e decreasing to zero. Then v0=2e-e^2, v1=2e^2-e^4, W=2e+e^2-e^4, and d=2-e-e^2. Consequently v0/W->1 and d^2 ln(4/d^2)/W->2, by ln(1+x)/x->1. Equation (1) tends to K(q). For q>=1/2 exchange the variance roles: m0=-1+e^2, m1=1-e. All data biases remain interior. The limiting contracted table is a literal; its zero deficit is not divided. Thus K(q) is a supremum over genuine interior laws, not an entropy ratio assigned to a degenerate function.

Finally g(t)<1 gives R<K*=2+4/ln2. The joint interior path q=e, m0=-1+e, m1=1-e^2 tends to K*. The recovered rational certificate at e=1/65536 proves R>777/100. At q=1/2 the exact fixed-selector supremum is 4+2/ln2, whereas the common-data-mean slice had maximum 4. If q is actually deterministic, contract it and obtain the selected literal with H^+=Delta=0; K(q)'s endpoint limit is not a value of a 0/0 quotient.

### 2. Arbitrary-arity independent-cell two-mean tables: exact root ownership

Let a selector bits have arbitrary independent probabilities q_i, and let c index all 2^a cells. Each cell has its own independent data sign. Its mean is m0 or m1 according to a Boolean label profile b(c) in {-1,1}. Put u=(m0+m1)/2, t=(m1-m0)/2, h=u+t b, r_ci=P(z_i=c_i), p_c=product_i r_ci and v_c=1-(u+t b(c))^2.

The mean-only spectrum and the distinct one-data-coordinate spectra are disjoint. Direct expansion yields

    H^+(F)=t^2 H_q^+(b)+t^2 Var_q(b)log2(1/t^2)+E_c,
    Delta(F)=t^2 Delta_q(b)+D_c,
    E_c=sum_c p_c v_c sum_i ell(r_ci),
    D_c=sum_c p_c v_c sum_i(1-r_ci).                       (4)

At t=0 the scale term is zero by continuity. These are the previously checked unequal-mean ledger, now supplied with a complete payment of its scale normalization.

For each selector coordinate i, averaging over its other coordinates gives exactly

    (D_c)_i=q_i(1-q_i) E_{-i}[v_{b(z_i=0)}+v_{b(z_i=1)}].

A crossing edge of b has the two different labels, so its bracket is W=v0+v1. A noncrossing edge has a nonnegative bracket. The actual spectral coordinate influence of b is 4q_i(1-q_i)P(edge crosses). Therefore

    D_c >= W I_q(b)/4.                                   (5)

Equation (3), with d=2|t|, gives t^2 ln(1/t^2)<=W/2. Poincare Var(b)<=I(b) and (5) pay the scale term by 2D_c natural units. Also -r ln r<=1-r gives (ln2)E_c<=(2ln2+2)D_c. Adding these two charges gives the arity-uniform repaired interface

    H^+(F)<=t^2 H_q^+(b)+K*D_c.                           (6)

Together with (4), a certified H_q^+(b)<=C_b Delta_q(b) implies H^+(F)<=max(C_b,K*)Delta(F). The scale charge and the centered-data charge are subdivisions of the one D_c reserve; no copy of t^2 Delta(b) is also spent on them. The 96 recovered exact profile cases cover all 16 two-address-bit Boolean label tables at three bias vectors and two mean pairs.

### 3. Two reused data wires: different coefficient, unrestricted induced means

The controlled two-wire gate M_b(z,y0,y1) selects y0 or y1 according to b(z), and is a genuine disjoint composition mux(b,y0,y1). It is not the independent-cell gate in (4). Let the actual output probability of b be q_b. The coefficient multiplying the selector profile is

    beta=I_selector(mux)/Var(b)=(1-m0 m1)/2,               (7)

because, conditional on data values, the outer sign derivative in its selector is (y1-y0)/2. Its squared expectation is (1-m0m1)/2. Exact disjoint composition therefore gives

    H^+(M_b)=H^+(mux at q_b,m0,m1)+beta H_q^+(b),
    Delta(M_b)=Delta(mux at q_b,m0,m1)+beta Delta_q(b).     (8)

The initial new pilot incorrectly imported t^2 from the mean-only sector in (4); the first parity-mux fixture detected it. For q_selector=(1/8,1/4,1/2), m0=-1/2,m1=1/2, the correct beta is 5/8, not 1/4. The preserved code/spec and exact diagnosis are in out/PILOT_FAILURE.md. The corrected code uses (7). This repair changes no recovered independent-cell theorem and supplies no repair to A042's majority proof.

For any profile with corrected constant C_b, (8) gives constant max(K(q_b),C_b), hence max(K*,C_b). In particular arbitrary-fan-in parity profiles have C_b=2/ln2, so every parity-controlled mux has constant K*. All physical input laws are permitted; there is no common-mean or equal-output restriction to be imposed after composition. The family includes a=1, where the sharp lower-bound path above makes K* optimal for the family.

For completeness the elementary parity bound is independently reconstructed. Put a_i=(E sign_i)^2, Z=product_i a_i, R=sum_i(1-a_i)-1+Z. Parity has Delta=R and natural corrected entropy Omega=sum_i(a_i-Z)ln(1/a_i). Appending another squared mean a changes R by (1-a)(1-Z), and changes Omega by (1-a)Z ln(1/Z)+a ln(1/a)(1-Z). Each of the two terms is at most (1-a)(1-Z), using -s ln s<=1-s. Starting from one literal, where R=Omega=0, proves Omega<=2R. Zero squared means follow by continuity. This is Lemma 7.5's established scalar mechanism, not a new parity claim.

At a generic disjoint composition G(f1,...,fk), let V_j=Var(fj)>0 and alpha_j=I_j(G)/V_j. Occupied child blocks A and their nonempty physical subsets T_j uniquely determine each output set; its coefficient is Ghat(A)product_j fhat_j(T_j)/sqrt(V_j). Splitting the corrected logarithm and counting physical degrees proves

    H^+(G(f))=H^+(G)+sum_j alpha_j H^+(fj),
    Delta(G(f))=Delta(G)+sum_j alpha_j Delta(fj).          (9)

All alpha_j and deficits are nonnegative. Induction applies the maximum constant to every finite read-once tree of parity-controlled muxes, literals and established AND/OR/parity gates, with arbitrary arities and no depth factor. Constant children are frozen before division. An outer mux with a constant selector reduces to one data child; with both data children constant it is a constant or signed selector. These contractions are explicitly checked. The original product law determines every induced mean used in (7)--(9).

On uniform physical inputs H=H^++h0, with h0=-m^2 log2(m^2)<=Var/ln2. Since K*>1/ln2, ordinary H<=K*I follows. A balanced root satisfies H<=K*(I-1). The broad existence of such read-once closure is prior O'Donnell--Tan; the delta is the explicit sharp mux constant, unequal-mean normalization and the complete frozen contraction checks.

### 4. Scoped independent review of A042's majority main theorem

The reviewed source is A042-SHARP-MAJORITY3-BIASED-ENDPOINT@1, statement hash 396cfaaabff2fa337f7a038ca4380cbede25d84a6ccd96032829a36dbecad11e. Only theorem (T), sections 1--3, is accepted in this review; the independent-rate 400-error certificate and full endpoint/edge classification are not accepted by this record.

Independently integrate the sign polynomial 2x1x2+2x1x3+2x2x3-4x1x2x3-1. If sigma_i^2=4p_i(1-p_i), normalized coefficients are c_i=p_j+p_k-2p_jp_k, c_ij=(1-2p_k)/2 and c_123=-1/2. With pair mass B and triple mass T=product_i sigma_i^2/4, Delta=B+2T. Indicator pivotal derivatives give sum_i sigma_i^2 c_i(1-c_i)=2B+3T. The scalar c^2 ln(1/c^2)<=2c(1-c) gives singleton entropy <=4Delta-2T. A pair's remaining natural logarithmic cost is (sigma_i^2 sigma_j^2/4)z ln(1/z), z=(1-2p_k)^2; -z ln z<=1-z makes this at most the very same T. Adding the three pair costs and the triple cost produces

    E <= (4+ln4)Delta-(ln4-1)T.                           (10)

This reconstructs the exact shared-triple ownership and favorable remainder. It uses no numerical optimization or source code from A042. The independent centered-moment implementation checks (10) on 27 cases, including fair inputs and zero pair coefficients. Verdict: HOLDS for the global inequality (10), no substantive repair supplied, reviewer A044 is not a contributor to the original version. This reduces an unpaid review obligation but does not mark the entire bundled boundary theorem accepted.

### 5. Exact first unsupported universal line

For arbitrary label tables b, (6) still contains t^2 H_q^+(b); (8) still contains beta H_q^+(b). There is no dimension-independent payment for either inherited Boolean profile entropy by its profile deficit in this run.

This is actual universal difficulty, not just a loose estimate. In independent-cell addressing choose means -s,+s according to any fixed Boolean profile b, s<1. All data biases are interior. Put v=1-s^2, A_q=2sum_i q_i(1-q_i), and S_q=sum_i[4q_i(1-q_i)-2q_i^2 log2 q_i-2(1-q_i)^2 log2(1-q_i)]. The exact identities are

    Delta(F_s)=s^2 Delta_q(b)+v A_q,
    H^+(F_s)=s^2 H_q^+(b)+s^2 Var_q(b)log2(1/s^2)+v S_q. (11)

For every fixed b with positive deficit the ratio tends to its own corrected ratio as s increases to one. Thus the supremum on all arbitrary-profile two-mean address tables over all arities and product laws equals the universal product-biased corrected FEI+ supremum, as an extended real number: one direction is class inclusion, and the reverse direction follows from (11). No claim that full uniform FEI implies universal biased FEI+ is made. Uniform b at deterministic endpoints already gives full uniform FEI difficulty. Rarity, two means, or an arity-uniform centered-data payment alone cannot close the conjecture.

NEXT must pay an actual higher-degree profile/prime residual, with its inherited terminal cost retained. Another mean-only base case would not move that universal obligation. No divergent corrected ratio or Boolean unbounded ordinary H/I family has been found.

## executed validation with domain, arithmetic, commands and outputs

Recovered predecessor validation: out/RECOVERED_STAGE2_CHECK.json, 245 cases, 7,690 exact assertions, 10.3426 computation seconds. This contains the exact mux spectrum/formal-log formula, strict K(q) interval signs, 24 boundary records, and all 96 two-mean profile identities and (5)--(6). It is byte-for-byte copied, not rerun or claimed newly independent. Copies and source hashes are in out/RECOVERY_RECEIPTS.json.

New helper v3.1: out/FROZEN_SPEC.json. Maximum physical dimension is six. Nonconstant compositions: all 27 triples from AND2/OR2/XOR2 at two six-coordinate product laws (54 cases). Constant-selector: 36 cases. Constant-data: 24 cases. Majority main-theorem review: the 3^3 grid (27 cases). Parity-controlled mux: four three-coordinate selector bias vectors and two unequal mean pairs (8 cases). Total 149. No symmetry reduction or dimension escalation. Spectra use exact centered-moment Fraction arithmetic without square roots; entropy identities are exact rational prime-log dictionaries. All strict comparisons use range-reduced 32-term atanh rational intervals with positive geometric remainder. Numerical decimal displays are not proof premises.

Executed bootstrap command: python -X utf8 runs/20261013T235618Z-account05-A044-non-symmetric-gate-classes/code/bootstrap.py. It copies only own sources/output and generates the shared arithmetic helper. Executed check command: python -X utf8 runs/20261013T235618Z-account05-A044-non-symmetric-gate-classes/code/check_composition.py. Final validation record: out/CHECK.json. Final output: PASS, 149 cases, 3626 exact assertions, 37.8829 computation seconds. Certified K* enclosure: (7.770780163555,7.770780163556).

The initial v3 failure and exact correction are preserved. Repeating the frozen domain was justified by the changed coefficient, not by a desire for a larger search. Both attempts are bounded pilots; memory estimate 64 MB, peak not measured, no job over 300 MB, no GPU, no background service, and no automatic dimension growth. The continuum supremum and depth-independent closure are analytic proofs; finite passing cases are verification only.

## proof dependencies and changed downstream conclusions

The mux optimum and independent-cell scale repair use direct Boolean Fourier expansion, mean geometry, log inequalities and Poincare. Disjoint composition is reconstructed and agrees with O'Donnell--Tan and threshold Proposition 7.1. The parity constant is reconstructed from Lemma 7.5's scalar induction. The existing binary review is consumed with its source and statement hash; the majority main inequality is independently reviewed, and its unreconstructed boundary certificate remains pending. No unreviewed tax or general prime inequality is a premise.

A060/A091 can use the all-bias mux constant at arbitrary induced data means. A041/A045 receive (5)--(6), which precisely divides one actual centered-data deficit between scale normalization and conditional data entropy. B20 receives the distinction between independent-cell t^2 and reused-wire beta, and the exact arbitrary-profile embedding (11). The three weighted-threshold physical-TC/pivotal-credit controls remain valid: no such helper is asserted here. The two-mean class is not presented as easier than universal biased FEI+.

## one next mathematical action and independent reviewer

Have A091/A090 independently reconstruct (1)--(3), sharpness, and the scale ownership (5)--(6). Next mathematical action: use the degree-resolved majority singleton credit now independently checked in (10) as a test of A041's mixed-sector reference on the next source-specified prime profile, and preserve t^2 Delta(b) as a terminal reserve in (6). Isolate the first failed normalized higher-degree reference rather than repeating binary, mux, or majority endpoint grids. This follows the lead's all-prime bridge and the current B09 frontier.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, byte-identical PACKET_DELTA.json, code/, frozen specifications, exact outputs, recovery records, review scope and persistence receipts are saved in this new A044 run. The earlier .final-marked run is preserved unchanged despite its missing protocol handoff. STATUS.md is two lines, WORKLOG.md appends recovery/repair, and LEARNED.md retains the exact coefficients and scope. out/PERSISTENCE_RECEIPTS.json plus out/VALIDATION.json verify local hashes, schemas and compatibility bytes. All files are below 20 MB. No local save blocker; remote mirrors, adoption, supervisor copying and new independent acceptance are unverified.

## Universal bridge

This stage moves the B09 lead's all-prime corrected-product bridge by closing the unequal-data-mean mux with the sharp constant 2+4/ln2, completing its unrestricted induced-bias composition payment, and repairing arbitrary-arity two-mean scale debt from exactly one centered-data deficit; it also independently validates the majority shared-triple inequality. The remaining universal charge is precisely the inherited Boolean profile entropy t^2 H^+(b) or beta H^+(b), and (11) proves the arbitrary-profile two-mean class retains the full biased FEI+ supremum. No universal C018/C019/C020/C024 payment is claimed. NEXT tests one actual higher-degree prime/mixed reference against the preserved profile reserve, which targets this surviving universal entropy cost rather than collecting another isolated gate constant.
