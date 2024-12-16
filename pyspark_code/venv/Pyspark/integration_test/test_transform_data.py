import pytest
from pyspark.sql import SparkSession
from glue_script import transform_data  # Replace with your actual module name

# @pytest.fixture(scope="module") -- This means the fixture will run once for the entire module (the file containing the test functions), 
# not per test. It's useful when you want to perform some expensive setup 
# (like initializing a database connection) that doesn’t need to be done for every individual test, 
# but only once for all the tests in the module.

def spark():
    """Fixture to provide a SparkSession."""
    return SparkSession.builder.master("local").appName("pytest").getOrCreate()

def test_transform_data(spark):
    # Input DataFrame
    input_data = [(1, "Alice"), (2, "Bob")]
    input_df = spark.createDataFrame(input_data, ["existing_column", "name"])

    # Expected Output DataFrame
    expected_data = [(2, "Alice"), (4, "Bob")]
    expected_df = spark.createDataFrame(expected_data, ["new_column", "name"])

    # Assert DataFrame equality
    assert transform_data(input_df).collect() == expected_df.collect()
