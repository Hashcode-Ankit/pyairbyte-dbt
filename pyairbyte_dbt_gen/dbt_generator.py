import os
import shutil
from dbt.include.starter_project import PACKAGE_PATH as starter_project_directory
from utils import create_file_path, create_clickhouse_profile
from typing import Optional
class DBTAirbyte:
    def __init__(self,project_name:str,workspace_folder: str,profile: str ) -> None:
        self.project_name = project_name
        self.workspace_folder = workspace_folder or os.curdir
        self.segragate_dir_name = "main"
        self.profile =  profile or "default"

        # create sample dbt project in the workspace directory 
        dbt_project_path  = create_file_path(workspace_folder,self.project_name,self.segragate_dir_name)
        shutil.copytree(starter_project_directory, dbt_project_path, dirs_exist_ok=True)
        # rewrite dbt project yml
        dbt_project_yml_path = create_file_path(dbt_project_path,"dbt_project.yml")
        with open(dbt_project_yml_path, "r+") as project_file:
            project_yaml = project_file.read()
            project_yaml = project_yaml.replace("{project_name}",self.project_name)
            project_file.seek(0)
            project_file.truncate(0)
            project_file.write(project_yaml)


    def setup_db_profile(self,type:str, username: str, password:str, host: str, port: int, secure: bool = False, driver: str = "http")-> Optional[str]:
        """
        setup dbt database profile
        currently we support only clickhouse
        """
        profile = None

        if type =="clickhouse":
            profile =  create_clickhouse_profile(self.project_name,self.profile,username,password,host,port,driver,secure)
        
        if not profile: 
            return f"we dont support the database {type}"
        
        profile_dir_path = create_file_path(self.workspace_folder,self.project_name,"profiles.yml")
        with open(profile_dir_path, "w") as profile_file:
            profile_file.writelines(profile)
        
    def create_schema(self, model_name:str) :
        """
        creates schema file for the given airbyte data
        """
        # Todo: creats the schema.yml for the given data
