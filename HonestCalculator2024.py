
msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

msg_3 = "Yeah... division by zero. Smart move..."

msg_4 = "Do you want to store the result? (y / n):"

msg_5 = "Do you want to continue calculations? (y / n):"

msg_6 = " ... lazy"

msg_7 = " ... very lazy"

msg_8 = " ... very, very lazy"

msg_9 = "You are"

msg_10 = "Are you sure? It is only one digit! (y / n)"

msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"

msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

operation = {"+", "-", "*", "/"}

global memory
global result
memory = 0
result = 0


def calculator():
    global result
    global memory
    while True:

        calc = input(msg_0)
        x, oper, y = calc.split()

        if x == 'M':
            x = memory
            pass
        else:
            pass

        if y == 'M':
            y = memory
            pass
        else:
            pass

        try:
            x = float(x)
            y = float(y)
        except ValueError:
            print(msg_1)
            continue

        if oper not in operation:
            print(msg_2)
            continue

        check(x, y, oper)

        if oper == '+':
            result = x + y
        elif oper == '-':
            result = x - y
        elif oper == '*':
            result = x * y
        elif oper == '/':
            try:
                result = x / y
            except ZeroDivisionError:
                print(msg_3)
                continue

        result = float(result)
        print(result)

        memory_fnc()
        break


def memory_fnc():
    global result
    global memory
    while True:
        store_result = str(input(msg_4))
        try:
            if store_result == 'y':
                if is_one_digit(result) is True:
                    msg_index = 10
                    while True:
                        if msg_index == 10:
                            want_continue = str(input(msg_10))
                        elif msg_index == 11:
                            want_continue = str(input(msg_11))
                        elif msg_index == 12:
                            want_continue = str(input(msg_12))

                        if want_continue == 'y':
                            if msg_index < 12:
                                msg_index = msg_index + 1
                                continue
                            else:
                                memory = result
                                break
                        elif want_continue == 'n':
                            break
                        else:
                            continue
                if is_one_digit( result ) is False:
                    memory = result
                    pass

                # print( f"""SAVED Memory Result {result}""" )
                while True:
                    continue_check = str(input(msg_5))
                    try:
                        if continue_check == 'y':
                            calculator()
                        elif continue_check == 'n':
                            exit()
                    except ValueError:
                        continue

            elif store_result == 'n':
                # print( f"""UNSAVED Memory Result {result}""" )
                continue_check = str(input(msg_5))
                try:
                    if continue_check == 'y':
                        calculator()
                    elif continue_check == 'n':
                        exit()
                except ValueError:
                    continue
                break
        except ValueError:
            memory()


def is_one_digit(v):
    if (-10 < v < 10) and v == int(v):

        return True
    else:
        return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) is True and is_one_digit(v2) is True:
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg = msg + msg_8

    if msg != '':
        msg = msg_9 + msg
        print(msg)
    else:
        pass


calculator()
