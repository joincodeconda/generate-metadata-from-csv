# generate-metadata-from-csv

## Step 1: Generate Metadata with PhotoTag.ai

First things first, let's generate some metadata for your images:

1. **Visit [PhotoTag.ai](https://phototag.ai)** and log in to your account. If you don’t have an account, creating one is quick and free.
2. **Upload Your Photos**: Once logged in, you can upload the photos you wish to generate metadata for. PhotoTag.ai allows you to upload and process multiple images simultaneously, saving you a lot of time.
3. **Export Metadata**: After the AI has analyzed your photos, click on the **Export** button located in the top right corner of the dashboard. Ensure the export setting is on **Default** to get a CSV file containing titles, descriptions, and keywords for each photo.

## Step 2: Setting Up Your Environment

Before we proceed with the Python script that will add the metadata to your photos, you need to ensure your computer is ready to run it.

### Install Python

If you haven't already, download and install Python from the [official website](https://www.python.org/downloads/). During installation, make sure to select the option to **Add Python to PATH**.

### Install Required Python Packages

Our script requires a few Python packages to run. Open your command line or terminal and install the following packages:

```bash
pip install pandas piexif
```

This command installs:
- `pandas` for reading the CSV file.
- `piexif` for handling the EXIF data in the images.

## Step 3: The Python Script

Use the Python script located in this repo. This script reads the exported CSV file and writes the generated metadata into the corresponding images' metadata.

**Note**: Remember to replace `csv_file_path = 'your_metadata.csv'` and `image_directory = 'your_images_directory/'` with your actual file path and image directory. For example, if everything is saved in the Downloads folder, you should use `csv_file_path = 'Downloads/your_metadata.csv'` and `image_directory = 'Downloads/'`.

### Where to Save the Python Script

1. **Create a New Text File**: Open a text editor (Notepad, TextEdit, or any code editor), and paste the Python script code into it.
2. **Save the File**: Save this file with a `.py` extension, for example, `generate-metadata-from-csv.py`. It’s best to save this script in the same directory as your photos or in a dedicated project folder.

## Step 4: Running the Script

With everything set up, it’s time to run the script and load the generated metadata onto your images.

1. **Open Terminal or Command Prompt**: Navigate to the folder where you saved `generate-metadata-from-csv.py`.
2. **Run the Script**: Type `python generate-metadata-from-csv.py` and press Enter.

## Conclusion

Enhancing your images with accurate and rich metadata not only makes your work more searchable but also more professional. By following the steps outlined in this guide, you can leverage PhotoTag.ai’s powerful AI to automate the enhancement of your image metadata, saving you time and effort. Whether you’re cataloging a vast digital library or just starting with digital photography, this tool is designed to streamline your workflow and elevate your digital presence.
