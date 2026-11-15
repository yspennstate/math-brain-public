import sys
from fractions import Fraction as F
sys.path.insert(0, r"~/AppData/Local/Temp/claude/727c9a8b9fa813fe/agent-66b6-4575-b3c4-a8807fd17369/scratchpad/zen8/toeplitz-hankel-section-profiles/engine")
from exact_volume import pairing_volume_exact

def pm_of(word):
    pos = {}
    for i, ch in enumerate(word):
        pos.setdefault(ch, []).append(i)
    pm = [None] * len(word)
    for a, b in pos.values():
        pm[a], pm[b] = b, a
    return tuple(pm)

def vol(word, kind="T"):
    return F(pairing_volume_exact(pm_of(word), kind))

def gaps(core, ins):
    return [vol(core[:g] + ins + core[g:]) for g in range(len(core))]

print("abab+cdcd", sorted(set(gaps("abab", "cdcd"))), "want 9/20")
print("abcabc+dede", sorted(set(gaps("abcabc", "dede"))), "want 61/180")
print("abcdabcd+efef", sorted(set(gaps("abcdabcd", "efef"))), "want 19/70")
print("abacbdcd+efef", sorted(set(gaps("abacbdcd", "efef"))), "want 1/4, 313/1260")
print("flatten a(abab)a", vol("xababx"), "want p(abab) = 2/3")
print("12123434", vol("abab" + "cdcd"), "12341234", vol("abcdabcd"), "want 9/20, 2/5")
print("w3w3 Hankel", vol("abcabcdefdef", "H"), "want 23/90")
