from  dbt_generator import DBTAirbyte

def main():
    workspace = "/Users/apple/Desktop/Airbyte OS/pyairbyte-dbt/pyairbyte_dbt_gen/.dbt_workspace"
    dbt_airbyte = DBTAirbyte("demo_project",workspace,"demo_profile")
    dbt_airbyte.setup_db_profile("clickhouse","username","password","host",443)

if __name__ == "__main__":
    main()
