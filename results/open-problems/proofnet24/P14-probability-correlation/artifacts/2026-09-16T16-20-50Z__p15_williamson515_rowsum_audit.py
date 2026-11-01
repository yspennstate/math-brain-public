#!/usr/bin/env python3
"""Independent exact P14 audit of P15's Williamson-515 row-sum filter.

Scope: recompute the sorted positive odd quadruples 1<=a<=b<=c<=d<=45
with a^2+b^2+c^2+d^2=2060, and the payload SHA-256 used by P15.
This is only a necessary Williamson row-sum condition; it makes no
Williamson or Hadamard existence claim.
"""
from hashlib import sha256

TARGET = 2060
EXPECTED_COUNT = 29
EXPECTED_SHA256 = "a769190c974f5cd9210fbbd337fa055418314e26ec4a7de8fe89d440e028e5a6"

sol = []
for a in range(1, 46, 2):
    for b in range(a, 46, 2):
        for c in range(b, 46, 2):
            for d in range(c, 46, 2):
                if a*a + b*b + c*c + d*d == TARGET:
                    sol.append((a, b, c, d))

payload = "\n".join(",".join(map(str, t)) for t in sol) + "\n"
digest = sha256(payload.encode("ascii")).hexdigest()

print(f"target={TARGET}")
print(f"count={len(sol)}")
for t in sol:
    print("signature=" + ",".join(map(str, t)))
print(f"payload_sha256={digest}")
print("scope=necessary Williamson row-sum filter only; no Williamson/Hadamard existence claim")

assert len(sol) == EXPECTED_COUNT
assert digest == EXPECTED_SHA256
print("P14_INDEPENDENT_AUDIT_PASS")
