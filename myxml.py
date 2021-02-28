# Write a function, myxml, that allows you to create simple XML output. The output from the function will always
# be a string. The function can be invoked in a number of ways, as shown in table


def myxml(tag, content="", **param):
    attrs = ''.join([f' {k}="{v}"' for k, v in param.items()])
    return f"<{tag}{attrs}>{content}</{tag}>"


if __name__ == '__main__':
    print(myxml("foo"))
    print(myxml("foo", "bar"))
    print(myxml("foo", "bar", a=1, b=2))
    print(myxml("foo", "bar", a=1, b=2, c=3, d=4, e=5))
