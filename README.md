# E-commerce ELT Pipeline Project
This project is a real-world ELT project based. But instead
of using data from sources like databases,... This project will use 
the kaggle E-commerce dataset.  
The technologies, tools, concepts that this project will use:
- Data Lake: Amazon S3
- Data Warehouse: Snowflake
- Medallion Architecture
- Automate Pipeline: Apache Airflow
- Database Schema: Star Schema
- Data Build Tool: dbt
- BI tools: Streamlit
# How the project work
1. Download the dataset from kaggle using kagglehub.
2. Upload the data automatically to data lake (Amazon S3)
3. Transfer data from Data Lake to Data Warehouse (Bronze Layer)
4. Design Schema
5. Use dbt for transformations at Silver and Gold layer
6. Load datas into BI tools
# How to run  the project
1. Set up python, env
```shell
python -m venv .venv
source .venv/bin/activate # On Windows: .venv/Scripts/activate
pip install -r requirements.txt
cp .env.exmaple .env
```