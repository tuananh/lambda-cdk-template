from aws_cdk import core as cdk, aws_lambda as lambda_

class LambdaCDKStack(cdk.Stack):
    """The LambdaCDKStack Stack."""

    def __init__(
        self,
        scope: cdk.Construct,
        construct_id: str,
        config: dict,
        **kwargs,
    ) -> None:
        """Construct a new LambdaCDKStack."""
        super().__init__(scope, construct_id, **kwargs)

        self.my_function = lambda_.Function(
            scope=self,
            id="my_function",
            runtime=lambda_.Runtime.PYTHON_3_8,
            code=lambda_.Code.asset("lambda/"),
            handler="index.lambda_handler",
            timeout=cdk.Duration.seconds(config["lambda_timeout"]),   
        )