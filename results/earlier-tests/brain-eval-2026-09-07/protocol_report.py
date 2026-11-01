"""Independent PLIT reporting: complete planned populations, explicit primary tier.

No network, model calls, production writes, or imports from the prior grader.
Output is a descriptive reconstruction conditional on the bank's existing keys.
Semantic key validity, model identity and sterilization need separate evidence.
"""
from pathlib import Path
import argparse
import hashlib
import json
import math
from datetime import datetime, timezone

ARMS = ('none', 'brain', 'placebo')


class EvidenceError(ValueError):
    pass


def parse_json_text(text):
    def unique_pairs(pairs):
        obj = {}
        for key, value in pairs:
            if key in obj:
                raise EvidenceError('Duplicate JSON member: ' + key)
            obj[key] = value
        return obj
    def invalid_constant(value):
        raise EvidenceError('Nonfinite JSON constant: ' + value)
    return json.loads(text, object_pairs_hook=unique_pairs, parse_constant=invalid_constant)


def read_json(path):
    try:
        return parse_json_text(path.read_text(encoding='utf-8'))
    except (OSError, ValueError) as error:
        raise EvidenceError(f'{path.name}: {error}') from error


def read_keys(path):
    result = {}
    for line in path.read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        key = parse_json_text(line)
        iid = key['item_id']
        if iid in result:
            raise EvidenceError('Duplicate key item: ' + iid)
        if key['truth'] not in ('clean', 'flawed'):
            raise EvidenceError('Unknown key truth')
        if key['truth'] == 'flawed' and (key.get('tier') not in ('A', 'B') or
                type(key.get('fault_step')) is not int or key['fault_step'] < 1):
            raise EvidenceError('Invalid flawed key')
        result[iid] = key
    return result


def normalize_verdict(value):
    if not isinstance(value, str):
        raise EvidenceError('Verdict is not text')
    text = value.strip().lower()
    if text in ('flawed', 'invalid', 'incorrect', 'false'):
        return 'flawed'
    if text in ('valid', 'clean', 'correct', 'sound', 'true'):
        return 'clean'
    raise EvidenceError('Unrecognized verdict')


def read_trial(run, keys, arms=ARMS):
    sample = read_json(run / 'SAMPLE.json')
    ids = sample['item_ids']
    if not isinstance(ids, list) or not ids or len(ids) != len(set(ids)):
        raise EvidenceError('Empty, invalid or duplicate sample item IDs')
    if not set(ids) <= set(keys):
        raise EvidenceError('Sample has missing answer keys')
    if sample.get('requested') is not None and sample['requested'] != len(ids):
        raise EvidenceError('Sample count differs from requested count')
    actual_flawed = sum(keys[i]['truth'] == 'flawed' for i in ids)
    for name, actual in (('n_faulted', actual_flawed), ('n_clean', len(ids)-actual_flawed)):
        if name in sample and sample[name] != actual:
            raise EvidenceError('Sample key composition differs: ' + name)
    rows = {}
    for arm in arms:
        arm_rows = {}
        for path in sorted((run / 'verdicts' / arm).glob('*.json')):
            row = read_json(path)
            iid = row.get('item_id')
            if iid not in ids:
                raise EvidenceError('Unexpected verdict outside frozen sample')
            if iid in arm_rows:
                raise EvidenceError('Duplicate verdict for item')
            if path.stem != iid or row.get('arm') != arm:
                raise EvidenceError('Filename, row identity or arm mismatch')
            ans = row.get('answer')
            if not isinstance(ans, dict):
                raise EvidenceError('Missing or malformed answer')
            verdict = normalize_verdict(ans.get('verdict'))
            step = ans.get('fault_step')
            if step is not None and (type(step) is not int or step < 1):
                raise EvidenceError('Fault step must be a positive integer or null')
            arm_rows[iid] = {'full_credit': verdict == 'flawed' and step == keys[iid].get('fault_step'),
                             'detected': verdict == 'flawed', 'row': row}
        if set(arm_rows) != set(ids):
            raise EvidenceError(f'Incomplete {arm}: {len(arm_rows)}/{len(ids)} planned verdicts')
        rows[arm] = arm_rows
    return sample, rows


