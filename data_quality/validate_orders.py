import great_expectations as ge

def validate_orders():

    df = ge.read_parquet("orders_transformed.parquet")

    df.expect_column_values_to_not_be_null("order_id")

    df.expect_column_values_to_be_between("amount", min_value=1)

    result = df.validate()

    print(result)