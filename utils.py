from wrapper import Wrapper

def try_int(data: str) -> Wrapper:
    try:
        return Wrapper.Success(int(data))
    except:
        return Wrapper.Failure("Int cast Invalid")