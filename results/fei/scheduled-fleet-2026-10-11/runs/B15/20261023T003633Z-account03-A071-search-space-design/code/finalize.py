"""Scalar adversarial boundaries, all-history ledger verification and protocol save."""
from subsidy import *
import hashlib,datetime

def scalar_checks():
    values=list(map(F,[-2,-1,0,1,2]))+[F(-1,2),F(1,2)]
    As=[F(0),F(1,4),F(1,2),F(1),F(2),F(4)];cases=checks=0;branches={}
    def test(x):
        nonlocal checks
        assert x;checks+=1
    for s0,s1,A in itertools.product(values,values,As):
        ss=[s0,s1];ns=[max(F(0),-s) for s in ss];ps=[max(F(0),s) for s in ss]
        N=sum(ns,F(0))/2;P=sum(ps,F(0))/2;aggregate=P-N+A
        if aggregate<0:continue
        for T in sorted({F(0),aggregate/2,aggregate}):
            cases+=1;gap=max(F(0),N-A)
            if A>=N:
                if P>0:k=[p/P for p in ps];branch='A>=N,P>0'
                elif N>0:k=[n/N for n in ns];branch='P=0,N>0'
                else:k=[F(1),F(1)];branch='P=N=0'
                credits=[n+(A-N)*v for n,v in zip(ns,k)];flow=[F(0),F(0)]
            else:
                test(N>0 and P>0);branch='N>A'
                k=[p/P for p in ps];credits=[A*n/N for n in ns]
                flow=[gap*n/N-gap*v for n,v in zip(ns,k)]
            debits=[T*v for v in k]
            test(sum(k)/2==1);test(sum(credits)/2==A);test(sum(flow)==0);test(sum(debits)/2==T)
            test(all(c>=0 for c in credits));test(all(d>=0 for d in debits))
            test(all(s+a+f-d>=0 for s,a,f,d in zip(ss,credits,flow,debits)))
            test(sum(max(0,f) for f in flow)/2==gap)
            # Independent necessary lower bound: a recipient with negative s needs n-a.
            test(sum(max(0,f) for f in flow)/2>=max(F(0),N-sum(credits)/2))
            for L in [F(-2),F(0),F(3)]:test(sum(L*v for v in k)/2==L)
            branches[branch]=branches.get(branch,0)+1
    return dict(cases=cases,exact_checks=checks,branches=branches)

