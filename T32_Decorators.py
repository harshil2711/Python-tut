# Decorators are used to deorate the existing function.

def dec1(fx):
    def mfx():
        print("Good morning")
        fx()
        print("Have a great day")
    return mfx

@dec1
def func1():
    print("this is function 1")

func1()

# Output
# Good morning
# this is function 1
# Have a great day

# _______________________________________________________________________


def dec1(fx):
    def mfx(a , b):
        print("Good morning ")
        fx(a , b)
        print("Thanks for your time")
    return mfx


@dec1
def add(a , b):
    print(a + b)
    # print(f"hello {name}")/

add(5,6)


# Output
# Good morning
# 11
# Thanks for your time