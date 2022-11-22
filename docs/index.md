```{include} ../README.md
:start-line: 0
:end-line: 3
```

`lnschema-wetlab` is an extendable wetlab schema to track data generation in wet labs.

Concepts:

Data objects (`dobject`) get directly linked to

- `experiment`: An experiment performed to generate data.
- `biosample`: The biological samples from which data are generated.
- `readout`: The measurements types applied to the biosamples.

The order of this tuple is inspired by the workflow:

- Plan an `experiment` based on an `experiment_design`:
  - `experiment_design`: metadata that describes experiments to perform
- Prepare a `biosample` containing all metadata including `tissue`, `species`, `patient`, `perturbagen`, `time`, `dose`, `mutation`, etc.
  - `techsample` A biosample extension for specific experiments that require pooling or splitting biosamples.
- Choose one or several `readout`.

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
