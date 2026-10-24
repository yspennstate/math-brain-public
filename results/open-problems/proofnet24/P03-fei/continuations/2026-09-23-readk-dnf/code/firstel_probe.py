import numpy as np, sys
sys.argv = ['x', '1']
import importlib
import firstel
for eps in (1e-2, 1e-4, 1e-6, 1e-9, 1e-12, 1e-15):
    r = firstel.analyse(np.array([3.0, 2.0, 1.0]), 1.9, np.array([0.0, 1 - 2 * eps, 0.0]))
    print(f"eps={eps:.0e}: Bd/J {r['ratio']:6.2f}  LHS/J {r['lhs']:5.2f}  T1 {r['T1']:6.2f} T2 {r['T2']:6.2f} T3 {r['T3']:6.2f}")
