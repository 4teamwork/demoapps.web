from demoapps.web.testing import DEMOAPPS_FUNCTIONAL
from ftw.lawgiver.tests.base import WorkflowTest


class TestSESWebWorkflowSpecification(WorkflowTest):
    layer = DEMOAPPS_FUNCTIONAL
    workflow_path = '../profiles/default/workflows/demoapps_web_workflow'
