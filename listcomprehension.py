# sample data
params = {
    "filter_type": 'awa'
}
master = [
    {
        "_id": "a",
        "pms_details": [
            {
                "customer_id": "a",
                "data": {
                    "type": "awa"
                }

            }]
    },
    {
        "_id": "aa",
        "pms_details": [
            {
                "customer_id": "aa",
                "data": {
                    "type": "was"
                }

            }]
    },
    {
        "_id": "sw",
        "pms_details": [
            {
                "customer_id": "sw",
                "data": {
                    "type": "awa"
                }

            }]
    }
]
# sample data

result = []
for customer in master:
    for item in customer["pms_details"]:
        if item["customer_id"] == customer["_id"]:
            if item["data"]["type"] == params["filter_type"]:
                result.append(customer)

print(result)

# nested for in list comprehension with a condition
a = [
    customer
    for customer in master for item in customer["pms_details"] if
    item["customer_id"] == customer["_id"] and item["data"]["type"] == params["filter_type"]
]

print(a)

a = [10, 20, None, 12]
newA = list(filter(lambda y: y < 20, filter(lambda x: x > 10 if x else False, a)))
