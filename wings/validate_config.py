import toml


class ValidateConfig():
    """ Validate a wings.toml config file """
    def __init__(self, config_file):
        self.config = toml.load(config_file)
        self._validate()

    def _validate(self):
        """ Validation rules for the config """

        # First, we check if all required keys are present.
        REQUIRED_KEYS = ["name", "runtime"]

        for key in REQUIRED_KEYS:
            if key not in self.config.keys():
                raise IOError(
                    "Required key '{}' missing from wings.toml.".format(key))

        if 'service' not in self.config['runtime']:
            raise IOError("Required key 'service' missing from [runtime].")

        # Next, we make check for a valid runtime service.
        RUNTIME_SERVICES = ["lambda"]
        service = self.config['runtime']['service']

        if service not in RUNTIME_SERVICES:
            raise IOError(
                "'{}' is an invalid runtime service. Must be one of: {}"
                .format(service, ', '.join(RUNTIME_SERVICES)))

        # Finally, we validate the service specific configuration.
        LAMBDA_LANGUAGES = ["python36"]
        if service == 'lambda':
            if 'language' not in self.config['runtime']:
                raise IOError(
                    "Required key 'language' missing from [runtime]. "
                    "Supported values for 'language' are: "
                    "{}".format(', '.join(LAMBDA_LANGUAGES)))

            language = self.config['runtime']['language']
            if language not in LAMBDA_LANGUAGES:
                raise IOError("'{}' is an invalid lanaguage for Lambda. "
                              "Supported languages are: {}".format(
                                language, ', '.join(LAMBDA_LANGUAGES)))
