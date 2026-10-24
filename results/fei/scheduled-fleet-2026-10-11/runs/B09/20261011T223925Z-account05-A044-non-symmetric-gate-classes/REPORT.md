# A044: equal-mean addressing and the exact unpaid mean-profile residual

## exact target, quantifiers, hypotheses and units

Full FEI remains OPEN. This run narrows the packet to a checked explicit nonsymmetric family: for every a>=0, the addressing gate F(z,y)=y_z has a address bits and 2^a distinct sign data inputs. The address bits have arbitrary independent Bernoulli probabilities q_i. All data inputs have one common sign mean m, with variance v=1-m^2. All coordinates are independent. For this class the sharp all-arity estimate is H_mu^+(F)<=4(I_mu(F)-Var_mu(F)). The common-mean restriction is part of the theorem, not something imposed after composition. Endpoints are included by restriction. Logarithms in H^+ are base two. I_mu is spectral expected degree, not unweighted pivotal count.

Artifact complete; narrowed mathematical result proved below and checked exactly; independent acceptance pending. The packet as broadly contracted is NOT complete: an all-product-bias gate result with unrestricted induced data means is not proved, and publication novelty is not established. B09's pending-review cap was already reached. This is a verification/narrow exploration and gap handoff, not a request to add another broad acceptance-ready candidate to the queue.

## sources actually read, revisions and theorem locators

Read EXECUTION_PROTOCOL.json in full (2026-10-11-execution-v2); README and CURRENT_STATUS; claim/obstruction registries; packet matrix and A044 contract; STREAM_NEXT_ACTIONS B09; relevant campaign plan A041--A045 and universal gaps. Read BOARD.md at stage start. B09 STREAM_NOTES.md did not exist at the supplied path. Read CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS and NATIVE_MAPPING; source ONE_BIT_ENDPOINT (physical addressing here differs from its spectral-address hypothesis). Read prior B09 report 20261011T195500Z-account01-B09-biased-restriction-uncertainty: its uncertainty bound and tensor-versus-composition guard are not assumed in this proof.

Threshold 38pp text: section 6.1 normalization; Proposition 7.1 equations (67)--(70), Corollary 7.2; section 8 addressing and Lemma 8.4. The scalar binary correction is already implicit in Lemma 8.4; the concavity proof below independently verifies that part of the existing baseline. Earlier threshold 29pp introduction was checked for version context. Percolation 30pp introduction, Theorems 1.1--1.3 and product normalization were checked, as was the earlier/alternate 31pp introduction; no percolation theorem is used. These are selected relevant portions, not a claim to have audited both papers in full.

Read reductions/paper/biased.tex normalization, exact composition and rare-tribes guard; the three weighted controls are imported as obstructions, not proof ingredients. Primary source checked online: O'Donnell--Tan, https://www.cs.cmu.edu/~odonnell/papers/fei-composition.pdf, Theorem 1, Proposition 2 and Theorems 2--3. Composition with the maximum gate constant is prior art; bounded arity in that source does not itself certify this unbounded-arity family. No match for 'address' occurred in that PDF, which is not a novelty certificate. Uniform addressing is already baseline; the delta here is the exact arbitrary-address-bias/common-data-bias ledger and the explicit heterogeneous mean residual. Source hashes are saved in out/SOURCE_HASHES.json.

## complete derivation or exact first unsupported line

For a Bernoulli coordinate with probability q use phi=(z-q)/sqrt(q(1-q)), and sigma^2=4q(1-q). Define P(S)=fhat(S)^2 and

H_mu^+(f)=sum_{S nonempty} P(S) log2(sigma_S^2/P(S)), Delta_mu(f)=sum_{S nonempty} (|S|-1)P(S).

Zero masses contribute zero. For each address c in {0,1}^a put r_ci=q_i if c_i=1 and r_ci=1-q_i otherwise, and p_c=product_i r_ci. Its cell indicator A_c has coefficient magnitude r_ci on an omitted coordinate and sqrt(q_i(1-q_i)) on an included coordinate. Thus, for T subseteq [a],

ahat_c(T)^2=p_c product_{i in T}(1-r_ci) product_{i notin T}r_ci.

Write each data sign y_c=m+sqrt(v) psi_c. Then F=m+sqrt(v)sum_c A_c psi_c. Every nonconstant Fourier set has exactly one data coordinate c, so there is no collision. Its squared coefficient is v ahat_c(T)^2. The empty squared coefficient is m^2. Consequently Var(F)=v, total data influence is v, and

