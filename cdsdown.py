import cdsapi

dataset = "seasonal-original-single-levels"
request = {
    "originating_centre": "ecmwf",
    "system": "51",
    "variable": ["total_precipitation"],
    "year": ["2024"],
    "month": ["12"],
    "day": ["01"],
    "leadtime_hour": [
        "408",
        "432",
        "456",
        "480",
        "504",
        "528",
        "552",
        "576",
        "600"
        "624",
        "648",
        "672",
        "696",
        "720",
    ],
    "data_format": "netcdf",
    "area": [40, 70, 5, 100]
}

client = cdsapi.Client()
client.retrieve(dataset, request).download()

