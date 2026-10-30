#!/usr/bin/env python
"""Writes CLAIMS.json, PROGRESS.json, PACKET_DELTA.json and out/RECEIPTS.json for this run. Usage: python -X utf8 write_records.py RUNDIR"""
import hashlib, json, os, sys
RUN = sys.argv[1]
RID = '20261011T225832Z-claude-B12-erasure-ledger-depth'
def sha(s): return hashlib.sha256(s.encode('utf-8')).hexdigest()
res = json.load(open(os.path.join(RUN, 'out', 'results.json'), encoding='utf-8'))
claims = []
def claim(cid, stmt, hyp, status, src, deps, first, nxt, supersedes=None, refutes=None):
    claims.append(dict(claim_id=cid, version=1, exact_statement=stmt, hypotheses=hyp, statement_sha256=sha(stmt),
                       contributors=['claude-B12-lead'], proof_source=src, proof_dependencies=deps, review_records=[],
                       status=status, supersedes=supersedes or [], refutes=refutes or [], first_unproved_line=first, next_consumers=nxt))
claim('B12-L1-MONOTONE-ERASURE',
      'Let F=g(h_1,...,h_m) on pairwise disjoint blocks of independent uniform signs, g Boolean on m bits, every h_k Boolean and balanced. '
      'Fix a coordinate i in block j; write a_T=ghat(T), b_T=ghat(T+{j}) for T not containing j, q=Inf_j(g)=sum_T b_T^2, alpha=hhat_j({i}), '
      'phi(u,v)=(u+v)ln(u+v)-u ln u-v ln v and L_j(x)=sum_T phi(a_T^2, x b_T^2) (nats). Then L_j is nondecreasing and concave on [0,1] with '
      "L_j'(x)=sum_T b_T^2 ln(1+a_T^2/(x b_T^2)) and L_j(1)=B_j(g); hence L_j(alpha^2) <= min{B_j(g), alpha^2 B_j(g)+q alpha^2 ln(1/alpha^2)} "
      'and, by the A057 erasure split, B_i(F) <= q B_i(h_j) + min{B_j(g), alpha^2 B_j(g)+q alpha^2 ln(1/alpha^2)}.',
      ['disjoint blocks', 'uniform product measure', 'children balanced', 'B_i = erasure entropy H(1[i in S] | S minus i) of the squared Fourier law, nats'],
      'PROVED', 'REPORT.md section L1 (one-line derivative of phi in v; L_j(1) is the packet form of B_j(g); concavity from second derivative)',
      ['A057-COHERENT-ERASURE-SPLIT v1 (identity only; lead re-derived it and replayed it exactly on 6,468 cases)'], None,
      ['A057 (outer-erasure transport)', 'A059 (depth)', 'A091 review'])
claim('B12-L2-DEFICIT-LOG-BANK',
      'For every balanced Boolean h on finitely many independent uniform signs, Lambda(h) := sum_i hhat({i})^2 ln(1/hhat({i})^2) <= (4+6/e)(I(h)-1) nats. '
      'Consequently, in a balanced disjoint composition F=g(h_1,...,h_m), sum_j q_j Lambda(h_j) <= (4+6/e)(I(F)-I(g)), q_j=Inf_j(g).',
      ['h Boolean, E h = 0', 'I = total influence', 'natural logarithms'],
      'PROVED', 'REPORT.md section L2: with M=max|hhat({i})|, u=1-M, s=sum of the other influences, I-1>=s-u and I-1>=1-W1>=u(2-u)-(1-u)s give I-1>=u/2 and s<=3(I-1); '
      'M^2 ln(1/M^2)<=2Mu<=2u and r^2 ln(1/r^2)<=(2/e)r with |hhat({i})|<=Inf_i(h)',
      ['|hhat({i})| <= Inf_i(h) (half-difference)', 'I(F)=sum_j q_j I(h_j) for balanced disjoint children (A056 identity)'], None,
      ['A057', 'A059', 'A091 review'])
claim('B12-R1-FORMULA-BANK-REUSE-IS-DEPTH-LOSSY',
      'For k>=2 let g_k(y,z_1,...,z_k)=sign((k-1)y+z_1+...+z_k), u=2^(1-k), and let F_{k,d} be the read-once chain F_0=x_0, F_{t+1}=g_k(F_t, fresh z^(t)). '
      'Then F_{k,d} is odd, so B(F_{k,d})=sum_i B_i(F_{k,d})=0; I(F_{k,d})=1+(k-1)(1-(1-u)^d)<k; H(F_{k,d})=H(g_k)(1-(1-u)^d)/u. The level-by-level iteration of the '
      'A057 root ledger charges the coherent bank sum_{s=0}^{d-1}(1-u)^{s+1} Lambda(F_{k,d-1-s}) nats, and for d=2^(k-1) this is >= e^(-2-2u)(2^(k-1)-1). '
      'Hence bank/I(F) >= e^(-3)(2^(k-1)-1)/k, unbounded: no constant-factor, depth-uniform bound follows from iterating the root ledger over formula depth with the '
      'q*Lambda bank (a fortiori with the (2/e)I bank), although B=0 and H<=4I-type bounds hold on the family. The L1 bound evaluates every L-term of the family exactly (all 0).',
      ['read-once chain of balanced odd threshold gates', 'uniform measure'],
      'PROVED', 'REPORT.md section R1; exact brute-force certificate for (k,d) in {(2,1..4),(3,1..3)} and closed-form table k=2..14 in out/results.json',
      ['A056 balanced chain rule (H, I, coefficient formula)', 'oddness kills every erasure pair'], None,
      ['A059 (do not iterate the root ledger over depth)', 'A057 (bank must be charged on a non-reusing physical tree)'])
