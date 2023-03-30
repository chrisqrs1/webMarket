import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
from PIL import Image
import logging


pathStrategies = Path('/Users/christopheedlinger/OneDrive - QRS1/Data/Processed Data/VIX/Strategies/Implied Convexity')

pathProcessedData = Path('/Users/christopheedlinger/OneDrive - QRS1/Data/Processed Data/VIX/processedData')

@st.cache_data()
def load_data(
        directory: Path,
        filename: str) -> pd.DataFrame:
    df = pd.read_parquet(directory / filename)
    return df



def scatter_plot(df) -> go.Figure:
    pass



def set_logger(
        log_directory: Path = Path("log"),
        log_file: Path | None = Path('logfile.log'),
        name: str = __name__,
        file_level: int = logging.INFO,
        console_level: int | None= logging.INFO

) -> logging.Logger:

    logging.basicConfig(datefmt='%d-%b-%y %H:%M:%S')
    logger = logging.getLogger(name)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    if isinstance(log_file, Path):
        if not os.path.isdir(log_directory):
            os.makedirs(log_directory)
        file_handler = logging.FileHandler(log_directory / log_file, mode='a', encoding='utf-8')
        file_handler.setLevel(file_level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    if isinstance(console_level, int):
        console_handler = logging.StreamHandler()
        console_handler.setLevel(console_level)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger
