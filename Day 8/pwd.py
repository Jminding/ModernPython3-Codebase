import os

class PasswordManager:
    
    def __init__(self):
        pass
    
    def read(self, file: str) -> dict:
        file = open(os.path.join("Day 8", file), "r")
        file_contents = file.read().strip()
        pwd = eval(file_contents)
        file.close()
        return pwd

    def write(self, file: str, content: dict) -> bool:
        try:
            file = open(os.path.join("Day 8", file), 'w')
            file.write(str(content))
            file.close()
        except Exception:
            return False