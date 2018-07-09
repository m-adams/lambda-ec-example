# lambda-ec-example
This is an example lambda function to demonstrate indexing using a lambda function in AWS to ingest from an SNS topic to Elastic Cloud

Create a lambda function in AWS and link it to your SNS topic
Compress the items in this repository in to a zip archive

Upload the zip file in to the lambda function in the lambda editing page.

Set the environment variables for your Elastic Cloud cluster

Test with the standard test event.

You may wish to change the fields that are sent to elasticsearch either in the lambda function or in an elasticsearch ingest pipeline.
