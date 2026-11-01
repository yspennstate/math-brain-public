from pathlib import Path
import hashlib,json,runpy,datetime,re
R=Path(__file__).resolve().parents[1]; O=R/'out'; A=R.parents[1]
OLD=R.parent/'20261023T115918Z-fleet03-A017-recursive-addressing'
ROOT=A.parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_bytes((json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode('utf-8'))
def text(p,s):p.write_bytes(s.encode('utf-8'))
def find(d,key):
    if isinstance(d,dict):
        if key in d:return d[key]
        for v in d.values():
            z=find(v,key)
            if z is not None:return z
    if isinstance(d,list):
        for v in d:
            z=find(v,key)
            if z is not None:return z
    return None
def main():
    cert=read(O/'certificate.json'); assert cert['status']=='PASS' and cert['roots']==2560 and cert['exceeds']==0 and cert['sector_phase_rows']==6144
    assert cert['assertions']==37889 and read(O/'pilot.json')['elapsed_seconds']<60
    spec=read(O/'spec.json');assert spec['helper_sha256']==sha(R/'code/check.py')
    save(O/'witness_spec.json',dict(helper_version='A017-direct-witness-v1',helper_sha256=sha(R/'code/independent.py'),
      family='One retained actual six-bit maximum root plus BOTH full children',domain='One fixed witness from frozen2560-root search',case_count=1,
      symmetry='none',arithmetic='Direct integer characters; Fraction;256-term unreduced atanh intervals with proved geometric error',
      memory_estimate_MB=20,max_runtime_seconds=60))
    runpy.run_path(str(R/'code/independent.py'),run_name='__main__')
    audit=read(O/'witness_certificate.json');assert audit['status']=='PASS' and audit['verdict']=='PAID_SAME_K'
    fullaudit=read(O/'independent_full.json');assert fullaudit['status']=='PASS' and fullaudit['roots']==2560 and fullaudit['checks']==10241
    protocol=read(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
    cf=find(protocol,'claim_fields');pf=[k.split(' (')[0] for k in find(protocol,'progress_fields')];rf=find(protocol,'report_fields')
    source_paths=[Path('BOARD.md'),Path('claude/B04/STREAM_NOTES.md'),OLD/'PROOF.md',OLD/'out/source_b.json',Path('agents/A024/runs/20261023T125238Z-fleet03-A024-biased-child-stability/DERIVATION.md')]
    save(O/'source_receipts.json',[dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size) for p in source_paths])
    (O/'source_b.json').write_bytes((OLD/'out/source_b.json').read_bytes())
    claim=read(OLD/'CLAIMS.json')[0];claim.update(version=5,
      exact_statement='For every real h on original physical coordinates, p=||h||_2^2 and e_j=I_j(h), min_T I(h chi_T)=sum_j min(e_j,p-e_j), with I(h chi_T)=I(h)+|T|p-2sum_(j in T)e_j. For every Boolean f and physical selected i, D=(f0-f1)/2,A=(f0+f1)/2,p=Inf_i(f), its actual entropy debit is at most Gamma=min(3p/ln2+2E_*(D),3(1-p)/ln2+2E_*(A)). Actual influence spent remains p and both full children remain. For the prior shared-gate tensor family G_t=A_(b^tensor(t)), every complete adaptive selected-factor permutation has sum w Gamma>=9t(t-1)/64, hence for fixed kappa sum w positivepart(Gamma-kappa*p)>=9t(t-1)/64-kappa*t/16, although actual queries are paid SAME K=4+2/ln2. For every Boolean c depending on at most three of the five unqueried coordinates of the saved six-bit b, exact enumeration of2560 descriptions proves Delta_i(bc)<=Delta_i(b)<K/8, Inf_i(bc)=1/8. Thus ANY adaptive stopped selected-factor prefix of a product of arbitrary such factors through ONE shared A_h gate is paid at SAME K solely from original queried influence E[N]/16, retaining both full terminals. No full FEI claim.',
      hypotheses=['Uniform original physical cube; Boolean signs; entropy bits; real energies use full Dirichlet form.','Universal character correction uses no disjointness assumption and creates no new payment source.','Tensor obstruction uses the saved six-bit b, disjoint factor blocks, selected original0 once per factor, ONE unqueried shared p0,z.','Bounded-overlap certificate permits arbitrary Boolean c on at most three unqueried physical coordinates of each seed; it does not cover all five-coordinate multipliers.','Full terminal entropy/influence retained; no arbitrary terminal price, universal source or existential policy claimed.'],
      proof_source=['PROOF.md','code/check.py','code/independent.py','code/audit_full.py','out/spec.json','out/certificate.json','out/witness_certificate.json','out/independent_full.json','out/source_b.json'],
      proof_dependencies=[dict(claim_id='A017-FOUR-EDGE-COMPATIBILITY',version=4,status='AUTHOR_CHECKED_PENDING_INDEPENDENT_REVIEW',used_for='Actual six-bit seed, same-gate tensor identities and prior K margin; new universal bound has a self-contained derivation.')],
      review_records=[],status='AUTHOR_CHECKED_PROOF_AND_EXACT_CERTIFICATES_PENDING_REVIEW',supersedes=['A017-FOUR-EDGE-COMPATIBILITY@4'],refutes=[],first_unproved_line=None,
      next_consumers=['A018','A019','A020','A024','A090','A091','B04','C019','C024'])
    claim['statement_sha256']=hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()
    claim['exact_statement']+=' The same prefix payment holds after multiplying the ENTIRE root by any ONE fixed physical character avoiding every prescribed queried coordinate; the character may reuse shared p0,z labels at every level. Thus at-most-three-coordinate nonlinear seed multipliers times arbitrary unqueried characters are covered, with the actual modulated root influence account and both full terminals retained.'
    claim['statement_sha256']=hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()
    assert set(claim)==set(cf);save(R/'CLAIMS.json',[claim])
    nxt='Pay positive ACTUAL coupled entropy correction for an overlapping indecomposable core from SAME diminished original source, after old debits and BOTH full terminals; avoid derivative-energy/character reoptimization, already obstructed quadratically. A024 compare actual half-spectrum credit; A090/A091 independently reconstruct v5.'
    progress=read(OLD/'PROGRESS.json');progress.update(run_id=R.name,attempt_id='A017-stage21-physical-character-correction-and-bounded-overlap',
      method='Exact physical character-energy minimization and two-sector entropy estimate; all-width adaptive tensor proxy lower bound; exhaustive fixed six-bit overlapping multipliers; independent direct-character/rational-log witness audit.',
      mathematical_delta='Valid universal character-overlap correction and stopping estimate; even the strongest character/sector proxy has a quadratic bad-filtered bill. Certified all2560 at-most-three-coordinate overlap seeds and ALL-width adaptive stopped mixed-factor prefixes at SAME K from actual queried influence. General source price remains OPEN.',
      mathematical_status='UNIVERSAL_CORRECTED_BOUND_AND_PROXY_OBSTRUCTION;BOUNDED_OVERLAP_HISTORY_PAYMENT;FULL_FEI_OPEN',
      claim_versions_used=[dict(claim_id='A017-FOUR-EDGE-COMPATIBILITY',version=4)],claims_created_or_changed=[dict(claim_id=claim['claim_id'],version=5)],
      next_consumers=claim['next_consumers'],next_action=nxt,stagnant_substantive_attempts=0,
      blockers=['New and inherited claims await independent review.','Arbitrary positive noncharacter-overlap entropy correction and universal original source remain unpaid.','Supervisor transfer and independent remote receipt pending; full FEI OPEN.'])
    assert set(progress)==set(pf);save(R/'PROGRESS.json',progress);(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
    sections=[
      'For every Boolean f on any uniform physical cube, derive a valid character-invariant selected-query estimate while retaining the actual original influence p. For ALL t, test whether this repaired proxy pays the prescribed shared-gate tensor history. Separately settle exactly the frozen2560 descriptions b*c with c using at most three unqueried seed coordinates, then compose their actual query payments through ONE shared gate. Units: bits. Full FEI remains OPEN.',
      'Current BOARD B04/A024/reviewer rows, own STATUS, B04 STREAM_NOTES v2 (2026-10-11) especially established(4) and open line; stage20 PROOF.md and checker; saved six-bit actual source; current protocol schemas; A024 v6 DERIVATION sections1-2 and report excerpts. The universal estimate is proved self-contained in PROOF section2. Protocol and campaign/paper context were read in earlier stages; no fresh complete reread of all papers is claimed. A math-recall attempt failed argument parsing and supplies no mathematical evidence. Source SHA256 receipts are in out/source_receipts.json.',
      'PROOF.md sections1-2 prove exact character correction, minimum energy, BOTH-sector bound and stopping telescope for arbitrary physical overlap. Section3 proves sum w Gamma>=9t(t-1)/64 for EVERY complete adaptive selected-factor order through the SAME guard, despite actual SAME-K payment. Section4 certifies Delta_i(bc)<=delta for ALL frozen2560 seeds, and proves ALL-width mixed-factor stopped-prefix payment from original queried influence only. The first unsupported universal line is an original-influence payment for positive actual entropy correction at an arbitrary overlapping indecomposable core; no arbitrary terminal FEI estimate or initial bank is assumed.',
      'Frozen out/spec.json precedes all runs. Commands: python -X utf8 code/check.py --freeze; --pilot; --run (from the run directory, with full script paths used in execution). Pilot:32 roots,384 sector-phase rows,1857 assertions,1.395s. Full:2560 roots,6144 sector-phase rows,37889 assertions,20.729s; all2560 paid,zero above delta. Integer Walsh/Fraction edges and48-term rational logarithm enclosures; no symmetry quotient or float sign. Witness frozen independently by out/witness_spec.json and audited by code/independent.py using direct root/BOTH-child character sums and256-term unreduced rational logarithms. Both outputs PASS. This is separate author verification, not external review. Fixed memory70MB/20MB below300MB; no memok admission needed, no GPU or detached job, no dimension escalation.',
      'A017-FOUR-EDGE-COMPATIBILITY@5 supersedes@4 without changing prior scoped conclusions. New universal implication has an elementary entropy/isoperimetry proof. Finite overlap extension depends on the saved actual six-bit seed and exact enumeration; ALL-width statement additionally uses physical product independence and the inherited same-gate identity. No external acceptance is claimed. A024 actual-spectrum algebra-norm bound is compared as a frontier, not assumed influence-priced. No claim that all adaptive policies fail, or that H/I diverges.',
      nxt,
      'All four protocol files plus proof, frozen specifications, scripts and exact outputs are saved in A017. out/PERSISTENCE_RECEIPTS.json records sizes/SHA256 and is reread for verification. Every file is under20MB; PACKET_DELTA equals PROGRESS byte-for-byte with packet_ids=[A017]. STATUS has exactly STATE/NEXT lines; WORKLOG and LEARNED appended. Independent acceptance and supervisor remote transfer remain pending. Brain self-care degraded/unverified: wake owner-model100.6h,state-of-mind85.2h,dream35.9h stale; personalization from these notes is unverified, and they were not used mathematically. No process was stopped; no mathematical job is left running.'
    ]
    assert len(rf)==len(sections)
    sections[3]+=' Additional frozen ALL-root audit: code/audit_full.py --freeze, --pilot, --run;2560 roots and5120 full children reconstructed by direct integer character sums and unreduced256-term log intervals,10241 checks PASS, including a deliberately underpriced positive control. This independently checks the finite overlap enumeration through a different author entropy representation, not an external review.'
    sections[2]+=' The payment also survives ONE fixed global physical character avoiding all queried coordinates, even when it reuses the shared p0,z labels at every level; no character or gate is installed anew.'
    report='# A017 stage21: exact character overlap, bounded reuse, and the surviving proxy obstruction\n\n'
    report+='\n\n'.join('## '+k+'\n\n'+v for k,v in zip(rf,sections))
    report+='\n\n## Universal bridge\n\nThis stage moves C019/C024 by giving a valid universal physical-character correction and paying actual adaptive prefixes with up to three reused seed coordinates per factor at SAME K through ONE shared gate. It also rules out the strengthened derivative proxy on an all-dimensional family: even after choosing the best character and A/D sector its adverse bill is at least9t(t-1)/64-kappa*t/16, versus original influence1+9t/8. What remains is positive actual noncharacter-overlap entropy liability at an arbitrary reached core, paid from the SAME unused original account with old debits and BOTH full terminals. NEXT attacks that liability directly; further character optimization or another tensor census cannot repair the proved quadratic obstruction. Full FEI is OPEN.\n'
    text(R/'REPORT.md',report)
    text(A/'STATUS.md','STATE: A017 stage21 saved: universal exact character correction/two-sector bound; repaired proxy still quadratic;2560 bounded-overlap seeds and ALL-width mixed-factor prefixes SAME-K paid; FEI OPEN/review pending.\nNEXT: '+nxt+'\n')
    marker='2026-10-23 stage21 (20261023T140902Z)'
    for fn,body in [('WORKLOG.md','Derived a valid universal phase/sector query bound and proved its quadratic proxy obstruction. All2560 three-coordinate overlap descriptions paid <=base delta;37889 checks plus direct-root/BOTH-child unreduced-log audit PASS. Extended actual SAME-K prefixes to arbitrary products of these seeds through ONE gate. No general overlapping source price; independent review and supervisor transfer pending.'),('LEARNED.md','For real h, min_T I(h chi_T)=sum_j min(e_j,||h||^2-e_j), an exact overlap correction. For Boolean f, Delta_i<=min(3p/ln2+2E_*(D),3(1-p)/ln2+2E_*(A)); physical payer stays p. This repaired proxy STILL has sum>=9t(t-1)/64 on G_t selected adaptive orders. All fixed seed multipliers c on <=3 of five unqueried coordinates satisfy Delta_i(bc)<=delta; a2560-case exact certificate plus product/gate identities pays arbitrary mixed-factor stopped prefixes at SAME K. Arbitrary overlapping entropy correction, not phase correction, is the unpaid universal step.')]:
        p=A/fn; old=p.read_text(encoding='utf-8') if p.exists() else ''
        if marker not in old:text(p,old+'\n\n## '+marker+'\n\n'+body+'\n')
    assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
    extra='2026-10-23 stage21 full direct audit and shared-character corollary'
    for fn in ['WORKLOG.md','LEARNED.md']:
        p=A/fn; old=p.read_text(encoding='utf-8')
        if extra not in old:text(p,old+'\n\n## '+extra+'\n\nAll2560 roots and5120 BOTH-child tables independently reconstructed by author direct-character entropy,10241 exact checks PASS (2400 noncharacter descriptions). ONE fixed global character avoiding prescribed queried coordinates can reuse shared p0,z at every level: entropy debits and physical queried influence stay unchanged. Original modulated-root account and full terminals remain; arbitrary nonlinear overlap and full FEI OPEN.\n')
    for p in R.rglob('*'):
        if p.is_file():
            assert p.stat().st_size<20*1024*1024
            if p.suffix=='.json':read(p)
    assert (R/'PACKET_DELTA.json').read_bytes()==(R/'PROGRESS.json').read_bytes()
    receipt=dict(status='LOCAL_HASH_VALIDATED',timestamp_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
      files=[dict(path=str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(R.rglob('*')) if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json'],
      rolling=[dict(path=str(A/fn),sha256=sha(A/fn)) for fn in ['STATUS.md','WORKLOG.md','LEARNED.md']],remote='SUPERVISOR_PENDING',independent_review='PENDING')
    save(O/'PERSISTENCE_RECEIPTS.json',receipt)
    for row in read(O/'PERSISTENCE_RECEIPTS.json')['files']:assert sha(R/row['path'])==row['sha256']
    print(json.dumps(dict(status='LOCAL_FILES_VALIDATED',files=len(receipt['files']),claim_version=5,full_fei='OPEN',review='PENDING')))
if __name__=='__main__':main()
