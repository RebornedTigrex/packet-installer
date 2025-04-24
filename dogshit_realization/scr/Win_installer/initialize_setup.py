import os

def initialize_setup(self): # Эта хуйня работает только с msi. TODO: Добавить поддержку exe.
        self._load_config()
        command = 'msiexec /i '
       
        arguments = f"{self.config_data["arg"]}"
        for file in self._parse_files():
            print(command + file + " " + arguments)
            try:
                
                os.system(command=command + file + " " + arguments)
                print("Installation successful!")
            except:
                print("Bro, your file sucks")