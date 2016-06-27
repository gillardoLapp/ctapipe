import pytest
from traitlets import Float, TraitError

from .. import Tool


def test_tool_simple():
    """test the very basic functionality of a Tool"""

    class MyTool(Tool):
        description = "test"
        userparam = Float(5.0, help="parameter").tag(config=True)

    tool = MyTool()
    tool.userparam = 1.0
    tool.log_level = 'DEBUG'
    tool.log.info("test")
    tool.run([])
