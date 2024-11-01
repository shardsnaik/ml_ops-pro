from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConig_return_type:
    root_dir: Path
    source_URL: str
    local_data_file : Path
    unzip_dir : Path
