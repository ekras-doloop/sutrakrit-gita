"""Test that the example per-verse object validates against the schema,
and that any rendered objects in `rendered/` validate as well.

This is the regression test that ensures the schema is well-formed
and that no rendered object drifts out of conformance.
"""

import json
from pathlib import Path

import jsonschema
import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = REPO_ROOT / "schema" / "per-verse-object.schema.json"
EXAMPLE_PATH = REPO_ROOT / "schema" / "example-bg-2-55.json"
RENDERED_DIR = REPO_ROOT / "rendered"


@pytest.fixture
def schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text())


def test_schema_is_valid_jsonschema(schema):
    """The schema document itself must be a valid JSON Schema."""
    jsonschema.Draft202012Validator.check_schema(schema)


def test_example_validates_against_schema(schema):
    """The committed example for BG 2.55 must validate against the schema."""
    example = json.loads(EXAMPLE_PATH.read_text())
    jsonschema.validate(instance=example, schema=schema)


@pytest.mark.parametrize(
    "rendered_file",
    sorted(RENDERED_DIR.glob("bg_*.json")) if RENDERED_DIR.exists() else [],
)
def test_rendered_object_validates(schema, rendered_file):
    """Every per-verse object in `rendered/` must validate against the schema."""
    obj = json.loads(rendered_file.read_text())
    jsonschema.validate(instance=obj, schema=schema)


def test_rendered_objects_have_audit_trails(schema):
    """Every per-verse object must have a complete audit_trail.

    This is a separate check beyond schema validation because the schema
    only requires audit_trail's presence and basic structure; this test
    ensures that the audit_trail is substantively populated for every
    rendered object.
    """
    if not RENDERED_DIR.exists():
        pytest.skip("rendered/ directory does not yet exist (build in progress)")

    for rendered_file in sorted(RENDERED_DIR.glob("bg_*.json")):
        obj = json.loads(rendered_file.read_text())
        audit = obj.get("audit_trail", {})
        assert audit.get("substrate_version"), f"{rendered_file}: missing substrate_version"
        assert audit.get("fitted_weights"), f"{rendered_file}: missing fitted_weights"
        assert audit.get("corpus_provenance"), f"{rendered_file}: missing corpus_provenance"
        assert audit.get("extraction_date"), f"{rendered_file}: missing extraction_date"
