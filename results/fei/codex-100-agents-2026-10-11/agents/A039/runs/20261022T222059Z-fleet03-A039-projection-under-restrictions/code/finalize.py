from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json
R=Path(__file__).resolve().parents[1]
OWN=R.parents[1]
BASE=OWN.parents[1]
PROTO=Path("math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json")
def read(p):return p.read_text(encoding="utf-8")
def write(p,s):p.write_text(s,encoding="utf-8")
def dump(p,v):write(p,json.dumps(v,indent=2,ensure_ascii=False)+"\n")
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(read(p))
C=load(R/"out/CHECK.json");P=load(R/"out/PILOT.json");proto=load(PROTO)
assert C["summary"]["status"]==P["summary"]["status"]=="PASS"
assert C["script_sha256"]==digest(R/"code/check.py")
assert C["summary"]["admitted_history_pairs"]==126 and C["summary"]["boundary_pairs"]==13
# Independent readback of the signed repair: do not import the generator.
repairs=[]
for row in C["results"]:
 if row["n"]<3:continue
 n=row["n"];e=F(1,1<<n);I0=1+(n+1)*e/2;If=e/2
 A=tuple(map(F,row["A"]));H0=tuple(map(F,row["H0"]))
 net=(A[0]+F(7,16)+H0[0]-4*(I0-If),A[1]+F(7,16)+H0[1]-4*(I0-If))
 assert net[1]<0
 assert F(row["mixed_x_bank"])==2*e
 # Complete canonical source inequality, not root spectral entropy alone.
 headroom=(4*I0-H0[1]-A[1]-F(7,16),4*I0-H0[0]-A[0]-F(7,16))
 assert headroom[0]>F(3,16)
 repairs.append({"n":n,"net_before_positive_part":[str(x) for x in net],"source_headroom_after_old_booking":[str(x) for x in headroom],"net_bill":["0","0"],"remaining_actual_bank":str(2*e)})
dump(R/"out/SIGNED_READBACK.json",{"status":"PASS","independent_rational_predicates":16,"fixtures":repairs,"scope":"Readback validator uses source-bound exact rational endpoints; no copied checker imports or floating signs."})
claim1="A039-RARE-CORE-ADAPTIVE-DATA-SOURCE-PAYMENT"
claim2="A039-RARE-CORE-MIXED-CONTROLLER-SEPARATED-LIABILITY-OBSTRUCTION"
statement1=("For every integer n>=3, e=2^-n, and actual uniform Boolean priority gate F_n(x,a,b,z)=(-1)^a if x=0, v_n(z) if x=b=1, +1 otherwise, where v_n=1-2*1{z=0}, let M be the original completed canonical matched-empty/marginal occupancy projection and A=D_2(P||M). After querying a and any finite adaptive fresh-data-only stopping history, retaining x,b and every physical outcome/reference-only row, put D=H0-EHleaf, R=I0-EIleaf, S=E(4Ileaf-Hleaf) and L=A+[D-4R]_+. Then S-L>7/16 bits. Hence every prior booking 0<=omega<=7/16 is paid from the same final owner with S-L-omega>0; no intermediate reference or bank is renewed.")
statement2=("For the same F_n and original M, every n>=16 admits the actual history query a, all n data coordinates, then x, keeping b and all actual terminals. Its final entropy is zero, final influence e/2, final surplus S=2e, and separated complete liability L=A. The genuine canonical A>(n^2/2-n-2)e>=110e, hence S-L<-(n^2/2-n-4)e<0 even with no earlier booking. This refutes arbitrary-mixed-history extension of the separated-liability payment only. In contrast, for any history with supplied actual S>=0, old omega<=7/16 and an unspent original query allowance 4R, the signed bill N=[A+omega+D-4R]_+ obeys S-N=min(S,4I0-H(M)-omega)>=0 in this rare family; root headroom is >3/16. This does not authorize reusing spent query allowance or a fresh-reference reset.")
sources=[
 PROTO, BASE/"BOARD.md",BASE/"claude/B08/STREAM_NOTES.md",
 OWN/"runs/20261014T055326Z-fleet05-A039-projection-under-restrictions/PROOF.md",
 OWN/"runs/20261014T055326Z-fleet05-A039-projection-under-restrictions/REPORT.md",
 OWN/"runs/20261014T025407Z-fleet05-A039-projection-under-restrictions/RARE_OBSTRUCTION.md",
 BASE/"agents/A038/runs/20261022T210124Z-fleet03-A038-occupancy-term-audit/ANALYTIC_PROOF.md",
 BASE/"agents/A038/runs/20261022T210124Z-fleet03-A038-occupancy-term-audit/REPORT.md",
 BASE/"agents/A088/runs/20261014T053751Z-fleet05-A088-booleanity-referee/REPORT.md"]
