# helloWorld.py# -*- coding: utf-8 -*-

# 定义一个函数，让调用更加结构化
def hello():
    print("Hello, World!")


# https://www.runoob.com/python3/python3-name-main.html
# 当脚本被直接运行时，__name__的值为"__main__"
# 这种模式允许模块在被导入时不会执行某些代码，而只有在作为独立脚本运行时才会执行这些代码。
# 这使得模块可以被重用而不会执行不必要的代码
if __name__ == "__main__":
    hello()

# 而这部分会在脚本被导入时执行
hello()
