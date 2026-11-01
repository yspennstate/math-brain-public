"""Collect slab-certificate results into one table.

Reads result_*.json files (from run_batch.sh workers or local runs),
checks every slab passed together with its global section, and writes
results/certified_intervals.csv: one row per kappa slab with the
certified alpha_*(kappa) interval and the located fixed-point boxes.

Run:  python collect_slabs.py result_pos_*.json -o results/certified_intervals.csv
"""

import argparse
import csv
import glob
import io
import json
import os
import sys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('patterns', nargs='+')
    ap.add_argument('-o', '--out', default='results/certified_intervals.csv')
    ap.add_argument('--expect', default=None,
                    help='slab schedule JSON the results must cover '
                         'one-to-one; binds count, range, and every '
                         'full slab record, and records schedule and '
                         'source sha256s in a provenance sidecar.')
    ap.add_argument('--unsafe-unbound', action='store_true',
                    help='run without an expected schedule; the '
                         'collection then validates whatever files '
                         'matched the glob and a missing shard '
                         'shrinks the strip silently.  Never for a '
                         'certified release.')
    args = ap.parse_args()
    if not args.expect and not args.unsafe_unbound:
        ap.error('--expect <schedule.json> is required '
                 '(or pass --unsafe-unbound explicitly)')

    files = []
    for p in args.patterns:
        files += glob.glob(p)
    if not files:
        print('no result files matched', file=sys.stderr)
        raise SystemExit(2)

    rows = []
    n_fail = 0
    n_globals = 0
    globals_ok = True
    for f in sorted(files):
        with open(f) as fh:
            recs = json.load(fh)
        for rec in recs:
            if 'global' in rec:
                n_globals += 1
                if not rec['global']['ok']:
                    globals_ok = False
                    print(f"{f}: GLOBAL FAIL", file=sys.stderr)
                continue
            s = rec['slab']
            if not rec['ok']:
                n_fail += 1
                bad = [c['name'] for c in rec['checks'] if not c['ok']]
                print(f"{f}: slab [{s['kappa_lo']}, {s['kappa_hi']}] "
                      f"FAIL: {bad}", file=sys.stderr)
                continue
            rows.append({
                'kappa_lo': s['kappa_lo'],
                'kappa_hi': s['kappa_hi'],
                'alpha_lb': s['alpha_lb'],
                'alpha_ub': s['alpha_ub'],
                'q_lb': s['q_lb'],
                'q_ub': s['q_ub'],
                'source': f,
                '_full': s,
            })
    rows.sort(key=lambda r: float(r['kappa_lo']))

    # continuity of the certified strip: consecutive slabs must share
    # their kappa boundary or the union is not an interval
    gaps = []
    for a, b in zip(rows[:-1], rows[1:]):
        if a['kappa_hi'] != b['kappa_lo']:
            gaps.append((a['kappa_hi'], b['kappa_lo']))

    lo = rows[0]['kappa_lo'] if rows else '-'
    hi = rows[-1]['kappa_hi'] if rows else '-'
    print(f"{len(rows)} slabs certified, {n_fail} failed; "
          f"{n_globals} global record(s), "
          f"{'ok' if globals_ok else 'FAILED'}; "
          f"kappa strip [{lo}, {hi}]"
          + (f"; GAPS: {gaps}" if gaps else "; contiguous"))

    # expected-schedule binding: without it the collection validates
    # whatever files matched the glob, so a missing shard shrinks the
    # strip silently and still exits green.  All validation happens
    # BEFORE anything is written, so a failed run cannot destroy the
    # last good artifact.
    SLAB_KEYS = ('kappa_lo', 'kappa_hi', 'alpha_lb', 'alpha_ub',
                 'q_lb', 'q_ub', 'psi_lb', 'psi_ub')
    schedule_bad = False
    prov = None
    if args.expect:
        import hashlib
        raw = open(args.expect, 'rb').read()
        sched_sha = hashlib.sha256(raw).hexdigest()
        sched = json.loads(raw)
        # exact full-record equality: every schedule slab must appear
        # exactly once with ALL its rectangle fields unchanged, not
        # just its kappa boundaries
        want = [tuple(s[k] for k in SLAB_KEYS) for s in sched]
        got = [tuple(r['_full'][k] for k in SLAB_KEYS) for r in rows]
        missing = sorted(set(want) - set(got))
        extra = sorted(set(got) - set(want))
        dups = len(got) - len(set(got))
        if missing or extra or dups or len(got) != len(want):
            schedule_bad = True
            print(f"SCHEDULE MISMATCH vs {args.expect}: "
                  f"want {len(want)} got {len(got)}, "
                  f"{len(missing)} missing, {len(extra)} extra, "
                  f"{dups} duplicated"
                  + (f"; first missing kappa {missing[0][:2]}"
                     if missing else ''),
                  file=sys.stderr)
        else:
            print(f"schedule bound: {len(want)}/{len(want)} slabs "
                  f"one-to-one on all {len(SLAB_KEYS)} rectangle "
                  f"fields vs {args.expect} (sha256 {sched_sha[:16]})")
        src_shas = {}
        for f in sorted({r['source'] for r in rows}):
            src_shas[f] = hashlib.sha256(open(f, 'rb').read()).hexdigest()
        prov = {
            'schedule': args.expect,
            'schedule_sha256': sched_sha,
            'slabs_expected': len(want),
            'slabs_certified': len(got),
            'kappa_lo': lo, 'kappa_hi': hi,
            'sources_sha256': src_shas,
            'bound': not schedule_bad,
        }
    else:
        print("WARNING: no --expect schedule; range/count/completeness "
              "are unproven (a missing shard would pass)", file=sys.stderr)

    if n_fail or not globals_ok or n_globals == 0 or gaps or schedule_bad:
        print("validation FAILED; nothing written", file=sys.stderr)
        raise SystemExit(1)

    # pair-transactional publication: the CSV is built in memory, its
    # sha256 goes into the sidecar together with the collector's own
    # source sha and command line, both files land via tmp+rename, and
    # the sidecar's output_csv_sha256 lets a consumer detect a torn
    # pair (a crash between the two renames) instead of trusting it
    import hashlib
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=[k for k in rows[0]
                                        if k != '_full'],
                       lineterminator='\n')
    w.writeheader()
    w.writerows([{k: v for k, v in r.items() if k != '_full'}
                 for r in rows])
    csv_bytes = buf.getvalue().encode()
    if prov is not None:
        prov['output_csv'] = args.out
        prov['output_csv_sha256'] = hashlib.sha256(csv_bytes).hexdigest()
        prov['collector_sha256'] = hashlib.sha256(
            open(os.path.abspath(__file__), 'rb').read()).hexdigest()
        prov['command'] = sys.argv
        prov['verify'] = ('recompute sha256 of output_csv and compare '
                          'to output_csv_sha256; a mismatch means a '
                          'torn or superseded pair')
    tmp = args.out + '.tmp'
    with open(tmp, 'wb') as fh:
        fh.write(csv_bytes)
    if prov is not None:
        ptmp = args.out + '.provenance.json.tmp'
        with open(ptmp, 'w') as fh:
            json.dump(prov, fh, indent=1)
        os.replace(tmp, args.out)
        os.replace(ptmp, args.out + '.provenance.json')
        print(f"wrote {args.out} and its provenance sidecar "
              f"(csv sha {prov['output_csv_sha256'][:16]})")
    else:
        os.replace(tmp, args.out)
        print(f"wrote {args.out} (UNBOUND, no sidecar)")


if __name__ == '__main__':
    main()