source_manifest=[]
for path in sources:
 assert path.is_file(),str(path)
 source_manifest.append({"path":str(path),"sha256":digest(path),"bytes":path.stat().st_size})
dump(R/"out/SOURCE_RECEIPTS.json",source_manifest)
deps=[{"source":str(sources[3]),"sha256":digest(sources[3]),"scope":"finite coherent KL telescope; reconstructed in PROOF.md"},
 {"source":str(sources[6]),"sha256":digest(sources[6]),"scope":"separated-liability min identity only; independently rederived, no use of balanced-family theorem"}]
claims=[]
for cid,statement,ps in [(claim1,statement1,["PROOF.md"]),(claim2,statement2,["MIXED_CONTROLLER_OBSTRUCTION.md","SIGNED_REPAIR.md"])]:
 claims.append({"claim_id":cid,"version":1,"exact_statement":statement,
 "hypotheses":["Actual uniform Boolean F_n; base-2 entropy and KL; original completed canonical occupancy reference, not full product TC.","All physical outcomes and full terminal costs retained; fair extension on source-zero reference rows.","Prior bookings counted once. Signed repair additionally requires the specified query allowance to be genuinely unspent."],
 "statement_sha256":hashlib.sha256(statement.encode("utf-8")).hexdigest(),"contributors":["A039"],
 "proof_source":[str(R/p) for p in ps]+[str(R/"code/check.py"),str(R/"out/CHECK.json")],
 "proof_dependencies":deps,"review_records":[{"reviewer":"A039","kind":"author adversarial checks","verdict":"analytic proof plus exact finite certificates; external review pending; Lean not run after memok WAIT"}],
 "status":"PROVED_UNREVIEWED","supersedes":[],"refutes":[] if cid==claim1 else ["Extension of A+[D-4R]_+ payment from adaptive data-only to arbitrary mixed controller histories"],
 "first_unproved_line":"Universal arbitrary-core source eligibility and a prescribed fresh-reference reset using the same remaining original allowance; neither is supplied here.",
 "next_consumers":["A038","A047","A050","A064","A088","A091","A092","A094","A096","A097"]})
dump(R/"CLAIMS.json",claims)
runid=R.name
progress={
 "protocol_revision":proto["revision"],"run_id":runid,"stream":"B08","packet_id":"A039",
 "gap_id":"C024-SAME-SOURCE-HISTORY-ELIGIBILITY","attempt_id":"rare-core-adaptive-history-and-mixed-controller-v1",
 "method":"Exact spectral/physical restriction identities, canonical variational competitor, signed whole-history compensation, rational certificate readback.",
 "mathematical_delta":"For every n>=3, every a-first adaptive data-only history pays complete original source and any old booking<=7/16 from SAME actual final owner. For every n>=16, next x refutes separated-liability extension with A/e>n^2/2-n-2; signed source-inclusive payment repairs that artificial barrier if original query allowance is unused.",
 "deliverable_status":"COMPLETE_LOCAL","mathematical_status":"SCOPED_AUTHOR_PROOF_EXACT_CHECKS_PASS; FULL_FEI_OPEN; INDEPENDENT_REVIEW_PENDING; NOT_LEAN_CHECKED",
 "claim_versions_used":[{"source":x["source"],"sha256":x["sha256"],"scope":x["scope"]} for x in deps],
 "claims_created_or_changed":[{"claim_id":x["claim_id"],"version":1} for x in claims],
 "source_artifacts":[str(R/p) for p in ["PROOF.md","MIXED_CONTROLLER_OBSTRUCTION.md","SIGNED_REPAIR.md","FROZEN_SPEC.json","code/check.py","out/CHECK.json","out/SIGNED_READBACK.json","out/VALIDATION_REPAIRS.json","out/SOURCE_RECEIPTS.json"]],
 "next_consumers":["A038","A047","A050","A088","A094","A096","A097"],
 "next_action":"Carry one prescribed descendant fresh-reference reset through the signed source-inclusive account; explicitly subtract all prior bookings and reserve only the genuinely unspent part of original 4R. A088/A094 reconstruct the variational competitor and source-zero history; A038/A047/A050 inspect liability ordering.",
 "stagnant_substantive_attempts":0,
 "blockers":["Full FEI remains open: arbitrary-core root source cross-entropy is unpaid.","Fresh canonical/product reset introduces a transfer bill outside original inherited A.","Lean admission WAIT; no formal certification.","External independent review, supervisor copies, registry adoption and mirrors unverified."],
 "packet_ids":["A039"]}
