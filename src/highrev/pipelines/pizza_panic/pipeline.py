"""Pizza Panic Kedro pipeline."""

from kedro.pipeline import Pipeline, node

from .nodes import prepare_features, split_data, search_candidates


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=prepare_features,
                inputs=["pizza_orders", "pizza_restaurants"],
                outputs="pizza_features",
                name="prepare_pizza_features",
            ),
            node(
                func=split_data,
                inputs=["pizza_features", "params:pizza_settings"],
                outputs="pizza_split",
                name="split_pizza_data",
            ),
            node(
                func=search_candidates,
                inputs=[
                    "pizza_split",
                    "params:pizza_settings",
                    "params:pizza_selection",
                ],
                outputs=["pizza_results", "pizza_models"],
                name="search_pizza_candidates",
            ),
        ]
    )