import airbyte 

supported_databases = ["clickhouse","duckdb"]
def get_data()->airbyte.ReadResult :
    """
    function returns the data from the source provided config
    """
    source: airbyte.Source = airbyte.get_source("source-faker")
    source.select_all_streams()
    source.set_config(
        config={
            "count": 50_000,  # Adjust this to get a larger or smaller dataset
            "seed": 123,
        },
    )
    try: 
     source.check() 
    except airbyte.exceptions.AirbyteConnectorCheckFailedError as e:
        print(e)
        return None
     
    return source.read()
    