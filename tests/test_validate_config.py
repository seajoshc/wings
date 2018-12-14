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
