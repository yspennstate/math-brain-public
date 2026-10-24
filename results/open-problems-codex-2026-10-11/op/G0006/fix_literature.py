from pathlib import Path
p=Path('LITERATURE.md');s=p.read_text(encoding='utf8')
s=s.replace('Theorem 1.1 assumes a parameter lambda_1 strictly ABOVE lambda_c at which there is already no percolation; it then gives exponential decay for smaller parameters. It does not provide that starting nonpercolating supercritical parameter.', 'Theorem 1.1 (PDF p. 4) assumes a parameter lambda at which there is already no percolation and gives exponential decay at every smaller parameter. To deduce the desired gap one would first need a nonpercolating parameter strictly above lambda_c; the theorem does not provide one.')
s+='\nOriginal Liggett--Steif preprint, Section 8, Question 2, PDF p. 25, states verbatim (subscripts normalized):\n\n> For d ≥ 2, does there exist λ > λc such that νλ does not percolate? (In words, is the critical value for percolation different than the usual critical value?)\n\nThis is the original form of the same question. Final-paper section numbering differs from this preprint.\n'
p.write_text(s,encoding='utf8')
assert 'assumes a parameter lambda_1 strictly ABOVE' not in s
print('Literature statement corrected and original question recorded.')
