"""C9 driver. modes: count T W | piece T W k0 k1 r_in out | trap T W r_end out"""
import sys, json
sys.path[:0] = ['.']
from c9_flow import *
import c9_cone
import os
U = F(os.environ.get('C9_U', '1/5000')); KAPPA = F(os.environ.get('C9_KAPPA', '1/10')); HMAX = float(os.environ.get('C9_HMAX', '2.0'))   # cone lemma checked at (1/5000, 1/10) and (1/20000, 1/100)

def kraw():
    # Krawczyk root box, cached (exact: interval endpoints as integers in units of 1/S, centre as rationals)
    import os
    if os.path.exists('kraw_cache.json'):
        d = json.load(open('kraw_cache.json'))
        return [I(a, b) for a, b in d['X']], [F(v) for v in d['xc']]
    xs = c9_cone.plateau_float()
    ok, Xstar, xc = c9_cone.krawczyk(xs, F(1, 10 ** 9)); assert ok
    json.dump({'X': [[v.lo, v.hi] for v in Xstar], 'xc': [str(v) for v in xc], 'note': 'Krawczyk OK on ETA, rho 1e-9'}, open('kraw_cache.json', 'w'))
    return Xstar, xc

def setup(T, W):
    Xstar, xc = kraw()
    xs = c9_cone.plateau_float()     # the same float input the cached reference was built from
    P, Pinv, par, w = c9_cone.adapted_frame(xs)
    p0 = [xc[i] + P[i][0] * U for i in range(N)]
    off = norm2_up(matvec(Pinv, [Xstar[i] - I.of(xc[i]) for i in range(N)]))
    r_face = up(off + KAPPA * U)
    import os
    cache = ('ref_T%s_W%s.json' % (T, W)) if U == F(1, 5000) else ('ref_T%s_W%s_U%s%s.json' % (T, W, str(U).replace('/', 'o'), '' if HMAX == 2.0 else '_h%s' % HMAX))
    if os.path.exists(cache):
        d = json.load(open(cache))
        tq = [F(v) for v in d['tq']]; nodes = [[F(v) for v in x] for x in d['nodes']]; slopes = [[F(v) for v in x] for x in d['slopes']]
        assert nodes[0] == p0
    else:
        tq, nodes, slopes = build(p0, float(T), float(W), hmax=HMAX)
        json.dump({'tq': [str(v) for v in tq], 'nodes': [[str(v) for v in x] for x in nodes],
                   'slopes': [[str(v) for v in x] for x in slopes]}, open(cache, 'w'))
    return P, Pinv, r_face, tq, nodes, slopes

def frame_at(nodes, k, P0, Pinv0):
    return (P0, Pinv0) if k == 0 else frame(fdrive.jac(fl(nodes[k]), ETA_F))

