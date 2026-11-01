from pathlib import Path
p=Path(__file__).with_name('make_literature.py')
t=p.read_text(encoding='utf8')
t=t.replace('Equation (8), Section 5, PDF page 8','Equation (8), Section 5, PDF page 7')
t=t.replace('GitHub returned one repository for "Potts reconstruction" (a vision reconstruction repository, not a mathematical solution), and zero for "Potts monotonicity".','GitHub returned one repository for "Potts reconstruction", long-mathematics/openai-math-extensions, containing Christopher D. Long\'s 11 October 2026 heterogeneous four-state capacity manuscript, and zero for "Potts monotonicity". The mathematical repository was inspected and its four-state OpenAI dependencies followed directly. These are leads rather than an arbitrary-alphabet comparison theorem.')
p.write_text(t,encoding='utf8')
print('Corrected source page and GitHub lead description.')
