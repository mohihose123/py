
class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def empty(self):
        return len(self.items) == 0


def priority(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op == '^':
        return 3
    return 0


# تبدیل رشته به لیست (برای اعداد چند رقمی)
def tokenize(exp):
    tokens = []
    num = ""

    for ch in exp:
        if ch.isdigit():
            num += ch
        else:
            if num != "":
                tokens.append(num)
                num = ""
            if ch != " ":
                tokens.append(ch)

    if num != "":
        tokens.append(num)

    return tokens


def infix_to_postfix(exp):
    s = Stack()
    result = []

    tokens = tokenize(exp)

    for token in tokens:

        if token.isdigit():
            result.append(token)

        elif token == '(':
            s.push(token)

        elif token == ')':
            while s.top() != '(':
                result.append(s.pop())
            s.pop()

        elif token in ['+', '-', '*', '/', '^']:
            while (not s.empty()) and s.top() != '(' and priority(s.top()) >= priority(token):
                result.append(s.pop())
            s.push(token)

    while not s.empty():
        result.append(s.pop())

    return result


def evaluate_postfix(exp):
    s = Stack()

    for token in exp:

        if token.isdigit():
            s.push(int(token))

        else:
            b = s.pop()
            a = s.pop()

            if token == '+':
                s.push(a + b)
            elif token == '-':
                s.push(a - b)
            elif token == '*':
                s.push(a * b)
            elif token == '/':
                s.push(a / b)
            elif token == '^':
                s.push(a ** b)

    return s.pop()


# برنامه اصلی
infix = input("ebarat miavandi ra vared kon: ")

postfix = infix_to_postfix(infix)
answer = evaluate_postfix(postfix)

print("ebart pasvande:", " ".join(postfix))
print("natije:", answer)