if __name__ == '__main__':
    from resource_limits import apply_limits; apply_limits()
    # a BelowNormal job on a saturated box is EcoQoS-throttled to ~0.1% of a core (measured 18 Oct); opt out, keep the priority
    import subprocess; subprocess.run([sys.executable, 'ecoqos_off.py', str(os.getpid())], capture_output=True)
    mode = sys.argv[1]
    P, Pinv, r_face, tq, nodes, slopes = setup(sys.argv[2], sys.argv[3])
    if mode == 'count':
        K = len(tq) - 1
        print('r_face', float(r_face), 'K', K)
        for k in range(0, K + 1, max(1, K // 15)):
            x = fl(nodes[k]); print(k, round(float(tq[k]), 2), np.round(x, 6), 'dist_teacher', np.linalg.norm(x - fl(TEACHER)))
    elif mode == 'piece':
        k0, k1 = int(sys.argv[4]), min(int(sys.argv[5]), len(tq) - 1)
        r_in = r_face if sys.argv[6] == 'face' else F(sys.argv[6])
        P0, Pinv0 = frame_at(nodes, k0, P, Pinv)
        run_chain(tq, nodes, slopes, P0, Pinv0, r_in, k0, k1, sys.argv[7], nsub=int(sys.argv[8]) if len(sys.argv) > 8 else 6)
    elif mode == 'bpiece':
        # block-wise tube; v_in 'face' = per-block offset of the root box plus kappa*U on every stable block
        import c9_blocks as CB
        k0, k1 = int(sys.argv[4]), min(int(sys.argv[5]), len(tq) - 1)
        if sys.argv[6] == 'face':
            Xstar, xc = kraw()
            zo = matvec(Pinv, [Xstar[i] - I.of(xc[i]) for i in range(N)])
            blocks = [[i] for i in range(N)]
            if os.environ.get('C9_FACE') == 'section':
                # section u_xc = U about the box centre: every cone solution crosses it while u_x* is within zo_0 of U,
                # so the u-error starts at exactly 0 and |s_xc| <= kappa (U + zo_0) + zo_i (cone lemma needed up to U + zo_0)
                z0 = F(zo[0].maxabs(), S)
                v_in = [F(0)] + [up(F(zo[i].maxabs(), S) + KAPPA * (U + z0)) for i in range(1, N)]
            else:
                v_in = [up(F(zo[i].maxabs(), S) + (0 if i == 0 else KAPPA * U)) for i in range(N)]
            P0, Pinv0 = P, Pinv
        else:
            d = json.loads(open(sys.argv[6]).readlines()[-1]); assert d['piece_done'][1] == k0
            v_in = [F(x) for x in d['v_out']]
            P0, Pinv0, blocks = CB.frame_b(fdrive.jac(fl(nodes[k0]), ETA_F)); assert blocks == d['blocks_out']
            assert 'P_sha' in d and CB.frame_sha(P0) == d['P_sha'], 'frame rebuilt at the piece boundary differs from the one v_out is measured in'
        CB.run_chain_b(tq, nodes, slopes, P0, Pinv0, blocks, v_in, k0, k1, sys.argv[7], nsub=int(sys.argv[8]) if len(sys.argv) > 8 else 6)
    elif mode == 'bresume':
        # continue a block tube from line k of an earlier bpiece log: v (radii at node k+1, in the frame of node k+1) taken
        # exactly from 'vx' when logged, else from the float rounded up by 2^-40 relative (float(x) >= x (1 - 2^-53))
        import c9_blocks as CB
        src, kk, out = sys.argv[4], int(sys.argv[5]), sys.argv[6]
        d = [json.loads(l) for l in open(src) if '"k": %d,' % kk in l][0]; assert d['k'] == kk and not d.get('fail')
        v_in = [F(x) for x in d['vx']] if 'vx' in d else [up(F(x) * (1 + F(1, 2 ** 40))) for x in d['v']]
        CB.run_chain_b.shift = F(d.get('shift', 0)) * (1 + F(1, 2 ** 40))
        P0, Pinv0, blocks = CB.frame_b(fdrive.jac(fl(nodes[kk + 1]), ETA_F))
        assert os.environ.get('C9_SRC_FLOW') == '1' or len(blocks) == len(v_in)
        if os.environ.get('C9_FLOWCOL') == '1' and os.environ.get('C9_SRC_FLOW') == '1':
            # the source log is itself a flow-frame piece: its v is already in the flow frame of node k+1. Rebuild that frame
            # at the logged DELTA (C9_SRC_DELTA) and at the current one; they must be the same exact matrix, so v carries over
            import c9_cluster
            d_now = c9_cluster.DELTA
            c9_cluster.DELTA = float(os.environ['C9_SRC_DELTA']); Pa, _, ba = CB.frame_b(fdrive.jac(fl(nodes[kk + 1]), ETA_F), nodes[kk + 1])
            c9_cluster.DELTA = d_now; Pb, Pinvb, bb = CB.frame_b(fdrive.jac(fl(nodes[kk + 1]), ETA_F), nodes[kk + 1])
            assert Pa == Pb and ba == bb and len(bb) == len(v_in), 'source and resumed flow frames differ at node k+1'
            P0, Pinv0, blocks = Pb, Pinvb, bb
        elif os.environ.get('C9_SRC_FLOW') == '1':
            # source is a flow-frame piece, this one runs in the plain clustered frame (all eigenvalues negative here, so no
            # reset is needed): carry v from the source's flow frame (C9_SRC_DELTA) into the plain frame (C9_DELTA) by switch()
            import c9_cluster
            d_now = c9_cluster.DELTA
            os.environ['C9_FLOWCOL'] = '1'; c9_cluster.DELTA = float(os.environ['C9_SRC_DELTA'])
            Ps, Pinvs, bs = CB.frame_b(fdrive.jac(fl(nodes[kk + 1]), ETA_F), nodes[kk + 1]); assert len(bs) == len(v_in)
            os.environ['C9_FLOWCOL'] = '0'; c9_cluster.DELTA = d_now
            P0, Pinv0, blocks = CB.frame_b(fdrive.jac(fl(nodes[kk + 1]), ETA_F))
            v_in = CB.switch(Pinv0, blocks, Ps, bs, v_in)
        elif os.environ.get('C9_FLOWCOL') == '1':
            # the source log measured v in the plain frame; carry it into the flow-adapted frame at the same node
            P1, Pinv1, b1 = CB.frame_b(fdrive.jac(fl(nodes[kk + 1]), ETA_F), nodes[kk + 1])
            v_in = CB.switch(Pinv1, b1, P0, blocks, v_in); P0, Pinv0, blocks = P1, Pinv1, b1
        k1 = min(int(sys.argv[7]), len(tq) - 1)
        print(json.dumps({'resume_from': src, 'k': kk, 'P_sha': CB.frame_sha(P0)}), flush=True)
        CB.run_chain_b(tq, nodes, slopes, P0, Pinv0, blocks, v_in, kk + 1, k1, out, nsub=int(sys.argv[8]) if len(sys.argv) > 8 else 6)
    elif mode == 'trap':
        # ball of radius rho about the exact teacher point in its eigenframe; residual is f(teacher), an exact zero
        r_end = F(sys.argv[4]); out = sys.argv[5]
        K = len(tq) - 1
        PK, PinvK = frame(fdrive.jac(fl(nodes[K]), ETA_F))
        if os.environ.get('C9_TRAP_FRAMEB') == '1':
            # the tube's radii live in the block frame it ended in (frame_b at node K under the run's env), not in frame()
            import c9_blocks as CB
            PK, PinvK, _bK = CB.frame_b(fdrive.jac(fl(nodes[K]), ETA_F))
        SWAP = [F(1), F(0), F(1), F(0), F(1), F(1), F(0)]       # teacher-swapped zero, exact for every eta
        TG = min((TEACHER, SWAP), key=lambda T: float(sum((nodes[K][i] - T[i]) ** 2 for i in range(N))))
        Pt, Pinvt = frame(fdrive.jac(fl(TG), ETA_F))
        off = norm2_up(matvec(Pinvt, [I.of(nodes[K][i] - TG[i]) for i in range(N)]))
        sw = opnorm2_up([[sum(Pinvt[i][l] * PK[l][j] for l in range(N)) for j in range(N)] for i in range(N)])
        need = up(off + sw * r_end)
        res = norm2_up(matvec(Pinvt, f_point(TG)))
        rec = {'frameb': os.environ.get('C9_TRAP_FRAMEB') == '1', 'target': [str(v) for v in TG], 'K': K, 't_end': float(tq[K]), 'r_end': str(r_end), 'offset': float(off), 'sw': float(sw), 'need_rho': float(need),
               'resid': float(res), 'cond_Pt': float(np.linalg.cond(np.array([[float(v) for v in row] for row in Pt])))}
        with open(out, 'w') as fh:
            for rho in [F(1, 10 ** 4), F(3, 2 * 10 ** 4), F(2, 10 ** 4), F(3, 10 ** 4), F(1, 10 ** 3), F(3, 10 ** 3), F(1, 10 ** 2)]:
                if rho <= need: continue
                for ns in (1, 2, 3):
                    worst = None
                    cells = [(-rho + 2 * rho * F(a, ns), -rho + 2 * rho * F(a + 1, ns)) for a in range(ns)]
                    import itertools
                    for cc in itertools.product(cells, repeat=N):
                        z = [iv(*c) for c in cc]
                        box = [I.of(TG[i]) + sum((I.of(Pt[i][k]) * z[k] for k in range(N)), I.of(0)) for i in range(N)]
                        mu = lognorm_up(mm_iv_rat(mm_rat_iv(Pinvt, jac_box(box)), Pt))
                        worst = mu if worst is None else max(worst, mu)
                    ok = worst < 0 and res < -worst * rho
                    rec['trap_%s_%d' % (float(rho), ns)] = {'mu': float(worst), 'ok': bool(ok)}
                    fh.write(json.dumps(rec) + '\n'); fh.flush()
                    if ok:
                        rec['PASS'] = {'rho': str(rho), 'nsplit': ns, 'mu': str(worst)}
                        fh.write(json.dumps(rec) + '\n'); print(json.dumps(rec)); sys.exit(0)
        print(json.dumps(rec))