dump(R/"PROGRESS.json",progress);dump(R/"PACKET_DELTA.json",progress)
s=C["summary"];ps=P["summary"]
rows={r["n"]:r["inherited_full_history"]["source_zero_rows"] for r in C["results"] if "inherited_full_history" in r}
report=f"""# exact target, quantifiers, hypotheses and units

For the actual rare-core priority gate F_n specified in PROOF.md, retain the ORIGINAL completed canonical occupancy projection M, including its matched empty mass. Let A=D(P||M), D=H0-EHleaf, R=I0-EIleaf and S=E(4Ileaf-Hleaf). All entropy/KL units are bits. Prove or refute same-owner payment of L=A+[D-4R]_+ after physical restrictions, with every old booking and actual terminal retained. n>=3 for the adaptive data theorem; n>=16 for the all-dimensional mixed-controller obstruction. Full FEI remains OPEN.

# sources actually read, revisions and theorem locators

Execution protocol read in full, revision {proto['revision']}; BOARD snapshot 2026-10-22 22:17 UTC; B08 lead v2 dated October 11. Own last populated run 20261014T055326Z, PROOF equations (1)-(4), REPORT and rolling learned facts; rare-core obstruction in run 20261014T025407Z. A038 new run 20261022T210124Z ANALYTIC_PROOF section 1 equation (2) and REPORT; its balanced-root theorem is not assumed for this biased core. A088 run 20261014T053751Z REPORT supplies the warning to retain conditional and terminal bills. Exact local bytes are pinned in out/SOURCE_RECEIPTS.json.

Campaign README/status, relevant registry/packet/next-action entries, B08 campaign-plan material, supplement CAMPAIGN/CLAIMS/COUNTEREXAMPLES/SEED_LEMMAS/NATIVE_MAPPING and source listing were consulted. The four context paper text versions were consulted at restriction/shared-data/relative-entropy locators; no new paper theorem is used. The current user deadline 2026-10-23 14:49 UTC supersedes old protocol dates. Later marker-only fleet05 folders were not counted as mathematical stages. The wake warned of stale owner-context notes; a conversational alert preceded reliance on them.

# complete derivation or exact first unsupported line

PROOF.md supplies a complete analytic proof: after a-first exposure every adaptive data-only history is represented by the two remaining dimensions on its unique all-zero paths. Exact actual spectra give S>2-(3/2)2^-n. The canonical entropy gap A=H(M)-H0 and H(M)<=2+(n+1)h2(2^(-n-1)), together with S-L=min(S-A,Sroot-A), prove S-L>7/16 uniformly for every n>=3. An old booking omega<=7/16 leaves positive remaining capacity; neither reference nor owner is renewed.

MIXED_CONTROLLER_OBSTRUCTION.md then queries x after all data. The actual final bank becomes 2e, while a fully feasible moment-and-empty-matching competitor proves A>(n^2/2-n-2)e>=110e for every n>=16. Thus the separated-liability rule fails even with no old debit. The x influence is exactly 1/2. This is a scoped payment-rule counterexample, not a FEI counterexample; the actual root satisfies H0<4I0.

SIGNED_REPAIR.md prevents overclaiming that failure. If the original 4R allowance is still unused, N=[A+omega+D-4R]_+ satisfies S-N=min(S,4I0-H(M)-omega). The same rare root has headroom>3/16 after omega<=7/16. Thus the signed rule pays any history with a supplied actual S>=0, including the mixed-x frontier. A spent allowance cannot be used again. First unsupported universal line: obtain this source headroom for an arbitrary Boolean core and pay a prescribed NEW descendant reference transfer from the same remaining original allowance, retaining full terminal laws.

# executed validation with domain, arithmetic, commands and outputs

Frozen mathematical helper/domain/resource spec is FROZEN_SPEC.json. Commands from A039:

    python -X utf8 -B runs/{runid}/code/check.py --pilot
    python -X utf8 -B runs/{runid}/code/check.py

Revised pilot PASS: {ps['checks']} exact assertions, {ps['runtime_seconds']:.6f}s, below 60s. Main PASS: {s['checks']} exact assertions, {s['runtime_seconds']:.6f}s, below 55s. Main covers all 126 depth pairs for n=3,4,5,6 and 13 diagnostic boundary pairs for n=1,2; the latter do not extend the stated analytic theorem. Actual truth-table restrictions independently match entropy formulas as exact prime-log identities and influence formulas by both spectra and physical edges. All admitted pairs pay the conservative source plus old 7/16 booking. Mixed-x negative margins are certified at n=3..6 with every physical terminal retained. Five fixed scalar competitor fixtures n=16,17,24,32,64 and exact monotonicity anchors check the all-n inequalities; the proof, not those fixtures, establishes the infinite quantifier.

Original-reference propagation was separately executed through full a/data histories at n=3,4, retaining {rows.get(3)} and {rows.get(4)} source-zero rows. KL equality is proved by chain rules; interval overlaps in this check are consistency tests, not equality proofs. out/CHECK.json preserves full rational endpoints. out/SIGNED_READBACK.json adds 16 rational predicates through a separate validator without importing the generator, proving the signed bill zero at the stored mixed frontiers even with omega=7/16. Pilot counts and readback counts are not added to the main count.

Arithmetic: integer Walsh/Fraction probabilities, exact prime-log cancellation, 50 rational canonical-root bisections, 24-term positive atanh logarithms with a proved tail, outward interval rounding at 2^-140 and final log rounding at 2^-110. The first unrounded pilot failed its runtime guard; no PASS was claimed. The denominator-growth repair and the corrected x-influence prose are preserved in out/VALIDATION_REPAIRS.json. The scalar domain list omitted from the first prose spec was explicitly added before the main job; the revised pilot had already executed that fixed domain from code. There is no floating sign decision.

Estimated memory<=100MB, no heavy search, automatic n escalation, GPU, detached worker, git, mail, deletion, trading access or other-agent writes. Fresh memok returned WAIT: physical free 3.9GB below required 4.0GB (commit gate passed). Therefore Lean was not launched. code/payment.lean is UNCHECKED; result rung is analytic proof with exact certificates, not Lean-checked.

# proof dependencies and changed downstream conclusions

The earlier coherent source telescope and A038's scalar min identity are reconstructed with unchanged definitions; only their exact source files/sections are used. Two scoped claim versions are PROVED_UNREVIEWED. No independent acceptance of the new A038 package or new universal theorem is asserted. For A038/A047/A050, biased rare cores now admit arbitrary data-only histories with quantified old-debit capacity; mixed-controller failure must be attributed to the separated positive-part convention, and any signed repair must identify genuinely unspent query allowance. A088/A094 should reconstruct the feasible competitor and source-zero continuation independently.

# one next mathematical action and independent reviewer

Pay one prescribed descendant fresh-reference reset from the signed source-inclusive account, with old omega and every previously consumed part of 4R explicitly subtracted. Keep the original M and both complete terminal references. A088/A094 independently review the variational lower bound and adaptive reduction; A038/A047/A050 consume the corrected liability ordering. No messages were sent; this is a source-bound local handoff.

# actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, identical PACKET_DELTA.json, proofs, frozen spec, code and exact outputs are saved within this assigned A039 run. out/PERSISTENCE_RECEIPTS.json records post-write readback SHA256/bytes, exact protocol field sets, statement hashes and the per-file size cap. Rolling STATUS.md is two lines; WORKLOG.md/LEARNED.md contain dated append-only stage entries. Only A039 files were authored. External adoption, Brain ingestion, supervisor GitHub copy, mirror verification and independent review remain unverified.

Universal bridge: This moves C024 history transfer and C019 stopping-tree payment by proving a SAME-source all-adaptive-data history interface with >7/16-bit margin, isolating an all-n next-controller failure of the separated liability, and supplying the exact signed repair when ORIGINAL query allowance is unused. The universal FEI constant improves by zero: arbitrary-core source headroom and fresh-reference transfer remain unpaid. NEXT tackles one such transfer with the old debit and the unspent original allowance exposed, the shortest route past the actual universal ownership barrier rather than another isolated class entropy bound.
"""
write(R/"REPORT.md",report)
now=datetime.now(timezone.utc).isoformat()
marker=runid
for name,entry in [
 ("WORKLOG.md",f"\n\n### {now} — {marker}\nResumed from last populated stage5; later marker-only runs not treated as results. Read B08/current board and A038 balanced update. Derived biased rare-core all-adaptive-data source payment >7/16; constructed true matched-empty/marginal variational competitor showing next-x separated-liability failure A/e>n^2/2-n-2 for all n>=16. Distinguished signed source-inclusive repair with unused 4R. Unrounded pilot hit runtime guard; outward rounding repair pilot/main PASS ({ps['checks']}/{s['checks']} assertions; {ps['runtime_seconds']:.3f}/{s['runtime_seconds']:.3f}s). 16 separate signed readback predicates PASS. memok WAIT, Lean not run. Full FEI OPEN, review/copy unverified. NEXT: prescribed fresh reset with same unused original allowance, full terminals and old debits.\n"),
 ("LEARNED.md",f"\n\n### {now} — {marker}\nFor rare F_n, original completed occupancy A, and any a-first adaptive data-only history, unique zero-path depths k0,k1 give If=1/2+e(k0+k1+2)/4 and Hf=e[2^k0 J_(k0+2)+2^k1 J_(k1+2)]/2. Hence SAME S-L>7/16 for all n>=3, L=A+[D-4R]_+, and any old omega<=7/16 remains paid. After all data then x, S=2e and L=A>(n^2/2-n-2)e for all n>=16: separated-liability extension fails. A feasible competitor uses independent rare indicators Ber(e/2) and fair correlated (x,a) table (t,1/2-t,1/2-t,t), t=(1-e)^2/[4(1-e/2)^(n+1)], matching the special empty mass exactly. This is NOT a general signed-payment obstruction: N=[A+omega+D-4R]_+ gives S-N=min(S,4I0-H(M)-omega), provided 4R is unspent. Original source headroom after omega<=7/16 exceeds3/16. Never move the positive part without identifying the original allowance owner. Reference interval fractions need outward size control after operations; otherwise a tiny exact pilot can exceed60s from denominator growth. No Lean certification on admission WAIT.\n")]:
 path=OWN/name
 existing=read(path) if path.exists() else ""
 if marker not in existing:write(path,existing+entry)
