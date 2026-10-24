# A047 boundary search: sharp fixed-child endpoint and unequal-bias signs

## exact target, quantifiers, hypotheses and units

Freeze B09's actual one-selector ledger, M=H(S_X|S_Y), J=H(S_Y)-E H(child spectrum), and debt J-M. The tax-free J<=M helper is already refuted; the new target is the sharp possible coefficient in a repaired endpoint tax, not another refutation of that retired statement. For every fixed finite pair of Boolean children g,h in a common fixed product-biased orthonormal basis, select h with probability p and g otherwise, independently of the data. All entropies are in bits. Prove a universal bound on lim (J-M)/(p log2(1/p)), characterize sharpness, and certify boundary signs. Data dimension and data biases are fixed in taking this limit; no uniform remainder in those parameters is asserted.

Result: the exact coefficient is 2Z+2c-2 <= 1/2-2(c-1/2)^2 <= 1/2, where c=E(gh) and Z=sum_{G_T=0} H_T^2. The maximum is attained by genuine Boolean children, including balanced children and a dictator typical child. For disjoint child spectral supports M=J=h2(p) exactly for all p. The sharply unequal AND endpoint q->0 at fixed p has debt 4p(1-p)q log2((1-p)/p)+O_p(q^2 log(1/q)). Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2 was read in full. README, CURRENT_STATUS snapshot 2026-10-11T20:06:24Z, claim/obstruction/packet registries, STREAM_NEXT_ACTIONS, campaign plan and A047 contract were consulted. The board snapshot is 2026-10-11 21:55 UTC. B10/STREAM_NOTES.md was absent, so no lead direction was inferred. A046's board entry already identifies its AND lower-bound intake; this stage adds the arbitrary-child upper coefficient and zero-debt classification.

Original B09 REPORT.md sections 2, 4, 5, 8, run 20261011T195500Z-account01-B09-biased-restriction-uncertainty, source commit adb671ffcda143fa68347806bb96e8c305621a7d, supplies the frozen ledger. The repair report verification/B09_interval_repair_20261011/REPORT.md supplies the signed-division warning. Neither the B09 uncertainty theorem nor an upstream A046 claim is a proof dependency here.

The supplemental CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS and NATIVE_MAPPING were consulted; sources/ONE_BIT_ENDPOINT.md, BLOCK_RESTRICTION_IDENTITY_2026-09-18.md and GAMMA_ENDPOINT_LEDGER.md were read for distinction between exact identities and universal payment. The threshold 38pp and earlier 29pp text introductions/Theorem A, and the percolation 30pp and other 31pp introductions/Theorems 1.1-1.2 were read for scope and normalization. These papers are context only; their remaining proofs were not reconstructed and no theorem from them is assumed. The source-byte manifest records hashes, not claims of full proof audit. No web or priority search was needed for this self-contained calculation; no novelty claim is made.

## complete derivation or exact first unsupported line

Write G_T,H_T for normalized child Fourier coefficients. Parent squared masses on residual label T and selector label 0,1 are

    a_T=((1-p)G_T+pH_T)^2,
    b_T=p(1-p)(H_T-G_T)^2,
    q_T=a_T+b_T=(1-p)G_T^2+pH_T^2.

For finite lists, positive limiting masses have entropy change O(p); masses p*r+O(p^2) have entropy r*p*log2(1/p)+O(p); masses O(p^2) have entropy O(p^2 log(1/p)). Thus H(q) gains coefficient Z=sum_{G_T=0}H_T^2, while H(a,b) gains Z+D, where D=sum_{G_T!=0}(H_T-G_T)^2. Averaged child entropy has only a linear change. Therefore J has leading coefficient Z, M has D, and the debt has Z-D. By Parseval D+Z=2-2c, so debt coefficient=2Z+2c-2. Cauchy-Schwarz on g's support gives c^2<=1-Z; substitute and complete the square to obtain <=1/2-2(c-1/2)^2. Equality in the final bound requires c=1/2 and H restricted to g's spectral support equals G/2.

On two fair data bits take g=1 and h=1-2*1_{Y1=Y2=0}. Then c=1/2, Z=3/4, D=1/4: the coefficient is 1/2. Multiply both by a fresh fair character: this permutes residual Fourier labels, preserving M,J,c,Z and makes both children balanced. The typical child becomes a dictator. Hence any universal replacement tax with fixed-child endpoint coefficient strictly less than 1/2 is false, even when both children are balanced. This strengthens endpoint information but is not a family with unbounded H/I.

Disjoint supports give marginal law q made from two distinguishable pieces, with weights 1-p,p. Hence J=h2(p). In a G-only fiber b_T/q_T=p; in an H-only fiber b_T/q_T=1-p, hence M=h2(p) as well. A constant and a balanced child are an important instance. Equal children give M=J=0; opposite children give J=0,M=h2(4p(1-p)).

For biased AND, its four squared masses are ((1-2pq)^2,4p(1-p)q^2,4p^2q(1-q),4p(1-p)q(1-q)). At fixed q the rare-p coefficient is 4q(1-2q). At fixed p and q->0 put v=4pq(1-q). Grouping the Y-present parent masses gives H(parent)=h2(v)+v*h2(p)+O_p(q^2 log(1/q)); the remaining X-only mass is O_p(q^2). Therefore J-M=2h2(v)-H(parent)-p*h2(4q(1-q))=4pq[log2(1/p)-h2(p)]+O_p(q^2 log(1/q)). Since the bracket equals (1-p)log2((1-p)/p), the stated expansion follows. It is positive to leading order for p<1/2 and negative for p>1/2.

