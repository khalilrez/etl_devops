from data.api import get_api_data
from data.transformations import get_transformed_data
from data.loading import load_into_database
from config.config import Config

api_url = Config.API_URL

api_records = get_api_data(api_url)
df = get_transformed_data(api_records)
load_into_database(df)
