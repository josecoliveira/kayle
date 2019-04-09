import os
import subprocess
import shlex


def main():
    inputs_file_names = os.listdir("inputs")
    inputs_file_names = os.listdir("outputs")
    # output = os.system("python submissions/submission.py < inputs/input1.txt")
    # print(output)
    command = "python submissions/submission.py"
    args = shlex.split(command)
    p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    try:
        print("try")
        # outs, errs = p.communicate(input="1".encode("utf-8"), timeout=15)
        outs, errs = p.communicate(input="1".encode("utf-8"), timeout=15)
    except subprocess.TimeoutExpired:
        print("except")
        p.kill()
        outs, errs = p.communicate()

    print("Outs", outs.decode("utf-8"))
    print("Errs", errs)


if __name__ == "__main__":
    main()
