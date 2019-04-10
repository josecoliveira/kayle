import os
import subprocess
import shlex


def get_tests():
    inputs_file_names = os.listdir("inputs")
    outputs_file_names = os.listdir("outputs")
    if len(inputs_file_names) != len(outputs_file_names):
        raise Exception("Number os inputs and outputs is not equal.")
    tests = []
    for i in range(len(inputs_file_names)):
        input_file = open("inputs/" + inputs_file_names[i], "r")
        output_file = open("outputs/" + outputs_file_names[i], "r")
        input_content = input_file.read()
        output_content = output_file.read()
        tests.append({
            "name": inputs_file_names[i],
            "input": input_content,
            "output": output_content
        })
    return tests


def main():
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

    tests = get_tests()
    print(tests)


if __name__ == "__main__":
    main()
