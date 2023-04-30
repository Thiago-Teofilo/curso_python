from pathlib import Path
import os
from datetime import datetime

# new_dir = Path(os.path.join(os.path.dirname(__file__))) / 'new_dir'
# new_dir.mkdir(exist_ok=True)

# new_subdir1 = Path(os.path.join(new_dir)) / 'subdir1'
# new_subdir2 = Path(os.path.join(new_dir)) / 'subdir2'
# new_subdir1.mkdir(exist_ok=True)
# new_subdir2.mkdir(exist_ok=True)

# for subdir in new_dir.glob('*'):
#     if subdir.is_dir():
#         new_file = subdir / "file.txt"
#         new_file.touch()
#         new_file.write_text(str(datetime.now()))

###############################################################################

# p = Path(__file__).parent / 'new_dir'
# [print(x) for x in p.iterdir() if x.is_dir()]

###############################################################################

file = Path(__file__).parent / 'new_dir' / 'subdir1' / 'file.txt'

with file.open() as f: f.readlines()