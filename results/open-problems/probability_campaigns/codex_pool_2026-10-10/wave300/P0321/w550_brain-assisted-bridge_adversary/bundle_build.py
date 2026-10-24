"""Prepare a small draft and patch; submission is a separate explicit step."""
import difflib
import json
import pathlib

root = pathlib.Path(__file__).resolve().parent

def entry(key, name, title, statement, assumptions, artifact):
    return {"key": key, "namespace": "probability.point-processes", "logical_name": name,
            "kind": "concept", "title": title, "statement": "DRAFT CONCEPT; mathematical review and ingestion are tracked separately. "+statement,
            "proof_text": None, "assumptions": assumptions, "domain": "probability and statistical mechanics",
            "source": {"source_id": "owner-p0321-w550-20261010:"+key,
                       "url": "urn:owner:probability-research:w550:20261010:"+artifact,
                       "revision": "author-checked-draft-2026-10-10-v1",
                       "license": "owner-own-work (campaign deduction; see separate independent-review receipts)",
                       "excerpt": None}}

entries = [
 entry("phase-bridge", "riesz-hexatic-microscopic-correlation-bridge-gap", "Riesz hexatic phase: microscopic bridge remains missing",
       "The P0321 target asks for an intermediate two-dimensional repulsive Riesz-gas phase with rapid positional and slow sixfold orientational correlations. The primary phase discussion in Lewin, arXiv:2202.09240v2, VI.2 does not specify one fully quantified existence theorem. A proof must specify exponent, Gibbs law, density/temperature interval, observable, and correlation quantifiers. A spatial nearest-cell Delaunay bond mark and a two-particle Palm mark are distinct observables. No microscopic orientational algebraic lower bound for a Riesz state is established by the present draft; current openness is UNKNOWN, with no novelty claim.",
       ["Campaign bridge analysis, not a solved phase theorem.", "Primary source is cited and paraphrased, not reproduced."], "ATTEMPT.md"),
 entry("additive-route", "fixed-additive-error-algebraic-order-transfer-rejected-route", "Rejected route: fixed additive correlation accuracy",
       "Candidate inference to be tested: if an effective radial correlation A has a positive algebraic lower tail and an actual radial correlation B satisfies sup_r |A(r)-B(r)|<=epsilon for a fixed epsilon>0, then B also has a positive algebraic lower tail. This candidate inference is refuted by the accompanying bounded-field construction; the error must instead be controlled relative to the vanishing signal, or another sufficient estimate must be proved.",
       ["The candidate inference uses only bounded stationary-field correlations and fixed positive additive accuracy.", "No additional Gibbs or geometric identification premise is supplied."], "INDEPENDENT_DERIVATION.md"),
 entry("additive-counterexample", "bounded-stationary-fields-additive-accuracy-without-algebraic-tail", "Bounded-field obstruction to fixed additive transfer",
       "For every 0<a<=2 and R>=1, stationary isotropic unit-modulus fields on R^2 realize A(r)=(1+r^2)^(-a/2) and B_R(r)=A(r)exp(-(r/R)^2). A uniform phase and a Gaussian wavevector conditionally of covariance 2G I_2, with G~Gamma(a/2,1), give A; adding an independent Gaussian wavevector of covariance 2R^-2 I_2 gives B_R. Their uniform difference is <=R^-a, while r^a A(r)->1 and r^b B_R(r)->0 for every b>0. Arbitrarily small fixed additive error therefore permits destruction of the whole algebraic tail. These fields are not asserted to be Riesz Gibbs states or geometric bond fields.",
       ["0<a<=2 and R>=1; r>=0 is Euclidean separation.", "Abstract stationary fields; no ergodicity or particle Gibbs specification is required for this construction."], "INDEPENDENT_DERIVATION.md"),
 entry("relative-bridge", "scale-relative-correlation-error-sufficient-algebraic-transfer", "Sufficient scale-relative correlation comparison",
       "Let a,r0>0, 0<c<=C and 0<=delta<c. Suppose for every r>=r0 a real effective correlator satisfies c r^-a<=A(r)<=C r^-a and a microscopic complex correlator in the same state and at the same parameters satisfies |B(r)-A(r)|<=delta r^-a. Then (c-delta)r^-a<=Re B(r)<=|B(r)|<=(C+delta)r^-a. This follows from Re B>=A-|B-A| and the triangle inequality. Uniform finite-volume estimates pass to a fixed-distance limit before r tends to infinity. The required comparison has not been derived for microscopic Riesz bond order.",
       ["The same state, parameter values, distances, and observable conventions are compared.", "For the finite-volume route all constants are volume independent and fixed-distance correlations converge."], "INDEPENDENT_DERIVATION.md"),
 entry("density-route", "density-pair-decorrelation-does-not-imply-process-mixing-route", "Rejected route: density pairs determine process mixing",
       "Candidate inference to be tested: rapid decay of the truncated particle-density two-point function, together with fast empty-disk probabilities, implies quantitative alpha mixing of full point-process restrictions in separated windows. This inference is refuted by the accompanying stationary Cox process. A density pair function is a second-order statistic; alpha mixing controls all measurable local events. Neither a Gibbs specification nor ergodicity of that counterexample is claimed.",
       ["Stationarity, simplicity, finite positive intensity, and fast void tails.", "No independent process-mixing hypothesis may be silently substituted by a density pair bound."], "PAIR_DENSITY_COUNTEREXAMPLE.md"),
 entry("cox-counterexample", "stationary-cox-compact-density-correlation-without-window-mixing", "Cox process: finite-range density correlation with persistent block dependence",
       "A uniform shifted unit-square grid and a fair global bit B choose conditionally iid cell intensities. For B=0 their law is {1/2,3/2} with equal weights; for B=1 their law is {1-1/sqrt(2),1,1+1/sqrt(2)} with weights {1/4,1/2,1/4}. A conditional Poisson process with these positive intensities is stationary, simple, locally finite, and has intensity 1. Both mark laws have mean 1 and variance 1/4, giving rho_T^(2)(h)=(1/4)(1-|h1|)_+(1-|h2|)_+ and V(t)<=exp(-(1-1/sqrt(2))pi t^2). For integer k>=3, vacancy in [0,1)^2 and its translate by (k,0) has covariance Var(q_B(U))>=exp(-3)/(4*98304^2)>0, hence alpha is bounded below by that constant. Conditional independence given B,U is used explicitly. This is not a Riesz Gibbs construction, isotropic phase, or ergodic example.",
       ["Conditionally iid cell marks given the global regime; uniform independent grid phase.", "Alpha is the event-supremum dependence coefficient of the two window restrictions."], "PAIR_DENSITY_COUNTEREXAMPLE.md")
]
relations = [
 {"from_key":"phase-bridge", "to_existing_logical":"math:probability.core:open-problem-p0321-existence-of-a-hexatic-phase-for-two-dimensional-riesz-gases", "kind":"cites", "rationale":"The existing end asks to 'Prove or refute the intermediate hexatic phase' and explicitly labels current status unverified. The draft end identifies the unresolved microscopic correlation bridge and preserves that uncertainty. The existing logical ID was read from the population store in read-only mode."},
 {"from_key":"additive-counterexample", "to_existing_logical":"math:probability.core:attempt-p0321-existence-of-a-hexatic-phase-for-two-dimensional-riesz-gases", "kind":"semantic_association", "rationale":"The existing end says a 'vanishing rotation-averaged one-point order parameter cannot rule out the proposed phase' and has 'No independent review'. The draft end supplies a separate bounded-field obstruction to fixed additive two-point transfer. Both warn about invalid order-parameter inferences; neither constructs a Riesz phase."},
 {"from_key":"additive-counterexample", "to_key":"additive-route", "kind":"refutes", "rationale":"The source end realizes 'uniform difference <=R^-a' and 'r^b B_R(r)->0 for every b>0'; the target end claims that fixed 'sup_r |A-B|<=epsilon' preserves an algebraic lower tail. Choosing R large meets any fixed tolerance and contradicts that conclusion."},
 {"from_key":"cox-counterexample", "to_key":"density-route", "kind":"refutes", "rationale":"The source end has 'rho_T^(2)(h)=(1/4)(1-|h1|)_+(1-|h2|)_+' and 'alpha is bounded below' at every distant integer translate; the target end tries to infer full process mixing from rapid density pair decay and void tails."},
 {"from_key":"relative-bridge", "to_key":"additive-counterexample", "kind":"semantic_association", "rationale":"The source end requires '|B-A|<=delta r^-a' with 'delta<c'; the target end demonstrates that a fixed error bound alone loses an algebraic tail. The relation concerns the error scale; it does not assert a microscopic Riesz comparison exists."},
 {"from_key":"relative-bridge", "to_key":"phase-bridge", "kind":"semantic_association", "rationale":"The source end is a sufficient comparison in 'the same state and at the same parameters'; the target end identifies the missing 'microscopic orientational algebraic lower bound'. The implication remains conditional until the actual Riesz observable and comparison are derived."},
 {"from_key":"cox-counterexample", "to_key":"phase-bridge", "kind":"semantic_association", "rationale":"The source end separates density pair decay from full window dependence; the target end requires precise positional and geometric orientational observables. This blocks an inference, and supplies no Riesz phase theorem."}
]
bundle = {"spec":"mathbrain-draft-v1", "author_agent":"w550", "bundle_slug":"p0321-correlation-transfer-obstructions-w550-v1", "entries":entries, "relations":relations}
(root/"bundle_001.json").write_text(json.dumps(bundle, ensure_ascii=False, indent=2), encoding="utf-8")
patch_dir = root/"patches"
patch_dir.mkdir(exist_ok=True)
helper = (root/"target_source_fallback.py").read_text(encoding="utf-8")
patch = "".join(difflib.unified_diff([], helper.splitlines(keepends=True), fromfile="a/~/.claude/dreaming/target_source_fallback.py", tofile="b/~/.claude/dreaming/target_source_fallback.py"))
(patch_dir/"01_target_source_fallback.diff").write_text(patch, encoding="utf-8")
print(json.dumps({"entries":len(entries), "relations":len(relations), "all_new_results_kind":"concept", "patch":str(patch_dir/"01_target_source_fallback.diff")}))
