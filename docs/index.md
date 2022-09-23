```{include} ../README.md
:start-line: 0
:end-line: 3
```

`lnschema-wetlab` is an extendable wetlab schema to track data generation in wet labs.

Concepts:

Datasets generated in an experiment (`dobject`) are linked to `biometa`, which stores all information about experimental and scientific entities.

- `experiment`: An experiement performed to generate data.
- `biosample`: The biological samples from which data are generated.
- `readout`: The measurements types applied to the biosamples.
- `featureset`: The sets of features that are contained in the data.

These entities allow mapping arbitrarily complex experimental designs.
While other schema designs are possible, this design enables simple queries by directly linking `biometa` against the 4-tuple.

The order of this tuple is inspired by the workflow:

- Plan an `experiment` based on an `experiment_design`:
  - `experiment_design`: metadata that describes experiments to perform
- Prepare a `biosample` containing all metadata including `tissue`, `species`, `patient`, `perturbagen`, `time`, `dose`, `mutation`, etc.
  - `techsample` A biosample extension for specific experiments that require pooling or splitting biosamples.
- Choose one or several `readout`.
- Determine a set of features that will be measured.

Install:

```
pip install lnschema-wetlab
```

Get started:

- The LaminDB [guide](https://lamin.ai/docs/db/guide) explains usage of this schema.
- Browse the [API reference](api) to learn about the tables within this schema.

```{toctree}
:maxdepth: 1
:hidden:

api
guide/index
changelog
```