v2 = res['V2_A057_split']; v6 = res['V6_A058']
claim('B12-REPLAY-A056-A057-A058',
      'Finite exact statements: (i) AND2(maj3(x,a,b),z) with x=+1 has mean -1/4, I=5/4, H=4-(9/8)log2(3) bits; (ii) the A057 erasure split B_i(F)=q B_i(h_j)+L_j(alpha_i^2) '
      f'holds exactly on all {v2["identity_checks"]} coordinate checks over the {v2["pairs"]} frozen (g,h) pairs, and J:=D_i(F)-qD_i(h_j)-L_j lies in [0,2q alpha^2] on {v2["L1_checks"]} cases '
      f'(max J/(q alpha^2) = {v2["J_over_qx_max"]:.4f}); (iii) A058 example f_k has H=2k+1 bits, I=k+1/2 for k=1,2,3, and the anchored identities '
      f'H(f)=H(F)+sum d_j H(b_j), I(f)=I(F)+sum d_j I(b_j) hold exactly on {v6["random"]["instances"]} random instances.',
      ['domains frozen in out/FROZEN_SPEC.json'], 'CERTIFIED',
      'code/b12_verify.py, out/results.json (prime-log exact identities; 40-digit evaluation with explicit margin for the J and L1 inequalities)', [], None,
      ['A091/A090 (lead replay is not the protocol review)'])
json.dump(claims, open(os.path.join(RUN, 'CLAIMS.json'), 'w', encoding='utf-8'), indent=1)
prog = dict(protocol_revision='2026-10-11-execution-v2', run_id=RID, stream='B12', packet_id='A057', gap_id='B12-coherent-remainder-depth',
            attempt_id='claude-B12-1', method='exact prime-log replay + analytic lemmas on the erasure packet function + explicit depth family',
            mathematical_delta='L1: the A057 packet remainder L_j is monotone with L_j(1)=B_j(g), so L_j(alpha^2)<=min{B_j(g), alpha^2B_j(g)+q alpha^2 ln(1/alpha^2)}; '
                               'L2: first-level log bank Lambda(h)<=(4+6/e)(I(h)-1) nats for balanced h (deficit-paid, best seen ratio 3ln2 at Maj3); '
                               'R1: iterating the root ledger over formula depth is unboundedly lossy (odd threshold chains: B=0, I<k, bank>=e^-3(2^(k-1)-1)); '
                               'A056/A057/A058 finite claims replayed exactly with zero failures.',
            deliverable_status='complete except REPORT.md (refused by the subagent Write guard; content in the lead StructuredOutput)', mathematical_status='PROVED (L1, L2, R1); CERTIFIED (replay); full FEI OPEN',
            claim_versions_used=['A057-COHERENT-ERASURE-SPLIT v1', 'A057-NONREUSING-ALPHA-LOG-PAYMENT v1', 'A056 balanced/biased composition identities v1', 'A058 anchored overlap theorem v1'],
            claims_created_or_changed=[c['claim_id'] + ' v1' for c in claims],
            source_artifacts=['agents/A056/runs/20261011T214407Z-fleet05-A056-balanced-composition/REPORT.md',
                              'agents/A057/runs/20261011T220314Z-fleet05-A057-coherent-restriction-remainder (REPORT.md, LEARNED.md)',
                              'agents/A058/runs/20261011T222138Z-fleet05-A058-overlapping-compositions/OVERLAPPING_COMPOSITION_CLASS.tex, OVERLAP_ENTROPY_LEDGER.md',
                              'mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'],
            next_consumers=['A091 (review L1, R1 after A057 claims)', 'A057', 'A059', 'A056', 'A058'],
            next_action='Prove the biased-child erasure split so L1 and the A057 physical-tree bank apply at every node of an adaptive restriction tree; then test sum_v w_v min{B_j(g_v), alpha_v^2 B_j(g_v)+q_v alpha_v^2 ln(1/alpha_v^2)} <= K I(f) on the sparse-bent physical tree.',
            stagnant_substantive_attempts=0,
            blockers=['stream is over the 2-claim unreviewed cap (A057 has 2 pending): lead claims queue behind them for A091/A090',
                      'git, brain and mesh writes are the coordinator\'s; this run is saved only on local disk',
                      'REPORT.md was refused by the subagent Write guard ("return findings as text"); its full content is in the lead StructuredOutput for the coordinator to materialize; .final withheld until REPORT.md exists'],
            packet_ids=['A057'])
json.dump(prog, open(os.path.join(RUN, 'PROGRESS.json'), 'w', encoding='utf-8'), indent=1)
json.dump(prog, open(os.path.join(RUN, 'PACKET_DELTA.json'), 'w', encoding='utf-8'), indent=1)
rec = {}
for sub in ('code', 'out'):
    for fn in sorted(os.listdir(os.path.join(RUN, sub))):
        p = os.path.join(RUN, sub, fn)
        if os.path.isfile(p) and fn != 'RECEIPTS.json':
            rec[sub + '/' + fn] = hashlib.sha256(open(p, 'rb').read()).hexdigest()
for fn in ('CLAIMS.json', 'PROGRESS.json', 'PACKET_DELTA.json'):
    rec[fn] = hashlib.sha256(open(os.path.join(RUN, fn), 'rb').read()).hexdigest()
json.dump(rec, open(os.path.join(RUN, 'out', 'RECEIPTS.json'), 'w', encoding='utf-8'), indent=1)
print(json.dumps(rec, indent=1))
