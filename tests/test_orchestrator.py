
import unittest
from src.orchestrator import Orchestrator

class TestOrchestrator(unittest.TestCase):

    def setUp(self):
        self.orchestrator = Orchestrator()

    def test_add_model(self):
        class MockModel:
            pass
        mock_model = MockModel()
        self.orchestrator.add_model("test_model", mock_model)
        self.assertIn("test_model", self.orchestrator.models)
        self.assertEqual(self.orchestrator.get_model("test_model"), mock_model)

    def test_run_model(self):
        class MockCallableModel:
            def __call__(self, input_data):
                return f"Processed: {input_data}"
        mock_callable_model = MockCallableModel()
        self.orchestrator.add_model("callable_model", mock_callable_model)
        result = self.orchestrator.run("callable_model", "hello")
        self.assertEqual(result, "Processed: hello")

    def test_run_non_existent_model(self):
        with self.assertRaises(ValueError):
            self.orchestrator.run("non_existent_model", "data")

    def test_define_workflow(self):
        def my_workflow(data):
            return f"Workflow processed: {data}"
        self.orchestrator.define_workflow("my_custom_workflow", my_workflow)
        self.assertTrue(hasattr(self.orchestrator, "my_custom_workflow"))
        self.assertEqual(self.orchestrator.my_custom_workflow("test"), "Workflow processed: test")

    def test_list_models(self):
        class MockModel1: pass
        class MockModel2: pass
        self.orchestrator.add_model("model1", MockModel1())
        self.orchestrator.add_model("model2", MockModel2())
        self.assertCountEqual(self.orchestrator.list_models(), ["model1", "model2"])

if __name__ == '__main__':
    unittest.main()
