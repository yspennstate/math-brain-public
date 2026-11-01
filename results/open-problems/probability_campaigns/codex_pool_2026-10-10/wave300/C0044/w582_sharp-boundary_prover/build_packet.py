"""Bounded exact audit and draft preparation; never integrates or writes a store."""
from __future__ import annotations

import ctypes
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import re
import shutil
import sqlite3
import time
import urllib.request

ROOT = Path(__file__).resolve().parent
INBOX = Path('~/math-brain-inbox/w582')
HOOK = Path('~/primary_directive/hooks1000/proposals/math-w582.jsonl')
STAMP = datetime.now(timezone.utc).isoformat()


def dump(name, value):
    (ROOT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class MemoryStatus(ctypes.Structure):
    _fields_ = [('length', ctypes.c_uint32), ('load', ctypes.c_uint32)] + [
        (name, ctypes.c_uint64) for name in ['total_phys', 'avail_phys', 'total_page',
                                           'avail_page', 'total_virtual', 'avail_virtual', 'extended']]


def fresh_gate():
    memory = MemoryStatus()
    memory.length = ctypes.sizeof(memory)
    if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(memory)):
        raise RuntimeError('Unable to measure available memory')
    gate = {'utc': STAMP, 'purpose': 'exact rational arithmetic audit only',
            'available_physical_bytes': memory.avail_phys,
            'free_disk_bytes': shutil.disk_usage(ROOT).free,
            'cpu_budget_seconds': 2, 'wall_budget_seconds': 30,
            'memory_budget_bytes': 32 * 1024 * 1024, 'gpu': False,
            'child_agents': False, 'background_work': False}
    gate['pass'] = gate['available_physical_bytes'] >= gate['memory_budget_bytes'] and gate['free_disk_bytes'] >= 1024 * 1024
    dump('COMPUTE_GATE.json', gate)
    if not gate['pass']:
        raise RuntimeError('Exact-arithmetic resource gate refused')
    return gate


def q(k):
    return 1 - F(1, 4) * F(1, 3) ** k if k >= 0 else F(3, 4) * F(3) ** k


def exact_audit():
    gate = fresh_gate()
    cpu, wall = time.process_time(), time.perf_counter()
    assertions, cases = 0, 0

    def check(condition):
        nonlocal assertions
        assertions += 1
        if not condition:
            raise AssertionError(f'Exact assertion {assertions} failed')

    for d in [2, 3, 4, 8]:
        transverse = F(1, 4 * (d - 1))
        kappa = min(F(1, 8), transverse)
        for k in range(-40, 41):
            right, left = (F(3, 8), F(1, 8)) if k >= 0 else (F(1, 8), F(3, 8))
            row = [right, left] + [transverse] * (2 * (d - 1))
            check(sum(row) == 1)
            check(min(row) >= kappa > 0)
            check(0 < q(k) < 1)
            check(q(k) == right * q(k + 1) + left * q(k - 1) + F(1, 2) * q(k))
            check(1 - q(k) == right * (1 - q(k + 1)) + left * (1 - q(k - 1)) + F(1, 2) * (1 - q(k)))
            check(right - left == (F(1, 4) if k >= 0 else -F(1, 4)))
            cases += 1
    check(q(0) == F(3, 4))
    check(q(-40) < q(-20) < q(-10))
    check(1 - q(40) < 1 - q(20) < 1 - q(10))
    for d in [2, 3, 4, 8]:
        ell = [F(i + 1, d) for i in range(d)]
        kappa = F(1, 2 * d)
        drift = sum(kappa * t + kappa * (-t) for t in ell)
        variance = sum(2 * kappa * t * t for t in ell)
        check(drift == 0)
        check(variance == 2 * kappa * sum(t * t for t in ell) > 0)
    cpu_seconds, wall_seconds = time.process_time() - cpu, time.perf_counter() - wall
    check(cpu_seconds <= gate['cpu_budget_seconds'])
    check(wall_seconds <= gate['wall_budget_seconds'])
    result = {'utc': STAMP, 'status': 'PASS', 'command': 'python -X utf8 -B build_packet.py',
              'rational_boundary_cases': cases, 'exact_assertions': assertions,
              'cpu_seconds': cpu_seconds, 'wall_seconds': wall_seconds,
              'q_at_origin': str(q(0)), 'q_at_minus_40': str(q(-40)),
              'scope': 'Finite exact checks of row normalization, ellipticity, both harmonic recurrences, drift and variance formulas. Infinite-path conclusions are justified by ATTEMPT.md, not by these checks.'}
    dump('VERIFICATION.json', result)
    return result


