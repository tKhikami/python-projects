import sys

if len(sys.argv[1:]) > 1:
    print("AssertionError: more than one argument is provided")
    sys.exit(1)
elif len(sys.argv[1:]) == 0:
    sys.exit(0)

try:
    if int(sys.argv[1]) % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

except:
    print("AssertionError: argument is not an integer")
    sys.exit(1)