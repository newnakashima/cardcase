import glob
import subprocess
for test in glob.glob("test/*"):
    print(test)
    subprocess.run(["python", test], stdout=subprocess.PIPE)
