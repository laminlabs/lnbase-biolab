```{include} ../README.md
:start-line: 0
:end-line: 3
```

`lnschema-wetlab` is a highly flexible and extendable wetlab schema to track data generation in wet labs.

Any data (`dobject`) generated in an experiment should be **simply queryable** and, hence, **directly** linked to the following entities present in `biometa`:

- `experiment`: an experiement performed to produce the data of interest
- `biosample`: biological samples that the data is generated from
  - `techsample` may be used to extend the biosample in specific experiments that requires pooling or spliting of biosamples
- `readout`: types of measurements collected in the data
- `featureset`: sets of features that data contains

These entities allow mapping arbitrarily complex experimental designs (like many other schema choices would).

The order of this tuple is inspired by the workflow:

- Plan an `experiment` based on an `experiment_design`:
  - `experiment_design`: metadata that describes experiments to perform
- Prepare a `biosample` containing all metadata including `tissue`, `species`, `patient`, `perturbagen`, `time`, `dose`, `mutation`, etc.
- Choose one or several `readout`
- Determine a set of features that will be measured

Install:

```
pip install lnschema-wetlab
```

Get started:

- [Tutorials](https://lamin.ai/docs/db/tutorials/index) walk you through setup and usage of the LaminDB with this schema.
- Browse the [API reference](api) to check out schema tables.
- [Reach out](https://lamin.ai/contact) to learn about modules that connect your assays, pipelines, instruments & workflows within our data platform enterprise offer.

```{toctree}
:maxdepth: 1

api
guides/index
changelog
```
