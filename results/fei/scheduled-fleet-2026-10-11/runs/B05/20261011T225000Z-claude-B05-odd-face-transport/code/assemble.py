import json, hashlib, os, sys
RUN = sys.argv[1]
RID = '20261011T225000Z-claude-B05-odd-face-transport'


def sha_stmt(statement, hypotheses):
    return hashlib.sha256(json.dumps({'statement': statement, 'hypotheses': hypotheses}, sort_keys=True,
                                     separators=(',', ':')).encode('utf-8')).hexdigest()


def sha_file(p):
    h = hashlib.sha256()
    with open(p, 'rb') as fh:
        h.update(fh.read())
    return h.hexdigest()


H_ALL = ['f:{0,1}^n->{-1,1}, n>=1', 'entropies in bits, Fourier weights p_S = hat f(S)^2',
         'g=f|x_i=0, h=f|x_i=1, d=Inf_i(f)=Pr[g!=h]',
         'B_i(f)=sum_T q_T h2(e_T/q_T), q_T=(a_T^2+b_T^2)/2, e_T=(a_T-b_T)^2/4, a=hat g, b=hat h']
SRC = ['runs/' + RID + '/REPORT.md', 'runs/' + RID + '/code/iso_check.py', 'runs/' + RID + '/out/iso_check.log']
claims = []


def add(cid, statement, hyps, status, proof_source, deps, first_unproved=None, refutes=None, nxt=None):
    claims.append(dict(claim_id=cid, version=1, exact_statement=statement, hypotheses=hyps,
                       statement_sha256=sha_stmt(statement, hyps), contributors=['claude-B05-lead'],
                       proof_source=proof_source, proof_dependencies=deps, review_records=[], status=status,
                       supersedes=[], refutes=refutes or [], first_unproved_line=first_unproved,
                       next_consumers=nxt or ['B19', 'A087', 'A094', 'A023', 'A025']))


add('B05-ODDFACE-ISO-PAYMENT',
    'For every Boolean f and coordinate i: B_i(f) <= h2(d) <= (1/2) I(g h) + log2(e) d, and d log2(1/d) <= (1/2) I(g h) <= (1/2)(I(g)+I(h)).',
    H_ALL, 'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW',
    'REPORT.md section 2 Lemma 1; exhaustive n<=4 check out/iso_check.log Part A',
    ['concavity of h2 (Jensen with weights q_T)',
     'cube edge-isoperimetric inequality e(S) <= (|S|/2) log2 |S| (Harper 1964, Bernstein 1967, Hart 1976)'])
add('B05-ODDFACE-TELESCOPE',
    'Let N_odd(f) be the number of 2-faces of {0,1}^n on which f has corner product -1 and Q(f)=2^(1-n) N_odd(f). For every i, Q(f) = (1/2) I(g h) + (Q(g)+Q(h))/2; hence in every restriction tree sum_v w_v (1/2) I(g_v h_v) = Q(f) - sum_leaves w Q(leaf) <= Q(f), each odd face charged at exactly one node; and Q(f) = (1/4) sum_i I(f|x_i=0 f|x_i=1).',
    H_ALL, 'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW',
    'REPORT.md section 2 Lemma 2; telescope checks out/iso_check.log Parts A and C', [])
add('B05-ODDFACE-UNCONDITIONAL',
    'For every Boolean f, H(f) <= (log2 e + c_JS) I(f) + Q(f), with c_JS = 2/ln 2 under C005 and c_JS = 4 unconditionally (Topsoe).',
    H_ALL, 'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW', 'REPORT.md section 2 Theorem 3',
    ['B05-ODDFACE-ISO-PAYMENT v1', 'B05-ODDFACE-TELESCOPE v1',
     'C005 (JS constant) or Topsoe 2000: JS_nats <= (ln2/2) Delta'])
add('B05-ODDFACE-LOCALIZED-REDUCTION',
    'For every Boolean f, every restriction tree T with constant leaves and every K >= log2 e: H(f) <= (K + c_JS) I(f) + sum over v in T with B_v > K d_v of w_v (1/2) I(g_v h_v). Hence FEI holds with C = K + c_JS + Kp on any family admitting such trees with bad-node odd-face credit <= Kp I(f).',
    H_ALL, 'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW', 'REPORT.md section 2 Theorem 4',
    ['B05-ODDFACE-ISO-PAYMENT v1', 'B05-ODDFACE-TELESCOPE v1', 'C005'])
add('B05-ODDFACE-LOCALIZED-BRIDGE',
    'There are absolute K, Kp such that every Boolean f admits a restriction tree with constant leaves whose bad nodes (B_v > K d_v) carry odd-face credit sum w_v (1/2) I(g_v h_v) <= Kp I(f).',
    H_ALL, 'OPEN',
    'REPORT.md section 2 Theorem 4 (first unproved line); evidence out/iso_check.log Part C and out/b05_ledger_k6.log',
    ['B05-ODDFACE-LOCALIZED-REDUCTION v1'],
    first_unproved='the existence, for every Boolean f, of a tree whose bad-node odd-face credit is <= Kp I(f); no argument yet; candidate obstruction: nested rare-flip towers')
