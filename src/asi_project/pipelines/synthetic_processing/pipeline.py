"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import synthetic,preprocess_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
         node(
                func=preprocess_data,
                inputs=["syndata"],
                outputs=["preprocessed_oversampled_bank1","preprocessed_undersampled_bank1", "data_encoder1"],
                name="synned_node",
            )

    ])
