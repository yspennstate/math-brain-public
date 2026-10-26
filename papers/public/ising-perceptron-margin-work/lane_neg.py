"""Negative-side lane: per-slab certification past the rectangle
lambda wall.

The strip's negative edge at kappa ~ -0.946 is a wall of the
RECTANGLE method: the local-concavity enclosure over a slab's full
(q, psi) rectangle crosses zero there while the pointwise lambda(z)
stays negative until kappa ~ -1.3.  This driver mirrors the positive
Nakajima lane's move with the roles inverted.  Per slab, over
N_SUB = 8 kappa sub-balls:

  fp rectangle   located q at both alpha endpoints (mean-value
                 Picard, depth N_LOC), hull +- DELTA, endpoint
                 inwardness and the contraction product on the thin
                 rectangle -- rect_strip's one_piece, reused;
  amp / lambda   evaluated on the LOCATED (q, psi) boxes hulled over
                 the two alpha endpoints, not the slab rectangle:
                 the located width ~1e-6 collapses the enclosure to
                 near the point value;
  crossing       certified G signs at both alpha endpoints on the
                 sub-ball's located boxes (G > 0 at alpha_lb,
                 G < 0 at alpha_ub) -- each sub-ball carries its own
                 crossing, so the clause holds for every kappa in
                 the slab.

Appends one JSON line per slab to --out (checkpointed; rerun skips
completed slabs).  Every enclosure is serialized; want-direction is
recorded per check.

Run: python lane_neg.py slabs.json [--out results/lane_neg.jsonl]
         [--start I] [--end J] [--delta 5e-4] [--nloc 4000]
"""
import argparse
import json
import os

import certify_km_slab as C
from core import dec, hull, iv, endpoints
from locate_alpha import locate_deep_n

N_SUB = 8


def sub_balls(klo, khi):
    lo = dec(klo)
    hi = dec(khi)
    w = (hi - lo) / N_SUB
    out = []
    for i in range(N_SUB):
        a = lo + w * i
        b = lo + w * (i + 1)
        out.append(iv(a, b))
    return out


def one_slab(slab, delta, n_loc, n_eval):
    alo = dec(slab['alpha_lb'])
    ahi = dec(slab['alpha_ub'])
    q_seed = iv(dec(slab['q_lb']), dec(slab['q_ub']))
    checks = []
    ok_all = True

    def chk(name, ball, want):
        lo, hi = endpoints(ball)
        good = (float(lo) > 0) if want == '>0' else (float(hi) < 0)
        checks.append(dict(name=name, want=want, lo=str(lo), hi=str(hi),
                           ok=bool(good)))
        return good

    for i, kb in enumerate(sub_balls(slab['kappa_lo'], slab['kappa_hi'])):
        la = locate_deep_n(alo, kb, q_seed, n_loc)
        lb = locate_deep_n(ahi, kb, q_seed, n_loc)
        if la is None or lb is None:
            checks.append(dict(name='locate[%d]' % i, want='>0',
                               lo='-1', hi='-1', ok=False))
            ok_all = False
            continue
        qa, pa = la
        qb_, pb_ = lb
        # fp rectangle clause on the thin located rectangle
        ql1, qh1 = endpoints(qa)
        ql2, qh2 = endpoints(qb_)
        qlo = min(ql1, ql2) - dec(str(delta))
        qhi = max(qh1, qh2) + dec(str(delta))
        for aname, av in (('lb', alo), ('ub', ahi)):
            v_lo = C.P_of(C.R_of(qlo, av, kb)) - qlo
            v_hi = qhi - C.P_of(C.R_of(qhi, av, kb))
            ok_all &= chk('inward %s lo[%d]' % (aname, i), v_lo, '>0')
            ok_all &= chk('inward %s hi[%d]' % (aname, i), v_hi, '>0')
        qbox = iv(qlo, qhi)
        Ra = C.R_of_wide(qbox, alo, kb)
        Rb = C.R_of_wide(qbox, ahi, kb)
        plo_ = min(endpoints(Ra)[0], endpoints(Rb)[0])
        phi_ = max(endpoints(Ra)[1], endpoints(Rb)[1])
        contr = C.Pprime_bound(plo_, phi_) * C.dRdq_bound(qbox, ahi, kb)
        ok_all &= chk('1 - contraction[%d]' % i, 1 - contr, '>0')
        # amp and lambda on the located boxes (hull over endpoints)
        qloc = hull(qa, qb_)
        ploc = hull(pa, pb_)
        amp = C.cond_amp_works_cert(ahi, qloc, ploc, kb, n=n_eval)
        ok_all &= chk('1 - amp-works[%d]' % i, 1 - amp, '>0')
        lam = C.cond_local_concavity_cert(ahi, qloc, ploc, kb, n=n_eval)
        ok_all &= chk('lambda(z_hat)[%d]' % i, lam, '<0')
        # crossing: certified G signs at both alpha endpoints
        Ga = C.G_mean_value_deep(alo, qa, pa, kb, n=n_eval)
        Gb = C.G_mean_value_deep(ahi, qb_, pb_, kb, n=n_eval)
        ok_all &= chk('G(alpha_lb)[%d]' % i, Ga, '>0')
        ok_all &= chk('G(alpha_ub)[%d]' % i, Gb, '<0')
    return ok_all, checks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('slabs')
    ap.add_argument('--out', default='results/lane_neg.jsonl')
    ap.add_argument('--start', type=int, default=0)
    ap.add_argument('--end', type=int, default=0)
    ap.add_argument('--delta', type=float, default=5e-4)
    ap.add_argument('--nloc', type=int, default=4000)
    ap.add_argument('--neval', type=int, default=8000)
    args = ap.parse_args()
    slabs = json.load(open(args.slabs))
    end = args.end or len(slabs)
    done = set()
    if os.path.exists(args.out):
        for line in open(args.out):
            try:
                done.add(json.loads(line)['kappa_lo'])
            except Exception:
                pass
    n_ok = n_bad = 0
    with open(args.out, 'a', encoding='utf-8', newline='\n') as fh:
        for idx in range(args.start, end):
            s = slabs[idx]
            if s['kappa_lo'] in done:
                continue
            ok, checks = one_slab(s, args.delta, args.nloc, args.neval)
            rec = dict(kappa_lo=s['kappa_lo'], kappa_hi=s['kappa_hi'],
                       alpha_lb=s['alpha_lb'], alpha_ub=s['alpha_ub'],
                       q_lb=s['q_lb'], q_ub=s['q_ub'],
                       n_sub=N_SUB, delta=args.delta, n_loc=args.nloc,
                       ok=bool(ok), checks=checks)
            fh.write(json.dumps(rec) + '\n')
            fh.flush()
            n_ok += 1 if ok else 0
            n_bad += 0 if ok else 1
            print('%s slab [%s, %s]' % ('OK  ' if ok else 'FAIL',
                                        s['kappa_lo'], s['kappa_hi']),
                  flush=True)
    print('DONE %d ok, %d fail -> %s' % (n_ok, n_bad, args.out))


if __name__ == '__main__':
    main()
