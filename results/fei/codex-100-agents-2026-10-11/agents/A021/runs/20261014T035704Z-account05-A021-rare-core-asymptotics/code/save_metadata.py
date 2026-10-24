from pathlib import Path
import json, hashlib, datetime
RUN=Path(__file__).resolve().parents[1]
HOME=RUN.parents[1]
ROOT=HOME.parents[1]
def dump(path,obj): path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
sources=[ROOT/'BOARD.md',ROOT/'claude/B05/STREAM_NOTES.md',
 ROOT/'agents/A023/runs/20261014T022245Z-account05-A023-amortized-rarity-budget/REPORT.md',
 ROOT/'agents/A023/runs/20261014T022245Z-account05-A023-amortized-rarity-budget/PROOF.md',
 ROOT/'agents/A023/runs/20261014T022245Z-account05-A023-amortized-rarity-budget/REVIEW_A021.md',
 ROOT/'agents/A025/runs/20261014T032227Z-account05-A025-rare-event-counterfamily/REPORT.md',
 ROOT/'agents/A025/runs/20261014T032227Z-account05-A025-rare-event-counterfamily/PROOF.md',
 ROOT/'agents/A029/runs/20261014T025327Z-account05-A029-child-deficit-transport/REPORT.md',
 ROOT/'agents/A029/runs/20261014T025327Z-account05-A029-child-deficit-transport/DERIVATION.md',
 ROOT/'agents/A029/runs/20261014T025327Z-account05-A029-child-deficit-transport/CLAIMS.json',
 ROOT/'agents/A022/runs/20261014T014918Z-account05-A022-one-point-surgery/REPORT.md',
 HOME/'runs/20261014T011316Z-account05-A021-rare-core-asymptotics/DERIVATION.md',
 Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')]
dump(RUN/'out/source_inventory.json',[dict(path=str(p),sha256=sha(p)) for p in sources])
statement=('For every even m>=4, every bent Boolean b on m uniform bits, distinct point edits b_u,b_v, and independent positive-width point blocks A,B of widths r,s, set g0=z*b,g1=z*b_u,g2=z*b_v and f=g0+A(g1+B(g2-g1)-g0). With alpha=2^-r,beta=2^-s,delta=2^-m,pi=(1-alpha,alpha(1-beta),alpha*beta), IC=2*r*alpha*delta+4*s*alpha*beta*delta, D=H(f)-sum pi_j H(gj), Rstar=2 sum_{i<j}pi_i*pi_j I(gi*gj), VA=2*alpha*(1-alpha)*delta*(1+(1-2*beta)^2), VB=8*alpha*beta*(1-beta)*delta,V=VA+VB, and L=VA*(2*r-2)+VB*(2*r+2*s-4)+2*alpha*(1-alpha)*delta*(1-2*beta)^2*log2(1/(1-2*beta)^2), one has |D-m*V-L-3*V/ln(2)|<=8*sqrt(delta)*V/ln(2) and Rstar<=D<=Rstar+18*IC. The coefficient of Rstar in any uniform bound D<=lambda*Rstar+K*IC with fixed finite K is necessarily lambda>=1. The nested sufficient reserve excess is exactly 2*alpha*(1-alpha)*beta*(1-beta)*I(g1*g2), equal to IC*(m-e_adj)/4 when r=s=1.')
hyp=['Uniform cubes; Shannon Fourier entropy in bits; ordinary total influence.', 'The balancing sign z, data, A and B use mutually disjoint coordinates.', 'u!=v, m even and >=4, r,s positive integers; 0 log(1/0)=0.', 'No claim for arbitrary non-flat cores, arbitrary depth, or source rate 11/2.']
digest=hashlib.sha256(json.dumps(dict(statement=statement,hypotheses=hyp),sort_keys=True,separators=(',',':')).encode()).hexdigest()
claim=dict(claim_id='A021-COHERENT-THREE-CORE-RESERVE',version=1,exact_statement=statement,hypotheses=hyp,statement_sha256=digest,contributors=['A021'],proof_source=['DERIVATION.md','code/check.py','out/validation.json'],proof_dependencies=[],review_records=[],status='PROVED_LOCALLY_REVIEW_PENDING',supersedes=[],refutes=[],first_unproved_line=None,next_consumers=['A023','A025','A029','B05','B20'])
dump(RUN/'CLAIMS.json',[claim])
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=RUN.name,stream='B05',packet_id='A021',gap_id='G-R-SELECT',attempt_id='A021-stage5-first-nonconstant-coherent-refund',method='Consume A023 whole-block payment and A025/A029 repeated ownership obstruction; independently reconstruct A029 edgewise reserve identity; compute coherent Fourier sectors and uniform signed Taylor refund; exact rational log and Walsh validation',mathematical_delta='Coefficient-one symmetric data reserve pays actual entropy decrement on the first three-distinct-core common-bent-reference hierarchy with an absolute control rate18, uniformly in both selector widths and core dimension. Divergent hierarchical surcharge is not an actual leading entropy obligation. All complete terminal laws retained.',deliverable_status='COMPLETE_LOCAL_ARTIFACT',mathematical_status='SCOPED_COHERENT_REFUND_PROVED_LOCALLY; A029_RESERVE_IDENTITY_INDEPENDENTLY_REVIEWED; NEW_REVIEW_PENDING; FULL_FEI_OPEN',claim_versions_used=[dict(claim_id='A023-OVERLAP-EXPOSURE-GOOD-CONTROL-LEDGER',version=3,statement_sha256='32444a38f9d32b7d226f04c6322d4a7ea0a271e808d5a3e5da35cdef76e5605c',role='Reviewed whole-block clause consumed as target; new theorem reconstructed from Fourier definitions, not dependent on bundled claim'),dict(source='A029 run20261014T025327Z DERIVATION.md',role='Independently accepted exact surcharge and capacity identities only')],claims_created_or_changed=[dict(claim_id=claim['claim_id'],version=1)],source_artifacts=['REPORT.md','DERIVATION.md','REVIEW_A029.md','SEARCH_SPEC.json','code/check.py','out/validation.json','out/interval_cases.jsonl','out/direct_fixtures.json','out/source_inventory.json'],next_consumers=['A023','A025','A029','B05','B20'],next_action='A029 independently review the coherent-sector refund; generalize the signed rowwise curvature refund to non-flat references with one terminal-pair reserve before extending hierarchy depth.',stagnant_substantive_attempts=0,blockers=['No general non-flat-reference coherent refund or arbitrary-depth reserve ownership.','Source control rate11/2 replacement not proved; scoped constant18 only.','Independent review, shared adoption and mirror verification pending.'],packet_ids=['A021'])
dump(RUN/'PROGRESS.json',progress); dump(RUN/'PACKET_DELTA.json',progress)
report='''# exact target, quantifiers, hypotheses and units

Pay the actual Fourier entropy decrement of the first nested hierarchy with three distinct nonconstant balanced cores by its symmetric terminal-pair data reserve, with a control rate independent of both selector widths and data dimension. The family, all quantifiers and accounts are in DERIVATION.md: z times a bent seed and its two distinct point flips, even m>=4, positive widths r,s. Entropy is in bits; influence is ordinary uniform-cube influence. This is a narrow repair to the existing reserve mechanism, not a new broad FEI candidate.

# sources actually read, revisions and theorem locators

BOARD.md snapshot 03:56 UTC; B05 STREAM_NOTES.md v2; own stage4 STATUS/derivation; full execution protocol v2. Consumed A023 run022245 whole-point-block payment in PROOF.md (bundled claim v3), A025 run032227 repeated reserve counterfamily, and A029 run025327 DERIVATION.md sections on two physical children and the first surcharge. Read A022 run014918 REPORT.md to avoid presenting its already-paid two-edit class as novel. A023 REVIEW_A021.md accepts the earlier upper price/K6/K7 subclaims, not the complete older bundle. Exact source paths and SHA256 values are in out/source_inventory.json. No fresh external literature claims are used.

# complete derivation or exact first unsupported line

DERIVATION.md gives the full Fourier-sector reconstruction and signed Taylor proof. With delta=2^-m and the explicitly defined masses V and L,

    D=mV+L+3V/ln(2)+E, |E|<=8 sqrt(delta)V/ln(2).
    Rstar<=D<=Rstar+18 IC.

The error constant is uniform in BOTH selector widths and m. Adjacent edits retain the destroyed internal edge correction. For fixed widths D/Rstar tends to one and Rstar/IC diverges, so coefficient one on this reserve is necessary as well as sufficient. The independently verified sufficient-ledger surcharge divided by IC is (m-e_adj)/4 for two fair selectors. Its divergence is canceled in actual entropy by a coherent signed refund. REVIEW_A029.md independently accepts the exact general edgewise identities only.

First unsupported universal line: applying this refund to arbitrary non-flat or zero reference rows and arbitrary hierarchy depth while charging one terminal capacity. Even the existing source control rate11/2 is not established by this scoped proof. All actual terminal entropy and influence are retained. This does not disprove FEI or refute A023's sufficient bound.

# executed validation with domain, arithmetic, commands and outputs

Frozen SEARCH_SPEC.json precedes execution. Command: python -X utf8 runs/20261014T035704Z-account05-A021-rare-core-asymptotics/code/check.py. PASS: 144 entropy instances, 288 adjacency/reserve cases (even m=4..20, r,s=1..4) and16 direct Walsh fixtures (m=4,6; r,s=1,2; two edit distances). Actual helper runtime0.800357 seconds. All logs have rational atanh-series enclosures with28 terms, a proved geometric tail and192-bit outward rounding. Full-cube Walsh, edge-product influence and queried influence identities are exact rational arithmetic, max truth table2048 entries. Interval records and fixtures are saved under out/. No high-memory job, dimension escalation or external writes. Finite certificates supplement the all-parameter analytic proof; they do not replace it.

# proof dependencies and changed downstream conclusions

The new scoped theorem follows from the Boolean Fourier definitions, without relying on the complete bundled A023 claim. A029's algebra was separately reconstructed edgewise. The new result resolves its first unpaid surcharge only on a common-flat-reference family and at rate18. It shows that repeated positive reserve bills can materially overestimate actual entropy even with three distinct terminals; constant-failure folding is not needed for this refund. This supplies a required test for any global potential: coefficient less than one on the symmetric data reserve cannot work at any fixed control price. A022's existing class FEI result is not claimed as new. Independent review of the new theorem is pending.

# one next mathematical action and independent reviewer

Next prove or refute a rowwise signed curvature refund for non-flat references that closes the same two-block terminal-pair bill, before increasing depth or enumerating another class. A029 should independently reconstruct the critical coherent-sector and curvature steps; A023 is the downstream stopping-ledger consumer. This is a handoff written to local artifacts, not a sent message.

# actual persistence receipts or precise save blocker

All four required protocol files, proof, scoped review, frozen specification, code and exact outputs are saved in this run. out/ARTIFACTS.json records local SHA256 receipts (excluding itself). Rolling STATUS.md, WORKLOG.md and LEARNED.md are updated. No shared registry, mirror, GitHub adoption, independent acceptance or public release is asserted.

## Universal bridge

This moves C024 history transfer toward C019 stopping-tree payment by removing the entire dimension-growing first three-core hierarchy surcharge from actual entropy on the common-flat-reference test family: a single coefficient-one symmetric reserve plus18 IC suffices, and coefficient one is optimal. What remains is a non-flat and arbitrary-depth signed refund with the same physical terminal owners; rate11/2 also remains unproved. NEXT targets that missing signed history inequality directly, rather than another isolated FEI class that A022 already covers.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
(HOME/'STATUS.md').write_text('STATE: A021 stage5 saved: coherent three-distinct-core refund D=Rstar+O(IC), coefficient1 optimal, uniform two-width error; 288 interval cases+16 Walsh checks PASS; full FEI OPEN.\nNEXT: A029 review; extend signed rowwise curvature refund to non-flat references while retaining one terminal-pair reserve before increasing hierarchy depth.\n',encoding='utf-8')
with (HOME/'WORKLOG.md').open('a',encoding='utf-8') as out: out.write('\n'+now+' | Stage5 '+RUN.name+': consumed A023 whole-block theorem and A025/A029 repetition obstruction; independently reconstructed A029 XOR-edge surcharge. Proved actual three-distinct-core common-bent-reference entropy decrement Rstar<=D<=Rstar+18IC and uniform expansion with error8 sqrt(delta)V/ln2, optimal coefficient1. Sufficient surcharge/IC=(m-adj)/4 diverges but coherent entropy refunds it. Exact pilot288 reserve cases and16 Walsh fixtures PASS in0.800357s, max2048 table, no heavy compute. Saved proof and source-bound review; general non-flat/depth bridge remains open.\n')
with (HOME/'LEARNED.md').open('a',encoding='utf-8') as out: out.write('\nStage5: For nested point selectors of widths r,s and three balanced cores z*b,z*b_u,z*b_v from any even-m bent seed (m>=4), actual terminal decrement D=mV+L+3cV+E, |E|<=8c sqrt(delta)V uniformly in widths; V=4delta[alpha(1-alpha)+2alpha^2 beta(1-beta)]. With Rstar=2sum pi_i*pi_j I(gi*gj), Rstar=mV-8 adjacency*delta*pi1*pi2 and Rstar<=D<=Rstar+18IC, IC=2r alpha delta+4s alpha beta delta. Coefficient1 is necessary in any D<=lambda Rstar+KIC. The hierarchical surplus2alpha(1-alpha)beta(1-beta)I12 is real as sufficient ledger but not leading actual entropy; fair widths give surplus/IC=(m-adjacency)/4. Coherent constant-selector Fourier rows refund it through weighted Taylor curvature. Common flat reference and no zero rows are essential proved hypotheses; rate11/2, arbitrary non-flat cores and depth unproved. A029 surcharge/capacity identities independently accepted at exact edgewise scope only.\n')
dump(RUN/'out/ARTIFACTS.json',[dict(path=str(p.relative_to(RUN)),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(RUN.rglob('*')) if p.is_file() and p.name!='ARTIFACTS.json'])
print(json.dumps(dict(run=RUN.name,claim_sha256=digest,files=len(list(RUN.rglob('*'))),saved=True)))
