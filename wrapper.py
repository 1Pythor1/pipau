from __future__ import annotations

class Wrapper:
    def __init__(self, check: bool, msg: str, data):
        self.check = check
        self.msg = msg
        self.data = data
    
    def Success(data = None) -> Wrapper:
        return Wrapper(True, "Success", data)
    
    def Failure(msg: str) -> Wrapper:
        return Wrapper(False, msg, None)
    
    def EnrichFailure(self, msg: str) -> Wrapper:
        self.msg += f"\n{msg}"
        return self