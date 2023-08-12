import boto3
import time
from IPython.display import IFrame
import csv
from trp import Document
import os


def startJob(s3BucketName, objectName, textract):
    response = None
    response = textract.start_document_analysis(
        DocumentLocation={
            'S3Object': {
                'Bucket': s3BucketName,
                'Name': objectName
            }
        },
        FeatureTypes=["TABLES"]
    )

    return response["JobId"]


def isJobComplete(jobId, textract):
    response = textract.get_document_analysis(JobId=jobId)
    status = response["JobStatus"]
    print("Job status: {}".format(status))

    while(status == "IN_PROGRESS"):
        time.sleep(5)
        response = textract.get_document_analysis(JobId=jobId)
        status = response["JobStatus"]
        print("Job status: {}".format(status))

    return status


def getJobResults(jobId, textract):

    pages = []
    response = textract.get_document_analysis(JobId=jobId)

    pages.append(response)
    print("Resultset page recieved: {}".format(len(pages)))
    nextToken = None
    if('NextToken' in response):
        nextToken = response['NextToken']

    while(nextToken):
        response = textract.get_document_analysis(
            JobId=jobId, NextToken=nextToken)

        pages.append(response)
        print("Resultset page recieved: {}".format(len(pages)))
        nextToken = None
        if('NextToken' in response):
            nextToken = response['NextToken']

    return pages

def call_textract(s3BucketName, documentName, selected_language_code, require_translate):
    # Amazon S3 client
    s3 = boto3.client('s3')

    # Amazon Textract client
    textract = boto3.client('textract')

    IFrame(s3.generate_presigned_url('get_object', Params={
           'Bucket': s3BucketName, 'Key': documentName}), 900, 400)

    jobId = startJob(s3BucketName, documentName, textract)
    print("Started job with id: {}".format(jobId))
    if(isJobComplete(jobId, textract)):
        response = getJobResults(jobId, textract)

    # Specify the filename for the CSV file
    csv_filename = os.path.splitext(documentName)[0]+'.csv'

    doc = Document(response)
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for page in doc.pages:
            # Print tables
            for table in page.tables:
                for r, row in enumerate(table.rows):
                    formatRow = []
                    for c, cell in enumerate(row.cells):
                        formatRow.append(cell.text)
                    writer.writerow(formatRow)

    print(f"Table data saved to {csv_filename}")

    if require_translate:
        # Translate the CSV file to the selected language using Amazon Translate
        translate = boto3.client('translate')
        response = translate.translate_text(
            Text=open(csv_filename, 'r').read(),
            SourceLanguageCode="auto",
            TargetLanguageCode=selected_language_code
        )

        translated_csv_filename = os.path.splitext(documentName)[0] + f'_{selected_language_code}.csv'

        with open(translated_csv_filename, 'w', newline='') as translated_csvfile:
            translated_csvfile.write(response['TranslatedText'])

        print(f"Translated CSV data saved to {translated_csv_filename}")

