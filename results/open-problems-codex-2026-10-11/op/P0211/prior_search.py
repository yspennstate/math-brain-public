import pathlib,json
root=pathlib.Path('~/<private-repo>/06_math_research')
for folder in list(root.glob('probability_1000_intake_*'))+[root/'codex_pool_2026_10_10']:
 if folder.exists():
  count=0
  for path in folder.rglob('*'):
   if path.is_file() and path.suffix in ('.jsonl','.md'):
    count+=1
    for line in path.read_text(encoding='utf8',errors='replace').splitlines():
     if 'P0211' in line: print(str(path),line[:12000])
  print('searched',folder,count)
