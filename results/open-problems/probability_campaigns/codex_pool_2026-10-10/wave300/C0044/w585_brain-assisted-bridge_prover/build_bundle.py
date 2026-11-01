"""Build an author-only draft and a reviewable insertion diff; no live writes."""
import json
from pathlib import Path
import difflib

ROOT = Path(__file__).resolve().parent
NS = "probability.randomenvironment"
source = {
    "source_id": "owner-campaign:w585:C0044-density-bridge-20261010",
    "url": "urn:owner-campaign:w585:C0044-density-bridge-20261010",
    "revision": "2026-10-10-author-only-independent-review-pending",
    "license": "owner-own-work; DRAFT, no theorem promotion or novelty claim",
    "excerpt": None,
}

rows = [
    ("posterior", "rwre-directional-escape-full-environment-posterior", "DRAFT RWRE directional escape posterior martingale",
     "For a static nearest-neighbor RWRE and fixed nonzero l, define A_l={X_n dot l tends to +infinity}, q(omega)=P_0^omega(A_l), and tau_x omega(y,e)=omega(x+y,e). If F_n reveals the full environment and the first n steps, then q(tau_Xn omega)=P_0(A_l|F_n), converging almost surely and in L1 to 1_A_l. DRAFT deduction; independent review pending.",
     ["static nearest-neighbor Markov RWRE", "fixed deterministic nonzero direction", "full environment belongs to F_n"]),
    ("positivity", "rwre-quenched-escape-positivity-does-not-imply-one", "DRAFT RWRE quenched positivity is weaker than zero-one",
     "For stationary ergodic strictly elliptic static nearest-neighbor RWRE, p=P_0(A_l)>0 implies q(omega)=P_0^omega(A_l)>0 almost surely; p<1 implies q<1 almost surely. Thus a mixed p would have 0<q<1 almost surely. Positivity alone does not prove p=1: the zeros of q and 1-q propagate by harmonicity, while their values need not be translation invariant. DRAFT deduction; independent review pending.",
     ["stationary ergodic environment law", "strict ellipticity", "static nearest-neighbor RWRE", "fixed deterministic direction"]),
    ("density", "rwre-environment-seen-incoming-finite-time-density", "DRAFT incoming density of the environment seen from a RWRE",
     "Let P be a translation-stationary law of static nearest-neighbor environments on Z^d, tau_x omega(y,e)=omega(x+y,e), and mu_n the annealed law of tau_Xn omega from 0. For every n>=0, d mu_n/dP=f_n, where f_n(omega)=sum_{|x|_1<=n} P_{-x}^omega(X_n=0); f_n>=0 and E_P f_n=1. The formula gives finite-time absolute continuity, not a stationary law or uniform integrability. DRAFT deduction; independent review pending.",
     ["translation-stationary environment law", "static nearest-neighbor RWRE", "integer n>=0"]),
    ("concentration", "mixed-directional-transience-forces-incoming-density-concentration", "DRAFT mixed directional transience forces density concentration",
     "In stationary ergodic strictly elliptic static nearest-neighbor RWRE let q=P_0^omega(A_l), p=E_P q, and f_n=d Law(tau_Xn omega)/dP. If 0<p<1, then B_epsilon={q<=epsilon or q>=1-epsilon} has b_epsilon=P(B_epsilon)->0 as epsilon decreases to zero, while a_n=integral_B_epsilon f_n dP->1. For r>1, E_P f_n^r>=a_n^r/b_epsilon^(r-1) whenever b_epsilon>0. Hence E_P f_n^r->infinity. No time-diverging subsequence of f_n or its Cesaro averages is uniformly integrable. DRAFT deduction; independent review pending.",
     ["stationary ergodic strict-elliptic static nearest-neighbor RWRE", "fixed deterministic direction", "0<P_0(A_l)<1"]),
    ("criterion", "directional-rwre-zero-one-subsequential-density-uniform-integrability", "DRAFT directional zero-one bridge from incoming-density uniform integrability",
     "For stationary ergodic strictly elliptic static nearest-neighbor RWRE on Z^d, define f_n(omega)=sum_{|x|_1<=n}P_{-x}^omega(X_n=0) and F_N=(1/N)sum_{n<N}f_n. EXTRA ASSUMPTION: either {f_nj} or {F_Nj} is uniformly integrable for a deterministic sequence n_j or N_j tending to infinity. Then P_0(X_n dot l tends to +infinity) is zero or one for every fixed nonzero l. A uniform L^r bound, r>1, on that subsequence is sufficient. IID and strict positivity alone do not discharge the extra assumption in this packet. DRAFT conditional proof; independent review pending; C0044 remains unresolved here.",
     ["stationary ergodic environment law", "strict ellipticity", "static nearest-neighbor RWRE", "subsequential uniform integrability of incoming densities or their Cesaro averages"]),
    ("counterexample", "normalized-densities-need-not-be-uniformly-integrable", "DRAFT refutation: normalized densities need not be uniformly integrable",
     "On ([0,1],Lebesgue), g_m=m times indicator_[0,1/m] is a nonnegative probability density for each m. If m>K, its mass above K equals one, so the family is not uniformly integrable; integral g_m^r=m^(r-1) for r>1. Thus first-moment normalization and individual absolute continuity cannot justify a uniform integrability bridge. This family is not claimed to be an RWRE realization or a counterexample to C0044. DRAFT exact counterexample; independent review pending.",
     ["Lebesgue probability measure on [0,1]", "positive integers m"]),
    ("gap", "c0044-missing-incoming-density-uniform-integrability-bridge", "DRAFT C0044 missing incoming-density bridge",
     "C0044 asks for P_0(A_l) in {0,1} in a static iid strictly elliptic nearest-neighbor environment on Z^d, d>=3. The conditional incoming-density argument requires subsequential uniform integrability of f_n=sum_{|x|_1<=n}P_{-x}^omega(X_n=0), or its Cesaro averages. The elementary bound f_n=O(n^d) and E_P f_n=1 do not prove that condition. Shared sites and adaptive path selection prevent treating incoming probabilities as independent factors. Current openness is UNKNOWN because a September 23, 2026 primary preprint claims resolution but has not been independently checked in this packet. This is a gap record, not a theorem.",
     ["static iid strictly elliptic nearest-neighbor RWRE", "d>=3", "fixed deterministic nonzero direction", "external claimed resolution unverified here"]),
]
entries = [{"key":key,"namespace":NS,"logical_name":logical,"kind":"concept","title":title,
            "statement":statement,"proof_text":None,"assumptions":assumptions,
            "domain":"probability theory","source":dict(source)} for key,logical,title,statement,assumptions in rows]
