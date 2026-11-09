import argparse

def p6_cli_add(left, right):
    return left + right  # P6_PYTHON_CLI_BUG

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('left', type=int)
    parser.add_argument('right', type=int)
    args = parser.parse_args()
    print(p6_cli_add(args.left, args.right))
