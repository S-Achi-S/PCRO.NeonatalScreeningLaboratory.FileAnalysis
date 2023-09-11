from dataclasses import dataclass
from pathlib import Path
import pandas as pd


@dataclass
class ObjectApp:
    """Class for keeping object data."""
    #
    file_path = Path
    file_name = str
    file_extension = str
    file_size = float
    #
    upload_file = bool
    read_file = bool
    check_file_extension = bool
    #
    data_frame = pd.DataFrame()
    data_frame_after_process = pd.DataFrame()

    #
    def __post_init__(self):
        if not self.file_path:
            raise ValueError("file_path must be provided")
