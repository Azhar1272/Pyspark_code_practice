import pytest
from pyspark.sql import SparkSession
from glue_script import transform_data  # Replace with your actual module name

@pytest.fixture(scope="module")
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

    # Apply transformation
    result_df = transform_data(input_df)

    # Assert DataFrame equality
    assert result_df.collect() == expected_df.collect()
