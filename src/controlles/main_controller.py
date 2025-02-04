from pathlib import Path

class MainController:
    def __init__(self, view):
        self.view = view
        self._files = set()  # Permite apenas arquivos unicos na lista
        self._filesCount = len(self._files)
        self._connect_signals()

    def _connect_signals(self):
        self.view.btn_load.clicked.connect(self.load_files)
        self.view.file_dropped.connect(self.add_files)

    def load_files(self):
        init_dir = self.view.input_files.text() or str(Path.home())
        files, _ = self.view.open_file_dialog(init_dir)

        self.add_files(files)

    def add_files(self, files):
        for file in files:
            file_path = Path(file)
            if file_path not in self._files:  
                self._files.add(file_path)  
                self.view.list_files.addItem(file_path.name)
        self._filesCount = len(self._files)
