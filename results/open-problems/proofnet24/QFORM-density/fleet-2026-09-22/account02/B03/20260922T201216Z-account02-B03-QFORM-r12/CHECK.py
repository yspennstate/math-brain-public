import math

C_star = 16 * math.sqrt(2) / (3 ** (3/4))
weighted_time_constant = math.sqrt(2 * math.pi) * C_star

print(f"C_STAR={C_star:.15f}")
print(f"WEIGHTED_TIME_CONSTANT={weighted_time_constant:.15f}")
for r in (1, 2, 3):
    partner = 8 * r / (2 * r - 1)
    print(f"PARTNER_R{r}={partner:.15f}")

assert C_star < 9.927
assert abs(weighted_time_constant / math.sqrt(2 * math.pi) - C_star) < 1e-12
print("STATUS=PASS")
