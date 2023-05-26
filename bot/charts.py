import quickchart
from quickchart import QuickChart

def chart(ctx, data):
    for key in data:
        activities = data[key]
        activity_names = []
        activity_times = []
        for i in activities:
            activity_names.append(i.name)
            activity_times.append(i.time)
        qc = QuickChart()
        qc.config = {
            "type": "line",
            "data": {
                "type": "bar",
                "labels": activity_names,
                "datasets": [{
                    "label": "screentime",
                    "data": activity_times

                }]
            }
        }

        # Print a chart URL
        print(key + ": " + qc.get_url())

        # Print a short chart URL
        print(key + ": " + qc.get_short_url())


'''qc.config = {
    "type": "line",
    "data": {
        "type": "bar",
        "labels": ["Hello world", "Test",'a' 'b','c'],
        "datasets": [{
            "label": "Foo",
            "data": [1, 2]

        }]
    }
}

# Print a chart URL
print(qc.get_url())

# Print a short chart URL
print(qc.get_short_url())'''
