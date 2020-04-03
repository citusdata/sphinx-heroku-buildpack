import os
import static

with open('/app/.build-dir') as fb:
    build_dir = fb.read().strip()

build_path = os.path.join('/app', build_dir, 'html')
application = static.Cling(build_path)
