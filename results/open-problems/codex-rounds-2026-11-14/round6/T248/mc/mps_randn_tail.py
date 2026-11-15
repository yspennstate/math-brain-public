"""Count draws of torch.randn on the Apple GPU beyond 7 in absolute value. A true Gaussian gives about 2.6e-12 per
draw, so 2e8 draws should show none. Usage: python3 mps_randn_tail.py"""
import torch

dev = torch.device("mps")
torch.manual_seed(1)
n_big, n_tot, top = 0, 0, 0.0
for _ in range(8):
    z = torch.randn(16, 500, 3125, device=dev)
    a = z.abs()
    n_big += int((a > 7).sum().item())
    top = max(top, float(a.max().item()))
    n_tot += z.numel()
    del z, a
print(f"draws {n_tot:.3e}  beyond 7: {n_big}  rate {n_big / n_tot:.3e}  max |z| {top:.2f}  (2^-23 = {2**-23:.3e})")
