# streamplate-technical-task
Using the venue dataset provided, write up a Python API that returns a list of categories and the venues under those categories that are closest to the coordinates provided. It should follow the requirements:
Accepts arguments:
- latitude (required)
- longitude (required)
- limit (optional): Limits the closest X venues that will be used to generate the categories and
sort them under. If no limit is provided, the closest 10 venues will be used and sorted.

Restrictions:
- The list of categories should be sorted in descending order of how many venues each category has, then in alphabetical order.
- The list of venues for each category should be sorted in ascending order of venue's distance from the provided coordinates.
- The API should include error checking for its arguments and return suitable responses.
- The API should run in under 0.7 seconds.
