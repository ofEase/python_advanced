# /前面是位置参数， * 后面只能是关键参数
def greet(name, /, gender, *, age, height):
    print(f"my name is {name}, is {gender}, {age} old, {height}")


if __name__ == "__main__":
    greet("张三", "男", age=18, height=172)
