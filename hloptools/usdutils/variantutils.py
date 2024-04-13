"""
Utilities for working with USD Variants
"""

from pxr import Usd, Sdf
from typing import *


def _add_variant_set(sdf_layer: Sdf.Layer, path: Union[str, Sdf.Path], variantset_name: str) -> Usd.Prim:
    """
    Adds a variant set to the given path on the given layer.
    :param sdflayer: The layer to add the variant set to.
    :param path: The path to add the variant set to.
    :param variantset_name: The name of the variant set to add.
    :return: The prim of the variant set.
    """
    variant_set_prim = sdf_layer.GetPrimAtPath(path)
    Sdf.VariantSetSpec(variant_set_prim, variantset_name)
    variant_set_prim.SetInfo("variantSetNames", Sdf.StringListOp.Create(prependedItems=[variantset_name]))
    return variant_set_prim

