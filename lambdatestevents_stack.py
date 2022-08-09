from aws_cdk import (
    Stack,
    aws_eventschemas as schemas
)
# from constructs import Construct
from constructs import Construct

from schemaconfig import schema

class LambdaTestEventsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        #Pass the Lambda Function Name at cdk synth/cdk deploy time with -c lambda_function_name=
        lambdafunctionname = self.node.try_get_context("lambda_function_name")
        #EventBridge Schema for Lambda Test Events
        lambdatesteventschema = schemas.CfnSchema(self, 'MyLambdaTestEventSchema',
                                    description='My Lambda Test Event Schema',
                                    content=schema,
                                    registry_name='lambda-testevent-schemas',
                                    type="OpenApi3",
                                    schema_name="_" + str(lambdafunctionname) + "-schema",
                                    tags=[schemas.CfnSchema.TagsEntryProperty(
                                        key="key",
                                        value="value"
                                    )]
                                    )