def main():
    begin=time.perf_counter();root=ROOT;home=root.parents[1]
    rows=json.loads((root/'out/SUBSIDY_CASES.json').read_text(encoding='utf-8'))
    ad=json.loads((root/'out/ADAPTIVE.json').read_text(encoding='utf-8'))
    result=json.loads((root/'out/RESULTS.json').read_text(encoding='utf-8'))
    source=json.loads((root/'out/SOURCE_REVIEW.json').read_text(encoding='utf-8'))
    ck(len(rows)==10 and len(source['states'])==18 and len(source['policies'])==4)
    ck({(r['b'],r['original_coordinate']) for r in rows}=={(b,i) for b in (0,1) for i in range(1,6)})
    allocation=[];flatfail=0
    for r in rows:
        A=r['incoming_A'];ss=[c['S'] for c in r['full_children']]
        lowA=55 if r['b']==0 else 45
        ck(A[0]*1000>lowA*Q and A[1]*1000<(lowA+1)*Q)
        ck(all(s[1]<0 for s in ss));N=r['N'];ck(N[0]>0)
        if F(r['physical_influence'])==0:
            e=(0,0);k=[const(1),const(1)]
        else:
            e=r['new_query_e'];ck(e[0]>0);ck(r['negative_part_gap'][1]<0)
            k=[div(neg(s),N) for s in ss]
            ck(all(x[0]*5>3*Q and x[1]*5<7*Q for x in k))
            ck(r['flat_A_new_gross'][0]>0);flatfail+=1
        credit=[mul(A,v) for v in k];booked=[mul(e,v) for v in k]
        equalcheck(avg(credit),A);equalcheck(avg(booked),e)
        for s,a,d in zip(ss,credit,booked):equalcheck(sub(plus(s,a),d),(0,0))
        allocation.append(dict(b=r['b'],i=r['original_coordinate'],kernel=k,credit=credit,booked=booked,new_flow=[[0,0],[0,0]]))
    ck(flatfail==9)
    active=[r for r in rows if F(r['physical_influence'])>0]
    for r in active:
        lo,hi=r['new_query_e'];den=10000
        low=96 if r['b']==0 else 32;high=97 if r['b']==0 else 33
        ck(lo*den>low*Q and hi*den<high*Q)
    # Complete full-reveal leaves: each row's bit1 child stops; bit0 continues.
    terminal_receipts=[]
    for chain in ad['chains']:
        ck(chain['complete']);m0=chain['initial'];leaves=[]
        for n,r in enumerate(chain['rows']):
            ck(r['newgross']==[0,0]);ck(r['T'][0]>0)
            ck(all(c[0]>=0 for c in r['credits']));ck(all(d[0]>=0 for d in r['booked']))
            leaves.append(dict(weight=F(1,1<<(n+1)),credit=r['credits'][1],booked=r['booked'][1],S=r['children_S'][1]))
        final=chain['rows'][-1]
        leaves.append(dict(weight=F(1,1<<m0),credit=final['credits'][0],booked=final['booked'][0],S=final['children_S'][0]))
        ck(sum(l['weight'] for l in leaves)==1)
        total_credit=(0,0);total_book=(0,0);mean_s=(0,0)
        for leaf in leaves:
            total_credit=plus(total_credit,scale(leaf['credit'],leaf['weight']))
            total_book=plus(total_book,scale(leaf['booked'],leaf['weight']))
            mean_s=plus(mean_s,scale(leaf['S'],leaf['weight']))
            equalcheck(sub(plus(leaf['S'],leaf['credit']),leaf['booked']),(0,0))
        initial_A=chain['rows'][0]['A'];equalcheck(total_credit,initial_A)
        equalcheck(total_book,plus(mean_s,initial_A))
        terminal_receipts.append(dict(initial=m0,conditional_credit_mean=total_credit,original_A=initial_A,
            root_credit_weight='1/64',root_donor_outgoing_weight='1/64',root_recipient_final_weights=[str(l['weight']/64) for l in leaves],
            leaves=[dict(l,weight=str(l['weight'])) for l in leaves]))
    scalars=scalar_checks()
    verification=dict(flat_subsidy_failure_cases=flatfail,no_new_flow_cases=10,
      adaptive_full_chains=2,active_recursive_rows=9,source_states_reviewed=18,source_policies_reviewed=4,
      scalar=scalars,financial_leaf_receipts=terminal_receipts,first_query_allocations=allocation,
      exact_ledger_checks=engine.tests,runtime_seconds=time.perf_counter()-begin)
    ck(verification['runtime_seconds']<55)
    (root/'out/VERIFICATION.json').write_text(json.dumps(verification,indent=2)+'\n',encoding='utf-8')
    run=root.name
    next_action=('A072/A089 carry the same incoming credit and every booked query label into an OTHER-core query '
      'at a stopped negative F_plus=J(-1,+1,g^4) leaf; keep the original stopped donor already spent, '
      'the opposite complete terminal and parked2tau unchanged. A074/A092 independently review the '
      'inherited-credit optimizer, seven profiles and all-adaptive financial conservation. Then replace '
      'the explicit AND profile by a sufficient signed component condition for N<=A and T>=0.')
    theorem=('For finite positive-weight support w summing to1, real signed capacities s, inherited nonnegative '
      'credit A and nonnegative total debit T, conserving mean credit A and requiring nonnegative credit '
      'a and booked debit d, payment with zero-mean signed new flow f and s+a+f-d>=0 exists iff '
      'T<=E(s)+A. With N=E(-s)_+ the minimum additional gross flow E(f)_+ is max(0,N-A). '
      'On the declared A089 negative J(g^6) terminals, all ten next core1 queries and every adaptive '
      'partial or complete reveal within that AND4-plus-dummy/AND5 core have a conserving allocation '
      'with zero new flow, original donor expenditure fixed and rate4 unchanged. Nine active queries '
      'refute constant-in-outcome subsidy allocation without new flow. No arbitrary-core eligibility or FEI theorem.')
    digest=hashlib.sha256(theorem.encode()).hexdigest()
    source_path=Path(r'~\brain_workers\FEI100_20261011\agents\A089\runs\20261022T225420Z-account03-A089-repair-specialist')
    old=json.loads((source_path/'CLAIMS.json').read_text(encoding='utf-8'))[0]
    # Acceptance is exact-version and full stated scope, with the independent reconstruction recorded.
    reviewed=dict(old);reviewed['review_records']=list(old.get('review_records',[]))+[dict(reviewer='A071',decision='ACCEPT_UNCHANGED',statement_sha256=old['statement_sha256'],artifact=str(root/'REPORT.md'),scope='Written reconstruction of sharp signed theorem; independent18 states,4 full physical policies and old donor label conservation.')]
    reviewed['status']='INDEPENDENTLY_ACCEPTED_BY_A071_UNCHANGED'
    claim=dict(claim_id='A071-INHERITED-SUBSIDY-NO-RENEWAL',version=1,exact_statement=theorem,
      hypotheses=['uniform physical cubes for application','finite capacities and real weights','A>=0,T>=0; all supports positive-weight','specified original Boolean family and prior subsidy','nonnegative booked total; signed individual labels allowed','all quantities bits; rate4'],
      statement_sha256=digest,contributors=['A071'],proof_source=['REPORT.md','code/subsidy.py','code/adaptive.py','out/VERIFICATION.json'],
      proof_dependencies=[old['claim_id']+'@1 '+old['statement_sha256']+' independently accepted unchanged','finite character orthogonality and occupied-mask entropy chain rule'],
      review_records=[dict(reviewer='A071 second spectrum construction',status='INTERNAL_REPRODUCTION_NOT_EXTERNAL_ACCEPTANCE',artifact='out/SOURCE_REVIEW.json and out/SEVEN_PROFILES.json')],
      status='AUTHOR_PROOF_AND_EXACT_FINITE_CERTIFICATES_PENDING_REVIEW',supersedes=[],
      refutes=['Constant-in-outcome reuse of inherited subsidy without new sibling flow, on9 actual active queries'],
      first_unproved_line='For arbitrary retained Boolean components, inherited unused credit implies N<=A and T>=0, or additional flow is paid from a genuinely unused ancestor bank.',
      next_consumers=['A072','A074','A075','A089','A092','B15','B20'])
    claims=[reviewed,claim]
    (root/'CLAIMS.json').write_text(json.dumps(claims,indent=2)+'\n',encoding='utf-8')
    progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=run,stream='B15',packet_id='A071',
      gap_id='B15-ARBITRARY-CORE-BIASED-ADMISSION',attempt_id='A071-stage18-inherited-subsidy-all-core1-trees',
      method='Consume negative full-terminal obstruction; sharp inherited-credit optimizer;10 physical queries,7 profile reduction of all adaptive core1 trees, two independent spectrum constructions.',
      mathematical_delta='Nine active rows require nonflat credit but no new transfer; full AND4/AND5 reveal paid from SAME original subsidy with stopped donor unchanged; minimum extra gross flow max(0,N-A).',
      deliverable_status='COMPLETE_LOCAL; independent review and remote adoption pending',
      mathematical_status='SOURCE_ACCEPTED_UNCHANGED; CONDITIONAL_OPTIMIZER_AUTHOR_PROOF; FINITE_ALL_CORE1_HISTORIES_CERTIFIED; FULL_FEI_OPEN',
      claim_versions_used=[old['claim_id']+'@1 '+old['statement_sha256']],claims_created_or_changed=[old['claim_id']+'@1 independent review','A071-INHERITED-SUBSIDY-NO-RENEWAL@1'],
      source_artifacts=['out/SOURCE_PINS.json','FROZEN_SPEC.json','ADAPTIVE_SPEC.json','SCALAR_SPEC.json','out/SOURCE_REVIEW.json','out/SUBSIDY_CASES.json','out/ADAPTIVE.json','out/VERIFICATION.json'],
      next_consumers=claim['next_consumers'],next_action=next_action,stagnant_substantive_attempts=0,
      blockers=['Universal signed-component eligibility remains open.','New theorem independent review, supervisor adoption and remote persistence unverified.'],packet_ids=['A071'])
    for n in ['PROGRESS.json','PACKET_DELTA.json']:(root/n).write_text(json.dumps(progress,indent=2)+'\n',encoding='utf-8')
    report=f'''# exact target, quantifiers, hypotheses and units

The original subsidy pays every adaptive core1 reveal without a new donor draw. The new conditional allocation theorem prices an inherited subsidy by max(0,N-A), rather than charging the full negative-part need N again. This is an author proof plus exact finite certificates, pending independent review; full FEI remains OPEN.

All physical inputs are uniform and Boolean signs; entropy and accounts are bits. Retain g negative on{{0,1,2}} in six bits, h negative on{{0,1,2,4,8,16,32,6,17,40}}, J(x)=-h(x xor1), and F=J(g^6). The A089 prefix fixes core0 original bits2=0,0=0,3=0, then core1 bit0=b, then core0 bits4=5=0, leaving two30-bit negative full terminals. Each carries incoming subsidy A=-S4, booked debit0, residual0; its positive stopped sibling has already paid A, booked B-A and has residual0. Both have original reach1/64. That stopped donor and the separate parked2tau account remain fixed. This stage queries every core1 original coordinate1..5 for both b values (10 labelled alternatives), then closes every adaptive partial/full reveal within that same core.

# sources actually read, revisions and theorem locators

Read current BOARD2026-10-23 00:31 UTC, B15 STREAM_NOTES v2 unchanged2026-10-11, own STATUS/previous run and the execution protocol schema. The lead's old n5 census assignment is closed in prior A071 work; current dispatch consumes the newly supplied negative-terminal dependency. Read A08920261022T225420Z REPORT in full, exact CLAIMS and source locators; A07220261021T225156Z and A07520261022T234728Z REPORTs supply coordination context. Source-byte pins are in out/SOURCE_PINS.json. All executable helpers are copies of A071's own preceding run, executed locally with bytecode disabled; no other agent executable is run or edited.

The A089 claim {old['claim_id']}@1, SHA256 {old['statement_sha256']}, is independently accepted unchanged: its general signed-capacity proof is reconstructed below, all18 physical signs and both final-bit orders for each b are checked, and the original old debit/transfer kernel is reconstructed. This does not accept unrelated statements in other source reports. Earlier protocol/campaign/paper intake stays background; no fresh literature theorem or brain card is a premise. One read-only math recall returns no inherited-subsidy theorem used here. Wake self-care reports personal-model/state-of-mind notes87.1/71.6 hours stale; this is disclosed and those notes are not mathematical evidence. Current telemetry reports status ok, low available RAM (about2.8GB) and disk contention; bounded jobs estimate120MB and no running work is stopped. User's current campaign deadline governs over older protocol dates.

# complete derivation or exact first unsupported line

Write S=4I-H. The occupied-block chain rule gives H(F)=sum q_j H(g_j)+C and I(F)=sum q_j I(g_j). Query excess e=H_parent-mean H_child-4Inf_query therefore satisfies e=mean S_child-S_parent. Independent direct core character sums and product-law centered moments check the composition representation, Parseval and physical influences, including constant cores. No child is dropped when its core is constant: the remaining full function stays nonconstant.

First independently recover A089's source: on the18 restrictions of core0 bits4,5, exactly two full S values are negative; they require subsidies A0 in(55/1000,56/1000) and A1 in(45/1000,46/1000). In either bit order, final children have capacities -A,B with B>A. With saturated incoming D, T=D+e=(B-A)/2. The kernel(0,2) transports old/new labels to debit(0,B-A) and transfer(A,-A). Both residuals are zero. The earlier parked2tau is untouched. The generic source theorem follows by defining P=E(s)_+,N=E(-s)_+: feasibility needs T<=P-N and the minimum new gross transfer is N, attained by k=(s)_+/P, debit T*k and flow(-s)_+-N*k. For P=0 feasibility forces N=T=0. This reconstructs the source proof and its physical application, not just its title or hash.

The new allocation lemma retains inherited credit. Let finite weights be nonnegative and sum to1; work on their positive-weight support. Let signed raw capacities s_b, A>=0 and T>=0 be supplied. Seek nonnegative inherited credits a_b and nonnegative total booked debits d_b, with E a=A, E d=T, signed NEW flow f with E f=0, and s_b+a_b+f_b-d_b>=0. Put n=(-s)_+,p=(s)_+,N=E n,P=E p. Such a payment exists iff T<=P-N+A. Its least additional gross flow E(f)_+ is max(0,N-A).

Necessity: average residual gives aggregate feasibility. On each negative-capacity outcome, f_b>=n_b-a_b+d_b>=n_b-a_b. Therefore E(f)_+>=N-E_[s<0]a>=N-A, and it is also nonnegative. This uses nonnegative inherited credit and nonnegative total booked debit; allowing arbitrary signed credit would change the optimization.

Sufficiency if A>=N: if P>0 choose k=p/P; if P=0<N choose k=n/N; if P=N=0 choose k=1. Set a=n+(A-N)k,d=T*k,f=0. The kernel is nonnegative and has mean1, mean a=A, mean d=T, and residual=(P+A-N-T)k>=0 (when P=0 the same formula applies). No vanishing denominator is cancelled.

If N>A, feasibility and T>=0 force N>0 and P>0. Put z=N-A,k=p/P and set a=(A/N)n,d=T*k,f=(z/N)n-z*k. Then E a=A,E f=0, and residual=(P-z-T)k>=0. Positive flow occurs only on negative-capacity recipients, so its mean is exactly z. Thus the lower bound is sharp. Every inherited signed DEBIT label and the new e label travel as L*k, preserving their means even if T=0; incoming credit is separately conserved by a. The donor's original outgoing A is not refreshed by these child allocations. The scalar proof covers A=0,N=0,P=0,T=0, equality and negative raw capacities.

Application to all10 next rows: all20 raw full children are negative. For nine active queries N<A and e=A-N>0. The remaining b0/original-bit1 query is a dummy with exact e=0,N=A. For an active row use k_b=(-s_b)/N, incoming credit a_b=A*k_b and new debit d_b=e*k_b. Then s_b+a_b-d_b=s_b+(A-e)k_b=s_b+N*k_b=0 exactly. Both means are retained. All nine kernels lie strictly between3/5 and7/5. For b0, e is in(96/10000,97/10000); for b1 in(32/10000,33/10000). The stopped donor remains at reach1/64, outgoing A and debit B-A; the new recipients have reach1/128 each. Root-weighted financial conservation follows from their conditional means.

This exposes a false stronger rule: leaving A CONSTANT in the two new outcomes needs new row flow, despite zero optimal extra flow. Its minimal gross is E(-(s+A))_+, strictly positive in all9 active rows (displays0.0037277438922 for b0 and0.0050729786245 for b1). These decimals do not decide signs. The correct mean-one nonflat redistribution of the SAME original subsidy pays them without new flow. No source theorem is blamed for the stronger rule; it is an explicit countersearch target.

All-adaptive extension: after b0 the active core is AND4 with one dummy; after b1 it is AND5. Define AND_m to be negative exactly on the all-zero input (AND_0 is constant-1), and F_m=J(-1,AND_m,g,g,g,g),0<=m<=5, and F_plus=J(-1,+1,g,g,g,g). An active data query has full children F_(m-1),F_plus and physical influence q1*2^(1-m). Only these seven profiles are needed. Within-core permutations preserve the actual function, all q weights, spectra and inherited kernel. A failure answer makes only this core constant; the OTHER full cores remain. Dummy queries cost zero and stopping prunes the tree. Consequently every adaptive query order/stopping policy is covered by the finite m recursion; no general affine mixing or untested coordinate symmetry is invoked.

Carry credit A_v and booked debit D_v with invariant S(F_m)+A_v=D_v, starting with the actual A=-S,D=0. At each active query calculate the SAME T=D_v+e, not just e, and apply the inherited-credit optimizer to the two raw children. In all nine recursion rows (m4..1 and m5..1) T>0 and N<A_v; hence new flow is exactly0, every old label keeps its mean and all child residuals stay exactly0. Credit may increase CONDITIONALLY along the success branch, but its conditional mean stays A_v; root-weighted terminal credit equals the original A, as checked explicitly in VERIFICATION. It is not a new draw from the stopped donor. Both complete chains, their stopped full F_plus terminals and all earlier root branches remain in the account. Local mean identities compose by iterated finite expectation, without multiplying unrelated conditional probabilities. The two chains cover all adaptive core1 histories, not queries in the four remaining cores.

First unsupported universal line: arbitrary retained Boolean component data imply N<=A_v and T=D_v+e>=0, or the optimizer's positive gap max(0,N-A_v) can be paid from a genuinely unused ancestor account. These signs are certified on seven explicit profiles here; the allocation theorem alone cannot establish them for arbitrary spectra. No unrestricted FEI constant changes, and no counterfamily with unbounded H/I is given.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC fixes10 labelled queries plus18 dependency states, explicit Boolean tables/prefix, no quotient, completeness limit, source helper pins, Fraction arithmetic and192-bit outward logs,120MB estimated memory and55s caps. The two-case pilot takes1.938s; full subsidy.py takes{result['runtime_seconds']:.3f}s and records{result['engine_checks']} engine checks. Both spectrum paths agree on all relevant states and exactly2 source negative signs. Four source policies are checked separately. The zero-influence dummy is handled by an algebraic identity, not a float tolerance.

ADAPTIVE_SPEC precedes the seven-profile extension. adaptive.py finishes in{ad['runtime_seconds']:.3f}s; all7 full profiles are reconstructed independently, both inherited-account chains complete, and all9 physical recursion rows have certified zero additional flow. SCALAR_SPEC precedes the exact rational adversarial grid: {scalars['cases']} allocation cases and{scalars['exact_checks']} checks, including signed capacities, T=0, A=N, P=N=0, A=0 and N>A. No sample is called a proof over a continuum: the continuum result is the explicit algebraic proof above. Independent spectrum reproduction shares the bounded-log primitive, whose range-reduced80-term atanh enclosure has error at most18/[8*161*3^161], with every arithmetic step rounded outward. The first scalar boundary helper failed after an integer-zero sum became float; out/FIRST_FAILURE.json preserves the defect. Typed Fraction zeros repair the helper, and the rerun passes all677 scalar cases. No failed-run verdict is used. Final accepted checks use no floating-point sign or equality tolerance. Interval overlaps diagnose identities established algebraically; they do not prove equalities or zero residuals.

Commands from A071: python -B -X utf8 runs/{run}/code/subsidy.py --pilot; then subsidy.py; adaptive.py; finalize.py. All exact outputs are in out/. Every job is expected<=120MB and observed mathematical runtime below55s, so no >300MB job or memok admission is needed. Jobs are serial, with no GPU, detached work, new worker, automatic dimension/rate escalation or full30/36-bit table materialization. No Lean certification is claimed. The proof rung is author algebraic proof plus exact finite certificates and distinct spectrum reproduction, awaiting independent review. No project tree, brain, other agent, shared checklist or remote repository is written under the user A071-only boundary; no git or messaging occurs.

# proof dependencies and changed downstream conclusions

A089's exact-version signed-terminal theorem is independently accepted unchanged and recorded with its original statement hash. The finite proof rederives all physical identities from actual Boolean profiles, rather than assuming universal child FEI. The new theorem and adaptive extension remain independently unreviewed. Downstream A072/A089 may now replace flat subsidy reuse or a fresh charge N by conserved incoming credit and only the additional gap max(0,N-A). The actual supplied core1 interface is fully paid, including its complete reveal and all old stopped accounts. This is stronger than another first-row check but supplies no arbitrary-core admission theorem.

# one next mathematical action and independent reviewer

{next_action} The next negative F_plus leaf has explicit subsidy(-S_plus), total booked debit0, and an already spent ancestor donor, so it exposes the same universal eligibility question after a genuinely completed core rather than a fresh root. Do not call positive terminal capacity a fresh owner or omit any source entropy. A074/A092 should reconstruct the nonflat credit kernels, boundary construction, exact core1 symmetry and root-weighted terminal credit receipts.

# actual persistence receipts or precise save blocker

The four protocol files, three frozen specs, local code,10-case/18-state certificates,7-profile recursion, scalar grid and financial terminal receipts are saved inside this A071 run. STATUS is exactly two lines; WORKLOG and LEARNED append the result. out/MANIFEST.json gives sizes and hashes except itself; out/SCHEMA_VALIDATION.json checks exact protocol field sets, unchanged source statement hashes and identical PROGRESS/PACKET_DELTA. Each file is under20MB. Supervisor copy, shared-registry adoption, remote mirror verification and independent acceptance of the NEW theorem remain unverified. Checklist/brain writes and git pushes are not performed because the explicit owner boundary permits writes only inside A071.

# Universal bridge

This stage moves C019 stopping-tree payment through every adaptive partial or complete reveal of the newly exposed core1, using the SAME original negative-terminal subsidy and unchanged spent donor, with zero additional transfer on all9 recursion rows. The sharp inherited-credit price max(0,N-A) replaces an unnecessary fresh N charge and nine real flat-subsidy failures have explicit nonflat repairs. What remains is universal signed-component eligibility and payment of any positive additional gap under other-core queries. NEXT keeps the existing stopped negative full terminal, original donor expenditure and old labels, so it attacks the missing history-sensitive FEI payment directly rather than collecting another isolated root class bound.
'''
    (root/'REPORT.md').write_text(report,encoding='utf-8')
    (home/'STATUS.md').write_text('STATE: A071 stage18: A089 signed transfer independently accepted; SAME subsidy pays all adaptive core1 reveals via7 profiles,9 recursion rows;9 flat-subsidy failures;FEI OPEN, new review pending.\nNEXT: A072/A089 query OTHER core in stopped negative F_plus with SAME credit,booked labels,spent donor;A074/A092 review inherited-credit optimizer and all-tree receipts.\n',encoding='utf-8')
    now=datetime.datetime.now(datetime.timezone.utc).isoformat()
    for name,line in [('WORKLOG.md',f'{now} | Stage18: A089 negative terminal transfer accepted unchanged. Ten next queries,18 source states,4 policies,7-profile all-adaptive core1 extension certified. Same inherited subsidy, no fresh donor/no new row flow. Nine flat-allocation failures. {scalars["cases"]} scalar cases. New optimizer and extension pending review;FEI open.'),('LEARNED.md',f'{now} | Signed full capacity s with inherited credit A>=0 has minimum ADDITIONAL zero-mean gross flow max(0,E(-s)+ -A), provided0<=T<=E(s)+A; credit and total debit must remain nonnegative. Do not recharge full negative part N after a subsidy is already assigned. On A089 negative terminals, nine active core1 rows need nonflat mean-one credit kernels in(3/5,7/5), but no new donor draw; constant credit across outcomes spuriously needs flow. AND4/AND5 profiles give every adaptive core1 reveal at same4 with old debit/credit means retained. Conditional credit grows on rare branches while total expected original subsidy is conserved. Arbitrary-component N<=A and T>=0 remain unpaid.')]:
        with (home/name).open('a',encoding='utf-8',newline='') as f:f.write('\n'+line+'\n')
    protocol=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
    expected=set(protocol['required_per_run']['progress_fields']);expected.remove('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
    ck(set(progress)==expected)
    for c in claims:ck(set(c)==set(protocol['required_per_run']['claim_fields']));ck(hashlib.sha256(c['exact_statement'].encode()).hexdigest()==c['statement_sha256'])
    ck((root/'PROGRESS.json').read_bytes()==(root/'PACKET_DELTA.json').read_bytes())
    ck(len((home/'STATUS.md').read_text(encoding='utf-8').splitlines())==2)
    validation=dict(progress_fields_exact=True,claim_fields_exact=True,statement_hashes_exact=True,delta_identical=True,status_two_lines=True,
        original_source_hash=old['statement_sha256'],new_claim_hash=digest)
    (root/'out/SCHEMA_VALIDATION.json').write_text(json.dumps(validation,indent=2)+'\n',encoding='utf-8')
    manifest={}
    for p in root.rglob('*'):
        if p.is_file() and p.name!='MANIFEST.json':
            ck(p.stat().st_size<20_000_000);manifest[str(p.relative_to(root))]=dict(bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest())
    (root/'out/MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(files=len(manifest),scalar=scalars,source_accepted=old['claim_id'],new_claim=claim['claim_id'],schema=validation)))

if __name__=='__main__':main()
