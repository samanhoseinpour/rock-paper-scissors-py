from datetime import datetime


def logger(func):
    def wrapped_func(*args, **kwargs):
        print(args, kwargs)
        return func(*args, **kwargs)

    return wrapped_func


def play_time(func):

    def wrap_function(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)      # run main function
        end_time = datetime.now()
        duration = end_time - start_time
        hours = duration.seconds // 3600
        minutes = duration.seconds // 60
        seconds = duration.seconds % 60
        print(
            f"Elapsed time: {hours} hours, {minutes} minutes, "
            f"{seconds} seconds")

        return result

    return wrap_function
