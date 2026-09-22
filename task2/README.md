# Task 2 — Wikipedia Category Aggregation

## Task

Collect all entries from the Russian Wikipedia category "Животные по алфавиту" and save the number of entries for each Russian letter to `beasts.csv`.

Each category entry is counted as-is without additional text analysis.

## Approach

The solution uses the official MediaWiki API to retrieve category entries.

Category entries are retrieved through the `categorymembers` API endpoint with pagination handled using the `cmcontinue` token.

The processing is split into three steps:

1. fetch category titles from Wikipedia;
2. count titles by their first Russian letter;
3. write the aggregated counts to a CSV file.

Only article entries from the main namespace are requested, and the output preserves the full Russian alphabet order.

## Output

The generated `beasts.csv` file has the following format:

```csv
А,1348
Б,1836
В,563
...
Я,230
```

The exact counts may change over time as Wikipedia content is updated.

## Testing

The test suite covers:

* API pagination;
* title aggregation by initial letter;
* uppercase and lowercase Russian letters;
* the `Ё` character;
* unsupported initial characters;
* CSV output;
* HTTP error propagation.