Delta(F)=I_address(F)=v sum_i 2q_i(1-q_i).

The data variance sigma_c^2=v cancels exactly in the corrected logarithm. For a fixed c, the conditional law of T includes i with probability 1-r_ci. Using q_i(1-q_i)=r_ci(1-r_ci), that coordinate's mean corrected log is

ell(r)= (1-r)log2(4r^2)-2log2 r = 2(1-r)-2r log2 r.

Hence the complete formula, without omitted normalizers, is

H^+(F)=v sum_i [4q_i(1-q_i)-2q_i^2 log2 q_i-2(1-q_i)^2 log2(1-q_i)].

To bound it, put g(t)=t ln(1/t)/(1-t). Its integral representation is

g(t)=integral_0^1 t/[s+(1-s)t] ds.

For every s in (0,1), the integrand has second derivative -2s(1-s)/[s+(1-s)t]^3<=0. Therefore g is concave on (0,1). Jensen gives g(q)+g(1-q)<=2g(1/2)=2 ln2. Multiplying by q(1-q)/ln2 gives

q^2 log2(1/q)+(1-q)^2 log2(1/(1-q))<=2q(1-q).

Substitution proves H^+(F)<=8v sum_i q_i(1-q_i)=4Delta(F). If a>=1, all q_i=1/2 and v>0, equality holds: H^+=2av and Delta=av/2. Thus 4 is sharp. At a=0 the function is a dictator and both quantities vanish. Deterministic address bits are removed and unused data discarded; a deterministic common data value makes F constant. The same formulas extend continuously with t log t=0 at t=0.

### Exact heterogeneous-data decomposition and the remaining gap

Now allow arbitrary data means m_c with v_c=1-m_c^2, and define the real address mean profile h(z)=m_z. Then

F=h(z)+sum_c sqrt(v_c) A_c(z) psi_c(y_c).

The address-only spectrum of h and the distinct one-data-coordinate spectra are disjoint. Apply the same calculation, interpreting H_q^+(h) by the same coefficient formula for the bounded real function h. This gives the exact identities

H_mu^+(F)=H_q^+(h)+sum_c p_c v_c sum_i ell(r_ci),

Delta_mu(F)=Delta_q(h)+sum_c p_c v_c sum_i(1-r_ci).

Here Delta_q(h)=I_q(h)-Var_q(h)>=0 by degree counting. For every r in (0,1), -r ln r<=1-r, so

ell(r)<=(2+2/ln2)(1-r).

Thus the entire centered-data part is arity-uniformly paid at K0=2+2/ln2; the only unpaid part is the actual mean-profile entropy. The first unsupported line for an unrestricted address-gate theorem is a bound on H_q^+(h)-C Delta_q(h) using the centered-data slack with one absolute C. It is not valid to assert H_q^+(h)<=C Delta_q(h) for every bounded real h: a scaled dictator has positive H^+ and zero deficit.

More decisively, at deterministic data endpoints v_c=0, choose m_c=b(c) for any Boolean b on the address cube. Then F=b(z), and both identities reduce to those for b. At uniform address inputs, a universal H^+(address)<=C Delta(address) over all independent data biases would therefore imply H(b)<= (C+1/ln2)I(b): the omitted empty atom h0<=Var(b)/ln2<=I(b)/ln2. This is an actual Boolean embedding, not a relaxed spectral law. Consequently extending this gate to unrestricted data biases is at least full-FEI strength. Conversely no claim that full uniform FEI supplies the all-biased gate inequality is made.

### Composition corollary with every bias condition explicit

Consider a finite read-once formula on mutually disjoint physical child blocks. At each addressing node, all its data children have the same output mean under the ORIGINAL specified product input law; its address children may have arbitrary output means. Assume terminal children satisfy H^+<=C_leaf Delta. Then the root satisfies H^+<=max(4,C_leaf)Delta, with no factor depending on depth or any fan-in. For literal leaves C_leaf=0, the constant is 4.

For completeness, if an outer gate G receives child functions f_j with means mu_j and variances V_j>0, an occupied set of child blocks A and nonempty child subsets T_j determine exactly one physical Fourier set. Its coefficient is Ghat(A)product_{j in A} fhat_j(T_j)/sqrt(V_j). Taking corrected logs and expected degrees gives

