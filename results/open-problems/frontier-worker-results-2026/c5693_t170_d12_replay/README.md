# T170 D12: independent replay of the base-row certificate

`replay_d12.py` checks T170-LEAD-ROLLING-D12-001 v1 (dimension 12, cap C = 512, scale S = 2^40,
alpha0 = 109131241376 units). It was written from the proof text alone, sections 1 and 3. It does not
import or read the certifier's code.

It rebuilds every interior value h[a,b,c] with c >= 2 from the stated ceiling recursion. Within each
a-slice it sweeps the anti-diagonals b + c. It checks that each ceiling slack lies in [0, den) and that
every |h| is at most S. Then it checks every base-row inequality at c = 1 against alpha0.

Run: `python replay_d12.py <base_bias json>`, about 13 minutes on one core.

Result, 17 Oct 2026 (`replay.log`):

- base file sha256: 1c7e9d95534edb98fecfc9c6d29b0c5130eaf5fc3ed0dce4cdbfa2509412acc0
- interior values: 133,955,584 of 133,955,584 (C*C*(C-1))
- smallest ceiling slack: 0
- largest base requirement: 109,131,226,328, against alpha0 109,131,241,376, a margin of 15,048 units at (427, 1, 1)
- largest total rate: 20,467, against R = 35,328
- largest |h|: 106,983,757,728, against S = 2^40

REPLAY PASS. This replay was run by a different session than the certifier, but under the same
account. It is a consistency check, not an external review.
