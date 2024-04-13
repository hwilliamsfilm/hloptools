"""
Utilities for working with USD Sdf Layers
"""

from pxr import Usd, Sdf


def _copy_to_anonymous(layer_to_copy: Sdf.Layer) -> (Sdf.Layer, Usd.Stage):
    """
    Copies the content of the given layer to a new anonymous layer.
    :param layer_to_copy: The layer to copy.
    :return: The new layer and stage.
    """
    new_layer = Sdf.Layer.CreateAnonymous()
    new_layer.TransferContent(layer_to_copy)
    new_stage = Usd.Stage.Open(new_layer)
    return new_layer, new_stage

