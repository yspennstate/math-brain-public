import math
import random

random.seed(20260923)
N = 500_000
mx = -1.0
arg = None
for _ in range(N):
    h = random.random() * 0.249999
    theta_lo = 1.0 - 2.0*h + 1e-12
    theta_hi = 1.0 - h
    theta = theta_lo + (theta_hi-theta_lo)*random.random()
    u = random.random() * 0.249999
    tau = math.sqrt(max(0.0, 1.0-theta))*random.random()
    v = random.random()  # |z|

    q0 = u*(1.0-h+h*v*v)/(1.0-h)
    q1 = (
        theta*u + h*tau*tau
        + 2.0*math.sqrt(theta*h*u)*tau*v
        + h*u*(1.0-v*v)
    )/(theta+h)
    val = q0+q1
    if val > mx:
        mx = val
        arg = (h, theta, u, tau, v, q0, q1)

Z_lower = 3.0/32.0
C_capped = 3.0*math.e*(32.0/3.0)**(1.0/3.0)
C_diffuse = 3.0*math.exp(5.0/6.0)*128.0**(1.0/6.0)

print(f"samples={N}")
print(f"max_sampled_q0_plus_q1={mx:.15f}")
print("argmax=(h,theta,u,tau,v,q0,q1)")
print(tuple(round(x, 15) for x in arg))
print(f"Z_lower={Z_lower:.15f}")
print(f"capped_branch_constant={C_capped:.15f}")
print(f"diffuse_branch_constant={C_diffuse:.15f}")
assert mx < 1.0
assert C_capped < 17.952
assert C_diffuse < 15.497
