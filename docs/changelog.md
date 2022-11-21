# Changelog

<!-- prettier-ignore -->
Name | PR | Developer | Date | Version
--- | --- | --- | --- | ---
✨ Add relationships to `Biosample` | [36](https://github.com/laminlabs/lnschema-wetlab/pull/36) | [falexwolf](https://github.com/falexwolf) | 2022-11-21 | 0.9.1
🏗️ Introduce relationships | [35](https://github.com/laminlabs/lnschema-wetlab/pull/35) | [falexwolf](https://github.com/falexwolf) | 2022-11-17 | 0.9.0
🐛 Fix table name | [34](https://github.com/laminlabs/lnschema-wetlab/pull/34) | [falexwolf](https://github.com/falexwolf) | 2022-11-03 | 0.8.2
🐛 Fix treatment ref | [33](https://github.com/laminlabs/lnschema-wetlab/pull/33) | [falexwolf](https://github.com/falexwolf) | 2022-11-03 | 0.8.1
🎨 Modularize and capitalize | [32](https://github.com/laminlabs/lnschema-wetlab/pull/32) | [falexwolf](https://github.com/falexwolf) | 2022-11-03 | 0.8.0
✨ Added `project_experiment` table | [31](https://github.com/laminlabs/lnschema-wetlab/pull/31) | [sunnyosun](https://github.com/sunnyosun) | 2022-10-20 | 0.7.2
🚚 Moved the `project` table to core schema | [30](https://github.com/laminlabs/lnschema-wetlab/pull/30) | [sunnyosun](https://github.com/sunnyosun) | 2022-10-19 | 0.7.1
🔥 Removed `cell_marker_id` from `biosample` | [29](https://github.com/laminlabs/lnschema-wetlab/pull/29) | [sunnyosun](https://github.com/sunnyosun) | 2022-10-17 | 0.7.0
🚚 Added created_by to project table | [28](https://github.com/laminlabs/lnschema-wetlab/pull/28) | [falexwolf](https://github.com/falexwolf) | 2022-10-14 | 0.6.0
⬆️ Upgrade to lnschema_core 0.9.0 | [27](https://github.com/laminlabs/lnschema-wetlab/pull/27) | [falexwolf](https://github.com/falexwolf) | 2022-09-30 | 0.5.0
✏️ Changed ids to str | [26](https://github.com/laminlabs/lnschema-wetlab/pull/26) | [sunnyosun](https://github.com/sunnyosun) | 2022-09-29 | 0.4.3
🍱 Added treatment, removed techsample_id in biosample | [25](https://github.com/laminlabs/lnschema-wetlab/pull/25) | [sunnyosun](https://github.com/sunnyosun) | 2022-09-28 | 0.4.2
🎨 Added biosample_techsample, changed imports to default | [24](https://github.com/laminlabs/lnschema-wetlab/pull/24) | [sunnyosun](https://github.com/sunnyosun) | 2022-09-28 | 0.4.1
🎨 Fix type annotations and link table | [23](https://github.com/laminlabs/lnschema-wetlab/pull/23) | [falexwolf](https://github.com/falexwolf) | 2022-09-26 | 0.4.0
🐛 Fix type annotation of timestamps | [22](https://github.com/laminlabs/lnschema-wetlab/pull/22) | [falexwolf](https://github.com/falexwolf) | 2022-09-24 |
🎨 Update all primary keys to base62 and overhaul bio & techsample tables | [21](https://github.com/laminlabs/lnschema-wetlab/pull/21) | [falexwolf](https://github.com/falexwolf) | 2022-09-23 |
🍱 Add migrations infra | [20](https://github.com/laminlabs/lnschema-wetlab/pull/20) | [falexwolf](https://github.com/falexwolf) | 2022-09-23 |
✨ Added filepath to techsample | [19](https://github.com/laminlabs/lnschema-wetlab/pull/19) | [sunnyosun](https://github.com/sunnyosun) | 2022-09-13 | 0.3.7
🎨 Added `external_id` | [17](https://github.com/laminlabs/lnschema-wetlab/pull/17) | [sunnyosun](https://github.com/sunnyosun) | 2022-09-06 | 0.3.6
🐛 fixed the foreign key types | [16](https://github.com/laminlabs/lnschema-wetlab/pull/16) | [sunnyosun](https://github.com/sunnyosun) | 2022-09-01 | 0.3.5
🚚 Rename `project` to `project_id` in the experiment table | [15](https://github.com/laminlabs/lnschema-wetlab/pull/15) | [sunnyosun](https://github.com/sunnyosun) | 2022-08-30 | 0.3.4
🎨 Restrict `efo_id` to be unique | [14](https://github.com/laminlabs/lnschema-wetlab/pull/14) | [sunnyosun](https://github.com/sunnyosun) | 2022-08-30 | 0.3.3
🎨 Updated biosample table to include more columns | [13](https://github.com/laminlabs/lnschema-wetlab/pull/13) | [sunnyosun](https://github.com/sunnyosun) | 2022-08-28 | 0.3.2
🚚 Rename `readout_type` to `readout`, add descriptions | [12](https://github.com/laminlabs/lnschema-wetlab/pull/12) | [sunnyosun](https://github.com/sunnyosun) | 2022-08-26 | 0.3.1
🏗️ Make table load configurable | [11](https://github.com/laminlabs/lnschema-wetlab/pull/11) | [falexwolf](https://github.com/falexwolf) | 2022-08-25 | 0.3.0
🎨 Default bio and tech samples | [10](https://github.com/laminlabs/lnschema-wetlab/pull/10) | [sunnyosun](https://github.com/sunnyosun) | 2022-08-25 |
🐛 Imported additional tables | [9](https://github.com/laminlabs/lnschema-wetlab/pull/9) | [sunnyosun](https://github.com/sunnyosun) | 2022-08-24 | 0.2.4
✨ Added `techsample` table | [8](https://github.com/laminlabs/lnschema-wetlab/pull/8) | [sunnyosun](https://github.com/sunnyosun) | 2022-08-24 | 0.2.3
✏️ Fixed id type to int | [7](https://github.com/laminlabs/lnschema-wetlab/pull/7) | [sunnyosun](https://github.com/sunnyosun) | 2022-08-23 | 0.2.2
✨ Added `experiment` and `experiment_type` tables. | [6](https://github.com/laminlabs/lnschema-wetlab/pull/6) | [sunnyosun](https://github.com/sunnyosun) | 2022-08-23 | 0.2.1
🚚 Rename `lndb-schema-wetlab` to `lnschema-wetlab` | [5](https://github.com/laminlabs/lnschema-wetlab/pull/5) | [falexwolf](https://github.com/falexwolf) | 2022-08-19 | 0.2.0
🔧 Add schema module id | [4](https://github.com/laminlabs/lnschema-wetlab/pull/4) | [falexwolf](https://github.com/falexwolf) | 2022-08-18 |
🎨 Updated readout to use EFO | [3](https://github.com/laminlabs/lnschema-wetlab/pull/3) | [sunnyosun](https://github.com/sunnyosun) | 2022-08-10 | 0.1.2
🐛 Add correct wetlab schema | [2](https://github.com/laminlabs/lnschema-wetlab/pull/2) | [falexwolf](https://github.com/falexwolf) | 2022-07-31 |
🚚 Add code from `lnschema-biology` | [1](https://github.com/laminlabs/lnschema-wetlab/pull/1) | [falexwolf](https://github.com/falexwolf) | 2022-07-31 | 0.1.0
