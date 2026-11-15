"""Small arithmetic checks of C001/C002; no training simulation or big arrays."""
import json
import math
from decimal import Decimal, localcontext
from pathlib import Path


def main():
    rows = []
    for depth in (10**6, 10**8, 10**12):
        width = math.floor(depth / (10000 * math.log(depth)))
        q = depth / width
        a, b = 1 / 200, 3 / 1000
        log_z = 3 * math.log(depth) - b * q
        log_higher_ratio = math.log(2) + 8 * math.log(depth) - (2*b-a)*q
        log_drift_ratio_without_G = 2 * math.log(depth) - q / 1000
        assert q >= 10000 * math.log(depth)
        assert log_z <= -27 * math.log(depth) + 1e-9
        assert log_higher_ratio <= 0
        assert log_drift_ratio_without_G <= -8 * math.log(depth) + 1e-9
        boundary_width = math.floor(depth / math.log(depth))
        boundary_q = depth / boundary_width
        delta = math.exp(-b * boundary_q)
        log_rho = -10 * a / boundary_width
        log_product = depth * math.log1p(math.expm1(log_rho) + delta)
        assert -math.expm1(log_rho) <= delta / 2
        assert log_product >= depth * delta / 4
        with localcontext() as ctx:
            ctx.prec = 60
            dd = Decimal(depth)
            dq = dd / Decimal(boundary_width)
            drho = (-Decimal('0.05') / Decimal(boundary_width)).exp()
            ddelta = (-Decimal('0.003') * dq).exp()
            independent_log_product = dd * (drho + ddelta).ln()
        rel_error = abs(log_product - float(independent_log_product)) / log_product
        assert rel_error < 1e-12
        rows.append(dict(L=depth, m_narrowed=width, q=q,
                         log_z=log_z, log_higher_ratio=log_higher_ratio,
                         log_drift_ratio_without_G=log_drift_ratio_without_G,
                         m_boundary=boundary_width,
                         boundary_log_product=log_product,
                         boundary_decimal_relative_error=rel_error))
    out = Path(__file__).resolve().parents[1] / 'logs' / 'arithmetic_check.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(dict(status='pass', rows=rows), indent=2)+'\n', encoding='utf-8')
    print(out.read_text(encoding='utf-8'), flush=True)


if __name__ == '__main__':
    main()