def source_receipts():
    source_dir = Path('~/Downloads/Probability_1000_intake_claude_20260907/sources/drewitz_ramirez_rwre_2014')
    pdf, text = source_dir / 'source.pdf', source_dir / 'text.txt'
    expected = '5b79b728fd6a0add60442b5a686ed69fdff9041c04d595269824a91e1792ff43'
    receipt = {'primary': {'path': str(pdf), 'url': 'https://arxiv.org/pdf/1309.2589',
                           'bytes': pdf.stat().st_size, 'sha256': sha(pdf),
                           'expected_intake_sha256': expected}}
    receipt['primary']['matches_intake_hash'] = receipt['primary']['sha256'] == expected
    if not receipt['primary']['matches_intake_hash']:
        raise RuntimeError('Primary source bytes do not match the intake receipt')
    locators = []
    with text.open(encoding='utf-8', errors='replace') as handle:
        for line_no, line in enumerate(handle, 1):
            if any(s in line for s in ['Open question 3.2.', '(IID) the coordinate', '(E) for every']):
                locators.append({'line': line_no, 'label': 'question' if 'Open question' in line else 'assumption'})
            if len(locators) >= 3:
                break
    receipt['primary']['text_path'] = str(text)
    receipt['primary']['text_locators'] = locators
    raw = 'https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/DirectionalWalk.lean'
    try:
        request = urllib.request.Request(raw, headers={'User-Agent': 'w582-scoped-source-audit'})
        with urllib.request.urlopen(request, timeout=12) as response:
            data = response.read(128 * 1024 + 1)
        if len(data) > 128 * 1024:
            raise RuntimeError('Single-file source size cap exceeded')
        lines = data.decode('utf-8').splitlines()
        candidates = [{'line': n, 'text': line.strip()} for n, line in enumerate(lines, 1) if 'by sorry' in line]
        snippet = '\n'.join(f'{n}: {line}' for n, line in enumerate(lines, 1) if 76 <= n <= 82)
        (ROOT / 'COMPARATOR_SNIPPET.txt').write_text('As read ' + STAMP + '\n' + raw + '\n' + snippet + '\n', encoding='utf-8')
        receipt['comparator'] = {'url': raw, 'as_read_utc': STAMP,
                                  'whole_file_sha256': hashlib.sha256(data).hexdigest(),
                                  'whole_file_bytes': len(data), 'admitted_placeholders': candidates,
                                  'local_excerpt': 'COMPARATOR_SNIPPET.txt',
                                  'scope': 'Comparator statement only; no claim about a separate complete proof file.'}
    except Exception as exc:
        receipt['comparator'] = {'url': raw, 'download_status': 'unavailable', 'error': str(exc),
                                  'web_evidence': 'Tool read on 2026-10-10 found directional_zero_one ending by sorry on line 81.'}
    dump('SOURCE_RECEIPTS.json', receipt)
    return receipt


