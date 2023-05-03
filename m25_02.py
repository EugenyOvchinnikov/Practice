import random


errors_list = ['KillError', 'DrunkError', 'CarCrashError']

if random.random() < 1 / 2:
    now_error = random.choice(errors_list)
    raise Exception(now_error)
else:
    print('нет исключения')


# raise Exception('KillError')







    # KillError,
    # DrunkError,
    # CarCrashError,
    # GluttonyError,
    # DepressionError.