H^+(G(f))=H^+(G)+sum_j alpha_j H^+(f_j),

Delta(G(f))=Delta(G)+sum_j alpha_j Delta(f_j), alpha_j=I_j(G)/V_j>=0.

Each gate and child term is therefore paid by the maximum constant; induction proves the corollary. Constant children are frozen before division. Deterministic address children reduce fan-in; common deterministic data means make the node constant. Equal data means are checked at the induced law at every node, not presumed to persist under arbitrary changes of the leaf law or arbitrary physical restrictions. For uniform physical input and balanced data subtrees, all addressing outputs are balanced and the corollary yields H<=4(I-1). If the root is unbalanced, H<=4(I-Var)+h0<=4I using h0<=Var/ln2. Generic read-once formulas over these gates with unrestricted inherited data biases are not covered.

## executed validation with domain, arithmetic, commands and outputs

Frozen spec: out/FROZEN_SPEC.json, helper A044-address-v1; a=0,1,2; each address q and common data r in {1/8,1/2,7/8}; all 39 tuples, no symmetry reduction. At most six variables. Direct truth-table expectations with Fraction independently recover every squared Fourier coefficient; no square roots or floating point. Formal prime-log dictionaries verify the entropy formula exactly. Strict finite signs use rational atanh intervals with explicit geometric remainder. Uniform equality is checked symbolically, not via a tolerance. Physical pivotal probability times 4q(1-q) is checked independently against each spectral coordinate influence.

Executed: python -X utf8 runs/20261011T223925Z-account05-A044-non-symmetric-gate-classes/code/check_address.py

Output: PASS, 39 cases, 2,193 recorded assertions, 1.54 seconds. One further final case-count assertion precedes persistence. Memory estimate 32 MB; no >300 MB job, no GPU, no dimension escalation. out/CHECK.json records all cases. The all-arity theorem is proved analytically above; a finite grid is not the finite-to-infinite bridge. No heterogeneous grid or composition truth-table experiment is claimed.

## proof dependencies and changed downstream conclusions

The narrowed gate proof uses the standard biased basis and elementary concavity only. Composition is independently reconstructed here from the exact noninterfering expansion, agreeing with threshold Proposition 7.1 and O'Donnell--Tan Theorem 1. It uses neither the unreviewed B09 uncertainty theorem nor A041/A042 conjectural endpoints. Weighted-threshold physical-TC, coefficient-one pivotal-credit and every-coordinate conditional-TC controls cannot refute this argument: it asserts none of those payments and uses exact spectral identities; these weighted gate families are not common-mean address gates. Their counterexamples remain intact. The low-selector-energy regime is genuinely included: q_i approaching 0 makes I_address/a arbitrarily small while the corrected payment remains uniform.

A059/A060/A091 may consume the equal-mean composition condition; A041/A045 and B20 should retain the mean-profile residual and arbitrary Boolean endpoint embedding. No downstream acceptance, messaging, brain ingestion, shared-index update or mirror save is claimed.

## one next mathematical action and independent reviewer

Next: independently review the already queued B09/A041 normalization claims, then test a proposed structural condition on mean profiles that excludes arbitrary Boolean endpoint tables while remains closed under actual induced biases. Do not repeat the common-mean baseline. Primary reviewer A091, alternate A090. The equal-mean condition is a useful narrowed theorem, but is not a solution to the full packet's unrestricted inherited-bias demand.

## actual persistence receipts or precise save blocker

All required artifacts and rolling files are saved inside A044; code/output and source hashes accompany them. out/RECEIPTS.json records file sizes and SHA256 values generated after the report and JSON artifacts. No filesystem save blocker. Supervisor copy, independent acceptance and durable mirrors remain unverified.

## Universal bridge

This stage moves C020 whole-set witness cost on common-mean address gates by paying the complete corrected spectral label cost at the sharp constant 4, uniformly through vanishing selector energy and all allowed arities. Its unrestricted extension leaves exactly H_q^+(h) with the displayed centered-data slack; deterministic Boolean mean tables recover an arbitrary FEI instance. No universal gap is closed. The shortest next route is to review the queued bias normalization and then constrain/pay this real mean-profile residual in a composition-stable way; merely adding another zero-profile gate class would not address full FEI.
