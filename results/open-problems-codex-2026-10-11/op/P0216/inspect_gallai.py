import pathlib
R=pathlib.Path(__file__).resolve().parent
txt=(R/'orientation_paper.txt').read_text(encoding='utf8')
print('AUTHORS AND TITLE\n'+txt[:2200])
print('PDF PAGE 5\n'+txt.split('--- PDF PAGE 5 ---')[1].split('--- PDF PAGE 6 ---')[0])
for line in txt.splitlines():
 if 'Gallai' in line or 'Transitiv orientierbare' in line:print('GALLAI_REF',line)