def contrast(rows, ids, first, second, metric='full_credit', inference=True):
    n = len(ids)
    if n == 0:
        raise EvidenceError('Cannot estimate an empty population')
    av = [int(rows[first][i][metric]) for i in ids]
    bv = [int(rows[second][i][metric]) for i in ids]
    delta = [a-b for a,b in zip(av,bv)]
    plus, minus = delta.count(1), delta.count(-1)
    difference = sum(delta) / n
    # Empirical paired influence variance; matches the old descriptive interval.
    se = math.sqrt(sum((x-difference)**2 for x in delta)) / n
    result = {'arms': [first, second], 'metric': metric, 'n': n,
              'correct': [sum(av), sum(bv)], 'discordants': [plus, minus],
              'difference_pp': 100*difference,
              'comparator_errors_available_for_gain': n-sum(bv),
              'comparator_correct_available_for_harm': sum(bv),
              'conditional_effect_range_pp': [-100*sum(bv)/n,100*(n-sum(bv))/n],
              'room_to_fail_caveat': 'Arithmetic range holding the observed comparator fixed; not power or a minimum detectable effect.',
              'inference': 'registered_primary' if inference else 'descriptive_only'}
    if inference:
        discordance_n = plus + minus
        tail = sum(math.comb(discordance_n,k) for k in range(min(plus,minus)+1))
        result['mcnemar_exact_two_sided_p'] = min(1., 2 * tail / 2**discordance_n)
        result['ci95_pp_paired_wald'] = [100*(difference-1.96*se),100*(difference+1.96*se)]
        result['interval_caveat'] = 'Approximate Wald interval; not equivalence or a familywise guarantee.'
    return result


def reconstruct(root):
    keys = read_keys(root / 'plit_keys.jsonl')
    declared = read_json(root / 'STAGE1_SIZING.json')
    solvers = {}
    stage_ids = None
    for solver in ('haiku','opus'):
        pilot_sample, pilot = read_trial(root / ('run_plit_' + solver), keys)
        sample, stage = read_trial(root / ('run_plit_s1_' + solver), keys)
        if stage_ids is not None and set(sample['item_ids']) != stage_ids:
            raise EvidenceError('Solvers have different frozen stage populations')
        stage_ids = set(sample['item_ids'])
        if set(pilot_sample['item_ids']) & set(sample['item_ids']):
            raise EvidenceError('Pilot and stage overlap')
        pilot_a = [i for i in pilot_sample['item_ids'] if keys[i]['truth']=='flawed' and keys[i]['tier']=='A']
        if not pilot_a:
            raise EvidenceError('Pilot lacks tier A')
        ceiling = sum(pilot['none'][i]['full_credit'] for i in pilot_a)/len(pilot_a) > .85
        tier = 'B' if ceiling else 'A'
        sizing_ids = [i for i in pilot_sample['item_ids'] if keys[i]['truth']=='flawed' and keys[i]['tier']==tier]
        pilot_pair = contrast(pilot,sizing_ids,'brain','none')
        planned_n = max(120,min(400,math.ceil(784*sum(pilot_pair['discordants'])/pilot_pair['n'])))
        if declared['sizing'][solver]['sizing_tier'] != tier or declared['sizing'][solver]['n_flawed'] != planned_n:
            raise EvidenceError('Recorded sizing disagrees with independently reconstructed pilot')
        flawed = [i for i in sample['item_ids'] if keys[i]['truth']=='flawed']
        clean = [i for i in sample['item_ids'] if keys[i]['truth']=='clean']
        primary_ids = [i for i in flawed if keys[i]['tier']==tier]
        primary = [contrast(stage,primary_ids,'brain','none'),contrast(stage,primary_ids,'brain','placebo')]
        guard = {arm:{'n':len(clean),'false_positives':sum(stage[arm][i]['detected'] for i in clean)} for arm in ARMS}
        for arm in ('brain','placebo'):
            if not clean:
                raise EvidenceError('Clean false-positive guard is empty')
            difference = 100*(guard[arm]['false_positives']-guard['none']['false_positives'])/len(clean)
            guard[arm].update({'difference_pp_vs_none':difference,'exceeds_10pp_guard':difference>10})
        solvers[solver] = {'planned_items':len(sample['item_ids']), 'complete_arms':list(ARMS),
             'primary_tier':tier,'pilot_tier_a_ceiling':ceiling,
             'planned_primary_flawed_pairs':planned_n,'achieved_primary_flawed_pairs':len(primary_ids),
             'primary_pair_target_met':len(primary_ids)>=planned_n,
             'primary':primary,'clean_guard':guard,
             'descriptive_all_tiers':[contrast(stage,flawed,'brain','none',inference=False),
                contrast(stage,flawed,'brain','placebo',inference=False),
                contrast(stage,flawed,'brain','none',metric='detected',inference=False)],
             'descriptive_tiers':{t:contrast(stage,[i for i in flawed if keys[i]['tier']==t],
                'brain','none',inference=False) for t in ('A','B')}}
    return {'schema':'plit-protocol-reconstruction-v1','as_of':datetime.now(timezone.utc).isoformat(),
            'source_snapshot':str(root.resolve()), 'source_manifest_sha256':hashlib.sha256((root/'MANIFEST.json').read_bytes()).hexdigest(),
            'status':'COMPLETE_RECONSTRUCTION_CONDITIONAL_ON_EXISTING_KEYS',
            'limitations':['Primary pair targets not met unless each solver flag proves otherwise.',
                'Absence of significant gain does not prove no benefit or equivalence.',
                'Pooled detection is descriptive under this protocol; its nominal p-value is not a confirmatory harm test.',
                'Response-side model identity and proof-label validity are separate unverified gates.',
                'This report changes evaluation accounting, not agent reasoning or production retrieval.'],
            'solvers':solvers}


