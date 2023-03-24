```{include} ../README.md
:start-line: 0
:end-line: 3
```

`lnschema-wetlab` is an extendable schema to track data generation in wet labs.

Data objects (`File`) get directly linked to

- `Experiment`: An experiment performed to generate data.
- `Biosample`: The biological samples from which data are generated.
- `Readout`: The measurements types applied to the biosamples.

The order of this tuple is inspired by the workflow:

- Plan an `Experiment` based on an `ExperimentType`:
  - `ExperimentType`: metadata that describes experiments to perform
- Prepare a `Biosample` containing all metadata including `Tissue`, `Species`, `Donor`, `Treatment`, `Time`, `Mutation`, etc.
  - `Techsample` A biosample extension for specific experiments that require pooling or splitting biosamples.
- Choose one or several `Readout`.

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
