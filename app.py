#!/usr/bin/env python3
import os

import aws_cdk as cdk

from lambdatestevents_stack import LambdaTestEventsStack


app = cdk.App()
LambdaTestEventsStack(app, "LambdaTestEventsStack")

app.synth()