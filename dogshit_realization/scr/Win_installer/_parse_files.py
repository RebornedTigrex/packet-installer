import os

def _parse_files(self): # TODO: Переписать с pathlib
        files = []
        if self.config_data["parce_type"] == "all":
            for filename in os.listdir(self.config_data["parce_dir"]):
                if filename.endswith(".msi") or filename.endswith(".exe") and not filename.startswith("script"): # Хардкод. Да. TODO: Сделать нормальную проверку названия исполняемого файла.
                    files.append('"'+os.path.abspath(os.path.join(filename)).replace("\\", "/")+'"')
        if len(files) == 0:
            raise ValueError("No msi files found in the specified directory") # TODO: Сделать нормальную обработку отсутствия установочных файлов.
        return files