class Toolchain():
    def __init__(self, config):
        """ Constructor for Toolchain objects """
        self.config = config

    def build_toolchain(self):
        required_resources = self._determine_required_resources()
        self._create_all_resources(required_resources)
        pass

    def _determine_required_resources(self):
        """
        Check the config and determine what cloud resources to create
        for the specified runtime service.
        """
        if self.config['runtime']['service'] == 'lambda':
            return self._lambda_required_resources()
        pass

    def _lambda_required_resources(self):
        required_resources = [
            "function_iam_role", "codepipeline_iam_role", "lambda_function",
            "codepipeline", "codedeploy"
        ]
        existing_resources = self._look_for_existing_wings_resources()
        for required_resource in required_resources:
            if required_resource in existing_resources:
                required_resources.remove(required_resource)
        return required_resources

    def _look_for_existing_wings_resources(self):
        return []

    def _create_all_resources(self, resources):
        pass
