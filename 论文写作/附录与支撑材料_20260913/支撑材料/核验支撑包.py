"""Verify packaged file integrity; no optimization is performed."""
from pathlib import Path
import ast, lzma, hashlib, json
root=Path(__file__).resolve().parent
m=json.loads((root/'文件校验清单.json').read_text(encoding='utf-8'))
for name,h in m.items():assert hashlib.sha256((root/name).read_bytes()).hexdigest()==h,name
for row in json.loads((root/'核验/文件来源与哈希.json').read_text(encoding='utf-8')):
 if row['lossless_xz']:assert hashlib.sha256(lzma.decompress((root/row['path']).read_bytes())).hexdigest()==row['source_sha256'],row['path']
for p in (root/'源码').rglob('*.py'):ast.parse(p.read_text(encoding='utf-8-sig'),filename=str(p))
print('PASS',len(m),'file hashes; XZ recovery and Python syntax.')
