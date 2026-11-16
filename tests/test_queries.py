import argparse
from pathlib import Path

from rdflib import Graph

def format_row(values):
    return "| " + " | ".join(
        value.ljust(width) for value, width in zip(values, widths)
    ) + " |"

# Defining terminal arguments
parser = argparse.ArgumentParser(
    description="Run SPARQL SELECTs"
)
parser.add_argument("data", type=Path)
parser.add_argument("query", type=Path)
args = parser.parse_args()

# Executing the query
graph = Graph().parse(args.data, format="turtle")
query = args.query.read_text(encoding="utf-8")
result = graph.query(query)

if result.type != "SELECT":
    parser.error("Only SELECT queries are permited.")


# Formatting the returned columns and preserving missing values
if result.vars:
    headers = [str(variable) for variable in result.vars]
else:
    parser.error("Query without return values")

rows = []
for row in result:
    rows.append([
        value.n3(namespace_manager=graph.namespace_manager)
        if value is not None else "—"
        for value in row
    ])

widths = [
    max([len(header)] + [len(row[index]) for row in rows])
    for index, header in enumerate(headers)
]
separator = "+-" + "-+-".join("-" * width for width in widths) + "-+"


# Printing the final result
print(separator)
print(format_row(headers))
print(separator)
for row in rows:
    print(format_row(row))
print(separator)

print(f"\nTotal rows: {len(rows)}")
