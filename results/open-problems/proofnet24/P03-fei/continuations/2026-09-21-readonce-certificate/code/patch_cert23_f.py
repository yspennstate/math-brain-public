"""patch: memory-bounded adaptive driver - cells are processed depth-first in batches; a batch whose failing set grows past
CAP cells is split into pieces that are pushed on a stack, so the live cell population never exceeds about 2*CAP"""
p = "fei_cert23.py"; s = open(p, encoding="utf-8", newline="").read()
start = s.index("def _adaptive(bound_fn, x0, x1, y0, y1, max_depth, name, chunk=1000000):")
end = s.index("def phi1_lower(cert, X, Y):")
new = '''def _adaptive(bound_fn, x0, x1, y0, y1, max_depth, name, chunk=1000000, cap=4000000, batch=2000000):
    """bound_fn returns (lower bound, width attributable to x, width attributable to y); a failing cell is split in two
    along the axis with the larger attributed width.  Memory-bounded: the initial cells are processed in batches of
    `batch`, each refined depth-first; whenever a level's failing set exceeds `cap` cells it is cut into pieces that
    are queued separately, so at most about 2*cap cells are alive at any time."""
    t0 = time.time(); n_init = len(x0)
    stack = [(x0[i:i + batch], x1[i:i + batch], y0[i:i + batch], y1[i:i + batch], 0) for i in range(0, n_init, batch)][::-1]
    total_cells = 0; max_depth_seen = 0; worst_final = np.inf; batches_done = 0
    while stack:
        cx0, cx1, cy0, cy1, depth = stack.pop()
        while True:
            lo = np.empty(len(cx0)); wx = np.empty(len(cx0)); wy = np.empty(len(cx0))
            for s in range(0, len(cx0), chunk):
                e = min(len(cx0), s + chunk)
                lo[s:e], wx[s:e], wy[s:e] = bound_fn(Iv(cx0[s:e], cx1[s:e]), Iv(cy0[s:e], cy1[s:e]))
            total_cells += len(cx0); max_depth_seen = max(max_depth_seen, depth)
            bad = lo < 0; nb = int(bad.sum())
            if nb == 0:
                break
            if depth == max_depth:
                j = int(np.argmin(lo)); worst_final = min(worst_final, float(lo[j]))
                print("  %s FAILED at max depth %d: cell [%.6f, %.6f] x [%.6f, %.6f] bound %.3e" % (name, depth, cx0[j], cx1[j], cy0[j], cy1[j], lo[j]), flush=True)
                return False
            bx0, bx1, by0, by1 = cx0[bad], cx1[bad], cy0[bad], cy1[bad]
            sx = wx[bad] >= wy[bad]
            xm = (bx0 + bx1) / 2; ym = (by0 + by1) / 2
            nx0 = np.concatenate([bx0[sx], xm[sx], bx0[~sx], bx0[~sx]]); nx1 = np.concatenate([xm[sx], bx1[sx], bx1[~sx], bx1[~sx]])
            ny0 = np.concatenate([by0[sx], by0[sx], by0[~sx], ym[~sx]]); ny1 = np.concatenate([by1[sx], by1[sx], ym[~sx], by1[~sx]])
            depth += 1
            if len(nx0) > cap:
                # queue the pieces and continue with the first one
                pieces = [(nx0[i:i + cap], nx1[i:i + cap], ny0[i:i + cap], ny1[i:i + cap], depth) for i in range(0, len(nx0), cap)]
                stack.extend(pieces[1:][::-1])
                cx0, cx1, cy0, cy1, depth = pieces[0]
            else:
                cx0, cx1, cy0, cy1 = nx0, nx1, ny0, ny1
        batches_done += 1
        if batches_done % 5 == 0 or not stack:
            print("  %s: %d batches done, %d queued, %d cells evaluated so far, deepest level %d  (%.0f s)" % (name, batches_done, len(stack), total_cells, max_depth_seen, time.time() - t0), flush=True)
    print("  %s VERIFIED: %d initial cells, %d cells evaluated, deepest level %d  (%.0f s)" % (name, n_init, total_cells, max_depth_seen, time.time() - t0), flush=True)
    return True

'''
s = s[:start] + new + s[end:]
open(p, "w", encoding="utf-8", newline="").write(s)
import py_compile; py_compile.compile(p, doraise=True); print("memory-bounded driver installed, compiles")