write(OWN/"STATUS.md","STATE: A039 stage6 saved: all-n rare adaptive-data source payment>7/16; next-x separated bill refuted all n>=16; signed unused-allowance repair; 12194 exact main checks PASS; FEI OPEN, review pending.\nNEXT: Pay one prescribed fresh-reference reset from SAME signed source account and unused original 4R after old bookings, retaining both full terminals; A088/A094 review, A038/A047/A050/A096/A097 consume.\n")
# Protocol/readback checks are deliberately separate from mathematical predicates.
expected=set(proto["required_per_run"]["progress_fields"]);expected.remove("packet_ids (one primary ID, for compatibility)");expected.add("packet_ids")
assert set(progress)==expected
expected_claim=set(proto["required_per_run"]["claim_fields"])
for x in claims:
 assert set(x)==expected_claim
 assert hashlib.sha256(x["exact_statement"].encode("utf-8")).hexdigest()==x["statement_sha256"]
assert (R/"PROGRESS.json").read_bytes()==(R/"PACKET_DELTA.json").read_bytes()
assert len(read(OWN/"STATUS.md").splitlines())==2
for heading in proto["required_per_run"]["report_fields"]:assert "# "+heading in read(R/"REPORT.md")
assert read(R/"REPORT.md").rstrip().split("\n\n")[-1].startswith("Universal bridge:")
receipts=[]
for p in sorted(R.rglob("*")):
 if p.is_file() and p.name!="PERSISTENCE_RECEIPTS.json":
  assert p.stat().st_size<20_000_000
  receipts.append({"path":str(p.relative_to(R)),"sha256":digest(p),"bytes":p.stat().st_size})
dump(R/"out/PERSISTENCE_RECEIPTS.json",{"readback_at":now,"protocol_fields":"PASS","claim_statement_hashes":"PASS","progress_delta_identical":True,"report_fields":"PASS","size_limit_bytes":20_000_000,"own_status_lines":2,"files":receipts,"remote_copy":"UNVERIFIED","independent_review":"PENDING"})
print(json.dumps({"status":"COMPLETE_LOCAL","math_checks":s["checks"],"signed_readback_predicates":16,"source_zero_rows":rows,"files_receipted":len(receipts),"full_FEI":"OPEN","report":str(R/"REPORT.md")}))

