"""Arithmetic and special-function sanity checks for C001 v2; no simulation."""
import json
import math
from fractions import Fraction as F
from pathlib import Path


def main():
    C = 420
    a, b, h = F(4, 175), F(403, 21000), F(1, 21000)
    powers = {
        'long_failure': C*(F(125, 6668)-a/2)-3,
        'z_decay': C*b-F(5, 2),
        'higher_slack': C*(2*b-a)-F(13, 2),
        'drift_slack': C*(a-b-h)-F(3, 2),
        'output_decay': C*a,
        'horizon_power_at_boundary': C*h,
    }
    assert powers['long_failure'] == F(612, 8335)
    assert powers['z_decay'] == F(139, 25)
    assert powers['higher_slack'] == F(1, 50)
    assert powers['drift_slack'] == F(1, 50)
    assert powers['output_decay'] == F(48, 5)
    assert powers['horizon_power_at_boundary'] == F(1, 50)
    moment_checks = []
    for dimension in (1, 2, 10, 100, 10000):
        for exponent in (0.5, 1.5):
            exact_log_moment = (exponent/2*math.log(2/dimension)
                                +math.lgamma((dimension+exponent)/2)
                                -math.lgamma(dimension/2))
            curvature_bound = -exponent*(2-exponent)/(4*(dimension+2))
            assert exact_log_moment <= curvature_bound+1e-10
            moment_checks.append(dict(d=dimension, s=exponent,
                                      exact_log_moment=exact_log_moment,
                                      curvature_bound=curvature_bound))
    critical = 250+20*math.sqrt(66)
    assert 412.48 < critical < 412.481
    opt = []
    for candidate in (412, 413, 420):
        grid = max((candidate*s*(2-s)/40-9.5*s, s)
                   for s in (2*j/10000 for j in range(1, 10000)))
        opt.append(dict(C=candidate, grid_max=grid[0], s=grid[1]))
    assert opt[0]['grid_max'] < 3 < opt[1]['grid_max']
    result = dict(status='pass', powers={k:str(v) for k,v in powers.items()},
                  critical_constant=critical, moment_checks=moment_checks,
                  optimization_grid=opt)
    path = Path(__file__).resolve().parents[1]/'logs/v2_arithmetic_check.json'
    path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2),flush=True)


if __name__ == '__main__':
    main()
