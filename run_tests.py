import subprocess


def main():
    cmd = ["python", "-m", "unittest", "discover"]
    subprocess.run(cmd)


# python -m unittest discover
