import os.path
import sys


def rename(inp_dir, old_ext, new_ext):
    for path, dirs, files in os.walk(inp_dir):
        for name in files:
            base_name, ext = os.path.splitext(os.path.join(path, name))
            if old_ext == ext:
                os.rename(os.path.join(path, name), base_name + new_ext)


if __name__ == '__main__':
    if len(sys.argv) == 4:
        rename(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print('3 arguments required. \nUsage: python main.py path/to/src/dir .oldExt .newExt')
