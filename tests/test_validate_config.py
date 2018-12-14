import pytest
import toml
from unittest.mock import patch
from wings.validate_config import ValidateConfig


@patch('toml.load')
def test_validate_config_with_valid_data(mock_toml_load):
    mock_toml_load.return_value = toml.loads("""
        name = "wings"
        description = "Weeeee"

        [runtime]
        service = "lambda"
        language = "python36"
    """)

    config = ValidateConfig('/fake_path_yo/wings.toml').config

    assert config == {
        'description': 'Weeeee',
        'name': 'wings',
        'runtime': {
            'language': 'python36',
            'service': 'lambda'
        }
    }


@patch('toml.load')
def test_validate_config_with_missing_name_key(mock_toml_load):
    mock_toml_load.return_value = toml.loads("""
        description = "Weeeee"

        [runtime]
        service = "lambda"
        language = "python36"
    """)

    with pytest.raises(KeyError):
        ValidateConfig('/fake_path_yo/wings.toml').config


@patch('toml.load')
def test_validate_config_with_missing_runtime_key(mock_toml_load):
    mock_toml_load.return_value = toml.loads("""
        name = "wings"
        description = "Weeeee"

        service = "lambda"
        language = "python36"
    """)

    with pytest.raises(KeyError):
        ValidateConfig('/fake_path_yo/wings.toml').config


@patch('toml.load')
def test_validate_config_with_missing_service_key(mock_toml_load):
    mock_toml_load.return_value = toml.loads("""
        name = "wings"
        description = "Weeeee"

        [runtime]
        language = "python36"
    """)

    with pytest.raises(KeyError):
        ValidateConfig('/fake_path_yo/wings.toml').config


@patch('toml.load')
def test_validate_config_with_invalid_service_value(mock_toml_load):
    mock_toml_load.return_value = toml.loads("""
        name = "wings"
        description = "Weeeee"

        [runtime]
        service = "blah"
        language = "python36"
    """)

    with pytest.raises(ValueError):
        ValidateConfig('/fake_path_yo/wings.toml').config


@patch('toml.load')
def test_validate_config_with_missing_language_key(mock_toml_load):
    mock_toml_load.return_value = toml.loads("""
        name = "wings"
        description = "Weeeee"

        [runtime]
        service = "lambda"
    """)

    with pytest.raises(KeyError):
        ValidateConfig('/fake_path_yo/wings.toml').config


@patch('toml.load')
def test_validate_config_with_invalid_language(mock_toml_load):
    mock_toml_load.return_value = toml.loads("""
        name = "wings"
        description = "Weeeee"

        [runtime]
        service = "lambda"
        language = "python69420"
    """)

    with pytest.raises(ValueError):
        ValidateConfig('/fake_path_yo/wings.toml').config