The first unsupported line is a dimension-independent finite-p improvement, for example J-M <= (1/2)[h2(p)+log2 max(p,1-p)]. The endpoint theorem does not prove that inequality; the O_{g,h}(p) constants depend on the fixed pair and basis. It also does not control simultaneous p,q endpoints or pay a composition/stopping tree. Full details are in BOUNDARY_ASYMPTOTICS.tex.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was written before the first run. No symmetry reduction was used. All actual sign truth tables on n=0,1,2,3 were paired in order: 4,16,256,65536 cases, totaling 65,812. Integer fast Walsh agrees with an independently coded direct character sum. Parseval, inverse transform, physical correlation and edge influence counts are checked exactly. Pair debt coefficients and the Cauchy and 1/2 upper bounds use integers/rationals only.

| Data bits | Pairs | Positive coefficients | Zero coefficients | Maximum | Balanced-pair maximum |
|---|---:|---:|---:|---|---|
| 0 | 4 | 0 | 2 | 0 | no balanced children |
| 1 | 16 | 0 | 12 | 0 | 0 |
| 2 | 256 | 32 | 64 | 1/2 | 0 |
| 3 | 65,536 | 1,472 | 10,336 | 1/2 | 1/2 |

Five named boundary pairs were checked at p=1/8,1/64,1/1024: constant/quarter defect, constant/balanced, dictator/balanced quarter surgery, equal, opposite. FROZEN_SPEC_UNEQUAL.json then froze five biased-AND cases: p=1/8 or 1/1024 crossed with q=1/64 or 1/65536, and p=3/4,q=1/65536. Exact Fraction spectra and rational entropy intervals certify the asserted strict signs; intervals enclosing zero for the zero-debt controls are supported by the analytic identity, not reported as numerical equalities.

The independent log implementation range-reduces x=2^k*r with 1<=r<2. For z=(r-1)/(r+1), ln(r)=2 sum_{j=0}^{39} z^(2j+1)/(2j+1)+R and 0<=R<=2*z^81/(81*(1-z^2)). Divide nonnegative numerator intervals by the positive ln(2) interval and add exact k. All endpoints, interval sums and differences are rational; decimal approximations are display only. Twenty-five powers of two and zero-mass entropy are regression checks. Saved interval numerators/denominators in out/results.json and out/unequal.json are the certificates; no floating sign is accepted.

Commands: `python -X utf8 code/boundary.py` and `python -X utf8 code/unequal.py` from this run directory (equivalently the full relative paths used in execution). Both return PASS. Observed initial compute time was 0.6263 seconds and unequal search 0.0578 seconds; tool launch overhead is distinct. Peak RSS was not measured; estimated live data is under 100 MB, well below the 300 MB memok threshold. No heavy job, automatic dimension increase, GPU, background process, git or external write was used. Final replay output and source hashes are persisted in out.

## proof dependencies and changed downstream conclusions

Only finite entropy expansion, orthonormal Parseval and Cauchy-Schwarz enter the new proof. No unreviewed campaign claim is assumed. B09's additive tax has rare-selector coefficient 1; actual Boolean debt needs at least coefficient 1/2, while every fixed-child endpoint has coefficient at most 1/2. This establishes a genuine Boolean lower-bound scale rather than relying on an upper bound's asymptotics. Balancedness and a typical dictator do not remove that logarithm. This does not prove that coefficient 1/2 is valid at finite p or uniformly in a changing family. The already known tax-free refutation remains unchanged.

## one next mathematical action and independent reviewer

Derive a finite-p fiber envelope using the two actual normalized child coefficient vectors and their overlap constraint, then determine whether the half-tax candidate survives uniformly in dimension and moving biases. A092 is the primary independent reviewer; A087 is alternate. A049 can extract the balanced witness; A050/A042 can use the coefficient to constrain a repaired tax; A071 can use spectral-support novelty to target the next finite search. This handoff is saved locally; no message was sent to another agent and no review is claimed.

## actual persistence receipts or precise save blocker

All required run files, the requested BOUNDARY_SEARCH_PLAN.json and BOUNDARY_ASYMPTOTICS.tex, scripts, interval certificates and source-hash manifest are saved inside A047. STATUS.md, WORKLOG.md and LEARNED.md are current. The finishing script validates exact protocol field sets and hashes persisted files. Missing B10 lead notes are an access fact, not a mathematical blocker. Supervisor copy, GitHub/brain ingestion, independent acceptance and downstream use remain unverified.

## Universal bridge

This stage moves C019 stopping-tree payment by identifying the sharp fixed-child leading logarithmic debt that any product-biased physical-selector repair must retain: coefficient at least 1/2, with a general endpoint upper bound of 1/2 and an exact zero-debt class. It neither bounds the whole expected path cost nor supplies nonreusing tax transport or terminal entropy payment. NEXT seeks a uniform finite-p envelope, because the current pair-dependent remainder is the first obstacle to inserting this bound into a universal stopping-tree ledger; that is a direct missing bridge rather than another isolated FEI class theorem.
