from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=  True)
class preparebaseModelConfig:
    root_dir:Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int
    