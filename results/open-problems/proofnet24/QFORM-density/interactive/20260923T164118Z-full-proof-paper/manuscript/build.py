"""Build the anonymous manuscript using standard local TeX tools."""
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parent
commands = [
    ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'main.tex'],
    ['bibtex', 'main'],
    ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'main.tex'],
    ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'main.tex'],
]
for index, command in enumerate(commands, 1):
    result = subprocess.run(command, cwd=root, capture_output=True, text=True)
    (root / f'build-{index}.txt').write_text(result.stdout + result.stderr)
    if result.returncode:
        raise SystemExit(f'{command[0]} failed; see build-{index}.txt')
log = (root / 'main.log').read_text(errors='replace')
bad = [line for line in log.splitlines() if
       ('undefined' in line.lower() and 'warning' in line.lower())
       or 'Overfull' in line or 'multiply defined' in line]
if bad:
    raise SystemExit('Review the final LaTeX log:\n' + '\n'.join(bad))
print('Built main.pdf with resolved references and no overfull boxes.')
