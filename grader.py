import os
import subprocess
import shlex
import json
from typing import List, Union
import csv

Num = Union[int, float]


def convert_string_matrix_to_float(matrix: List[List[str]]) -> List[List[float]]:
    return [list(map(lambda x: float(x), line)) for line in matrix]


def get_matrix_from_string(string: str) -> List[List[Num]]:
    if string[-1] == '\n':
        string = string[0:-1]
    matrix = list(map(lambda x: x.split(' '), string.split('\n')))
    return convert_string_matrix_to_float(matrix)


def get_tests() -> list:
    inputs_file_names = os.listdir("inputs")
    outputs_file_names = os.listdir("outputs")
    inputs_file_names.sort()
    outputs_file_names.sort()
    if len(inputs_file_names) != len(outputs_file_names):
        raise Exception("Number os inputs and outputs is not equal.")
    tests = []
    for i in range(len(inputs_file_names)):
        input_file = open("inputs/" + inputs_file_names[i], "r")
        output_file = open("outputs/" + outputs_file_names[i], "r")
        input_content = input_file.read()
        output_content = output_file.read()
        output_matrix = get_matrix_from_string(output_content)
        tests.append({
            'name': inputs_file_names[i],
            'input': input_content,
            'output': output_matrix
        })
    return tests


def compare_matrix(player_matrix: List[List[Num]], judge_matrix: List[List[Num]]) -> bool:
    # Check number os lines
    player_num_lines = len(player_matrix)
    judge_num_lines = len(judge_matrix)
    if player_num_lines != judge_num_lines:
        print("Number of lines are not the same")
        return False

    # Check if lines have the same size
    if any(len(player_matrix[0]) != len(line) for line in player_matrix):
        print("Matrices have note the same number elements each line")
        return False

    # Check elements are the same
    for i in range(len(judge_matrix)):
        for j in range(len(judge_matrix[i])):
            if player_matrix[i][j] != judge_matrix[i][j]:
                print("Some element are different")
                return False

    return True


def main():
    all_reports = []
    tests = get_tests()
    tests_names = [test['name'] for test in tests]
    submissions = os.listdir("submissions")

    for index_submission, submission in enumerate(submissions):
        print('Grading submission {0}. {1}'.format(index_submission, submission))
        report = dict()
        report['Submission'] = submission
        tests_passed = 0
        for index_test, test in enumerate(tests):
            # print('- Test {0}. {1}'.format(index_test, test['name']))
            command = 'python submissions/{0} < inputs/{1}'.format(submission, test['name'])
            args = shlex.split(command)
            p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            veredict_text = '- Test {0}. {1}: '.format(index_test, test['name'])
            try:
                outs, errs = p.communicate(input=test['input'].encode('utf-8'), timeout=15)
                if p.returncode != 0:
                    veredict_text += 'RUNTIME ERROR'
                    report[test['name']] = 'RUNTIME ERROR'
                else:
                    player_output = outs.decode('utf-8')
                    player_matrix = get_matrix_from_string(player_output)
                    if compare_matrix(player_matrix, test['output']):
                        veredict_text += 'ACCEPTED'
                        tests_passed += 1
                        report[test['name']] = 'ACCEPTED'
                    else:
                        veredict_text += 'WRONG ANSWER'
                        report[test['name']] = 'WRONG ANSWER'
            except subprocess.TimeoutExpired:
                veredict_text += 'TIME LIMIT EXCEEDED'
                report[test['name']] = 'TIME LIMIT EXCEEDED'
                p.kill()
            except subprocess.CalledProcessError:
                veredict_text += 'RUNTIME ERROR'
                report[test['name']] = 'RUNTIME ERROR'
            print(veredict_text)
        report['Tests passed'] = tests_passed
        report['Grade'] = tests_passed / len(tests)
        all_reports += [report]

    csv_columns = ['Submission'] + tests_names + ['Tests passed', 'Grade']
    csv_file_name = 'report.csv'
    try:
        with open(csv_file_name, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
            writer.writeheader()
            for data in all_reports:
                writer.writerow(data)
    except IOError:
        print('I/O Error')


if __name__ == "__main__":
    main()
