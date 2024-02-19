import pandas as pd
import piexif
import os

# Replace 'your_metadata.csv' with the path to your CSV file from PhotoTag.ai
csv_file_path = 'your_metadata.csv'
# Replace 'your_images_directory/' with the path to the directory containing your images
image_directory = 'your_images_directory/'

def read_csv(csv_path):
    """Read the CSV file and return a pandas DataFrame."""
    return pd.read_csv(csv_path)

def write_metadata_to_image(image_path, title, description, keywords):
    """Write metadata into an image's EXIF data."""
    try:
        # Load the image's EXIF data if it exists, or create a new EXIF dict
        exif_dict = piexif.load(image_path) if os.path.exists(image_path) else {'0th': {}, 'Exif': {}, 'GPS': {}, '1st': {}, 'thumbnail': None}
        
        # Encode the metadata to be compatible with EXIF
        exif_dict['0th'][piexif.ImageIFD.ImageDescription] = description.encode('utf-8')
        exif_dict['0th'][piexif.ImageIFD.XPTitle] = title.encode('utf-16le')
        exif_dict['0th'][piexif.ImageIFD.XPKeywords] = keywords.encode('utf-16le')
        
        # Dump the EXIF data back into a bytes object
        exif_bytes = piexif.dump(exif_dict)
        
        # Insert the EXIF bytes back into the image
        piexif.insert(exif_bytes, image_path)
        print(f"Metadata written to {image_path}")
    except Exception as e:
        print(f"Error writing metadata to {image_path}: {e}")

def process_images(dataframe, directory):
    """Process each image according to the metadata in the dataframe."""
    for index, row in dataframe.iterrows():
        image_path = os.path.join(directory, row['file'])
        if os.path.exists(image_path):
            # Convert keywords list to a comma-separated string
            keywords = ', '.join(row['keywords'].split(';'))
            write_metadata_to_image(image_path, row['title'], row['description'], keywords)
        else:
            print(f"File not found: {image_path}")

if __name__ == "__main__":
    metadata_df = read_csv(csv_file_path)
    process_images(metadata_df, image_directory)
