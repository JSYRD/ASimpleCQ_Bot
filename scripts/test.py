class A():
    def __init__(self) -> None:
        pass

class B(A):
    def __init__(self) -> None:
        super().__init__()
    
b = B()
print(isinstance(b, A))