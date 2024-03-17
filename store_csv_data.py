import csv
import pymongo
from datetime import datetime


# Function to store game data in MongoDB
def store_game_data(data):
    client = pymongo.MongoClient('mongodb+srv://w2b_admin:w2b_admin@w2bsg.dnmytqb.mongodb.net/?retryWrites=true&w=majority&appName=W2BSG')
    db = client['w2bsg_db']
    collection = db['games']

    with open(data, 'r') as file:
        # Define the fieldnames including the renamed column
        fieldnames = ['DateTime', 'price']

        reader = csv.DictReader(file, fieldnames=fieldnames)
        # Skip the header row
        next(reader)
        for row in reader:
            # Split date and time into separate fields
            date_time_str = row.pop('DateTime')
            date_time = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
            row['date'] = date_time.date().strftime('%Y-%m-%d')
            row['time'] = date_time.time().strftime('%H:%M:%S')

            # Add game name to the data
            row['game_name'] = game_name

            # Store the parsed data
            collection.insert_one(row)

# Parse CSV file and extract data
csv_file_path = '/Users/mavricklee/Desktop/CSCI42/W2BSG/assets/pricetrend_csv/rust_pricetrend.csv'  # Path to your CSV file

# Specify the game name
game_name = "Rust"

# Store data in MongoDB
store_game_data(csv_file_path)
print("Data stored successfully.")