import csv
import xml.etree.ElementTree as ET

def xml_to_csv(xml_file, csv_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Open CSV file in write mode with newline='' to prevent extra newlines in the output
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write header row
        writer.writerow(['id', 'author', 'title', 'genre', 'price', 'publish_date', 'description'])

        # Iterate over each book element in the XML
        for book in root.findall('book'):
            # Extract data from each book element
            book_data = [
                book.get('id'),
                book.find('author').text,
                book.find('title').text,
                book.find('genre').text,
                book.find('price').text,
                book.find('publish_date').text,
                book.find('description').text
            ]
            # Write data to CSV file
            writer.writerow(book_data)

if __name__ == "__main__":
    xml_file = "C:\\Users\\tl323\\de_practice\\book.xml"
    csv_file = "books.csv"
    xml_to_csv(xml_file, csv_file)
    print(f"CSV file '{csv_file}' has been generated successfully.")
