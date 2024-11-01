from dataclasses import dataclass
from pathlib import Path

@dataclass 
class TrainingConfig:
    root_dir: Path
    trained_model: Path
    update_base_model_path: Path
    training_data: Path
    prams_epochs: int
    params_batch_size: int
    params_agumentation: int
    params_img_size: list
