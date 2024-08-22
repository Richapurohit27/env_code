import os
import yaml
from PIL import Image

def generate_thumbnail(source_file, thumbnail_size, destination_dir):
    image = Image.open(source_file)
    image.thumbnail(thumbnail_size)
    filename = os.path.splitext(os.path.basename(source_file))[0]
    thumbnail_filename = f"{filename}_thumbnail.png"
    thumbnail_path = os.path.join(destination_dir, thumbnail_filename)
    image.save(thumbnail_path, "PNG")
    print(f"Thumbnail generated: {thumbnail_path}")

def main():
    try:
        # Load configuration from YAML file
        with open(r"C:\\Users\\tl323\\de_practice\\config.yaml", "r") as config_file:
            config = yaml.safe_load(config_file)

        source_dir = config.get("source_directory", "")
        destination_dir = config.get("destination_directory", "")
        small_thumbnail_size = config.get("small_thumbnail_dimension", (80, 80))
        medium_thumbnail_size = config.get("medium_thumbnail_dimension", (300, 300))
        large_thumbnail_size = config.get("large_thumbnail_dimension", (500, 500))

        # Iterate over source directory and generate thumbnails
        for filename in os.listdir(source_dir):
            source_file = os.path.join(source_dir, filename)
            if os.path.isfile(source_file):
                generate_thumbnail(source_file, small_thumbnail_size, destination_dir)
                generate_thumbnail(source_file, medium_thumbnail_size, destination_dir)
                generate_thumbnail(source_file, large_thumbnail_size, destination_dir)

    except FileNotFoundError:
        print("Configuration file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
