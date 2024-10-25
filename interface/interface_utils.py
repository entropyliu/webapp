"""interface utils"""
from datetime import datetime
import pytz

def rename_key(key):
    """
    :param key:
    :return: renamed key for data from OFR
    """
    key = key.replace("FNYR-", "")
    key = key.replace("Pctl", "%")
    key = key.replace("-A", "")
    key = key.replace("_", " ")
    return key

def format_figure(figure):
    """
    :param figure:
    :return: formatted figure
    """
    figure = figure.update_layout(
        {
            "paper_bgcolor": "rgba(0, 0, 0, 0)",
            "plot_bgcolor": "rgba(0, 0, 0, 0)",
        }
    )
    figure.update_xaxes(showgrid=False)
    figure.update_yaxes(showgrid=False, zeroline=False)
    figure.update_layout(font={'color': "#E0E0E0"}, margin={'l': 60, 'r': 0})
    return figure

def end_date():
    """
    :return: return data in EST
    """
    return datetime.now(pytz.timezone("America/New_York")).replace(hour=0, minute=0, second=0, microsecond=0)
