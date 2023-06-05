from pathlib import Path

# optionally pass in a path like "emails" from current dir
path = Path()
# print(path.mkdir())
# print(path.exists())
# print(path.rmdir())
# search for files and directories in a certain path
# '*.*' - gett all files in current dir
# '*' - gett all files and dirs
# '*.py' - gett all files with extension
for file in path.glob('*'):
    print(file)