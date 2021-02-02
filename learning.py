import time


def usetime(func):
    def wrap():
        start = time.time()
        func()
        time.sleep(1)
        end = time.time()
        use_time = end - start
        print(f"{func.__name__} used {use_time}")

    return wrap


@usetime
def step1():
    print("step1************")


@usetime
def step2():
    print("step2************")


step1()
step2()


def say_hello(contry):
    def wrapper(func):
        def deco(*args, **kwargs):


            func(*args, **kwargs)

            if contry == "china":
                print("你好")
            elif contry == "usa":
                print("hello")
            else:
                return


        return deco

    return wrapper


@say_hello("china")
def xiaoming(txt):
    print("小明说：{}".format(txt))


@say_hello("usa")
def jack(txt):
    print("jack：{}".format(txt))

xiaoming("xiaomingshouxxxx")
jack("99999")

