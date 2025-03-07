from abc import abstractmethod
import json


@abstractmethod
def _get_reasoning_for_anomaly(anomaly_belnr) -> json:
    """
    Abstract method to get reasoning for a given anomaly.

    Parameters:
    anomaly_belnr (Any): The anomaly for which reasoning is to be provided.

    Returns:
    Any: The reasoning for the given anomaly.
    """
    pass


def max():
    pass
