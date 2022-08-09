
# Create Lambda Test Events using AWS CDK!

To create Lambda Test Events run:
```
❯ cdk deploy -c lambda_function_name=MY_LAMBDA_FUNCTION_NAME
```

To change the Lambda Test Event information edit `schemaconfig.py`

To generate a new event structure for `schemaconfig.py` based off existing Lambda Test Event templates:
1. Create a Shareable Test Event using a Lambda Test Event in the Console
2. run:
```
❯ aws schemas describe-schema --registry-name lambda-testevent-schemas --schema-name _MY_LAMBDA_FUNCTION_NAME-schema --query 'Content' > schema-definition.json
```
3. Ensure the `schema =` is set in `schemaconfig.py`

## Other generic CDK Stuff below

This is a project for CDK creation of AWS Lambda Test Events with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
