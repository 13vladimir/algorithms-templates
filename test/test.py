commands = [['push_front', '861'], ['push_front', '-819'], ['pop_back'], ['pop_back']]

for action, value in commands:
    print(action, value)
    [print(getattr(queue, action)())
     if value == '' else getattr(queue, action)(value)]