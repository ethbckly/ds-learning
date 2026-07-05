def retry(func):
    def wrapper(*args, **kwargs):
        for i in range(3):
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                print(f"Attempt {i+1} failed.")
                      
                if i == 2:
                    raise e
    return wrapper


@retry
def unreliable():
    raise Exception("Failed")

unreliable()