add('B05-ODDFACE-B05-FAMILY-PAID',
    'On the archived B05 sparse-activation family (bent k bits, one-point flip, r controls active on one point, selector y): I(F) = 2^(-k-r) + 2^(-r)(k/2 + k 2^(-k)) + r 2^(-r)(1 - 2^(-k/2) + 2^(-k)); in the selector-first tree the root credit (k+r)2^(-k-r) is <= 2^(1-k) I(F) for k >= 2; exact bad-node credit / I at K=4 is 0.0851, 0.0284, 0, 0 (k=4, r=8) and 0.0249, 0.0113, 0.0193, 0.0057 (k=6, r=12) in the orders selector-first, control-first, data-first, control-data-selector.',
    H_ALL + ['k>=4 even, r>=1 (ledgers only at (4,8) and (6,12))'],
    'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW (formula and root bound); CERTIFIED_EXACT_FINITE (ledgers)',
    'REPORT.md section 2 Proposition 5; out/b05_ledger_k6.log',
    ['B05-SPARSE-ACTIVATION-VARIANCE-REFUND-NOGO v1 (family definition)'])
add('B05-A021-REMAINDER-SIGN-CORRECTION',
    'In A021 v1 section 2, R(q) := -2(1-q)^2 log2(1-q) - (2cq - 3cq^2) with c = log2 e equals +4c sum_{j>=3} q^j/[j(j-1)(j-2)] and satisfies 0 <= R(q) <= 2cq^3/[3(1-q)]; consequently G_s = R(u) - R(2u)/2 <= 0. A021 states the opposite signs (R <= 0, G_s >= 0).',
    ['0 < q <= 1/2', '0 < u <= 1/4'], 'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW',
    'REPORT.md section 3; out/a021_remainder_sign.txt (50-digit values)', ['power series of ln(1-q)'],
    refutes=['A021-UNIFORM-RARE-CORE-EXPANSION v1 (remainder sign clause only)',
             'A021-CONTROL-FIRST-KL-LEDGER v1 (G_s sign clause only)'],
    nxt=['A021', 'A023', 'A087', 'A094'])
with open(os.path.join(RUN, 'CLAIMS.json'), 'w', encoding='utf-8') as fh:
    json.dump(claims, fh, indent=1)
progress = dict(
    protocol_revision='2026-10-11-execution-v2', run_id=RID, stream='B05', packet_id='A023', gap_id='G-R-SELECT',
    attempt_id='B05-claude-1',
    method='isoperimetric bound on the rare logarithm, exact odd-face telescope, localized reduction; exhaustive and exact-ledger certificates',
    mathematical_delta='Universal local bound B_i <= (1/2)I(gh) + log2(e) Inf_i with a single-use odd-face credit that telescopes exactly to Q(f) = 2^(1-n) N_odd; H <= (3/ln2) I + Q; FEI reduced to bounding odd-face credit at bad (rare, spread) nodes; the B05 no-go family is paid with ratio <= 0.025 at k=6; A021 remainder signs corrected.',
    deliverable_status='COMPLETE', mathematical_status='PARTIAL_PROGRESS_FEI_OPEN',
    claim_versions_used=['C005', 'C013', 'C018', 'C019', 'B05-SPARSE-ACTIVATION-VARIANCE-REFUND-NOGO v1',
                         'A021-UNIFORM-RARE-CORE-EXPANSION v1', 'A021-CONTROL-FIRST-KL-LEDGER v1',
                         'A023-FIRST-REVELATION-BIASED-CONTROL-LEDGER v1'],
    claims_created_or_changed=[c['claim_id'] + ' v1' for c in claims],
    source_artifacts=SRC + ['runs/' + RID + '/out/b05_ledger_k6.log', 'runs/' + RID + '/out/a021_remainder_sign.txt'],
    next_consumers=['B19', 'A087', 'A094', 'A021', 'A023', 'A025'],
    next_action='Compute the bad-node odd-face credit against I exactly on nested rare-flip towers (depth 2 and 3, four frozen orders).',
    stagnant_substantive_attempts=0,
    blockers=['git, brain and mesh persistence delegated to the coordinator by task rule'])
with open(os.path.join(RUN, 'PROGRESS.json'), 'w', encoding='utf-8') as fh:
    json.dump(progress, fh, indent=1)
delta = dict(progress)
delta['packet_ids'] = ['A023']
with open(os.path.join(RUN, 'PACKET_DELTA.json'), 'w', encoding='utf-8') as fh:
    json.dump(delta, fh, indent=1)
files = ['CLAIMS.json', 'PROGRESS.json', 'PACKET_DELTA.json', 'code/iso_check.py', 'code/b05_ledger_k6.py',
         'code/a021_remainder_sign.py', 'code/assemble.py', 'out/iso_check.json', 'out/iso_check.log',
         'out/b05_ledger_k6.json', 'out/b05_ledger_k6.log', 'out/a021_remainder_sign.txt']
rec = ['## 7. Persistence receipts', '',
       'Saved on disk in this run directory (sha256 below). Git, brain and mesh persistence belong to the coordinator by task rule; there is no save blocker on disk.', '']
for f in files:
    rec.append('- %s  %s' % (f, sha_file(os.path.join(RUN, f))))
body = open(os.path.join(RUN, '_body.md'), encoding='utf-8').read().rstrip() + '\n\n' + '\n'.join(rec) + '\n\n'
bridge = open(os.path.join(RUN, '_bridge.md'), encoding='utf-8').read()
with open(os.path.join(RUN, 'REPORT.md'), 'w', encoding='utf-8') as fh:
    fh.write(body + bridge)
for c in claims:
    print(c['claim_id'], c['statement_sha256'][:16], c['status'])
