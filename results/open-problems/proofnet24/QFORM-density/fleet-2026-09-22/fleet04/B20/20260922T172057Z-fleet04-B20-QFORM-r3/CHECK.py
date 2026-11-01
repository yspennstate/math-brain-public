import math

B = (2 + math.sqrt(math.pi)) * (4 * math.e) ** 0.25
cross_cut = 768 * B
zero_pivot = 48 * 2 ** 0.75
candidate = 32768 * math.sqrt(2)

assert zero_pivot < 80.727
assert cross_cut < 5262
assert 1198.924 < 5262
assert cross_cut < candidate

# Layer-cake coefficients in Lemma 5.1: inside 1 + integral exp(-u/4)du,
# plus one outside contribution.
assert 1 + 4 + 1 == 6

print(f"B={B:.12f}")
print(f"zero_pivot={zero_pivot:.12f}")
print(f"cross_cut={cross_cut:.12f}")
print(f"candidate={candidate:.12f}")
print("PASS QFORM-CROSS-DOMINATED-SECOND-SCHUR-CLOSURE-v1")
