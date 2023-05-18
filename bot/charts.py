import quickchart
from quickchart import QuickChart

qc = QuickChart()
qc.width = 500
qc.height = 300
qc.device_pixel_ratio = 2.0
qc.config = {
    "type": "bar",
    "data": {
        "labels": ["Hello world", "Test"],
        "datasets": [{
            "label": "Foo",
            "data": [1, 2]
        }]
    }
}

# Print a chart URL
print(qc.get_url())

# Print a short chart URL
print(qc.get_short_url())