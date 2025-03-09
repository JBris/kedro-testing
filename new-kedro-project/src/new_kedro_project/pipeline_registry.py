"""Project pipelines."""

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline

def foo():
    return "dummy"

def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = find_pipelines()
    pipelines["__default__"] = sum(pipelines.values())
    return pipelines

from kedro.pipeline import pipeline, node


# def register_pipelines():
#     return {"__default__": pipeline([node(foo, None, "dummy_output")])}