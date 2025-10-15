import sys
#from sys import argv, exit
#if len(argv) == 2:
#    print(f"hello {argv[1]}")
#else:
#    print("hello world")   


#for i in argv[1:]:
#    if i != 'argv.py':
#        print(i)

#    print(i)

if len(sys.argv) != 2:
    print("Missing command argument")
    sys.exit(1)
print(f"hello {sys.argv[1]}")
sys.exit(0)