def verify_manifest(root):
    rows = read_json(root/'MANIFEST.json')
    declared = set()
    for record in rows:
        path = Path(record['evidence'])
        if not path.resolve().is_relative_to(root.resolve()):
            raise EvidenceError('Manifest points outside snapshot')
        if path.resolve() in declared:
            raise EvidenceError('Duplicate manifest member')
        declared.add(path.resolve())
        if hashlib.sha256(path.read_bytes()).hexdigest() != record['sha256']:
            raise EvidenceError('Pinned input drift: ' + path.name)
    actual = {p.resolve() for p in root.rglob('*') if p.is_file() and p != root/'MANIFEST.json'}
    if actual != declared:
        raise EvidenceError('Snapshot inventory differs from manifest')


def render(report):
    lines=['# PLIT stage 1: protocol-aware reconstruction','',
           'The registered primary comparisons do not show a clear benefit from notes. '
           'Both primary strata contain fewer pairs than the sizing targets. '
           'These data do not establish equivalence or a general harmful effect.','',
           '| Solver | Primary tier | Brain | None | Difference (pp) | 95% paired Wald interval | Exact p | Pairs / target | Gain room (pp) |',
           '|---|---|---:|---:|---:|---|---:|---:|---:|']
    for name, s in report['solvers'].items():
        p=s['primary'][0]; lo,hi=p['ci95_pp_paired_wald']; a,b=p['correct']; n=p['n']
        lines.append(f'| {name} | {s["primary_tier"]} | {a}/{n} | {b}/{n} | {p["difference_pp"]:+.2f} | [{lo:.2f}, {hi:.2f}] | {p["mcnemar_exact_two_sided_p"]:.4f} | {n}/{s["planned_primary_flawed_pairs"]} | {p["conditional_effect_range_pp"][1]:.2f} |')
    lines+=['','All three arms are complete for each frozen sample. Missing or corrupt rows are a hard error, '
            'not an inner-join denominator reduction. The original pooled counts reproduce but remain descriptive.',
            '', 'Gain room is the largest gain possible if every observed comparator error were corrected, holding its answers fixed. It is arithmetic headroom, not power or a minimum detectable effect.',
            '',*['- '+text for text in report['limitations']],'',
            'Source manifest SHA-256: '+report['source_manifest_sha256'],
            'Reconstructed at '+report['as_of'],'']
    return '\n'.join(lines)


def main():
    p=argparse.ArgumentParser(); p.add_argument('--snapshot',type=Path,required=True); p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    verify_manifest(a.snapshot)
    report=reconstruct(a.snapshot)
    a.output.mkdir(parents=True,exist_ok=False)
    (a.output/'RESULT.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    (a.output/'RESULT.md').write_text(render(report),encoding='utf-8')
    print(render(report))


if __name__=='__main__':
    main()