by_key = {e["key"]:e for e in entries}
links = [
    ("concentration","posterior","depends_on","The conditional posterior tends to an indicator, so the walk-sampled mass near the endpoint values tends to one."),
    ("concentration","positivity","depends_on","Strict interior quenched probabilities make the original mass near zero and one tend to zero."),
    ("concentration","density","depends_on","The change of measure identifies the integrals to which Holder applies."),
    ("criterion","concentration","depends_on","Uniform absolute continuity contradicts the concentration forced by a mixed escape probability."),
    ("gap","criterion","cites","The sufficient criterion names the exact additional density assumption still missing."),
    ("gap","counterexample","cites","The exact normalized-density example rejects normalization as a substitute for the missing condition."),
]
relations = []
for a,b,kind,reason in links:
    relations.append({"from_key":a,"to_key":b,"kind":kind,
                      "rationale":reason+' Supporting from-card: "'+by_key[a]['statement']+'" Supporting to-card: "'+by_key[b]['statement']+'"'})
bundle = {"spec":"mathbrain-draft-v1","author_agent":"w585","bundle_slug":"c0044-density-bridge-20261010","entries":entries,"relations":relations}
text = json.dumps(bundle,ensure_ascii=False,indent=2)+'\n'
(ROOT/'bundle_001.json').write_text(text,encoding='utf-8')
(ROOT/'patches').mkdir(exist_ok=True)
target = '~/math-brain-inbox/w585/bundle_001.json'
diff = ''.join(difflib.unified_diff([],text.splitlines(keepends=True),fromfile='a/'+target,tofile='b/'+target))
(ROOT/'patches'/'01_c0044_density_bridge.diff').write_text(diff,encoding='utf-8')
print(json.dumps({'entries':len(entries),'relations':len(relations),'draft':str(ROOT/'bundle_001.json'),'live_store_changed':False}))
