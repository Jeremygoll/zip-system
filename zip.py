import os
import zipfile
import sh

firstDownload = True
folderInZip = ""

# put zip file to s3 bucket zip-system-put
def putZipToS3(zip):
    sh.aws('s3', 'cp', zip, 's3://zip-system-put')

# Download the sample data from S3
def download_from_s3(docket_id, name_id):  
    global firstDocketID
    global folderInZip
    if name_id != None or name_id != "" or name_id != " ":
        firstDocketID = name_id
    else:
        if firstDownload:
            firstDocketID = docket_id
            folderInZip = False
    total_size_limit=500000000 # Set a total size limit (default: 500MB)
    if not os.path.exists(f"temp-data/{firstDocketID}"):
        os.makedirs(f"temp-data/{firstDocketID}")
    docket_dir = f"temp-data/{firstDocketID}/{docket_id}"
    if os.path.exists(docket_dir):
        return False  # Skip if the directory already exists
    os.makedirs(docket_dir)
    # Download files recursively from S3
    docket_info = docket_id.split("-")
    sh.aws('s3', 'cp', 's3://mirrulations/' + docket_info[0] + '/' + docket_id, docket_dir, '--recursive')
    # Calculate total size of downloaded files
    total_size = sum(os.path.getsize(os.path.join(root, file)) for root, _, files in os.walk(docket_dir) for file in files)
    if total_size > total_size_limit:
        sh.rm('-r', docket_dir)  # Delete downloaded data if limit exceeded
        return True
    else:
        return False

# Zip temp-data into data.zip keeping temp-data/ as the root directory
def zipSampleData(name_id, docket_ids):
    global firstDocketID
    zip_file_name = f"{name_id}.zip"  # Define the name of the zip file
    with zipfile.ZipFile(zip_file_name, 'w') as zipf:
        for docket_id in docket_ids:
            docket_dir = f"temp-data/{firstDocketID}/{docket_id}"
            for root, _, files in os.walk(docket_dir):  
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, "temp-data")) 