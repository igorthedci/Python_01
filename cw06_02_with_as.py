"""
МЕНЕДЖЕР КОНТЕКСТА
"""

class File:
    
    def __exit__(self, exception):
        pass
        self.close()


class MyClass:

    def __enter__(self):
        pass

    def __exit__(self, exception):
        exception == self.exception