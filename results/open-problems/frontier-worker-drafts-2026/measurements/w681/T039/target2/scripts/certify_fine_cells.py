"""Fine positive-cell certificate with a squared Hilbert-Schmidt completion bound."""
from pathlib import Path
import hashlib
import math
import certify_positive_cells_graded as graded
import fine_tables
core=graded.core
ROOT=graded.ROOT
original_certify=core.certify
def load_tables(args):
    a, q, e, constants = fine_tables.load(args)
    base = core.base
    r = math.nextafter(args.table_rho_max, math.inf)
    d = base.sub_lo(1., base.mul_pos_hi(r, r))
    invd = base.div_pos_hi(1., d)
    alpha = base.div_pos_hi(r, base.sqrt_pos_lo(d))
    beta = base.mul_pos_hi(base.mul_pos_hi(2., r), invd)
    needed_a = base.mul_pos_hi(beta, base.mul_pos_hi(args.cutoff, args.cutoff))
    needed_q = base.mul_pos_hi(alpha, args.cutoff)
    def extend(table, needed, stage):
        if needed <= table.xmax:
            return table
        endpoint = float(base.up(needed))
        parameter = base.ball(table.xmax, endpoint)
        if stage == 'a':
            values = {'TPLUS': core.pos.midpoint_integral(parameter, args.v_panels, core.pos.positive_a_integrand),
                      'P': parameter * (-parameter).exp()}
        else:
            sqrtpi = core.arb.pi().sqrt()
            values = {'HPLUS': core.pos.midpoint_integral(parameter, args.v_panels, core.pos.positive_q_integrand),
                      'S': sqrtpi * (1 + 2 * parameter * parameter) * (parameter * parameter).exp() * parameter.erfc() - 2 * parameter}
        ranges = {}
        for name, value in values.items():
            lower, upper = base.bounds(value)
            ranges[name] = base.SparseRange.build(core.np.append(table.ranges[name].mins[0], max(0., lower)),
                                                 core.np.append(table.ranges[name].maxs[0], upper))
        return base.UniformTable(core.np.append(table.edges, endpoint), ranges)
    return extend(a, needed_a, 'a'), extend(q, needed_q, 'q'), e, constants
core.tables=load_tables

def certify(lo,hi,args,tabs):
    # Unique namespace preserves every earlier passing witness byte for byte.
    runroot=ROOT/'runs/fine_cells_v1';(runroot/'logs').mkdir(parents=True,exist_ok=True)
    original_root=core.ROOT
    try:
        core.ROOT=runroot
        row=original_certify(lo,hi,args,tabs)
    finally:core.ROOT=original_root
    row['witness_file']=str((runroot/row['witness_file']).relative_to(ROOT))
    row['triangle_operator_upper']=row['operator_upper']
    lam=core.base.ball(row['finite_operator_upper'],row['finite_operator_upper'])
    tau=core.base.ball(row['outside_hs_squared_upper'],row['outside_hs_squared_upper'])
    row['operator_upper']=core.base.bounds((lam*lam+tau).sqrt())[1]
    row['pass']=row['operator_upper']<2.
    row['tail_composition']='sqrt(finite_operator_upper^2 + entire_outside_HS_squared_upper)'
    row['fine_implementation_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return row
core.certify=certify
if __name__=='__main__':raise SystemExit(core.main())
