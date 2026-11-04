"""Register Kedro pipelines."""

from kedro.pipeline import Pipeline

from highrev.pipelines.pizza_panic.pipeline import (
    create_pipeline as create_pizza_pipeline,
)


def register_pipelines() -> dict[str, Pipeline]:
    """Register the Pizza Panic experiment."""

    pizza_pipeline = create_pizza_pipeline()

    return {
        "pizza_panic": pizza_pipeline,
        "__default__": Pipeline([]),
    }