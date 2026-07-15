# coding: utf-8

"""Contract regression test against the live demo.multiflexi.eu server.

Guards against a repeat of the drift found in 2026-07: the generated pydantic
models here are derived from multiflexi-api/openapi-schema.yaml, but that
schema can silently diverge from what the PHP API server actually returns.
Mock-based unit tests can't catch that class of bug by construction, so this
test hits the real demo server instead.

Opt-in only (network dependent): set MULTIFLEXI_LIVE_DEMO_TESTS=1 to run it,
e.g. in a scheduled CI job, not on every commit.
"""

import os
import unittest

import pytest

import multiflexi_client
from multiflexi_client.configuration import Configuration as MultiFlexiApiConfiguration

DEMO_HOST = os.environ.get(
    "MULTIFLEXI_LIVE_DEMO_HOST",
    "https://demo.multiflexi.eu/api/VitexSoftware/MultiFlexi/1.0.0",
)
DEMO_USERNAME = os.environ.get("MULTIFLEXI_LIVE_DEMO_USERNAME", "demo")
DEMO_PASSWORD = os.environ.get("MULTIFLEXI_LIVE_DEMO_PASSWORD", "demo")


@pytest.mark.live_demo
@unittest.skipUnless(
    os.environ.get("MULTIFLEXI_LIVE_DEMO_TESTS") == "1",
    "set MULTIFLEXI_LIVE_DEMO_TESTS=1 to run tests against the live demo server",
)
class TestLiveDemoContract(unittest.TestCase):
    """Reproduces the 4 calls that crashed with pydantic.ValidationError in 2026-07."""

    def setUp(self):
        configuration = MultiFlexiApiConfiguration(host=DEMO_HOST)
        configuration.username = DEMO_USERNAME
        configuration.password = DEMO_PASSWORD
        self.api_client = multiflexi_client.ApiClient(configuration)

    def tearDown(self):
        self.api_client.close()

    def test_list_apps_returns_a_list(self):
        api = multiflexi_client.AppApi(self.api_client)
        result = api.list_apps("json")
        self.assertIsInstance(result, list)
        self.assertGreaterEqual(len(result), 1)
        for app in result:
            self.assertIsInstance(app, multiflexi_client.App)

    def test_list_run_templates_returns_a_list(self):
        api = multiflexi_client.RuntemplateApi(self.api_client)
        result = api.list_run_templates("json")
        self.assertIsInstance(result, list)
        for runtemplate in result:
            self.assertIsInstance(runtemplate, multiflexi_client.RunTemplate)

    def test_get_app_by_id_exit_codes_is_a_dict(self):
        api = multiflexi_client.AppApi(self.api_client)
        app = api.get_app_by_id(64, "json")
        self.assertIsInstance(app, multiflexi_client.App)
        if app.exit_codes:
            self.assertIsInstance(app.exit_codes, dict)
            for detail in app.exit_codes.values():
                self.assertIsInstance(detail, multiflexi_client.ExitCodeDetail)
                self.assertIn(
                    detail.severity, {"success", "error", "warning", "info", None}
                )

    def test_get_run_template_by_id_field_types(self):
        api = multiflexi_client.RuntemplateApi(self.api_client)
        runtemplate = api.get_run_template_by_id(1, "json")
        self.assertIsInstance(runtemplate, multiflexi_client.RunTemplate)
        self.assertIsInstance(runtemplate.active, bool)
        self.assertNotIsInstance(runtemplate.success, str)
        self.assertNotIsInstance(runtemplate.fail, str)


if __name__ == "__main__":
    unittest.main()
