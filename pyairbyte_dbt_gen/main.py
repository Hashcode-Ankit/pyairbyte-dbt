from  dbt_generator import DBTAirbyte
import os

def main():
    workspace = os.curdir
    dbt_airbyte = DBTAirbyte("demo_project",workspace,"demo_profile")
    dbt_airbyte.setup_db_profile("clickhouse","username","password","host",443)

if __name__ == "__main__":
    main()
