# End-to-end Adam (PyTorch update, bias correction) with random reshuffling and eta_k = eta0/sqrt(k) on the scalar model;
# prints the epoch-averaged iterate at checkpoints, to compare with the frozen-x limit point x*.
import numpy as np, sys
n = 10; b2 = float(sys.argv[1]); b1 = float(sys.argv[2]); eta0 = float(sys.argv[3]); K = int(float(sys.argv[4])); seed = int(sys.argv[5])
b = np.array([n - 1.0] + [-1.0] * (n - 1)); a = np.ones(n); rng = np.random.default_rng(seed)
x, m, v, k = 0.5, 0.0, 0.0, 0  # x0 = 1 gives g = 0 and v = 0 at step 1 (0/0)
acc = 0.0; cnt = 0
while k < K:
    for i in rng.permutation(n):
        k += 1; g = a[i] * x + b[i]
        m = b1 * m + (1 - b1) * g; v = b2 * v + (1 - b2) * g * g
        x -= eta0 / np.sqrt(k) * (m / (1 - b1 ** k)) / (np.sqrt(v / (1 - b2 ** k)) + 0.0)
        if k > K // 2: acc += x; cnt += 1
    if k % (K // 10) < n: print(k, x, flush=True)
print("mean x over second half", acc / cnt)
