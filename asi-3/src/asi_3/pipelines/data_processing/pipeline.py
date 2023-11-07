"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import preprocess_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
         node(
                func=preprocess_data,
                inputs=["mushrooms", "params:rm_cols"],
                outputs="preprocessed_mushrooms",
                name="mushrooms_processed_node",
            )

    ])
