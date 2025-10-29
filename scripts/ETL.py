# %%
from load import load_data_into_db
from transformation import transform_data, load_data
from Db_connection import connect_to_db, close_connection

# Main ETL function that orchestrates loading, transforming, and loading data into the database
def main():
		df0 = load_data(1)
		df = transform_data(df0)
		# load_data returns None (it performs inserts); print confirmation from load_data
		load_data_into_db(df)
		


if __name__ == "__main__":
	main()



