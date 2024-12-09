import panda as pd

def result(data):
    product_ids = set(item["product_id"] for item in data)
    result = {}

    for id in product_ids:
        #total_price = 0
        # total_sales = 0
        total_price = sum(item["usd_price"] for item in data if id == item ["product_id"])
        total_sales = sum(1 for item in data if id == item ["product_id"])

        # for item in data:
        #     if id == item ["product_id"]:
        #         total_price += item["usd_price"]
        #         total_sales += 1
        
        result[id] = {
                "total_sales":total_sales, 
                "total_price":total_price, 
                "avg_sale": total_price/total_sales
            }
    
    return result

data = [
    {"sale_id": 1, "product_id": 111, "store_id": 123, "usd_price": 5},   
    {"sale_id": 2, "product_id": 222, "store_id": 124, "usd_price": 15},
    {"sale_id": 3, "product_id": 222, "store_id": 125, "usd_price": 20},
    {"sale_id": 10, "product_id": 111, "store_id": 123, "usd_price": 10},
    {"sale_id": 31, "product_id": 222, "store_id": 125, "usd_price": 25},
    {"sale_id": 11, "product_id": 333, "store_id": 130, "usd_price": 30}
]

output = result(data)
print(output)

#{333: {'total_sales': 1, 'total_price': 30, 'avg_sale': 30.0}, 222: {'total_sales': 3, 'total_price': 60, 'avg_sale': 20.0}, 111: {'total_sales': 2, 'total_price': 15, 'avg_sale': 7.5}}


df = pd.DataFrame(data)

# Group by product_id and calculate both sum and average
final_result = df.groupby('product_id')['usd_price'].agg(['sum', 'mean']).reset_index().rename(columns={'sum': 'total_sales', 'mean': 'average_sales'})
print(final_result)