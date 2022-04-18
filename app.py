#!/usr/bin/env python3

from aws_cdk import core as cdk
from config import Config
from cdk_stack.lambda_cdk_template import (
    LambdaCDKStack,
)

config = Config()

app = cdk.App()
LambdaCDKStack(
    scope=app,
    construct_id="LambdaCDKStack",
    config=config.base(),
)

app.synth()
