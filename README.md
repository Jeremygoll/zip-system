# zip-system

### Requirements before use

This file serves as a way to recursively download folders from AWS S3. It utilizes the `sh` library.

First and foremost, you must download the AWS Cli here: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

After you clone the repo you will have to create a virtual environment and install the necessary requirements

```
pip install -r requirements.txt
```

Finally before you run any of the corresponding programs you will need to configure your AWS credentials locally before using this:
[AWS Configure](https://repost.aws/knowledge-center/s3-locate-credentials-error)
The necessary information can be found via 1Password. 
### Using zip.py

This file serves as a way to zip up files.

When zip.py starts up it will prompt you to enter the ID(s) of the files you would like zipped.

```
Enter the file IDs separated by commas:
```
Example of what to enter:
```
Enter the file IDs separated by commas: IHS-2005-0004,CRB-2009-0003,CRB-2006-0005
```
### Using sendEmail.py

This file serves as a way to send emails

In order for it to work you must complete the following:

1. Create a spare Gmail account 
2. Add 2-Step Verification to the account 
    1. Go to the account settings for the email account 
    2. On the left-hand side go to the Security tab 
    3. 2-Step Verification will be under the "How to sign into Google" section within the Security tab 
3. Go to [THIS](https://myaccount.google.com/apppasswords) link and create an App Password
    1. If it says "The setting you are looking for is not available for your account." repeat step 2
    2. Enter whatever name you want for the App Password
    3. Hit the "create" button
    4. A pop-up with a generated password will appear. Copy the password and save it somewhere
4. Go to the projects folder and create a .env file (if there is not one already)
    1. Within the .env file make sure it contains the following
        ```
        EMAIL=ENTER_YOUR_EMAIL_HERE
        PASSWORD=ENTER_YOUR_APP_PASSWORD_HERE_(MAKE SURE THERE ARE NO SPACES WITHIN THE PASSWORD!)
        ```
    


