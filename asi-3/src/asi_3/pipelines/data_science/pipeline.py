"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import train_test_val_split,train_model, train_model,eval_model



def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([

         node(
                func=train_test_val_split,
                inputs=["mushrooms_processed","params:target_var_name" ,"params:test_size", "params:val_size"],
                outputs=['X_train', 'X_test', 'y_train', 'y_test',  'X_val', 'y_val'],
                name="split_data_node",
            ),
            
         node(
                func=train_model,
                inputs=['X_train', 'y_train'],
                outputs="classifier",
                name="train_model_node",
            ),
        node(
                func=eval_model,
                inputs=["classifier", 'X_test','y_test'],
                outputs=None,
                name="eval_model_node",
            )





    ])
