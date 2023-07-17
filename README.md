# PoE-Textract

PoE Textract is an Amazon Textract Tabular Formatted Parser Application for UoT Price of Empire project. The application can let users upload pdf or image files and scan the tabular data into csv files. 

## Table of Contents

- [Stack](#stack)
- [Pipeline](#pipeline)
- [Setup](#setup)
	- [Install](#install)
    - [Usage](#usage)
- [Deployment](#deployment)
- [Contributors](#contributors)
- [License](#license)

## Stack
- <strong>GUI</strong> Python Tkinter
- <strong>Data</strong> All data is saved in Amazon S3 and Amazon DynamoDB
- <strong>Processing</strong> Amazon Textract

## Pipeline
<img src="./public/textract-pipeline.drawio.png" width="800"/>

## Setup
### Install the required dependencies 

This project mainly depends on [Tkinter](https://docs.python.org/3/library/tkinter.html#module-tkinter)

```sh
$ pip install -r requirements.txt
```

## Usage
1.	Run the app:
    ```sh
    $ python file_uploader.py
    ```
2.	The FileUploader window will open.
3.	Click the "Upload File" button to select a PDF or image file.
4.	Once the file is uploaded, the file name will be displayed.
5.	Click the "Download File" button to save the uploaded file to a desired location.

## Deployment

## Contributors

## License