def scoped_store_lookup():
    database = Path('~/math-brain-build/local/population/brain.sqlite3')
    result = {'path': str(database), 'access': 'mode=ro', 'search': 'C0044 or exact directional-zero-one title; at most 5 rows', 'rows': []}
    if not database.exists():
        result['status'] = 'unavailable'
        dump('STORE_LOOKUP.json', result)
        return
    start = time.monotonic()
    try:
        with sqlite3.connect('file:' + database.as_posix() + '?mode=ro', uri=True, timeout=0.5) as connection:
            connection.set_progress_handler(lambda: int(time.monotonic() - start > 3), 5000)
            tables = [r[0] for r in connection.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE '%node%'")]
            for table in tables:
                if not re.fullmatch(r'[A-Za-z0-9_]+', table):
                    continue
                columns = {r[1] for r in connection.execute('PRAGMA table_info(' + table + ')')}
                if not {'id', 'title'}.issubset(columns):
                    continue
                body = 'substr(body,1,1800)' if 'body' in columns else "''"
                for row in connection.execute('SELECT id,title,' + body + ' FROM ' + table + " WHERE title LIKE '%C0044%' OR title LIKE '%Zero-one law for directional transience%' LIMIT 5"):
                    result['rows'].append({'table': table, 'id': row[0], 'title': row[1], 'body_excerpt': row[2]})
                if result['rows']:
                    break
        result['status'] = 'targeted read complete' if result['rows'] else 'no matching card in inspected node tables'
    except Exception as exc:
        result['status'], result['error'] = 'bounded read unavailable', str(exc)
    result['elapsed_seconds'] = time.monotonic() - start
    result['scope_limit'] = 'Population mirror only; this does not certify all owner solved/retired work or the latest control-repository state.'
    dump('STORE_LOOKUP.json', result)


def build_bundle(claims):
    attempt = (ROOT / 'ATTEMPT.md').read_text(encoding='utf-8')
    namespace = 'probability.random_environment'
    entries = []

    def add(key, logical, kind, title, statement, proof, assumptions, anchor):
        entries.append({'key': key, 'namespace': namespace, 'logical_name': logical, 'kind': kind,
                        'title': title, 'statement': statement, 'proof_text': proof, 'assumptions': assumptions,
                        'domain': 'probability theory; random walks in random environment',
                        'source': {'source_id': 'campaign:w582:C0044:' + key,
                                   'url': (ROOT / 'ATTEMPT.md').as_uri() + '#' + anchor,
                                   'revision': '2026-10-10-author-derivation-review-pending',
                                   'license': 'owner-own-work (campaign derivation; novelty not claimed)', 'excerpt': None}})

    add('target', 'directional-zero-one-iid-elliptic-rwre-question-c0044', 'concept',
        'C0044 target and its unresolved proof status',
        'Historical question, current openness UNKNOWN: for d>=3, iid nearest-neighbor transition rows on Z^d satisfying strict ellipticity, and each fixed nonzero deterministic l, is the annealed probability of A_l={lim_n X_n dot l=+infinity} in {0,1}? Strict ellipticity means every transition is positive almost surely; no common positive lower bound is required. The source is Drewitz-Ramirez, arXiv:1309.2589, Open question 3.2. Recent claims have not passed the complete-proof and independent-review gates in this packet.',
        None, ['d>=3', 'iid transition rows', 'strict ellipticity', 'fixed nonzero direction'], 'target')
    lookup = {claim['id'].rsplit('-', 1)[-1]: claim for claim in claims}
    details = [('L1', 'floor', 'quenched-directional-escape-uniform-floor-forces-certainty', 'Uniform escape floor forces probability one'),
               ('L2', 'trichotomy', 'quenched-directional-escape-harmonic-trichotomy', 'Quenched harmonic trichotomy and spatial positivity'),
               ('L3', 'balanced', 'zero-local-projected-drift-rwre-projection-oscillation', 'Zero local projected drift implies oscillation'),
               ('L4', 'positive', 'uniform-positive-local-projected-drift-implies-escape', 'Uniform positive projected drift implies escape')]
    for label, key, logical, title in details:
        claim = lookup[label]
        section = attempt.split('## ' + label + ':', 1)[1].split('\n## ', 1)[0].strip()
        add(key, logical, 'lemma', title + ' (draft review packet)',
            'Author-derived scoped result; review/provenance gates tracked separately. ' + claim['statement'],
            section, claim['assumptions'], label.lower())
    add('floor-warning', 'pointwise-escape-positivity-does-not-supply-uniform-floor', 'concept',
        'Pointwise escape positivity is not a uniform floor',
        'For a fixed elliptic nearest-neighbor environment, pointwise positivity of q(x)=P_x^omega(A_l) propagates along finite paths, but the path probability depends on distance. Uniform ellipticity gives q(x)>=kappa^{|x-y|_1}q(y), which need not give a positive infimum over x. A deterministic outward-layered uniformly elliptic environment has 0<q(x)<1 everywhere and inf q=0; it refutes this auxiliary bridge outside the iid class, not the iid C0044 question.',
        None, ['fixed elliptic nearest-neighbor environment', 'q is a directional escape probability'], 'ce1')
    relations = [
        ('floor', 'target', 'semantic_association', 'Floor: "inf_x q(x)>0" supplies an extra sufficient hypothesis for target: "annealed probability ... in {0,1}".'),
        ('trichotomy', 'floor', 'depends_on', 'Trichotomy: "inf_x q=0 and sup_x q=1" for interior values follows by applying floor: "q(x)=1 for every x" to q and its complement.'),
        ('trichotomy', 'target', 'semantic_association', 'Trichotomy: "0<E[q(0)]<1" isolates the mixed alternative that target: "iid ... probability ... in {0,1}" must exclude.'),
        ('balanced', 'target', 'specializes', 'Balanced: "zero local drift projected onto ... l" proves probability zero for the target iid subclass of such uniformly elliptic rows.'),
        ('positive', 'target', 'specializes', 'Positive: "local drift ... at least ... delta>0" proves probability one for the target iid subclass of such rows.'),
        ('floor-warning', 'trichotomy', 'depends_on', 'Warning: "pointwise positivity ... need not give a positive infimum" is supported by trichotomy: interior q has "inf_x q=0".'),
        ('balanced', 'positive', 'analogous_to', 'Balanced: "zero local drift" yields oscillation; positive: "delta>0" yields directional escape. This compares two explicitly different drift hypotheses.')]
    bundle = {'spec': 'mathbrain-draft-v1', 'author_agent': 'w582',
              'bundle_slug': 'c0044-sharp-harmonic-and-drift-boundaries-20261010',
              'entries': entries, 'relations': [{'from_key': f, 'to_key': t, 'kind': k, 'rationale': r} for f, t, k, r in relations]}
    keys = {entry['key'] for entry in entries}
    required = {'key', 'namespace', 'logical_name', 'kind', 'title', 'statement', 'proof_text', 'assumptions', 'domain', 'source'}
    for entry in entries:
        assert required.issubset(entry)
        assert entry['source']['license'].startswith('owner-own-work')
        assert entry['kind'] in {'concept', 'lemma', 'theorem', 'definition'}
        assert (bool(entry['proof_text']) if entry['kind'] in {'lemma', 'theorem'} else entry['proof_text'] is None)
        assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*', entry['logical_name'])
    graph = {key: [] for key in keys}
    allowed = {'depends_on', 'defines', 'proves', 'refutes', 'generalizes', 'specializes', 'analogous_to', 'cites', 'semantic_association'}
    for relation in bundle['relations']:
        assert relation['from_key'] in keys and relation['to_key'] in keys and relation['kind'] in allowed
        if relation['kind'] == 'depends_on':
            graph[relation['from_key']].append(relation['to_key'])
    def visit(key, stack):
        assert key not in stack, 'depends_on cycle'
        for child in graph[key]:
            visit(child, stack | {key})
    for key in keys:
        visit(key, set())
    dump('bundle_001.json', bundle)
    return bundle


def main():
    verification = exact_audit()
    receipts = source_receipts()
    scoped_store_lookup()
    claims = [json.loads(line) for line in (ROOT / 'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line]
    for claim in claims:
        assert claim['status'] in {'conjecture', 'numerical evidence', 'sketch', 'proved special case', 'independently checked proof'}
        assert all(k in claim for k in ['statement', 'assumptions', 'source', 'proof_or_counterexample', 'independent_reviewer', 'remaining_gap'])
    claims[0].update(status='independently checked proof', independent_reviewer='w584; scoped KEEP in ~/brain_workers/w584/CLAIMS.jsonl, row 1',
                     review_status='one scoped mathematical KEEP; cross-login and response-side served-model gate unverified',
                     remaining_gap='General iid strict ellipticity has not been shown to supply a positive quenched spatial infimum.')
    (ROOT / 'CLAIMS.jsonl').write_text(''.join(json.dumps(c, ensure_ascii=False) + '\n' for c in claims), encoding='utf-8')
    bundle = build_bundle(claims)
    INBOX.mkdir(parents=True, exist_ok=True)
    source, destination = ROOT / 'bundle_001.json', INBOX / 'bundle_001.json'
    if destination.exists():
        if destination.read_bytes() != source.read_bytes():
            raise RuntimeError('Existing worker bundle differs; do not overwrite')
    else:
        part = INBOX / 'bundle_001.json.part'
        if part.exists():
            raise RuntimeError('Existing .part checkpoint requires reconciliation')
        part.write_bytes(source.read_bytes())
        part.rename(destination)
    state = json.loads((ROOT / 'SOURCE_STATUS.json').read_text(encoding='utf-8'))
    state.update(primary_statement_source={'title': 'Selected Topics in Random Walks in Random Environment',
                                          'authors': ['Alexander Drewitz', 'Alejandro F. Ramirez'],
                                          'source_id': 'drewitz_ramirez_rwre_2014', 'arxiv_version': '1309.2589v1 (2013)',
                                          'url': 'https://arxiv.org/pdf/1309.2589',
                                          'location': 'Open question 3.2, PDF page 42; (IID), PDF page 6; (E)/(UE), Definition 2.3, PDF page 7',
                                          'short_quote': 'Consider a RWRE satisfying the assumptions (E) and (IID).',
                                          'sha256': receipts['primary']['sha256'], 'hash_status': 'matches intake; not a proof'},
                 prior_attempt_digest_status='complete, targeted C0044-A001/A002; see PRIOR_ATTEMPTS.md',
                 owner_solved_retired_status='bounded population-mirror read only; no exhaustive/current status certificate',
                 recent_comparator_receipt=receipts['comparator'],
                 independent_review='L1 scoped KEEP by w584; four additional mathematical claims pending; served-model/login gate unverified',
                 brain_submission={'state': 'submitted DRAFT', 'path': str(destination), 'local_schema_check': 'PASS; not coordinator validation'},
                 brain_review={'state': 'partially reviewed', 'scope': 'L1 only; no complete provenance gate'},
                 brain_ingestion={'state': 'not ingested by this worker; no receipt observed'},
                 brain_retrieval={'state': 'not tested; no live card claimed'})
    dump('SOURCE_STATUS.json', state)
    hook = {'id': 'S20-w582-01', 'area': 'math', 'event': 'PreToolUse',
            'cue': 'Saving a RWRE escape proof that infers inf_x q(x)>0 only from q(x)>0 at every x.',
            'fire_when': 'A proof says ellipticity and pointwise positive quenched escape imply a common positive floor over all starting sites.',
            'silent_when': 'A separate checked argument supplies inf_x q(x)>=c>0, or the claim is limited to a finite set of starting sites.',
            'text': 'Pointwise positivity of q does not give a uniform spatial floor. Finite-path bounds decay with distance. State and justify the floor separately; a counterexample without iid refutes only the auxiliary bridge.',
            'evidence': str(ROOT / 'ATTEMPT.md') + ' L2/CE1; VERIFICATION.json exact recurrence checks; scar prob1000_ranking_hour_555_problems_and_the_unread_inbox_corrections_2026_09_07',
            'proposer': 'w582'}
    assert len(hook['text']) <= 300
    dump('HOOK_PROPOSAL.json', hook)
    HOOK.parent.mkdir(parents=True, exist_ok=True)
    if not HOOK.exists() or not any(json.loads(line).get('id') == hook['id'] for line in HOOK.read_text(encoding='utf-8').splitlines() if line):
        with HOOK.open('a', encoding='utf-8') as handle:
            handle.write(json.dumps(hook, ensure_ascii=False) + '\n')
    report = f'''C0044 packet prepared: four scoped lemmas and one explicit boundary counterexample. No complete solution or novelty claim.

Exact target: iid strictly elliptic nearest-neighbor environments, d>=3, each fixed nonzero direction. Primary PDF hash matches the intake. C0044-A002 corrects A001's vacuous intersection claim. Current openness is UNKNOWN: recent manuscripts claim a solution, but the checked comparator statement contains an admitted placeholder; the complete proof and independent model gate are unverified.

The new brain draft has {len(bundle['entries'])} entries and {len(bundle['relations'])} relations. It focuses on the harmonic trichotomy and two drift subclasses. The outward counterexample is a baseline independently found by w583; no separate counterexample lemma is submitted here. One scoped mathematical KEEP for L1 is recorded from w584; the rest are pending. Response-side author/referee model evidence is UNKNOWN.

Validation command: python -X utf8 -B ~/brain_workers/w582/build_packet.py
Measured result: {verification['rational_boundary_cases']} exact row/harmonic cases, {verification['exact_assertions']} rational assertions, zero failures; {verification['cpu_seconds']:.6f} CPU seconds, {verification['wall_seconds']:.6f} wall seconds for arithmetic. Draft field/license/relation/DAG checks passed. These finite checks support the arithmetic, not the infinite-path proofs. Before the guard, pointwise positivity could be mistaken for a uniform floor; CE1 gives q(0)=3/4 and inf q=0. The packet now requires the floor as a separate assumption. No measured improvement to live recall is claimed.

Apply: after the required independent KEEP and provenance gates, the validating coordinator may integrate ~/math-brain-inbox/w582/bundle_001.json under BUNDLE_SPEC.md. This worker did not run the integrator, change live code, or write any store. There is no live-code patch to apply.

Risk: confusing deterministic nonstationary CE1 with an iid counterexample, weakening strict ellipticity to no ellipticity in L2, dropping the uniform drift or variance floor, or mistaking a comparator placeholder/hash for a proof. The packet labels all these boundaries. Submitted, reviewed, ingested, and retrievable are separate states in SOURCE_STATUS.json.

NEXT: w584 audit L2/L3/L4 and CE1 with exact artifact hashes; obtain response-side served-model/login evidence, then have the validating coordinator integrate only scoped kept draft rows.
'''
    (ROOT / 'REPORT.md').write_text(report, encoding='utf-8')
    names = ['STATEMENT.md', 'ATTEMPT.md', 'CLAIMS.jsonl', 'PRIOR_ATTEMPTS.md', 'SOURCE_STATUS.json',
             'SOURCE_RECEIPTS.json', 'STORE_LOOKUP.json', 'VERIFICATION.json', 'REPORT.md', 'bundle_001.json']
    hashes = {name: sha(ROOT / name) for name in names}
    dump('ARTIFACT_HASHES.json', {'utc': STAMP, 'purpose': 'ordinary review file hashes, not store sealing', 'sha256': hashes})
    review = '''# w582 C0044 review packet

Scope: audit the five exact claims in CLAIMS.jsonl against their proofs in ATTEMPT.md. Parent C0044 is unproved in this packet; current openness UNKNOWN. L1 already has one scoped KEEP in w584/CLAIMS.jsonl. Please review L2 (irreducibility and spatial ergodicity), CE1 (nonstationary counterexample only), L3 (bounded stopping and variance floor), and L4 (uniform drift and summable Azuma tail).

Primary statement and assumptions: STATEMENT.md. Prior attempt correction: PRIOR_ATTEMPTS.md. Exact primary-source hash and comparator admission: SOURCE_RECEIPTS.json. Arithmetic and resource gate: VERIFICATION.json / COMPUTE_GATE.json. All hashes below bind bytes for review, not mathematical truth.

Author response-side served model: UNKNOWN. Requested gpt-6.1-sol and an acc2 allocation do not prove served identity. Please supply referee response-side served-model/login evidence if available. No full independent provenance gate is claimed.

Brain draft: ~/math-brain-inbox/w582/bundle_001.json; 6 entries, 7 relations; owner-own-work sources. It has not been integrated or shown retrievable. Do not promote the target question or the auxiliary floor assumption to a general theorem.

'''
    review += '\n'.join(f'- {name}: {digest}' for name, digest in hashes.items()) + '\n\nNEXT: audit the stated special cases, record any correction against these bytes, and integrate only after the required scoped KEEP/provenance gates.\n'
    (ROOT / 'REVIEW_PACKET.md').write_text(review, encoding='utf-8')
    print(json.dumps({'status': 'packet ready', 'claims': len(claims), 'bundle_entries': len(bundle['entries']),
                      'relations': len(bundle['relations']), 'verification': verification,
                      'submitted': str(destination), 'hook_proposal': str(HOOK),
                      'current_openness': 'UNKNOWN', 'ingested': False}, ensure_ascii=False))


if __name__ == '__main__':
    main()
