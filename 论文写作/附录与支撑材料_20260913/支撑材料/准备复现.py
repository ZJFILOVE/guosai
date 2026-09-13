"""Copy source and official inputs to a new run tree, without overwriting supplied results."""
from pathlib import Path
import argparse, shutil
p=argparse.ArgumentParser()
p.add_argument('--data-dir',type=Path,required=True)
p.add_argument('--output',type=Path,required=True)
a=p.parse_args(); base=Path(__file__).resolve().parent; out=a.output.resolve(); data=a.data_dir.resolve()
names=['C题.pdf','附件1.xlsx','附件2.xlsx','附件3.xlsx','附件4.xlsx','result1.xlsx','result2.xlsx','result3.xlsx','result4-2.xlsx','result4-3.xlsx']
for n in names:
 if not (data/n).is_file():raise FileNotFoundError(data/n)
if out.exists():raise FileExistsError('Choose a new output directory: '+str(out))
out.mkdir(parents=True)
shutil.copytree(base/'源码/代码',out/'代码')
(out/'基础数据').mkdir()
for n in names:shutil.copy2(data/n,out/'基础数据'/n)
for d in ['建模思路','论文写作/问题三']:(out/d).mkdir(parents=True,exist_ok=True)
print('Prepared:',out)
