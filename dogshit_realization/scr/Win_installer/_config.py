from pathlib import Path
import json, os

class configUtils:
    def __init__(self, config_path = f"{Path(__file__).parents[1]}/config.json"):
        self.config = config_path
        
        self.parent_dir = Path(__file__).parents[1] # dogshit_realization/
        
        test = "test"
        
        self.config_base = {
        "parce_dir": f"{self.parent_dir}/sources",
        "parce_type": "all",
        "arg": "/qn /promptrestart", # TODO: Аргументы должны быть более универсальными (Не только для msi).
        # "uni_args": "q, promptrestart", # Строчка пока бесполезна
        "install_dir": f"D:/Programs/{test}",
        
        "git_integration": True, # Если аргумент True и parce_type == all, то скрипт устанавливает все пакеты на гите после установки пакетов в директории.
        "git_url": "https://github.com/path_to_your_repo.git"
        }
        self.config_data = self.config_base
    
    def _load_config(self)-> None:
            try:
                with open(self.config, 'r') as f:
                    self.config_data = json.load(f)
                
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
    
      