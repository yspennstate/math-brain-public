import pathlib
import sqlite3

owner = pathlib.Path('~')
for rel in ['<private-repo>/06_math_research/probability_1000_intake_claude_20260907', '<private-repo>/06_math_research/probability_1000_attempts_H_20260912', '<private-repo>/06_math_research/probability_1000_attempts_I_20260914']:
    root = owner / rel
    print('FILES', root)
    for p in sorted(root.iterdir()):
        print(p.name)
print('NAMED MEMOS')
for pat in ['*P0174*', '*P0389*', '*C0089*', '*P0030*', '*P0234*', '*C0010*', '*C0068*', '*C0101*', '*C0148*', '*P0022*']:
    for p in (owner / 'Downloads').glob(pat):
        if p.is_file() and p.suffix in {'.md', '.txt', '.pdf', '.json'}:
            print(p)
db = owner / 'math-brain-build/local/population/brain.sqlite3'
con = sqlite3.connect(db.as_uri() + '?mode=ro', uri=True)
for name, ddl in con.execute("SELECT name, sql FROM sqlite_master WHERE type='table'"):
    print('TABLE', name, ddl[:500] if ddl else '')
con.close()
