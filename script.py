import os, json

class MsiInstaller:
    
    def __init__(self, config_path = "config.json"):
        
        self.config = config_path
        
        
        self.abspath = os.getcwd()
        self.config_base = {
        "parce_dir": f"{self.abspath}",
        "parce_type": "all",
        "arg": "/qn /promptrestart", # TODO: Аргументы должны быть более универсальными (Не только для msi).
        "install_dir": "D:/Programs",
        
        "git_integration": True, # Если аргумент True и parce_type == all, то скрипт устанавливает все пакеты на гите после установки пакетов в директории.
        "git_url": "https://github.com/path_to_your_repo.git"
        }
        self.config_data = self.config_base

    def _load_config(self)-> None:
        try:
            with open(self.config, 'r') as f:
                self.config_data = json.load(f)
            os.close(self.config)
            
            if "parce_type" not in self.config_data:
                raise Exception("ParamDoestExist:1:", "Configuration parameter 'parce_type' is missing. 'parce_type' set to default value.")
            if "arg" not in self.config_data:
                raise Exception("ParamDoestExist:2:", "Configuration parameter 'arg' is missing. 'arg' set to default value.")
            
            
        except json.JSONDecodeError:
            print(f"Invalid JSON'{self.config}' or file does not exist. Script is using default configuration.")
            
        except Exception as err:
            print(f"Panic! In metood {self._load_config.__name__}: {err.args}")
            if err.args[0] == "ParamDoestExist:1:":
                self.config_data["parce_type"] = self.config_base["parce_type"]
            if err.args[0] == "ParamDoestExist:2:":
                self.config_data["arg"] = self.config_base["arg"]
    
    def _parse_files(self):
        files = []
        if self.config_data["parce_type"] == "all":
           for filename in os.listdir(self.config_data["parce_dir"]):
            if filename.endswith(".msi") or filename.endswith(".exe") and not filename.startswith("script"): # Хардкод. Да. TODO: Сделать нормальную проверку названия исполняемого файла.
                files.append('"'+os.path.abspath(os.path.join(filename)).replace("\\", "/")+'"')
        if len(files) == 0:
            raise ValueError("No msi files found in the specified directory") # TODO: Сделать нормальную обработку отсутствия установочных файлов.
        return files
            
       

    def initilize_setup(self): # Эта хуйня работает только с msi. TODO: Добавить поддержку exe.
        self._load_config()
        command_msi = 'msiexec /i '
       
        arguments = f"{self.config_data["arg"]}"
        for file in self._parse_files():
            print(command_msi + file + " " + arguments)
            try:
                
                os.system(command=command + file + " " + arguments)
                print("Installation successful!")
            except:
                print("Bro, your file sucks")
        


obj = MsiInstaller()

obj.initilize_setup()