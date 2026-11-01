import pathlib,subprocess,pymupdf
s=pathlib.Path('source.txt').read_text(encoding='utf8')
for key in ['Theorem 2.1','Theorem 3.2','Problem 4.6','Theorem 3.4','v_t','vt','?t']:
 i=s.find(key);print('\n',key, i);print(s[max(i-300,0):i+2200])
r=subprocess.run(['git','-C','~/math-open-problems','ls-tree','-r','--name-only','origin/master'],capture_output=True,text=True,encoding='utf8')
paths=[x for x in r.stdout.splitlines() if 'P0177' in x or 'global_free' in x or 'brownian_mode' in x.lower()]
pathlib.Path('prior_paths.txt').write_text('\n'.join(paths),encoding='utf8');print('matching prior paths',len(paths));print('\n'.join(paths[:35]))
d=pymupdf.open('source.pdf')
for i,p in enumerate(d):
 if 'Problem 4.6.' in p.get_text():print('Problem PDF page',i+1);pathlib.Path('problem_page.txt').write_text(p.get_text(),encoding='utf8')
